# Sybil-asymptotic security — proofs

Working notes. Verified numerically by `code/sybil_bound.py`.

Destination: the paper provisionally titled *The Multiplicity Freedom*.
These are the results it should open with, since none of them needs an adversary
in the loop — which is the whole point, and the reason this fragment closes part
of the gap Vol III left open.

---

## 0. Setup

Fix a Combination Proof M of order K (Def 2.6): reward

> r(s) = f(π₁(s), …, π_K(s)),

with f monotonically non-decreasing in each argument and f(v) = 0 whenever any
vᵢ falls below its threshold tᵢ.

**Adversary.** A holds budget C in the resource of Def 2.4. It may register N
identities, allocate its budget among them, and collects Σⱼ r(sⱼ).

**Per-projection gate cost.** γᵢ = C(πᵢ, tᵢ ; A) — the fake-cost of bringing
projection i to its threshold on one identity (Def 2.4). Write γ for the uniform
case.

**Per-identity gate cost.** Γ = the minimum expenditure that brings *all* K
projections on a single identity to their thresholds.

---

## 1. Three hypotheses, and where they come from

The results below need exactly three assumptions, and the pleasing thing —
which is the paper's structural argument — is that **each one is already an
anchor the program built, for reasons that had nothing to do with Sybils.**

**(H1) Duplication-non-invariance.** r is not invariant under duplication of a
state: a copy does not earn what the original earns.

> Without H1 nothing below holds. An adversary would pay Γ once, copy the state
> N times, and field N identities for the price of one — cost independent of N.
> H1 is exactly Gauge-Fixing's second test-suite demand and its unique-encoding
> anchor (§4.3), and exactly the copy-symmetry problem of Proof of Coherence
> §4.2. It is what makes expenditure *additive across identities*.

**(H2) A positive resource floor.** γᵢ > 0 for at least one i.

> Without H2, Γ = 0 and N is unbounded. This is Douceur's impossibility result
> in the notation: absent a constrained, verifiable resource, Sybil attack is
> always available. H2 is Gauge-Fixing's dissipation floor — the anchor that, in
> Proof of Preservation's words, "prices the minting of identities and does
> nothing else, so that the count of witnesses means something."

**(H3) Approximate independence, graded.** ι ∈ [0,1] as in CP §7.1: the fraction
of π_j's fake-cost not recoverable from having faked πᵢ.

> H3 determines how Γ grows with K, and therefore how much richness buys. It is
> the framework's existing load-bearing assumption, doing a second job here.

Three of the four forger freedoms named at Proof of Preservation §58 —
duplication, multiplicity, and (via ι) the reuse of ground work — appear here as
H1, H2, H3. The fourth, backdating, does not enter these results.

---

## 2. Lemma (cost of the conjunction)

Under H3, the cost of clearing all K gates on one identity is

> Γ = γ₁ + Σ_{k=2}^{K} (marginal cost of π_k given π₁ … π_{k-1} already faked).

The framework does not fix the marginal term, so take the two natural models. In
the uniform case γᵢ = γ:

**Linear recoverability** — each further projection costs ιγ:

> Γ_lin = γ · (1 + (K−1)ι)

**Compounding recoverability** — the k-th projection costs ι^{k−1}γ, so having
faked more predecessors makes the next one cheaper still:

> Γ_cmp = γ · (1 − ι^K)/(1 − ι),  and Γ_cmp = γK at ι = 1

Both agree at ι = 0 (Γ = γ) and ι = 1 (Γ = γK), and Γ_cmp ≤ Γ_lin in between.
Which model holds is an **empirical question about a substrate**, not something
to be settled by choosing. It matters a great deal — see §4.

---

## 3. Theorem 1 (the Sybil cap)

**Statement.** Under H1 and H2, an adversary with budget C can field at most

> N ≤ ⌊ C / Γ ⌋

identities that receive non-zero reward, whatever allocation it chooses.

**Proof.** Let J be the set of identities receiving non-zero reward. By
conjunction-gating, j ∈ J implies πᵢ(sⱼ) ≥ tᵢ for every i, so by definition of Γ
the adversary expended at least Γ on identity j. By H1, expenditure on distinct
identities cannot be shared — a state that earns for j does not also earn for
j′ — so the expenditures are additive. Hence |J|·Γ ≤ C. ∎

**Verified.** `sybil_bound.py` T1: six random instances, fielded count equals
⌊C/Γ⌋ in every case; exhaustive search over discretised allocations in small
cases finds no uneven split that exceeds the bound.

**Remark.** Taken alone this is close to definitional — identities cost Γ, so you
get C/Γ of them. Its content is entirely in what Γ *is*, which is the next
theorem. The reason to state it separately is that it isolates H1 and H2: the
bound exists at all only because copies do not pay and identities are not free.

---

## 4. Theorem 2 (richness amplification, and its ceiling)

**Statement.** Under H1–H3, with uniform γ and the linear model,

> N ≤ C / [ γ (1 + (K−1)ι) ]

and since a Combination Proof cannot have order exceeding richness (K ≤ ρ(𝒮),
CP §5), the strongest cap any mechanism on that substrate can achieve is
C / [γ(1 + (ρ−1)ι)].

**So richness bounds Sybil resistance and Goodhart resistance alike** — the same
ceiling, two properties. The framework currently claims only the second.

**Corollary 2a (independence is everything).** At ι = 1 the cap falls as 1/K:
each projection divides the adversary's fleet. At ι = 0 the cap is C/γ for every
K: **richness buys nothing at all.** Conjunction-gating amplifies the resource
floor by a factor of exactly 1 + (K−1)ι, and by nothing if the projections are
redundant.

**Corollary 2b (the amplification has a hard ceiling under compounding).**

> Γ_cmp = γ(1 − ι^K)/(1 − ι) → γ/(1 − ι) as K → ∞

so N ≥ C(1 − ι)/γ no matter how many projections are added. **Under compounding
recoverability, no amount of richness drives the Sybil cap below C(1−ι)/γ.**
Only at ι = 1 exactly does amplification scale without limit.

Verified (T2 table, γ=1, C=100): at ι = 0.25, going from K = 4 to K = 8 moves the
compounding cap from 75.3 to 75.0 — saturated — while the linear cap moves from
57.1 to 36.4. The two models diverge by a factor of two at K = 8, so **the choice
between them is not cosmetic and cannot be left open in the paper.**

**Sobering internal evidence.** `independence.py` measured ι ≈ 0 at the operating
threshold for a structure-aware adversary on the nested complex — the kernel and
the spectral dimension moved together. If that generalises, Corollary 2a says
richness buys no Sybil resistance on that substrate. The measurement was of two
projections of the *same operator*, which is the worst case for independence, so
it does not settle the general question. But it must be reported, and it is the
strongest reason to think ι is the quantity the whole program turns on.

---

## 5. Theorem 3 (only convexity punishes splitting)

Theorem 1 caps the fleet. It does **not** say splitting is unprofitable within
the cap — that depends on the shape of f above the gate.

**Statement.** Let f be defined on the gated region with f(0) = 0.

1. If f is convex, then N·f(v/N) ≤ f(v) for all N ≥ 1: splitting is never
   profitable. Strictly convex ⟹ strictly unprofitable.
2. If f is linear, N·f(v/N) = f(v): splitting is exactly **Sybil-neutral**.
3. If f is strictly concave, N·f(v/N) > f(v): splitting is strictly profitable.

**Proof.** For f convex with f(0) = 0 and λ ∈ [0,1],
f(λv) = f(λv + (1−λ)·0) ≤ λf(v) + (1−λ)f(0) = λf(v). Take λ = 1/N and multiply
by N. Strictness follows from strict convexity for v ≠ 0. Linearity gives
equality; strict concavity reverses the inequality throughout. ∎

**Verified** (T3, v = 10): v² gives ratios 0.500 / 0.250 / 0.125 at N = 2/4/8
(exactly 1/N); v^1.5 gives 0.707 / 0.500 / 0.354 (exactly N^−1/2); identity gives
1.000 throughout; √v gives 1.414 / 2.000 / 2.828 (exactly √N); log1p gives
1.494 / 2.090 / 2.705.

**Corollary 3a — the design warning, and the most useful thing here.**
Diminishing-returns reward curves are the standard choice for limiting whale
dominance and encouraging decentralisation. Above the gate they are
**Sybil-positive**: a square-root reward pays an adversary 2.83× as much for
splitting into eight identities as for concentrating. The shape chosen to prevent
concentration actively subsidises fragmentation. A conjunction-gated mechanism
that wants Sybil resistance must be **convex above its gates and gated at the
bottom** — the gate caps the fleet, the convexity makes splitting a loss, and
neither does the other's job.

---

## 6. What is not proven

- **Γ is only as precise as Def 2.4.** The framework declines to fix the resource
  r ("some mixture of compute, capital, and the rarer resource of capability"),
  so Γ is defined relative to an attacker class and these are bounds in that
  relative sense, not absolute numbers.
- **The two ι models are models.** Neither is derived from the framework, and §4
  shows they disagree by a factor of two at K = 8. Deciding between them for a
  concrete substrate is the first open problem the paper should name.
- **H1 is assumed, never established.** No concrete mechanism in the corpus has
  been shown to be duplication-non-invariant; Gauge-Fixing §5 *demands* it as a
  test and Proof of Coherence §4.2 offers two candidate resolutions (Shapley,
  provenance-weighting) without settling either. Every result here is conditional
  on a property the program has specified and not yet verified.
- **No collusion.** Sybils are treated as an adversary partitioning its own
  budget. Coalitions between Sybils and honest participants, and Sybils
  distributed across levels of a holarchy, are untouched — and the second of
  those is where *Gluing the Gates* would say the interesting failures live.
- **Nothing about detection.** These are bounds on what an adversary can field,
  not procedures for noticing that it has.

---

## 7. Consequences for the paper

The results give it an unusual shape for this corpus: it can **open with
theorems** rather than with a derivation, which no paper in the program has done.
The narrative writes itself from §1 — three hypotheses, each an anchor the
program already built for other reasons, and the Sybil bound falls out of their
conjunction. That is the same argumentative move as Gauge-Fixing's ("compose
anchors until only honest sections survive"), one layer up.

The honest headline is not "conjunction-gating gives Sybil resistance." It is:

> **Conjunction-gating amplifies the resource floor's Sybil resistance by a
> factor of 1 + (K−1)ι, and by nothing at all if the projections are redundant.
> Under compounding recoverability the amplification saturates at 1/(1−ι) no
> matter how rich the substrate. The gate caps the adversary's fleet; only
> convexity above the gate makes splitting a loss; and diminishing-returns
> rewards, the conventional anti-concentration choice, subsidise Sybils.**

Which does shrink the security gap, as proposed — but by less than the initial
statement of the idea suggested, and the shrinkage is entirely a function of ι.
Everything in this program now points at that one quantity.
