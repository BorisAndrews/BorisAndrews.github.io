---
title: SP integrators
permalink: /publications/sp-integrators/
---

# High-order conservative and accurately dissipative numerical integrators via auxiliary variables

### Boris D Andrews, [Patrick E Farrell](https://pefarrell.org/)

### 16.jul.2024 ([arXiv](https://doi.org/10.48550/arXiv.2407.11904))

> *[...] we propose an approach for the construction of **timestepping schemes** that **preserve dissipation laws** and **conserve multiple general invariants**, via finite elements in time and the systematic introduction of auxiliary variables. [...] We [devise] novel arbitrary-order schemes that conserve to machine precision **all known invariants of Hamiltonian ODEs** [...] and arbitrary-order schemes for the **compressible Navier–Stokes equations that conserve mass, momentum, and energy, and provably possess non-decreasing entropy**.*

<!-- Symplectic integrators are often praised for their *"energy-conserving properties"*. There is an idea that they are the **gold standard** for simulating Hamiltonian systems because they conserve energy. <br>
This is\* a misconception. *(\*in general)*

**Symplecticity** improves the group behaviour of a collection of simulations. This is great\.\.\. <br>
\.\.\.but, it **doesn't guarantee energy conservation**. <br>
In fact, we must choose: <br>
> *Symplectic integrators can't conserve energy.* <br>
> — 📄 Ge, Marsden (1988)

We can see this clearly in the Benjamin–Bona–Mahony (BBM) equation, a model for (among other things) long water waves. <br>
Solutions, \\(u\\), to these equations conserve energy, \\(\int[\frac{1}{2}u^2 + \frac{1}{6}u^3]\\). This makes them very stable and persistent over long times.

So what happens with a symplectic integrator (e.g. 2-stage Gauss)? <br>
The energy of the simulated solution creeps down and down. Here, this means after a while we just get a bunch of artificial oscillatory garbage.

Patrick Farrell and I propose a framework to modify simulations to keep those conservation laws. <br>
The idea is based on a combination of auxiliary variables and finite elements in time.

As an example, we apply it to Hamiltonian systems. This gives us a way to modify a simulation of a Hamiltonian system so it conserves energy. <br>
As an example of a Hamiltonian system, we consider BBM.

So what happens with a **modified** symplectic integrator (e.g. **modified** 2-stage Gauss)? <br>
The energy of our simulated solution stays level. Thus, no wiggly garbage: much more realistic. <br>
(N.B. The video is meant to look stationary; that's how we know we've got the right behaviour. It is loading fine!)

It's not just BBM though, and it's not just conservation laws. <br>
For example, in the paper we construct simulations for compressible fluids that:
- Conserve mass/momentum/energy.
- Increase total entropy. <br>
Again, this means more realistic simulations.

If you're:
- doing any kind of simulation in time, and\.\.\.
- want realistic solutions, then\.\.\. <br>
**you should probably be thinking about these issues**. <br>
And if you're thinking about these issues, then I hope our work can help you out! 😊 -->

## co-authors

### {% include collaborators/patrick.md %}

## talks

{% include timeline.md %}

<div class="timeline">
  <div class="outer">
    <div class="card">
      <div class="info">
        <h3 class="title">2025</h3>
        <p><ul>
          <li><strong>Invited talk, <em>Brown Unversity</em></strong></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2024</h3>
        <p><ul>
          <li><strong>Internal seminar, <em>Rice University</em></strong></li>
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
