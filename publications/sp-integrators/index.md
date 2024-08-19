---
title: SP INTEGRATORS
permalink: /publications/sp-integrators/
---

# HIGH-ORDER CONSERVATIVE AND ACCURATELY DISSIPATIVE NUMERICAL INTEGRATORS VIA AUXILIARY VARIABLES

### Boris Andrews, {% include collaborators/patrick/short.md %}

### 16.JUL.2024 ([arXiv](https://doi.org/10.48550/arXiv.2407.11904))

> *[...] we propose an approach for the construction of **timestepping schemes** that **preserve dissipation laws** and **conserve multiple general invariants**, via finite elements in time and the systematic introduction of auxiliary variables. [...] We [devise] novel arbitrary-order schemes that conserve to machine precision **all known invariants of Hamiltonian ODEs** [...] and arbitrary-order schemes for the **compressible Navier–Stokes equations that conserve mass, momentum, and energy, and provably possess non-decreasing entropy**.*

While the results of this work are more general, I would like to provide some exposition for it through the lens of
- Hamiltonian systems,
- symplectic integrators, and
- the Benjamin--Bona--Mahony (BBM) equation,

as I find these results be informative, curious, motivating, and (not least) *cool*!

Symplectic integrators are frequently lauded for their *"energy-conserving properties"*.
Their status as the gold standard for simulating Hamiltonian systems is often put down to this. <br>
Yet, this belief is *not entirely accurate*.

**Symplecticity** enhances the collective behaviour of a group of simulations, which is beneficial! However, it **does not guarantee energy conservation**. <br>
In fact, as noted by [*Ge and Marsden (1988)*](https://doi.org/10.1016/0375-9601(88)90773-6): <br>
> *Symplectic integrators cannot\* conserve energy.* <br>
> *(\*in general)*

![ge_marsden_quote](assets/img/ge_marsden.png)

This limitation is evident in the *Benjamin–Bona–Mahony (BBM)* equation, a model for phenomena including long water waves. <br>
**Solutions to the BBM equation conserve energy**, \\(\int[\frac{1}{2}u^2 + \frac{1}{6}u^3]\\), contributing to their stability and persistence over time.

![waves_off_timor_sea](assets/img/waves_off_timor_sea.jpg)

Simulating the BBM equations using the 2-stage Gauss method, a **symplectic integrator**, we observe a **gradual decline in the simulated energy**. <br>
This decline manifests as *artificial, unphysical oscillations in the solution*.

<video controls style="width: 100%; height: auto;">
  <source src="assets/vid/no_av.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video><br>

In our preprint, Patrick Farrell and I propose a framework to modify numerical time discretisations to preserve conservation laws exactly. We achieve this through:
- **Finite elements in time**
- The systematic introduction of **auxiliary variables**

Unlike other approaches (e.g. projection methods) this approach *preserves the symmetry* of the initial timestepping scheme, crucial for realistic simulations.

Applying our framework to Hamiltonian systems (incl. the BBM equation) we derive a general Hamiltonian integrator with exact energy conservation.
Simulating the BBM equations using the ***modified* 2-stage Gauss method**, we observe **exact energy conservation** in the simulation.
This *avoids the artificial oscillations* and provides far more qualitatively accurate results. <br>
(Note: The video *should* appear stationary. It's loading fine; this is the correct solution behaviour!)

<video controls style="width: 100%; height: auto;">
  <source src="assets/vid/av.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video><br>

Crucially however, our framework extends *beyond Hamiltonian systems*, and beyond conservation laws.
For instance, we use it to develop numerical schemes for the *compressible Navier--Stokes equations* that:
- **Conserve mass, momentum, and energy**
- **Increase total entropy**

<video controls style="width: 100%; height: auto;">
  <source src="assets/vid/compressible_ns.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video><br>

Further applications of the framework can be found in the paper, and we are actively pursuing many more at the moment! <br>
The framework is *general and powerful*. If you are investigating any type of transient system, we hope our work can provide a simple approach for generating more physically realistic simulations.

*We would both gladly discuss it further!*
- <a href="mailto:boris.andrews@maths.ox.ac.uk">boris.andrews@maths.ox.ac.uk</a>
- <a href="mailto:patrick.farrell@maths.ox.ac.uk">patrick.farrell@maths.ox.ac.uk</a>

## Co-authors

### {% include collaborators/patrick/full.md %}

## Talks

{% include timeline.md %}

<div class="timeline">
  <div class="outer">
    <div class="card">
      <div class="info">
        <h3 class="title">2025</h3>
        <p><ul>
          <li><strong>SIAM DS25, <em>Denver, Colorado</em></strong></li>
          <li><strong>Invited talk, <em>Brown Unversity</em></strong></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2024</h3>
        <p><ul>
          <li><strong>Internal seminar, <em>Rice University</em></strong></li>
          <li>Firedrake User Meeting 2024, <em>University of Oxford</em></li>
          <div style="text-align: center; padding: 10px 0;"><strong>⬆️ UPCOMING | PAST ⬇️</strong></div>
          <li>PDEsoft, <em>University of Cambridge</em></li>
          <li>Finite Element Fair, <em>University College London (UCL)</em></li>
          <li><strong>Exploiting Algebraic and Geometric Structure in Time-integration Methods workshop, <em>University of Pisa</em></strong></li>
          <li>UKAEA PhD student engagement day, <em>CCFE</em></li>
          <li>Junior Applied Mathematics Seminar, <em>University of Warwick</em></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2023</h3>
        <p><ul>
          <li><strong>ICIAM 2023, <em>Waseda University</em></strong></li>
          <li>Numerical analysis group internal seminar, <em>University of Oxford</em></li>
          <li>Junior Applied Mathematics Seminar, <em>University of Oxford</em></li>
          <li>Met Office presentation, <em>University of Oxford</em></li>
        </ul></p>
      </div>
    </div>
  </div>
</div>
