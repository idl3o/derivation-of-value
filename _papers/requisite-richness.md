---
layout: document
title: "Requisite Richness"
subtitle: "Variety as a Lower Bound on Substrate Richness"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /requisite-richness/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-07-30
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "The framework gives richness as a ceiling on how secure a mechanism can be made. Ashby's law supplies the floor, and the floor is set by the adversary rather than by the substrate. Between them, substrate selection stops being an optimisation and becomes a feasibility question: some substrates are simply too poor for some adversaries, and no cleverness repairs them."
status: "v0.1 · working draft"
order: 14
---

## Abstract

Definition 5.1 makes richness a **ceiling**: a mechanism cannot be a Combination Proof of order higher than ρ(𝒮), however clever its construction. The framework has no corresponding floor, and so cannot say when a substrate is *too poor* — only when a construction is too ambitious. This paper supplies the floor from Ashby's law of requisite variety, in its information form: a regulator's capacity cannot exceed its capacity as a channel, so the residual variety in what a mechanism is protecting is at least the adversary's variety minus the mechanism's own. Translating, a Combination Proof's projection vector must carry at least as much variety as the adversary's strategy space, which yields a lower bound on richness set by the attacker rather than by the substrate. The two bounds together change the character of substrate selection: it is a **feasibility** question before it is an optimisation one, and a substrate whose richness falls below the requisite variety of its adversary class cannot be repaired by better projections, more careful thresholds, or any amount of design. The paper then takes up Conant and Ashby's good-regulator theorem, which bears directly on the framework's open universality question, and is careful about it — the theorem is contested, and establishes less than its title promises. A closing section proposes Beer's Viable System Model as a ready-made test case for the compositionality criterion of *Gluing the Gates*.

---

## 1. A Ceiling Without a Floor

The framework's richness measure does one job well and leaves its complement undone.

Definition 5.1 sets ρ(𝒮) as the supremum, over collections of intrinsically verifiable projections, of the size of any pairwise approximately independent subset, and the implication drawn from it is a bound from above: a mechanism cannot be a Combination Proof of order higher than ρ, regardless of construction. The framework calls this the shift from constructing proxies to *selecting substrates*, and it is the right shift. But a ceiling alone answers only one of the two questions a designer has.

It answers: *how good can this substrate be made?* It does not answer: *is this substrate good enough?*

The second question has no home in the framework as it stands, because nothing in it refers to the adversary's size. Fake-cost (Definition 2.4) is relative to an attacker class, and the multiplication claim says how fake-costs compose, but no statement anywhere says that a substrate can be **too poor for its opponent** — that there exist (substrate, adversary) pairs for which no Combination Proof suffices, and that the failure is a property of the pairing rather than of any designer's ingenuity.

That statement exists, in a literature seventy years old, and it is the oldest result in cybernetics.

---

## 2. Requisite Variety

Ashby's law, from *An Introduction to Cybernetics* [1], is usually quoted in its compressed form — *only variety can destroy variety* — and usually quoted loosely. The precise version is what this paper needs.

Ashby's setting has three terms. A set of **disturbances** D originates outside the system and threatens, if nothing intervenes, to drive the **essential variables** E outside their acceptable range. A **regulator** R acts to prevent this. The law states that R's capacity as a regulator cannot exceed R's capacity as a channel of communication, and in its information-theoretic form,

> H(E) ≥ H(D) − H(R)

so that holding the essential variables to zero residual variety requires H(R) ≥ H(D). A regulator with less variety than its disturbances cannot, whatever its design, hold the system it regulates. The shortfall passes through to the essential variables and appears there as failure.

The law is often invoked as a slogan about complexity and rarely with its terms fixed. Fixing them is the whole of the translation, so we do it explicitly.

**The disturbances D** are the adversary's strategy space: the set of distinct behaviours an attacker in the class of Definition 2.4 can adopt. Its variety H(D) is the log of the number of strategies the mechanism must be able to tell apart, weighted by their distribution.

**The essential variable E** is the reward error: the discrepancy between what the mechanism pays and what honest participation warrants. Goodhart-asymptotic security is precisely the claim that this variable stays in range as the adversary grows more capable.

**The regulator R** is the mechanism's projection vector (π₁, …, π_K). It is the only channel through which the substrate's state reaches the reward function, and its variety is the variety the mechanism can distinguish — no more, since anything the projections cannot separate the reward cannot separate either.

---

## 3. The Floor

**Proposition 3.1 (requisite richness).** Let M be a Combination Proof of order K on substrate 𝒮, facing an adversary class of strategy variety H(D). If the mechanism is to hold the reward error to zero residual variety, then

> H(π₁, …, π_K) ≥ H(D)

and since the projections' joint variety cannot exceed what K intrinsically verifiable projections of 𝒮 can carry, and K ≤ ρ(𝒮),

> ρ(𝒮) · h ≥ H(D)

where h bounds the variety carried by any single projection of 𝒮.

*Sketch.* The projection vector is the only channel from substrate to reward, so the reward is a function of it and can distinguish no more than it does. Apply Ashby's law with R the projection vector and E the reward error; the second inequality substitutes the framework's own ceiling on K and a per-projection variety bound. ∎

The proposition is a translation rather than a discovery, and its interest is entirely in what it makes sayable. Richness now has bounds on both sides, and they come from different places: **the ceiling is a property of the substrate, and the floor is a property of the adversary.**

**Corollary 3.2 (some substrates are simply too poor).** If ρ(𝒮)·h < H(D), then no Combination Proof on 𝒮 regulates the reward error against that adversary class — not for want of a better construction, but because the channel is too narrow. No choice of projections, thresholds, or reward shape repairs it. The substrate must be exchanged.

This is a strong claim in a program that has been careful about strong claims, so its limits should be stated at once. It is a bound on *variety*, not on cost. It says the mechanism cannot **distinguish** enough, not that attacks are cheap; a mechanism can have requisite variety and still be defeated by an adversary willing to pay. Requisite variety is necessary, not sufficient, and the framework's existing fake-cost apparatus remains the sufficiency side.

---

## 4. Feasibility Before Optimisation

Put the two bounds together and substrate selection changes character.

> ρ(𝒮) · h ≥ H(D)   (floor: can this substrate see the adversary at all?)
>
> K ≤ ρ(𝒮)       (ceiling: how far can construction go on it?)

The framework has presented substrate selection as an optimisation — read a substrate's structure, find its richness, build to the highest order it supports. The floor makes it a **feasibility problem first**. Before asking how good a mechanism on 𝒮 can be, one asks whether 𝒮 admits any adequate mechanism at all against the adversary in question, and the answer can be no.

This reframing sharpens something the program has said loosely elsewhere. *Kar-Coin* observed that civilisational capacity is "the richest substrate the anthology has found" and treated that as its principal attraction. Proposition 3.1 says why richness is not a luxury there: an adversary against a civilisation-scale mechanism has enormous strategic variety, so the floor is correspondingly high, and a substrate of modest richness would have been disqualified before any question of construction arose. The reach for a rich substrate was not ambition. It was a requirement, and the program did not have the vocabulary to say so.

It also puts a floor under the Sybil results. *The Multiplicity Freedom* shows richness bounding the Sybil cap from above — more independent projections divide the adversary's fleet further. Proposition 3.1 shows the adversary's variety bounding required richness from below. **Between them, ρ is squeezed on both sides by facts about the opponent**, which is an unusual position for a quantity the framework introduced as a property of the substrate alone.

---

## 5. Conant–Ashby, and the Universality Question

The framework's §7.4 asks whether Combination Proofs are *necessary* for the multiplication and publicity-positive properties, or merely sufficient. It records that the strongest form of the framework would be a theorem establishing necessity, and that no such theorem exists.

Cybernetics has a theorem of that shape, and it is worth examining precisely because the examination ends in a qualified answer rather than a triumphant one.

Conant and Ashby [2] proved a result whose title is *Every good regulator of a system must be a model of that system*. In modern formulation: any regulator that is optimal — minimising the entropy of the regulated outcome — **and maximally simple among the optimal ones** must be a homomorphic image of the system it regulates.

The relevance to this program is immediate and almost too neat. The framework's substrate, in its worked instance, *is* models: a coherence complex over the world-models of many participants, scored by how well those models glue. A theorem saying that regulating a system requires modelling it, applied to a mechanism whose substrate is itself models, suggests a self-referential necessity argument of exactly the kind §7.4 wants.

**But the theorem establishes less than its title claims, and this must be said plainly.** The result is a statement about regulators that are maximally simple among optimal ones. It does not show that every good regulator is a model; it shows that the non-redundant ones are. A regulator carrying unnecessary complexity may regulate optimally without being a homomorphic image of anything. The paper is also, by wide agreement, difficult to read, and there is standing debate about what precisely it proves.

**Claim 5.1, stated weakly on purpose.** If a Combination Proof is a good regulator in Conant and Ashby's sense, and if it is minimal among the mechanisms achieving its regulation, then it is a homomorphic image of the substrate it scores. Whether Combination Proofs are minimal in the required sense is not established here, and the conditional is doing real work.

What that would buy, if it went through, is a necessity argument of the right *shape* for §7.4 — a mechanism that regulates a substrate must reproduce the substrate's structure, and reproducing the structure of a substrate with ρ independent projections means having ρ independent projections. What it would not buy is the theorem itself. This section identifies a route and declines to claim it is a road.

---

## 6. A Test Case the Literature Already Built

Stafford Beer's Viable System Model [3, 4] is a designed holarchy: five interacting subsystems, recursively structured so that every viable system contains and is contained by viable systems of the same form. It is the most developed applied holarchy in existence, it was built by someone who had read Ashby closely, and it has been deployed.

That makes it a ready-made test case for the criterion of *Gluing the Gates*. That paper asks when the gates of nested mechanisms glue, and shows that when they do not, security is the minimum over levels rather than the product. The VSM is a nesting whose interfaces are specified in unusual detail — the channels between levels are the model's main content — so the question *does the VSM glue?* is answerable rather than rhetorical.

We do not answer it here. We note that the question is well-posed against an existing artefact, which is rarer in this program than it should be, and that a negative answer would be more interesting than a positive one: a designed holarchy that fails the compositionality criterion would show the criterion has teeth against something other than a construction built to illustrate it.

---

## 7. What Is Declined

**That the variety measure is commensurable.** Proposition 3.1 relates H(D), an entropy over adversary strategies, to ρ, a count of independent projections, through a per-projection variety bound h. Whether h is well-defined for the substrates the program cares about is not established, and if it is not, the proposition degrades from a bound to an analogy. This is the paper's principal weakness and it is load-bearing: everything in §3 and §4 depends on the two quantities living on a common scale.

**That requisite variety is sufficient.** It is necessary. A mechanism with adequate variety can still be beaten by an adversary willing to pay, which is what the fake-cost apparatus is for. Nothing here replaces it.

**That Conant–Ashby transfers.** §5 states the conditional and does not discharge it. The theorem is contested in its own literature, its hypotheses are stronger than its title, and no argument is given here that Combination Proofs satisfy them.

**That H(D) is knowable.** The floor is stated in terms of an adversary's strategy variety, which a designer does not have and cannot easily estimate. The proposition is useful for saying that a floor *exists* and for comparative reasoning between substrates; it is not a number anyone can compute for a deployment.

**Any claim about Beer.** §6 proposes a test and does not run it.

---

## 8. Open Problems

**8.1. Make h precise.** Bound the variety a single intrinsically verifiable projection of a given substrate class can carry. Without this the central proposition is not usable, and with it the floor becomes computable in the same regime where the ceiling already is.

**8.2. Estimate H(D) adversarially.** The program's one measurement of an adversary-relative quantity came from putting an adversary in a loop and watching. The same instrument might bound strategy variety from below by counting distinguishable attacks that actually work — a lower bound on H(D) is all Corollary 3.2 needs to disqualify a substrate.

**8.3. Does the floor compose?** *Gluing the Gates* showed richness does not compose. Requisite variety plausibly does not either, and worse: an adversary attacking a holarchy may deploy variety at whichever level is narrowest, which would make the *binding* floor the maximum over levels while the available richness is the minimum. If so, nesting is doubly penalised, and that is worth knowing before anything is nested.

**8.4. Minimality of Combination Proofs.** Claim 5.1's conditional turns on whether a Combination Proof is minimal among mechanisms achieving its regulation. Conjunction-gating is a strong structural constraint and may make minimality tractable to check.

**8.5. Run the VSM through the criterion.** §6's question, answered.

---

## References

[1] W. R. Ashby. *An Introduction to Cybernetics.* Chapman & Hall, 1956. (Law of Requisite Variety; the information-theoretic form H(E) ≥ H(D) − H(R).)

[2] R. C. Conant and W. R. Ashby. *Every Good Regulator of a System Must Be a Model of That System.* International Journal of Systems Science 1(2), 89–97, 1970.

[3] S. Beer. *Brain of the Firm.* Allen Lane, 1972.

[4] S. Beer. *The Heart of Enterprise.* Wiley, 1979.
