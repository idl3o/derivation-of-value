---
layout: document
title: "No Global Section"
subtitle: "Contextuality as the General Form of Composition Failure"
eyebrow: "An Anthology · Paper · v0.2"
permalink: /no-global-section/
anthology: "Derivation of Value"
version: "v0.2"
date: 2026-08-06
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Every department hits its metrics and the firm fails. That is not an anecdote about organisations — it is contextuality, in Abramsky and Brandenburger's exact sense, and it comes with thirty years of mathematics attached. Importing it grades composition failure into three strengths, supplies a route past the affine-gate hypothesis, and settles what a vanishing obstruction can and cannot certify."
status: "v0.2 · working draft"
order: 13
---

## Abstract

*Gluing the Gates* observed that conjunction-gated mechanisms do not compose: every constituent gate can be satisfied while no globally admissible assignment exists. It located the obstruction in cohomology under a hypothesis — that gate conditions are affine on stalks — which the program's own worked instance violates, since a threshold on a spectral quantity is not affine. This paper removes the hypothesis by identifying the phenomenon. Local sections everywhere and no global section is *contextuality*, characterised by Abramsky and Brandenburger for quantum non-locality and studied since with tools this program can use directly. Three things follow. The contextuality literature works with presheaves of **distributions** over admissible sets rather than with the sets themselves, which recovers an abelian object without linearising anything — the route past the affine hypothesis, and this paper's load-bearing conjecture. The strength hierarchy transfers, grading composition failure into probabilistic, logical, and strong, each with a different design response, where *Gluing the Gates* had only a single binary. And the established cohomological obstruction is *sufficient but not necessary*, which settles a question the earlier paper left ambiguous: a non-vanishing obstruction is grounds to redesign the interfaces, and a vanishing one is not a certificate that the gates glue. The paper closes on a speculation marked as such — contextuality is a quantum *resource* and not only a pathology, and whether economic contextuality is likewise harvestable is a question the program's adversary-positive machinery is shaped to ask.

---

## 1. The Shape of the Problem

A mechanism is nested inside another. Each level scores its participants, gates their reward on a conjunction of projections, and reports upward. Every level's gate is satisfied. The whole fails anyway.

*Gluing the Gates* gave this a construction — three holons on a cycle whose restriction maps compose around to a non-identity scalar, each locally admissible, jointly admitting nothing — and a name, non-compositionality, and a consequence: absent compositionality, a holarchy's Goodhart-asymptotic security is the minimum over its levels rather than the product, because an adversary selects which level to attack. It then located the obstruction in H¹ of a gate sheaf, under the assumption that gate conditions are affine on stalks.

That assumption is the paper's weak point, and it is weak in a specific and embarrassing way: the program's own worked instance violates it. *Proof of Coherence* gates on the dimension of a kernel and on properties of a spectrum. A threshold on an eigenvalue distribution is not an affine condition on a stalk. The theory was stated for a case the program does not have.

The repair is not to strengthen the algebra. It is to notice that the phenomenon has been studied for fifteen years in another field, under conditions that include the non-affine case from the start.

---

## 2. Contextuality

Abramsky and Brandenburger [1] gave a sheaf-theoretic account of quantum non-locality and contextuality, and the central move is the one this program needs. A *measurement scenario* consists of a set of measurements, a family of *contexts* — sets of measurements that can be performed jointly — and, for each context, the outcomes available. A *model* assigns to each context a distribution over its joint outcomes, subject to the requirement that overlapping contexts agree on their intersection.

The question is whether those local assignments extend. Is there a single global assignment — a distribution over outcomes for *all* measurements at once — whose restriction to each context recovers what was observed? For classical systems there always is. For quantum systems there need not be, and Abramsky and Brandenburger's result is that non-locality and contextuality are characterised **precisely** as the obstruction to the existence of such a global section.

The translation to the present setting is direct, and we state it as a definition rather than an analogy because nothing is being weakened in transit.

**Definition 2.1 (the gate scenario).** Given a holonic substrate and an induced mechanism in the sense of *Gluing the Gates*, the associated *gate scenario* has: as measurements, the holons; as contexts, the interfaces — the sets of holons that must agree on a shared boundary; and as outcomes at each holon, the states satisfying that holon's conjunction gate. A *gate model* assigns to each interface the admissible joint states of the holons meeting there.

**Claim 2.2.** A gate model has a global section exactly when the induced mechanism is compositional in the sense of *Gluing the Gates* Definition 3.4. Non-compositionality is therefore contextuality of the gate model.

The claim is a translation, and its content is that both sides mean what they appear to mean. Local admissibility everywhere with no global admissible assignment is, on the left, "every department hits its metrics and the firm fails," and on the right, a contextual model. The departments stand to the firm as local measurement outcomes stand to an absent joint distribution, and they are obstructed by the same mathematics.

There is something worth pausing on here beyond the technical convenience. Contextuality is usually presented as the strange thing about quantum mechanics — the feature that resists classical explanation and marks the boundary of intuition. The claim of this section is that it is also an ordinary feature of organisations, and that an economist who finds every division healthy and the enterprise sick is looking at a Bell-type phenomenon. Whether that is a deep fact about composition or a coincidence of formalism is not settled here, and §6 declines to settle it.

---

## 3. Past the Affine Hypothesis

The reason contextuality is the right import, rather than merely a pleasing one, is that its literature solved the exact technical problem *Gluing the Gates* left open.

Gate conditions are not affine. Admissible states at a holon form some subset of its state space — a superlevel set of a projection, generally curved, possibly disconnected. Sheaves of *sets* do not have an H¹ in the ordinary sense; their gluing obstruction is non-abelian and there is no readily computable invariant.

Abramsky, Mansfield and Barbosa [2] address the same difficulty by changing the object. Rather than working with the admissible sets, they work with an abelian presheaf derived from the model's **support** — from distributions over the admissible outcomes rather than the outcomes themselves. Čech cohomology on that presheaf yields an obstruction class, and the class vanishes when the family has a global section. Linearity is recovered not by linearising the constraints but by passing to distributions over them, which is free.

**Conjecture 3.1 (the route past affineness).** The same construction applies to gate scenarios. Passing from admissible state sets to distributions over admissible states yields an abelian presheaf whose Čech cohomology carries an obstruction to the existence of a globally admissible assignment, with no assumption that the gate conditions are affine.

This is the paper's load-bearing conjecture and it is not yet established. What supports it is that nothing in the construction of [2] appears to use quantum structure — the input is a compatible family of distributions over local outcome sets, which a gate scenario supplies. What could defeat it is the difference in what the distributions *mean*: in the quantum case they are given by the physics and are the object of study, while in a gate scenario the mechanism designer would have to choose them, and an arbitrary choice may make the obstruction an artefact of the choice rather than a property of the mechanism. Settling this is the first item in §7, and if it fails the honest outcome is a negative result: that gate scenarios are contextual in the qualitative sense while resisting the quantitative treatment, which would itself be worth recording.

---

## 4. Three Strengths of Failure

*Gluing the Gates* had one notion of composition failure: either the gates glue or they do not. The contextuality literature grades it, and the grades correspond to genuinely different situations for a mechanism designer.

**Probabilistic.** No global distribution reproduces the observed local ones, though every individual local assignment is separately extendable. In mechanism terms: each level's admissible states can be realised, and the *frequencies* with which they must occur cannot be reconciled. A mechanism in this regime is not broken in any single run. It is miscalibrated across runs, and the failure appears as a persistent discrepancy between what levels report and what the whole exhibits.

**Logical.** Some local assignment does not extend to any global one, though others do. In mechanism terms: there exist particular admissible configurations of a level which no global configuration contains — states a constituent can legitimately reach that the whole cannot accommodate. This is the regime an adversary wants, because it can *steer* toward such a configuration, satisfy its own gate honestly, and thereby guarantee the whole fails.

**Strong.** No local assignment extends at all. In mechanism terms: the levels are jointly unsatisfiable, and the mechanism cannot be made to work by any choice of participant behaviour. This is not an attack surface; it is a specification error, and it should be caught before deployment.

The design responses differ accordingly, and the grading is the practical payoff of the import. Probabilistic contextuality calls for recalibrating thresholds. Logical contextuality calls for redesigning interfaces, because there is an exploitable configuration and an adversary will find it. Strong contextuality calls for abandoning the composition. A binary "the gates do not glue" cannot distinguish a miscalibration from a specification error, and *Gluing the Gates* offered nothing finer.

---

## 5. What a Vanishing Obstruction Certifies

*Gluing the Gates* stated its cohomological criterion as a biconditional and then hedged in prose. The contextuality literature settles the matter, and not in the direction the earlier paper's phrasing suggested.

Abramsky, Mansfield and Barbosa's obstruction vanishes when a global section exists — so a non-vanishing class does prove contextuality — but its non-vanishing is **sufficient and not necessary**. There are contextual models the cohomology does not see. The invariant has false negatives, and they are a known feature rather than an artefact of a weak proof.

**Consequence 5.1.** For gate scenarios, the cohomological obstruction is a **detector of composition failure, not a certificate of composition safety.** A non-vanishing class is grounds to redesign the interfaces. A vanishing class licenses nothing.

This is a substantially weaker guarantee than a compositionality criterion would ideally provide, and it should be stated in the form a designer will actually use: the invariant can tell you that you have a problem and cannot tell you that you do not. *Gluing the Gates* has been amended to say so.

The shape of this limitation will be familiar. The negentropy paper established that H¹ = 0 certifies coherence and not truth: a consistent fabrication glues as well as a fact. The present result is the same disappointment one level out. **H¹ = 0 does not even certify that the levels compose** — only that this particular invariant found no reason to think they do not. The program has now encountered, twice, the discovery that vanishing cohomology is weaker evidence than it looks, and the pattern is worth naming: cohomology detects the obstructions it was built to detect, and silence from it is not evidence of absence.

---

## 6. Contextuality as a Resource — Speculative

This section is speculation and is marked as such. It is included because the question it raises is well-posed and because the program's machinery is unusually well shaped to ask it.

In quantum information, contextuality is not only a pathology. It is a **resource**: the feature that certain quantum advantages are known to consume, and without which some computational speedups are unavailable. A system that fails to admit a global section is, in that setting, doing something a globally-sectioned system cannot.

*Combination Proofs* §4 establishes conditions under which failed adversarial effort subsidises the substrate it attacks — adversary-positivity, resting on residue that persists whether or not a claim is admitted. The question this suggests is whether non-gluing is similarly harvestable: whether a designer can *use* a holarchy's failure to admit a global section rather than only detect and repair it.

A concrete form of the question: the logical-contextuality regime of §4 was described above as the one an adversary wants, because it can steer toward a locally admissible configuration that no global configuration contains. Read the other way, such configurations are *distinguishing* — they separate participants who reached them from participants who did not, using structure no single level can see. Whether that separation can be made into a projection, and whether such a projection would be independent of the level-local ones in the sense the framework requires, is not addressed here.

We flag the obvious hazard. The move from "contextuality is a resource in quantum computation" to "contextuality is a resource in mechanism design" is exactly the kind of transfer this program forbids elsewhere, and stating it as a question rather than a claim is the minimum discipline. It earns its place only because §2 established the two settings share a formalism, not merely a word.

### 6.1 The question has a setting, and half an answer — v0.2

Two developments since v0.1 bear on the paragraph above, and they pull in opposite directions.

**The setting.** This section's question presumes a mechanism that must produce a global section and is embarrassed when it cannot. A mechanism that *delivers* coherence per recipient rather than paying for it globally has no such requirement: a message need only cohere in its context, and non-gluing across contexts costs it nothing. That is developed in `_plan/service-reframe.md` and is the first concrete setting in which this section's speculation is a design question rather than an analogy. The obstruction this paper spent six sections establishing stops being an obstruction when the deliverable is local — which is the strongest available form of "contextuality as resource" for this program, and it required no transfer from quantum computation to state.

**The half-answer, and it is discouraging.** The closing sentence above asks "whether such a projection would be independent of the level-local ones in the sense the framework requires." Independence has since been shown to be the *less* binding of two requirements a projection must satisfy (*Combination Proofs* v0.6 §7.1). A projection can be perfectly independent — ι = 1.000 measured — and still contribute nothing, if its trace is cheap to forge. The question this section poses must therefore be asked twice, and the second asking is the hard one: **is a contextuality-derived projection expensive to counterfeit?** Nothing here suggests it would be, and a separation visible only through structure no single level can see is, on the face of it, a separation an adversary can assert as easily as earn.

---

## 7. What Is Declined

**That Conjecture 3.1 is established.** It is not. The entire quantitative content of the paper rests on it, and it has not been checked against a constructed gate scenario. Until it is, this paper's contribution is the identification of §2 and the grading of §4, both of which stand independently.

**That the translation is content-free.** Claim 2.2 asserts that two definitions agree. If gate scenarios turn out to require structure that measurement scenarios lack — an ordering on contexts, say, or a notion of a level being *above* another that the contextuality formalism does not carry — the translation is partial and the imported results transfer only in part.

**Any quantum claim.** Nothing here says that economic systems are quantum, that quantum effects appear in mechanisms, or that quantum hardware bears on the problem. The shared object is a sheaf-theoretic obstruction. Two settings can share a formalism and nothing else, and §6 is speculation precisely because it is the one place tempted to say more.

**A repair.** The paper diagnoses and grades. It does not say how to build an interface whose gate scenario is non-contextual, which is the question a designer actually has.

**That the earlier hedging was adequate.** *Gluing the Gates* stated a biconditional and qualified it in prose. §5 shows the qualification was the correct reading and the statement was not, which is a correction to a paper of this program and is recorded as one.

---

## 8. Open Problems

**8.1. Check Conjecture 3.1.** Construct a small gate scenario with genuinely non-affine gates — thresholds on a spectral quantity, as the program's worked instance uses — determine whether local admissibility without global admissibility occurs, and whether the distributional presheaf detects it. This is a computation, not a research programme, and it should be done before anything is built on §3.

**8.2. Which distributions.** If the designer chooses the distributions in the presheaf, the obstruction may depend on that choice. Is there a canonical one — maximum entropy over admissible states, say — and does the obstruction it yields have a mechanism-theoretic meaning?

**8.3. Grading a real mechanism.** Where in the hierarchy of §4 do the program's existing constructions sit? The answer is presumably different for the coherence complex and for a nested deployment of it, and neither has been determined.

**8.4. Necessary invariants.** Given that cohomology has false negatives, is there an invariant for gate scenarios that is necessary as well as sufficient — or a proof that none is computable? The contextuality literature's experience suggests pessimism, and a pessimistic answer would be worth having explicitly.

**8.5. Contextuality and the verifiability boundary.** *Gluing the Gates* §8.4 asked whether the verifiability boundary and the composition obstruction are the same boundary. In the present language: are the projections that resist intrinsic verification the same projections whose gate scenarios are contextual? A positive answer would collapse two of the framework's open problems into one.

---

## References

[1] S. Abramsky and A. Brandenburger. *The Sheaf-Theoretic Structure of Non-Locality and Contextuality.* New Journal of Physics 13, 113036, 2011. arXiv:1102.0264.

[2] S. Abramsky, S. Mansfield, and R. S. Barbosa. *The Cohomology of Non-Locality and Contextuality.* arXiv:1111.3620, 2011.

[3] S. Abramsky. *Contextuality: At the Borders of Paradox.* In *Categories for the Working Philosopher*, Oxford University Press, 2017. arXiv:2011.04899.

[4] *A Sheaf-Theoretic Characterization of Tasks in Distributed Systems.* arXiv:2503.02556.
