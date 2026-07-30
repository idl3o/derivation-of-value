---
layout: document
title: "A Consistent Fiction"
subtitle: "Organizational Closure and the Limit of Coherence-Based Attestation"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /a-consistent-fiction/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-07-30
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "The program named its own worst failure mode — 'a consistent fiction is consistent', collapsing to 'autopoietic-cult attractors' — and never studied it. Maturana and Varela's theory is the study. A coherence mechanism is operationally closed in their exact sense, its fiction space has dimension d, and closing it costs d scalars of contact with the world, once. The program's anchors do not supply them, by an explicit rule; the inward axis might."
status: "v0.1 · working draft"
order: 17
---

## Abstract

*Proof of Coherence* §2, tabulating the weaknesses of the traditions it draws on, records against coherentism that "a consistent fiction is consistent" and that coherence-of-coherence "collapses to autopoietic-cult attractors." The word was borrowed and the theory behind it never consulted. This paper consults it. Maturana and Varela define an autopoietic system as a network of processes producing components which regenerate the network that produced them, and Varela's closure thesis holds that every autonomous system is *operationally closed* — operating solely on the basis of its own self-produced structures rather than on input received from outside. A coherence mechanism satisfies that description exactly rather than metaphorically: it scores agreement among participants' models, participants optimise toward the score, and so the criterion is produced by the things it judges. Three results follow, two of them measured. The **fiction space** — the set of distinct outcomes all scoring as perfectly coherent — has dimension d, the stalk dimension: consensus dynamics from five random starts converge to five different global sections spanning the whole kernel, and coherence does not choose between them. **Structural coupling costs d scalars, once**: pinning d numbers at a *single vertex* collapses the fiction space entirely, because a global section of a connected coherent sheaf is determined by its value at any one point, and the requirement scales with components rather than with network size. And the program does not pay it: *Gauge-Fixing*'s anchors fix the four gauge freedoms, all of which concern **provenance**, while the fiction space is a freedom of **content**. The anchors make the fiction unforgeable and well-attributed. They do not make it true, and the discipline that keeps an anchor from "swelling into a proxy" is precisely what forbids the contact that would. The escape, if there is one, is the inward axis: measuring an artifact is content-bearing and is not testimony.

---

## 1. A Word Borrowed Without Its Theory

The program has been honest about this failure mode since its whitepaper's first version, and imprecise about it in the same breath.

*Proof of Coherence* §2 sets out four traditions from which its conditions are drawn, and against each records what it cannot do alone. Against internal consistency — coherentism, the tradition that supplies the mechanism's name — it records: "A consistent fiction is consistent. Coherence-of-coherence collapses to autopoietic-cult attractors."

That sentence does two things. It states, correctly and without flinching, the deepest objection to the entire construction: a network of models that agree with one another may be agreeing about nothing. And it names the mechanism of the failure with a word imported from theoretical biology — *autopoietic* — which the document then never uses again, does not define, and takes no results from.

This paper takes the results. The claim is that the borrowing was more apt than the borrower knew, that the failure mode has a precise formal description in a literature fifty years old, and that the description yields a *measurement*: how much room a perfectly coherent network has to be consistently wrong, and what it would cost to remove that room.

---

## 2. Autopoiesis, Operationally

Maturana and Varela [1] define an autopoietic system as one "organized as a network of processes of production of components which through their transformations and interactions continuously regenerate the network of processes that produced them, and constitute the system as a concrete unity in the space in which it exists."

Two derived notions do the work here, and both must be kept operational rather than philosophical, since the surrounding literature carries freight this paper does not need and does not import.

**Operational closure.** Varela's closure thesis [2] holds that every autonomous system is operationally closed: its processes are related as a network, recursively depend on one another in their own generation, and — the formulation that matters — the system "operates solely on the basis of its own self-produced structures rather than on input it receives directly from the outside." Closure is not isolation. A closed system may be thoroughly perturbed by its environment. What it may not do is take its *criteria* from there.

**Structural coupling.** Such a system nonetheless constructs an internal world "shaped and connected to the outside only because this organization has to meet requirements of self-stabilization and survival." Coupling is the residual contact — the places where the environment is permitted to constrain rather than merely disturb.

The pair gives the shape of the question. Not *is the system closed?*, which for anything self-regulating is nearly always yes, but: **how much coupling does it retain, and is that enough to keep its self-produced criteria tethered to something it did not produce?**

---

## 3. The Mechanism Is Operationally Closed

Apply the definition without softening it.

A coherence mechanism scores participants on the agreement among their models — how well local sections glue, whether obstructions vanish, how the spectrum of the resulting operator behaves. Participants are rewarded for raising that score, so they adjust their models toward it. The models are the components; their agreement is the network of relations; and the agreement is what produces the reward that produces the models. The criterion is generated by the very things it judges.

That is Varela's formulation almost word for word: the system operates on the basis of its own self-produced structures rather than on input from outside. Nothing in the mechanism's scoring consults the world. It consults the participants, and the participants consult each other.

The whitepaper's own sentence was therefore not loose. Coherence-of-coherence *is* an autopoietic attractor, and calling it a "cult" is only the social instance of a structural fact. What follows makes the fact quantitative.

---

## 4. The Fiction Space

Hansen and Ghrist [3] showed the sheaf Laplacian implements a consensus algorithm: gradient flow on the Dirichlet energy drives any initial assignment toward the kernel, which is the space of global sections. A coherence-maximising network is therefore a dynamical system with a known attractor set, and we can ask what is in it.

**Definition 4.1 (fiction space).** The *fiction space* of a coherence substrate is the set of distinct assignments that score as perfectly coherent — the kernel of the sheaf Laplacian, ker Δ_𝓕 ≅ H⁰.

If it were a point, coherence would determine content, and maximising coherence would be the same operation as finding the world. It is not a point.

For a coherent sheaf over a connected complex with d-dimensional stalks, dim ker = d exactly. Measured (`code/fiction_space.py`) at d = 3, n = 20: consensus from five random initial conditions converges to five distinct global sections — residuals at 10⁻¹⁵, components outside the kernel at 10⁻¹⁴ — whose kernel projections span three dimensions. **They exhaust the fiction space.** Five different worlds, each perfectly coherent, each a fixed point of the mechanism's own dynamics, and the mechanism has no preference among them. The initial condition chose; coherence did not.

**Corollary 4.2, and it is uncomfortable.** The fiction space has dimension d, the stalk dimension — the expressive capacity of each participant's model. So **richer models buy more room to be consistently wrong.** The framework has treated richness as an unmixed good, a ceiling on how secure a mechanism can be made. On this reading it is also a floor under how far a coherent network can drift, and the two are the same parameter.

---

## 5. What Closure Costs to Break

The measurement of the escape is more encouraging than the measurement of the problem, and it is the paper's one piece of good news.

**Definition 5.1 (structural coupling).** The *coupling* of a mechanism is the number of scalars in its state that are pinned to a reference the network did not produce.

Measured on the same complex, pinning scalars at a single vertex reduces the fiction space one dimension at a time: pin one, dim 2; pin two, dim 1; pin three, dim 0. **Pinning d scalars at one vertex collapses the fiction space completely.**

The reason is structural rather than numerical. A global section of a connected coherent sheaf satisfies x_v = R_vᵀc for a single c ∈ ℝᵈ, so the entire section is determined by its value at any one point. Fix the value at one vertex and every other vertex follows.

**Proposition 5.2.** For a coherent sheaf, the coupling required to collapse the fiction space is d per connected component, and is independent of the number of vertices.

Measured: one component needs 3 scalars, two components need 6, four need 12, on a network of fixed size. **A network ten times larger needs no more contact with the world. A network that has split in two needs twice as much** — which makes connectivity a coupling requirement as well as, from the H⁰ duplication result, a Sybil requirement.

This is a remarkably cheap escape. Not a majority of honest participants, not continuous oversight, not a trusted validator set — d numbers, at one place, once.

---

## 6. The Anchors Do Not Supply It

And the program has forbidden exactly that contact, on purpose, for a reason it was right to have.

*Gauge-Fixing the Section Space* fixes four freedoms an adversary otherwise enjoys: backdating, grinding, duplication, and the free minting of identities. Every one of them concerns **provenance** — when a section was made, by whom, against which challenge, and exactly once. Not one of them constrains what a section *says*. The fiction space is a freedom of content, and no gauge anchor touches it.

The prohibition is explicit. That paper's test suite demands the physical anchor be consumed "*only* as randomness and timing, never once cited as a certificate of order," and the reason given is exactly right: an anchor cited as evidence of the property becomes a proxy for it, and proxies get eaten. The discipline that keeps the beacon from swelling into an oracle is the same discipline that prevents it from supplying content.

So the anchors, however well constructed, make the fiction **unforgeable and well-attributed**. They do not make it true. Volume V's residue does not rescue this either: residue was shown there to be negentropy *with its provenance fixed*, and provenance is precisely the axis that leaves the fiction space untouched.

**The program has chosen closure, knowingly, and has never priced the choice.** That is the paper's central claim. The choice is defensible — a mechanism with an oracle in it is a mechanism whose security is the oracle's — but it has been made implicitly, as a consequence of anchor hygiene, rather than faced as the trade it is: *closure against d scalars of contact.*

**Where an escape might be.** One family of contact is not testimony. Kar-Coin's inward axis attests by *artifact*: to check a claim about a lattice you measure the lattice, and measuring is not asking. Such a reading is content-bearing — it says what is the case, not merely who said it and when — and it involves no party that must be honest. If a coherence complex could take even one stalk from a physical measurement of a shared world rather than from a participant's report, Proposition 5.2 says that is enough to close the fiction space for the whole component. That is a conjecture and not a construction, and §8 states what it would need. But it suggests the inward axis was never only about capacity. It may be the program's only available form of structural coupling.

---

## 7. What Is Declined

**That closure is a pathology.** It is not, and Maturana and Varela do not treat it as one — closure is how living systems maintain identity through perturbation, and a mechanism with no closure at all would have no stable criterion to defend. The claim here is narrower: closure does not track truth, and a mechanism whose only criterion is self-produced cannot distinguish a coherent world from a coherent fiction *by any amount of internal effort*.

**Luhmann, enactivism, second-order cybernetics.** The autopoiesis literature extends into social systems theory and philosophy of mind, and this paper imports none of it. The operational definitions of §2 are all that is used, and the extensions are contested in their own field.

**That d scalars are free.** They are cheap in *quantity* and not necessarily in *kind*. A pinned value must come from somewhere, and if it comes from a party asked to be honest, the mechanism has bought closure-escape with an oracle — minimal, single-point, but real, and the framework's own Definition 2.3 would reject it. §6's suggestion turns entirely on whether measurement can supply content without testimony. Nothing here establishes that it can.

**That the fiction space is the whole of closure.** It measures freedom in the *perfectly coherent* limit. What happens at partial coherence, where H¹ ≠ 0 and the dynamics have not converged, is not addressed and is where every deployed system actually lives.

**Anything built.** The measurements are on a toy coherent sheaf with no adversary. A real network is noisy, partial, and contested, and none of those is modelled here.

---

## 8. Open Problems

**8.1. The fiction space at partial coherence.** Definition 4.1 is stated at the attractor. Real networks sit away from it, with obstructions present and dynamics still running. The right object is presumably a set of *approximately* coherent states — states below some energy — whose volume, rather than dimension, measures the available fiction. That reading would also connect to the tolerance condition that the H⁰ duplication result surfaced, since both are about what a threshold admits.

**8.2. Can measurement supply content without an oracle?** The whole of §6's escape route. What is needed is a construction in which one stalk's value is fixed by a physical measurement that many parties can independently repeat, with disagreement detectable — and an argument that this does not violate intrinsic verifiability. If it exists, closure costs d scalars per component and the program can pay. If it does not, closure is permanent and should be stated as a property of the mechanism rather than a limitation of the current draft.

**8.3. Does the coupling bound survive adversaries?** Proposition 5.2 holds for a coherent sheaf with consistent frames. An adversary controlling vertices near the anchor, or contesting the anchored value, is not modelled. The bound is a best case.

**8.4. Richness against fiction.** Corollary 4.2 puts richness on both sides of the ledger — more independent projections raise the security ceiling, and larger stalks enlarge the fiction space. Whether these are the same d, and whether a substrate can be rich in projections while thin in stalks, decides whether the tension is real or an artefact of the sheaf formulation.

**8.5. Is the anchor discipline separable?** *Gauge-Fixing*'s rule forbids citing the physical anchor as a certificate of order, to stop it becoming a proxy. Whether a *different* anchor could supply content while the beacon continues to supply only randomness and timing — two anchors with two disciplines — is a design question the program has never asked, because it had only one reason to want an anchor.

---

## References

[1] H. R. Maturana and F. J. Varela. *Autopoiesis and Cognition: The Realization of the Living.* D. Reidel, 1980.

[2] F. J. Varela. *Principles of Biological Autonomy.* North-Holland, 1979. (The closure thesis.)

[3] J. Hansen and R. Ghrist. *Opinion Dynamics on Discourse Sheaves.* SIAM Journal on Applied Mathematics 81(5), 2021. (The sheaf Laplacian as a consensus dynamic.)

Measurements are reproducible from `code/fiction_space.py`.
