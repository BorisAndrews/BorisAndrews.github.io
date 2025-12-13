---
title: SP INTEGRATORS (PART 1)
permalink: /publications/sp-integrators-a/
---

# ENFORCING CONSERVATION LAWS AND DISSIPATION INEQUALITIES NUMERICALLY VIA AUXILIARY VARIABLES

### Boris Andrews <code>&#124;</code> {% include collaborators/patrick/short.md %}

### 29.APR.2025 ([arXiv](https://doi.org/10.48550/arXiv.2407.11904)) <code>&#124;</code> 31.DEC.2025 ([SISC](https://doi.org/10.1137/25M1756673))

{% include highlight-box.md %}
<div class="highlight-box" onclick="window.location.href='https://doi.org/10.1137/25M1756673';"><b>
    CHECK OUT IN SISC!
</b></div>

> *We propose a general strategy for **enforcing multiple conservation laws** and **dissipation inequalities** in the **numerical solution of initial value problems**. [...] We demonstrate these ideas by their application to the **Navier-Stokes equations**. We generalize [...] the **energy-dissipating and helicity-tracking** scheme of Rebholz for the **incompressible** [...] equations, and devise a time discretization of the **compressible** equations that **conserves mass, momentum, and energy, and provably dissipates entropy**.*

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL ABSTRACT</b>
    <div class="details">
        We propose a general strategy for enforcing multiple conservation laws and dissipation inequalities in the numerical solution of initial value problems.
        The key idea is to represent each conservation law or dissipation inequality by means of an associated test function;
        we introduce auxiliary variables representing the projection of these test functions onto a discrete test set, and modify the equation to use these new variables.
        We demonstrate these ideas by their application to the Navier-Stokes equations.
        We generalize to arbitrary order the energy-dissipating and helicity-tracking scheme of Rebholz for the incompressible Navier-Stokes equations, and devise a time discretization of the compressible equations that conserves mass, momentum, and energy, and provably dissipates entropy.
    </div>
</div>

<!-- ***Accurate simulations don't just come from throwing your equations haphazardly into a computer.***
***They require respect for the laws of nature.*** -->

No matter whether you're modelling a fluid, a plasma, any mechanical system, whatever, your partial differential equations (PDEs) almost always possess some fundamental physical structures.
These might be include conserved quantities like **mass**, **momentum**, or **energy**, or dissipated quantites such as (as famously dictated by the *Second Law of Thermodynamics*) **entropy**.

In the ***continuous world***, these laws are mathematical certainties.
Exact solutions to our PDE models must satisfy these laws.

In the ***discrete world*** of numerical simulations, however, they're often the first casualties.
Numerical simulations give approximate solutions;
approximate solutions only necessarily satisfy physical laws approximately.

When a solver fails to respect these invariants, simulations can drift.
They can become unstable.
They can produce physically impossible results, like the coffee in your cup magically generating its own energy and jumping onto your desk.
That's not something you want to just *"accept"* when you're simulating the air flowing past the wings of an aircraft.
Preserving these properties isn't just *"nice to have"*;
it's vital for long-term stability and physical fidelity.

### The challenge

Conserving simple, quadratic quantities (e.g. the $L^2$ energy in Navier–Stokes) is pretty well-understood (in particular in finite element discretisations).
The challenge spikes dramatically when dealing with **non-quadratic quantities of interest**, in particular when there are **multiple such structures**.

Standard time-stepping schemes generally force an unhappy compromise:
- Either accept some drift in your conserved quantities,
- or introduce some *"artificial dissipation"* (a fictious damping force to keep the simulation stable at the cost of accuracy).

Conservative or accurately dissipative PDE integrators have then generally historically been constructed on an *ad-hoc* system-by-system basis.

### The literature to date

If you're familiar with the field, you may know of some of these integrators.
In particular, I'll highlight two disparate bodies of work:
- **Auxiliary variables** (i.e. mixed finite element methods):
These have been effective in preserving the behaviour of multiple quantities of interest, but have struggled with non-quadratic properties.
- **Finite elements in time**:
These have been effective in preserving the behaviour of arbitrary, potentially non-quadratic, quantities of interest, but have generally only been applicable for a single structure to be preserved.

<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>A QUICK NOTE ON FINITE ELEMENTS IN TIME</b>
    <div class="details">
        Our framework relies on finite elements in time, specifically a class of integrators called <b>continuous Petrov-Galerkin (CPG)</b> methods. <br><br>

        Unlike classical Runge–Kutta (RK) methods which treat time as a sequence of discrete points, CPG treats time as a continuous dimension (similar to space in traditional finite elements).
        This works for arbitrary order in time, and in theory is no more computationally difficult than a classical implicit RK method:
        The \(S\)-stage CPG method has no more degrees of freedom than an \(S\)-stage implicit RK method. <br><br>

        To see why CPG is so vital for non-quadratic quantities of interest, you'll just have to read the paper!
    </div>
</div>

Our work unifies these distinct ideas.

<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>A QUICK NOTE ON SYMPLECTIC INTEGRATORS</b>
    <div class="details">
        Symplectic integrators are frequently lauded for their <i>"energy-conserving properties"</i>.
        Their status as the gold standard for simulating Hamiltonian systems is often put down to this. <br><br>

        Yet, this belief is <i>not entirely accurate</i>... <br><br>
        
        Symplecticity enhances the <i>collective</i> behaviour of a group of simulations. This is great!
        If I'm e.g. simulating the motion of a host of example asteroids passing through our solar system, it'd nice to have an accurate prediction about what percent of these might hit Earth. <br><br>

        However, this <b>does not guarantee energy conservation</b>. <br><br>

        In fact, as noted by [<i>Ge and Marsden (1988)</i>](https://doi.org/10.1016/0375-9601(88)90773-6): <br>
        <b><i>Symplectic integrators cannot (in general) conserve energy.</i></b> <br><br>

        <img src="assets/img/ge_marsden.png" alt="ge_marsden_quote">
    </div>
</div>

### Our proposed framework

We introduce a general, arbitrary-order framework that doesn't just give you one integrator;
we provide a **sequence of procedural steps** that allows you to turn pretty much any specific PDE model of your choosing into a **structure-preserving scheme**.
The core innovation is the systematic joint use of **auxiliary variables** and **finite elements in time**.

Here's the key idea:

1. **Quantify the physics:**
For each conservation or dissipation laws you want to preserve, identify a certain *"associated test function"* (explained in more detail in the paper).
2. **Project:**
Make a mixed finite element discretisation by introducing these associated test functions as auxiliary variables (projections of these associated test functions onto the discrete test set).
3. **Discretise in time**:
Discretise in time using finite elements in time.

It's as simple and general as that!
All those existing mixed finite element methods and finite-element-in-time schemes mentioned above for example just turn out actually to be special cases of our wider framework.

### A neat little demo: *compressible Navier–Stokes*

To prove the power of this framework, we applied it to one of the most challenging systems in computational physics:
the **compressible Navier–Stokes equations**.

This is a nasty system with a lot of physically important structures:
* **Mass conservation**
* **Momentum conservation**
* **Energy conservation**
* **Entropy dissipation/generation** *(i.e. the Second Law of Thermodynamics)*

We use our framework to preserve ***all of these properties*** simultaneously.
To our knowledge, this is the first scheme to achieve this in the general setting we consider.

Just to get you excited, here's a fun video of some numerical results from the paper, illustrating a numerical shockwave simulation using our discretisation:

<video controls style="width: 100%; height: auto;">
    <source src="assets/vid/compressible_ns.mp4" type="video/mp4">
    Your browser does not support the video tag.
    Sorry you're missing out on the pretty colours!
</video>

### Ready to upgrade *your* integrator?

If you're looking to build simulations that are both simple and physically meaningful, we invite you to explore the full details of the framework, proofs, and implementation strategies in the manuscript.

<div class="highlight-box" onclick="window.location.href='https://doi.org/10.1137/25M1756673';"><b>
    CHECK OUT IN SISC!
</b></div>

*We would both gladly discuss it further!*
- <a href="mailto:boris.andrews@maths.ox.ac.uk">boris.andrews@maths.ox.ac.uk</a>
- <a href="mailto:patrick.farrell@maths.ox.ac.uk">patrick.farrell@maths.ox.ac.uk</a>

## VIDEOS

Check out Patrick's **Langtangen Seminar** (22.APR.2025) at *[Simula](https://www.simula.no/)* below:

{% include video-container.md %}
<div class="video-container">
    <iframe src="https://www.youtube.com/embed/wfFcZsxicw0" frameborder="0" allowfullscreen></iframe>
</div><br>

His earlier **ACM Colloquium** (13.NOV.2024) at the {% include universities/edinburgh.md %} and {% include universities/heriot-watt.md %} can be found [here](https://media.ed.ac.uk/media/13+11+2024+Patrick+Farrell+%28Oxford%29%3A+Designing+conservative+and+accurately+dissipative+numerical+integrators+in+time/1_o19b1nuj/245536282).

## RELATED WORKS

In a [recently submitted manuscript](/publications/sp-integrators/), {% include collaborators/patrick/short.md %} and I apply these ideas to two very general classes of problems:
- **Arbitrary ODEs with multiple invariants**, for which we construct a general integrator that's able to preserve as many invariants as desired
- **Arbitrary ODEs and PDEs from the GENERIC formalism**, a general class of energy-conserving and entropy-generating system, for which we're similarly able to construct a general integrator that preserves both of these properties

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
