---
layout: document
title: "The Second Pool"
subtitle: "An Anchor Per Projection, and Whether the Reading Survives It"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /the-second-pool/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-09-06
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "The purchase the exclusion principle priced, made on the program's own substrate: a second anchor — Gauge-Fixing's delay chain, modelled for the first time — gives the temporal projection a pool the kernel's encodings do not touch, and independence returns to 1.000 with both gaps positive and summing to the two anchors' share of the budget, as the arithmetic said it would. What the arithmetic did not say is what the purchased projection evidences. Run in the order the predecessor prescribed, the gate comes first and fails: under induced maps a persistence reading measures how uniformly the network moved, uniform motion is a time-dependent gauge, and so coherent change and no change score identically — a frozen participant with a paid chain is admissible and out-scores honest persistence nine times over. The reading that refuses the cult is the chain read cohomologically, and it carries nothing but its anchor."
status: "v0.1 · working draft"
order: 21
---

## Abstract

*Independent and Expensive* v0.1 ended with two open problems in a stated order: whether any temporal reading carries a signal that survives its own anchor (§8.4), and, only after that, whether persistence can be given a pool of its own so that the first projection pair on the sheaf that is independent *and* expensive can be exhibited at an explicit price (§8.2). This paper runs them in that order. The gate is settled first by a gauge argument the predecessor's unanticipated 9.135 already contained: under induced restriction maps the sheaf Laplacian is the graph Laplacian in the frame gauge, so the epoch-to-epoch motion of the eigenspace a persistence reading compares is exactly the motion of the frames, and the reading is a weighted sum over the network of how *uniformly* the frames moved. Uniform motion is a time-dependent global gauge; a network in which every participant rotates identically scores 1.000, as full stasis does, and the honest participant's excess over the anchor-only strategy is measured, paired on the same free parts across ten seeds, at a mean of −0.046 with the sign flipping once. Nothing survives. The purchase is then made regardless, because the arithmetic said it could be: *Gauge-Fixing* §4.2's delay chain is modelled for the first time as a per-vertex per-transition encoding keyed to this epoch's beacon and to the participant's own previous section, and the priced temporal reading is a gluing condition on the two-layer sheaf of consecutive epochs rather than a value read. Independence returns to 1.000 in both directions at every positive setting of the two dials, each trace gap equals its anchor's receipt share of the joint budget to every decimal, and the two sum to one minus the reconciliation share — the corpus's largest pool of paid work, measured here at up to a third of the honest total, claimed by neither reading. The sheaf agrees with the model because, in the induced-map model, every reading is free given its anchor and the claims *are* the receipts; the chain even transports the static anchor's value for nothing, so the two anchors are independent as receipts and not as values. The empirical content is in who clears which reading: under the gluing condition the cheapest forger of persistence is a follower who transports last epoch's frame and did no spatial work; under the overlap reading it is the frozen participant holding a receipt, admissible, at 9.13× honest. The gluing reading refuses the frozen participant — Gauge-Fixing §4.3's non-glueability on the time axis, smallest eigenvalue 0.183 against a threshold of 0.05 — and reads nothing beyond its anchor, survival zero by construction. The prior art is drawn: the anchor is a proof of sequential work in the corpus's vocabulary, Ateniese et al. chain challenges to the previous proof and Chia alternates space with time, and Baig and Pietrzak show a time component *necessary* to stop space being reused across challenges, which is this paper's question in qualitative form; the accounting has no antecedent found. Every number is reproducible from `code/two_pool.py`, and the model is declared for what it is.

---

## 1. The Gate and the Purchase

The predecessor closed on a dependency, and the dependency is honoured here by running its two halves in the order stated.

*Independent and Expensive* proved, in a model small enough to prove things in, that independence and trace gap are claims on one budget, and measured on the sheaf that the one dial the program owned for pricing the temporal projection spent its independence in the same stroke — because both projections read the same encodings. It then said what the escape would cost: a second pool, an anchor per projection, the gaps summing to at most one. And it said, in §8.4, that before the second pool was built a prior question had to be answered, because its own instrument had returned a number nobody asked for. Under the epoch-keyed beacon anchor, a participant who froze every frame at epoch zero scored 9.135 times the honest participant's persistence progress, and was refused by the admissibility rule rather than by any price. The anchor that gave persistence its price appeared to be eating the signal persistence was supposed to carry. A second pool is worth nothing to a projection whose signal its anchor has already eaten, and that is why §8.4 was placed before §8.2.

This paper runs the gate first. §3 derives what an eigenspace-overlap persistence reading actually measures under induced restriction maps, and the derivation is short enough that the 9.135 is a corollary rather than a surprise: the reading measures the uniformity of the frames' motion across the network, uniform motion is a gauge, and the honest participant — whose free parts drift — can only move less uniformly than one who holds still. §4 measures it, paired across seeds, and finds nothing surviving. The purchase is then made anyway, in §5 and §6, for two reasons. The arithmetic predicted an outcome to the decimal and the program's rule is that predictions of that kind are run, not assumed. And the priced reading has to change — from a value the anchor dominates to a gluing condition the anchor prepares — and whether the changed reading carries anything is a question the gate result on the old reading does not answer.

The conclusion, stated before the machinery: **the second pool buys exactly what the exclusion said it would, and the purchased projection evidences its anchor.** Independence returns; both gaps are positive; the sum is the two anchors' share of the joint budget; and the reading that refuses the frozen participant is the chain read cohomologically, with a survival of zero by construction. The overlap reading, which had a signal to lose, cannot tell coherent change from no change, because in this model they are one orbit of the temporal gauge. That is the negative form of *Proof of Coherence* v0.5 §4.5's unfilled requirement — score coherent change, not persistence — for the whole class of readings that compare eigenspaces across epochs.

---

## 2. Prior Art, and the Boundary of the Claim

The anchor is borrowed and the accounting is not, and the line between them is drawn here so that the paper claims only the second.

A per-transition encoding that cannot be produced without the previous state and cannot be produced before the current epoch's randomness is a proof of sequential work in the corpus's vocabulary. The construction has a settled literature: Mahmoody, Moran and Vadhan's publicly verifiable proofs of sequential work [1], Cohen and Pietrzak's simplification [2], and the verifiable delay functions of Boneh, Bonneau, Bünz and Fisch [3], Wesolowski [4] and Pietrzak [5], which *Gauge-Fixing* §4.2 names as its delay chain. The closest structural antecedent to what §5 builds is Ateniese, Chen, Etemad and Tang's proof of storage-time [6], in which each period's challenge is derived by a VDF from the previous period's proof so that proofs cannot be batch-generated; it chains to the previous state without a per-epoch public beacon. Filecoin's proof-of-spacetime [7] draws its per-deadline challenges from a randomness beacon and is stateless between deadlines: beacon without chain. Chia [8] alternates proofs of space with VDFs, each challenge computed from the previous output, and so has both, in a consensus setting. Moran and Orlov [9] define the space-time resource as a trade-off against CPU work, and Fisch [10] gives the tight proofs of space and replication that *Gauge-Fixing* §4.3's encoding is modelled on. None of these is claimed; the transition anchor of Definition 5.1 is their common shape rendered in this program's stalks.

What the literature does not contain, and what is claimed: an accounting of the *independence* of two proofs layered on one substrate as a ratio of marginal forging costs, with both proofs' trace gaps normalised by the joint work they together evidence, and the measurement of whether a temporal anchor buys independence from a static one on the same data. The nearest question in that literature is Baig and Pietrzak's [11], who show that a proof-of-space longest-chain protocol without a time component permits the space to be reused across challenges — a time component is *necessary* for the two resources to be distinct. That is the qualitative form of this paper's question, answered as an impossibility. Minotaur [12] runs the opposite way: it treats work and stake as *fungible*, security holding when the adversary's cumulative share across resources is bounded, which is exactly the additive reading this program's exclusion principle says is available only when the pools are disjoint. Neither computes ι. The prior-art check also found the paper's most uncomfortable result already deployed: Bittensor's weight-copying problem [13], in which a validator holding stale consensus weights out-earns an honest validator because the bonding mechanism rewards proximity to consensus, is a frozen participant scoring above an active one on a persistence-like reading, in production, on the substrate *Proof of Coherence* was written for. Fraboni, Vidal and Lorenzi [14] give the same phenomenon a convergence proof in federated learning: a client returning the previous global model passes aggregation. The stasis premium is not this paper's discovery; its price, its admissibility under a paid chain, and the gauge reason it cannot be scored away are.

---

## 3. What the Reading Reads

The predecessor's 9.135 has a derivation, and the derivation says what a persistence reading is.

**Setup.** Vertices v ∈ V with stalks ℝᵈ, d = 3; at epoch t a frame R_v(t) ∈ O(d) per vertex; restriction maps induced, O_uv = R_u(t)ᵀR_v(t), so that every declared configuration is flat and the kernel of the sheaf Laplacian Δ(t) has dimension d (*Sign and Work* Proposition 5.1). Write G(t) for the block-diagonal matrix with blocks R_v(t), and L for the graph Laplacian. Then Δ(t) = G(t)ᵀ (L ⊗ I_d) G(t): in the frame gauge the sheaf Laplacian is the graph Laplacian, with every level d-fold degenerate. Its bottom-K eigenspace, for K = kd with the k-th and (k+1)-th graph eigenvalues distinct, is V_t = G(t)ᵀ(Φ ⊗ I_d), where Φ is the n × k matrix of bottom graph modes. On the specimen n = 256, \|E\| = 371, the graph's fourth and fifth eigenvalues are 0.0226 and 0.0254, so the reading's K = 12 selects exactly the first four modes.

**Proposition 3.1 (the overlap reading is a uniformity of motion).** The persistence reading of `temporal_iota.py` — the mean over consecutive epochs of (1/K)‖V_tᵀV_{t+1}‖²_F — equals, for induced maps,

> (1/K) Σ_{k,l ≤ K/d} Σ_{i,j ≤ d} ( Σ_v φ_k(v) φ_l(v) [M_v]_{ij} )²,   with M_v = R_v(t) R_v(t+1)ᵀ.

*Proof.* V_tᵀV_{t+1} = (Φᵀ ⊗ I) G(t)G(t+1)ᵀ (Φ ⊗ I), and G(t)G(t+1)ᵀ is block-diagonal with blocks M_v. Its ((k,i),(l,j)) entry is Σ_v φ_k(v)φ_l(v)[M_v]_{ij}. ∎

M_v is the rotation that carries vertex v's frame from epoch t to epoch t+1. The reading is a graph-weighted average of these rotations, squared: it is large when the M_v are the same across the network and small when they differ.

**Corollary 3.2 (the temporal gauge).** If M_v = M for every v — every frame moved by the same rotation, R_v(t+1) = Mᵀ R_v(t) — then Σ_v φ_kφ_l M_{ij} = δ_{kl} M_{ij} and the reading equals (1/K)(K/d)‖M‖²_F = 1, whatever M is. Stasis is the case M = I. *A network in which every participant updates identically scores exactly what a network in which nobody updates scores.*

Under induced maps a shared global section is x_v = R_v(t)ᵀc for one c ∈ ℝᵈ; a coherent change of the shared world-model is a rotation of c; and a rotation of c is a left rotation of every frame at once, which is Corollary 3.2's hypothesis. So within this model coherent change and no change are one orbit of a gauge the reading is invariant under, and no reading in the class — any function of the overlap of consecutive eigenspaces of induced Laplacians — can separate them. This is *Proof of Coherence* v0.5 §4.5's requirement, that a temporal projection must score *coherent* change rather than persistence, closed in the negative for that class.

**What the anchor does to the honest score.** Under the beacon anchor, column 0 of R_v(t) is a unit vector drawn independently per vertex and per epoch, and the remaining columns are the orthonormalised complement of the free part against it. Then M_v = b_v(t)b_v(t+1)ᵀ + F_v(t)F_v(t+1)ᵀ, whose first term is i.i.d. noise across the network and whose second term moves with the beacon even when the free part does not, because the complement of a moving column moves. The honest participant adds drift to the free part, and drift is per-vertex noise. So the honest M_v are less uniform than a frozen participant's, which are the identity, and the honest score sits just above the frustrated baseline while stasis sits at 1. On the specimen: honest 0.1391, frustrated 0.0332, stasis 1.0000, ratio (1 − 0.0332)/(0.1391 − 0.0332) = 9.13. The number was not a symptom of a threshold or a seed; it is Corollary 3.2 with the anchor's rotation in the denominator.

**Definition 3.3 (survival).** For a reading π with anchor A, let h be the honest score, f the frustrated baseline, and a* the *best* score among admissible strategies that pay for nothing but A. The survival of π through A is S(π; A) = (h − a*)/(h − f). It is 1 when the anchor-only class recovers nothing of the honest excess and 0 when it recovers all of it; negative when the anchor-only class scores above honest. The supremum over the class is the convention *The Multiplicity Freedom* v0.4 adopted for ι — the adversary chooses the strategy, so the instrument must — and it matters: taking a single weak anchor-only strategy as a* manufactures survival, and §4 prints that number beside the honest one so that the trap is on the record.

---

## 4. The Gate, Measured

`code/two_pool.py`, Part 3. The reading is the overlap reading; its anchor is the static beacon encoding at cost En per vertex per epoch; the anchor-only class is the three strategies that pay the static receipts and nothing else — encode with a fresh free part each epoch, encode with the free part frozen, and encode with the free part frozen while declaring the honest transition without paying for it. The prediction, stated before running: S ≤ 0, because the best static-only strategy holds everything still that the honest participant lets drift, and drift can only make the M_v less uniform.

| quantity | value |
|---|---|
| honest (seed 12) | 0.1391 |
| frustrated baseline | 0.0332 |
| best static-only strategy (seed 32) | 0.1242 |
| honest with the beacon pinned at epoch 0, drift kept (control) | 0.9252 |
| retention of the drift signal through the anchor | 0.119 |
| naive S, using the chain-only follower as "anchor only" | +1.131 |

The unpaired comparison gives S = +0.141, and it is not the instrument's answer, because honest and static-only were drawn from different free parts and the difference between two draws is of the size of the effect. Paired on the same free parts, across ten seeds:

| seed | honest | static-only | S |
|---|---|---|---|
| 12 | 0.1391 | 0.1472 | −0.077 |
| 32 | 0.1178 | 0.1242 | −0.075 |
| 41 | 0.1337 | 0.1367 | −0.030 |
| 42 | 0.1315 | 0.1357 | −0.043 |
| 43 | 0.1281 | 0.1342 | −0.064 |
| 44 | 0.1394 | 0.1336 | +0.055 |
| 45 | 0.1325 | 0.1353 | −0.028 |
| 46 | 0.1270 | 0.1355 | −0.090 |
| 47 | 0.1289 | 0.1383 | −0.099 |
| 48 | 0.1307 | 0.1316 | −0.009 |

Mean −0.046, range −0.099 to +0.055, one seed of ten positive. The prediction held within the seed spread and not beyond it: drift is random, and on one draw in ten it happened to move the frames more uniformly rather than less. What can be said is exact in one direction and bounded in the other. The honest participant's excess over a frozen encoder is not distinguishable from zero at the resolution the instrument has, and the control that pins the beacon says where the excess went — with the beacon held at epoch zero and everything else honest, persistence is 0.9252, so the anchor removes 88% of the drift signal before the anchor-only class removes the rest.

The naive number is the one to keep in view. The chain-only follower of §5, which pays no static receipt, scores 0.0194 on this reading, below the frustrated baseline, because a per-vertex chain forces maximally non-uniform motion. Taking it as the anchor-only strategy gives S = +1.131, a signal that not only survives but exceeds the honest one. Nothing survives; the wrong instrument says everything does. The difference is Definition 3.3's supremum, and the program's rule that an adversary chooses.

**The stasis row, restated.** On this reading, with the anchor gauged out — every eigenvector's stalk component along the beacon column removed before comparison — the frozen participant still scores 1.0000 against an honest 0.0812. Removing the anchor from the reading does not restore a signal the honest participant never had; it confirms that the reading was measuring uniformity, and the frozen participant is maximally uniform by definition.

The gate is failed for the overlap reading. §8.4 of the predecessor is answered: on the time axis, for this class of readings, no signal survives the anchor, and the reason is not the anchor's dominance but the reading's gauge.

---

## 5. The Transition Anchor

The second pool has to be a structurally distinct paid quantity — *Sign and Work* §5.2 measured the existing anchor's rank as a switch, so adding columns buys nothing — and it has to live somewhere the static encoding does not: on the transitions.

**Definition 5.1 (transition anchor).** For each vertex v and each transition into epoch t ≥ 1, a map T_v(t) ∈ O(d) whose first column is κ_v(t) = R_v(t−1)ᵀ b_v(t): this epoch's beacon column, expressed in the participant's own previous frame. Producing an admissible T_v(t) costs E_t per vertex per transition. The honest transition T_v(t) = R_v(t−1)ᵀR_v(t) carries κ_v(t) automatically, since its first column is R_v(t−1)ᵀ times the first column of R_v(t), which is the beacon.

This is *Gauge-Fixing* §4.2's delay chain — "each section carries a chain rooted in the epoch beacon; the chain is a certificate of having-been-there" — rendered as an encoding on the temporal structure. It is keyed to the current beacon, so it cannot be precomputed, and to the previous section, so it cannot be produced without having held one. The static anchor of *Gauge-Fixing* §4.3 is kept unchanged: column 0 of R_v(t) must be b_v(t), at cost En per vertex per epoch.

**Definition 5.2 (transition sheaf).** For each transition t−1 → t, the cellular sheaf on two copies of the complex — vertices (v, t−1) and (v, t), space edges in each layer carrying that layer's induced maps, and a rung (v, t−1)–(v, t) per vertex carrying T_v(t) as its restriction map with unit weight. The priced temporal reading π_persist is the count of eigenvalues of its Laplacian below the kernel tolerance (0.05, the same tolerance π_ker uses), averaged over the seven transitions.

**Proposition 5.3 (what glues).** With induced space maps in both layers, the transition sheaf has a global section iff D_v := R_v(t−1) T_v(t) R_v(t)ᵀ is the same matrix at every vertex; its kernel is then d-dimensional, and its spectrum is the graph spectrum together with the graph spectrum shifted by two, so the reading counts the spatial modes that survive the transition and the rung branch never approaches the tolerance. *Proof.* Layer sections are x_{v,t−1} = R_v(t−1)ᵀc and x_{v,t} = R_v(t)ᵀc′; the rung condition x_{v,t−1} = T_v x_{v,t} reads c = D_v c′, which has a solution for every c′ iff the D_v coincide. The honest transition gives D_v = I. The spectral statement is the block computation of a Cartesian product with a flat connection. ∎

The reading is therefore a gluing condition — H¹ of the squares formed by a space edge and two rungs — and not a read of the anchor's value. It tolerates the temporal gauge of Corollary 3.2 (a global rotation gives D_v = I at every vertex) and it couples neighbours through the space edges. That is the discipline of *Gauge-Fixing* §4.4 and test (iv): the anchor prepares the sheaf's inputs so that H¹ can see, and the mechanism never cites the anchor's value as a certificate of order. Whether the reading carries anything *besides* the anchor is §6's question and Definition 3.3's.

**Proposition 5.4 (the chain transports the beacon).** A participant holding any frame R_v(t−1) who pays the chain and sets R_v(t) = R_v(t−1) T_v(t) obtains a frame whose first column is R_v(t−1)κ_v(t) = b_v(t): this epoch's beacon value, at no encoding cost. *Proof.* R_v(t−1)R_v(t−1)ᵀ = I. ∎

So the two anchors' *values* are not independent: the static anchor's is derivable from the chain's. In the mechanism *Gauge-Fixing* specifies this does not arise, because §4.3's encoding is a slow sequentially dependent function of the section and the beacon, verifiable as fresh production and not as a value; the model's "column 0 equals the beacon" is a stand-in for that, and Proposition 5.4 is the stand-in's failure. The instrument therefore gates on **receipt and value**: the static gate requires the encoding to have been *paid* for this epoch and the column to match; the chain gate requires the transition to have been paid and κ to match. A gate that checked values alone would price the kernel at one epoch's encoding, report ι(ker\|persist) = 1/8, and at small E_t return a conjunction cheaper than one of its conjuncts, which is an impossible number and was the tell.

**The consequence to state plainly.** In the induced-map model every reading is free given its anchor — *Sign and Work* Proposition 5.1 on the space axis, Proposition 5.3 on the time axis — so the claims are the receipts, and the trace gaps and independence of the two projections are the paid-DOF model's arithmetic executed on receipts. The joint work is W = 8nEn + 7nE_t + 8\|E\|c, with c the reconciliation cost per edge per epoch (*Sign and Work* §5.2). Under receipt gates:

**Corollary 5.5 (the two-pool arithmetic).** f(π_ker) = 8nEn, f(π_persist) = 7nE_t, f(both) = 8nEn + 7nE_t; hence ι = 1 in both directions at every En, E_t > 0, τ(π_ker) = 8nEn/W, τ(π_persist) = 7nE_t/W, and τ(π_ker) + τ(π_persist) = 1 − 8\|E\|c/W. This is *Independent and Expensive* Theorem 3.4 with two disjoint claims and one unclaimed pool, and the instrument must return it to every decimal. Any deviation is a gate bug, not a finding.

The empirical content is therefore not in the grid. It is in **who** clears each reading at that cost, whether the frozen participant is refused on gluing grounds rather than by fiat, and whether the gluing reading carries anything its anchor does not.

**Calibration.** The model's three-pool miniature — static pool of three, transition pool of three, reconciliation pool of two read by neither, two free — returns τ = 0.375 and 0.375, ι = 1.000 both ways, sum 0.750 = 1 − 2/8, worst deviation from the designed values zero. On the sheaf, seven facts the construction must reproduce before its numbers are read, all reproduced: the honest transition carries κ at every transition; honest glue equals honest kernel count (18 = 18, six graph eigenvalues below tolerance, threefold each); the frustrated baseline glues nothing; a participant who froze everything and declares the identity transition without paying glues perfectly (did not move, says so — 18); the chain-only follower carries the beacon by value at every transition t ≥ 1 with no static receipt (Proposition 5.4); the global-rotation control scores 1.000 on the overlap reading (Corollary 3.2); the frozen participant with a paid chain glues nothing, smallest eigenvalue 0.183 against a tolerance of 0.05.

---

## 6. The Purchase, Measured

`code/two_pool.py`, Parts 2 and 4. Fourteen strategies, every one written down, scored once each on both readings; costs are receipts and do not move the eigenvalues, so the (En, E_t) grid is bookkeeping over one table.

**Who clears what.** Receipts: S for the eight static encodings, C for the seven chain encodings.

| strategy | receipts | π_ker | glue | overlap | note |
|---|---|---|---|---|---|
| honest | S C | 18 | 18 | 0.1391 | pays reconciliation too |
| frustrated | — | 0 | 0 | 0.0332 | baseline |
| freeze everything, declare identity | — | 18 | 18 | 1.0000 | 9.13× honest overlap |
| encode, free part fresh each epoch | S | 18 | 0 | 0.0256 | below baseline |
| encode, free part frozen | S | 18 | 0 | 0.1242 | |
| encode, free part frozen, declare honest T unpaid | S | 18 | 18 | 0.1242 | the receipt refuses it |
| pay chain, random frames | C | 18 | 0 | 0.0230 | the reading is not the receipt |
| pay chain, follow it (still) | C | 18 | 18 | 0.0194 | carries the beacon by value |
| pay chain, follow it (random) | C | 18 | 18 | 0.0259 | |
| pay both, no reconciliation | S C | 18 | 18 | 0.1242 | |
| freeze frames, pay chain (still) | C | 18 | 0 | 1.0000 | 9.13× honest, **admissible** |
| freeze frames, pay chain (random) | C | 18 | 0 | 1.0000 | λ_min 0.183 |
| honest, beacon pinned (control) | S C | 18 | 18 | 0.9252 | |
| global rotation (control) | — | 18 | 18 | 1.0000 | the gauge |

Three rows carry the paper. **The follower** pays the chain, transports last epoch's random frame along it, and glues perfectly — 18 of 18 at every transition — having done no spatial work and holding no static receipt. It is the cheapest forger of the priced temporal reading at every setting of the dials. **The frozen participant with a receipt** pays the chain, moves nothing, is admissible for the temporal gate, and scores 9.13× the honest participant on the overlap reading: the cult with a receipt, which *Proof of Coherence* v0.5 §4.5 said a persistence score would pay a premium for, now priced at 7nE_t and admitted. On the gluing reading the same participant scores zero, because its declared transitions carry κ but its frames did not move, so D_v = R_v T_v R_vᵀ differs from vertex to vertex and nothing glues — the smallest eigenvalue is 0.183, over three times the tolerance, and the refusal is on gluing grounds, not by a staleness rule. That is *Gauge-Fixing* §4.3's "engineered to be non-glueable" on the time axis, and it is real. **The declarer** encodes the static anchor, freezes its free part, and declares the honest transition without paying for it: it glues perfectly, and only the missing receipt refuses it. The gluing reading's value is free to anyone holding the previous frame; the chain's price is the whole of its security.

**The grid.** Both readings return the same numbers, because the claims are the receipts. Persistence read as the gluing condition:

| En | E_t | τ(π_ker) | τ(π_persist) | ι(ker\|persist) | ι(persist\|ker) | sum | 1 − reconciliation share | clears persist / both |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0.161 | 0.141 | 1.000 | 1.000 | 0.301 | 0.301 | follower / pay both |
| 1 | 4 | 0.113 | 0.396 | 1.000 | 1.000 | 0.509 | 0.509 | follower / pay both |
| 1 | 16 | 0.052 | 0.724 | 1.000 | 1.000 | 0.775 | 0.775 | follower / pay both |
| 4 | 1 | 0.434 | 0.095 | 1.000 | 1.000 | 0.529 | 0.529 | follower / pay both |
| 4 | 4 | 0.338 | 0.295 | 1.000 | 1.000 | 0.633 | 0.633 | follower / pay both |
| 4 | 16 | 0.179 | 0.626 | 1.000 | 1.000 | 0.805 | 0.805 | follower / pay both |
| 16 | 1 | 0.754 | 0.041 | 1.000 | 1.000 | 0.795 | 0.795 | follower / pay both |
| 16 | 4 | 0.671 | 0.147 | 1.000 | 1.000 | 0.818 | 0.818 | follower / pay both |
| 16 | 16 | 0.466 | 0.408 | 1.000 | 1.000 | 0.873 | 0.873 | follower / pay both |

Worst deviation from Corollary 5.5, zero. At En = 0 or E_t = 0 the corresponding gate is vacuous and the corresponding ι is undefined — the free corner *Independent and Expensive* §4 describes, where the independence of a free thing is not a quantity — and the instrument prints it as such. Under the overlap reading the grid is identical and the "clears persist" column reads *frozen with receipt* at every positive E_t, and *freeze everything* at E_t = 0.

**What was bought.** The first projection pair on the program's substrate that is independent and expensive: ι = 1.000 in both directions, τ positive on both, at every positive setting. The price is explicit and it is two anchors. And the sum of the gaps is bounded away from one by the reconciliation share 8\|E\|c/W — 0.699 of the honest budget at En = E_t = 1, 0.367 at 4 and 4, 0.127 at 16 and 16. That share is the coherence work itself, paid by the honest participant every epoch and claimed by neither reading, which is *Independent and Expensive* §8.5's pool with a number attached: on this substrate, between an eighth and two thirds of what honesty costs is outside the mechanism's security budget, and the fraction falls only as the anchors are made expensive relative to the coherence work — *Sign and Work* §8.3's perverse route, now with two anchors on it.

**Survival of the priced reading.** S(glue; chain) = 0.000: the best chain-only strategy scores the gluing reading to the integer. The prediction was that this would hold by construction, and it does. The reading that refuses the cult carries nothing but its anchor.

---

## 7. What the Purchase Bought

Read back into the corpus, the result is one purchase and one impossibility, and the second is worth more than the first.

**The exclusion's fork is now measured on both branches.** *Independent and Expensive* §6 said that within one pool no projection pair clears both requirements and across pools clearing both is purchasable. The one-pool branch was measured there; the two-pool branch is measured here and returns the arithmetic to the decimal. "A Combination Proof of order K is K anchors wearing readings" is no longer an inversion of the framework's self-description but a construction: two anchors, two receipts, two readings each free given its anchor. §8.2 of that paper is discharged and §8.4 is answered, and the answers are recorded there as its v0.2.

**The perverse route has a second lane.** *Sign and Work* §8.3 asked whether the mechanism can approach soundness other than by making its anchor expensive relative to its coherence work, ending up measuring its anchor. The second pool does not open a non-perverse route; it doubles the perverse one. Each reading's gap is exactly its anchor's receipt share, and the shortfall to one is exactly the coherence share, on both axes now. §8.1 of that paper — is there a coherence reading whose gap is not bought entirely by its anchor? — is not answered here, since the gluing reading is an induced-map reading and Proposition 5.3 is the telescoping argument on the time axis. It is narrowed: the one place a better gap could hide is unchanged, and it is not on the temporal axis of a declared-frame sheaf.

**"Score coherent change" has no instance in the class.** *Proof of Coherence* v0.5 §4.5 corrected itself to say a temporal projection must score coherent change rather than persistence and offered no formulation. Corollary 3.2 says why none was found: for readings that compare eigenspaces of induced Laplacians across epochs, coherent change is a gauge and the reading is invariant under it. A formulation must break the symmetry with an external per-vertex reference on the transitions — which is the chain — and once the chain is in the reading, the reading is its anchor. The service line's open problem 3, a delivery score that is not satisfaction, was noted to be the same problem in another setting; it inherits the same answer for the same class.

**Gauge-Fixing's suite gains a second respondent.** §5 test (i) had one fragment executed, on §4.3 with the anchor removed. The delay chain of §4.2 is now modelled, its non-glueability against a frozen participant is measured, and test (iv) — the anchor consumed as timing and never cited as a certificate of order — is honoured by construction in the gluing reading. What §4.2 also shows in this model is Proposition 5.4: a chain rooted in the beacon carries the beacon, so the *values* of §4.2 and §4.3 are not independent, and the encoding of §4.3 does its work only because it is a verifiable production and not a checkable value. That is a design constraint the paper did not state and now does.

**Two anchors, one discipline.** *A Consistent Fiction* §8.5 asked whether two anchors with two disciplines are admissible — one supplying content while the beacon supplies only randomness and timing. The two anchors here share one discipline, provenance, and share a value by Proposition 5.4. The question is not answered; it is shown that "two anchors" alone does not reach it.

**Richness buys nothing, a third way.** *The Multiplicity Freedom* Corollary 5.4 gave two: redundancy (ι = 0) and forgeability (τ = 0). The purchased projection has ι = 1 and τ > 0 and contributes to the Sybil cap exactly its anchor's receipt share, which an anchor without a reading would contribute equally. A reading that evidences only its anchor is not redundant and not free; it is *idle*, and the corollary's two failure modes are the two ways a term ι_kτ_k vanishes while this is the way a term is non-zero and still buys no reading.

**The stasis premium is deployed.** Bittensor's weight-copying [13] is a persistence-like reading paying a frozen participant above an active one on the substrate the whitepaper was written for, and the remedies on offer — commit-reveal with a timelock — are a chain. This paper's model says the chain will refuse the copier on gluing grounds and will carry nothing else; whether the deployed remedy behaves the same way is not measured here.

**Conjecture R, again.** A new formalism — the two-layer sheaf — was introduced and relocated the difficulty by exactly one receipt: the temporal reading's security is the chain's price, as the static reading's is the encoding's. Seven confirmations.

---

## 8. What Is Declined

**That the model is the mechanism.** Receipts stand in for verifiable productions; column-equality stands in for a sequentially dependent encoding; per-vertex independent drift stands in for model updating; induced maps make every declared configuration flat. Proposition 5.4 is the clearest place the stand-in fails, and it is reported as the model's failure, not the mechanism's.

**That the transition anchor is new.** It is a proof of sequential work with a public beacon, and §2 names the constructions it is between. What is claimed is the accounting and the measurement.

**That the τ/ι grid is a finding.** It is Corollary 5.5 executed. The grid is printed because the program's rule is that a prediction of that shape is run, and because a gate bug would have shown there and did, once, as a conjunction cheaper than a conjunct.

**That the gate result generalises beyond the class.** Corollary 3.2 is a statement about readings that compare eigenspaces of induced Laplacians. A reading that measures restriction maps at overlaps rather than inducing them from declared frames — *Sign and Work* §8.1's candidate — is outside the class and outside this paper.

**That survival was measured to be zero on the overlap reading.** It was measured to be indistinguishable from zero: mean −0.046 across ten paired seeds with one positive. The gauge argument says why it should be at most zero; the instrument's resolution says only that it is small.

**That the frozen participant is defeated.** It is refused by one reading and paid nine times over by the other, and both readings are in the corpus. A mechanism scoring persistence by overlap, with or without a chain, pays the cult. A mechanism scoring the gluing condition refuses it and scores nothing else.

**That *A Consistent Fiction* §8.5 is answered.** Two anchors of one discipline, sharing a value, do not test two disciplines.

**That the reconciliation share can be claimed.** Its size is measured, not its claimability, which is *Independent and Expensive* §8.5 and *Sign and Work* §8.1 unchanged.

**That the deployed instance is verified against a primary source.** Bittensor's weight-copying [13] is cited from operator documentation and a third-party analysis, both web-only and dated by access; the phenomenon is reported there, not measured here, and §9.4 is where it would be.

**That measured τ certifies anything.** Every fake-cost is a minimum over fourteen written-down strategies; measured τ ≥ true τ, always. A cheaper follower would lower the temporal gap, which would tighten the sum, not loosen it. The direction of error runs with the theorem, as before.

**That Proposition 5.2's cost model is settled.** The joint budget counts reconciliation as work on top of encoding, as *Sign and Work* §5.2 does and §7 of that paper declines. If reconciliation is redundant at full rank the reconciliation share shrinks, the two gaps sum closer to one, and the purchase looks better than it is.

---

## 9. Open Problems

**9.1. A reading outside the class.** Corollary 3.2 bounds every eigenspace-overlap reading of an induced sheaf. Restriction maps *measured* at overlaps — two participants' sections compared on shared data, the map fitted rather than declared — are outside it, on both axes. Whether such a reading has a temporal gauge of its own, and whether its gap is bought by something other than an anchor, is the one question this paper and *Sign and Work* §8.1 both leave at the same door.

**9.2. Two disciplines.** Build the anchor *A Consistent Fiction* §8.5 asks for — one that supplies content, while the beacon supplies timing — alongside the chain, and measure whether their values are independent. Proposition 5.4 says the pair built here is not the test.

**9.3. The budget across levels.** Unchanged from *Independent and Expensive* §8.3, and sharper: each level of a holarchy would carry its own two receipts, and *Gluing the Gates* Proposition 6.1 suggests the joint budget is the minimum over levels rather than the sum. Building it is the next paper.

**9.4. The deployed chain.** Bittensor's commit-reveal remedy for weight copying is a chain on a persistence-like reading. Whether it refuses the copier on structural grounds, and whether the reading that remains carries anything but the remedy, is measurable against a public mechanism and has not been.

**9.5. The idle projection.** A projection with ι = 1 and τ > 0 that evidences only its anchor contributes to the Sybil cap and not to the reading. Whether *The Multiplicity Freedom*'s Theorem 5.1 should count it — the cap it buys is real — or whether the framework needs a third condition on projections beyond independent and expensive, *evidencing*, is a question of what a Combination Proof is for.

---

## References

[1] M. Mahmoody, T. Moran, S. P. Vadhan. *Publicly Verifiable Proofs of Sequential Work.* ITCS 2013, 373–388. ePrint 2011/553.

[2] B. Cohen, K. Pietrzak. *Simple Proofs of Sequential Work.* EUROCRYPT 2018, LNCS 10821, 451–467. ePrint 2018/183.

[3] D. Boneh, J. Bonneau, B. Bünz, B. Fisch. *Verifiable Delay Functions.* CRYPTO 2018, LNCS 10991, 757–788. ePrint 2018/601.

[4] B. Wesolowski. *Efficient Verifiable Delay Functions.* EUROCRYPT 2019, LNCS 11478, 379–407. ePrint 2018/623.

[5] K. Pietrzak. *Simple Verifiable Delay Functions.* ITCS 2019, LIPIcs 124, 60:1–60:15. ePrint 2018/627.

[6] G. Ateniese, L. Chen, M. Etemad, Q. Tang. *Proof of Storage-Time: Efficiently Checking Continuous Data Availability.* NDSS 2020. ePrint 2020/840.

[7] Protocol Labs. *Filecoin Specification: Proof-of-SpaceTime; Randomness.* spec.filecoin.io, accessed 2026-09-06.

[8] B. Cohen, K. Pietrzak. *The Chia Network Blockchain.* Whitepaper, July 2019.

[9] T. Moran, I. Orlov. *Simple Proofs of Space-Time and Rational Proofs of Storage.* CRYPTO 2019, LNCS 11692, 381–409. ePrint 2016/035.

[10] B. Fisch. *Tight Proofs of Space and Replication.* EUROCRYPT 2019, LNCS 11477, 324–348. ePrint 2018/702.

[11] M. A. Baig, K. Pietrzak. *On the (In)security of Proofs-of-Space based Longest-Chain Blockchains.* Financial Cryptography 2025. ePrint 2025/942.

[12] M. Fitzi, X. Wang, S. Kannan, A. Kiayias, N. Leonardos, P. Viswanath, G. Wang. *Minotaur: Multi-Resource Blockchain Consensus.* ACM CCS 2022, 1095–1108. ePrint 2022/104.

[13] Taostats documentation, *Weight Copying*; Inference Labs, *Analysis of Weight Copying Mitigations in Bittensor*, 2024. Accessed 2026-09-06.

[14] Y. Fraboni, R. Vidal, M. Lorenzi. *Free-rider Attacks on Model Aggregation in Federated Learning.* AISTATS 2021, PMLR 130, 1846–1854. arXiv:2006.11901.

Propositions verified and measurements reproducible from `code/two_pool.py`, which imports the specimen, the beacon and the frame completion from `code/exclusion.py` unchanged.
