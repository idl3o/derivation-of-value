---
layout: document
title: "A World with Memory"
subtitle: "The Pool as Conditional Entropy, and the Resolution of the Gate"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /a-world-with-memory/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-09-08
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "One's Own Anchor left its one surviving reading with a memoryless world, and its coalition was the weakest attacker in the class that holds nothing but the public record. Against the optimal predictor the reading's price is a step in the world's innovation given the record, and a world with momentum shrinks that innovation at fixed drift until the coalition passes at zero derivations and, past a point, sits below honest: the record is a better model of the world than a fresh derivation. The budget the exclusion principle partitions is the entropy of the world conditional on everything public, plus the anchors' own; ι and τ are ratios of conditional information, and the four constraints the corpus had accumulated on ι are met by that reading in one line each. The gate's resolution is the honest derivation variance, so refusing the predictor on a world of innovation q costs every honest participant k of order σ²/q derivations per prompt: evidencing is priced in inverse proportion to how much there is to evidence. Fresh prompts restore the pool at any memory, at the semantic cost the cover line named and did not price."
status: "v0.1 · working draft"
order: 27
---

*v0.1 · working draft. Answers* One's Own Anchor *§9.1 and takes up* Combination Proofs *§7.1 in the form the exclusion line left it. Instrument `code/world_memory.py`, calibrated on the predecessor's published step before any new number was read.*

## Abstract

*One's Own Anchor* found one reading with a native share — restriction maps fitted at overlaps, gated on every edge's residual after commitment — and found that what it evidences is the world's innovation since the last public record. Its world was AR(1), memoryless, so the innovation given the record was the whole one-step drift and the coalition it wrote down, last epoch's record decayed, was the optimal predictor. §9.1 of that paper asked what a world with memory does to the price. This paper answers it with the coalition the predecessor's class actually contains: the conditional mean of the world given every record so far, which for a Gaussian linear world is the Kalman filter. On a world with momentum — the same drift per epoch as the predecessor's failing row, of which a fraction φ² is predictable from the past — the predictor's error is the steady state of a Riccati recursion, at least the innovation q = (1 − φ²)δ² and tending to it as the record's sources multiply, and the coalition passes at zero derivations exactly when that error falls below a threshold set by the gate: measured at every setting to the third decimal on the mean residual, with the pass calls landing where the *maximum* over gated edge-epochs puts them, which the first prediction missed by using the mean, and the paper records the miss. Past φ = 0.95 with shared prompts the predictor's residual is below honest's own: the record is a better model of the world than a fresh derivation, and the fiction is truer than honesty. The general statement is then made. The paid pool of *Independent and Expensive* is the entropy of the world conditional on the public record, plus the anchors' own entropy; a projection's trace gap is the least information about that pool a passing section must carry, over the pool, and its independence from another projection is the fraction of that information the other does not already extract. So defined, ι degenerates where the claim vanishes, is asymmetric, reduces to claim-disjointness in the set model, and against the reading's own anchor gives the native share when multiplied by τ — the four constraints the corpus had accumulated, met in one line each — and the pairwise exclusion and the budget law are the chain rule. The metric-versus-divergence fork of *Combination Proofs* §7.1 resolves as both with different jobs: ι is a ratio of divergences, and the Fisher information of k derivations, k/σ², is the gate's *resolution*. The pass threshold is proportional to the honest derivation variance σ²/k, so refusing the predictor on a world of innovation q costs every honest participant k ≥ c σ²/q derivations per prompt, c set by the gate's own spread; measured, the predictor passes up to k = 8 and fails from k = 16 with shared prompts, and fails from k = 4 with edge-local ones, where the record's noise is on the mechanism's side. A fully predictable world is expensive to evidence in proportion to how little there is to evidence. Fresh prompts — a column the record has never covered — defeat the predictor at any memory and restore the predecessor's boundary share to the fourth decimal, at the semantic cost *Every Basis at Once* §8.1 named and did not price. The prior art is drawn: that agents report the prior instead of investing effort, and that a mechanism can pay only for information beyond the public state, are the effort-elicitation and market-scoring literatures; the identification of the exclusion line's budget with that entropy, the formalisation meeting the corpus's four constraints, the step on the sheaf against the optimal record-only attacker, the resolution law and its measurements are claimed.

---

## 1. The Weakest Attacker

*One's Own Anchor* §6 committed sections before comparing them and priced the coalition that holds no model of the world by what it must derive: above a step in the world's innovation δ the coalition's best input, last epoch's public record, fails the residual gate on its boundary edges and it pays honest's rate there. The step was where the arithmetic put it, at δ* = (σ/√k)·√(tol²k/σ² − 1 − 1/b), measured at 1.50 against 1.58 and 1.75 against 1.87 in units of the honest noise σ/√k.

The world in that instrument was AR(1): G(t) = √(1−δ²)·G(t−1) + δ·ξ(t). For a memoryless world the last record, decayed, *is* the conditional mean of G(t) given everything public, and the coalition was optimal in its class. §9.1 said what the class contains once the world has memory: "for a world with momentum it is the extrapolation error, smaller; for a world an adversary can partly predict from outside the network it is smaller still." The supremum-over-attackers rule the corpus adopted in *The Multiplicity Freedom* v0.4 and applied to every baseline since — a fake-cost is a minimum over strategies, and a single weak strategy fabricates a result — applies to the world as well as to the reading. A coalition that can extrapolate is stronger than one that copies, and the price the predecessor measured is a ceiling.

This paper takes the class to its supremum. The coalition holds the public record and nothing else, and its estimate of the world is the conditional mean given the record: for a Gaussian linear world, the Kalman filter [8]. Three questions are asked of the instrument, in the order the corpus prefers. Whether the predecessor's step reproduces at zero memory. What the optimal predictor does at the predecessor's failing drift once the drift has memory. And what it costs the mechanism to refuse it.

The answer to the third is the paper's result and it has two halves. The world's innovation given the record is the pool the exclusion line has been partitioning, stated in the currency the surviving reading measures. And the gate reads that pool at a resolution set by honest work, so a predictable world is expensive to evidence in exact proportion to how little of it there is.

---

## 2. Prior Art, and the Boundary of the Claim

The prior-art check was run before drafting, per the rule that has caught this program four times.

**That an agent reports the prior instead of investing effort** is the effort-elicitation problem of peer prediction. Dasgupta and Ghosh model proficiency as endogenous and the shirking agent as one who reports without observing [1]; Radanovic, Faltings and Jurca's peer truth serum pays for information beyond a public prior, so that reporting the prior earns nothing in expectation [2]. The predictor of §4 is that shirker with the best prior available — the record, filtered — and the step of Proposition 4.1 is the condition under which the mechanism can tell it from an observer.

**That a mechanism can pay only for information beyond the public state** is Hanson's market scoring rule [4, 5]: a trader's expected payment is the improvement of the market's estimate over its current public price, so a world the price already predicts yields nothing to trade. Kong and Schoenebeck's mutual-information paradigm pays each agent the mutual information between her report and a peer's, and shows any garbling of a report reduces it [3]; the information two honest neighbours share beyond the record, I_pair of §4, is that quantity for the residual reading, and the paper's claim is what a gate at overlaps can *see* of it. Holmström's informativeness principle is the sixty-year-old form [6]. Bara states the Sybil-resistance criterion as I(Θ; Z | R) = 0 [7], concurrently with *One's Own Anchor* and independently; this paper's §3 is the accounting that criterion implies for the exclusion line.

**That prediction from a noisy record is a Kalman filter** is 1960 [8], and the steady-state Riccati recursion is textbook. **That the maximum of N chi-square variates sits at the (1 − 1/N) quantile**, and the Wilson–Hilferty approximation to that quantile [11], are older than the mechanism-design literature and are used here to correct a prediction. **That sample complexity governs what an information measure can be estimated from** is Aznag et al. [10], concurrent and adjacent: their question is how many samples an unbiased estimator of a mutual information needs; this paper's is how many derivations a *gate* needs before the information is visible to it at all.

What is claimed. That the paid pool of *Independent and Expensive* — the budget its exclusion principle partitions — is the entropy of the world conditional on the public record, plus the anchors' entropy, and that ι and τ so defined meet the four constraints the corpus accumulated on them (§3). That against the optimal record-only attacker the residual reading's price is a step in the world's innovation given the record, on the program's own sheaf, with the constant corrected from the mean to the maximum and the correction on record (§4). That the gate's resolution is the honest derivation variance, so the price of evidencing a world scales as the inverse of its innovation (§5). And the measurements. *Combination Proofs* §7.1 conjectured that ι would be information-theoretic; the conjecture was the program's, and §3 is the first time it has been written down against the constraints and checked.

---

## 3. The Pool Is the Entropy of the World Given the Record

The set model of *Independent and Expensive* §3 divided a substrate's degrees of freedom into paid and free, and *One's Own Anchor* §3 divided the paid ones into anchor work and native work. Both papers declared the model a simplification and asked (*I&E* §8.1) whether the partition law survives a graded cost structure. This section supplies the graded structure the surviving reading already implies.

**Setting.** Epochs t. A world W_t, the random variable the honest participant derives from. A public record R_{t−1}: every section published before epoch t, every anchor value revealed, every frame declared. An anchor A_t: the entropy the receipt check reads — the beacon draw, the chain's output — fresh at each epoch and independent of the world. A section X_v(t), committed before the epoch's reveal. A projection π with a gate, and the honest acceptance probability the gate is set to.

**Definition 3.1 (information claim).** For a projection π and a conditioning variable Z that includes the record, the *information claim* of π given Z is

> I_min(π | Z) = inf I( X ; W_t, A_t | Z ),

the infimum over section laws that pass π's gate with honest's acceptance probability. It is the least information about the world and the anchor, beyond Z, that a passing section must carry. In the cost model it is the fake-cost, with information as the currency: a forger who holds Z must acquire I_min(π | Z) from somewhere, and in the model the only sources are derivation and the anchor's receipt.

**Definition 3.2 (pool, trace gap, independence, native share).** The pool at epoch t is h_t = h(W_t | R_{t−1}) + h(A_t). Then

> τ(π) = I_min(π | R) / h_t,   ι(π | π′) = ( I_min(π ∧ π′ | R) − I_min(π′ | R) ) / I_min(π | R),   τ_N(π) = ( I_min(π ∧ π_A | R) − I_min(π_A | R) ) / h_t,

where π_A is the receipt check, whose claim is I_min(π_A | R) = h(A_t).

**Proposition 3.3 (the four constraints).** *Independent and Expensive* §7 and *One's Own Anchor* §3 handed P6 four constraints. Each is met.

(i) *Degenerate where claims vanish.* I_min(π | R) = 0 makes ι(π | π′) a ratio with zero denominator, undefined; τ(π) = 0 there. This is the free corner of *I&E* §5, where measured ι moved with the attack, as the quantity's degeneracy rather than a defect of the instrument.

(ii) *Asymmetric.* Let π′ read a strict subset of what π reads, with I_min(π′) < I_min(π) and I_min(π ∧ π′) = I_min(π). Then ι(π′ | π) = 0 and ι(π | π′) = 1 − I_min(π′)/I_min(π) > 0. The asymmetry encodes attack ordering, as *Combination Proofs* §7.1 said it should.

(iii) *Claim-disjointness in the set model.* Let the world be |P| independent uniform bits, each costing one unit to derive, and the free degrees of freedom be computable from the record. A projection reading S has I_min = |S ∩ P| bits, the conjunction I_min = |(S ∪ S′) ∩ P|, and ι(π | π′) = |S ∩ P ∖ S′| / |S ∩ P|, which is *I&E* Definition 2.5 verbatim; h_t = |P| = W and τ = |S ∩ P| / W.

(iv) *The native share.* τ_N(π) = ι(π | π_A) · τ(π), by the same algebra as *One's Own Anchor* Proposition 3.2. And for a declared-frame reading, I_min(π ∧ π_A | R) = h(A_t): a forger holding the anchor reproduces honest's law with no further information, which is Theorem 3.4 of that paper in this currency.

**Corollary 3.4 (the exclusion and the budget law are the chain rule).** τ(π₁) + ι(2 | 1)·τ(π₂) = I_min(π₁ ∧ π₂ | R) / h_t ≤ 1, since no section carries more information about (W_t, A_t) beyond R than their conditional entropy; equality when a passing section determines them. For any K, I_min(π₁ ∧ … ∧ π_K | R) ≤ h_t: richness partitions the pool and nothing multiplies it, because conditional mutual information is bounded by conditional entropy. *I&E* Theorems 3.3 and 3.4, without the set model.

**What the definition says about the world.** The native part of the pool, h(W_t | R_{t−1}), is not a property of the mechanism. It is the world's innovation given everything public, and it is the quantity the surviving reading prices. For a world whose record reveals its past exactly, it is the entropy rate h(W_t | W_{<t}); for a Gaussian world with the momentum of §4 that is (dM/2)·log(2πe·(1 − φ²)δ²) per epoch, which at fixed one-step drift δ² falls by (dM/2)·log(1 − φ²) as memory rises. A world with memory shrinks the pool. That is the theorem §9.1 asked for, and it is one line; what is not one line is what the gate can claim of a pool that has shrunk, which is §§4–5.

**The fork in §7.1.** *Combination Proofs* asked whether ι is a metric on projection space, in the Fisher sense, or a divergence, and recorded that the measured asymmetry favours the divergence. Definition 3.2 is a ratio of conditional informations — a divergence, asymmetric by construction. Fisher information is not discarded; it enters in §5 as the gate's resolution, which is a different job.

---

## 4. The Step, With Memory

`code/world_memory.py`. Everything not stated here is *One's Own Anchor* §4: d = 3, m = 16, σ = 0.3, k = 4, tol = 1.5·σ·√(2/k) = 0.318, s = σ²/k = 0.0225, the seed-7 complex with n = 256 and 371 edges, the block coalition of 128, and the residual gate on every edge. Twenty-four epochs, of which the first four are excluded from scoring so the filter has settled; forty gated boundary edge-epochs per run.

**The world.** G(t) = G(t−1) + Δ(t), Δ(t) = φ·Δ(t−1) + √(1−φ²)·δ·ξ(t), with Δ(0) stationary and ξ standard normal, seeded from the world's family and disjoint from the beacon's. The one-step drift has variance δ² at every φ. The fraction of it predictable from the exact past is φ², and the innovation given the exact past is q = (1 − φ²)·δ². At φ = 0 the world is a random walk with the AR(1) world's one-step error, so the predecessor's step must reproduce there. δ is held at the predecessor's failing row, 3 σ/√k = 0.45, throughout §4.

**The attackers**, each holding the record and nothing else. *Naive*: last record — the predecessor's coalition. *Extrapolate*: last record plus φ times the last difference. *Kalman*: the conditional mean of G(t) given every record, per column, with the record's noise s/b for b honest sources on the column; its one-step error v_pred is the steady state of the Riccati recursion, at least q and tending to q as b → ∞. Wherever the predictor fails, the derive-the-boundary strategy of the predecessor is run and its cost counted.

**Proposition 4.1 (the step).** The predicting coalition's boundary residual squared is (v_pred + s)·(1 − 1/m) per entry in expectation, and the gate takes the maximum over N gated edge-epochs, each a chi-square variate on ν = dm − 3 degrees of freedom. It passes iff

> v_pred < v*_N = tol² / ( (1 − 1/m)·c_N² ) − s,

where c_N² is the (1 − 1/N) quantile of χ²_ν/ν. On the specimen c_N² = 1.45 at N = 40 and v*_N = 2.30 s. The mean-based threshold, c = 1, is 3.80 s.

**Calibration.** On the predecessor's scoring window — eight epochs, scored from the second — the naive attacker on the random walk fails first at δ = 1.50 (edge-local) and 1.75 (shared) in units of σ/√k, the imported instrument's grid points exactly. On this paper's window of twenty scored epochs the edge-local call moves one grid step earlier, to 1.25: the gate is a maximum, and a longer window has a higher one. That is the first sign of the correction below, and it was read as a miss before it was understood.

**Three attackers at φ = 0.9.**

| prompts | attacker | honest r | coalition r | predicted | v_pred / s | passes | derive passes |
|---|---|---|---|---|---|---|---|
| edge-local | naive | 0.2072 | 0.4607 | 0.4817 | 10.00 | no | yes |
| edge-local | extrapolate | 0.2072 | 0.3983 | 0.3878 | 6.13 | no | yes |
| edge-local | kalman | 0.2072 | 0.3320 | 0.3291 | 4.13 | no | yes |
| shared | naive | 0.2035 | 0.4801 | 0.4595 | 9.01 | no | yes |
| shared | extrapolate | 0.2035 | 0.2408 | 0.2406 | 1.74 | **yes** | yes |
| shared | kalman | 0.2035 | 0.2408 | 0.2406 | 1.74 | **yes** | yes |

The drift is the predecessor's δ = 3 row, at which its coalition failed under both prompt models. With shared prompts, where the record has 128 sources per column, the extrapolator already passes at zero derivations and the filter adds nothing to it. With edge-local prompts and one source per column the record's noise enters the velocity estimate at (1 + φ)² + φ² times s/b, and the filter, which averages the velocity over the whole record, brings the error from 6.1 s to 4.1 s and still fails. The naive rows sit a few per cent under their prediction: the momentum world's drift is highly autocorrelated, and twenty epochs of it is a small sample of its stationary variance. Every Kalman row matches to the third decimal.

**The sweep in φ.**

| prompts | φ | q / s | v_pred / s | I_pair | honest r | coalition r | predicted | passes | e(C) | per identity |
|---|---|---|---|---|---|---|---|---|---|---|
| edge-local | 0.00 | 9.00 | 9.91 | 0.830 | 0.2087 | 0.4789 | 0.480 | no | 0.0054 | 1.0 |
| edge-local | 0.50 | 6.75 | 8.75 | 0.711 | 0.2082 | 0.4566 | 0.454 | no | 0.0054 | 1.0 |
| edge-local | 0.80 | 3.24 | 5.79 | 0.438 | 0.2075 | 0.3824 | 0.378 | no | 0.0054 | 1.0 |
| edge-local | 0.90 | 1.71 | 4.13 | 0.254 | 0.2072 | 0.3320 | 0.329 | no | 0.0054 | 1.0 |
| edge-local | 0.95 | 0.88 | 2.99 | 0.123 | 0.2070 | 0.2917 | 0.290 | no | 0.0054 | 1.0 |
| edge-local | 0.99 | 0.18 | 1.53 | 0.012 | 0.2065 | 0.2322 | 0.231 | **yes** | 0 | 0 |
| shared | 0.00 | 9.00 | 9.01 | 0.830 | 0.2041 | 0.4612 | 0.459 | no | 0.0078 | 0.5 |
| shared | 0.50 | 6.75 | 6.77 | 0.711 | 0.2040 | 0.4048 | 0.405 | no | 0.0078 | 0.5 |
| shared | 0.80 | 3.24 | 3.27 | 0.438 | 0.2036 | 0.2998 | 0.300 | no | 0.0078 | 0.5 |
| shared | 0.90 | 1.71 | 1.74 | 0.254 | 0.2035 | 0.2408 | 0.241 | **yes** | 0 | 0 |
| shared | 0.95 | 0.88 | 0.91 | 0.123 | 0.2034 | **0.2021** | 0.201 | **yes** | 0 | 0 |
| shared | 0.99 | 0.18 | 0.21 | 0.012 | 0.2034 | **0.1628** | 0.160 | **yes** | 0 | 0 |

I_pair is the mutual information two honest neighbours share beyond the record, −½·log(1 − (q/(q+s))²) per entry: everything a comparison at an overlap has to see, (q/s)²/2 when q ≪ s. The drift is 3 σ/√k in every row. What moves is the fraction of it the record predicts, and three things are in the table.

**The coalition's share is a step in the innovation given the record.** e(C) is the predecessor's boundary share, 0.0054 edge-local and 1/128 shared, wherever the predictor fails, and zero wherever it passes; there is nothing in between, because above the step the coalition derives its boundary as before and below it derives nothing. The pass calls land where Proposition 4.1 with c_N puts them and nowhere else: edge-local passes only at φ = 0.99 (v_pred = 1.53 s < 2.30 s) and fails at 0.95 (2.99 s); shared passes from 0.90 (1.74 s) and fails at 0.80 (3.27 s).

**The first prediction was wrong, and the record says so.** Predictions were stated in the instrument's docstring before running, with the mean-based threshold 3.80 s: edge-local at φ = 0.95 and shared at φ = 0.80 were predicted to pass and failed, and two calls in §5 moved the same way. Every mean residual matched its prediction to the third decimal; only the pass calls at the edge were wrong, and they were wrong because the gate is a maximum over forty samples and the mean is not. The quantile correction is in Proposition 4.1 and resolves all four with no new miss; the original constant is printed beside it in the instrument. This is the corpus's usual route to a correction — an impossible pattern, four misses in one direction — and it is recorded rather than repaired.

**Past φ = 0.95 with shared prompts the coalition is below honest.** The predictor's residual is 0.2021 against honest's 0.2034 at φ = 0.95 and 0.1628 against 0.2034 at 0.99: the record, filtered, is a better estimate of the world than a fresh derivation at noise s, exactly when v_pred < s. In such a world the fiction is truer than honesty, and the reading cannot see which is which because there is no difference to see. *The Budget Across Levels* §6 found a fabrication of honest scale sitting inside honest's spread at no cost; this is that finding with the world supplying the fabrication.

---

## 5. The Resolution of the Gate

Proposition 4.1's threshold is proportional to s = σ²/k: the gate's resolution is the honest derivation variance, and the only way to lower it is to demand more derivations of every honest participant.

**Proposition 5.1 (the price of evidencing).** With tol = 1.5·σ·√(2/k) scaling with k, the predictor passes iff v_pred(k) < c·σ²/k with c = 4.5/((1 − 1/m)·c_N²) − 1, which is 2.30 at N = 40. As b → ∞, v_pred → q and the predictor is refused iff

> k ≥ k* = c·σ² / q.

Refusing the optimal record-only attacker on a world of innovation q costs every honest participant k* derivations per prompt, and the mechanism's total honest cost per epoch, k*·m·Σ deg(v), scales as 1/q.

**Measured**, at φ = 0.95, δ fixed at 0.45 in absolute units, q = 0.0197, predicted k* = 2.30·0.09/0.0197 = 10.5 (mean-based 17.3).

| prompts | k | s | tol | v_pred | v*_N | honest r | coalition r | passes |
|---|---|---|---|---|---|---|---|---|
| edge-local | 1 | 0.0900 | 0.636 | 0.1424 | 0.2072 | 0.4140 | 0.4708 | yes |
| edge-local | 2 | 0.0450 | 0.450 | 0.0965 | 0.1036 | 0.2927 | 0.3665 | yes |
| edge-local | 4 | 0.0225 | 0.318 | 0.0674 | 0.0518 | 0.2070 | 0.2917 | **no** |
| edge-local | 8 | 0.0112 | 0.225 | 0.0488 | 0.0259 | 0.1464 | 0.2384 | no |
| edge-local | 16 | 0.0056 | 0.159 | 0.0371 | 0.0129 | 0.1035 | 0.2007 | no |
| shared | 1 | 0.0900 | 0.636 | 0.0227 | 0.2072 | 0.4070 | **0.3310** | yes |
| shared | 2 | 0.0450 | 0.450 | 0.0213 | 0.1036 | 0.2877 | **0.2526** | yes |
| shared | 4 | 0.0225 | 0.318 | 0.0205 | 0.0518 | 0.2034 | **0.2021** | yes |
| shared | 8 | 0.0112 | 0.225 | 0.0202 | 0.0259 | 0.1438 | 0.1712 | yes |
| shared | 16 | 0.0056 | 0.159 | 0.0199 | 0.0129 | 0.1017 | 0.1534 | **no** |
| shared | 32 | 0.0028 | 0.112 | 0.0198 | 0.0065 | 0.0719 | 0.1436 | no |

Honest passes every edge at every k by construction of tol. The shared predictor passes to k = 8 and fails from 16, on either side of k* = 10.5; the edge-local predictor fails from k = 4, because with one source per column the record's own noise is on the mechanism's side and v_pred exceeds q by a factor of three. Bold coalition residuals are below honest's, at k ≤ 4 with shared prompts, where v_pred < s. The rows are what Proposition 5.1 says with the constant corrected, and the two k-sweep calls the mean-based constant got wrong — shared failing from 32, edge-local from 8 — are in the instrument's record.

**Fisher, and what the metric prices.** k derivations at noise σ² carry Fisher information k/σ² per entry about the world; q·k/σ² is the signal-to-noise ratio of the innovation against the honest noise, and the gate resolves the innovation only above the ratio 1/c its own spread sets. The information *content* of the world beyond the record is the divergence of §3; the information *resolution* of the gate is the metric. *Combination Proofs* §7.1 posed them as rivals for one job. They have two.

**Fresh prompts.** The bound is on recorded prompts. If every epoch's prompts are new — no column the coalition must fit has ever appeared in the record — the predictor has nothing to predict from and its error is the world's whole variance.

| prompts | φ | record | honest r | coalition r | passes | e(C) | designed |
|---|---|---|---|---|---|---|---|
| edge-local | 0.90 | full | 0.2072 | 0.3320 | no | 0.0054 | 0.0054 |
| edge-local | 0.90 | none | 0.2068 | 4.9463 | no | 0.0054 | 0.0054 |
| edge-local | 0.99 | full | 0.2065 | 0.2322 | yes | 0 | 0.0054 |
| edge-local | 0.99 | none | 0.2079 | 6.0564 | no | 0.0054 | 0.0054 |
| shared | 0.90 | full | 0.2035 | 0.2408 | yes | 0 | 0.0078 |
| shared | 0.90 | none | 0.2057 | 4.7859 | no | 0.0078 | 0.0078 |
| shared | 0.99 | full | 0.2034 | 0.1628 | yes | 0 | 0.0078 |
| shared | 0.99 | none | 0.2054 | 5.9057 | no | 0.0078 | 0.0078 |

Rotating the prompts restores the predecessor's share at any memory, to the fourth decimal. What it costs is not in the model: a prompt no participant has held before is *Every Basis at Once* §8.1's semantic cost, named there for the redrawn cover and applying here to the redrawn prompt, and the instrument charges honesty the same k per prompt whether the prompt is old or new. That is a choice of the model, declared in §7.

---

## 6. What the Bound Bought

Read back into the corpus.

**§9.1 is answered, in the direction the paper feared.** The native share of the residual reading is bounded by the world's innovation given the record, and on a world with memory the bound bites at drifts where the memoryless coalition paid honest's rate. The reading survives; what it evidences is smaller than the predecessor measured, by the factor (1 − φ²) at fixed drift and by more once the record's sources multiply. The predecessor's table is a ceiling and the supremum rule said so.

**The exclusion line has a currency.** *Independent and Expensive* proved the partition law in a set model and declared the model a simplification; *The Second Pool* found the two anchors' gaps summing to one minus a reconciliation share; *One's Own Anchor* found the native pool and priced it in derivations. Definition 3.2 is the graded structure §8.1 of the first paper asked for: the pool is h(W_t | R_{t−1}) + h(A_t), the claims are conditional informations, and the partition law is the chain rule. An anchor is a second pool because it is a second entropy source, independent of the world; proof of work's search is the same thing, which is why *I&E* §6 could read it as an anchor. What the model does not do is price a claim in *work* — §7 returns to this.

**P6 has a candidate.** Four constraints, four one-line checks, and the fork in *Combination Proofs* §7.1 resolved as two jobs. What is not shown is the multiplication claim's leading-order clause — that fake-cost multiplies in ι as substrate depth grows — which Definition 3.2 neither proves nor refutes and which §8.2 keeps. The candidate is recorded in *Combination Proofs* v0.7 as a candidate.

**The titles say work; the pool says information; the price says both.** The cost of evidencing is k*·m per prompt with k* = c σ²/q: work, in the unit the honest participant pays, set by information, in the unit the world supplies. Neither alone. A mechanism cannot choose its world's innovation. It can choose its resolution, and the resolution is bought from every honest participant at once.

**The cover line has a second reason to exist.** *Every Basis at Once* redrew the cover to raise a coalition's boundary. Fresh prompts redraw the *record*, and a column the record has never covered cannot be predicted from it at any memory. The two redraws have the same price — a prompt the participant has no reason to hold — and EB §8.1's semantic cost is now the price of the pool as well as of the cut. The design curve that paper asked for has a third axis.

**The fiction is truer than honesty, once.** Below v_pred = s the record is a better model of the world than a derivation at noise s, and *A Consistent Fiction*'s closure result is inverted on a predictable world: the operationally closed mechanism, reading only its own record, produces a *better* section than contact does. Nothing is wrong with the reading. What is evidenced is contact with what the record does not contain, and where the record contains nearly everything there is nearly nothing to evidence, and the honest participant is paying for noise.

**Conjecture R, a twelfth time.** The formalism imported was information theory. It relocated the difficulty from the reading to the world's entropy rate conditional on the record, which the formalism does not supply and which the mechanism does not control. The relocation is exact and the difficulty is unmoved.

---

## 7. What Is Declined

**That the pool identification is new.** That only information beyond the public state can be paid for is Hanson [4, 5]; that garbling a report reduces its mutual information with a peer's is Kong and Schoenebeck [3]; that the criterion is I(Θ; Z | R) = 0 is Bara [7]. What is claimed is the identification of the exclusion line's budget with that entropy, the definitions meeting the four constraints, and the step and the resolution law on the sheaf.

**That P6 is discharged.** A candidate is on the table that meets the four constraints on the specimens where they were stated. The multiplication claim's leading-order clause is untouched, the definition has been measured only through the native share, and I_min is an infimum over section laws that no instrument in the corpus computes directly. *Combination Proofs* §7.1 remains open with a candidate in it.

**That the world is general.** Gaussian, linear, with the record's noise white; the Kalman filter is optimal there and only there. For a nonlinear world the statement of §3 holds with conditional entropy in place of variance, and Proposition 4.1 has no closed form. A world an adversary can predict from outside the network — a side channel — is not modelled and reprices everything at the side channel's cost, as *One's Own Anchor* §6 already said.

**That the attacker class is exhaustive.** Record-only; the predictor is optimal within it. A coalition with a partial model of the world combines the two and does better; every cost here is a ceiling, measured cost ≥ true cost, always.

**That the first prediction was right.** It was not; §4 records it. The correction is the maximum over gated samples, and its constant is Wilson–Hilferty's approximation to a chi-square quantile, exact to a few per cent, with N counted as the gated edge-epochs of one run. A different scoring window has a different c_N, and the calibration line shows one grid step of that.

**That the resolution law is exact.** k* ∝ σ²/q is the law; the constant is the gate's own spread and depends on the window, the tolerance rule and the degrees of freedom. What is exact is the proportionality and the direction.

**That fresh prompts are free.** The instrument charges honesty k per prompt whether or not the prompt has been seen. *Every Basis at Once* §8.1 says a prompt a participant has no reason to hold costs more, and how much more is not modelled here or there.

**That the result is a defect of the reading.** A reading that cannot distinguish a good model of the world from contact with it is doing what *One's Own Anchor* §8 said it does: it evidences information not computable from the record, and where the record computes the world there is none. The defect, if it is one, is the world's.

**That the naive rows were reproduced.** They sit up to eight per cent under their prediction, inside the draw of a highly autocorrelated drift over twenty epochs, and they are not the paper's numbers; the filter's rows are, and they match.

---

## 8. Open Problems

**8.1. The nonlinear world.** Definition 3.2 is stated for any world; Proposition 4.1 for a Gaussian one. A world whose innovation is not Gaussian — heavy-tailed, or with a predictable component the filter cannot represent — has a step in conditional entropy with no closed form, and whether the resolution law survives with entropy in place of variance is the first question a deployed world would ask.

**8.2. Multiplication to leading order.** The one clause of *Combination Proofs* §7.1 the candidate does not address: whether the fake-cost of a conjunction multiplies in ι as substrate depth grows. In information units the conjunction's claim is a sum bounded by the pool (Corollary 3.4), and a product needs a cost structure that is convex in information, which §3 does not have. The graded model of *Independent and Expensive* §8.1 and this question are one question.

**8.3. The prompt schedule.** Fresh prompts restore the pool; recorded prompts let honesty reuse work. A schedule that rotates a fraction of the prompts each epoch has a pool that interpolates, at a semantic cost that rises with the fraction, and the optimum is a curve with the redrawn cover's curve (*Every Basis at Once* §8.1) as its other axis. Two knobs, one price.

**8.4. The deployed world's innovation.** q/s is measurable from a record alone — the residual of the optimal predictor against the next reveal — and *The Second Pool* §9.4's deployed chain has a record. Whether an actual subnet's world has innovation above or below its mechanism's resolution is an empirical question with a number, and the number decides whether the surviving reading evidences anything there.

**8.5. Paying for the model.** Below v_pred = s the record's model of the world is better than a derivation. A mechanism that scored the *predictor* — paid for the record's own improvement, which is Hanson's market scoring rule on the mechanism's own history — would be paying for exactly what commitment refuses. Whether that composes with the residual gate, and what it evidences, is the service line's question (`_plan/service-reframe.md`) arriving from the pool's side.

---

## References

[1] A. Dasgupta, A. Ghosh. *Crowdsourced Judgement Elicitation with Endogenous Proficiency.* WWW 2013, 319–330.

[2] G. Radanovic, B. Faltings, R. Jurca. *Incentives for Effort in Crowdsourcing Using the Peer Truth Serum.* ACM Transactions on Intelligent Systems and Technology 7(4), 48:1–48:28, 2016.

[3] Y. Kong, G. Schoenebeck. *An Information Theoretic Framework for Designing Information Elicitation Mechanisms That Reward Truth-telling.* ACM Transactions on Economics and Computation 7(1), 2:1–2:33, 2019.

[4] R. Hanson. *Combinatorial Information Market Design.* Information Systems Frontiers 5(1), 107–119, 2003.

[5] R. Hanson. *Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation.* Journal of Prediction Markets 1(1), 3–15, 2007.

[6] B. Holmström. *Moral Hazard and Observability.* Bell Journal of Economics 10(1), 74–91, 1979.

[7] M. Bara. *Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence.* arXiv:2609.01873, 2026.

[8] R. E. Kalman. *A New Approach to Linear Filtering and Prediction Problems.* Transactions of the ASME, Journal of Basic Engineering 82(1), 35–45, 1960.

[9] B. Waggoner, Y. Chen. *Output Agreement Mechanisms and Common Knowledge.* HCOMP 2014, 220–226.

[10] A. Aznag, R. Bowers, R. Cummings, J. Hartline, M. vonAllmen, B. Waggoner. *Sample Complexity of Peer Prediction.* arXiv:2608.16838, 2026.

[11] E. B. Wilson, M. M. Hilferty. *The Distribution of Chi-Square.* Proceedings of the National Academy of Sciences 17(12), 684–688, 1931.

[12] T. M. Cover, J. A. Thomas. *Elements of Information Theory.* 2nd ed., Wiley, 2006.

[13] A. Singer, H.-T. Wu. *Vector Diffusion Maps and the Connection Laplacian.* Communications on Pure and Applied Mathematics 65(8), 1067–1144, 2012.

Propositions verified and measurements reproducible from `code/world_memory.py`, which imports the reading, the coalition and the specimen of `code/evidencing.py` unchanged and reproduces that module's published step on its own scoring window before reading a new number.
