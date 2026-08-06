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
| **Framework** | *Combination Proofs* **v0.4** |
| **Whitepaper** | *Proof of Coherence* v0.4 |
| **Papers** | *Gauge-Fixing* **v0.2**, *Gluing the Gates*, *The Multiplicity Freedom* **v0.4**, *No Global Section*, *Requisite Richness*, *Sign and Work* **v0.3**, *A Consistent Fiction*, *Coutility*, *Borrowed Again* |

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

### Inconclusive — but ι moved

**The third attack design succeeded.** `temporal_iota.py` builds the epochs
`independence.py` said would be required, rather than attacking the snapshot harder,
and both attacks move their own target while leaving the other alone — which neither
sparsification nor rewiring managed.

| | |
|---|---|
| ι(dim \| ker), static | ≈ 0.08 (unchanged) |
| **ι(ker \| persist), temporal** | **1.000, at every coalition size** |
| ι(persist \| ker) | 0.723 mean — but 0.28 / 0.86 / 1.03 across intensity |
| asymmetry | **0.277**, above the 0.15 threshold |

**Is ι symmetric? On this pair, no** — so the right object is a **divergence, not a
metric**, and P6's Fisher route must carry the asymmetry rather than quotient it.

**Is ι even a scalar? Now doubtful.** ι(persist \| ker) spreads three quarters across
attack intensity. CP §7.1 types it as a function of substrate and projection pair; on
this evidence it is also a function of the attack that measures it, which would leave
Γ = γ(1 + (K−1)ι) undefined until an adversary is named. Three points with a monotone
trend — suggestive, not established. The conservative repair, now recommended in
*Multiplicity Freedom* v0.4: read ι as an **infimum over the attacker class**.

**And the finding that reorders the problem: independence was never the binding
constraint.** π_persist is maximally independent *and* free to forge — a coalition
that never changes its restriction maps outscores honest participants who update
theirs, by a factor of five. τ(π_persist) ≈ 0, so by *Sign and Work* Prop 4.1 it
inflates the fleet without bound and contributes nothing to the Sybil cap. **CP §7.1
has stated one of two requirements on a projection for the whole life of the
framework.** *Multiplicity Freedom* v0.4 Cor 5.4 records the consequence: there are
two ways for richness to buy nothing — redundancy and forgeability — and only the
first was named.

**Conjectured, on two data points and therefore weak: ι and τ pull against each
other.** A projection independent of coherence is one coherence does not constrain,
and one coherence does not constrain is one an adversary satisfies without coherence
work. The static spectral projection failed on ι and inherited coherence's τ; the
temporal projection passes ι and has no τ. Third such tension found this session,
after ρ/τ.

**Still unresolved:** ι has no formalisation, and the multiplication claim still rests
on it. What changed is that the quantity now has a measured direction, an established
asymmetry, a reason to doubt its type, and an argument that it was the wrong thing to
optimise alone.

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

### ι moved, and pointed somewhere else

Two sessions of ι sitting still ended with the third attack design. The result is not
the formalisation — that is still absent — but a reordering: **the framework had been
optimising one of two requirements.** A projection must be independent *and* expensive
to forge, ι and τ appear to trade off, and the program's hardest open problem may have
been the more tractable of the pair all along. The τ work of this session, which
looked like writing around the critical path, turned out to supply the instrument that
made the ι result legible. That is luck rather than method, and is recorded as luck.

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
2. **Is ι a scalar?** Promoted above "formalise ι", because it is prior to it: a
   formalisation of a quantity that varies with the attack measuring it will
   formalise the wrong object. Three data points and a monotone trend. Cheap to
   settle — more intensities, more attack designs, on machinery that now exists.
3. **Formalise ι.** Five dependents. The temporal route has now been built and the
   measurement obtained, so what remains is the formalisation itself, under two new
   constraints: it must be a **divergence** rather than a metric, and it must survive
   whatever answer problem 2 returns.
4. **Find a projection clearing ι *and* τ.** The reordered form of the framework's
   central design problem, and new. Every projection the program has examined fails
   one: the static spectral one fails ι, the temporal one fails τ. Whether the two
   requirements are jointly satisfiable at all is not known, and a negative answer
   would bound Combination Proofs of order K > 1 on coherence substrates.
5. **Is any coherence reading's gap not bought by its anchor?** *S&W §8.1.* A reading
   scoring cycle agreement directly, with restriction maps measured at overlaps
   rather than induced by declared frames, is the one place a better gap could hide.
   If it does not hide there, coherence-based attestation is bounded in a way the
   framework has not admitted.
6. **State C1, C2 and C3 as framework conditions**, and answer the question behind
   them: which other stated conventions are load-bearing and unpriced.
7. **Attack the §5.2 cost model.** Prop 5.2 assumes reconciliation is work *on top of*
   producing sections. At full rank that is arguable; if double-counted, τ rises and
   the strict inequality weakens. Cheap, and it bears on a just-published result.
8. **Which recoverability model** — linear or compounding. They diverge 2× at K = 8.
9. **Can measurement supply content without an oracle?** *ACF §8.2.*
10. **Exhibit a Combination Proof as an open game.** *Coutility §7.1.*
11. **Make h precise.** Without it *Requisite Richness* §§3–4 are analogy — and it now
    has a ceiling as well as a floor to be commensurable with.
12. **Select a paper to refute Conjecture R.** *`_plan/ruliad.md` §7.*
13. **The build.** *Gauge-Fixing* §5 now has one respondent on one fragment of one
    item. Tests (ii), (iii), (iv) and the conjunction remain.
14. **The security proof.** Shrunk by the Sybil fragment, not closed.

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

It also, at the end, moved ι — after two sessions of not moving it — by building the
epochs rather than attacking the snapshot a third time. The result is not a
formalisation. It is a reordering: **a projection must be independent and expensive to
forge, the framework has been stating only the first as an open problem, and on the
evidence the two requirements pull against each other.** Every projection the program
has examined fails one of them. Whether any projection clears both is now the central
design question and has never been asked.

The Sybil bounds, the program's only theorems, are now conditional on three unstated
or unpriced conditions, on a τ that cannot reach 1, and on an ι that may not be a
constant.

Nothing is built. The security proof is not closed. What the program gained this
session is almost entirely negative results, which is the kind it has been best at
producing and the kind its discipline is built to survive — but a corpus of nineteen
documents in which the central mechanism has been shown to contribute nothing to
forgery resistance, and the central parameter shown to be measuring the less binding
of two constraints, is a corpus that should expect its next result to be a subtraction
too.
