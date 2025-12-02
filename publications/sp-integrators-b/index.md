---
title: SP INTEGRATORS (PART 2)
permalink: /publications/sp-integrators-b/
---

# CONSERVATIVE AND DISSIPATIVE DISCRETISATIONS OF MULTI-CONSERVATIVE ODEs AND GENERIC SYSTEMS

### Boris Andrews <code>&#124;</code> {% include collaborators/patrick/short.md %}

### 28.NOV.2025 ([arXiv](https://doi.org/10.48550/arXiv.2511.23266))

{% include highlight-box.md %}
<div class="highlight-box" onclick="window.location.href='https://doi.org/10.48550/arXiv.2511.23266';"><b>
    CHECK OUT ON ARXIV!
</b></div>

> *[...] we present two novel contributions: (i) an arbitrary-order time discretisation for **general conservative ordinary differential equations** that **conserves all known invariants** and (ii) an **energy-conserving** and **entropy-dissipating** scheme for [...] differential equations written in the **GENERIC** format [...]. We illustrate the advantages of our approximations with numerical examples of the **Kepler** and **Kovalevskaya problems**, a **combustion engine model**, and the **Benjamin–Bona–Mahony** equation.*

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL ABSTRACT</b>
    <div class="details">
        Partial differential equations (PDEs) describing thermodynamically isolated systems typically possess conserved quantities (like mass, momentum, and energy) and dissipated quantities (like entropy).
        Preserving these conservation and dissipation laws on discretisation in time can yield vastly better approximations for the same computational effort, compared to schemes that are not structure-preserving. <br><br>
        In this work we present two novel contributions: (i) an arbitrary-order time discretisation for general conservative ordinary differential equations that conserves all known invariants and (ii) an energy-conserving and entropy-dissipating scheme for both ordinary and partial differential equations written in the GENERIC format, a superset of Poisson and gradient-descent systems.
        In both cases the underlying strategy is the same: the systematic introduction of auxiliary variables, allowing for the replication at the discrete level of the proofs of conservation or dissipation.
        We illustrate the advantages of our approximations with numerical examples of the Kepler and Kovalevskaya problems, a combustion engine model, and the Benjamin-Bona-Mahony equation.
    </div>
</div>

*(Full details available soon! Details below offer a brief overview of the material in the manuscript on GENERIC systems only.)*

The [GENERIC formalism](https://en.wikipedia.org/wiki/GENERIC_formalism/) extends Hamiltonian systems to include both:
- a *conserved* energy
- a *non-decreasing* entropy

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL DETAILS</b>
    <div class="details">
        The general GENERIC ODE in \(\mathbf{x} : \mathbb{R}_+ \to \mathbb{R}^d\) is
        \[
            \dot{\mathbf{x}}  =  L(\mathbf{x})\nabla E(\mathbf{x}) + M(\mathbf{x})\nabla S(\mathbf{x}).
        \]
      Here, \(E, S : \mathbb{R}^d \to \mathbb{R}\) are the (conserved) energy and (non-decreasing) entropy, and \(L, M : \mathbb{R}^d \to \mathbb{R}^{d\times d}\) are the skew-symmetric (Poisson) matrix and positive semidefinite (friction) matrix.
        With the following orthogonality conditions,
        \[
            \nabla S(\mathbf{x})^\top L(\mathbf{x}) = 0,  \qquad
            \nabla H(\mathbf{x})^\top M(\mathbf{x}) = 0,
        \]
        the conservation of \(E\) and non-dissipation of \(S\) can be identified by testing against \(\nabla E\) and \(\nabla S\) respectively.
        Extending to PDEs is fiddly (for the introduction of Fréchet derivatives) but similar.
    </div>
</div>

As the name suggests, this is **extremely general**.
Examples of such systems include:
- the *compressible* Navier–Stokes equations
- the Boltzmann equation
- pretty much any *irreversible* thermodynamic system

We can apply the framework from [mine and Patrick Farrell's preprint](/publications/sp-integrators-a/) to preserve both the **conservative** and **non-dissipation** structures.
As such, we have a *general way to construct structure-preserving finite element methods for any of the above systems*, with arbitrary finite elements and at arbitrary order in space and time.

These properties are **crucial for accurately capturing the dynamics** of these systems.

## RELATED WORKS

This scheme can be viewed as a **special case of my earlier work** with {% include collaborators/patrick/short.md %}, on [general constructions for conservative and dissipative finite element integrators](/publications/sp-integrators/).

## RELATED OPEN PROBLEMS

{% include open-problems/title.md %}
{% include open-problems/all/conservative-pdes.md %}
{% include open-problems/all/dissipative-odes.md %}
{% include open-problems/all/viscoelastic.md %}
{% include open-problems/all/compressible-mhd.md %}

## TALKS

{% include timeline.md %}

<div class="timeline">
<div class="outer">
    <div class="card">
      <div class="info">
        <h3 class="title">2026</h3>
        <p><ul>
          <li>ECCOMAS WCCM, <em>Munich</em></li>
          <div style="text-align: center; padding: 10px 0;"><strong>⬆️ UPCOMING ⬆️</strong></div>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2025</h3>
        <p><ul>
          <div style="text-align: center; padding: 10px 0;"><strong>⬇️ PAST ⬇️</strong></div>
          <li>Biennial Numerical Analysis Conference, <em>University of Strathclyde</em></li>
          <li><strong>Numerical Mathematics & Scientific Computing Seminar, <em>Rice University</em></strong></li>
          <li><strong>SIAM CSE, <em>Fort Worth, Texas</em></strong></li>
          <li><strong>Scientific Computing Seminar, <em>Brown Unversity</em></strong></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2024</h3>
        <p><ul>
          <li>External ("tiny desk") Seminar, <em>Rice University</em></li>
          <li>Computing Division Technical Meeting, <em>UKAEA</em></li>
          <li>Firedrake User Meeting, <em>University of Oxford</em></li>
          <li>PDEsoft, <em>University of Cambridge</em></li>
          <li>Finite Element Fair, <em>University College London (UCL)</em></li>
          <li><strong>Exploiting Algebraic and Geometric Structure in Time-integration Methods workshop, <em>University of Pisa</em></strong></li>
          <li>UKAEA PhD Student Engagement Day, <em>UKAEA</em></li>
          <li>Junior Applied Mathematics Seminar, <em>University of Warwick</em></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2023</h3>
        <p><ul>
          <li><strong>ICIAM, <em>Waseda University</em></strong></li>
          <li>Numerical Analysis Group Internal Seminar, <em>University of Oxford</em></li>
          <li>Junior Applied Mathematics Seminar, <em>University of Oxford</em></li>
          <li>Met Office Presentation, <em>University of Oxford</em></li>
        </ul></p>
      </div>
    </div>
  </div>
</div>
