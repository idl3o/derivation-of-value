---
layout: document
title: "Key and Census"
subtitle: "On the Reduction of Every Mechanism to an Integer, and the Catalogue of the Places Where the Reduction Fails"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /key-and-census/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-11-06
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Every verifiable mechanism, taken to its incentive-compatible limit, proves possession of a single integer and nothing else: a predicate with no proxy slack is a preimage check, and a participant stripped of every forgeable property is a signature. The corpus had the reduction as far as the anchor — every declared-frame reading evidences nothing, a Combination Proof is its anchors wearing readings — and this paper takes the anchors to their own limit, where each is a preimage or a key. The derivations of value the mechanisms were built to carry do not survive the limit. Read as a presheaf over the space of situations, the anthology's papers agree on the mechanism and disagree on the reason, the disagreements are a cocycle that is not a coboundary, and the first cohomology does not vanish. There is a global key and no global derivation. The catalogue of the overlaps on which the derivations fail to glue is the Census, the word borrowed from the count of witnesses and used for a count of reasons."
status: "v0.1 · working draft"
order: 33
---

## Abstract

Every verifiable mechanism, taken to its incentive-compatible limit, proves possession of a single integer and nothing else. This is argued in two directions, for what is measured and for who is measured, and the two limits meet at one object. It is then argued that the derivations of value which the mechanisms were built to carry do not survive the limit, and that the anthology in which they are collected cannot be reduced to the integer its mechanisms prove: read as a presheaf of derivations over a space of situations, with the papers as a cover, the first cohomology does not vanish. The obstruction is exhibited and not computed. The catalogue of the overlaps on which it does not vanish is here called the Census, a second use of a word *The Census of Errors* made for witnesses.

---

## I. The Key

A mechanism is a pair (A, V): a space of admissible actions and a verification predicate on them. The predicate decides which actions are rewarded. Everything else the mechanism is said to do — to elicit effort, to price scarcity, to measure contribution, to derive value — is a story told about the predicate by people who built it.

The predicate can be written as a measurement followed by a threshold. Let m: A → ℝ be the measurement and t the threshold, so that V(a) holds exactly when m(a) ≥ t. The quantity the mechanism was meant to reward is some other function q: A → ℝ, which the designers could not measure directly, or they would have used it. The distance between m and q over the admissible space is the proxy slack:

> σ(A) = sup_{a ∈ A} \|m(a) − q(a)\|.

Goodhart's observation, in this notation, is that an optimiser against V moves toward the region of A where σ is largest. *Combination Proofs* treats Goodhart as a property of the substrate rather than of the proxy, calls a mechanism Goodhart-asymptotic when the cost of evading it grows without bound in a resource the mechanism controls, and imports Manheim and Garrabrant's four failure modes; in this notation the four are four ways of occupying the slack. Mechanisms differ in how long the drift takes. They do not differ in where it ends.

A narrower sense is used here, and it is this paper's rather than the framework's. A mechanism is called Goodhart-asymptotic, in this sense, when it is the limit of a sequence of mechanisms under which σ → 0. The sequence need not converge quickly. It need only converge.

The limit has a shape, and the shape is the subject of this paper. If σ = 0 then m = q on all of A, and the predicate decides q(a) ≥ t directly. There is no slack because there is no proxy. There is no proxy because the measurement *is* the quantity. A measurement that is identical to the quantity it measures is a tautology, and a tautology admits only one form of verification: the presentation of the thing itself.

Concretely. Fix a function h with the property that h(x) is cheap to compute and x is not cheap to recover from h(x). Let the admissible actions be bit-strings, let the quantity be q(a) = [h(a) = k] for some fixed k, and let the threshold be 1. The predicate is now: present a such that h(a) = k. The measurement is the quantity. The slack is zero. No optimiser can move toward a region of A where m exceeds q, because there is no such region. The mechanism is immune to Goodhart's drift because it has been reduced to a preimage check.

Every Goodhart-asymptotic sequence terminates in a mechanism of this form. The argument is the observation that a verification predicate with no slack is a predicate whose satisfaction cannot be approximated, and a predicate whose satisfaction cannot be approximated is a predicate whose satisfaction is a discrete fact about the action: a bit. The action either carries the bit or it does not. The carrier of a discrete fact that cannot be approximated, forged, or partially satisfied is, up to encoding, an integer.

The integer is the Key. It is what remains of a mechanism after the stories have been removed.

The corpus has this reduction as far as the anchor, and has it as a theorem. *One's Own Anchor* proves that every reading computed from declared restriction maps evidences nothing: an adversary holding the anchors' receipts reproduces the honest configuration at no native cost, because the honest configuration in that class costs exactly what the anchors cost. *Independent and Expensive* states the same from the budget's side — a Combination Proof of order K is not K readings of one substrate but K anchors wearing readings. Both results stop at the anchor. The present section takes the anchors to their own limit. The four of *Gauge-Fixing the Section Space* are a beacon, a delay chain, a unique encoding and a dissipation floor. A beacon is a public value and its check is equality with it. A delay chain is a sequence of squarings verified against a public value. A unique encoding is a preimage keyed to bearer and epoch. A dissipation floor is proof of work, a preimage under a target. Each is a preimage check or a signature. The reduction does not stop at the anchor; it stops at the integer, and K anchors wearing readings is K integers wearing readings.

The anthology's four substrates were built on this fact without stating it. Coherence: what *Proof of Coherence* pays for is a vanishing obstruction, and by the theorem above a vanishing obstruction under declared frames is worth exactly its anchors' receipts. Negentropy: *Proof of Preservation* could not make order attest itself, and *Gauge-Fixing* certifies it by the four checks just listed. Vector value: *Omnium*'s kernel enforces conservation on a content-addressed ledger, and what such a ledger admits is a hash. Capacity: *Kar-Coin*'s outward rungs are attested by report, and a report is a signed claim; the one rung that essay now records as attesting itself is the hash residue of proof of work, a preimage under a target. Each was presented as a derivation of value. Each, at the limit, proves possession of a number.

## II. Identity, taken to the same limit

The corpus took the other axis in two papers. *The Multiplicity Freedom* asked how many identities an adversary can field and proved the cap: under duplication-boundedness and a resource floor, at most its budget over the cost of one gated identity. *The Census of Errors* asked who a mechanism should pay and built the rule: a witness is an independence class of errors, a copy and its original share one payment, and past half the identities the forged world and the true one are formally interchangeable, so that only the price of an identity remains. Neither asked what the price of an identity is a price *of*. This section does, and finds the collapse of the first section arriving from the opposite direction.

A participant is a bundle of forgeable properties — history, stake, reputation, computed work, attested relationships — and one unforgeable property, which is whatever the Sybil-resistance primitive actually checks. Under Sybil pressure, every forgeable property is forged. The cost of manufacturing a property, against the cost of acquiring it honestly, is a finite ratio for every property except the primitive, and an adversary pays the ratio. A mechanism is called Sybil-asymptotic, in this paper's sense, when in the limit it conditions on the primitive alone.

The primitive, examined, is a key. Not metaphorically. The thing a Sybil-asymptotic mechanism checks is that a signature verifies against a public value, which is to say that the participant possesses the integer corresponding to that value. The identity has been stripped of everything that could be copied, and what cannot be copied is the number.

Two limits, taken independently, arrive at the same object. The Goodhart limit reduces *what is proven* to an integer. The Sybil limit reduces *who proves it* to an integer. A mechanism that is both Goodhart-asymptotic and Sybil-asymptotic is a mechanism in which a number proves possession of a number.

This is the entire content of the mechanisms of Volumes I and II. The derivations of value were carried on the forgeable properties. The limits removed the forgeable properties. The derivations went with them.

## III. The anthology as a presheaf

The papers in this series were written, by its house rules, to stand alone in a shared universe. Each paper fixes a local situation — a substrate, a population, a hash, an oracle — and derives, within that situation, what its mechanism rewards and why the reward is value. The derivations are local in the strict sense: they hold on an open set of conditions and are not asserted outside it.

This is the structure of a presheaf. Let X be the space of situations. For each open U ⊆ X, let 𝒟(U) be the set of derivations of value valid on U. A derivation valid on U restricts to a derivation valid on any U′ ⊆ U; the restriction maps are the obvious ones. A presheaf of derivations.

The question of whether the anthology is one proof or many is the question of whether this presheaf is a sheaf with a global section. Specifically: given the local derivations d_i ∈ 𝒟(U_i) for a cover {U_i} of X, whether there exists a single d ∈ 𝒟(X) restricting to each d_i. If such a d exists, the papers are redundant readings of it. If it does not, the papers are the content, and the failure of d to exist is what the anthology is about.

Section I supplies a candidate for d. On every U_i, the mechanism reduces in the limit to a preimage check, and a preimage check is the same object everywhere. Call it κ. The integer κ is a global section of the presheaf of *mechanisms*. The question is whether it is also a global section of the presheaf of *derivations*.

The two presheaves are not the same. A mechanism is the pair (A, V). A derivation is the mechanism together with an argument that the quantity q is value. The forgetful map from derivations to mechanisms is a morphism of presheaves, and κ lives in its image. The question is whether κ lifts.

## IV. The obstruction

It does not. The argument is short.

On each U_i, the local derivation d_i is a chain: an argument that effort is worth rewarding, that m_i tracks effort, that V_i selects m_i above threshold. The Goodhart limit on U_i sends m_i → q_i, where q_i is a preimage predicate. In the limit, the middle link of the chain — *m_i tracks effort* — has been replaced by *m_i is a preimage check*. The first link, *effort is worth rewarding*, now connects to nothing. A preimage check does not measure effort. It measures possession of the preimage, which may have been obtained by effort, by purchase, by theft, by birth, or by the collapse of a wavefunction in a quantum random number generator. The mechanism rewards all of these identically because it cannot distinguish them, and it cannot distinguish them because distinguishing them would reintroduce slack.

So the limit of d_i is not a derivation of value. It is the pair (κ, nothing). On each U_i the argument has been severed at the same joint. Volume V found this joint in prose — four substrates, one attestation problem, the wall never the substrate — and here it is the place where every local chain breaks.

On the overlaps U_i ∩ U_j, the mechanisms agree — both reduce to κ. The derivations do not agree, because on the overlap each paper's argument for why *its* preimage is valuable invokes properties specific to its substrate, and those properties are exactly what the limit discarded. The derivations agree where they are empty and disagree where they have content. The Čech cocycle built from the disagreements on overlaps is nontrivial. The first cohomology of the presheaf of derivations, with respect to the cover by papers, does not vanish:

> H¹({U_i}, 𝒟) ≠ 0.

There is no global derivation of value. There is a global key.

This is the result, and it is negative. The anthology set out to derive value and arrived at a number. The number is correct. The derivation is not a derivation. No framing in which this is secretly a success has been found, and none is offered.

## V. The Census, restated

*The Census of Errors* counted witnesses. A witness, for the purposes of payment, is an independence class of errors; two reporters who err together are one, and two who err apart are two. The word is borrowed here for a second count, and the borrowing is exact in one respect.

A nonvanishing H¹ is not a single fact. It is a class, and the class has representatives, and the representatives are the specific overlaps on which the specific local derivations fail to glue. Each entry in this Census is one such overlap: a place where two papers, agreeing on the mechanism, disagree on the reason, and where the disagreement cannot be resolved by restriction to a smaller set because the reason is already as local as it can be made. Two disagreements that differ only by a change of local reference are one entry, as two reporters who share an error are one witness. The count is of independent disagreements, and *The Extent of Value* gives it a number.

The Census is the cocycle, written out.

It is longer than any single paper in the series because the cover is fine. Each new substrate-class paper adds an open set, and each open set adds overlaps, and each overlap on which the derivations disagree adds an entry. The Census grows with the anthology and cannot be completed before the anthology is, which is to say it cannot be completed.

It is called a census of errors by analogy and not by inheritance. The errors the first Census counted were in the witnesses. The errors this one counts were never in the mechanisms. The mechanisms were correct and remain correct and reduce, every one, to κ. The errors were in the derivations, each of which was locally valid and none of which was the restriction of anything.

## VI. The volume that indexes itself

The Library of the older story contains, somewhere, a single book that is the catalogue of all the others. The narrator does not find it. The narrator reports that others have searched, that some claimed to have found it, that the claims were not verified.

The analogue is now exact. The anthology contains, as a limit, the single integer κ that every paper in it proves. The integer is the catalogue: each paper is an entry pointing to it. A paper could be written — this is that paper — which states that the anthology is κ and that the rest is commentary.

The paper would be locally correct. On the open set of mechanisms, the anthology *is* κ. The paper would also be a derivation, and as a derivation it would be a section over its own open set, and on the overlap with every other paper it would disagree with that paper about why κ is worth having. It would add an entry to the Census. It would not remove one.

The book that is the catalogue of all the books is itself a book, and so is listed in the catalogue, and so cannot be the catalogue. This was noticed in the older story and is not resolved here. The anthology contains the integer. The anthology is not the integer. Both are shown.

## VII. What the key is for

A short section, because the result is negative and should not be padded.

The mechanisms were not wasted. A mechanism that reduces to a key is a mechanism that cannot be gamed, and the demonstration that every incentive-compatible mechanism has this form is a demonstration of what incentive compatibility costs. It costs the derivation. The mechanism designer who wants a system that cannot be gamed is asking for a system that proves possession of a number and is silent about why the number matters. That silence is the price, and it is not negotiable, and *Combination Proofs* and *The Census of Errors* together fix the price — the first on what is measured, the second on who is paid.

The derivation of value, if it exists anywhere, exists in H¹. It is not a section. It is the obstruction to there being one. It is the catalogue of the places where the papers disagree about why the key is worth holding, and it is readable only by reading the papers, all of them, against each other, on their overlaps. There is no shorter form. The integer is the shorter form and the integer does not contain it.

The series continues. Each new paper adds an open set to the cover, a mechanism that reduces to κ, a local derivation that does not glue, and entries to the Census. None of them will produce the global section. This is now known in advance, and the papers are written anyway, since the obstruction is the content and the content is not finished.

---

## VIII. What Is Declined

**That Section I is a theorem.** It is an argument about definitions: a predicate with no slack is a bit, and a bit's carrier is an integer. The argument meets predicates on bit-strings. A predicate on a physical residue read directly — *The Involuntary Ledger*'s thermal channel, where the measurement is the quantity and the quantity is a real number — is not obviously a bit, and the reduction is asserted for it, not shown.

**That the derivations are shown to disagree.** Section IV asserts the cocycle is nontrivial from the observation that each paper's reason invokes its own substrate. No two derivations are written out side by side on an overlap and compared. The argument is short because it is schematic, and the first entry of the Census has not been written in full.

**That the presheaf is a sheaf, or that the topology is given.** Situation, open set and restriction are used without a topology on X being defined. Until one is, Section III is a figure and not a construction, and *The Extent of Value*, which takes the class as a definition, inherits the gap.

**That the result is new.** The principle behind the severed joint — a message computable from public information conveys no knowledge — is Goldwasser, Micali and Rackoff's, and *One's Own Anchor* already cites it. The reduction of a mechanism's security to its anchors is that paper's Theorem 3.4 and *Independent and Expensive*'s inversion. The Library is Borges's. What is claimed is the step from the anchor to the integer, the meeting of the two limits, and the presheaf reading of the anthology.

**That the two limits are one object.** A preimage check and a signature are treated as the same terminus. They differ in one respect the paper does not price: a preimage can be delegated by revealing it, and a signing key can be delegated by lending it, and the two delegations leave different residues.

**That anything is measured.** Nothing is. No module in `code/` corresponds to this paper.

## IX. Open Problems

1. **One entry, in full.** Choose two papers whose situations overlap — *Proof of Preservation* and *Proof of Coherence* on a mechanism that is both anchored and coherent is the natural pair — write both derivations out on the overlap, and exhibit the transition between them. The Census has no entry written in full and the cocycle no computed value.
2. **The topology.** Say what a situation is, what makes a set of situations open, and what restriction does to a derivation. Without these Section III is an analogy; with them it is checkable.
3. **The continuous residue.** Whether a predicate on a physical quantity read directly, with τ = 1 as an identity in *The Involuntary Ledger*'s sense, reduces to a bit, or whether the thermal channel is a counter-case to Section I.
4. **Conjecture 7.4.** *Combination Proofs* conjectures that every Goodhart-asymptotic mechanism factors through a conjunction of verifiably independent projections of some substrate. If each projection in its limit is a key, the conjecture reads: every such mechanism is a conjunction of keys. Whether that confirms the conjecture or trivialises it is not settled here.
5. **Preimage against signature.** Price the two delegations named in the fifth decline, and determine whether the Sybil limit and the Goodhart limit meet at one integer or at two kinds of integer.

## Neighbours

*Combination Proofs* asks what a mechanism measures, defines Goodhart-asymptotic by unbounded evasion cost in a controlled resource, and carries the universality conjecture that Open Problem 4 takes up. *The Census of Errors* asks who a mechanism pays and finds the cliff at half the identities; *The Multiplicity Freedom* proves the cap on the fleet. The three are the paper's premises on the two axes.

*One's Own Anchor* and *Independent and Expensive* carry the reduction to the anchor as a theorem and an inversion; Section I is their next step. *Gauge-Fixing the Section Space* enumerates the four anchors Section I reduces. *What Cannot Be Helped* finds the single joint in prose — four substrates, one attestation problem — and Section IV finds it as the place every local chain breaks.

*No Global Section* and *The Obstruction, Computed* are the corpus's other H¹: on gate scenarios, computed, machine-checked on the cycle, and found to be a detector and not a certificate. This paper's H¹ is on derivations and is exhibited, not computed; the same word, a different presheaf, and the lesson that a vanishing class licenses nothing carries over — a vanishing [v] would license a monologue, not a truth. *The Extent of Value* takes the class as a definition and follows it.

## References

- Borges, J. L. (1941). La biblioteca de Babel. In *El jardín de senderos que se bifurcan*. Buenos Aires: Sur.
- Douceur, J. R. (2002). The Sybil attack. *Proceedings of IPTPS*.
- Goldwasser, S., Micali, S., and Rackoff, C. (1989). The knowledge complexity of interactive proof systems. *SIAM Journal on Computing* 18(1).
- Goodhart, C. A. E. (1975). Problems of monetary management: the U.K. experience. *Papers in Monetary Economics*, Reserve Bank of Australia.
- Manheim, D., and Garrabrant, S. (2018). Categorizing variants of Goodhart's law. arXiv:1803.04585.

---

*Key and Census, v0.1. A paper in the Derivation of Value series. Set in the same universe as* Combination Proofs *and* The Census of Errors*, and dependent on neither. No measurement is made; nothing in `code/` corresponds.*
