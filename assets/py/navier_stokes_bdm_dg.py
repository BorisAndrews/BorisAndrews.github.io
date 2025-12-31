import firedrake
from firedrake import *

# 1. Mesh Definition
# Unit square mesh with N x N elements
N = 16
mesh = UnitSquareMesh(N, N)

# 2. Function Spaces
# Velocity: BDM (Brezzi-Douglas-Marini) degree 1
# Pressure: DG (Discontinuous Galerkin) degree 0
# This pair is inf-sup stable.
V = FunctionSpace(mesh, "BDM", 1)
Q = FunctionSpace(mesh, "DG", 0)
W = V * Q

# 3. Trial and Test Functions
u, p = TrialFunctions(W)
v, q = TestFunctions(W)

# 4. Solution Function
w = Function(W)
u_sol, p_sol = w.subfunctions

# 5. Problem Parameters
nu = Constant(0.01)  # Kinematic viscosity
f = Constant((1.0, 0.5))  # Forcing term to drive the flow

# 6. Variational Form
# We use a Symmetric Interior Penalty (SIP) method for the viscous term
# because BDM elements are H(div)-conforming but not H1-conforming.
# The tangential components are discontinuous across cell boundaries.

n = FacetNormal(mesh)
h = CellDiameter(mesh)
sigma = Constant(10.0)  # Penalty parameter for SIPG

def a_viscous(u, v):
    # Volume term: nu * grad(u) : grad(v)
    # Note: grad(u) is computed element-wise
    term = nu * inner(grad(u), grad(v)) * dx
    
    # Interior Facets
    # Consistency term: - < {nu*grad(u)}, [v] >
    # Symmetry term:    - < {nu*grad(v)}, [u] >
    # Penalty term:     + (sigma/h_avg) * < [u], [v] >
    # jump(u, n) computes the tensor jump u+ n+^T + u- n-^T
    term -= nu * inner(avg(grad(u)), jump(v, n)) * dS
    term -= nu * inner(avg(grad(v)), jump(u, n)) * dS
    term += (sigma / avg(h)) * nu * inner(jump(u, n), jump(v, n)) * dS
    
    # Boundary Facets (Weak imposition of no-slip BC u=0)
    # We use Nitsche's method / penalty on the boundary.
    # Consistency: - (nu*grad(u)*n) . v
    # Symmetry:    - (nu*grad(v)*n) . u
    # Penalty:     + (sigma/h) * u . v
    term -= nu * inner(grad(u), outer(v, n)) * ds
    term -= nu * inner(grad(v), outer(u, n)) * ds
    term += (sigma / h) * nu * inner(u, v) * ds
    
    return term

def b_pressure(u, p, v, q):
    # - (p, div(v)) + (q, div(u))
    return -p * div(v) * dx + q * div(u) * dx

def c_convection(u, z, v):
    # Non-linear convection term: (u . grad(u)) . v
    # For H(div) elements, we can use the standard term element-wise.
    # For higher Reynolds numbers, upwinding would be needed.
    return inner(dot(u, nabla_grad(z)), v) * dx

# Total variational form
# F(u, p; v, q) = 0
F = a_viscous(u_sol, v) + \
    c_convection(u_sol, u_sol, v) + \
    b_pressure(u_sol, p_sol, v, q) - \
    inner(f, v) * dx

# 7. Solver
# We use a non-linear solver (Newton's method)
# The Jacobian is computed automatically by Firedrake.
solve(F == 0, w, solver_parameters={
    "snes_monitor": None,
    "ksp_type": "preonly",
    "pc_type": "lu",
    "pc_factor_mat_solver_type": "mumps"
})

# 8. Output
print("Solution computed.")
u_out, p_out = w.subfunctions
u_out.rename("Velocity")
p_out.rename("Pressure")

# Save to file
outfile = File("navier_stokes_bdm_dg.pvd")
outfile.write(u_out, p_out)
print("Results saved to navier_stokes_bdm_dg.pvd")
