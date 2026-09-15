---
title: ENSTROPHY
permalink: /publications/enstrophy/
---

# STRONGLY ENSTROPHY-STABLE INTEGRATORS FOR THE INCOMPRESSIBLE NAVIER–STOKES EQUATIONS

### Boris Andrews <code>&#124;</code> {% include collaborators/matin/short.md %} <code>&#124;</code> {% include collaborators/patrick/short.md %}

### SEP.2026 ([arXiv](https://doi.org/10.48550/arXiv.2609.15520)) <code>&#124;</code> In review ({% include journals/focm.md %})

{% include highlight-box.md %}
<div class="highlight-box" onclick="window.location.href='https://doi.org/10.48550/arXiv.2609.15520';"><b>
    CHECK OUT ON ARXIV!
</b></div>

> *We propose a mixed finite element discretisation for the incompressible Navier–Stokes equations that **preserves the evolution laws of both energy and enstrophy** [...]. In two dimensions, [this leads] to a **Reynolds-number-independent bound on the velocity gradient** that naturally **stabilises the scheme**, even on severely under-resolved meshes. In three dimensions, the scheme preserves both dissipation and the **generation of enstrophy through vortex stretching**. [...]*

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL ABSTRACT</b>
    <div class="details">
        We propose a mixed finite element discretisation for the incompressible Navier–Stokes equations that preserves the evolution laws of both energy and enstrophy, in a stronger sense than previous discretisations.
        In two dimensions, the evolution law for enstrophy only permits dissipation for thermodynamically isolated systems, leading to a Reynolds-number-independent bound on the velocity gradient that naturally stabilises the scheme, even on severely under-resolved meshes.
        In three dimensions, the scheme preserves both dissipation and the generation of enstrophy through vortex stretching. <br><br>
        We enforce these evolution laws by systematically introducing auxiliary variables into the discretisation.
        While conforming implementations of these schemes require discrete Stokes complexes with enhanced regularity, we introduce both (i) equivalent reparametrisations and (ii) penalty formulations that require only the typical curl- and div-conforming spaces from the standard discrete de Rham complex.
        The scheme handles different types of boundary conditions and curved domains.
        The robust stabilisation properties of the proposed scheme are demonstrated through numerical simulations of a shear flow, a spherical vortex, and flow past an obstacle.
        We observe numerically that preserving the discrete evolution of enstrophy in this way has a strong stabilising effect on the numerical solution, especially in two dimensions.
    </div>
</div>

*(Further details available soon!)*

## RELATED WORKS

This represents a particularly exciting **application of my earlier work** with {% include collaborators/patrick/short.md %}, on [general constructions for conservative and dissipative finite element integrators](/publications/sp-integrators-a/), using the ideas to help in stabilisation efforts at high Reynolds numbers.

## RELATED OPEN PROBLEMS

{% include open-problems/title.md %}
{% include open-problems/all/roms.md %}

## CO-AUTHORS

### {% include collaborators/matin/full.md %}

### {% include collaborators/patrick/full.md %}

## VIDEOS

Check out my talk at the {% include conferences/2026/esi.md %} at the {% include organisations/esi/full.md %} within the {% include universities/vienna.md %} (MAY.2026) below:

{% include video-container.md %}
<div class="video-container">
    <iframe src="https://www.youtube.com/embed/yi4hbj7jGeQ" frameborder="0" allowfullscreen></iframe>
</div><br>

## TALKS

{% include timeline.md %}

<div class="timeline">
  <div class="outer">
    <div class="card">
      <div class="info">
        <h3 class="title">2026</h3>
        <p><ul>
          <li>SciCADE, <em>University of Edinburgh</em></li>
          <li>Programme on Differential Complexes, <em>Erwin Schrödinger International Institute (ESI), Vienna</em></li>
          <li>Workshop on Finite Element Tensor Calculus, <em>Tsinghua University</em></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2025</h3>
        <p><ul>
          <li>Numerical Analysis Group Internal Seminar, <em>University of Oxford</em></li>
          <li>ACOMEN, <em>Ghent University</em></li>
          <li>ECCOMAS MFET, <em>Aachen, Germany</em></li>
        </ul></p>
      </div>
    </div>
  </div>
</div>
