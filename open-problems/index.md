---
title: OPEN PROBLEMS
permalink: /open-problems/
---

# OPEN PROBLEMS & REWARDS

### a.k.a. Boris's BIG brainteasers

Welcome to my **open problems**!
This list collates all the big questions that have found there way onto my paper/whiteboard during my research, that I:
- Have decided not to tackle *(for the time being)*;
- Would be very keen to see solved.

Please do [let me know](https://www.maths.ox.ac.uk/user/10859/contact) if you're interested in any of these/currently working on something similar;
I would love to hear from you!

I've asigned to each of these a score for **difficulty** *(highly subjective)* and my own **personal interest in the question being resolved** *(also highly subjective)*.
This is rated in stars, going from {% include stars/1.md %} to {% include stars/5.md %};
dependent on the star rating in question, I'll buy you something *(ranging from maybe <span style="color: #4C72B0;">a coffee</span> to <span style="color: #C44E52;">dinner</span>)* next time we meet in-person if you manage to solve any of them!
*(Consider it a more hip version of the Fields medal.)*

<!-- IDEAS:

Does enstrophy tracking actually mean anything for the regularity of solutions in 3D? -->

<br>

{% include open-problems/title.md %}
{% include open-problems/all/conservative-pdes.md %}
{% include open-problems/all/dissipative-odes.md %}
{% include open-problems/all/maximum-principles.md %}
{% include open-problems/all/drifts.md %}
{% include open-problems/all/lvpp.md %}
{% include open-problems/all/sdes.md %}
{% include open-problems/all/adiabatic.md %}
{% include open-problems/all/superconvergence.md %}
{% include open-problems/all/5-field.md %}
{% include open-problems/all/collocation.md %}
{% include open-problems/all/viscoelastic.md %}
{% include open-problems/all/delay-des.md %}
{% include open-problems/all/lie-groups.md %}
{% include open-problems/all/roms.md %}
{% include open-problems/all/compressible-mhd.md %}

<br>

---

<div style="text-align: center;">
  <h2>{% include stars/5.md %}</h2>
</div>

---

<br>

### Conservative integrators for PDEs with arbitrarily many invariants {#conservative-pdes}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/3.md %}

In my [work on conservative integrators through auxiliary variables](/publications/sp-integrators/), I derived an integrator for general conservative ODEs that conserves arbitrarily many invariants.
This is very cool!
However, when this idea is applied to PDEs in semidiscrete form, the resultant discretisations destroy the locality of the variational formulation, ruining the sparsity of the assembled problem and rendering the integrator effectively useless.

> *Adapt my scheme to give an integrator for general conservative PDEs that conserves arbitrarily many invariants; in particular, the discretised variational form must be local in space.*

One might consider for example the [Korteweg–De Vries equation](https://en.wikipedia.org/wiki/Korteweg%E2%80%93De_Vries_equation), which, while having infinitely many invariants, it seems difficult to conserve any more than 2.

---

### Dissipative integrators for ODEs with arbitrarily many dissipated quantities {#dissipative-odes}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/3.md %}

Again, in my [work on conservative integrators through auxiliary variables](/publications/sp-integrators/), I derived an integrator for general conservative ODEs that conserves arbitrarily many invariants.
While the results of the manuscript further extend to dissipated quantities, the scheme in question does not, and it's not at all obvious how to extend it as such.

> *Adapt my scheme to give an integrator for general ODEs that preserves arbitrarily many dissipation inequalities.*

All the better if you manage to dissipate arbitrarily many such quantities for PDEs in the process!

---

### Discrete maximum principles via the [auxiliary variable framework](/publications/sp-integrators/) {#maximum-principles}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/3.md %}

Maximum (and minimum) principles can typically be proven by variational identites (e.g. by testing against \\(\text{min}(u, 0)\\))
[My work on structure-preserving integrators](/publications/sp-integrators/) gives a general framework for preserving conservation and dissipation laws by preserving variational identities.
It seems that one would be able, however the piece adamantly refuse to fall into place.

> *Show by example that auxiliary variables may be used to derive numerical integrators for PDEs that exhibit discrete maximum principles.*

Many thanks to {% include collaborators/yohance/short.md %} for useful discussions and insights here.
I hope they come to fruition!
This ties in with the [open problem on the latent variable proximal point algorithm](#lvpp).

<br>

---

<div style="text-align: center;">
    <h2>{% include stars/4.md %}</h2>
</div>

---

<br>

### Preservation of [guiding centre drifts](https://en.wikipedia.org/wiki/Guiding_center) through [auxiliary variables](/publications/sp-integrators/) {#drifts}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/2.md %}

In an [upcoming preprint](/publications/ap-integrators/), I adapt my [auxiliary variable framework](/publications/sp-integrators/) to the preservation of the magnetic moment of a charged particle as an adiabatic invariant.
This is exciting, but in practice the structure of interest for such simulations is the preservation of [guiding centre](https://en.wikipedia.org/wiki/Guiding_center) drifts.

> *Using auxiliary variables, construct an asymptotic-preserving integrator for charged particles that preserves energy conservation, adiabatic invariance of the magnetic moment, and guiding centre drifts; this must be done in a natural way that is uniformly accurate in the magnetic field strength.*

I'm letting "a natural way" do a lot of heavy lifting here, a term that I am leaving 100% up to my own jurisdiction.
There are a lot of very nasty "quick fixes" in the particle-pusher literature, and I really believe there's an elegant way to do this.

---

### Connections between the [latent variable proximal point (LVPP) algorithm](https://doi.org/10.48550/arXiv.2503.05672) and my [auxiliary variable framework](/publications/sp-integrators/) {#lvpp}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/3.md %}

The [LVPP algorithm](https://doi.org/10.48550/arXiv.2503.05672) uses auxiliary variables to improve the behaviour of an iterative algorithm.
My [auxiliary variable framework](/publications/sp-integrators/) uses auxiliary variables to improves the behaviour of an iterative algorithm (except in this case that iterative algorithm is a timestepping scheme).

> *Uncover a meaningful connection between the LVPP algorithm and my auxiliary variable framework.*

I've been search here for years, and I really think there is something here!
I'd be interested to see any way in which the two can be related which leads to new insights/improved algorithms.
This ties in with the [open problem on discrete maximum principles](#maximum-principles).

---

### Extension of the [auxiliary variable framework](/publications/sp-integrators/) to [SDEs](https://en.wikipedia.org/wiki/Stochastic_differential_equation) {#sdes}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/3.md %}

[Itô's lemma](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma) gives an identity for the [SDE](https://en.wikipedia.org/wiki/Stochastic_differential_equation) satisfied by a function of a stochastic process.
The auxiliary variables introduced by [my framework](/publications/sp-integrators/) are simply gradients (or at least, projections thereof), whereas it appears those that would be needed to preserve the SDEs deriving from Itô's lemma would need to be in some way stochastic?

> *Apply my auxiliary variable framework to preserve a meaningful and non-trivial stochastic conservation/dissipation structure for an SDE.*

I don't know much about SDE integrators, so this a little outside my remit.
It could very well be possible though, just might need some outside-the-box thinking!

<br>

---

<div style="text-align: center;">
    <h2>{% include stars/3.md %}</h2>
</div>

---

<br>

### Extension of the [auxiliary variable framework](/publications/sp-integrators/) to general adiabatic invariants {#adiabatic}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/1.md %}

Again, in an [upcoming preprint](/publications/ap-integrators/), I adapt my [auxiliary variable framework](/publications/sp-integrators/) to the preservation of the magnetic moment of a charged particle as an adiabatic invariant.

> *Apply my auxiliary variable framework to preserve general adiabatic invariants.*

It seems to me, on the surface at least, that the construction and ideas in the preprint could very well be generalised to arbitrary invariants.

---

### Superconvergence of the [auxiliary variable framework](/publications/sp-integrators/) {#superconvergence}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/2.md %}

In the analysis in my [auxiliary variable framework](/publications/sp-integrators/) preprint, we show that our scheme has \\(\mathcal{O}[\Delta t^s]\\) convergence, however in practice we observe \\(\mathcal{O}[\Delta t^{2s}]\\) superconvergence at timesteps.

> *Complete the proof of convergence for the auxiliary variable framework, and show superconvergence holds (under sufficient regularity conditions, of course).*

I fully expect the classical superconvergence result to hold.
The only obstacle, I believe, is my lack of knowledge about proving such results for CPG integrators!

---

### 5-field vs. [4-field](/publications/parker/) helicity-preserving finite element discretisations for magnetic relaxation {#five-field}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/2.md %}

Ok, you'll have to stick with me here cause this one's a long explanation...

In my recent preprint on [helicity-preserving integrators in MHD](/publications/parker/), we propose a helicity-preserving 4-field \\(\mathbf{B}_h, \mathbf{E}_h, \mathbf{H}_h, \mathbf{j}_h\\) discretisation for the magneto-frictional equations;
the field \\(\mathbf{H}_h\\) is a projection of \\(\mathbf{B}_h\\) onto a different finite element space, and \\(\mathbf{j}_h\\) a projection of \\(\mathrm{curl}\,\mathbf{B}_h\\).
This has the exciting property that, in the limit, it exhibits a non-trivial field configuration for which everywhere \\(\mathbf{H}_h\times\mathbf{j}_h = \mathbf{0}\\), mimicking the result on the continuous level wherein, in the limit, \\(\mathbf{B}\times\mathrm{curl}\,\mathbf{B} = \mathbf{0}\\)!
I have a hunch however, that this isn't the wonderous result it may appear on the surface.
My fear is that, while in the continuous setting the set of field configurations such that \\(\mathbf{B}\times\mathrm{curl}\,\mathbf{B} = \mathbf{0}\\) may be rich and infinite-dimensional, the discrete condition \\(\mathbf{H}_h\times\mathbf{j}_h = \mathbf{0}\\) might only admit a manifold of very limited dimension.
This would be a disaster if so.
The effect would be that, effectively, our discretisation could accuratively reproduce the long-time behaviour of the actual magneto-frictional equations 0% of the time.

Now, without much trouble, one can readily define a 5-field \\(\mathbf{B}_h, \mathbf{E}_h, \mathbf{H}_h, \mathbf{j}_h, \mathbf{u}_h\\) formulation without breaking any of the structures;
the field \\(\mathbf{u}_h\\) is a projection of \\(\mathbf{H}_h\times\mathbf{j}_h\\).
Solutions to this scheme would satisfy, in the limit, \\(\mathbf{u}-h = \mathbf{0}\\), which should admit a much richer space of possible solutions!

> *Back up my hunch; show that a 5-field helicity-preserving discretisation of the magneto-frictional equation exhibits a richer space of dynamics in the long time limit, either through example or (ideally) proof.*

Hardest part about this is trying to figure out what on Earth I'm talking about.

---

### Extension of the [auxiliary variable framework](/publications/sp-integrators/) to time discretisations beyond collocation RK methods {#collocation}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/2.md %}

The [auxiliary variable framework](/publications/sp-integrators/) gives a methodology for modifying certain classes of time discretisations to be structure-preserving, including collocation RK methods, and CPG.
There are, however, a vast world of RK methods that are not collocation RK methods:- RK4 and multi-step methods to name but a few.

> *Extend the auxiliary variable framework to allow for the structure-preserving modification of RK methods beyond collocation methods.*

If explicit methods like RK4 were included within the framework, this could be a huge boon for the accessibility of the work!

<br>

---

<div style="text-align: center;">
    <h2>{% include stars/2.md %}</h2>
</div>

---

<br>

### Application of the [auxiliary variable framework](/publications/sp-integrators/) to a viscoelastic fluid system {#viscoelastic}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/1.md %}

This should be a simple enough application of the [framework](/publications/sp-integrators/).
These kind of systems (e.g. Oldroyd-B fluids) are ripe for the picking;
they typically have both a conserved energy and dissipated entropy to preserve.

> *Apply the auxiliary variable framework to a problem in viscoelastic fluid dynamics.*

I've been in discussion with Aaron Brunk about an application in viscoelastic phase separation.

---

### Application of the [auxiliary variable framework](/publications/sp-integrators/) to delay DEs {#delay-des}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/1.md %}

This could be fun!
I've never really looked into the problem;
I don't know much about delay DEs and their structures, but I believe this should be possible.

> *Apply the auxiliary variable framework to a delay DE.*

---

### Conservative integrators for Hamiltonian systems in Lie groups {#lie-groups}

#### {% include interest/1.md %} <code>&#124;</code> {% include difficulty/2.md %}

Conservative integrators for Hamiltonian systems are generally posed over vector/function spaces, however the canonical space for such systems is often Lie groups.

> *Derive a conservative integrator for Hamiltonian systems in Lie groups (or show me something good exists in the literature that I've missed!).*

Maybe this could be done by adapting my [auxiliary variable framework](/publications/sp-integrators/) to problems posed over Lie groups, however things get really wonky here;
the associated test functions live in the Lie algebra, which get very annoyed when you try to project them into the Lie group.

<br>

---

<div style="text-align: center;">
    <h2>{% include stars/1.md %}</h2>
</div>

---

<br>

### Stable reduced order models (ROMs) from the [auxiliary variable framework](/publications/sp-integrators/) {#roms}

#### {% include interest/1.md %} <code>&#124;</code> {% include difficulty/1.md %}

One way of deriving ROMs is through very coarse finite element discretisations.
My [framework](/publications/sp-integrators/) could very well be applied in such a case, to derive conservative and dissipative reduced order models.

> *Bring the auxiliary variable framework to the world of reduced order modelling.*

One need not consider the CPG time discretisation for this to be interesting;
the auxiliary variables alone give stable ODE systems, which is interesting enough!

---

### Structure-preserving integrators for compressible MHD {#compressible-mhd}

#### {% include interest/1.md %} <code>&#124;</code> {% include difficulty/1.md %}

The compressible MHD equations are typically the equations of interest in fusion modelling (at least, within the realm of continuum mechanics).
We have defined stable integrators for the [compressible NS equations](/publications/sp-integrators/) and in [MHD](/publications/parker/) deriving from the [auxiliary variable framework](/publications/sp-integrators/);
constructing stable integrators for the compressible MHD equations should hopefully just be a case of combining the two!

> *Combine the stable auxiliary-variable integrators for the compressible NS equations and MHD to deriving a stable auxiliary-variable integrator in compressible MHD.* 

<br>

---

*(Credits to {% include collaborators/tabea/short.md %} for the idea & {% include collaborators/ridg/short.md %} for the inspiration for this page!)*

<!-- ---

To add:

- Existence for comp. NS
- Preconditioners
- Explicit integrators
- Can we get symplectic integrators via AVCPG? Relations to Ari Stern's work on multisymplecticity?
- Add link to Ari Stern/Aaron Brunk as collaborators
- Rob Kirby's quesiton of proving exponential decay -->
