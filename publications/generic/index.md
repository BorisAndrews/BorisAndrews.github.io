---
title: GENERIC PDEs
permalink: /publications/generic/
---

# HIGH-ORDER CONSERVATIVE-DISSIPATIVE INTEGRATORS FOR REVERSIBLE-IRREVERSIBLE SYSTEMS

### Boris Andrews

### Upcoming, Draft available on request

The [GENERIC formalism](https://en.wikipedia.org/wiki/GENERIC_formalism) extends Hamiltonian systems to include both:
- a conserved energy
- a non-decreasing entropy

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL DETAILS</b>
    <div class="details">
        The general GENERIC ODE in \(\mathbf{x} : \mathbb{R}_+ \to \mathbb{R}^d\) is
        \[
            \dot{\mathbf{x}}  =  L(\mathbf{x})\nabla E(\mathbf{x}) + M(\mathbf{x})\nabla S(\mathbf{x}).
        \]
        Here, \(E, S : \mathbb{R}^d \to \mathbb{R}\) are the (conserved) energy and (non-decreasing) entropy, and \(L, M : \mathbb{R}^d \to \mathbb{R}\) are the skew-symmetric (Poisson) matrix and positive-semidefinite (friction) matrix.
        With the following orthogonality conditions,
        \[
            \nabla S(\mathbf{x})^\top L(\mathbf{x}) = 0,  \qquad
            \nabla H(\mathbf{x})^\top M(\mathbf{x}) = 0,
        \]
        the conservation of \(E\) and non-dissipation of \(S\) can be identified by testing against \(\nabla E\) and \(\nabla S\) respectively
        Extending to PDEs is fiddly (for the introduction of Fréchet derivatives) but similar.
    </div>
</div>

As the name suggests, this is extremely general.
Examples of such systems include:
- The compressible Navier–Stokes equations
- The Boltzmann equation
- Pretty much any irreversible thermodynamic system (i.e. pretty much any thermodynamic system)

<!-- Add boldface -->

## Talks

{% include timeline.md %}

<div class="timeline">
  <div class="outer">
    <div class="card">
      <div class="info">
        <h3 class="title">2024</h3>
        <p><ul>
          <li><strong>Internal seminar, <em>Rice University</em></strong></li>
          <div style="text-align: center; padding: 10px 0;"><strong>⬆️ UPCOMING | PAST ⬇️</strong></div>
        </ul></p>
      </div>
    </div>
  </div>
</div>