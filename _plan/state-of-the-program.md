# State of the program — 2026-07-30

Working document. Not published to the site. Written to be read cold, by someone
who wants to know what is actually established.

Supersedes the mid-session version of this file, which was written before Volume V
and four of the papers below, and before the finding that reversed one of them.

---

## 1. Shape

**Nineteen documents, orders 1–19, all published.** Nine code modules, ~1,900 lines.
Twelve archived versions, four of which never went live.

| | |
|---|---|
| **Anthology** | Vol I *Derivation of Value* → Vol II ×3 (*Preservation*, *Omnium*, *Kar-Coin*) → Vol III *Admitted or Refused* (open ledger) → Vol IV *Borrowed Hardness* → **Vol V *What Cannot Be Helped*** |
| **Framework** | *Combination Proofs* v0.3 |
| **Whitepaper** | *Proof of Coherence* v0.4 |
| **Papers** | *Gauge-Fixing*, *Gluing the Gates*, *The Multiplicity Freedom* v0.3, *No Global Section*, *Requisite Richness*, *Sign and Work* v0.2, *A Consistent Fiction*, *Coutility*, *Borrowed Again* |

Volume V is the structural event. It named **residue** — the line between what an
action asserts and what it cannot help but leave — as the substrate the program had
derived four times without noticing, then deflated its own claim: residue is
*negentropy with its provenance fixed*, so the anthology has named more substrates
than it has. The substrates differ; the attestation problem does not.

---

## 2. What is established, graded

### Proved

**The Sybil bounds** (*Multiplicity Freedom* §§4–6, `sybil_bound.py`) — the only
theorems the program has. T1: an adversary fields at most ⌊C/Γ⌋ rewarded identities.
T2: Γ = γ(1 + (K−1)ι), so richness bounds Sybil resistance and Goodhart resistance
alike, and buys *nothing* at ι = 0; under compounding recoverability the
amplification saturates at 1/(1−ι). T3: the gate caps the fleet, but only convexity
above it punishes splitting — concave rewards are strictly Sybil-*positive*, at
2.83× for eight identities. **Now conditional on C1 and C2 (see §3).**

**Equilibrium ≠ admissibility** (*Coutility* Prop 4.1). The compositionality of an
equilibrium predicate does not imply the compositionality of an admissibility
predicate. Counterexample is nearly trivial and that is the point.

### Measured

| finding | value |
|---|---|
| ρ as fractional spectral dimension | d_s ≈ 1.61, converged n = 512→4096, R² ≈ 0.999, continuous in coupling across 1.26–2.23 |
| fiction space of a coherent sheaf | **exactly d** — five consensus runs converge to five distinct perfectly-coherent worlds spanning the whole kernel |
| structural coupling to close it | **d scalars, at one vertex, once** — and d per *component*, independent of network size |
| H1 on the rank functional | holds under every credit rule (marginal, Shapley, both provenance forms) |
| H1 on H⁰ | **fails** — scattered duplicates add d each: +3, +6, +12, +24 |
| griefing spread across credit rules | 100% / 50% / 0% (marginal & literal provenance / Shapley / filtered provenance) |
| trace gap τ, unconstrained H⁰ projection | **≈ 0** — the first τ measured, at the worst possible value |
| price of derived hardness | SLH-DSA 7,856–49,856 bytes vs ML-DSA 2,420–4,595 |

### Refuted

**The gap-hierarchy conjecture.** Gap hierarchy tracks exact *geometric*
self-similarity, not nesting. **Gauge-Fixing §5's spectral-gap test stands,
vindicated by the objection it survived.**

**Spectral dimension as an independent third projection.** ι ≈ 0 against a
structure-aware adversary; faking the kernel delivers d_s free. Proposed, tested,
withdrawn.

**That H1 generalises from rank to H⁰** — my own claim, made and reversed the same
day. The rank result was a property of §4.2's *simplification*, not of coherence
substrates.

### Conjectured, untested, load-bearing

- **Conjecture 3.1** (*No Global Section*): the distributional presheaf transfers to
  gate scenarios. **A published paper's quantitative content rests on this.**
- **Claim 4.3** (*Gluing the Gates*): cohomological obstruction under affine gates —
  and it detects failure without certifying safety.
- **Prop 3.1** (*Requisite Richness*): ρ·h ≥ H(D), conditional on a per-projection
  variety bound h that does not exist yet.
- **Claim 3.1** (*Coutility*): coutility propagates a gate. A prescription, not a
  theorem, until a Combination Proof is exhibited as an open game.

### Inconclusive

**Is ι symmetric?** Two attack designs failed — sparsification shatters the complex
and contaminates the kernel proxy with component count; degree-preserving rewiring
stays connected but moves d_s only 8%. ι(dim|ker) = 0.08 is solid; ι(ker|dim) is
unmeasured. **On the critical path and unresolved.**

---

## 3. The two conditions

Worth its own section because it is the session's most transferable finding.

Duplication on H⁰ is unboundedly profitable unless:

- **C1 — participation.** Every scored vertex must be connected to the honest
  complex. §3.1's construction implies it (a miner-task edge exists only if the
  miner submitted), which is *why it went unnoticed*. But that is a modelling
  convention, and an implementation admitting registered-but-inactive miners, or
  scoring disjoint subnets in one eigendecomposition, reintroduces the attack.
- **C2 — kernel tolerance below the spectral gap.** The score is always #{λ < ε},
  never dim ker. **This is the same quantity the §5 test suite already demands be
  measured** — so the gap measurement is not only a coalition-cost check, it is what
  makes the kernel score well-defined. Two requirements that were one, unnoticed.

Both read as numerical hygiene. **A condition that looks like hygiene and is
load-bearing is the kind an implementation drops.** Neither is stated as a security
condition anywhere in the framework.

---

## 4. Seven self-corrections

The most transferable output of the session is not a result.

1. Degenerate eigenvalues counterfeit a gap hierarchy — inflated the gasket to 74
   spurious gaps and the coherent sheaf to 67, *exactly* its stalk multiplicity.
2. Disconnection counterfeits kernel progress — 6.6 and 13.6, above the honest
   maximum, which is impossible.
3. §4.2's provenance formula never worked: r × p leaves M₁ at zero, because
   marginal removal already zeroed r.
4. H1 was stated about individual earnings; the theorem needs group totals.
5. The affine-gate hypothesis is violated by the program's own worked instance.
6. *Gluing the Gates* claimed as novel a structure that is contextuality.
7. Five vectors reported as spanning five dimensions inside a three-dimensional
   kernel — incomplete convergence counted as real directions.

**Four of seven were caught because an instrument returned an *impossible* number
rather than a merely surprising one.** Prefer diagnostics that can return
absurdities over ones that always return something plausible. This is the single
most reusable lesson here.

---

## 5. Through-lines

### Formalisms relocate difficulties; they do not dissolve them

Named in *Coutility* §5 after three instances. Residue relocates attestation, which
is why *Sign and Work* had to define τ. The cohomological invariant detects failure
and certifies nothing. Open games supply a composition operation that is well-typed
and preserves the predicate the framework does not gate on. **Each import was worth
making; each made the difficulty sharper; none made it smaller.** Expect the next
import to do the same.

### The substrate keeps doing the work the mechanism was credited with

H1 holds on rank because rank is a matroid rank function. Richness lives in the
coupling between holons, not the holons. Harvestability is decided before design.
The framework's own doctrine — *design begins with the selection of substrates* —
keeps being confirmed in ways it did not predict.

### One distinction, now derived six times

Outward/inward (Kar-Coin) · harvestable/not (CP §4) · asserted/traced identity
(Sybil) · marker/sematectonic (Sign and Work) · provenance/content (A Consistent
Fiction) · structured/unstructured signatures (Borrowed Again). Volume V named it
and then found it was negentropy-with-provenance. **The question of whether this is
depth or monomania is now partly answered: it is one distinction, and Vol V's
deflation is the honest form of saying so.**

### Everything points at ι

Five dependents: the multiplication claim, richness-as-packing-number, Sybil
amplification, the amplification ceiling, and τ. No formalisation. Two failed
measurements. **The critical path stalled silently this session while easier papers
got written around it** — recorded in the plan as a thing not to repeat.

### The program keeps finding its operator already performed elsewhere

Grassé's entomologists drew the assertion/residue line in 1959. NIST standardised a
hash-only signature scheme in reserve for exactly the reason Vol IV gives, without
the vocabulary. Abramsky characterised local-pass/global-fail fifteen years ago.
**The operator is not the program's invention; its contribution is noticing that
these are the same move.**

---

## 6. Open problems, ranked by leverage

1. **Test Conjecture 3.1.** A published paper's quantitative content depends on an
   untested conjecture. Different in kind from every other debt here. *NGS §8.1.*
2. **Formalise ι.** Five dependents, two failed measurements. Either find a third
   attack design or write P6 as an honest unresolved fork.
3. **State C1 and C2 as framework conditions.** Small work; without them the Sybil
   bounds are conditional on unstated conventions. And the sharper question behind
   it: *which other implicit conventions are load-bearing?*
4. **Which recoverability model** — linear or compounding. They diverge 2× at K = 8.
5. **Can measurement supply content without an oracle?** Decides whether autopoietic
   closure is escapable at all. *ACF §8.2.*
6. **Exhibit a Combination Proof as an open game.** *Coutility §7.1.*
7. **Make h precise.** Without it *Requisite Richness* §§3–4 are analogy.
8. **Is an unstructured delay function possible?** Otherwise both most-exposed
   components re-base onto structure. *Borrowed Again §7.2.*
9. **The build.** Gauge-Fixing §5 still has no respondent.
10. **The security proof.** Shrunk by the Sybil fragment, not closed.

---

## 7. Honest summary

The program is in much better condition than it was this morning, and its claims are
smaller and more conditional.

It gained its first theorems, its first refutations, its first adversarial
experiment, its first two measured parameters with numbers attached, a fifth volume,
and eight papers. It also discovered that its central independence assumption
resists measurement; that one of its published test suites was right for a reason
nobody had stated; that a correction in its whitepaper had never worked; that a
structure it thought novel had a fifteen-year literature; that its neatest claim
about the post-quantum migration was empirically wrong; and that a result it
established in the morning did not survive being tested against the functional the
mechanism actually uses.

Nothing is built. The security proof is not closed. And the substrate the program
most wants remains the least verifiable — though the inward axis has now done four
separate jobs, and may turn out to be the only form of structural coupling the
program can have.
