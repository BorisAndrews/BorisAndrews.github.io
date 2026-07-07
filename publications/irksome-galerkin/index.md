---
title: IRKSOME GALERKIN
permalink: /publications/irksome-galerkin/
---

# AUTOMATED GALERKIN TIME STEPPING IN IRKSOME

### Boris Andrews <code>&#124;</code> {% include collaborators/pablo/short.md %} <code>&#124;</code> {% include collaborators/patrick/short.md %} <code>&#124;</code> {% include collaborators/rob/short.md %} <code>&#124;</code> {% include collaborators/scott/short.md %}

### JUN.2026 ([arXiv](https://doi.org/10.48550/arXiv.2606.27300)) <code>&#124;</code> In review ({% include journals/sisc.md %})

{% include highlight-box.md %}
<div class="highlight-box" onclick="window.location.href='https://doi.org/10.48550/arXiv.2606.27300';"><b>
    CHECK OUT ON ARXIV!
</b></div>

> *[...] we present automation in **Irksome** for both **discontinuous Galerkin** and **continuous Petrov–Galerkin** time stepping of semidiscrete variational problems. The implementation supports auxiliary variables, flexible temporal quadrature, and monolithic algebraic solvers, and it enables switching between Runge–Kutta and Galerkin-in-time formulations with **minimal changes to user code**. [...]*

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL ABSTRACT</b>
    <div class="details">
        As the study of temporal and spatial discretization schemes continues to advance, recent work has focused on the use of Galerkin-in-time discretization schemes that enable broader structure-preservation than is known for Runge–Kutta integrators. While the promise of such discretizations is immense, their realization has, until now, generally relied on bespoke implementations that have limited their wider use. <br><br>
        In this work, we present automation in Irksome for both discontinuous Galerkin and continuous Petrov–Galerkin time stepping of semidiscrete variational problems. The implementation supports auxiliary variables, flexible temporal quadrature, and monolithic algebraic solvers, and it enables switching between Runge–Kutta and Galerkin-in-time formulations with minimal changes to user code. Numerical examples illustrate accuracy, solver performance, and structure preservation across representative PDE systems.
    </div>
</div>

[Irksome](https://github.com/firedrakeproject/Irksome) is a time-stepping library for [Firedrake](https://www.firedrakeproject.org/).
Its core design principle is that the user supplies only a *semidiscrete variational form*;
Irksome then handles the time discretisation automatically via manipulation of the [Unified Form Language (UFL)](https://github.com/FEniCS/ufl).
The original Irksome papers showed how to automate a broad class of **Runge–Kutta (RK)** methods at this abstract level, requiring essentially no changes to user code.

This paper extends that abstraction to **Galerkin-in-time** discretisations:
both **discontinuous Galerkin (DG)** and **continuous Petrov–Galerkin (CPG)** in time.
Switching between RK, DG and CPG typically requires changing only a *single line of code*.

### Why Galerkin-in-time?

RK methods face fundamental barriers in structure preservation:
they generally cannot conserve non-quadratic invariants or preserve non-quadratic dissipation inequalities.
DG and CPG in general methods do not have these limitations.
In particular, CPG with suitably chosen **auxiliary variables** can preserve multiple conservation and dissipation laws simultaneously (the approach taken in my [earlier work](/publications/sp-integrators-a/) with {% include collaborators/patrick/short.md %}).
General-purpose implementations of DG and CPG time stepping have not previously existed;
this work fills that gap within the Firedrake ecosystem.

<div class="highlight-box" onclick="window.location.href='https://doi.org/10.48550/arXiv.2606.27300';"><b>
    CHECK OUT ON ARXIV!
</b></div>

## TALKS

{% include timeline.md %}

<div class="timeline">
<div class="outer">
    <div class="card">
      <div class="info">
        <h3 class="title">2026</h3>
        <p><ul>
          <li>Firedrake User Meeting, <em>University of Oxford</em></li>
        </ul></p>
      </div>
    </div>
  </div>
</div>

## CO-AUTHORS

### {% include collaborators/pablo/full.md %}

### {% include collaborators/patrick/full.md %}

### {% include collaborators/rob/full.md %}

### {% include collaborators/scott/full.md %}
