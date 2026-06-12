---
title: GEOMETRIC FLOWS
permalink: /publications/geometric-flows/
---

# ARBITRARY-ORDER STRUCTURE-PRESERVING DISCRETIZATIONS FOR GEOMETRIC CURVATURE FLOWS

### {% include collaborators/ganghui/short.md %} <code>&#124;</code> Boris Andrews <code>&#124;</code> {% include collaborators/patrick/short.md %}

### 19.MAY.2026 ([arXiv](https://doi.org/10.48550/arXiv.2605.20371)) <code>&#124;</code> In review ({% include journals/sisc.md %})

{% include highlight-box.md %}
<div class="highlight-box" onclick="window.location.href='https://doi.org/10.48550/arXiv.2605.20371';"><b>
    CHECK OUT ON ARXIV!
</b></div>

> *[...] we present the first discretization of **geometric curvature flows** [...] that **preserves the evolution of area and volume** at **arbitrary order in space and time**. The key idea is to introduce **auxiliary variables** in a particular way so that the derivation of the area dissipation law can be replicated after discretization with continuous Petrov–Galerkin in time. [...] The proposed scheme also **preserves mesh quality** in the same manner as the **minimal deformation rate** strategy. [...]*

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL ABSTRACT</b>
    <div class="details">
        Geometric flows, where an immersed manifold evolves in time according to its own geometry, exhibit important structural properties.
        For example, surface diffusion dissipates surface area while conserving volume;
        it is desirable to preserve these properties on discretization.
        This has motivated a substantial body of research on structure-preserving discretizations for these flows, albeit at low order in time. <br><br>
        In this work, we present the first discretization of geometric curvature flows (curve shortening/mean curvature flow and curve/surface diffusion) that preserves the evolution of area and volume at arbitrary order in space and time.
        The key idea is to introduce auxiliary variables in a particular way so that the derivation of the area dissipation law can be replicated after discretization with continuous Petrov–Galerkin in time.
        These auxiliary variables are indicated by a general strategy for structure-preservation in time that applies to many other problems.
        The proposed scheme also preserves mesh quality in the same manner as the minimal deformation rate strategy.
        We demonstrate its structure-preserving properties and high-order convergence on several benchmark examples.
    </div>
</div>

Two of the most prominent examples of geometric flows (equations governing the evolution of surfaces driven solely by their own geometry) are:
- **mean curvature flow (MCF)**, in which a surface shrinks in the direction of its curvature;
- **surface diffusion (SD)**, in which a surface evolves to minimise its area while preserving the enclosed volume (like a soap bubble relaxing to a sphere).

Both flows satisfy fundamental structural properties:
- MCF and SD **dissipate area**.
- SD additionally **conserves enclosed volume**.

For reliable long-time simulation, it is desirable that numerical discretizations inherit these properties exactly, i.e. the discretisation be structure-preserving.
Structure preservation for geometric flows has attracted a rich body of work.
This paper presents the **first structure-preserving discretization** of MCF and SD that achieves **arbitrary order in both space and time**.

### The mesh quality problem

A crucial obstacle in geometric flow simulation is preventing **mesh distortion**.

On the continuous level, the evolution is entirely normal;
that is, *normal* in the geometric sense:
tangential velocity is redundant and unspecified.
In a spatial discretization, however, tangential motion redistributes mesh nodes;
left unchecked, a bad choice of tangential motion can degrades mesh quality significantly.

The **minimal deformation rate (MDR)** strategy ([Hu & Li, 2022](https://doi.org/10.1007/s00211-022-01309-9)) addresses this by choosing the tangential motion to minimise a certain *deformation energy* ($\int_{\mathcal{M}} \|\nabla_{\mathcal{M}} \dot{\mathbf{X}}\|^2$) modelling the rate at which the mesh quality degrades.
This is known to give vastly improved mesh quality comparable to classical method, but at the cost of the stability in area and volume.

### Our approach: auxiliary variables

The key insight is that are and volume stability can be re-introduced to the MDR discretisations of MCF and SD via:
- the systematic introducion of **auxiliary variables**, and
- a special kind of time discretisation called **continuous Petrov–Galerkin (CPG)**.

This yields fully discrete, structure-preserving discretisations for MCF and SD at **arbitrary polynomial orders** in space and time;
in particular, we impose practically no restrictions on the finite element spaces used.
This strategy (using auxiliary variables and CPG to replicate structure-preservation proofs after discretization) is taken directly from my **general framework** with {% include collaborators/patrick/short.md %}, described in an [earlier companion paper](/publications/sp-integrators-a/)

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>THE SCHEMES IN BRIEF</b>
    <div class="details">
        Over a given timestep $T_n$, the $s$-stage MCF discretisation is defined as follows:
        Find $\mathbf{X} \in \mathbb{P}_s(T_n; \mathbb{V}^d)$ satisfying initial data, and $(p, \mathbf{R}, \kappa) \in \mathbb{P}_{s-1}(T_n; \mathbb{V} \times \mathbb{V}^d \times \mathbb{V})$, satisfying: <br><br>

        $$\int_{T_n} (\dot{\mathbf{X}} \cdot \mathbf{n},\, y)_{\mathcal{M}} = -\int_{T_n} (\kappa,\, y)_{\mathcal{M}},$$
        $$\int_{T_n} \big[(\nabla_{\mathcal{M}} \dot{\mathbf{X}},\, \nabla_{\mathcal{M}} \mathbf{Q})_{\mathcal{M}} + (p\mathbf{n},\, \mathbf{Q})_{\mathcal{M}}\big] = 0,$$
        $$\int_{T_n} (\mathbf{R} \cdot \mathbf{n},\, \sigma)_{\mathcal{M}} = 0,$$
        $$\int_{T_n} \big[(\nabla_{\mathcal{M}} \mathbf{R},\, \nabla_{\mathcal{M}} \mathbf{\Lambda})_{\mathcal{M}} + (\kappa\,\mathbf{n},\, \mathbf{\Lambda})_{\mathcal{M}}\big] = -\int_{T_n} (\nabla_{\mathcal{M}} \mathbf{X},\, \nabla_{\mathcal{M}} \mathbf{\Lambda})_{\mathcal{M}},$$

        for all $(y, \mathbf{Q}, \sigma, \mathbf{\Lambda}) \in \mathbb{P}_{s-1}(T_n; \mathbb{V} \times \mathbb{V}^d \times \mathbb{V} \times \mathbb{V}^d)$. <br><br>

        The MDR tangential motion is encoded in the $p$ variable.
        The auxiliary variables $(\kappa, \mathbf{R})$ are introduced to preserve are dissipation;
        for further motivation for the introduction of these variables, see the manuscript. <br><br>
        
        The SD scheme is practically identical, the difference being a modified first equation in which $(\nabla_{\mathcal{M}} \kappa,\, \nabla_{\mathcal{M}} y)_{\mathcal{M}}$ replaces $(\kappa, y)_{\mathcal{M}}$.
        Volume conservation follows immediately from testing with $y = 1$.
    </div>
</div>

At the semi-discrete level, our formulation coincides with the very recently proposed *dual-MDR* scheme of [Gao, Li & Tang (2026)](https://doi.org/10.48550/arXiv.2604.18288).
The key innovations in our work lie in:
- the CPG time discretization, which carries the structure-preserving properties through to arbitrary order, and
- the construction through the [general framework for structure-preserving discretisations](/publications/sp-integrators-a/), which we believe will extend beyond MCF and SD in the future.

### Numerical results

Several benchmark problems in the manuscript confirm both the structure-preserving properties and the expected convergence rates.
Here's something that's not in the manuscript though:
A video of SD on an $8 \times 1 \times 1$ cuboid.

<video controls style="width: 100%; height: auto;">
    <source src="assets/vid/cuboid.mp4" type="video/mp4">
    It doesn't appear your browser supports the video tag, sorry!
</video><br>

<div class="highlight-box" onclick="window.location.href='https://doi.org/10.48550/arXiv.2605.20371';"><b>
    CHECK OUT ON ARXIV!
</b></div>

*We would gladly discuss it further!*
- <a href="mailto:ganghui.zhang@polyu.edu.hk">ganghui.zhang@polyu.edu.hk</a>
- <a href="mailto:boris.andrews@maths.ox.ac.uk">boris.andrews@maths.ox.ac.uk</a>
- <a href="mailto:patrick.farrell@maths.ox.ac.uk">patrick.farrell@maths.ox.ac.uk</a>

## RELATED WORKS

This paper represents an application of the **auxiliary variable framework** for structure-preserving time discretisations introduced in [my earlier paper](/publications/sp-integrators-a/) with {% include collaborators/patrick/short.md %}.

## CO-AUTHORS

### {% include collaborators/ganghui/full.md %}

### {% include collaborators/patrick/full.md %}
