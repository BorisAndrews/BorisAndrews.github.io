---
title: GENERIC PDEs
permalink: /publications/generic/
---

# CONSERVATIVE-DISSIPATIVE INTEGRATORS FOR REVERSIBLE-IRREVERSIBLE SYSTEMS

### Boris Andrews

### In preparation (Draft available on request)

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
      Here, \(E, S : \mathbb{R}^d \to \mathbb{R}\) are the (conserved) energy and (non-decreasing) entropy, and \(L, M : \mathbb{R}^d \to \mathbb{R}^{d\times d}\) are the skew-symmetric (Poisson) matrix and positive semi-definite (friction) matrix.
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

We can apply the framework from [mine and Patrick Farrell's preprint](/publications/sp-integrators/) to preserve both the **conservative** and **non-dissipation** structures.
As such, we have a *general way to construct structure-preserving finite element methods for any of the above systems*, with arbitrary finite elements and at arbitrary order in space and time.

These properties are **crucial for accurately capturing the dynamics** of these systems.

*(Further details available soon!)*

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
        <h3 class="title">2025</h3>
        <p><ul>
          <li><strong>Invited talk, <em>Brown Unversity</em></strong></li>
          <div style="text-align: center; padding: 10px 0;"><strong>⬆️ UPCOMING | PAST ⬇️</strong></div>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2024</h3>
        <p><ul>
          <li>External ("tiny desk") seminar, <em>Rice University</em></li>
        </ul></p>
      </div>
    </div>
  </div>
</div>
