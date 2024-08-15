---
title: sp.integrators
permalink: /publications/sp-integrators/
---

# high-order conservative and accurately dissipative numerical integrators via auxiliary variables

### boris.d.andrews, [patrick.e.farrell](https://pefarrell.org/)

### 16.jul.2024 ([arXiv](https://doi.org/10.48550/arXiv.2407.11904))

> *[...] we propose an approach for the construction of **timestepping schemes** that **preserve dissipation laws** and **conserve multiple general invariants**, via finite elements in time and the systematic introduction of auxiliary variables. [...] We [devise] novel arbitrary-order schemes that conserve to machine precision **all known invariants of Hamiltonian ODEs** [...] and arbitrary-order schemes for the **compressible Navier–Stokes equations that conserve mass, momentum, and energy, and provably possess non-decreasing entropy**.*

Symplectic integrators are often praised for their "energy-conserving properties". There's an idea that they're the **gold standard** for simulating Hamiltonian systems because they conserve energy.
This is* a misconception (*in general).

**Symplecticity** = A technical criteria improving the group behaviour of a collection of simulations. This is great…
…but, it **doesn't guarantee energy conservation**.
In fact, we must choose:
> *Symplectic integrators can't conserve energy.*
— 📄 Ge, Marsden (1988)

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
          <li><strong>invited talk, <em>brown unversity</em></strong></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2024</h3>
        <p><ul>
          <li><strong>internal seminar, <em>rice university</em></strong></li>
          <li>pdesoft, <em>university of cambridge</em></li>
          <li>finite element fair, <em>university college london</em></li>
          <li><strong>exploiting algebraic and geometric structure in time-integration methods workshop, <em>university of pisa</em></strong></li>
          <li>ukaea phd student engagement day, <em>ccfe</em></li>
          <li>junior applied mathematics seminar, <em>university of warwick</em></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2023</h3>
        <p><ul>
          <li><strong>ICIAM 2023, <em>waseda university</em></strong></li>
          <li>numerical analysis group internal seminar, <em>university of oxford</em></li>
          <li>junior applied mathematics seminar, <em>university of oxford</em></li>
          <li>met office presentation, <em>university of oxford</em></li>
        </ul></p>
      </div>
    </div>
  </div>
</div>
