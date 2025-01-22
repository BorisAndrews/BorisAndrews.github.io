---
title: PARKER PROBLEM
permalink: /publications/parker/
---

# TOPOLOGY-PRESERVING DISCRETIZATION FOR THE MAGNETO-FRICTIONAL EQUATIONS ARISING IN THE PARKER CONJECTURE

### {% include collaborators/mingdong/short.md %}, {% include collaborators/patrick/short.md %}, {% include collaborators/kaibo/short.md %}, Boris Andrews

### 20.JAN.2025 ([arXiv](https://doi.org/10.48550/arXiv.2501.11654))

> *[...] This work presents an **energy- and helicity-preserving** finite element discretization for the **magneto-frictional system**, for investigating the **Parker conjecture**. The algorithm **preserves a discrete version of the topological barrier** and a discrete Arnold inequality. [...]*

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL ABSTRACT</b>
    <div class="details">
        The Parker conjecture, which explores whether magnetic fields in perfectly conducting plasmas can develop tangential discontinuities during magnetic relaxation, remains an open question in astrophysics.
        Helicity conservation provides a topological barrier during relaxation, preventing topologically nontrivial initial data relaxing to trivial solutions;
        preserving this mechanism discretely over long time periods is therefore crucial for numerical simulation.
        This work presents an energy- and helicity-preserving finite element discretization for the magneto-frictional system, for investigating the Parker conjecture.
        The algorithm preserves a discrete version of the topological barrier and a discrete Arnold inequality.
        We also discuss extensions to domains with nontrivial topology.
    </div>
</div>

The results of this work are, to me, *tremendously exciting*.
They demonstrate how utterly vital it is, when designing a numerical simulation, that you **preserve your conservation and dissipation laws** from the continuous level to the discrete.

*Magnetic relaxation* is the process by which a magnetic or **magnetohydrodynamic (MHD)** system **converges to its equilibrium/steady state**.
MHD systems are typically long-duration, large-scale plasmas (e.g. the Sun, in particular its corona visible in the photo below) or liquid metals (e.g. the Earth's core).

![solar_corona](assets/img/corona.jpg)

In this work, we develop **accurate numerical simulations** for a certain **magnetic relaxation** model: *the magneto-frictional equations*.

<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>MAGNETO-FRICTIONAL EQUATIONS</b>
    <div class="details">
        The system is given by
        \[
            \dot{\mathbf{B}} + \mathrm{curl}\,\mathbf{E} = \mathbf{0},  \\
            \mathbf{E} + \mathbf{u}\times\mathbf{B} = \mathbf{0},  \\
            \mathbf{j} = \mathrm{curl}\,\mathbf{B},  \\
            \mathbf{u} = \mathbf{j}\times\mathbf{B},
        \]
        where \(\mathbf{E}, \mathbf{B}\) are the electric and magnetic fields (respectively) and \(\mathbf{u}, \mathbf{j}\) are the fluid's internal velocity and current (respectively).
    </div>
</div>

The magneto-frictional equations **conserve** a quantity called the *helicity*, \\(\mathcal{H}\\), and **dissipate** a quantity called the *energy*, \\(\mathcal{E}\\).

<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>DEFINITIONS FOR \(\mathcal{H}, \mathcal{E}\)</b>
    <div class="details">
        \[
            \mathcal{H} \coloneqq \int\mathbf{A}\cdot\mathbf{B},  \qquad
            \mathcal{E} \coloneqq \int\mathbf{B}\cdot\mathbf{B},
        \]
        where \(\mathbf{A}\) is the magnetic potential satisfying \(\mathcal{B} = \mathrm{curl}\,\mathbf{A}\).
    </div>
</div>

If \\(\mathcal{E}\\) ever hits \\(0\\), the system has relaxed to a *trivial steady state*, i.e. the magnetic field has vanished everywhere.
The interest thing however is that **this should never happen**.

A simple inequality, the *Arnold inequality*, says that \\(\mathcal{E}\\) **can not pass below a certain multiple of** \\(\mathcal{H}\\);
since \\(\mathcal{H}\\) is constant, this means \\(\mathcal{E}\\) can never reach \\(0\\).
In the equilibrium state therefore, the **magnetic field should not vanish**.

<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FUN TOPOLOGICAL DIVERSION</b>
    <div class="details">
        This has a neat <em>topological</em> interpretation!
        (Hence <em>"topology-preserving"</em> in the title.) <br>
        The helicity \(\mathcal{H}\) can be interpreted as a continuous analogue of an idea from <b>knot theory</b>: the <em>linking number</em>.
        This represents the number of times a pair of loops winds around the other (1, 2, 3 in the image below). <br><br>
        <img src="assets/img/linking.jpeg" alt="linking_numbers"><br>
        The helicity \(\mathcal{H}\) essentially quantifies how <b>knotted</b> the intial magnetic field is.
        The conservation of \(\mathcal{H}\) implies that magnetic relaxation <b>cannot untie these knots</b>. <br>
        Essentially, the relaxation process should <b>loosen the knots</b>, but <b>not untie them</b>.
    </div>
</div>

While these structures exist on the continuous level, they are not necessarily preserved in the simulation.
In particular, existing numerical schemes typically do not conserve \\(\mathcal{H}\\).

In our work, we construct a numerical scheme that **conserves** \\(\mathcal{H}\\) **exactly**;
compare with the \\(H(\mathrm{div})\\) scheme in the figure below, in which \\(\mathcal{H}\\) converges to \\(0\\).
Together with the Arnold inequality, this ensures \\(\mathcal{E}\\) cannot decay to \\(0\\), and that the magnetic field will not artificially vanish.

![sp_laws](assets/img/sp_laws.jpeg)



[This has a neat topological interpretation, hence *"topology-preserving"* in the title.]

---

The Parker conjecture supposes that ideal magnetic relaxation may develop tangential discontinuities.

---

The [GENERIC formalism](https://en.wikipedia.org/wiki/GENERIC_formalism/) extends Hamiltonian systems to include both:
- a *conserved* energy
- a *non-decreasing* entropy

{% include reveal-box.md %}
<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>FULL DETAILS</b>
    <div class="details">
        The general GENERIC ODE in \(\mathbf{x} : \mathbb{R}_+ \to \mathbb{R}^d\) is
        \[
            \dot{\mathbf{x}}  =  L(\mathbf{x})\nabla E(\mathbf{x}) + M(\mathbf{x})\nabla S(\mathbf{x}).
        \]
        Here, \(E, S : \mathbb{R}^d \to \mathbb{R}\) are the (conserved) energy and (non-decreasing) entropy, and \(L, M : \mathbb{R}^d \to \mathbb{R}^{d\times d}\) are the skew-symmetric (Poisson) matrix and positive-semidefinite (friction) matrix.
        With the following orthogonality conditions,
        \[
            \nabla S(\mathbf{x})^\top L(\mathbf{x}) = 0,  \qquad
            \nabla H(\mathbf{x})^\top M(\mathbf{x}) = 0,
        \]
        the conservation of \(E\) and non-dissipation of \(S\) can be identified by testing against \(\nabla E\) and \(\nabla S\) respectively.
        Extending to PDEs is fiddly (for the introduction of Fréchet derivatives) but similar.
    </div>
</div>

As the name suggests, this is **extremely general**.
Examples of such systems include:
- the *compressible* Navier–Stokes equations
- the Boltzmann equation
- pretty much any *irreversible* thermodynamic system

We can apply the framework from [mine and Patrick Farrell's preprint](/publications/sp-integrators/) to preserve both the **conservative** and **non-dissipation** structures.
As such, we have a *general way to construct structure-preserving finite element methods for any of the above systems*, with arbitrary finite elements and at arbitrary order in space and time.

These properties are **crucial for accurately capturing the dynamics** of these systems.

*(Further details available soon!)*
