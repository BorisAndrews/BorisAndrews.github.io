---
title: STEFAN–MAXWELL
permalink: /publications/stefan-maxwell/
---

# STRUCTURE-PRESERVING DISCRETISATIONS FOR THE QUASI-INCOMPRESSIBLE, THERMAL MAXWELL–STEFAN EQUATIONS

### Boris Andrews <code>&#124;</code> {% include collaborators/aaron_baier-reinio/short.md %} <code>&#124;</code> {% include collaborators/aaron_brunk/short.md %} <code>&#124;</code> {% include collaborators/patrick/short.md %} <code>&#124;</code> {% include collaborators/maria/short.md %}

### OCT.2026 (arXiv) <code>&#124;</code> In review

> *We study a thermal **Maxwell–Stefan–Navier–Stokes** system modelling **miscible mixtures** under a **quasi-incompressibility constraint**. [...] The first method [...] **guarantees generation of entropy** and **enforces the quasi-incompressibility constraint pointwise** [...]. The second method employs a **continuous Petrov–Galerkin** discretisation in time, which also generates entropy and satisfies the constraint pointwise, and in addition **conserves the total energy** and allows **high-order time approximations**. [...]*

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL ABSTRACT</b>
    <div class="details">
        We study a thermal Maxwell–Stefan–Navier–Stokes system modelling miscible mixtures under a quasi-incompressibility constraint.
        The system consists of the conservation laws for mass and momentum, and the balance law for entropy, which is preferred over the balance law for energy because it facilitates the development of two structure-preserving discretisation methods. <br><br>
        The first method applies a semi-implicit Euler scheme in time, together with suitable finite elements in space, which guarantees generation of entropy and enforces the quasi-incompressibility constraint pointwise, but numerically dissipates total energy.
        The second method employs a continuous Petrov–Galerkin discretisation in time, which also generates entropy and satisfies the constraint pointwise, and in addition conserves the total energy and allows high-order time approximations.
        The structure-preserving properties and behaviour of both numerical methods are demonstrated by a series of numerical experiments.
    </div>
</div>

*(Further details available soon!)*

## CO-AUTHORS

### {% include collaborators/aaron_baier-reinio/full.md %}

### {% include collaborators/aaron_brunk/full.md %}

### {% include collaborators/patrick/full.md %}

### {% include collaborators/maria/full.md %}
