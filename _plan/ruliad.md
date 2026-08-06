# The ruliad — 2026-08-05

Working document. Not published to the site.

A self-map of the program as a rule-space: one operator, the states it has been
applied to, where the branches rejoin, what survives every branch, and where nothing
has gone. Assembled from `state-of-the-program.md` (2026-07-30), `research-program.md`,
and the nineteen documents in `_papers/`. No new results are claimed here; the
contribution is a coordinate system, and one conjecture (§8) that the coordinate
system makes visible.

---

## 0. The metaphor tax, paid first

The program's own rule: an outside term enters as a definition doing work, or does not
enter. So, before using the word.

Wolfram's **ruliad** is the entangled limit of all possible computations — every rule,
applied to every state, for every number of steps. Taken literally this program has no
ruliad. It has *one* rule, and a rule-space of one is a multiway system, not a ruliad.

The construct earns its keep only under a substitution, and the substitution is the
useful part:

> **The rule axis is not the substrate axis. It is the formalism axis.**

The operator is fixed. What varies from document to document is the *formalism it is
executed in* — sheaf cohomology, gauge theory, contextuality, cybernetics, stigmergy,
autopoiesis, open games, post-quantum cryptography. Each import is a different rule
computing on the same state. That is a rule-space with eight or so members and a
well-defined question attached: **do they emulate each other, and what is invariant
across all of them?**

The corpus already has the answer to the second half and has not recognised it as one.
See §7.

If the substitution is rejected, this document degrades to a dependency graph with an
inflated name, and should be read that way. It would still be worth having.

---

## 1. The rule

    σ  ↦  derive(σ)

*Do not borrow the staked quantity from outside the mechanism; derive it from the
substrate the mechanism already stands on.*

Everything in the corpus is one application of this to some σ, in some formalism.

---

## 2. What a node is

A node is a pair:

    ⟨ substrate , formalism ⟩

The substrate is what gets staked. The formalism is the machinery the rule is executed
in. A document occupies a node; a *result* is an edge — the rule fired, and something
came out that can be graded.

Grades follow the state doc: **●** proved · **◐** measured · **○** conjectured,
load-bearing · **⨯** refuted · **▢** framing, no gradeable claim.

---

## 3. Visited nodes (19 documents)

| # | document | substrate σ | formalism | what the rule produced | |
|---|---|---|---|---|---|
| 1 | Vol I *Derivation of Value* | value | — (native) | the operator, stated | ▢ |
| 2 | *Combination Proofs* v0.3 | multi-projection score | mechanism design | ρ, ι, residue, harvestability | ○ |
| 3 | *Proof of Coherence* v0.4 | coherence among models | sheaf cohomology | H¹ as the score | ○ |
| 4 | *Onboarding* | — | exposition | — | ▢ |
| 5 | Vol II *Proof of Preservation* | negentropy | thermodynamics | preservation as stakeable | ▢ |
| 6 | *Gauge-Fixing* | the section space | gauge theory | four anchors; §5 test suite | ◐ |
| 7 | Vol II *Omnium* | dimension kinds | — | five kinds of dimension | ▢ |
| 8 | Vol II *Kar-Coin* v0.2 | attestation direction | Kardashev–Barrow | the inward/outward axis | ▢ |
| 9 | Vol III *Admitted or Refused* v0.2 | the ledger itself | — | open ledger, by design | ▢ |
| 10 | Vol IV *Borrowed Hardness* v0.2 | cryptographic hardness | — | borrowed vs derived | ▢ |
| 11 | *Gluing the Gates* | composition of gates | Čech cohomology | Claim 4.3 obstruction | ○ |
| 12 | *The Multiplicity Freedom* v0.3 | identity | arithmetic | **T1, T2, T3** | ● |
| 13 | *No Global Section* | composition failure | contextuality | three grades; Conj 3.1 | ○ |
| 14 | *Requisite Richness* | the richness floor | cybernetics | ρ·h ≥ H(D) | ○ |
| 15 | Vol V *What Cannot Be Helped* | residue | — | the assertion/residue line, then its deflation | ▢ |
| 16 | *Sign and Work* v0.2 | the trace | stigmergy | **τ = f/w**; τ inflates the Sybil cap by 1/τ | ◐ |
| 17 | *A Consistent Fiction* | closure | autopoiesis | fiction space = d; coupling = d scalars, once | ◐ |
| 18 | *Coutility* | the composition operation | open games | **Prop 4.1**: equilibrium ≠ admissibility | ● |
| 19 | *Borrowed Again* | signatures | PQ cryptography | migration moves *between* structures | ◐ |

**Nodes entered and vacated** — the rule fired and the result did not survive:

| ⨯ | gap hierarchy tracks nesting | it tracks geometric self-similarity; Gauge-Fixing §5 survived the objection and is stronger for it |
| ⨯ | d_s as an independent third projection | ι ≈ 0 against a structure-aware adversary |
| ⨯ | H1 generalises from rank to H⁰ | a property of §4.2's simplification, not of coherence substrates |

Three vacated nodes against nineteen occupied is the honest ratio, and it is recorded
here because a rule-space that only ever grows is not being tested.

---

## 4. The graph

```
                                   σ ↦ derive(σ)
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
   NEGENTROPY                      COHERENCE                       HARDNESS
   Vol II (5)                      PoC (3) · CP (2)                Vol IV (10)
        │                               │                               │
        │                          ┌────┴────┐                          │
        │                    gauge-fix   compose                   ┌────┴────┐
        │                     GF (6)     GtG (11)              structured  derived
        │                        │           │                  ML-DSA    SLH-DSA
        │                        │      ┌────┴────┐                  └────┬────┘
        │                        │  contextual  open games          BA (19) ◐
        │                        │  NGS (13) ○  Coutility (18) ●         │
        │                        │                                        │
        │                   ┌────┴─────┐                                  │
        │                closure    richness                              │
        │                ACF (17) ◐  RR (14) ○                            │
        │                                                                 │
        └──────────────────────┐                    ┌─────────────────────┘
                               │                    │
                          IDENTITY  ←── ι ──→   THE TRACE
                          MF (12) ●             S&W (16) ◐
                               │                    │
                               └────────┬───────────┘
                                        │
                                  RESIDUE — Vol V (15)
                                        │
                                  ⟨ deflation ⟩
                                        │
                       "residue is negentropy with its provenance fixed"
                                        │
                                        ▼
                        ═══ the branches were never distinct ═══
```

The last edge is the one that matters and it points backwards. Vol V walks the rule
down a fresh branch to a new substrate and then reports that the branch rejoins the
one it started on. That is a confluence, and the whole map has to be redrawn around it.

---

## 5. Confluence

The one distinction, derived independently six times:

| # | where | form |
|---|---|---|
| 1 | Kar-Coin (8) | outward / inward |
| 2 | Combination Proofs §4 (2) | harvestable / not |
| 3 | Multiplicity Freedom (12) | asserted / traced identity |
| 4 | Sign and Work (16) | marker / sematectonic |
| 5 | A Consistent Fiction (17) | provenance / content |
| 6 | Borrowed Again (19) | structured / unstructured signature |

Six paths, six vocabularies, one node. Vol V named it — assertion versus what an action
cannot help but leave — and then said the harder thing: the substrates the anthology
distinguished are not distinct substrates.

**The count that follows.** Nineteen documents. One substrate after the deflation.
Roughly eight formalisms. The apparent state space is a coordinate artefact; the real
one is *a single node, instrumented eight ways*.

The state doc raises the depth-or-monomania question and answers it "partly." The map
gives the structural form of the answer: **it is one node.** Whether instrumenting one
node eight times is depth or monomania is not a question the map can settle — but it is
now the correct question, and it is no longer answerable by pointing at the document
count.

---

## 6. Invariants

What every branch has produced, without exception:

**The attestation problem.** Formalisms relocate difficulties; they do not dissolve
them (*Coutility* §5, after three instances — now six).

- Residue relocates attestation into the trace → *Sign and Work* has to define τ.
- The cohomological invariant detects failure → certifies nothing (*NGS* claim 4).
- Open games supply a well-typed composition → preserving the predicate the framework
  does not gate on (*Coutility* Prop 4.1).
- Autopoiesis supplies closure → and prices the escape at d scalars the anchors are
  forbidden to supply (*ACF* §6).
- Requisite variety supplies a floor → in units not commensurable with ρ (*RR* §8.1).
- The PQ migration supplies derived hardness → at 2–10× bandwidth (*BA*).

Every import was worth making. Every one made the difficulty sharper. None made it
smaller.

**The load-bearing convention.** Twice now, a result has turned out to rest on
something nobody stated: C1 (participation) and C2 (kernel tolerance below the spectral
gap). Both read as numerical hygiene. Both are security conditions. The general form —
*which other implicit conventions are load-bearing?* — is open problem 3 in the state
doc and is arguably the most rulially general thing the program has found, because it
is a property of how the rule gets executed rather than of any substrate.

**The absurd instrument.** Four of seven self-corrections came from a diagnostic that
returned an *impossible* number rather than a merely surprising one. This is a fact
about the program's method, invariant across every formalism it has entered.

---

## 7. The rulial invariant, stated as a conjecture

The corpus's most-repeated observation, restated in these coordinates:

> **Conjecture R.** The attestation problem is invariant under change of formalism. No
> import relocates it out of the mechanism; every import that appears to has moved it
> into a quantity the importing formalism does not itself supply.

Six confirmations, zero counterexamples, and the corpus states it as a *through-line* —
a pattern noticed. In rulial coordinates it is a claim with a shape, and the shape has
a consequence the through-line form does not:

**It is falsifiable, and the corpus has never tried to falsify it.**

A refutation would be a formalism in which the forging cost *f* is derivable from the
substrate rather than assumed — τ ≥ 1 as a theorem rather than a design obligation
(*Sign and Work* Prop 3.4 makes τ ≥ 1 exactly Vol V's soundness clause, and calls
supplying it an obligation). Every planned paper P6–P11 is selected for the open
problem it *closes*. None is selected for the invariant it could *break*.

That is the map's one actionable recommendation and it is a recommendation about the
harvest plan's selection criterion, not about any paper in it: **add a slot for the
formalism most likely to refute R.** If R survives a paper written to kill it, it stops
being a through-line and becomes the program's central negative result — which is a
larger claim than anything on the current open-problems list, and cheaper than the
security proof.

Candidates, unresearched, offered as a starting point rather than a plan:
thermodynamics of computation (Landauer — a floor that is *physical* and therefore not
supplied by the mechanism); zero-knowledge proof systems (soundness as a theorem about
forging cost, which is the exact shape a refutation needs); interactive proof /
PCP-style verification. The corpus has filed the first as a v0.2 of *Gauge-Fixing* and
has not touched the other two.

---

## 8. The unreachable node

**ι.** Five dependents — the multiplication claim, richness-as-packing-number, the
Sybil amplification Γ = γ(1 + (K−1)ι), its saturation ceiling 1/(1−ι), and τ. No
formalisation. Two failed measurement attempts (`code/iota_asymmetry.py`).
ι(dim|ker) = 0.08 is solid; ι(ker|dim) is unmeasured.

In these coordinates ι is not one open problem among ten. It is **the metric on the
space** — the quantity that says how far apart two projections are, and therefore
whether a path between them is short or long. Without it the graph in §4 has edges but
no lengths, and every quantitative claim in the corpus reads a length off a metric that
does not exist.

P6 (*The Metric on the Projections*, information geometry) is literally the attempt to
construct it. Its central tension — ι is asymmetric, Fisher metrics are not — is a
statement that the space may not be metrisable at all, only divergence-equipped. That
is worth writing even as a negative result, and the plan already says so.

**The map's verdict on sequencing:** ι is not on the critical path because it is the
hardest problem. It is on the critical path because it is the only one whose absence
degrades results already published. Conjecture 3.1 (*NGS* §8.1) has the same property —
a published paper's quantitative content resting on an untested conjecture — and is
cheaper. State-doc ranking (Conj 3.1 first, ι second) stands.

---

## 9. Unentered branches

**Planned** (`research-program.md` §3): P6 information geometry · P7 renormalization ·
P8 Ostrom's nested enterprises · P9 costly signalling · P10 representational
measurement theory · P11 Markov blankets.

**Structurally empty — no plan, noted because the map shows the hole:**

| hole | what sits there | why it is empty |
|---|---|---|
| the refuting formalism | §7 | the selection criterion never asked for one |
| the build | Gauge-Fixing §5 has no respondent | construction, not research — and the harvest line cannot discharge it |
| the security proof | shrunk by the Sybil fragment, not closed | same |
| substrate rejection | no document argues a substrate is *unsuitable* | the corpus has only ever added substrates, and Vol V then merged them |
| adversary as author | every adversary in the corpus is a model, not a respondent | no external attempt on the mechanism has been made |

The last two are the ones the map surfaces that the plan does not list. Neither is a
paper, exactly. Both are the kind of hole a self-map exists to show.

---

## 10. What is declined

- **No new results.** Nothing here is graded that was not already graded in the state
  doc. Conjecture R is a restatement of an existing through-line into a falsifiable
  form; the restatement is the only novelty and it is a small one.
- **No claim of rulial completeness.** The formalism axis has eight members because
  eight have been imported, not because eight exhaust anything. A ruliad in Wolfram's
  sense would range over all possible formalisms and this ranges over the ones that
  happened.
- **No emulation claim.** Whether the eight formalisms emulate one another — the actual
  Wolfram question, and the one that would make "ruliad" more than a filing system — is
  untested and is not asserted. Confluence on the *substrate* axis (§5) is established
  by Vol V. Confluence on the *formalism* axis is not, and §6's evidence is consistent
  with the weaker reading that all eight merely fail in the same place.
- **No claim that the map changes the ranking.** It confirms the state doc's open-problem
  order and adds one item (§7) that is not on it. It does not reshuffle.
- **The Wolfram framing is a coordinate choice and is disposable.** If Conjecture R is
  refuted or the emulation question resolves negatively, the right response is to drop
  the word and keep §§5–9, which do not depend on it.

---

## 11. Summary

One rule. After Vol V's deflation, one substrate. Eight formalisms, nineteen documents,
three vacated nodes, two theorems, seven measurements, seven self-corrections.

Every formalism sharpened the attestation problem and none of them dissolved it. The
corpus records that as an observation. It is better read as a conjecture with six
confirmations and no adversary — and the cheapest unexplored move in the program is to
build the adversary.

The metric on the space does not exist yet. Until ι does, this map has a shape and no
distances.
