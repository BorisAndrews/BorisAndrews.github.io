from firedrake        import assemble, constant, functionspace
from ufl              import split_functions
from finat            import ufl
import avfet_modules.cheb_plus as cheb_plus
import itertools
import numpy



'''
[Loosely: Scripts for defining function spaces]
'''



def FETFunctionSpace(mesh, family, degree=None, order=0, name=None, vfamily=None, vdegree=None):
    """
    Create a simple space–time function space with Chebyshev-in-time structure.

    This returns a Firedrake MixedFunctionSpace consisting of order+1 copies of
    the provided spatial space. The copies represent the coefficients of a
    Chebyshev polynomial expansion in time on the reference interval [-1, 1].

    The returned MixedFunctionSpace is augmented with an `order` attribute (a
    one-element list `[order]`) so that downstream helpers can recover the time
    polynomial degree associated with this block.

    Parameters
    - mesh: Firedrake mesh
    - family: Firedrake element family (e.g. "Q", "CG"), or a ufl.Element
    - degree: spatial polynomial degree
    - order: time polynomial order (space has order+1 blocks)
    - name: optional base name for per-coefficient subspaces
    - vfamily, vdegree: vector element family/degree if `family` is a vector type

    Returns
    - MixedFunctionSpace with order+1 copies of the spatial space and an
      `order` attribute describing its time degree.
    """

    # Create mixed function space
    if name:
        new = functionspace.MixedFunctionSpace([
            functionspace.FunctionSpace(mesh, family, degree=degree, name=name+"_"+str(i), vfamily=vfamily, vdegree=vdegree)
            for i in range(order+1)
        ])
    else:
        new = functionspace.MixedFunctionSpace([
            functionspace.FunctionSpace(mesh, family, degree=degree, name=None, vfamily=vfamily, vdegree=vdegree)
            for i in range(order+1)
        ])

    # Store order
    new.order = [order]

    return new



def FETVectorFunctionSpace(mesh, family, degree=None, order=0, dim=None, name=None, vfamily=None, vdegree=None, variant=None):
    '''
    Vector variant of FETFunctionSpace that preserves the time order metadata.

    Creates a vector finite element from the scalar element definition and wraps
    it via `FETFunctionSpace` so the resulting MixedFunctionSpace carries the
    Chebyshev time expansion structure.
    '''
    sub_element = functionspace.make_scalar_element(mesh, family, degree, vfamily, vdegree, variant)
    if dim is None:
        dim = mesh.geometric_dimension()
    element = ufl.VectorElement(sub_element, dim=dim)

    return FETFunctionSpace(mesh, element, order=order, name=name)



def FETMixedFunctionSpace(spaces, name=None, mesh=None):
    '''
    Construct a mixed space–time function space from multiple FET blocks.

    This mirrors `functionspace.MixedFunctionSpace(spaces, ...)` but also
    aggregates the time orders from each component space into a single
    `order` list on the mixed space. This maintains the mapping between
    subspaces and their Chebyshev-in-time expansion degrees.
    '''

    # Create mixed function space
    new = functionspace.MixedFunctionSpace(spaces, name=None, mesh=None)

    # Sore orders
    new.order = []
    for space in spaces:
        new.order += space.order

    return new



'''
[Loosely: Scripts for splitting functions]
'''



def FETsplit(v):
    '''
    Split a MixedFunction into per-field Chebyshev coefficient tuples.

    Given a function defined on an FETMixedFunctionSpace, this groups the raw
    Firedrake subfunctions into tuples per physical field, where each tuple
    contains the `order+1` Chebyshev coefficients in time for that field.

    Returns a tuple of tuples with the same arity as the original list of
    spaces used to build the mixed space.
    '''

    # Split
    sub_functions_long = split_functions.split(v)

    # Regroup the different orders for functions of the same function space
    sub_functions_short = []
    order_sum = 0
    for order_ in v.function_space().order:
        sub_functions_short.append(tuple(sub_functions_long[order_sum:(order_sum+order_+1)]))
        order_sum += order_+1

    return tuple(sub_functions_short)



'''
[Loosely: Scripts for defining new functions]
'''



def integrate(u_t, u_IC, timestep):
    '''
    Integrate a Chebyshev-in-time representation of a time derivative.

    Given the Chebyshev coefficient tuple `u_t` for du/dt over [-1, 1] and a
    spatial Function `u_IC` representing the value at the beginning of the
    (physical) timestep, construct the Chebyshev coefficient tuple for `u`.

    The mapping uses exact relations between Chebyshev modes for the integral
    on the reference interval, scaled by `timestep`.
    '''

    # Normalise input
    timestep = float(timestep)

    # Create output, elementwise on input
    u = [u_IC]
    for i, u_t_ in enumerate(u_t):
        if i == 0:
            u[0]   = u[0]   + constant.Constant(timestep/2) * u_t_
            u     +=         [constant.Constant(timestep/2) * u_t_]
        elif i == 1:
            u[0]   = u[0]   - constant.Constant(timestep/2 * 1/4) * u_t_
            u     +=         [constant.Constant(timestep/2 * 1/4) * u_t_]
        else:
            u[0]   = u[0]   - constant.Constant(timestep/2 * (-1)**i * 1/(i**2-1)) * u_t_
            u[i-1] = u[i-1] - constant.Constant(timestep/2 * 1/2/(i-1)) * u_t_
            u     +=         [constant.Constant(timestep/2 * 1/2/(i+1)) * u_t_]

    return tuple(u)



def project(u, tol = 1e-15):
    '''
    L2 project a Chebyshev expansion to one lower time order.

    Takes a coefficient tuple `u` of length `order+1` and returns a new tuple
    where the contribution of the highest Chebyshev mode has been projected
    into the lower-order space using precomputed projection coefficients.
    Small coefficients (below `tol`) are dropped to avoid spurious fill-in.
    '''
    # Evaluate order of u
    order = len(u)-1

    # Evaluate projection of highest order polnoymial
    coeff = cheb_plus.chebprojvec(order-1, order)
    
    # Create output, element-wise on output
    out = []
    for (u_, coeff_) in zip(u, coeff):
        if abs(coeff_) >= tol:
            out += [u_ + constant.Constant(coeff_)*u[order]]
        else:
            out += [u_]

    return tuple(out)



'''
[Loosely: Scripts for defining residuals]
'''



def residual(F, res, input, poly=True, leg_pts=None, tol=1e-15):
    '''
    Assemble a space–time residual term over the previous time slab.

    This helper lifts a time-continuous residual kernel `res(*inputs, v)` to a
    Chebyshev-in-time finite element representation. Inputs are tuples of
    Chebyshev coefficients per field for the time slab and the final element of
    `input` must be the test-function coefficient tuple `v` for that field.

    Two evaluation paths are supported:
    - poly=True: exact mode-coupling via Chebyshev algebra and L2 projection
                 into P^order.
    - poly=False: Gauss–Legendre quadrature in time using a dual basis map.

    Parameters
    - F: existing UFL residual to add into
    - res: callable that builds a spatial UFL form given concrete inputs
    - input: tuple of coefficient tuples (..., v)
    - poly: choose exact polynomial path or quadrature path
    - leg_pts: optional number of GL points for quadrature path
    - tol: drop tolerance for tiny mode couplings

    Returns
    - Updated UFL residual form with the new contribution added.
    '''

    # Retrieve functions and order in time
    u_tup = input[0:len(input)-1]
    v     = input[-1]
    order = len(v)-1

    if poly:
        # Create a list to store enumeration objects for each u
        u_enum = [enumerate(u) for u in u_tup]

        # Generate all possible combinations of inputs
        for u_enum_comb in itertools.product(*u_enum):
            # 1. Create array of Chebyshev basis vectors for each given order...
            basis_vec_arr = [cheb_plus.basis_vec(order) for (order, _) in u_enum_comb]
            # 2. ...Evaluate product of basis vectors in Chebyshev basis...
            mul_vec = cheb_plus.chebmulrec(*basis_vec_arr)
            # 3. ...Take L^2 projection into P^order
            mul_vec_proj = cheb_plus.chebproj(order, mul_vec)

            # Add contribution at each degree in the test function
            for (coeff, v_) in zip(mul_vec_proj, v):
                # (But only if the corresponding coefficient is sufficiently large)
                if abs(coeff) >= tol:
                    F += constant.Constant(coeff)*res(*[u_ for (_, u_) in u_enum_comb], v_)
    else:
        # Get Gauss--Legendre points (Set no. of Gauss--Legendre points if not already set)
        if leg_pts == None:
            leg_pts = order + 10
        (pt, weight) = numpy.polynomial.legendre.leggauss(leg_pts)
      
        # Retrieve information on dual basis
        dualmat = cheb_plus.chebdualmat(order)

        # Add residual at each Gauss--Legendre point:
        for (pt_, weight_) in zip(pt, weight):
            # Evaluate each u at given point
            u_input = []
            # For each u:
            for u in u_tup:
                # 1. Construct array of basis vectors...
                basis_vec_arr = [cheb_plus.basis_vec(i) for i in range(len(u))]
                # 2. ...Evaluate each Chebyshev function at given Gauss--Legendre point...
                coeff = [cheb_plus.chebval(pt_, basis_vec) for basis_vec in basis_vec_arr]
                # 3. ...Add corresponding contributions from each u component
                for (i, (coeff_, u_)) in enumerate(zip(coeff, u)):
                    if i == 0:
                        u_input    +=              [constant.Constant(float(coeff_))*u_]
                    else:
                        u_input[-1] = u_input[-1] + constant.Constant(float(coeff_))*u_
            
            # Evaluate v at given point
            # 1. Construct array of basis vectors...
            basis_vec_arr = [cheb_plus.basis_vec(i) for i in range(order+1)]
            # 2. ...Evaluate each Chebyshev function at given Gauss--Legendre point...
            coeff = [cheb_plus.chebval(pt_, basis_vec) for basis_vec in basis_vec_arr]
            # 3. ...Convert to dual basis...
            coeff_dual = numpy.dot(dualmat, coeff)
            # 4. ...Add corresponding contributions from each v component to residual
            for (i, (coeff_dual_, v_)) in enumerate(zip(coeff_dual, v)):
                F += (
                    constant.Constant(float(weight_))
                  * constant.Constant(float(coeff_dual_))
                  * res(*u_input, v_)
                )

    return F



'''
[Loosely: Scripts for assembling output data over space-time intervals]
'''



def FETassemble(form, input, timestep, poly=True, leg_pts=None, tol=1e-15):
    '''
    Assemble a scalar space–time quantity over the previous time slab.

    Analogous to `residual`, but returns the assembled scalar resulting from
    integrating the provided kernel `form(*inputs)` over time and space across
    the last timestep. Supports exact Chebyshev mode algebra (poly=True) or
    Gauss–Legendre quadrature in time (poly=False).
    '''

    # Normalise timstep
    timestep = float(timestep)

    # Create output
    out = 0

    if poly:
        # Create a list to store enumeration objects for each u
        u_enum = [enumerate(u) for u in input]

        # Evaluate contributions to output tuple-wise
        for u_enum_comb in itertools.product(*u_enum):
            # 1. Create array of Chebyshev basis vectors for each given order...
            basis_vec_arr = [cheb_plus.basis_vec(order) for (order, _) in u_enum_comb]
            # 2. ...Evaluate product of basis vectors in Chebyshev basis...
            mul_vec = cheb_plus.chebmulrec(*basis_vec_arr)
            # 3. ...Integrate from -1...
            mul_vec_int = cheb_plus.chebint(mul_vec, lbnd=-1)
            # 4. ...And evaluate at 1
            coeff = float(cheb_plus.chebval(1, mul_vec_int))
            
            # If the result is sufficiently large...
            if abs(coeff) >= tol:
                # ...Add the contribution to the output
                out += (
                    coeff
                  * timestep/2
                  * assemble(form(*[u for (_, u) in u_enum_comb]))
                )
    else:
        # Get Gauss--Legendre points (Set no. of Gauss--Legendre points if not already set)
        if leg_pts == None:
            leg_pts = (len(input[0]) - 1) + 10
        (pt, weight) = numpy.polynomial.legendre.leggauss(leg_pts)

        # Add residual at each Gauss--Legendre point:
        for (pt_, weight_) in zip(pt, weight):
            # Evaluate each u at given point
            u_input = []
            # For each u:
            for u in input:
                # 1. Construct array of basis vectors...
                basis_vec_arr = [cheb_plus.basis_vec(i) for i in range(len(u))]
                # 2. ...Evaluate each Chebyshev function at given Gauss--Legendre point...
                coeff = [cheb_plus.chebval(pt_, basis_vec) for basis_vec in basis_vec_arr]
                # 3. ...Add corresponding contributions from each u component
                for (i, (coeff_, u_)) in enumerate(zip(coeff, u)):
                    if i == 0:
                        u_input    +=              [constant.Constant(float(coeff_))*u_]
                    else:
                        u_input[-1] = u_input[-1] + constant.Constant(float(coeff_))*u_
            
            # Add residual contribution to output
            out += (
                    weight_
                  * timestep/2
                  * assemble(form(*u_input))
                )

    return out



'''
[Loosely: Scripts for evaluating functions at specific times]
'''



def FETeval(u_ind, u_t_ind, t, timestep):
    """
    Evaluate an integrated Chebyshev-in-time field at a physical time.

    This helper reconstructs the value of a time-dependent field `u(t)` inside
    the current time slab from:
    - `u_ind`: a tuple `(U0, idx)` giving the spatial Function holding the
      value at the start of the slab, and optionally a subfunction index `idx`
      if `U0` is a mixed spatial Function; use `None` for scalar Functions.
    - `u_t_ind`: a tuple `(UT, group_idx)` where `UT` is the space–time Mixed
      Function holding all Chebyshev coefficients for the time derivative
      `du/dt`, and `group_idx` selects which grouped field inside `UT` to use.
      Group indices correspond to the order of component spaces used when
      constructing the enclosing FET(Mixed)FunctionSpace.
    - `t`: the physical time offset inside the slab (0 <= t <= timestep).
    - `timestep`: the physical size of the slab Δt.

    Internally, this maps `t` to the Chebyshev reference interval [-1, 1],
    integrates the Chebyshev basis exactly, and accumulates the contributions
    from the du/dt coefficients to recover `u(t)`.

    Returns
    - A Firedrake UFL object representing the spatial field evaluated at time t
      (suitable for assignment to a Function).
    """

    # Evaluate reference time on [-1, 1] interval
    t_ref = -1 + 2*t/timestep

    # Unpackage inputs
    (u_ind_0,   u_ind_1)   = u_ind
    (u_t_ind_0, u_t_ind_1) = u_t_ind

    # Normalise inputs
    t = float(t)
    timestep = float(timestep)
    if u_t_ind_1 == None:
        u_t_ind_1 = 0

    # Retrieve orders in time
    order = u_t_ind_0.function_space().order

    # 1. Create basis vector array...
    basis_vec_arr = [cheb_plus.basis_vec(i) for i in range(order[u_t_ind_1] + 1)]
    # 2. ...Calculate integrated vectors...
    basis_vec_int_arr = [cheb_plus.chebint(basis_vec, lbnd=-1) for basis_vec in basis_vec_arr]
    # 3. ...Evaluate integrated vectors at evaluation point
    coeff = [float(cheb_plus.chebval(t_ref, basis_vec_int)) for basis_vec_int in basis_vec_int_arr]

    # Evalute output
    if order == [0]:
        if u_ind_1 == None:
            out = u_ind_0 + timestep/2 * coeff[0] * u_t_ind_0.sub(0)
        else:
            out = u_ind_0.sub(u_ind_1) + timestep/2 * coeff[0] * u_t_ind_0.sub(0)
    else:
        if u_ind_1 == None:
            out = u_ind_0 + sum([
                timestep/2 * coeff_ * u_t_ind_0.sub(sum(order[:u_t_ind_1]) + u_t_ind_1 + i)
                for (coeff_, i)
                in zip(coeff, range(order[u_t_ind_1] + 1))
            ])
        else:
            out = u_ind_0.sub(u_ind_1) + sum([
                timestep/2 * coeff_ * u_t_ind_0.sub(sum(order[:u_t_ind_1]) + u_t_ind_1 + i)
                for (coeff_, i)
                in zip(coeff, range(order[u_t_ind_1] + 1))
            ])

    return out

