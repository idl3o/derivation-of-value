# State of the program — 2026-08-06

Working document. Not published to the site. Written to be read cold, by someone
who wants to know what is actually established.

Supersedes the 2026-07-30 version, which was written before the trace gap was
measured. Two of its entries move grade and one of its open problems is answered
in the negative.

---

## 1. Shape

**Nineteen documents, orders 1–19, all published.** Ten code modules, ~1,900 lines
plus `trace_gap.py`. Fourteen archived versions, four of which never went live.

| | |
|---|---|
| **Anthology** | Vol I *Derivation of Value* → Vol II ×3 (*Preservation*, *Omnium*, *Kar-Coin*) → Vol III *Admitted or Refused* (open ledger) → Vol IV *Borrowed Hardness* → Vol V *What Cannot Be Helped* |
| **Framework** | *Combination Proofs* v0.3 |
| **Whitepaper** | *Proof of Coherence* v0.4 |
| **Papers** | *Gauge-Fixing* **v0.2**, *Gluing the Gates*, *The Multiplicity Freedom* v0.3, *No Global Section*, *Requisite Richness*, *Sign and Work* **v0.3**, *A Consistent Fiction*, *Coutility*, *Borrowed Again* |

Two working documents opened and not published: `_plan/ruliad.md` (the corpus as a
rule-space indexed by imported formalism) and `_plan/gallery.md` (a cabinet of
outside specimens, explicitly below its own publication bar).

---

## 2. What is established, graded

### Proved

**The Sybil bounds** (*Multiplicity Freedom* §§4–6, `sybil_bound.py`). T1: an
adversary fields at most ⌊C/Γ⌋ rewarded identities. T2: Γ = γ(1 + (K−1)ι), so
richness bounds Sybil and Goodhart resistance alike, and buys nothing at ι = 0. T3:
the gate caps the fleet, but only convexity above it punishes splitting — concave
rewards are Sybil-*positive* at 2.83× for eight identities. Conditional on C1 and C2
(§3), **and now on τ, which §2's new results say is always below 1 for a coherence
reading** — so the quantitative content is scaled by a factor the framework cannot
set to 1.

**Equilibrium ≠ admissibility** (*Coutility* Prop 4.1).

**The trace-gap ceilings** (*Sign and Work* v0.3 §5, `trace_gap.py`). Prop 5.1: under
output anchors τ ≤ 1 − b₁/|E|, equality only where the score is vacuous. Prop 5.2:
under generative anchors τ = nE/(nE + |E|c) < 1 strictly. Prop 5.1 is a proof; Prop
5.2 is a proof *conditional on its cost model*, which §5 of that paper declines
explicitly and which is the first place to attack.

### Measured

| finding | value |
|---|---|
| ρ as fractional spectral dimension | d_s ≈ 1.61, converged n = 512→4096, R² ≈ 0.999, continuous in coupling 1.26–2.23 |
| fiction space of a coherent sheaf | **exactly d** |
| structural coupling to close it | **d scalars, at one vertex, once**, and d per *component* |
| H1 on the rank functional | holds under every credit rule |
| H1 on H⁰ | **fails** — scattered duplicates add d each |
| griefing spread across credit rules | 100% / 50% / 0% |
| trace gap τ, unconstrained H⁰ | **≈ 0** |
| **τ calibration, proof of work** | **1.054** against a known 1 (400 trials) |
| **τ ceiling, output anchors** | **1 − b₁/\|E\|**, exact across five cycle ranks |
| **τ, generative anchors, by rank** | **0, then 0.4874 flat for every rank ≥ 1** |
| **τ ceiling against coupling** | **1.000 → 0.315** as d_s rises 1.255 → 2.281 |
| price of derived hardness | SLH-DSA 7,856–49,856 B vs ML-DSA 2,420–4,595 |

### Refuted

**The gap-hierarchy conjecture.** Tracks geometric self-similarity, not nesting.
*Gauge-Fixing* §5's spectral-gap test stands, vindicated by the objection it survived.

**Spectral dimension as an independent third projection.** ι ≈ 0 against a
structure-aware adversary.

**That H1 generalises from rank to H⁰.**

**That τ ≥ 1 is attainable by a coherence reading.** *Sign and Work* v0.2 §7.2 asked
whether τ ≥ 1 is attainable or only approachable. For this class of reading the
answer is **only approachable**, by two unrelated routes, and the shortfall in each
case is exactly the coherence content. Proposed, tested, answered against.

### Conjectured, untested, load-bearing

- **Conjecture 3.1** (*No Global Section*): the distributional presheaf transfers to
  gate scenarios. **A published paper's quantitative content rests on this.** Still
  the highest-leverage item and untouched this session.
- **Claim 4.3** (*Gluing the Gates*): cohomological obstruction under affine gates.
- **Prop 3.1** (*Requisite Richness*): ρ·h ≥ H(D), conditional on an h that does not
  exist yet.
- **Claim 3.1** (*Coutility*): coutility propagates a gate.
- **Conjecture R** (`_plan/ruliad.md`): the attestation problem is invariant under
  change of formalism. Six confirmations, no adversary, and no paper is selected to
  break it.

### Inconclusive

**Is ι symmetric?** Unchanged from 2026-07-30. Two attack designs failed.
ι(dim\|ker) = 0.08 is solid; ι(ker\|dim) is unmeasured. **On the critical path and
unresolved, for the second consecutive session.** See §6.

---

## 3. The conditions that look like hygiene

Now three, and the third is the transferable one because it was *written down*.

- **C1 — participation.** Every scored vertex must be connected to the honest
  complex. A modelling convention in §3.1's construction, which is why it went
  unnoticed.
- **C2 — kernel tolerance below the spectral gap.** The score is always #{λ < ε},
  never dim ker. The same quantity §5's test suite already demands.
- **C3 — no anchor may be cited as a certificate of order.** *Gauge-Fixing* §4.4,
  stated in v0.1 as taste, and shown in v0.2 §5.1 to be a security condition: an
  anchor read as an order certificate is an *output* constraint, and satisfying a
  public constraint is constraint satisfaction rather than work, so no arrangement of
  such anchors reaches a sound trace gap.

C1 and C2 were unstated conventions discovered late. **C3 was stated, published, and
never costed** — which is a different and worse failure, because the corpus had the
rule in hand and did not know what it was buying. The general question, now with
three data points: *which other stated conventions are load-bearing in ways nobody
has priced?*

---

## 4. Self-corrections

Seven from the previous session, plus one.

1. Degenerate eigenvalues counterfeit a gap hierarchy.
2. Disconnection counterfeits kernel progress.
3. §4.2's provenance formula never worked.
4. H1 was stated about individual earnings; the theorem needs group totals.
5. The affine-gate hypothesis is violated by the program's own worked instance.
6. *Gluing the Gates* claimed as novel a structure that is contextuality.
7. Five vectors reported as spanning five dimensions inside a 3-D kernel.
8. **The τ calibration returned 2.74 on proof of work, whose answer is 1** — the
   attacker's cost measured on a single search against an honest mean over eight,
   where search length is geometric with standard deviation equal to its mean.

**Five of eight were caught because an instrument returned an *impossible* number.**
Correction 8 is the cleanest instance yet and the only one caught by a calibration
object placed there deliberately for the purpose. The lesson is now stronger than
"prefer diagnostics that can return absurdities": **build the specimen whose answer
you already know, and point the instrument at it first.** Without it, the same
estimator would have produced every trace-gap number with nothing to flag.

---

## 5. Through-lines

### Formalisms relocate difficulties; they do not dissolve them

Six instances. `_plan/ruliad.md` restates it as **Conjecture R** — falsifiable, six
confirmations, and no paper in the plan is selected to refute it. Selecting one is
the cheapest unexplored move in the program.

### The substrate keeps doing the work the mechanism was credited with

Sharpened considerably. The trace gap is now measured to be bought **entirely by the
anchors**, with the coherence layer contributing only to the denominator. The
mechanism's characteristic machinery — the sheaf, the gluing, the cohomology — turns
out to supply no forgery resistance at all. This is the strongest form the
through-line has taken and the least comfortable.

### One distinction, now derived six times

Unchanged. Vol V named it and found it was negentropy-with-provenance.

### Everything still points at ι

Five dependents, no formalisation, two failed measurements, and **a second session in
which the critical path did not move.** The previous state doc recorded this as a
thing not to repeat. It repeated. The τ work has independent standing through Prop
4.1 and was not avoidance in intent, but the outcome is the same and is recorded as
such.

### Anchors do two jobs and only one was costed

New. *A Consistent Fiction* prices structural coupling at d scalars at one vertex,
once, and that closes the fiction space. It opens **no trace gap whatever** — one
anchor is absorbed by gauge invariance rather than spent. Closing the space of
consistent fictions and making a trace expensive to forge are different purchases at
different prices, and the corpus had costed only the first.

---

## 6. Open problems, ranked by leverage

1. **Test Conjecture 3.1.** A published paper's quantitative content depends on an
   untested conjecture. Unchanged at the top, and untouched for two sessions. *NGS §8.1.*
2. **Formalise ι.** Five dependents, two failed measurements. The route named by
   `code/README.md` — that independence lives in temporal autocorrelations and
   "nothing short of building them will do" — has not been built. **Next.**
3. **Is any coherence reading's gap not bought by its anchor?** *S&W §8.1.* A reading
   scoring cycle agreement directly, with restriction maps measured at overlaps
   rather than induced by declared frames, is the one place a better gap could hide.
   If it does not hide there, coherence-based attestation is bounded in a way the
   framework has not admitted.
4. **State C1, C2 and C3 as framework conditions**, and answer the question behind
   them: which other stated conventions are load-bearing and unpriced.
5. **Attack the §5.2 cost model.** Prop 5.2 assumes reconciliation is work *on top of*
   producing sections. At full rank that is arguable; if double-counted, τ rises and
   the strict inequality weakens. Cheap, and it bears on a just-published result.
6. **Which recoverability model** — linear or compounding. They diverge 2× at K = 8.
7. **Can measurement supply content without an oracle?** *ACF §8.2.*
8. **Exhibit a Combination Proof as an open game.** *Coutility §7.1.*
9. **Make h precise.** Without it *Requisite Richness* §§3–4 are analogy — and it now
   has a ceiling as well as a floor to be commensurable with.
10. **Select a paper to refute Conjecture R.** *`_plan/ruliad.md` §7.*
11. **The build.** *Gauge-Fixing* §5 now has one respondent on one fragment of one
    item. Tests (ii), (iii), (iv) and the conjunction remain.
12. **The security proof.** Shrunk by the Sybil fragment, not closed.

---

## 7. Honest summary

The program's claims are again smaller and more conditional, and one of its central
constructions is worse off than it was a week ago.

It gained an instrument with a calibration object, two ceiling results reached by
unrelated routes, the first respondent to a test suite that had gone eleven months
without one, and a third instance of a convention that looked like hygiene and was
structural — the first of the three that had been written down and simply never
costed. It also established that the coherence layer contributes nothing to forgery
resistance; that Volume V's soundness clause is unattainable rather than merely unmet
for a coherence reading; that richness is paid for in trace gap, so the two quantities
the framework wants to maximise are in direct tension; and that the anchor purchase
*A Consistent Fiction* priced closes the fiction space while buying no trace gap at
all.

The Sybil bounds, the program's only theorems, are now conditional on three unstated
or unpriced conditions and on a τ that cannot reach 1.

Nothing is built. The security proof is not closed. ι did not move for a second
session, and the plan has now recorded that failure twice, which is one more time than
recording it is worth if it happens again.
