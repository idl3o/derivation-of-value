---
layout: document
title: "The Budget Across Levels"
subtitle: "Receipts Sum, Interfaces Nest, and the Adversary Picks the Level"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /the-budget-across-levels/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-09-07
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Three papers left the same question at the same door: whether a holarchy's security budget is the sum of its levels' budgets or the minimum. It is neither, because the question was asked of the wrong pool. Receipts are disjoint per level and sum, and every one of them is idle; native work nests, since a coarser level reads a subset of the finest level's interfaces and one derivation serves every level that reads it, so the evidencing budget of a holarchy is its finest level's boundary however many levels stand above it. A coalition's boundary lies entirely above its own level and halves per level exactly, so under a mechanism the adversary may satisfy at one level of its choosing it presents at or below its own level and pays nothing; under the conjunction it pays the every-edge price, which the sum over levels reproduces to the edge. What presenting as a holon saves is receipts. And the criterion that would tell legitimate composition from a Sybil refinement — that the adversary controls both sides of an interface — is exactly the condition under which an interface evidences nothing, and it is not a residual: the fiction glues better than honesty, and the coalition buys honest-level disagreement with its own noise for free."
status: "v0.1 · working draft"
order: 23
---

## Abstract

*Independent and Expensive* §8.3, *The Second Pool* §9.3 and *One's Own Anchor* §9.3 ask, in three forms, what nesting does to a security budget: whether a holarchy's pool is the sum of its levels' pools or the minimum, whether each level's receipts add, and whether a coalition presenting as one holon pays the holon's boundary or its constituents'. *Gluing the Gates* Proposition 6.1 predicted the minimum. This paper builds the holarchy the program already owns — the hierarchical complex is one by construction, its edges partitioned by the merge that introduced them and the interfaces between level-ℓ holons nested downward to the leaves — and finds the dichotomy was posed of the wrong pool. Anchor pools are disjoint per level and sum, and every one of them evidences nothing; native pools nest, because a coarser level reads a subset of the finest level's interfaces and a derivation on an edge serves every level that reads it, so the compositional holarchic mechanism's native budget is the finest level's, however many levels it has, and the independence between a level's gate and the leaf gate is exactly that level's receipt share. On the specimen a level-by-level sum of interface work would overstate the native budget by a factor of 2.30. A coalition that is a level-j block has its whole boundary at merge levels above j, halving per level as an exact double-counting identity rather than an expectation, so the adversary of Proposition 6.1 — free to satisfy one level's gate of its choosing — presents at or below its own level and derives nothing, while under the conjunction it derives every boundary edge and the sum over levels returns the every-edge price of the predecessor to the edge: three, two, three and two, at twelve, four, three and one per identity. An aggregate gate at a level prices only coalitions whose boundary exceeds two fifths of that level's edges, which on the specimen is the two largest blocks at the top two levels and nothing below. The boundary does not move with the level of presentation; the receipts do, and the receipts are idle. *The Multiplicity Freedom* §8.4's criterion for a Sybil refinement — the adversary controls both sides of an interface — is the condition under which an interface is interior to the coalition and evidences nothing, and it is not checkable from residuals: the naive fiction glues with residual zero against honest's 0.203, a two-sided gate refuses that, and a fabrication of honest scale with honest-level noise added, at no cost, sits at 0.199 inside honest's spread. The prior art is drawn — the minimum over units is the single-shard takeover of the sharding literature and Hirshleifer's weakest link, a group gate amortised over many identities is Douceur's Lemma 3, and cheap cuts in community-structured graphs are Viswanath et al. — and what is claimed is the cross-level composition with per-level anchors, the nesting theorem, the level-resolved boundary, and the measurements.

---

## 1. Three Questions at One Door

The exclusion line closed each of its papers on the same open problem under a different name. *Independent and Expensive* §8.3 asked whether the budget composes: whether a holarchy's pool is the sum of its levels' pools or the minimum, which decides whether nesting divides the budget or merely partitions it. *The Second Pool* §9.3 sharpened it: each level of a holarchy would carry its own two receipts, and *Gluing the Gates* Proposition 6.1 suggests the joint budget is the minimum over levels rather than the sum. *One's Own Anchor* §9.3, having priced a coalition by its boundary at one level, asked whether a coalition presenting as a holon pays the boundary of the holon or of its constituents, and said that *The Multiplicity Freedom* §8.4 — whether a holon presenting as many sub-holons is composition or a Sybil attack — turns on the answer.

The three are answered here together, and the answer is that the sum-or-minimum dichotomy was asked of the wrong pool. *One's Own Anchor* split a substrate's paid work into anchor work and native work and proved that only the second evidences anything. Anchor work is disjoint across levels and sums — that half of the dichotomy is arithmetic, and Proposition 6.1's minimum is what an adversary pays in receipts when a mechanism lets it choose its level. Native work does not sum and does not take a minimum. It *nests*: the interfaces between level-ℓ holons are a subset of the interfaces between level-0 holons, and a derivation on an edge serves every level that reads that edge, so a holarchy's native budget is the finest level's whatever stands above it. Nesting adds anchor pools and no native pool.

Read against a coalition, this says the boundary does not move with the level of presentation. A coalition that is a level-j block has every one of its boundary edges at a merge level above j, halving per level, and whether it presents as one holon or as 2^j leaves, the edges it must derive under a compositional mechanism are the same edges; what presenting coarse saves is receipts. Under a mechanism the adversary can satisfy at one level of its choosing, it presents at or below its own level and derives nothing. And the criterion *The Multiplicity Freedom* proposed for telling a Sybil refinement from legitimate composition — the adversary controls both sides of an interface — is the condition under which an interface is interior to the coalition, which is exactly the condition under which it evidences nothing; it is not a residual, and the paper measures why.

Everything below is proved in the paid-DOF model of *Independent and Expensive* or measured on the program's own complex with the residual reading of *One's Own Anchor*, predictions stated in `code/holarchy.py` before running.

---

## 2. Prior Art, and the Boundary of the Claim

The minimum over parallel units is established several times over, and the boundary is drawn so that §§3–6 claim only what lies past it.

That the security of a partitioned system is that of its cheapest partition is the single-shard takeover of the sharding literature: Buterin's account [3] puts it as a coalition holding a small fraction of the whole concentrating on one chain of many, and the remedy the literature converged on is random committee assignment, which converts the minimum toward the sum. Hafid, Hafid and Samih [4] and OmniLedger [5] compute the failure probability that *at least one* committee is captured, which is the same bound as a union; Monoxide [6] states outright that naive zoning makes one zone attackable at a fraction of the network's work and engineers the minimum back up to the whole. The economic form is older: Hirshleifer's weakest link [1], in which social provision is the minimum of individual provisions, carried into security effort by Varian [2]. None of these has levels. Their units are parallel, at one level, and an adversary chooses among them; the holarchy here has units inside units, an adversary who chooses a *level*, and an anchor at every level.

That a coalition clearing one group-level gate amortises it over unboundedly many identities is Douceur's Lemma 3 [7]: if acceptance is vouched by q accepted identities, a coalition holding q of them presents arbitrarily many. The many-as-one direction — a coalition presenting as a single agent to improve its reward — is collusion-proofness, contrasted with false-name-proofness by Yokoo, Sakurai and Matsubara [8] and shown by Zhang and Tang [9] to be unattainable jointly with Sybil-proofness on a query tree. That a cut prices a coalition is the attack-edge bound of SybilGuard and SybilLimit [10] and the vertex-cut mechanism of Conitzer et al. [11]; that community structure makes the cut cheap and that Sybils target their links is stated by Viswanath et al. [12] and given its conductance form by Alvisi et al. [13]. Rowe's layered attestation [14] characterises an adversary's cheapest evasion as corruption at a particular depth of a measurement hierarchy, which is Proposition 6.1's adversary in a setting without cost. Gaži, Kiayias and Zindros [15] give the firewall property — a sidechain's compromise does not propagate — which is the design that would *contain* the minimum rather than convert it, and Tirole [16] is the economics of collusion inside a three-tier hierarchy, with side-contracting costs at one tier rather than a choice among tiers.

What is claimed. That in a holarchy with an anchor per level, anchor pools sum and native pools nest, so the evidencing budget of the compositional mechanism is the finest level's and the independence between a level's gate and the leaf gate is that level's receipt share (§3). That a block coalition's boundary is level-resolved by an exact identity, halving per level above its own (§4). That Proposition 6.1's minimum is zero on the native side for every block coalition, that the conjunction's sum over levels is the every-edge price to the edge, that an aggregate gate at a level prices only the two largest blocks, and that the boundary does not move with the level of presentation (§5). And that the both-sides-controlled criterion is not a residual (§6). The minimum over units, the group gate, the cut and the cheap community cut are cited, not claimed.

---

## 3. The Holarchy, and What Nests

`code/holarchy.py`, Part 1. The hierarchical complex of *Requisite Richness* — 2^8 leaves, each merge of two sibling blocks joined by two random cross-edges, seed 7 — is a holarchy by construction, and the paper uses that structure rather than building another. A **level-j holon** is an aligned block of 2^j leaves. Every edge was introduced by exactly one merge, at the level ℓ where its endpoints first share a block, so the edge set **partitions by merge level**, E = E₁ ⊔ … ⊔ E₈, and the **interfaces between level-ℓ holons** — the edges not interior to any level-ℓ holon — are

> I_ℓ = E_{ℓ+1} ⊔ … ⊔ E₈,

nested downward, I₀ = E ⊃ I₁ ⊃ … ⊃ I₇ = E₈. A level-ℓ mechanism admits level-ℓ holons as identities. Each holds a receipt, an anchor pool A_ℓ disjoint from every other level's by construction, and the mechanism reads one of two things: its **own merges** E_ℓ, which asks whether each level-ℓ holon glues internally across the merge that formed it, or its **interfaces** I_ℓ, which asks whether the holons glue to each other. A level-ℓ holon's section on an interface edge is its endpoint leaf's section, so the derivation an honest leaf makes on an edge is the derivation every level reads there.

**Proposition 3.1 (receipts sum).** For a holarchic mechanism gating at levels J, the anchor pool is ⊔_{ℓ∈J} A_ℓ, and its fake-cost is Σ_{ℓ∈J} |A_ℓ|. *Disjoint pools; Independent and Expensive* Theorem 3.4 with one pool per level. ∎

**Proposition 3.2 (interfaces nest).** The native pool of the level-ℓ interface gate is I_ℓ ⊆ I₀. For any J, the native pool of the conjunction is I_{min J}, and for the compositional mechanism — every level gated — it is I₀ = E, the finest level's, independent of the number of levels. The own-merge gates partition I₀: the conjunction of all of them is I₀ as well. *Nested sets have union equal to the largest; a partition has union equal to the whole.* ∎

**Proposition 3.3 (independence between levels is the receipt share).** With Π_ℓ the level-ℓ interface gate reading A_ℓ ∪ I_ℓ, *Combination Proofs* Definition 2.5 gives

> ι(Π_ℓ \| Π₀) = \|A_ℓ\| / (\|A_ℓ\| + \|I_ℓ\|),

since I_ℓ ⊆ I₀ leaves the receipt as the only part of Π_ℓ's claim that Π₀ has not already paid. ∎

The consequence, stated once. Nesting a mechanism adds anchor pools, which are disjoint and sum, and adds no native pool. By *One's Own Anchor* Theorem 3.4 every anchor pool has native share zero. So the **evidencing budget of a holarchy is the finest level's native pool**, and the independence a level buys against the level below is exactly the idle part of its claim. The sum-or-minimum question of *Independent and Expensive* §8.3 has the answer *sum* for the pool that evidences nothing and *union* for the pool that does.

**The miniature, on the attacker.** Three holon levels; receipts |A₀| = 4, |A₁| = 2, |A₂| = 1; interfaces |I₀| = 6 ⊃ |I₁| = 3 ⊃ |I₂| = 1; merges J₁, J₂, J₃ of sizes 3, 2, 1; two free degrees of freedom. The brute-force attacker of `code/exclusion.py` sees acceptance only.

| gate | measured | designed |
|---|---|---|
| interface gate, level 0 | 10 | 10 |
| interface gate, level 1 | 5 | 5 |
| interface gate, level 2 | 2 | 2 |
| AND of interface gates | **13** | Σ\|A_ℓ\| + \|I₀\| = 13 |
| OR of interface gates (adversary picks) | **2** | min = 2 |
| AND of merge gates | 6 | \|I₀\| = 6 |
| OR of merge gates (adversary picks) | 1 | min = 1 |
| ι(Π₁ \| Π₀) | 0.400 | 2/5 |
| ι(Π₂ \| Π₀) | 0.500 | 1/2 |

Worst deviation zero. The naive per-level sum of the interface gates is 17 against the conjunction's 13: on the miniature a level-by-level accounting overstates the budget by 1.31, the overcount being the interfaces counted once per level that reads them. The reverse independences, ι(Π₀ \| Π₁) = 0.700 and ι(Π₀ \| Π₂) = 0.900, are the leaf level's receipt plus the interfaces the coarser level does not read; the asymmetry is the nesting.

---

## 4. The Level-Resolved Boundary

`code/holarchy.py`, Part 2. On the specimen the merge levels hold 128, 117, 64, 32, 16, 8, 4 and 2 edges — two per merge, with the pairs and quartets deduplicated at the two lowest levels — and the nested interface sets hold 371, 243, 126, 62, 30, 14, 6 and 2. Their sum is 854 against |E| = 371:

> Σ_ℓ \|I_ℓ\| / \|E\| = 2.30.

A holarchic accounting that charged each level for the interfaces it reads would overstate the specimen's native budget by that factor. The number is the mean number of levels that read an edge, and it is the first quantitative statement of what Proposition 3.2 declines to let a designer do.

**Proposition 4.1 (the boundary halves per level, exactly).** Let B be a level-j block. Every edge at merge level ℓ ≤ j is interior to some level-j block, so ∂B ∩ E_ℓ = ∅. Every edge at merge level ℓ > j has one endpoint in each of two distinct level-j blocks, so summed over the 2^{8−j} blocks at level j, Σ_B \|∂B ∩ E_ℓ\| = 2\|E_ℓ\|, and the mean over blocks is 2^{j+2−ℓ} where \|E_ℓ\| = 2^{9−ℓ}. Summed over ℓ > j the mean boundary is 4(1 − 2^{j−8}). ∎

This is a double-counting identity, not a sample mean, and the instrument returns it to the decimal:

| j | blocks | mean \|∂B\| | ℓ = j+1 | j+2 | j+3 | j+4 |
|---|---|---|---|---|---|---|
| 4 | 16 | 3.75 | 2.00 | 1.00 | 0.50 | 0.25 |
| 5 | 8 | 3.50 | 2.00 | 1.00 | 0.50 | |
| 6 | 4 | 3.00 | 2.00 | 1.00 | | |
| 7 | 2 | 2.00 | 2.00 | | | |

Below its own level a block has no boundary at all. The first block at each level — the coalition *One's Own Anchor* measured — has boundaries 3, 2, 3, 2, at levels {5: 2, 6: 1}, {6: 2}, {7: 2, 8: 1} and {8: 2}. The whole of a coalition's price sits in the two or three levels immediately above it, and the level immediately above always carries two edges of it, whatever the size.

---

## 5. Proposition 6.1, Priced

`code/holarchy.py`, Part 3. The residual reading of *One's Own Anchor* §4, commit-before-compare, edge-local prompts, the world's innovation at δ = 3σ/√k — well above the step, so that the coalition's stale record fails on any boundary edge a gate reads and it must derive. The coalition is the first block at level j ∈ {4, 5, 6, 7}, presenting at whatever level the gate admits. Twenty-six gates: the every-edge gate of the predecessor; each level's own-merge gate (every edge in E_ℓ below tolerance); each level's between-holons gate (every edge in I_ℓ); each level's *mean* gate (the mean residual over E_ℓ below tolerance — the aggregate of *Gluing the Gates* Proposition 4.1); and the mean over the network. For an every-edge-type gate the cheapest passing strategy derives exactly the boundary edges the gate reads; for a mean gate it derives the worst boundary edges one at a time until the mean clears, which needs derivations only where the coalition's boundary exceeds the fraction

> θ = (tol − r_h) / (r_stale − r_h) ≈ 0.41

of the level's edges. Derivations per epoch, averaged over the seven scored epochs:

| gate | \|C\| = 16 | 32 | 64 | 128 |
|---|---|---|---|---|
| every edge | **3** | **2** | **3** | **2** |
| own merges, ℓ ≤ j | 0 | 0 | 0 | 0 |
| own merges, ℓ = j+1 | 2 | 2 | 2 | 2 |
| own merges, ℓ = j+2 | 1 | 0 | 1 | — |
| **AND over own-merge gates** | **3** | **2** | **3** | **2** |
| **OR over own-merge gates** | **0** | **0** | **0** | **0** |
| between level-j holons | 3 | 2 | 3 | 2 |
| between level-7 holons | 0 | 0 | 1 | 2 |
| mean over merges, ℓ = j+1 | 0 | 0 | 0.86 | 1.43 |
| mean over merges, ℓ = j+2 | 0 | 0 | 0.86 | — |
| mean over the network | 0 | 0 | 0 | 0 |
| every edge, native cost per identity | 12 | 4 | 3 | 1 |

Three things are in the table, in the order the questions were asked.

**The sum over levels is the every-edge gate, to the edge.** The conjunction of every level's own-merge gate derives 3, 2, 3, 2 boundary edges — the predecessor's published numbers, at its published per-identity costs of 12, 4, 3, 1 — because the own-merge gates partition E and the boundary is a subset of E. This is Proposition 3.2 executed: the compositional mechanism is the finest level's gate, and *Gluing the Gates* Corollary 6.2's restored conjunction restores the every-edge price and nothing beyond it. The boundary does not multiply across levels. It is counted once.

**The minimum over levels is zero.** A mechanism the adversary may satisfy at one level of its choosing — Proposition 6.1's non-compositional case, an OR over the level gates — is defeated at zero derivations by every block coalition, because every own-merge gate at or below the coalition's level reads only edges interior to it, on which the fiction glues. The adversary picks the level, as Proposition 6.1 said, and the level it picks is its own. The between-holons gate at the top prices the two largest blocks only, at one and two edges, because only their boundaries reach the top merge; a mechanism that admits at the top and reads between its two halves is a mechanism for the half. And a level's *mean* gate prices only what exceeds θ of that level: the block of 128 is the whole of E₈ and pays 1.43 derivations per epoch there against the arithmetic's 2; the block of 64 is half of E₇ and half of E₈ and pays 0.86 at each against 1; the blocks of 16 and 32 are a quarter or less of any level and pay nothing. The mean over the network passes every coalition at zero, which is the failure *One's Own Anchor* §4 recorded — a network-level count cannot see a four-edge boundary in 371 — reproduced. The shortfalls against the arithmetic are the marginal epochs on which the realised stale residual sat just under the threshold; the count is the arithmetic's to within one derivation on about one epoch in seven.

**The boundary does not move with the level of presentation.** A level-j block presenting as one level-j holon, as two level-(j−1) holons, or as 2^j leaves has the same boundary — the same two or three edges above it — under the compositional mechanism, because ∂C ⊆ I_j ⊆ I_p for every presentation level p ≤ j. What changes with p is the receipt: one at level j, 2^{j−p} at level p, and the miniature's OR row is that receipt at the coarsest admitted level plus whatever interfaces the level reads. *One's Own Anchor* §9.3's question — the holon's boundary or the constituents' — has the answer that they are the same set of edges, and the saving of presenting coarse is entirely in the pool that evidences nothing.

---

## 6. Both Sides Controlled

`code/holarchy.py`, Part 4. *The Multiplicity Freedom* §8.4 proposed that a refinement is Sybil when the adversary controls both sides of an interface, and asked whether the criterion is checkable. In the vocabulary of *One's Own Anchor* Proposition 6.2, an interface with both sides controlled is an edge interior to the coalition, and the interior of a coalition is the fiction space: a consistent fabrication, free, evidencing nothing. The criterion is therefore correct, as a statement of *which* interfaces evidence nothing. The question is whether a residual can see it.

On the block of 64, with 90 interior edges, the two-sided gate 0.106 < r < 0.318 — the ordinary tolerance above and half honest's expected residual below:

| sections on the interior | mean r | min r | max r | two-sided | cost |
|---|---|---|---|---|---|
| honest | 0.2027 | 0.17 | 0.2695 | passes | — |
| naive fiction | 0.0000 | 2 × 10⁻¹⁶ | 0.0000 | **refused** | 0 |
| fabrication of honest scale, honest-level noise added | 0.1986 | 0.16 | 0.2434 | passes | **0** |

The honest interior residual is designed at (σ/√k)·√2·√(1 − 1/m) = 0.2054. The naive fiction — both endpoints of an interior edge written from one estimate — glues with residual zero at every interior edge, better than any honest pair, and a two-sided gate refuses it on that ground. The coalition's answer is to fabricate at honest scale and add the honest noise level to each endpoint independently, which costs nothing, and the result sits inside honest's spread on every interior edge. **Both sides controlled is not a residual.** The criterion is checkable only by a mechanism that derives the interior edge's prompts itself and compares — an audit at the auditor's native rate, which is an oracle by another name and *A Consistent Fiction* §8.2's question — or by changing which interfaces exist, which is §9.

One first-pass finding belongs on the record. The coalition's record-based estimate is zero on interior prompts, since no honest neighbour ever published them, so the first mimic was pure noise against pure noise and the Procrustes fit, with no signal to hold it, absorbed more of the noise than it should: 0.172, outside honest's spread, and a two-sided gate at a tighter floor would have caught it. The fiction has to have honest scale. That is a constraint on the coalition, satisfied for free, and not a defence.

---

## 7. What Nesting Bought

**The three questions.** *Independent and Expensive* §8.3: the budget composes as a sum on the anchor side and a union on the native side, and the union is the finest level's (Proposition 3.2). *The Second Pool* §9.3: each level's receipts add, and *Gluing the Gates* Proposition 6.1's minimum is what an adversary pays in receipts when it may choose its level — on the native side the minimum is zero (§5). *One's Own Anchor* §9.3: the holon's boundary and the constituents' are the same edges (§5). All three are struck through in their papers with this answer.

***Gluing the Gates* gains its measured instance.** Proposition 6.1 and Corollary 6.2 were sketches. On the specimen the non-compositional mechanism's cost is the minimum over levels and the minimum is zero; the compositional mechanism's cost is the sum over levels and the sum is the every-edge gate. The sketch was right about the shape and silent about the size: the conjunction it restores is worth exactly one boundary, counted once, and *Sign and Work* §8.4's question — does τ compose — has the same answer in the same shape: the anchor share sums over levels, the native share does not.

***The Multiplicity Freedom* §8.4 is answered and the answer is unkind.** The criterion is correct and not checkable from the reading. Combined with *One's Own Anchor* §6 — per-identity native cost falling as 1/\|C\| — and with §5 here — presentation level changes receipts only — the Sybil-across-levels problem is now fully priced: a holon refining into sub-holons pays more receipts and no more native work, a coalition coarsening into a holon pays fewer receipts and no less, and the reading cannot tell either from composition.

***Gauge-Fixing* §2, again.** The spectral-gap target was measured failing on the specimen by the predecessor; §4 says why in the holarchy's own terms. Two cross-edges per merge means two boundary edges at the level immediately above any block, and the design that would raise the boundary is a design with more cross-edges per merge, which *Requisite Richness* declined for its spectral dimension and *Sign and Work* §5.4 priced in trace gap. The overcount factor of 2.30 is also a statement about that paper's coalition bound: the bound scales with the gap of the cover, and the cover a holarchic mechanism actually reads is the finest level's, not the sum of the levels'.

**No new formalism was imported.** The holarchy is *Gluing the Gates*'s, the sheaf is the corpus's, the reading is the predecessor's. Conjecture R is not tested here, and the paper does not count itself as a confirmation.

---

## 8. What Is Declined

**That the minimum over levels is new.** It is the single-shard takeover [3–6] and Hirshleifer's weakest link [1, 2], and Proposition 6.1 already stated it for holarchies. What is new is that on the evidencing side the minimum is *zero* for every block coalition, for a structural reason — every level at or below the coalition's own reads only its interior — and that the conjunction restores one boundary, not a sum of boundaries.

**That receipts were modelled on the sheaf.** They were modelled on the attacker (§3) and not on the sheaf, because *One's Own Anchor* Theorem 3.4 makes every receipt idle and *The Second Pool* showed the receipt grid is arithmetic executed. The sheaf measurement is of native work alone. A mechanism whose receipts were not idle would need the sheaf rows, and the corpus has no such receipt.

**That the holarchy is general.** It is a binary tree of aligned blocks with two cross-edges per merge, so the boundary identity of Proposition 4.1 has the constant 2 in it and the halving is the tree's branching. A holarchy with span s and c cross-edges per merge would carry c boundary edges at the level immediately above a block and c/s^{ℓ−j−1} on average at level ℓ — the identity survives, the constants do not, and *Gluing the Gates* §8.3's depth-versus-span question is not touched.

**That the coalition strategies are exhaustive.** Every derivation count is a minimum over written-down strategies, so measured cost ≥ true cost. The greedy strategy against a mean gate derives the worst boundary edge first; a coalition that could lower a boundary edge's residual without deriving it would pay less. None was found.

**That the mean gate's shortfall is a finding.** The counts of 0.86 and 1.43 against the arithmetic's 1 and 2 are the realised stale residual on marginal epochs, inside the reading's spread. They are printed because the prediction was stated before running and the deviation is one derivation on one epoch in seven, not because they say anything the threshold did not.

**That the audit route is a defence.** §6 says the criterion is checkable by a mechanism that derives interior prompts itself. That prices the check at the auditor's native rate per audited edge, makes the auditor an oracle for those edges, and is *A Consistent Fiction* §8.2 unchanged. It is named, not recommended.

**That the level of presentation is priced.** §5 prices its native side and finds it invariant; the receipt side is one receipt per admitted holon, and whether presenting coarse is *rewarded* less is a question about the reward function's shape — *The Multiplicity Freedom* Theorem 6.1's convexity, on the level axis — which this paper does not ask.

**That the world model is general.** AR(1), memoryless, edge-local prompts; *One's Own Anchor* §8's declines carry over unchanged, and the shared-prompt model, in which one derivation serves the coalition and e(C) = 1/\|C\|, was not rerun here because the level structure does not enter it.

---

## 9. Open Problems

**9.1. Beacon-assigned overlaps.** The sharding literature's remedy for the minimum is random assignment: no coalition can arrange to be a unit. Transposed, the beacon would choose each epoch which pairs must overlap, and a block coalition's boundary would become a random cut of expected size proportional to \|C\|, restoring the cap *One's Own Anchor* §6 found missing. The price is the substrate's nesting itself: the hierarchical complex is the world-models' structure, not an assignment, and an overlap with a random stranger is a prompt the stranger's model has no reason to hold. Whether a substrate can carry both its own nesting and a beacon-assigned cover, and at what richness cost, is the design question §5 makes concrete and *One's Own Anchor* §9.4's curve is the first half of.

**9.2. Depth against span, priced.** Proposition 4.1's constants are the tree's. For a holarchy of span s and c cross-edges per merge, the boundary of a level-j block is c at the level immediately above it and falls by a factor of s per level thereafter, so the total is a geometric series whose sum depends on the span and whose distribution across levels depends on the depth. *Gluing the Gates* §8.3 asked what depth buys; on the evidencing side that is a computation on a holarchy that is not binary, and it has not been done.

**9.3. Receipts that are not idle.** Every level's receipt sums and evidences nothing, so the holarchy's whole evidencing budget is at one level. A receipt whose value the world determines — the content-anchor of *A Consistent Fiction* §8.5, on the level axis — would be a per-level pool that is not idle, and the sum-or-minimum question would then have a native side at every level. No such receipt exists in the corpus.

**9.4. The audit at a price.** §6's criterion is checkable by derivation. A mechanism that audited a random interior edge per coalition per epoch, at cost k·m, would price the fiction at the audit's detection probability times the penalty; whether that converges to the every-edge gate's price at less than the every-edge gate's cost is the standard question of random auditing, asked here of an interface.

**9.5. Reward across levels.** §5 leaves the reward function out. A holon admitted at level j is one identity with one reward; its 2^j leaves admitted at level 0 are 2^j identities. Whether a mechanism should pay a holon as one or as many, and whether *The Multiplicity Freedom* Theorem 6.1's convexity condition on the identity axis has a counterpart on the level axis, is the question *The Multiplicity Freedom* §8.4 becomes once its criterion is known to be unreadable.

---

## References

[1] J. Hirshleifer. *From Weakest-Link to Best-Shot: The Voluntary Provision of Public Goods.* Public Choice 41(3), 371–386, 1983.

[2] H. R. Varian. *System Reliability and Free Riding.* In L. J. Camp, S. Lewis (eds), Economics of Information Security, Springer, 1–15, 2004.

[3] V. Buterin. *Why Sharding Is Great: Demystifying the Technical Properties.* vitalik.eth.limo, 7 April 2021. Accessed 2026-09-07.

[4] A. Hafid, A. S. Hafid, M. Samih. *A Novel Methodology-Based Joint Hypergeometric Distribution to Analyze the Security of Sharded Blockchains.* IEEE Access 8, 179389–179399, 2020.

[5] E. Kokoris-Kogias, P. Jovanovic, L. Gasser, N. Gailly, E. Syta, B. Ford. *OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding.* IEEE S&P 2018. ePrint 2017/406.

[6] J. Wang, H. Wang. *Monoxide: Scale Out Blockchains with Asynchronous Consensus Zones.* NSDI 2019, 95–112. ePrint 2019/263.

[7] J. R. Douceur. *The Sybil Attack.* IPTPS 2002, LNCS 2429, 251–260.

[8] M. Yokoo, Y. Sakurai, S. Matsubara. *The Effect of False-Name Bids in Combinatorial Auctions: New Fraud in Internet Auctions.* Games and Economic Behavior 46(1), 174–188, 2004.

[9] Y. Zhang, P. Tang. *Collusion-Proof and Sybil-Proof Reward Mechanisms for Query Incentive Networks.* AAAI 2023. arXiv:2302.06061.

[10] H. Yu, P. B. Gibbons, M. Kaminsky, F. Xiao. *SybilLimit: A Near-Optimal Social Network Defense against Sybil Attacks.* IEEE S&P 2008, 3–17.

[11] V. Conitzer, N. Immorlica, J. Letchford, K. Munagala, L. Wagman. *False-Name-Proofness in Social Networks.* WINE 2010, LNCS 6484, 209–221.

[12] B. Viswanath, M. Mondal, A. Clement, P. Druschel, K. P. Gummadi, A. Mislove, A. Post. *Exploring the Design Space of Social Network-Based Sybil Defenses.* COMSNETS 2012.

[13] L. Alvisi, A. Clement, A. Epasto, S. Lattanzi, A. Panconesi. *SoK: The Evolution of Sybil Defense via Social Networks.* IEEE S&P 2013.

[14] P. D. Rowe. *Bundling Evidence for Layered Attestation.* TRUST 2016, LNCS 9824, 119–139.

[15] P. Gaži, A. Kiayias, D. Zindros. *Proof-of-Stake Sidechains.* IEEE S&P 2019. ePrint 2018/1239.

[16] J. Tirole. *Hierarchies and Bureaucracies: On the Role of Collusion in Organizations.* Journal of Law, Economics, & Organization 2(2), 181–214, 1986.

Propositions verified and measurements reproducible from `code/holarchy.py`, which imports the attacker of `code/exclusion.py` and the reading, the world and the coalition of `code/evidencing.py` unchanged.
