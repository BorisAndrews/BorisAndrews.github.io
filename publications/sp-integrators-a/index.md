---
title: SP INTEGRATORS (PART 1)
permalink: /publications/sp-integrators-a/
---

# ENFORCING CONSERVATION LAWS AND DISSIPATION INEQUALITIES NUMERICALLY VIA AUXILIARY VARIABLES

### Boris Andrews <code>&#124;</code> {% include collaborators/patrick/short.md %}

### 29.APR.2025 ([arXiv](https://doi.org/10.48550/arXiv.2407.11904))

{% include highlight-box.md %}
<div class="highlight-box" onclick="window.location.href='/publications/sp-integrators';">
    THIS REPRESENTS PART 1 OF AN EARLIER MANUSCRIPT, CURRENTLY BEING PARTITIONED INTO MULTIPLE SUBMISSIONS <br>
    <b>CLICK HERE TO CHECK IT OUT!</b>
</div>

> *We propose a general strategy for **enforcing multiple conservation laws** and **dissipation inequalities** in the **numerical solution of initial value problems**. [...] We demonstrate these ideas by their application to the **Navier-Stokes equations**. We generalize [...] the **energy-dissipating and helicity-tracking** scheme of Rebholz for the **incompressible** [...] equations, and devise the first time discretization of the **compressible** equations that **conserves mass, momentum, and energy, and provably dissipates entropy**.*

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL ABSTRACT</b>
    <div class="details">
        We propose a general strategy for enforcing multiple conservation laws and dissipation inequalities in the numerical solution of initial value problems.
        The key idea is to represent each conservation law or dissipation inequality by means of an associated test function;
        we introduce auxiliary variables representing the projection of these test functions onto a discrete test set, and modify the equation to use these new variables.
        We demonstrate these ideas by their application to the Navier-Stokes equations.
        We generalize to arbitrary order the energy-dissipating and helicity-tracking scheme of Rebholz for the incompressible Navier-Stokes equations, and devise the first time discretization of the compressible equations that conserves mass, momentum, and energy, and provably dissipates entropy.
    </div>
</div>

In my [earlier work](/publications/sp-integrators/) with {% include collaborators/patrick/short.md %}, we proposed a framework for the construction of **finite-element integrators** that **preserve multiple conservation laws** and **dissipation inequalities**, alongside various applications to different PDE systems.
This preprint serves as **part 1** of a partition of this work.

We re-establish the framework, including alongside the discussions of its applications to the **Navier–Stokes equations**, deriving *(to arbitrary order)* integrators that:
- for the **incompressible** equations, *dissipate energy* and, in the ideal case, *conserve helicity*;
- for the **compressible** equations, *conserve mass, momentum and energy* and *generate entropy*.

For further details, check out my earlier manuscript [here](/publications/sp-integrators/).

## VIDEOS

Check out Patrick's **Langtangen Seminar** on our work at *[Simula](https://www.simula.no/)* here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/wfFcZsxicw0" frameborder="0" allowfullscreen></iframe><br>

## RELATED WORKS

As stated above, this work represents part 1 of a resubmission of an [earlier manuscript](/publications/sp-integrators/) with {% include collaborators/patrick/short.md %}, partitioned into multiple parts.

For a neat and related application of these ideas to a problem in **magnetic relaxation** that really highlights their importance, check out my subsequent work with {% include collaborators/mingdong/short.md %}, {% include collaborators/patrick/short.md %} & {% include collaborators/kaibo/short.md %}, on [structure-preserving integrators for the magneto-frictional equations](/publications/parker/).

## RELATED OPEN PROBLEMS

{% include open-problems/title.md %}
{% include open-problems/all/viscoelastic.md %}
{% include open-problems/all/compressible-mhd.md %}

## CO-AUTHORS

### {% include collaborators/patrick/full.md %}

## TALKS

{% include timeline.md %}

<div class="timeline">
  <div class="outer">
    <div class="card">
      <div class="info">
        <h3 class="title">2025</h3>
        <p><ul>
          <li>Biennial Numerical Analysis Conference, <em>University of Strathclyde</em></li>
          <li>Numerical Analysis Group internal seminar, <em>University of Oxford</em></li>
          <div style="text-align: center; padding: 10px 0;"><strong>⬆️ UPCOMING | PAST ⬇️</strong></div>
          <li><strong>Numerical Mathematics & Scientific Computing seminar, <em>Rice University</em></strong></li>
          <li><strong>SIAM CSE, <em>Fort Worth, Texas</em></strong></li>
          <li><strong>Scientific Computing seminar, <em>Brown Unversity</em></strong></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2024</h3>
        <p><ul>
          <li>External ("tiny desk") seminar, <em>Rice University</em></li>
          <li>Computing Division technical meeting, <em>UKAEA</em></li>
          <li>Firedrake User Meeting, <em>University of Oxford</em></li>
          <li>PDEsoft, <em>University of Cambridge</em></li>
          <li>Finite Element Fair, <em>University College London (UCL)</em></li>
          <li><strong>Exploiting Algebraic and Geometric Structure in Time-integration Methods workshop, <em>University of Pisa</em></strong></li>
          <li>UKAEA PhD student engagement day, <em>UKAEA</em></li>
          <li>Junior Applied Mathematics Seminar, <em>University of Warwick</em></li>
        </ul></p>
      </div>
    </div>
    <div class="card">
      <div class="info">
        <h3 class="title">2023</h3>
        <p><ul>
          <li><strong>ICIAM, <em>Waseda University</em></strong></li>
          <li>Numerical Analysis Group internal seminar, <em>University of Oxford</em></li>
          <li>Junior Applied Mathematics Seminar, <em>University of Oxford</em></li>
          <li>Met Office presentation, <em>University of Oxford</em></li>
        </ul></p>
      </div>
    </div>
  </div>
</div>
