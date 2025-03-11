---
title: OPEN PROBLEMS
permalink: /open-problems/
---

# OPEN PROBLEMS & REWARDS

---

### a.k.a. Boris's BIG questions

(Intro)

(This is all stuff I'm not working on currently (got to keep the best ideas to myself))

(Contact me if you're working on/interested in any of these problems! I'd love to collab)

(What is this?)

(What are the rewards and how do I obtain them?)

(How do I rank hardness?)

(Reward options)

(Link to page on homepage)

(Link to open problems on other pages ("Related open problems"))

{% include open-problems/title.md %}
{% include open-problems/all/drifts.md %}

---

## {% include stars/5.md %}

---

### Conservative integrator for PDEs with arbitrarily many invariants {#conservative-pdes}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/3.md %}

In [my work on conservative integrators through auxiliary variables](/publications/sp-integrators/), I derived an integrator for general conservative ODEs that conserves arbitrarily many invariants.
This is very cool!
However, when this idea is applied to PDEs in semi-discrete form, the resultant discretisations destroy the locality of the variational formulation, ruining the sparsity of the assembled problem and rendering the integrator effectively useless.

> *Adapt my scheme to give an integrator for general conservative PDEs that conserves arbitrarily many invariants; in particular, the discretised variational form must be local in space.*

One might consider for example the [Korteweg–De Vries equation](https://en.wikipedia.org/wiki/Korteweg%E2%80%93De_Vries_equation), which, while having infinitely many invariants, it seems difficult to conserve any more than 2.

---

### Dissipative integrator for ODEs with arbitrarily many dissipated quantities {#dissipative-odes}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/3.md %}

Again, in [my work on conservative integrators through auxiliary variables](/publications/sp-integrators/), I derived an integrator for general conservative ODEs that conserves arbitrarily many invariants.
While the results of the manuscript further extend to dissipated quantities, the scheme in question does not, and it's not at all obvious how to extend it as such.

> *Adapt my scheme to give an integrator for general ODEs that dissipates arbitrarily many invariants.*

All the better if you manage to dissipate arbitrarily many invariants for PDEs in the process!

---

### Maximum principles via the [auxiliary variable framework](/publications/sp-integrators/) {#maximum-principles}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/3.md %}

Maximum (and minimum) principles can typically be proven by variational identites (e.g. by testing against \({\text min}(u, 0)\))
[My work on structure-preserving integrators](/publications/sp-integrators/) gives a general framework for preserving conservation and dissipation laws by preserving variational identities.
It seems that one would be able, however the piece adamantly refuse to fall into place.

> *Show by example that auxiliary variables may be used to derive numerical integrators for PDEs that exhibit discrete maximum principles.*

Many thanks to {% include collaborators/yohance/short.md %} for useful discussions and insights here.
I hope they come to fruition!

---

## {% include stars/4.md %}

---

### Drifts {#drifts}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/2.md %}

In an [upcoming preprint](/publications/ap-integrators/), I adapt my [auxiliary variable framework](/publications/sp-integrators/) to the preservation of the magnetic moment of a charged particle as an adiabatic invariant.
This is exciting, but in practice the structure of interest for such simulations is the preservation of [guiding centre](https://en.wikipedia.org/wiki/Guiding_center) drifts.

> *Using auxiliary variables, construct an asymptotic-preserving integrator for charged particles that preserves energy conservation, adiabatic invariance of the magnetic moment, and guiding centre drifts; this must be done in a natural way that is uniformly accurate in the magnetic field strength.*

I'm letting "a natural way" do a lot of heavy lifting here, a term that I am leaving 100% up to my own jurisdiction.
There are a lot of very nasty "quick fixes" in the particle-pusher literature, and I really believe there's an elegant way to do this.

---

### Proximal Galerkin/LVPP {#proximal-galerkin}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/3.md %}

---

### Extension of the [auxiliary variable framework](/publications/sp-integrators/) to SDEs {#sdes}

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/3.md %}

---

## {% include stars/3.md %}

---

### Extension of the [auxiliary variable framework](/publications/sp-integrators/) to general adiabatic invariants {#adiabatic}

#### {% include interest/3.md %} <code>&#124;</code> {% include difficulty/1.md %}

---

### Superconvergence

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/2.md %}

---

### Projection of u in MHD

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/2.md %}

---

### Non-collocation RK methods

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/2.md %}

---

## {% include stars/2.md %}

---

### Viscoelastic (Oldroyd-B)/Matrix-valued problems

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/1.md %}

---

### Application to delay DEs

#### {% include interest/2.md %} <code>&#124;</code> {% include difficulty/1.md %}

---

### Hamiltonian systems in Lie groups

#### {% include interest/1.md %} <code>&#124;</code> {% include difficulty/2.md %}

---

### Proof of exponential decay

#### {% include interest/1.md %} <code>&#124;</code> {% include difficulty/2.md %}

---

## {% include stars/1.md %}

---

### Model order reduction

#### {% include interest/1.md %} <code>&#124;</code> {% include difficulty/1.md %}

---

### Compressible MHD

#### {% include interest/1.md %} <code>&#124;</code> {% include difficulty/1.md %}

---

*(Credits to {% include collaborators/tabea/short.md %} for the idea & {% include collaborators/ridg/short.md %} for the inspiration for this page!)*

---

To add:

- Existence for comp. NS
