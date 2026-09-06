---
layout: document
title: "Independent and Expensive"
subtitle: "An Exclusion Principle for the Projections of One Substrate"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /independent-and-expensive/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-08-14
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "The framework's reordered central question — is any projection both independent and expensive to forge? — answered in a model small enough to prove things in: independence and trace gap are claims on one budget, the substrate's paid work, and disjoint claims on a finite pool cannot both be large. Richness partitions the budget; nothing multiplies it. The escape is an anchor per projection, and it is an escape by purchase, not by cleverness — measured on the sheaf, where the dial that buys persistence its gap spends its independence in the same stroke."
status: "v0.1 · working draft"
order: 20
---

## Abstract

*Combination Proofs* v0.4 §7.1 ends on a conjecture stated from two data points: a projection must be independent of its fellow projections **and** expensive to forge, the framework spent its whole life stating only the first as an open problem, and the two appear to pull against each other. The static spectral projection failed ι and inherited coherence's τ; the temporal projection passes ι perfectly and has no τ. Whether any projection clears both — the state of the program's open problem 4 — has never been asked as a theorem. This paper asks it in a model small enough to answer, and the answer is an exclusion principle. Decompose a substrate's state into **paid** degrees of freedom, whose admissible values cost work to produce, and **free** ones, which cost nothing. A projection's trace gap is then the size of its *claim* on the paid pool, and the independence of two projections is the *disjointness* of their claims — so soundness and independence draw on the same finite stock, and two projections each fully sound and fully mutually independent would need two units of a one-unit pool. Two theorems follow by inclusion–exclusion: a pairwise bound, τ₁ + ι(2\|1)·τ₂ ≤ 1, with equality exactly when the claims exhaust the pool; and a budget law, that the conjunction's fake-cost Γ never exceeds the substrate's honest work content at any order K, so that **richness partitions the budget and nothing multiplies it**. Proof of work is not a counterexample — its search is a second pool, which is to say an anchor — and that observation is the escape and its price: independence between sound projections is recovered only by *splitting* paid work into disjoint pools, an anchor per projection, with the trace gaps summing to at most one. The model is then pointed at the sheaf. The one dial the program owns that gives the temporal persistence projection a price — *Gauge-Fixing* §4.3's generative anchor keyed to the epoch beacon — is measured to buy τ(π_persist) at exactly Proposition 5.2's anchor share while driving ι(ker\|persist) from its measured 1.000 to 0.000 in the same stroke, because the encodings that price persistence are the whole of the kernel's fake-cost. The instrument also returned one number nobody asked for: under the epoch-keyed anchor, full stasis scores **9.1× honest persistence** and is excluded by admissibility rather than by price, because the beacon's own rotation dominates the eigenspace the projection reads — the anchored persistence reading is mostly measuring its anchor, which is *Sign and Work* §8.3's perverse route surfacing on the temporal axis. The prior art is named and the boundary drawn: that an informative signal must be differentially costly is Spence, Zahavi and the informativeness principle, sixty years assembled; the quantitative form — the corpus's two quantities as claims on one budget, the partition law, and the measured trade on a cohomological substrate — is not in that literature. Every claim here is proved in the model or measured on the instrument, and the model is declared as the simplification it is.

---

## 1. Two Requirements, One Question

The framework's central design question was reordered this month, and the reordering left a question nobody has asked.

For most of its life the program treated independence as the hard part of admitting a projection: *Combination Proofs* §7.1 — the quantitative independence measure ι — has been the framework's first open problem since v0.1, and five separate results are denominated in it. Then the third attack design succeeded (`code/temporal_iota.py`), and what it measured reordered the difficulty. The temporal persistence projection is perfectly independent of the kernel — ι(ker\|persist) = 1.000 at every coalition size — and free to forge: a coalition that never changes its restriction maps outscores honest participants who update theirs, so τ(π_persist) ≈ 0, and by *Sign and Work* Proposition 4.1 it inflates the adversary's fleet without bound. Independence was never the binding constraint. A projection must be independent **and** expensive, the framework had stated only the first as an open problem, and on the evidence of two projections the requirements pull against each other: the static spectral projection fails ι and inherits coherence's τ, the temporal one passes ι and has no τ.

The state of the program ranks the resulting question fourth by leverage and notes it has never been asked: *is there a projection that clears both, and if not, what bounds Combination Proofs of order K > 1 on coherence substrates?* This paper asks it. The method is the program's usual one in reverse — instead of importing a formalism and testing it against the corpus, it builds the smallest model in which the corpus's two quantities can be computed exactly, proves the exclusion there, and then measures the model's prediction on the sheaf reading the program actually uses.

The conclusion, stated before the machinery: **the tension is not an empirical accident of two projections. It is arithmetic.** Independence and trace gap are both claims on the same finite resource — the substrate's paid work — and the only question a substrate leaves open is how that budget is partitioned.

---

## 2. Prior Art, and the Boundary of the Claim

The qualitative core of this result is old, and saying so precisely is the condition for saying what is new.

That a signal carrying information at equilibrium must be differentially costly is the founding result of signalling theory: Spence's job-market signalling [1], Zahavi's handicap principle [2], and Grafen's demonstration that the handicap logic survives formalisation [3]. A signal free to produce is producible by every type, and a signal every type can produce separates no types — which is, transposed into this program's vocabulary, exactly "a projection coherence does not constrain is one an adversary satisfies without coherence work." Contract theory has the complementary half: Holmström's informativeness principle [4] makes a signal's contractual value turn on its statistical dependence on the agent's action, so a signal independent of the action is worthless for incentives however cheaply it is observed; and Holmström–Milgrom's multitask analysis [5] shows that incentivising the measurable tasks distorts effort away from the unmeasurable ones — the budget being, there, the agent's attention. The harvest line has this literature scheduled as its own paper (P9, *The Handicap*), and the present paper does not discharge that plan; it takes from the literature only the boundary of its own novelty.

What that literature does not contain, and what is claimed here: **the two quantities this corpus has spent nineteen documents constructing — ι as a fraction of unrecoverable fake-cost (*Combination Proofs* Definition 2.5), τ as the ratio of forging to earning (*Sign and Work* Definition 3.3) — are claims on a single budget, and their trade-off is a partition law with equality conditions**, not a pairwise tension between one signal and one cost. The signalling literature prices one signal against one pooling equilibrium; the partition law prices *K projections of one substrate against each other*, which is the object a Combination Proof actually is. And the measured instance — the trade executed by a single dial on a sheaf-cohomological substrate — has no antecedent in that literature at all. The prior-art check was run before drafting, per the rule that has now caught this program twice; this section is its record.

---

## 3. The Paid-Degrees-of-Freedom Model

The model deliberately contains nothing but the distinction the corpus keeps deriving.

**Definition 3.1 (pool).** A substrate's state decomposes into a set P of *paid* degrees of freedom — those whose admissible values cost work to produce: encodings, reconciliations, searches — and a set F of *free* ones, whose admissible values cost nothing. The substrate's work content is W = \|P\|, each paid degree costing one unit.

**Definition 3.2 (claim).** A projection, operationally, is the set S of degrees of freedom that determine whether it accepts. Its *claim* is S ∩ P. An attacker producing exactly the claim, and completing the free remainder arbitrarily, produces an accepted trace at cost \|S ∩ P\| — and no accepted trace is cheaper, since every degree the projection reads must be produced.

The corpus's two quantities are then computable. The trace gap, with w taken as the whole work the reading purports to evidence: τ(π) = \|S ∩ P\| / W. The graded independence, per Definition 2.5's "fraction of π_j's fake-cost not recoverable from having faked π_i": ι(j\|i) = \|S_j ∩ P ∖ S_i\| / \|S_j ∩ P\|, undefined when the claim is empty — a projection with no claim has a fake-cost of zero, and fractions of zero cost are not quantities. That degenerate corner is not a technicality; it is where the measured specimen lives, and §5 returns to it.

**Theorem 3.3 (pairwise exclusion).** For projections π₁, π₂ of one substrate,

> τ(π₁) + ι(2\|1) · τ(π₂) ≤ 1,

with equality exactly when the two claims jointly exhaust the pool.

*Proof.* The left side is (\|S₁ ∩ P\| + \|S₂ ∩ P ∖ S₁\|)/W = \|(S₁ ∪ S₂) ∩ P\|/W ≤ 1. ∎

**Theorem 3.4 (budget).** For projections π₁, …, π_K, the conjunction's fake-cost — the sum of sequential marginal costs, which is Lemma 3.1 of *The Multiplicity Freedom* built from the model's own quantities — satisfies

> Γ = Σ_k ι_k τ_k · W = \|(∪_k S_k) ∩ P\| ≤ W,

at every K. Equivalently: **the discounted trace gaps of any conjunction sum to at most one.**

*Proof.* Inclusion–exclusion again; the k-th marginal is the part of the k-th claim not already produced. ∎

The theorems are arithmetic, and their value is in what the arithmetic forbids and explains.

**Corollary 3.5 (the exclusion proper).** Two projections with τ = 1 each and ι = 1 between them would require two units of a one-unit pool. Full soundness and full mutual independence are jointly unattainable for projections of one substrate; K fully-independent projections of common gap t force K·t ≤ 1.

**Corollary 3.6 (publicity-positivity saturates).** *Combination Proofs* Proposition 4.2(ii) asserts that publishing a new independent projection *strictly* increases the attacker's fake-cost, the gap being the marginal fake-cost of π_{K+1}. By Theorem 3.4 that marginal is at most the unclaimed remainder W − Γ_K, which is zero once the pool is exhausted. Publicity-positivity is non-decreasing always and strict only while unclaimed paid work remains: the research literature is a security accumulator with a ceiling, and the ceiling is the substrate's work content. This is an amendment to that proposition and is recorded as one.

**Remark 3.7 (proof of work is not a counterexample — it is the escape).** A conjunction of a coherence reading with proof of work has both projections sound and mutually independent, which appears to violate Corollary 3.5. It does not: the hash search is paid work the coherence substrate does not contain — a *second pool*. Definition 3.1 counts it into W, the claims are disjoint, and the trace gaps, each normalised by the *joint* work both projections together evidence, split the enlarged budget rather than exceeding it. A second pool of paid work, imported from outside the substrate's native structure, is what this program has been calling an **anchor** since *Gauge-Fixing*. The exclusion is therefore escapable, and the escape has a price and a name: independence between sound projections is bought by adding paid work, an anchor per projection — never by adding readings.

**Remark 3.8 (where the normalisation binds).** τ's denominator is the work the projection *purports to evidence* (*Sign and Work* Definition 3.1). Projections each evidencing only their own private pool have τ = 1 apiece and the exclusion says nothing — but such projections are gates on K separate substrates, not K projections of one, and a Combination Proof's projections are offered precisely as K readings of one substrate's honesty. The exclusion binds exactly where the framework's construction lives.

---

## 4. Calibration

A model in which the theorems are provable is also a model in which an instrument can be checked against answers known by construction, and per the program's standing rule the instrument is pointed at the known answers first (`code/exclusion.py`, seeded; every number below reproduces).

The instrument is a brute-force attacker: minimum production cost over all subsets of degrees of freedom such that every reading accepts, seeing acceptance behaviour only — never the sets. On an 8-paid, 4-free universe, against six designed specimens:

| specimen | τ₁ | τ₂ | ι(2\|1) | designed | τ₁ + ι·τ₂ |
|---|---|---|---|---|---|
| disjoint, half each | 0.500 | 0.500 | 1.000 | 0.500 0.500 1.000 | **1.000** |
| nested | 0.750 | 0.375 | 0.000 | 0.750 0.375 0.000 | 0.750 |
| overlap 2 of 4 | 0.500 | 0.500 | 0.500 | 0.500 0.500 0.500 | 0.750 |
| free rider (τ = 0) | 0.625 | 0.000 | — | 0.625 0.000 — | 0.625 |
| exhaustive pair | 0.625 | 0.375 | 1.000 | 0.625 0.375 1.000 | **1.000** |
| both read everything | 1.000 | 1.000 | 0.000 | 1.000 1.000 0.000 | 1.000 |

Worst deviation of measured from designed: **zero**. The bound is never exceeded and is attained exactly on the pairs designed to exhaust the pool. Random conjunctions of K = 2 through 5 projections return Σ ι_k τ_k = Γ/W between 0.375 and 0.875, never above one. And the escape specimen behaves as Remark 3.7 requires: two projections each reading its own pool of four measure τ = 0.500 and 0.500 with ι = 1.000 in both directions — independent *and* each expensive, with the gaps summing to exactly the budget.

The free-rider row is the measured world in miniature: a projection reading only free degrees of freedom has τ = 0 and an undefined ι, because the independence of a free thing is free. This is the model's account of a fact the corpus found empirically and found troubling — that ι(persist\|ker) varies with the attack that measures it. Where claims are empty or nearly so, ι is a ratio of vanishing costs, and *which* vanishing cost an attack samples is the attacker's choice. The conservative repair *The Multiplicity Freedom* v0.4 recommends — ι as an infimum over the attacker class — is, in this model, simply the correct treatment of a boundary where the quantity degenerates.

---

## 5. The Sheaf Instance

The model predicts something the corpus is equipped to test: the one dial the program owns that gives the temporal persistence projection a price should destroy its independence in the same stroke, because the price and the dependence would be the same object.

**The construction.** The specimen pair is `temporal_iota.py`'s: π_ker, coherence at an instant, and π_persist, the overlap of consecutive bottom-k eigenspaces across epochs. The dial is *Gauge-Fixing* §4.3's generative anchor keyed to §4.1's beacon: at each epoch, an admissible section must carry the beacon's freshly-drawn column for *this* epoch, at encoding cost En per vertex per epoch. Holding still stops being free, because last epoch's encoding is stale this epoch. The reading is the one *Sign and Work* §5 prices — declared frames, induced connection, so every declared configuration is coherent and the kernel is free apart from the anchor (Proposition 5.1's telescoping). Honest participation pays the encodings plus reconciliation; forgery strategies pay what they pay, and acceptance is measured, not assumed (n = 256, \|E\| = 371, c = 3, eight epochs).

**The prediction**, stated before running: τ(π_persist) should rise with En as the anchor share n·En/(n·En + \|E\|·c) of Proposition 5.2, and ι(ker\|persist) should fall to zero at every En > 0, because the encodings that price persistence are the whole of the kernel's fake-cost.

**The result.**

| En | τ(persist) | Prop 5.2 share | τ(ker) | ι(ker\|persist) |
|---|---|---|---|---|
| 0 | 0.000 | 0.000 | 0.000 | undefined — the kernel is free |
| 1 | 0.187 | 0.187 | 0.187 | 0.000 |
| 4 | 0.479 | 0.479 | 0.479 | 0.000 |
| 16 | 0.786 | 0.786 | 0.786 | 0.000 |
| 64 | 0.936 | 0.936 | 0.936 | 0.000 |

The gap bought tracks the anchor share to three decimals at every setting, and the independence is spent the moment the gap exists. At En = 0 the pair sits at the free corner — τ = 0, ι undefined in cost terms, measured as 1.000 in `temporal_iota.py`'s progress terms, the two operationalisations parting company exactly where the model says the quantity degenerates. At every En > 0 the cheapest strategy that forges persistence (encode each epoch, freeze the free completion) has already paid everything the kernel costs, so the marginal price of the kernel is zero. **One pool. τ is a claim on it; ι is the disjointness of claims; the dial that buys the first spends the second.** This is the exclusion executed by a single parameter on the substrate the program actually uses, and it is the measured form of open problem 4's answer: on this substrate, with this anchor family, no setting of the dial clears both requirements, exactly as Theorem 3.3 requires of claims on one pool.

**And one number nobody asked for.** Full stasis — frames frozen at epoch 0, beacon included — scores **9.135× honest persistence progress** and is excluded by admissibility, not by price. The flag is the program's favourite species of result, an instrument returning an absurdity, and what it reveals was not predicted: under an epoch-keyed anchor the beacon's own rotation dominates the bottom eigenspace, so honest persistence collapses toward the frustrated baseline and most of what the anchored π_persist reads *is the beacon*. The anchor that gives persistence its price also eats the signal persistence was supposed to carry — the mechanism measures its anchor and calls it persistence. That is *Sign and Work* §8.3's perverse route to soundness surfacing unbidden on the temporal axis, and it sharpens the design problem: an anchored temporal reading must show its signal *survives* its anchor, and this one does not.

---

## 6. What the Exclusion Explains

Read back through the corpus, the partition law is the mechanism behind results that arrived separately and looked unrelated.

**The trace gap is bought entirely by the anchors** (*Sign and Work* §5.3). In the model's terms: the anchors are the substrate's only paid pools. Coherence work — reconciliation — is paid but leaves as residue only agreement, and agreement is free to fabricate, so the reconciliation pool is paid work no output reading can claim. Whatever claims exist are claims on anchors, which is why every measured τ in the corpus is an anchor share. Volume V's vocabulary says the same thing in one line: the coherence layer's work leaves no residue distinguishable from a fiction, and **τ's budget is residue-bearing work**.

**Richness is paid for in trace gap** (*Sign and Work* §5.4). Enriching the readings of a substrate multiplies claims on a pool that does not grow. The coupling knob raises the spectral dimension and dilutes each reading's share; the measured trade of ρ against τ is Theorem 3.4 with the pool held fixed while K rises.

**Two ways for richness to buy nothing** (*The Multiplicity Freedom* Corollary 5.4). Redundancy is a shared claim — ι = 0, the marginal is zero. Forgeability is an empty claim — τ = 0, there is nothing to add. The corollary's two failure modes are the two ways a term ι_k τ_k vanishes, and Theorem 3.4 says they are exhaustive.

**Conjecture R acquires a mechanism.** The ruliad's conjecture — that the attestation problem is invariant under change of formalism — has six confirmations and no stated reason. The model supplies a candidate reason: a formalism change replaces the *readings*, and readings cannot create paid degrees of freedom; they can only re-partition claims on the pool the substrate already carries. Every import that appeared to dissolve the attestation problem moved it into a quantity the importing formalism does not itself supply — which is to say, into the unclaimed or unclaimable part of the budget. This does not prove Conjecture R; it says what a refutation would have to do: exhibit a formalism whose adoption *adds paid work* rather than re-reading it, which is precisely what an anchor does and a reading cannot.

**And open problem 4 has an answer with a fork in it.** Within one pool: no projection pair clears both requirements, by Corollary 3.5, and the program's two measured projections sit at the two ends of the frontier. Across pools: clearing both is purchasable, an anchor per projection, with the gaps summing to at most one. The design consequence inverts the framework's self-description: **a Combination Proof of order K is not K readings of one substrate — it is K anchors wearing readings**, and its security budget is the sum of what its anchors cost, partitioned. The framework's worked instance read one pool twice, and its measured ι ≈ 0 was this fact wearing an empirical costume. The gauge-fixing architecture — four anchors, each pricing its own freedom — was a multi-pool conjunction before the framework had the vocabulary to say so, which is why the anchors carry all the τ.

---

## 7. What Is Declined

**That the model is the mechanism.** It is not, and the distance is declared. Paid-versus-free is a dichotomy where real cost structures are graded; claims are sets where real fake-costs are partially recoverable, convex, and attack-dependent; W is additive where real work compounds. The theorems are exact in the model and are offered as the *shape* of the constraint, not its final form. Whether the partition law survives a graded cost structure is §8.1, and until it is settled the exclusion is proved in a toy and measured in one instance.

**That the exclusion is proved for the sheaf.** §5 measures one reading, one anchor family, one dial, and finds the model's prediction executed to three decimals. That is a confirmation, not a derivation; a different anchor family could in principle price persistence out of a pool the kernel does not share, and §8.2 says what that would require.

**That the two operationalisations of ι agree.** Cost-based ι (Definition 2.5, used here) and progress-based ι (used by `temporal_iota.py`) coincide away from the free corner and part company at it — one undefined, the other 1.000. The disagreement is not a bug in either instrument; it is the degeneracy of the quantity where claims vanish, and it is this paper's account of why measured ι moved with attack intensity. But the account is a diagnosis, not a formalisation, and P6's task is unchanged.

**That Spence, Zahavi, Grafen or Holmström are escaped or superseded.** The qualitative principle is theirs, sixty years assembled, and §2 exists to say so. The claim here is the quantitative form on this program's quantities, with equality conditions and a measured instance — no more.

**That the budget cannot grow.** It can, by adding paid work — anchors. The exclusion bounds readings of a fixed substrate; it prices the escape rather than forbidding it. What it does forbid is growth by cleverness: no arrangement of readings, formalisms, or thresholds adds a unit to the pool.

**That this discharges P6.** The formalisation of ι is still absent. This paper constrains it — ι must degenerate where claims vanish, carry asymmetry, and reduce to claim-disjointness in the set-model limit — and hands those constraints to *The Metric on the Projections* rather than discharging them.

**That measured τ certifies anything.** Every τ in §5 is a minimum over written-down strategies, so measured τ ≥ true τ, always, and a cheaper forgery would only lower the table's numbers — which would tighten the exclusion, not loosen it. The direction of error runs with the theorem, which is the one comfort the instrument's limitation affords.

---

## 8. Open Problems

**8.1. The graded model.** Replace set-claims with a cost function on attack strategies — fractional recoverability, convex production, attacker-dependent shortcuts — and determine whether the partition law survives as an inequality on suitably-defined shares. The model's prediction held to three decimals on the sheaf, which suggests the set-model is less of a toy than it looks; a graded derivation would say why.

**8.2. The two-pool sheaf.** Give persistence an anchor of its own, disjoint from the kernel's — a per-epoch encoding on the temporal structure that the static encoding does not contain. The model predicts ι(ker\|persist) = 1 restored with both gaps positive and summing to at most one. Building it would exhibit, on the program's own substrate, the first projection pair that is independent *and* expensive — at a price the budget makes explicit.

**8.3. Does the budget compose?** *Gluing the Gates* showed richness does not compose across a holarchy and *Sign and Work* §8.4 asked the same of τ. The budget's composition is the sharper form of both: whether a holarchy's pool is the sum of its levels' pools, or the minimum, decides whether nesting divides the budget or merely partitions it, and Proposition 6.1 of that paper suggests the unkind answer.

**8.4. The signal that survives its anchor.** §5's unanticipated finding: the epoch-keyed anchor dominates the eigenspace the persistence projection reads. Whether any temporal reading carries a signal that survives its own anchor is *Sign and Work* §8.1 asked on the time axis, and it is prior to 8.2 — a second pool is worth nothing to a projection whose signal its anchor has already eaten.

**8.5. What the reconciliation pool could evidence.** The coherence work is paid and unclaimable by any output reading, which is why it appears only in denominators. A reading that made reconciliation *leave a residue* — restriction maps measured at overlaps rather than induced, per *Sign and Work* §8.1 — would convert the corpus's largest pool of paid-but-unclaimed work into budget. If that conversion is impossible, the coherence layer's work content is permanently outside its own security budget, and the layer should be priced as coordination, never as attestation.

---

## References

[1] M. Spence. *Job Market Signaling.* Quarterly Journal of Economics 87(3), 355–374, 1973.

[2] A. Zahavi. *Mate Selection — A Selection for a Handicap.* Journal of Theoretical Biology 53(1), 205–214, 1975.

[3] A. Grafen. *Biological Signals as Handicaps.* Journal of Theoretical Biology 144(4), 517–546, 1990.

[4] B. Holmström. *Moral Hazard and Observability.* Bell Journal of Economics 10(1), 74–91, 1979.

[5] B. Holmström and P. Milgrom. *Multitask Principal–Agent Analyses: Incentive Contracts, Asset Ownership, and Job Design.* Journal of Law, Economics, & Organization 7 (special issue), 24–52, 1991.

Theorems verified and measurements reproducible from `code/exclusion.py`.
