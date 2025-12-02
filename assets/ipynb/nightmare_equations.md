# Maxwell–Stefan mixtures with heat and a finite-element-in-time scheme

A compact, self-contained guide to the quasi-incompressible, heat-conducting Maxwell–Stefan mixture model and a Galerkin-in-time (finite element in time) discretization suitable for Firedrake/Irksome-style implementations.

---

## 1. Unknowns, data, and constraints

- Species partial densities: $\rho_i(x,t) \ge 0$, for $i=1,\dots,N$.
- Total density: $\rho := \sum_{i=1}^N \rho_i$.
- Barycentric velocity: $\boldsymbol u(x,t)$.
- Temperature: $\theta(x,t) > 0$.
- Pressure: $p(x,t)$ (acts as a Lagrange multiplier for quasi-incompressibility).
- Specific volumes (constants): $V_i > 0$, with the quasi-incompressibility constraint
  $$\sum_{i=1}^N V_i\,\rho_i = 1 \quad \text{a.e. in } \Omega.$$
- Helmholtz free energy density: $\rho F((\rho_i),\theta)$ with $F$ sufficiently smooth.

Shorthand:

- Chemical potentials per temperature:
  $$\frac{\mu_i}{\theta} = \frac{\partial}{\partial \rho_i}\Big(\frac{\rho F((\rho_i),\theta)}{\theta}\Big) + V_i\,\frac{p}{\theta}. $$

- Diffusive fluxes $\boldsymbol J_i$ satisfy the barycentric constraint
  $$\sum_{i=1}^N \boldsymbol J_i = \boldsymbol 0,$$
  which ensures total mass conservation when summing species balances.

---

## 2. Balance laws (strong form)

On a fixed domain $\Omega \subset \mathbb R^d$ with outward normal $\boldsymbol n$:

1) Species mass (for each $i$):
$$\partial_t \rho_i + \operatorname{div}(\rho_i\,\boldsymbol u) = \operatorname{div}\,\boldsymbol J_i.$$

2) Momentum:
$$\partial_t(\rho\,\boldsymbol u) + \operatorname{div}(\rho\,\boldsymbol u\otimes \boldsymbol u) = \operatorname{div}\,\boldsymbol\sigma.$$

3) Total energy (internal + kinetic, absorbed here in $\rho e$):
$$\partial_t(\rho e) + \operatorname{div}(\rho e\,\boldsymbol u) = \operatorname{div}\,\boldsymbol J_e + \boldsymbol\sigma : \nabla \boldsymbol u.$$

Here $\boldsymbol\sigma$ is the Cauchy stress (assumed symmetric). For a Newtonian model one often writes
$$\boldsymbol\sigma = -p\,\boldsymbol I + 2\eta\,\boldsymbol D(\boldsymbol u) + \lambda\,(\operatorname{div}\boldsymbol u)\,\boldsymbol I,$$
with $\boldsymbol D(\boldsymbol u)=\tfrac12(\nabla\boldsymbol u + \nabla\boldsymbol u^\top)$, but the theory below does not depend on this specific choice beyond symmetry and appropriate coercivity.

---

## 3. Constitutive laws for diffusive and heat fluxes

The Maxwell–Stefan structure with thermal coupling is encoded by
$$
\boldsymbol J_i = \sum_{j=1}^N M_{ij}((\rho_k),\theta)\,\nabla\!\left(\frac{\mu_j}{\theta}\right) \;\; -\;\; C_i((\rho_k),\theta)\,\nabla\!\left(\frac{1}{\theta}\right),
$$
$$
\boldsymbol J_e = -K((\rho_k),\theta)\,\nabla\!\left(\frac{1}{\theta}\right) + \sum_{j=1}^N C_j((\rho_k),\theta)\,\nabla\!\left(\frac{\mu_j}{\theta}\right).
$$

Thermodynamic/compatibility requirements:

- $M = (M_{ij})$ is symmetric positive semidefinite (PSD) and satisfies $\sum_{i=1}^N M_{ij}=0$ for each $j$.
- $\sum_{i=1}^N C_i = 0$.
- Thermal conductivity $K \ge 0$.
- These ensure $\sum_i \boldsymbol J_i = \boldsymbol 0$ (mass conservation) and nonnegative entropy production (Onsager symmetry).

---

## 4. Quasi-incompressibility and pressure

The specific-volume constraint $\sum_i V_i\rho_i=1$ is enforced via the chemical potentials through the pressure term $V_i p/\theta$ in $\mu_i/\theta$ (i.e., $p$ acts as the Lagrange multiplier imposing the volume constraint). A useful implied relation is the divergence condition
$$
\operatorname{div}\,\boldsymbol u = \operatorname{div}\!\left[\sum_{i,j=1}^N V_i\,M_{ij}\,\nabla\!\left(\frac{\mu_j}{\theta}\right)\right]
\; -\; \operatorname{div}\!\left[\sum_{i=1}^N V_i\,C_i\,\nabla\!\left(\frac{1}{\theta}\right)\right],
$$
which follows from differentiating the constraint in time and using the species balances and the constitutive fluxes.

---

## 5. Thermodynamic closure: free energy and chemical potentials

Define the Helmholtz free energy density $\rho F((\rho_i),\theta)$. Then
$$
\frac{\mu_i}{\theta} = \frac{\partial}{\partial\rho_i}\Big(\frac{\rho F}{\theta}\Big) + V_i\,\frac{p}{\theta}.
$$
For common choices of $F$ (e.g., ideal or regular-solution mixtures), this yields explicit expressions for $\mu_i$ and constitutive coefficients $(M_{ij}, C_i, K)$ that render the entropy production nonnegative. In particular, in matrix form the pair $(\boldsymbol J, \boldsymbol J_e)$ is an Onsager system driven by the thermodynamic forces $\nabla(\mu/\theta)$ and $\nabla(1/\theta)$.

---

## 6. Compact “final system” (as used for discretization)

Using the above closure, one can equivalently work with
$$
\partial_t \rho_i = \operatorname{div}\left[\sum_{j=1}^N M_{ij}\,\nabla\!\left(\frac{\mu_j}{\theta}\right) - C_i\,\nabla\!\left(\frac{1}{\theta}\right)\right],
$$
$$
\frac{\mu_i}{\theta} = \frac{\partial}{\partial\rho_i}\Big(\frac{\rho F}{\theta}\Big) + V_i\,\frac{p}{\theta},
$$
$$
\partial_t(\rho\,\boldsymbol u) + \operatorname{div}(\rho\,\boldsymbol u\otimes\boldsymbol u) = \operatorname{div}\,\boldsymbol S((\rho_i),\theta,\nabla\boldsymbol u) + \nabla\!\Big(\rho F - \sum_{i=1}^N \rho_i\,\mu_i\Big),
$$
$$
\operatorname{div}\,\boldsymbol u = \operatorname{div}\!\left[\sum_{i,j=1}^N V_i M_{ij}\,\nabla\!\left(\frac{\mu_j}{\theta}\right) - \sum_{i=1}^N V_i C_i\,\nabla\!\left(\frac{1}{\theta}\right)\right],
$$
$$
\partial_t(\rho e) + \operatorname{div}(\rho e\,\boldsymbol u) = -\operatorname{div}\left[K\,\nabla\!\left(\frac{1}{\theta}\right) - \sum_{j=1}^N C_j\,\nabla\!\left(\frac{\mu_j}{\theta}\right)\right] + \boldsymbol S: \nabla\boldsymbol u + \Big(\rho F - \sum_{i=1}^N \rho_i\,\mu_i\Big)\,\operatorname{div}\boldsymbol u.
$$
Here $\boldsymbol S$ denotes the viscous stress (e.g., Newtonian), and the pressure is absorbed in the thermodynamic term through the definition of $\mu_i$.

---

## 7. Entropy and energy structure

Define the specific entropy $s((\rho_i),\theta)$ via the Helmholtz free energy $F$ by
$$
\rho s = -\,\rho\,\partial_\theta F((\rho_i),\theta),
$$
and the total energy density by
$$
\rho e = \tfrac{\rho}{2}\,\|\boldsymbol u\|^2 + \rho F((\rho_i),\theta) + \theta\,\rho s.
$$

With the Maxwell–Stefan/Onsager structure for $(\boldsymbol J_i, \boldsymbol J_e)$ and a symmetric PSD mobility matrix $M$, one obtains the entropy balance
$$
\partial_t(\rho s) + \operatorname{div}(\rho s\,\boldsymbol u + \Psi) = \sigma_s \;\ge\; 0,
$$
where the entropy flux $\Psi$ and production $\sigma_s$ are
$$
\Psi = -\,K\,\nabla\!\Big(\tfrac{1}{\theta}\Big) + \sum_j C_j\,\nabla\!\Big(\tfrac{\mu_j}{\theta}\Big),
\qquad
\sigma_s = \nabla\!\Big(\tfrac{1}{\theta}\Big)\!:\!K\,\nabla\!\Big(\tfrac{1}{\theta}\Big)
\;+
\nabla\!\Big(\tfrac{\mu}{\theta}\Big)^{\!\top} M\,\nabla\!\Big(\tfrac{\mu}{\theta}\Big)
\;+
  	frac{1}{\theta}\,\boldsymbol S : \nabla\boldsymbol u,
$$
which is nonnegative due to $K\ge 0$, $M\succeq 0$, and $\boldsymbol S$’s coercivity.

Similarly, combining the momentum and energy equations yields the total energy balance
$$
\partial_t\!\int_\Omega \rho e\,\mathrm dx
\;=\; -\int_{\partial\Omega} (\boldsymbol J_e - (\rho e)\,\boldsymbol u)\cdot\boldsymbol n\,\mathrm dS,
$$
thus, in the absence of external sources, the total energy $\int_\Omega \rho e\,\mathrm dx$ is conserved in time (while kinetic energy may convert into internal energy via $\boldsymbol S: \nabla\boldsymbol u$).

---

## 8. Weak formulation (space) for FEM

Let test functions be $\varphi_i$ for each species equation, $\boldsymbol v$ for momentum, $\eta$ for energy, and $q$ for the divergence constraint. With $\langle a,b\rangle := \int_\Omega a\,b\,\mathrm dx$ and using integration by parts in space for diffusive terms:


### Species balances (for all $i$)

$$
\int_\Omega (\partial_t\rho_i)\,\varphi_i\,\mathrm dx + \int_\Omega \rho_i\,\boldsymbol u\cdot\nabla\varphi_i\,\mathrm dx + \int_\Omega \boldsymbol J_i\cdot\nabla\varphi_i\,\mathrm dx = 0.
$$

### Momentum

$$
\int_\Omega (\partial_t(\rho\boldsymbol u))\cdot\boldsymbol v\,\mathrm dx + \int_\Omega (\rho\,\boldsymbol u\otimes\boldsymbol u):\nabla\boldsymbol v\,\mathrm dx + \int_\Omega \boldsymbol S: \nabla\boldsymbol v\,\mathrm dx - \int_\Omega \Big(\rho F - \sum_i\rho_i\mu_i\Big)\operatorname{div}\boldsymbol v\,\mathrm dx = 0.
$$

### Divergence constraint (quasi-incompressibility in flux form)

$$
\int_\Omega (\operatorname{div}\boldsymbol u)\,q\,\mathrm dx + \int_\Omega \Big(\sum_{i,j} V_i M_{ij}\,\nabla(\mu_j/\theta) - \sum_i V_i C_i\,\nabla(1/\theta)\Big)\cdot\nabla q\,\mathrm dx = 0.
$$

### Energy balance

$$
\int_\Omega (\partial_t(\rho e))\,\eta\,\mathrm dx + \int_\Omega (\rho e\,\boldsymbol u)\cdot\nabla\eta\,\mathrm dx + \int_\Omega \Big(K\,\nabla(1/\theta) - \sum_j C_j\,\nabla(\mu_j/\theta)\Big)\cdot\nabla\eta\,\mathrm dx \\
= \int_\Omega (\boldsymbol S: \nabla\boldsymbol u)\,\eta\,\mathrm dx + \int_\Omega \Big(\rho F - \sum_i \rho_i\,\mu_i\Big)\,(\operatorname{div}\boldsymbol u)\,\eta\,\mathrm dx.
$$

The algebraic relation $\mu_i/\theta = \partial_{\rho_i}(\rho F/\theta) + V_i p/\theta$ closes the system; $p$ appears only through $\mu_i$ and may additionally be recovered (if desired) by volume-constraint residuals.

---

## 9. Continuous Petrov–Galerkin semi-discrete formulation

We consider a continuous Petrov–Galerkin (in time) semi-discrete system with solution variables

- Primary (time-continuous in the fully discrete setting): $(\rho_i)_{i=1}^N$, $\boldsymbol u$, and $\rho s$.
- Auxiliary (time-discontinuous in the fully discrete setting): $(\mu_i)_{i=1}^N$, $p$, and $\theta$.

Let the test functions be $\psi_i,\zeta_i,\boldsymbol v,\boldsymbol w, q, \omega, \gamma$, respectively. The skew-symmetric convective form is
$$
\mathcal C(\rho\boldsymbol u, \boldsymbol v, \boldsymbol w) = \tfrac12\big[(\rho\boldsymbol u\cdot\nabla\boldsymbol v)\cdot\boldsymbol w - (\rho\boldsymbol u\cdot\nabla\boldsymbol w)\cdot\boldsymbol v\big].
$$

The semi-discrete equations read: find $(\rho_i,\boldsymbol u,\rho s,\mu_i,p,\theta)$ such that
$$
\int_\Omega\Big[\partial_t\rho_i\,\psi_i - \rho_i\,\boldsymbol u\cdot\nabla\psi_i + \sum_j M_{ij}\,\nabla\!\Big(\tfrac{\mu_j}{\theta}\Big)\!\cdot\nabla\psi_i\Big] \,\mathrm dx = 0, \quad \forall\,\psi_i,
$$
$$
\int_\Omega\Big[\mu_i\,\zeta_i - \partial_{\rho_i}[\rho e] \,\zeta_i - V_i\,p\,\zeta_i\Big] \,\mathrm dx = 0, \quad \forall\,\zeta_i,
$$
$$
\int_\Omega\Big[\sqrt{\rho}\,\partial_t\boldsymbol m\cdot\boldsymbol v + \mathcal C(\rho\boldsymbol u, \boldsymbol u, \boldsymbol v) + \boldsymbol S(\rho,\theta,\nabla\boldsymbol u):\nabla\boldsymbol v - p\,\operatorname{div}\boldsymbol v
 + \sum_i \rho_i\,\nabla(\mu_i - V_i p)\cdot\boldsymbol v + \rho s\,\nabla\theta\cdot\boldsymbol v\Big] \,\mathrm dx = 0, \quad \forall\,\boldsymbol v,
$$
$$
\int_\Omega\Big[\boldsymbol m\cdot\boldsymbol w - \sqrt{\rho}\,\boldsymbol u\cdot\boldsymbol w\Big] \,\mathrm dx = 0, \quad \forall\,\boldsymbol w,
$$
$$
\int_\Omega\Big[\operatorname{div}\,\boldsymbol u\,q + \sum_{i,j} M_{ij}\,\nabla\!\Big(\tfrac{\mu_j}{\theta}\Big)\,V_i\,\nabla q\Big] \,\mathrm dx = 0, \quad \forall\,q,
$$
$$
\int_\Omega\Big[\partial_t(\rho s)\,\omega - \rho s\,\boldsymbol u\cdot\nabla\omega - \boldsymbol S(\rho,\theta,\nabla\boldsymbol u):\nabla\boldsymbol u\,\tfrac{\omega}{\theta} - K\,\nabla\!\Big(\tfrac{1}{\theta}\Big)\cdot\nabla\!\Big(\tfrac{\omega}{\theta}\Big)
 - \sum_{i,j} M_{ij}\,\nabla\!\Big(\tfrac{\mu_j}{\theta}\Big)\cdot\nabla\!\Big(\tfrac{\omega\,\mu_i}{\theta}\Big)\Big] \,\mathrm dx = 0, \quad \forall\,\omega,
$$
$$
\int_\Omega\Big[\theta\,\gamma - \partial_{\rho s}(\rho e)\,\gamma\Big] \,\mathrm dx = 0, \quad \forall\,\gamma.
$$

Interpretation (per line):

- Species mass balances with Maxwell–Stefan diffusion written in symmetric mobility form.
- Thermodynamic closure linking $\mu_i$ to $\partial_{\rho_i}(\rho e)$ and $p$ (via specific volume $V_i$).
- Momentum balance in skew-symmetric convective form $\mathcal C$, plus viscous stress $\boldsymbol S$, pressure work, thermodynamic forcing $\sum_i \rho_i\nabla(\mu_i - V_i p)$, and a thermal term $\rho s\,\nabla\theta$.
- Definition of the auxiliary momentum variable $\boldsymbol m \approx \sqrt{\rho}\,\boldsymbol u$.
- Quasi-incompressibility/divergence constraint in flux form consistent with the volume constraint.
- Entropy balance with viscous dissipation, Fourier heat conduction, and Maxwell–Stefan contributions written in Onsager form.
- Temperature closure through the Gibbs relation $\partial_{\rho s}(\rho e)=\theta$.


## 10. Symbol glossary

- $\rho_i$: partial density of species $i$; $\rho = \sum_i \rho_i$.
- $\boldsymbol u$: barycentric velocity.
- $\theta$: temperature.
- $p$: pressure (Lagrange multiplier for $\sum_i V_i\rho_i=1$).
- $F$: Helmholtz free energy per unit mass; $\rho F$ is per unit volume.
- $\mu_i$: chemical potential of species $i$.
- $M_{ij}$: Maxwell–Stefan mobility matrix (symmetric PSD, column sums zero).
- $C_i$: thermal diffusion (Soret/Dufour-type) coefficients with $\sum_i C_i=0$.
- $K$: thermal conductivity (nonnegative).
- $\boldsymbol J_i$: species diffusion flux; $\sum_i \boldsymbol J_i=\boldsymbol 0$.
- $\boldsymbol J_e$: energy flux.
- $\boldsymbol S$: viscous stress tensor (symmetric).
