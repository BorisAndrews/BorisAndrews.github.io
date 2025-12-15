from firedrake import *
from irksome import *
from pathlib import Path



def stefan_maxwell_irksome(
    Nspec:      int = 3,
    Nx:         int = 30,
    deg:        int = 1,
    vdeg:       int = 2,
    timedeg:    int = 2,
    Nt:         float = 1e3,
    dt:         float = 1e-4,
    Kval:       float = 1e-2,
    eta:        float = 1e-2,
    theta_min:  float = 1e-6,  # Quick fix to avoid instability when negative theta is hit during the Newton solve | Shouldn't affect solution if value is below minimum theta value
    scheme:     str = "cpg",
    output_dir: str = "output/",
    write_qois: bool = True,
    write_vtk:  bool = True,
):
    """
    Energy- and entropy-preserving Stefan-Maxwell scheme.
    - Unknowns (time-continuous): (rho_i), u, (rho s)
    - Auxiliary (time-discontinuous): (mu_i), p, theta, m
    Returns
    - Dictionary: {"time": [...], "energy": [...], "entropy": [...]}
    """
    # Ensure output directory exists
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Convert parameters to UFL objects
    K_c = Constant(Kval)
    eta_c = Constant(eta)
    dt_c = Constant(dt)
    # Specific volumes matching NGSolve setup
    V_i = [0.35, 0.35, 0.8]

    # Mesh and coordinate (2D periodic box)
    mesh = PeriodicUnitSquareMesh(Nx, Nx)
    x, y = SpatialCoordinate(mesh)

    # Function spaces
    S = FunctionSpace(mesh, "CG", deg)  # Scalar
    V = VectorFunctionSpace(mesh, "CG", vdeg)  # Vector
    Z = MixedFunctionSpace(([S]*Nspec) + [V, S] + ([S]*Nspec) + [S, S, V])  # Mixed space: (rho_1...rho_N, u, rho_s, mu_1...mu_N, p, theta, m)

    # Solution functions
    z = Function(Z, name="state")
    z_split = split(z)
    rho = z_split[0:Nspec]; m = z_split[Nspec]; rho_s = z_split[Nspec+1]; mu = z_split[(Nspec+2):(2*Nspec+2)]; p = z_split[2*Nspec+2]; theta = z_split[2*Nspec+3]; u = z_split[2*Nspec+4]
    z_out = z.subfunctions
    rho_out = z_out[0:Nspec]; m_out = z_out[Nspec]; rho_s_out = z_out[Nspec+1]; mu_out = z_out[(Nspec+2):(2*Nspec+2)]; p_out = z_out[2*Nspec+2]; theta_out = z_out[2*Nspec+3]; u_out = z_out[2*Nspec+4]

    # Split tests (UFL)
    tests = TestFunctions(Z)
    psi = tests[0:Nspec]; v = tests[Nspec]; omega = tests[Nspec+1]; zeta = tests[(Nspec+2):(2*Nspec+2)]; q = tests[2*Nspec+2]; gamma = tests[2*Nspec+3]; w = tests[2*Nspec+4]

    # Helpers for rho (easy)
    rho_tot = sum(rho)
    sqrt_rho = sqrt(rho_tot)
    rho_F = sum([rho[i] * ln(rho[i]/rho_tot) for i in range(Nspec)])
    rho_e = rho_tot * exp((rho_s + rho_F)/rho_tot)
    rho_e_tot = 0.5 * inner(m, m) + rho_e

    # Helpers for rho (hard - require variable objects for implicit differentiation)
    rho_var = [variable(r) for r in rho]
    rho_s_var = variable(rho_s)
    rho_tot_var = sum(rho_var)
    rho_F_var = sum([rho_var[i] * ln(rho_var[i]/rho_tot_var) for i in range(Nspec)])
    rho_e_var = rho_tot_var * exp((rho_s_var + rho_F_var)/rho_tot_var)
    d_rho_e_d_rhoi = [diff(rho_e_var, rho_var[i]) for i in range(Nspec)]
    d_rho_e_d_rhos = diff(rho_e_var, rho_s_var)

    # Mobility M_{ij}
    def M_ij(i, j): return (0.1*rho[i] if i == j else 0.0) - 0.1*rho[i] * rho[j] / rho_tot

    # Skew-symmetric convection form C(rho u, v, w)
    def C_skw(rho_u, v_in, w_in):
        return 0.5 * (
            inner(dot(grad(v_in), rho_u), w_in)
          - inner(dot(grad(w_in), rho_u), v_in)
        )

    # Deviatoric strain (symmetric gradient of u)
    Du = sym(grad(u))

    # Safe inverse theta to avoid instability
    inv_theta = conditional(
        ge(theta, theta_min),
        1/theta,
        (2*theta_min - theta)/theta_min**2
    )

    # Residual
    F = 0
    for i in range(Nspec):  # Mass (for each species)
        diff_flux_i = sum(M_ij(i, j) * grad(mu[j] * inv_theta) for j in range(Nspec))
        F += (
            inner(Dt(rho[i]), psi[i])
          - inner(rho[i] * u, grad(psi[i]))
          + inner(diff_flux_i, grad(psi[i]))
        ) * dx
    for i in range(Nspec):  # Chemical potential
        F += (
            inner(mu[i], zeta[i])
          - inner(d_rho_e_d_rhoi[i], zeta[i])
          - V_i[i] * inner(p, zeta[i])
        ) * dx
    F += (  # Momentum
        inner(sqrt_rho * Dt(m), v)
      + C_skw(rho_tot * u, u, v)
      + 2.0 * eta_c * inner(Du, sym(grad(v)))
      - inner(p, div(v))
      + sum([
            inner(rho[i] * grad(mu[i]), v)
          - V_i[i] * inner(rho[i] * grad(p), v)
        for i in range(Nspec)])
      + inner(rho_s * grad(theta), v)
    ) * dx
    F += (  # Modified momentum
        inner(m, w)
      - inner(sqrt_rho * u, w)
    ) * dx
    F += (  # Pseudo-incompressibility
        inner(div(u), q)
      + sum([sum([
            V_i[i] * inner(M_ij(i, j) * grad(mu[j] * inv_theta), grad(q))
        for j in range(Nspec)]) for i in range(Nspec)])
    ) * dx
    F += (  # Entropy
        inner(Dt(rho_s), omega)
      - inner(rho_s * u, grad(omega))
      - 2.0 * eta_c * inner(inner(Du, Du) * inv_theta, omega)
      - K_c * inner(grad(inv_theta), grad(omega * inv_theta))
      - sum([sum([
            inner(M_ij(i, j) * grad(mu[j] * inv_theta), grad(mu[i] * omega * inv_theta))
        for j in range(Nspec)]) for i in range(Nspec)])
    ) * dx
    F += (  # Temperature
        inner(theta, gamma)
      - inner(d_rho_e_d_rhos, gamma)
    ) * dx

    # Time integrator
    t = Constant(0.0)
    sp = {  # Nonlinear/linear solver settings
        "snes_monitor" : None,
        "snes_converged_reason" : None,
        "snes_atol" : 1e-5,
        "snes_max_it" : 100,
        "snes_type" : "newtonls",
        "snes_linesearch_type" : "bt",
        # "ksp_monitor" : None,
        # "ksp_converged_reason" : None,
    }
    scheme_dict = {
        "cpg"   : ContinuousPetrovGalerkinScheme(timedeg, quadrature_degree=4*timedeg-1),  # Can up degree as needed
        "gauss" : GaussLegendre(timedeg),
        "radau" : RadauIIA(timedeg)
    }
    if scheme == "cpg":
        stepper = TimeStepper(
            F, scheme_dict[scheme.lower()], t, dt_c, z,
            solver_parameters=sp, aux_indices=[Nspec+2+i for i in range(Nspec+3)]
        )
    else:
        stepper = TimeStepper(
            F, scheme_dict[scheme.lower()], t, dt_c, z,
            solver_parameters=sp
        )

    # Initial conditions aligned with Aaron's NGSolve code
    I_between = lambda val, a, b : conditional(And(gt(val, a), lt(val, b)), 1.0, 0.0)

    Iy01 = I_between(y, 0.1, 0.2)
    Iy89 = I_between(y, 0.8, 0.9)
    Ix01 = I_between(x, 0.1, 0.2)
    Ix89 = I_between(x, 0.8, 0.9)

    Ix01Iy01 = Ix01 * Iy01
    Ix89Iy01 = Ix89 * Iy01
    Ix01Iy89 = Ix01 * Iy89
    Ix89Iy89 = Ix89 * Iy89

    Icircle = conditional(lt((x - 0.5)**2 + (y - 0.5)**2, 0.25**2), 1.0, 0.0)

    rho1_ic = 0.2 + 0.9*(Iy01 + Iy89 + Ix01 + Ix89) - 0.9*(Ix01Iy01 + Ix89Iy01 + Ix01Iy89 + Ix89Iy89)
    rho2_ic = 0.2 + 0.9*Icircle
    rho3_ic = (1.0/V_i[2]) - (V_i[1]/V_i[2])*rho2_ic - (V_i[0]/V_i[2])*rho1_ic

    rho_out[0].interpolate(rho1_ic)
    rho_out[1].interpolate(rho2_ic)
    rho_out[2].interpolate(rho3_ic)

    u_ic = as_vector((-sin(pi*x)**2 * sin(2*pi*y), sin(pi*y)**2 * sin(2*pi*x)))
    rho_tot_out = sum(rho_out)
    u_out.interpolate(u_ic)
    m_out.interpolate(sqrt(rho_tot_out) * u_ic)

    theta_out.interpolate(2.0)
    rho_s_out.interpolate(rho_tot_out * ln(theta_out) - sum([rho_out[i] * ln(rho_out[i]/rho_tot_out) for i in range(Nspec)]))

    # Set up outputs
    E_form = rho_e_tot * dx
    S_form = rho_s * dx
    t_arr = []
    E_arr = []
    S_arr = []
    if write_qois:
        qoi_path = out_path / "qois.csv"
        with qoi_path.open("w", encoding="utf-8") as f:
            f.write("time,energy,entropy\n")
    def record_and_log():
        t_out = float(t)
        E_out = float(assemble(E_form))
        S_out = float(assemble(S_form))
        print(BLUE % f"Time (t) = {t_out:.6f}")
        print(GREEN % f"Energy  = {E_out:.8e}")
        print(GREEN % f"Entropy = {S_out:.8e}")
        t_arr.append(t_out)
        E_arr.append(E_out)
        S_arr.append(S_out)
        if write_qois:
            with (out_path / "qois.csv").open("a", encoding="utf-8") as f:
                f.write(f"{t_out},{E_out},{S_out}\n")
    record_and_log()
    if write_vtk:
        vtk = VTKFile(str(out_path / "u.pvd"))
        for (i, rho_out_) in enumerate(rho_out):
            rho_out_.rename(f"Density #{round(i)} (rho_{round(i)})")
        m_out.rename("Modified momentum (m)")
        rho_s_out.rename("Specific entropy (rho s)")
        for (i, mu_out_) in enumerate(mu_out):
            mu_out_.rename(f"Chemical potential #{round(i)} (mu_{round(i)})")
        p_out.rename("Pressure (p)")
        theta_out.rename("Temperature (theta)")
        u_out.rename("Velocity (u)")
        vtk.write(*rho_out, m_out, rho_s_out, *mu_out, p_out, theta_out, u_out, time=float(t))

    # Time loop
    for _ in range(round(Nt)):
        stepper.advance()
        t.assign(float(t) + float(dt_c))
        if write_vtk: vtk.write(*rho_out, m_out, rho_s_out, *mu_out, p_out, theta_out, u_out, time=float(t))
        record_and_log()

    return {"time": t_arr, "energy": E_arr, "entropy": S_arr}



output_dict = stefan_maxwell_irksome()
