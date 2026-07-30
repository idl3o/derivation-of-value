# State of the program — 2026-07-30

Working document. Not published to the site.

A collation after the session that added four papers, revised five, and put 1,219
lines of runnable code behind claims that had been prose. Written to be read cold,
by someone who wants to know what is actually established.

---

## 1. Shape

Fourteen documents, orders 1–14. Six code modules. Eight archived versions.

| | |
|---|---|
| **Anthology spine** | Vol I *Derivation of Value* → Vol II ×3 (*Preservation*, *Omnium*, *Kar-Coin*) → Vol III *Admitted or Refused* (open ledger) → Vol IV *Borrowed Hardness*. Complete and unchanged. |
| **Framework** | *Combination Proofs* v0.3 |
| **Whitepaper** | *Proof of Coherence* v0.3 |
| **Technical papers** | *Gauge-Fixing*, *Gluing the Gates*, *The Multiplicity Freedom* v0.2, *No Global Section*, *Requisite Richness* |

The spine did not move. Everything added is framework-level or technical — which
was the right call each time, and is worth noticing as a pattern: the essayistic
volumes name substrates, and the work that followed was all about *structure*
rather than about new things to stake.

---

## 2. What is established, graded

Grading matters more than listing. The program's ethic is that a claim which could
have been refuted and was not is worth more than one never permitted to fail, and
these are not all in the same condition.

### Proved (derivation, verified numerically)

**Sybil bounds** (*The Multiplicity Freedom* §§4–6, `sybil_bound.py`).
T1: an adversary with budget C fields at most ⌊C/Γ⌋ rewarded identities.
T2: Γ = γ(1 + (K−1)ι), so conjunction-gating amplifies the resource floor by a
factor scaling with order, and by *nothing* when projections are redundant; under
compounding recoverability the amplification saturates at 1/(1−ι).
T3: the gate caps the fleet but only convexity above it punishes splitting —
concave rewards are strictly Sybil-positive, at 2.83× for eight identities.

These are the only theorems in the program. They hold because Sybil cost is
arithmetic where fake-cost is capability-laden.

### Measured (numbers, converged, reproducible)

**ρ is a fractional spectral dimension.** d_s ≈ 1.61, converged across n = 512 →
4096 with scatter falling 0.054 → 0.007, R² ≈ 0.999, and *continuous* in coupling
density across 1.26–2.23. Integer richness is the measure-zero exception.
Pipeline calibrated against known answers first (gasket 1.365 → 1.392; lattice
2 → 2.098).

**H1 holds on coherence substrates, and no credit rule earns it.** All four
schemes satisfy duplication-boundedness at every N tested. The reason is
structural — the functional is a rank, a duplicate adds no rank.

**Griefing separates the schemes completely.** 100% loss under marginal removal
and literal provenance, 50% under Shapley, 0% under filtered provenance.

**The coherent sheaf returns the bare complex's exponent** (1.614 vs 1.607),
confirming gauge-equivalence and that d_s belongs to the substrate rather than the
apparatus.

### Refuted (predicted, tested, wrong)

**The gap-hierarchy conjecture.** Predicted that spectra of nested complexes carry
gaps at every scale, so Gauge-Fixing §5's single measured spectral gap would price
only the coarsest coalition. Gap hierarchy tracks *exact geometric* self-similarity,
not nesting: the gasket shows 18 across 5 scales, the nested complex at most one.
**The §5 test stands, vindicated by the objection it survived.**

**The spectral dimension as an independent third projection.** ι ≈ 0 at the
operating threshold against a structure-aware adversary — faking the kernel
delivers d_s for free. Proposed, tested, withdrawn. The cheap route to a
higher-order Combination Proof is closed.

### Conjectured (stated, untested, load-bearing)

**Conjecture 3.1** (*No Global Section*): the presheaf-of-distributions
construction transfers to gate scenarios, giving an obstruction without the affine
hypothesis. The quantitative content of that paper rests on it.

**Claim 4.3** (*Gluing the Gates*): the cohomological obstruction under affine
gates — with the imported caveat that it detects failure and does not certify
safety.

**Proposition 3.1** (*Requisite Richness*): ρ·h ≥ H(D), conditional on a
per-projection variety bound h that is not established. Without h it is analogy.

### Inconclusive (attempted, failed, recorded)

**Is ι symmetric?** Two attack designs failed — sparsification shatters the complex
and contaminates the kernel proxy with component count; degree-preserving rewiring
stays connected but moves d_s only 8% of the way. ι(dim|ker) = 0.08 is solid;
ι(ker|dim) is unmeasured. The metric-vs-divergence fork is open, and it is on the
critical path.

---

## 3. Six self-corrections

The most instructive output of the session is not any result. It is that six
claims were caught wrong before publication, and how.

1. **Degenerate eigenvalues counterfeit a gap hierarchy.** Local spacing collapses
   inside a degenerate block, so any adjacent gap scores enormous. Inflated the
   gasket to 74 spurious gaps and the coherent sheaf to 67 — the latter being
   *exactly* its 3-fold stalk multiplicity, i.e. the apparatus reporting itself as
   a property of the substrate.
2. **Disconnection counterfeits kernel progress.** Sparsification produced "kernel
   progress" of 6.6 and 13.6 — above the honest value, which is impossible. It was
   measuring shattering.
3. **§4.2's provenance formula does not work.** r × p leaves M₁ at zero, because
   marginal removal has already zeroed r. 0 × 1 = 0.
4. **H1 was mis-stated.** Written about individual earnings; the theorem needs
   group totals. Not equivalent — Shapley violates the first and satisfies the
   second.
5. **The affine-gate hypothesis is violated by the program's own worked instance.**
   A threshold on a spectral quantity is not affine.
6. **Gluing the Gates claimed as novel a structure that is contextuality**, in
   Abramsky and Brandenburger's exact sense. Caught by a prior-art check run after
   the draft, and now a checklist item to run *before*.

Four of the six were caught by the instrument contradicting itself — a number that
was impossible rather than merely surprising. That is an argument for building the
measurement even when the claim seems safe, and for preferring diagnostics that can
return absurdities over ones that always return something plausible.

---

## 4. Through-lines

### Everything points at ι

The multiplication claim depends on it. Richness-as-packing-number needs it as a
separation scale. Sybil amplification is a function of it, with a saturation
ceiling of 1/(1−ι). Composition inherits it. Four independent routes to one
quantity that has never been formalised and has now twice resisted measurement.

If the program has a single critical path, this is it, and the honest position is
that it is *harder* than it looked in the morning.

### The substrate keeps doing the work the mechanism was credited with

H1 holds because the functional is a rank, not because of any credit rule.
Richness lives in the coupling between holons, not in the holons. Harvestability
is a property of the substrate, decided before any mechanism is designed.
Sybil resistance is inherited from matroid structure.

The framework's own doctrine — *design begins with the selection of substrates* —
keeps being confirmed in ways it did not predict, and each confirmation removes
credit from the mechanism designer.

### One distinction, derived four times

The outward/inward split found in Kar-Coin turned out to be: the oracle problem
(attestation by report vs by residue), the harvestability problem (what a failed
attack leaves behind), Sybil resistance (identities minted by claim vs by
artifact), and — planned — stigmergy. Four derivations of one line. That is either
a deep structural fact or the program has one idea; the session did not settle
which, and the question deserves to be asked directly.

### Vanishing cohomology is weaker than it looks, twice

Gauge-Fixing: H¹ = 0 certifies coherence, not truth. No Global Section: H¹ = 0
does not even certify that levels compose. The pattern is now explicit —
cohomology detects the obstructions it was built to detect, and silence from it is
not evidence of absence.

### ρ became adversary-relative

Introduced as a property of the substrate alone. It now has a ceiling from the
substrate (Def 5.1), a floor from the adversary's variety (Ashby), and a role in
bounding the adversary's fleet (Sybil T2). A quantity that was intrinsic is now
squeezed on both sides by facts about the opponent.

---

## 5. Open problems, ranked by leverage

1. **Formalise ι.** Four dependents. Resists measurement. Blocks the
   information-geometry paper and the richness composition law.
2. **H1 beyond rank.** The result was measured on the rank toy. The real
   functional scores H⁰, and a duplicated stalk with consistent restriction maps
   may *add* section space. If it does, duplication is profitable under the actual
   mechanism while neutral under its simplification. **Cheap to test with existing
   machinery, and it decides whether zero-duplication is load-bearing or tidy.**
3. **Which recoverability model.** Linear and compounding diverge by a factor of
   two at K = 8, and the framework gives no ground to choose.
4. **Test Conjecture 3.1.** A computation, not a research programme, and the
   quantitative content of a published paper depends on it.
5. **Make h precise.** Without it *Requisite Richness* §§3–4 are analogy.
6. **The build.** Gauge-Fixing §5's suite still has no respondent.
7. **The security proof.** Shrunk by the Sybil fragment, not closed.

---

## 6. What I would do next

**Test H1 on the cohomological functional** (item 2). It is the cheapest item on
the list, it uses machinery that already exists, and it decides a question that is
currently load-bearing in two papers. It can also only produce a useful answer: if
duplication is neutral under H⁰ the H1 result generalises and zero-duplication is
a convenience; if it is profitable, zero-duplication becomes structural and the
Sybil paper needs a caveat it does not have.

**Then decide what ι is going to be.** Either find a third attack design, or write
the information-geometry paper as an unresolved fork — the candidate, the two
failed measurements, and the third design that would settle it. The critical path
should not stall silently while easier papers get written around it.

**Ask the four-derivations question directly.** Whether the outward/inward
distinction recurring in four guises is structure or monomania is answerable, and
the program is better off knowing. A paper that tried to *unify* the four and
failed would be more valuable than a fifth derivation.

---

## 7. Honest summary

The program is in better condition than it was, and its claims are smaller.

It gained its first theorems, its first refutations, its first adversarial
experiment, and its first discharged conditional. It also discovered that its
central independence assumption is harder to pin down than assumed, that one of
its published test suites was right for a reason nobody had stated, that a
correction in one whitepaper had never worked, and that a structure it thought was
novel had a fifteen-year literature.

Nothing is built. The security proof is not closed. The one substrate the program
most wants — civilisational capacity — remains the least verifiable, though it now
has an axis on which it might become verifiable at all.
