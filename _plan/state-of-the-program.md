# State of the program — 2026-09-07

Working document. Not published to the site. Written to be read cold, by someone
who wants to know what is actually established.

Supersedes the 2026-08-06 version, which was written before the exclusion was
proved. Three of its open problems are answered, one of them in a direction that
makes the program's only theorems weaker than they were, and its central question
has been replaced.

---

## 1. Shape

**Twenty-four documents, orders 1–24, all published. Five papers added since the
last journal, thirteen revisions.** Sixteen code modules. Thirty-five archived
versions, four of which never went live. Orders 23 and 24 were drafted after this
journal was written and are folded in below where they move a grade.

| | |
|---|---|
| **Anthology** | Vol I → Vol II ×3 (*Preservation*, *Omnium*, *Kar-Coin* v0.3) → Vol III → Vol IV *Borrowed Hardness* v0.3 → Vol V *What Cannot Be Helped* v0.2 |
| **Framework** | *Combination Proofs* **v0.6** |
| **Whitepaper** | *Proof of Coherence* v0.5 |
| **Papers** | *Gauge-Fixing* v0.3, *Gluing the Gates* v0.3, *The Multiplicity Freedom* v0.5, *No Global Section* v0.3, *Requisite Richness* v0.2, *Sign and Work* v0.3, *A Consistent Fiction* v0.2, *Coutility* v0.2, *Borrowed Again* v0.1, ***Independent and Expensive* v0.3**, ***The Second Pool* v0.3**, ***One's Own Anchor* v0.2**, ***The Budget Across Levels* v0.1**, ***The Obstruction, Computed* v0.2** |

The three new papers are one line, the **exclusion line**, and each answered the
open problem the previous one closed on. Order 20 proved that within one substrate
no projection pair is both independent and expensive. Order 21 bought the pair
anyway, with a second anchor, and found the purchased projection evidences nothing
but its receipt. Order 22 said what evidencing is, proved that every reading the
corpus had built does none, and built the one reading that does — which on the
program's own specimen prices a coalition by a boundary of at most four edges.

*Combination Proofs* was revised twice in one day, both times because a claim
moved: Prop 4.2(ii) (publicity-positivity saturates at the pool) and Def 2.6 (a
projection must be independent of its own anchor). A register pass on 08-10
converted forty-seven reader-directed questions to four, across the index and
six volume documents, and changed no claim.

Four working documents, none published: `_plan/ruliad.md`, `_plan/gallery.md`,
`_plan/research-program.md` (P0–P17, next entry P18), `_plan/service-reframe.md`
(S1/S2, untouched since it was opened).

---

## 2. What is established, graded

### Proved

**The Sybil bounds** (*Multiplicity Freedom* §§4–6). Unchanged as theorems.
Conditional, as before, on C1, C2 and on τ < 1. **New this period: the cap they
bound is per identity, and on a modular substrate the per-identity cost is not a
constant** — see Measured, and §7.

**The trace-gap ceilings** (*Sign and Work* §5). Prop 5.1 a proof; Prop 5.2
conditional on its cost model, which three papers have now declined and which the
reconciliation share of *The Second Pool* §6 rests on directly.

**The exclusion** (*Independent and Expensive* §3, `exclusion.py`). In the
paid/free model, τ is the size of a projection's claim on the paid pool and ι is
the disjointness of two claims. Theorem 3.3: τ₁ + ι(2|1)·τ₂ ≤ 1, equality when the
claims exhaust the pool. Theorem 3.4: Γ ≤ W at any K — **richness partitions the
budget; nothing multiplies it.** Proof of work is the escape, not a counterexample:
its search is a second pool, i.e. an anchor. A Combination Proof of order K is K
anchors wearing readings. Cor 3.6: *Combination Proofs* Prop 4.2(ii)'s strict
publicity-positivity saturates at the unclaimed remainder. Inclusion–exclusion on
sets; the model is declared a simplification and its predictions held to three
decimals on the sheaf.

**The temporal gauge** (*The Second Pool* §3). Under induced restriction maps the
sheaf Laplacian is L_graph ⊗ I in the frame gauge, so an eigenspace-overlap
persistence reading measures the *uniformity* of frame motion (Prop 3.1), and
uniform motion is a time-dependent global gauge (Cor 3.2). Coherent change and no
change are one orbit. This closes *Proof of Coherence* §4.5's "score coherent
change" requirement in the negative for the whole class, and derives the 9.135
the previous journal reported as a surprise.

**The two-layer gluing condition** (*The Second Pool* Prop 5.3). The priced
temporal reading glues iff D_v = R_v(t)·T_v·R_v(t+1)ᵀ coincides at every vertex —
a gluing condition, not a value read, so *Gauge-Fixing* test (iv) holds by
construction. Prop 5.4: the chain leaks the beacon — a follower transporting last
epoch's frame carries this epoch's beacon value unpaid — so both gates must check
receipt and value, and the two anchors are independent as receipts, not as values.

**Evidencing** (*One's Own Anchor* §3, `evidencing.py`). Split paid work into
anchor work A and native work N; let π_A be the receipt check. A projection's
native share — its marginal fake-cost for a forger holding every receipt, over the
budget — is exactly **τ_N(π) = ι(π|π_A)·τ(π)** (Prop 3.2). Evidencing is
independence from one's own anchor. The idle projection is ι(π|π_A) = 0. No third
condition on projections; Def 2.6 amended (Cor 3.3). **Theorem 3.4: every
declared-frame reading has native share zero**, for any function of the declared
objects, because the honest configuration in that class costs exactly the anchor.
Cor 3.5: a Combination Proof of such readings is its anchors, Γ = |A|. This is the
through-line "the gap is bought entirely by the anchors" promoted from a
measurement to a property of the class.

**The coalition's evidencing share** (*One's Own Anchor* Prop 6.2). Above the
commitment step, the cheapest passing strategy derives the boundary edges' prompts
and fabricates the interior, so e(C) = |∂C| / (2|E(C)| + |∂C|) (edge-local
prompts) or 1/|C| (shared prompts). Zero deviation on the specimen.

**The budget across levels** (*The Budget Across Levels* §§3–4, `holarchy.py`).
Receipts are disjoint per level and sum; interfaces nest, so a holarchy's native
budget is its finest level's and ι(Π_ℓ|Π₀) is the level's receipt share (Props
3.1–3.3, zero deviation on the attacker). A level-j block's boundary lies entirely
above its level and halves per level as a double-counting identity (Prop 4.1).
The sum-or-minimum question was asked of the wrong pool.

### Measured

| finding | value |
|---|---|
| τ(persist) under the beacon-keyed anchor, En = 1, 4, 16, 64 | **0.187 / 0.479 / 0.786 / 0.936**, Prop 5.2's share to three decimals |
| ι(ker \| persist) under the same anchor, every En > 0 | **1.000 → 0.000** — the dial that buys τ spends ι |
| stasis under the anchor, overlap reading | **9.135× honest**, excluded by admissibility not price |
| honest excess over the best anchor-only strategy, paired, ten seeds | **−0.046**, range −0.099 to +0.055, one seed positive |
| honest with the beacon pinned, drift kept | 0.925 — the anchor removes 88% of the drift signal |
| network rotating identically, overlap reading | **1.000** = stasis (the temporal gauge, on a control) |
| two-pool sheaf, ι both ways, every (En, E_t) > 0 | **1.000** |
| two-pool τ sum, diagonal 1 / 4 / 16 | 1 − reconciliation share; share **0.699 / 0.367 / 0.127** |
| frozen participant with a paid chain, overlap reading | 9.13× honest, **admissible** — the cult with a receipt |
| the same, gluing reading | refused, λ_min 0.183 against 0.05 |
| Procrustes fit under rerandomised frames | residuals unchanged to 6e-16 — the anchor is invisible to it |
| coalition boundary residual, public overlaps, shared prompts, b = 128 | **0.145 against honest 0.203** — below honest at every size; zero edge-local |
| commitment step δ*, measured vs predicted | 1.50 vs 1.58 (edge-local), 1.75 vs 1.87 (shared) |
| block-coalition boundary edges at \|C\| = 16 / 32 / 64 / 128 | **3 / 2 / 3 / 2** (contiguous ranges: 15–20) |
| native cost per identity, block coalition, 16 → 128 | **12 → 1**, against 186 for an honest vertex |
| specimen's spectral gap λ₂ | **0.0038**; Cheeger bound on a 128-block 0.12 edges against a realised 2 |
| rotational innovation of the world | free at any rate — the measured map's own temporal gauge |
| level-by-level overcount of the native budget, Σ\|I_ℓ\|/\|E\| | **2.30** |
| conjunction over levels vs every-edge gate, derivations per epoch | **3 / 2 / 3 / 2 both** — the sum is the every-edge gate |
| adversary picks a level, derivations | **0** at every coalition size |
| per-level mean gate, blocks of 64 and 128 | 0.86 / 1.43 against the arithmetic's 1 / 2; nothing below 64 |
| interior residual: naive fiction / honest / mimic at cost 0 | **0.000** / 0.203 / **0.199** — both sides controlled is not a residual |
| Čech obstruction, answer key (Bell / Hardy / PR / affine cycle) | 0 / **0 of 1** / 8 of 8 / 9 of 9 obstructed — the literature's miss reproduced |
| logically contextual gate models invisible at every section | **97 of 233** (42%); section rates 0.714 / 0.604 |
| strongly contextual gate models seen / seen at every section | 9 of 9 / 0.878 and 0.750 of sections |
| ℤ against ℚ obstruction, 31,056 sections | **never differ** — Cor 6.4, ring-independence on cycles |
| undirected reachability = obstruction vanishes; directed = extends | **31,056 of 31,056**, both |
| layers with no tolerance gate in the chain / misses there | 540 / **0**; with one: 510 layers / **0** obstructed |

Every number reproduced from a designed specimen first: the escape specimen and
five siblings at zero deviation (order 20), a three-pool miniature plus seven
sheaf facts (order 21), four native-share specimens and a frame-invariance check
(order 22). The instruments share seeds and reproduce each other's published
numbers, which is how the one error that mattered was caught (§4, correction 13).

### Refuted

**That any projection pair on one substrate clears ι and τ together.** Theorem.
Open problem 4 of the last journal, closed the way it said a negative answer would
close it — except that the bound is on *pools*, not on K, and a pool can be added.

**That a temporal reading of the induced class carries a signal surviving its
anchor.** *Independent and Expensive* §8.4, answered for the class by the gauge
argument and by ten paired seeds.

**That the framework needs a third condition.** *The Second Pool* §9.5 asked
whether *evidencing* is a condition beyond independent and expensive. It is
independence, demanded against the anchor rather than the other projections.

**That the Sybil cap caps a modular substrate.** *One's Own Anchor* §6. Theorem
5.1 of *The Multiplicity Freedom* bounds the fleet by resource over per-identity
cost; per-identity cost on a block coalition falls as 1/|C| because the boundary
does not grow. The fleet grows with the coalition. This is the period's worst
result and it is measured, not argued.

**That the specimen meets *Gauge-Fixing* §2's design target.** "Maximise the
spectral gap" was the whitepaper's one quantitative claim about the gluing layer.
λ₂ = 0.0038; the cheapest coalition of any size has at most four boundary edges.
*Requisite Richness* chose this family for its low spectral dimension. The target
stands; the specimen fails it; *Gauge-Fixing* v0.3 now says so, and records tests
(iii) and (iv) of its own suite.

**Two candidate novelties, refused before drafting.** The transition anchor is a
proof of sequential work with a public beacon (Mahmoody–Moran–Vadhan, Cohen–Pietrzak,
Ateniese et al., Chia). The measured-map reading is Singer–Wu's connection
Laplacian. Both cited, neither claimed. Third and fourth times the prior-art rule
has caught the program.

### Conjectured, untested, load-bearing

- ~~**Conjecture 3.1** (*No Global Section*).~~ **Computed, the same day** — *The
  Obstruction, Computed* v0.1. It holds in the form stated; no distribution is
  chosen; gate models carry two grades, not three; the invariant sees every strong
  model and misses two in five logical ones at every section. Then, v0.2 the same
  day: **on a cyclic cover the obstruction is undirected reachability in the
  bundle diagram** (Theorem 6.3, a flow argument, ring-independent — which is why
  ℤ = ℚ), extension is directed reachability, and a miss needs a tolerance gate
  in the chain. Four journals at the top of the list, one afternoon to compute —
  the ranking was right and the delay was not.
- **Claim 4.3** (*Gluing the Gates*), **Prop 3.1** (*Requisite Richness*), **Claim
  3.1** (*Coutility*). Unchanged.
- **Prop 5.2's cost model** (*Sign and Work*). No longer merely declined — the
  reconciliation share, measured at two thirds of the honest budget at the low
  corner, is that model's number. If reconciliation is double-counted, the share
  shrinks and the τ sum rises.
- **Conjecture R** (`_plan/ruliad.md`). **Eight confirmations**, and since order
  20 a candidate mechanism: formalism changes replace readings, readings cannot
  create paid degrees of freedom, so a refutation would have to add paid work —
  which is what an anchor does. Still no paper selected to try.

### The ι question, restated

The last journal doubted ι was a scalar, on three data points spread across
attack intensity. *Independent and Expensive* §5 gives the account: the spread was
at the **free corner**, where the projection's claim is empty, τ = 0, and ι is a
ratio of vanishing costs whose value is the attacker's choice. The infimum reading
*Multiplicity Freedom* v0.4 recommended is the correct treatment of that
degeneracy, not a repair. Away from the corner the two operationalisations agree
and ι returns 1.000 or 0.000 exactly on every specimen built since. **ι is a
scalar where it is defined**, and where it is not defined the projection has no
gap to be independent about.

What the period added instead is a second job for ι. Evidencing is ι(π|π_A) —
the same quantity, pointed at the reading's own anchor rather than at its fellows.
P6 now formalises one quantity with two uses, under four constraints: degenerate
where claims vanish; asymmetric; reduce to claim-disjointness in the set model;
and, against the anchor, coincide with the native share when multiplied by τ.

---

## 3. The conditions that look like hygiene

C1 (participation), C2 (tolerance below the gap) and C3 (no anchor as a
certificate of order) stand as before, unstated as framework conditions. Two
were added this period, and for the first time each was **priced on the day it
was stated**:

- **C4 — every gate checks receipt and value.** *The Second Pool* Prop 5.4. A
  value-only static gate is cleared by the chain, which transports the beacon
  for nothing; the instrument returned a conjunction cheaper than one of its
  conjuncts, and that impossibility was the tell.
- **C5 — commit before compare.** *One's Own Anchor* §5. Where overlaps are
  public before commitment, a coalition copies its neighbours' data and their
  noise with it, and its boundary residual is *below* honest's at every size: the
  boundary is a subsidy. Commitment inverts the sign. Waggoner and Chen had the
  qualitative half in 2014.

C4 and C5 are the same discovery as C1–C3 — a convention that turns out to carry
the security — made in the other order. The question behind all five, *which
stated conventions are load-bearing and unpriced*, still has no audit. What
changed is that the program now knows how to price one at birth: build the
strategy that exploits its absence and watch the instrument return an absurdity.

---

## 4. Self-corrections

Eleven from the previous journals, plus eight.

12. **Naive survival was +1.131.** Measured against the *weakest* anchor-only
    strategy. Against the best, paired, it is −0.046. The supremum-over-attackers
    rule *Multiplicity Freedom* v0.4 adopted for ι applies to every baseline, and
    the wrong number is printed beside the right one in the paper so the trap is
    on record.
13. **Honest's free parts were drawn twice**, returning 0.1229 for a quantity
    `exclusion.py` had published as 0.1391. Nothing else flagged it. Reproducing a
    *published* number before trusting a new one is now the rule, alongside the
    calibration object.
14. **The beacon-leak check tested epoch 0**, where the follower starts from a
    random frame, and reported no leak. The leak is at every t ≥ 1.
15. **A value-only static gate let the chain pay for the kernel**: f_ker fell to
    n·En and ι(ker|persist) to 1/8. Caught because a conjunction came out cheaper
    than a conjunct. Origin of C4.
16. **Unpaired survival was +0.14**; paired on the same free parts, −0.046. An
    effect the size of a draw must be measured on the same draw.
17. **The commit regime scored epoch 0**, where the coalition's public copy is
    exact by construction. Scored from epoch 1.
18. **A per-epoch normalisation divided eight epochs' work by seven epochs'
    cost.** Arithmetic; caught on reading the table.
19. **An edge-count gate could not see a four-edge boundary in 371.** The
    coalition passed at the network level with a residual it would have failed on
    every one of its boundary edges. Gate every edge; the network-level number is
    an average and averages are where coalitions hide.

**Five of eight were caught by an impossible number** (12, 13, 15, 18, 19), and
13 is a new kind: not an absurdity but a *disagreement with a prior instrument*,
on a quantity both compute. The corpus now has enough instruments that they can
check each other, and that check found the one error the absurdity flags missed.

**Corrections 12 and 16 are the same error twice**, on the same quantity, in one
afternoon: a baseline chosen or a pairing omitted so that the honest strategy
looked better than it was. Both times the instrument was returning what the
operator hoped for. This is the fourth journal in a row to record that pattern.

---

## 5. Through-lines

### Formalisms relocate difficulties; they do not dissolve them

Eight instances, and now a mechanism (order 20 §6). The two-layer sheaf relocated
the difficulty by exactly one receipt; the measured map relocated it from the
anchor to the public record and the world's innovation rate. The refutation, if
there is one, has to add paid work.

### The substrate keeps doing the work the mechanism was credited with

**Now a theorem for the class** (*One's Own Anchor* Thm 3.4). Every reading of
declared frames, maps or Laplacians has native share zero; a Combination Proof of
them is its anchors. The sheaf, the gluing and the cohomology supply no forgery
resistance because the honest configuration costs exactly what the anchor costs.
This is the through-line's terminal form for the induced class, and it is where
the line stops being uncomfortable and starts being useful: it says exactly which
readings not to build.

### What survives is information, not work

New, and the period's largest shift. The one reading with a native share — maps
fitted at overlaps, gated on every edge's residual — evidences the world's
innovation since the last public record. Not effort. Native work is priced only
because derivation is the model's sole channel to that innovation; a coalition
that could predict the world from outside would pay nothing. The commitment step
restates *Sign and Work*'s rule that satisfying a public constraint is never work,
with the world as the constraint. The program's titles say *work*; its surviving
instrument measures *contact*. Bara stated the criterion information-theoretically
five days before order 22, independently; the sheaf-valued form, the theorem, the
accounting and the measurements are the corpus's.

### The boundary is the whole of the price

New. The evidencing share of a coalition is its boundary's work over its total;
the boundary is SybilGuard's attack-edge count with a second face — the same cut
that bounds admission is the channel the world leaks through. On the hierarchical
specimen the boundary is at most four edges at any size, so identities inside pay
nothing and identities on the edge pay honest's rate. Richness at the coupling
knob was already paid in trace gap (*Sign and Work* §5.4); it is now also paid at
the boundary. The same bill, presented twice.

### Anchors do two jobs and only one was costed

Now three jobs. An anchor closes the fiction space (*A Consistent Fiction*),
buys a trace gap at its receipt share (*Sign and Work* Prop 5.2, *The Second
Pool*), and — the beacon — supplies most of what the reading reads. The third was
found by accident as a 9.135 and derived as a gauge. And an anchor's receipt and
its value are separable: the chain carries the beacon's value for nothing, so
what an anchor sells is the receipt.

### One distinction, now derived six times

Unchanged, and worth saying why: the exclusion line did not re-derive
sign-versus-work, it *priced* it. Paid and free degrees of freedom are that
distinction with a cost attached.

---

## 6. Open problems, ranked by leverage

1. ~~**Test Conjecture 3.1.**~~ **Done the same day** — *The Obstruction, Computed*
   v0.1–v0.2; see §2. The run-of-open-gates rule became Theorem 6.3 the same
   afternoon. Replaced by the **non-cyclic case** (TOC §9.2: conservation on a
   hypergraph) and the cost of Carù's refinement on cycles (TOC §9.1).
2. ~~**The budget across levels.**~~ **Done the same day** — *The Budget Across
   Levels* v0.1. The dichotomy was asked of the wrong pool: receipts sum and are
   idle, interfaces nest, the minimum over levels is zero on the native side and
   the conjunction is one boundary counted once. MF §8.4 answered: the criterion is
   correct and not a residual. Replaced by **beacon-assigned overlaps** (BAL §9.1):
   sharding's remedy transposed, a random cut that grows with |C|, at the cost of
   the substrate's own nesting. *I&E §8.3, Second Pool §9.3, OOA §9.3, MF §8.4.*
3. **Formalise ι**, now one quantity with two uses and four constraints (§2).
   Five dependents, and P6 remains critical path. Named again rather than
   repeated, per the plan's own instruction.
4. ~~**Revise *Gauge-Fixing* to say its target fails on the specimen.**~~ **Done** —
   v0.3, §2 amended, §5.2 records tests (iii) and (iv). Tests (i), (ii) and the
   conjunction remain (item 15).
5. **The expansion-versus-richness curve.** *OOA §9.4.* Raising λ₂ raises e(C) for
   every coalition at a richness cost already measured. The first design curve
   the residual reading makes measurable. Needs a family of complexes with
   varying gap; degree-preserving rewiring is on hand and untried for this.
6. **Attack the §5.2 cost model.** Promoted: the reconciliation share — up to two
   thirds of the honest budget — is that model's number. *S&W §7.*
7. **State C1–C5 as framework conditions**, and run the audit behind them.
8. **A world with memory.** The native share is bounded by the entropy rate of
   the world conditional on everything public. One theorem; belongs in an *OOA*
   v0.2. *OOA §9.1.*
9. **Two disciplines.** *ACF §8.5*, still untested — two anchors of one discipline
   are not the test (*Second Pool* Prop 5.4). *ACF §8.2* now has an instrument
   (*OOA §9.5*).
10. **Multi-task against commitment.** Whether peer prediction's repair and this
    paper's compose, and whether the composition prices a coalition's interior.
    *OOA §9.2.*
11. **The graded model.** Replace set-claims with a cost function; determine
    whether the partition law survives as an inequality. *I&E §8.1.*
12. **Which recoverability model**; **exhibit a Combination Proof as an open
    game**; **make h precise**. Unchanged, unmoved.
13. **Select a paper to refute Conjecture R.** Eight confirmations. The mechanism
    says what a refutation must do; nothing is scheduled to try.
14. **The deployed chain.** Bittensor's commit-reveal against a public mechanism.
    Empirical and web-dependent. *Second Pool §9.4.*
15. **The build.** *Gauge-Fixing* §5: test (iv) holds by construction in order
    21, test (iii) has its number in order 22 and the number fails. Tests (i),
    (ii) and the conjunction remain.
16. **The security proof.** Further off than at the last journal: the Sybil cap,
    its provable fragment, is now measured not to cap on a modular substrate.

---

## 7. Honest summary

The program's claims are smaller again, and this time one of its theorems has
been shown to bound the wrong thing.

It gained an exclusion principle, proved in a model and confirmed on the sheaf to
three decimals: independence and soundness are claims on one budget, and richness
partitions that budget. It made the purchase the principle permits — a second
anchor, a second pool — and found the purchased projection evidences its receipt
and nothing else. It then said what evidencing is, found the condition had been
in the framework all along pointed the wrong way, and proved that every reading
it had ever built does none of it. The through-line that the anchors buy the
whole gap is now a theorem for the class of readings the whitepaper describes.

It built the one reading outside that class, and the reading works: it has a gap
its anchor did not buy. What it evidences is information about the world since
the last public record — not work — and it evidences it on the coalition's
boundary alone. On the program's own specimen that boundary is at most four edges
at any coalition size, so the per-identity cost that the Sybil bounds divide by
falls as the inverse of the coalition, and the fleet grows with the coalition. The
corpus's only theorems still hold. What they bound, on a modular substrate, is
not the fleet.

Two conventions were found to be security conditions, and for the first time were
priced on the day they were found. Two claims to novelty were refused before
drafting. Eight errors were caught, five by impossible numbers and one by a new
route — two instruments disagreeing on a number both compute. Conjecture 3.1 has
now been the top-ranked problem through four journals and has not been touched;
that is a finding about the program, not about the conjecture.

Nothing is built. The security proof is further away than it was. The last
journal said the corpus should expect its next result to be a subtraction, and it
was — three of them, in a line, each answering the one before, and a fourth the
same day: nesting buys receipts, and receipts are idle. Then the debt at the top
of the list for four journals was paid in an afternoon, and the answer was the
corpus's usual shape: the invariant is a certificate and not a test, now with a
rate. The program's
titles say *work*. Its one surviving instrument measures contact with a world,
and what it evidences is the part of the world nobody has written down yet.
