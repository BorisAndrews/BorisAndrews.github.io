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
They demonstrate how vital it is, when designing a numerical simulation, that you **preserve your conservation and dissipation laws** from the continuous level to the discrete.

*Magnetic relaxation* is the process by which a magnetic or **magnetohydrodynamic (MHD)** system **converges to its equilibrium/steady state**.
These systems are typically long-duration, large-scale plasmas (e.g. the Sun, in particular its corona visible in the photo below) or liquid metals (e.g. the Earth's core).

![solar_corona](assets/img/corona.jpg)

In this work, we develop **accurate numerical simulations** for a certain **magnetic relaxation** model: *the magneto-frictional equations*.

<div class="reveal-box" onclick="var details = this.querySelector('.details'); details.style.display = (details.style.display === 'block') ? 'none' : 'block';">
    <b>MAGNETO-FRICTIONAL EQUATIONS</b>
    <div class="details">
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
        where \(\mathbf{A}\) is the magnetic potential satisfying \(\mathbf{B} = \mathrm{curl}\,\mathbf{A}\).
    </div>
</div>

If \\(\mathcal{E}\\) ever hits \\(0\\), the system has necessarily relaxed to a *trivial steady state*, i.e. the magnetic field has just vanished everywhere.
The interest thing however is that **this should never be the case**. <br>
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
        <img src="assets/img/linking.jpeg" alt="linking_numbers"><br><br>
        Essentially, \(\mathcal{H}\) quantifies how <b>knotted</b> the intial magnetic field is.
        The conservation of \(\mathcal{H}\) implies that magnetic relaxation <b>cannot untie these knots</b>. <br>
        It should <b>loosen them</b>, but <b>never untie them</b>.
    </div>
</div>

While these structures exist on the continuous level, they are not necessarily preserved in any old simulation.
In particular, **existing numerical schemes typically do not conserve** \\(\mathcal{H}\\). <br>
In our work, we construct a numerical scheme that **conserves** \\(\mathcal{H}\\) **exactly**;
compare with the \\(H(\mathrm{div})\\) scheme in the figure below, in which \\(\mathcal{H}\\) dissipates to \\(0\\).
Together with the Arnold inequality, this ensures \\(\mathcal{E}\\) cannot decay to \\(0\\)...

![sp_laws](assets/img/sp_laws.jpeg)

...and that the **computed magnetic field will not artificially vanish**!

![field_lines](assets/img/field_lines.jpeg)

I'd like to conclude this by emphasising:
*this is essentially the **first magnetic relaxation simulation that does not artificially dissipate to nothing***. <br>
This means it's the first that can be used to investigate these equations' long-term behaviour.
The *Parker conjecture* supposes that ideal magnetic relaxation may develop tangential discontinuities;
our scheme should prove vital for numerical investigations into its validity.

We hope our work can both **motivate the use of conservative/structure-preserving integrators**, and introduce **numerical discretisations** as a valid tool for **investigations into the Parker conjecture**.

*We would all gladly discuss it further!*
- <a href="mailto:mingdong.he@maths.ox.ac.uk">mingdong.he@maths.ox.ac.uk</a>
- <a href="mailto:patrick.farrell@maths.ox.ac.uk">patrick.farrell@maths.ox.ac.uk</a>
- <a href="mailto:kaibo.hu@ed.ac.uk">kaibo.hu@ed.ac.uk</a>
- <a href="mailto:boris.andrews@maths.ox.ac.uk">boris.andrews@maths.ox.ac.uk</a>

**Note:**
this scheme can be viewed as a special case of my *previous* work with {% include collaborators/patrick/short.md %}, on [general constructions for conservative finite element integrators](/publications/sp-integrators/).

## Co-authors

### {% include collaborators/mingdong/full.md %}

### {% include collaborators/patrick/full.md %}

### {% include collaborators/kaibo/full.md %}
