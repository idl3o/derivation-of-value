# Research program — the harvest line

Working document. Not published to the site.

**A second line opened 2026-08-06: see `_plan/service-reframe.md`.** Where this document
varies the imported *formalism*, that one varies what the mechanism *emits* — delivering
coherence as a service rather than paying for it. It carries two planned papers (S1 the
reframe, S2 the capture adversary, probably prerequisite), supplies P7 its first
measurable instance, and has one result already: usage does **not** supply structural
coupling, because satisfaction is maximised at zero contact with the world.

This plans the line opened by *Gluing the Gates*: **take an outside research topic
that the program has been circling without naming, and harvest it into a paper.**
Each entry below is specified far enough that drafting can begin from it directly.

Status key — `planned` · `researched` (sources verified) · `drafting` · `v0.x` (in `_papers/`)

---

## 1. Where the corpus stands

**Twenty-six documents, orders 1–26** (eleven when this plan was written). Everything
through order 26 is **published** as of 2026-09-07. The spine is Vols I–V: Vol III's
ledger stays open by design, and Vol V (*What Cannot Be Helped*, residue) was opened
this session with *Sign and Work* as its technical companion.

Eight papers were added: Gluing the Gates(11), The Multiplicity Freedom(12),
No Global Section(13), Requisite Richness(14), Vol V(15), Sign and Work(16),
A Consistent Fiction(17), Coutility(18), Borrowed Again(19). Five were revised:
Combination Proofs→v0.3, Proof of Coherence→v0.4, Kar-Coin→v0.2,
Admitted or Refused→v0.2, Borrowed Hardness→v0.2.

**Open problems inherited, by reference:**

| ref | problem |
|---|---|
| CP §7.1 | quantitative independence measure ι |
| CP §7.2 | the verifiability boundary — which projections admit intrinsic verifiers |
| CP §7.3 | ρ formally — **partly answered**: fractional spectral dimension, measured |
| CP §7.4 | universality — are Combination Proofs *necessary*, not just sufficient |
| GtG §8.1 | non-affine gates — **route identified** (presheaf of distributions), *untested* |
| GtG §8.2 | a composition law for ρ |
| GtG §8.3 | depth versus span |
| GtG §8.4 | is the verifiability boundary the same boundary as the composition obstruction |
| GtG §8.5 | adversary-positivity under nesting |
| Vol III | the Goodhart-asymptotic **security proof** — *shrunk* by the Sybil fragment, not closed |
| Vol III | the **build** — implement the Gauge-Fixing §5 suite |

**New debts this session created, ranked by how much rests on them:**

| ref | problem | why it matters |
|---|---|---|
| NGS §8.1 | ~~test Conjecture 3.1 (distributional presheaf)~~ done, P17 | a *published* paper's quantitative content rested on it; it holds |
| Sybil §8.2 | state C1 (participation) and C2 (tolerance ≤ spectral gap) as framework conditions | without them duplication on H⁰ is unbounded; both currently modelling conventions |
| Sybil §8.1 | which recoverability model — linear or compounding | they diverge 2× at K=8 and the framework cannot choose |
| Coutility §7.1 | exhibit a Combination Proof as an open game | Claim 3.1 is a prescription, not a theorem, until this exists |
| Coutility §7.2 | restate Goodhart-asymptotic security as an *equilibrium* property | if it works, compositionality comes free |
| ACF §8.2 | can measurement supply content without an oracle? | decides whether closure is escapable at all |
| RR §8.1 | make the per-projection variety bound h precise | without it Requisite Richness §§3–4 are analogy |
| BA §7.2 | is an *unstructured* delay function possible? | otherwise both most-exposed components re-base onto structure |
| S&W §7.1 | measure τ for the spectral projection | one τ measured so far, and it came out at 0 |

Two debts remain *construction*, not research: the security proof and the build. The
harvest line does not discharge them and should not pretend to.

**Standing methodological finding.** Seven claims were caught wrong before
publication this session, four of them because an instrument returned an
*impossible* number rather than a merely surprising one — kernel progress above the
honest maximum, 67 "gaps" equalling exactly the stalk multiplicity, five vectors
spanning five dimensions inside a three-dimensional kernel. **Prefer diagnostics
that can return absurdities over ones that always return something plausible.**

---

## 2. The cascade

```
        A1 contextuality ──────┬──> A2 open games ──> general composition theorem
              │                │
              │                └──> (GtG §8.1 closed)
              v
        GtG Claim 4.3 generalised
                                     A3 info geometry ──> CP §7.1 + §7.3 unified
                                                              │
                                                              v
                                                        GtG §8.2 (ρ composition law)

        B1 autopoiesis ──> bounds every "H¹ = 0 is not truth" caveat in the corpus
              │
              └──> re-reads Gauge-Fixing's anchors as structural coupling

        B2 stigmergy ──> GtG §8.5 + Conjecture 5.2 mechanism
              │
              └──> generalises adversary-positive residue (CP §4)

        C1 Ashby ──> ρ gains a FLOOR (currently ceiling only) ──> substrate selection
        A4 renormalization ──> GtG §8.3 (depth vs span) + Vol IV coda formalised
```

**Superseded — see §3 for current status.** The original recommendation was
A1 → B1 → C1 → B2 → A3 → A2 → A4 → C-tier, and almost none of it survived contact.

**What actually happened.** P0 (Sybil) was not on the map and jumped the queue,
targeting Vol III's largest debt rather than a framework subtlety; its core results
proved outright. P12 (signatures) was added mid-session on a user prompt and drafted
immediately, because it corrected a load-bearing sentence in Vol IV. A3 was promoted
to critical path on the strength of a premise that then failed to measure. And Vol V
opened, which the plan had not anticipated at all.

**Drafted: P0, P1, P2, P3, P4, P5, P12, plus Volume V.**
**Remaining: P6 (critical path, premise open) → P7 → C-tier P8–P11.**

**A3/P6 is the live problem.** Every quantitative claim in P0 is a function of ι, as
is the multiplication claim, as is richness once Def 5.1 is read as a packing number,
as is P0's amplification ceiling, and now as is Sign and Work's τ analysis. Five
independent dependents, no formalisation, and **two failed measurement attempts** —
sparsification shatters the complex and contaminates the kernel proxy; rewiring stays
connected but moves d_s only 8%. Either find a third attack design, or write P6 as an
honest unresolved fork. **What must not happen is the critical path stalling silently
while easier papers get written around it** — which is precisely what happened this
session, and is worth naming rather than repeating.

---

## 3. Papers

### P0 · Sybil — `order: 12` — **v0.1 drafted** → `the-multiplicity-freedom.md`

*"The Multiplicity Freedom" · "Sybil-Asymptotic Security as the Provable Fragment"*

Not in the original map. Added and drafted because it targets Vol III's largest
debt: Goodhart-asymptotic security is unproven because fake-cost rests on
*capability*, which resists formalisation — but **Sybil cost is arithmetic**, so
that fragment yields to proof without an adversary in the loop.

Three theorems, proved and verified (`code/sybil_bound.py`, `_plan/sybil-proof-notes.md`):
T1 the cap N ≤ ⌊C/Γ⌋; T2 amplification Γ = γ(1+(K−1)ι) with a saturation ceiling
of 1/(1−ι) under compounding recoverability; T3 only convexity above the gate
punishes splitting, and concave rewards are strictly Sybil-*positive*.

The structural find: all three hypotheses are anchors the program had already
built — duplication-non-invariance (identity gauge), a resource floor (dissipation
floor), graded independence (ι). Does **not** escape Douceur; quantifies him.

**Remaining debts this paper names.** §8.1 which recoverability model holds — the
two diverge by a factor of two at K=8 and the framework cannot choose between them.
~~§8.2 settle H1~~ **DONE** — PoC v0.3 §4.2.1, Sybil paper v0.2. H1 was
mis-stated (individual earnings, should have been group totals → restated as
*duplication-boundedness*); §4.2's literal provenance formula was shown not to
work and corrected to input-filtering; and H1 turns out to hold under **every**
credit rule because the coherence functional is a rank, so duplication-resistance
is inherited from the substrate rather than bought from the scheme. The fork
resolved to filtered provenance on the delay-chain anchor. Remaining open form is
narrower: for which substrate functionals does duplication-boundedness fail?

---

### P1 · Contextuality — `order: 13` — **v0.1 drafted** → `no-global-section.md`

**Title** "No Global Section" · **Subtitle** "Contextuality as the General Form of Composition Failure"
*(alternatives: "Every Level Healthy", "The Contextual Mechanism")*

**Thesis.** Composition failure in nested mechanisms is contextuality in Abramsky's
exact sense. This is not an analogy — it is the same obstruction in the same Čech
machinery. Importing the theory supplies what *Gluing the Gates* left open: a route
past the affine hypothesis, a hierarchy of failure strengths, and an honest account
of what the cohomological invariant can and cannot certify.

**Closes.** GtG §8.1. Upgrades GtG Prop 4.2 from a hand-built 3-cycle to an instance
of a studied phenomenon. Partially addresses GtG §8.4.

**Claims to establish.**
1. A gate sheaf is an *empirical model* in Abramsky–Brandenburger's sense: interfaces
   are measurement contexts, admissible states are outcomes, and the compatibility
   family is the interface agreement condition.
2. The presheaf-of-distributions construction recovers an abelian object **without
   linearising the gates** — this is the concrete route past GtG's affine hypothesis.
3. The strength hierarchy transfers: probabilistic / logical / strong contextuality
   become three grades of composition failure, each with a different design response.
   (Strong contextuality = no local assignment extends at all; logical = some do not.)
4. The invariant is a **detector, not a certificate** — non-vanishing is sufficient
   and not necessary. Already folded back into GtG Claim 4.3.
5. *Vol IV link, handle carefully.* Contextuality is a quantum **resource**, not only
   a pathology — it powers speedups. Ask whether economic contextuality is likewise
   harvestable (CP §4 adversary-positivity), i.e. whether a designer can *use* a
   holarchy's non-gluing rather than only detect it. This is the paper's speculative
   section and should be marked as such.

**Structure.** 1 What composition failure looks like · 2 Empirical models and gate
sheaves · 3 The translation · 4 Three grades of failure · 5 What the invariant
certifies · 6 Contextuality as resource (speculative) · 7 What is declined · 8 Open

**Sources — verified.**
- Abramsky & Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*, NJP 13:113036, 2011. arXiv:1102.0264
- Abramsky, Mansfield & Barbosa, *The Cohomology of Non-Locality and Contextuality*, arXiv:1111.3620, 2011
- *A Sheaf-Theoretic Characterization of Tasks in Distributed Systems*, arXiv:2503.02556
- To verify at draft time: *Contextuality: At the Borders of Paradox* (arXiv:2011.04899); *Cohomology in Constraint Satisfaction and Structure Isomorphism* (arXiv:2206.15253)

**Risks.** The contextuality setting is probabilistic; gates are deterministic
thresholds. The translation in claim 2 is the paper's load-bearing move and may not
survive contact — if it fails, the paper becomes a negative result, which is
publishable in this corpus and should be written as such rather than abandoned.
Do **not** let the quantum connection become mystical; §6 is explicitly speculative.

---

### P2 · Autopoiesis — `order: 17` — **v0.1 drafted** → `a-consistent-fiction.md`

*Prior art clear: nothing on autopoiesis in mechanism design. Two results measured
(`code/fiction_space.py`): the **fiction space** has dimension d — five consensus
runs converge to five distinct perfectly-coherent worlds spanning the whole kernel
— and **structural coupling costs d scalars once**, at a single vertex, scaling
with components rather than network size. The turn: Gauge-Fixing's anchors all fix
PROVENANCE, the fiction space is a freedom of CONTENT, so the program has chosen
closure knowingly and never priced it. Vol V's residue does not rescue it either,
being negentropy-with-provenance. Proposed escape (§6, conjecture): the inward
axis attests by artifact, and measuring is not testimony — so it may be the
program's only available structural coupling. §8.2 states what a construction
would need.*

*Original plan entry follows.*

**Title** "A Consistent Fiction" · **Subtitle** "Organizational Closure and the Limit of Coherence-Based Attestation"

Title is lifted from the corpus's own diagnosis at `proof-of-coherence.md:74`:
*"A consistent fiction is consistent. Coherence-of-coherence collapses to
autopoietic-cult attractors."* The program named this failure mode and never studied it.

**Thesis.** That failure mode is autopoiesis. Maturana and Varela's theory of
organizational closure is the formal account of a system that maintains its own
coherence with no reference outward, and it converts the corpus's most-repeated
caveat — *H¹ = 0 certifies coherence, not truth* — from a caution into a result with
a stated boundary.

**Closes.** Bounds every coherence-is-not-truth caveat in the corpus. Reframes
Gauge-Fixing's anchors.

**Claims to establish.**
1. A coherence mechanism at equilibrium satisfies the operational definition of an
   autopoietic system: organizationally closed, its components producing the network
   that produces them.
2. Closure is therefore not a bug that better scoring removes. It is the *attractor*
   of any purely coherence-based mechanism, and the design question is not how to
   avoid it but what bandwidth of structural coupling to the world is maintained.
3. **The sharp claim.** A coherence substrate with no physical anchor is not merely
   vulnerable to a consistent fiction — it *converges* to one. Gauge-Fixing's four
   anchors are then not a security patch bolted on; they are precisely the structural
   coupling that prevents autopoietic closure, and the paper re-reads them as such.
4. Consequence for the anchor discipline: Gauge-Fixing's rule that the physical anchor
   be consumed "only as randomness and timing, never as a certificate of order" is
   exactly a specification of *minimal* structural coupling — the least contact with
   the world that still prevents closure.

**Sources — to verify at draft time.**
- Maturana & Varela, *Autopoiesis and Cognition: The Realization of the Living*, 1980
- Varela, *Principles of Biological Autonomy*, 1979
- Luhmann's social-systems extension — **use with care**, it is contested and the
  paper does not need it. Prefer the operational biological definition.

**Risks.** The autopoiesis literature carries philosophical freight the corpus does
not want. Stay operational. Do not import enactivism or second-order cybernetics
wholesale. The claim is about closure and coupling, nothing more.

---

### P3 · Requisite variety — `order: 14` — **v0.1 drafted** → `requisite-richness.md`

*Drafted with the Conant–Ashby hedge built in: the theorem is contested and shows
only that regulators maximally simple among optimal ones are homomorphic images,
not that every good regulator is a model. Claim 5.1 states the conditional and
does not discharge it. Principal weakness, flagged in §7: the commensurability of
H(D) with ρ via a per-projection variety bound h — §8.1 is to make h precise.*

*Original plan entry follows.*

**Title** "Requisite Richness" · **Subtitle** "Variety as a Lower Bound on Substrate Richness"

**Thesis.** Definition 5.1 gives ρ as a **ceiling** on a mechanism's order. Ashby's
law of requisite variety supplies the missing **floor**, set by the adversary rather
than by the substrate — and substrate selection becomes a constrained problem rather
than a maximisation.

**Closes.** Turns richness from a bound into a requirement. Highest chance of an
actual theorem of anything in this plan.

**Claims to establish.**
1. Ashby: only variety can absorb variety; a regulator needs variety at least that of
   the disturbances it must counter.
2. Translation: a Combination Proof must have ρ at least the variety of the adversary
   strategy space it must *distinguish* — giving ρ ≥ (some measure of) the attack
   space, a lower bound complementing Def 5.1's upper one.
3. **Conant–Ashby is the gift here.** "Every good regulator of a system must be a
   model of that system" — and this program's substrate *is* models of the world.
   The good-regulator theorem may say something direct about why coherence among
   models is the right substrate, rather than one substrate among many. This bears
   on CP §7.4, the universality question, which no other planned paper touches.
4. Beer's VSM is a designed holarchy with recursion built in — a ready-made test case
   for *Gluing the Gates*' compositionality criterion. Does the VSM glue?

**Sources — to verify at draft time.**
- Ashby, *An Introduction to Cybernetics*, 1956 (law of requisite variety)
- Conant & Ashby, *Every Good Regulator of a System Must Be a Model of That System*, Int. J. Systems Science, 1970
- Beer, *Brain of the Firm* (1972), *The Heart of Enterprise* (1979)

**Risks.** Requisite variety is invoked loosely everywhere; state it precisely or not
at all. The bound in claim 2 needs a variety measure that is commensurable with ρ —
if none exists the claim degrades to an analogy and should be dropped.

---

### P4 · Stigmergy — `order: 16` — **v0.1 drafted** → `sign-and-work.md`

*"Sign and Work" · "Stigmergy, Sematectonic Traces, and the Cost of Forging a Residue".
Discharges Vol V's concession. Grassé's coinage splits along the volume's own line —
stigma/marker-based = assertion, ergon/sematectonic = residue — a distinction
Theraulaz & Bonabeau drew in 1999 and the biology implied in 1959. Defines the
**trace gap τ = f/w** (forging cost over earning cost); Prop 3.4: Vol V's soundness
clause is exactly τ ≥ 1; Cor 3.5: τ ≥ 1 ⟹ harvestable, so the biconditional and
adversary-positivity are one condition from opposite ends; **Prop 4.1: a trace gap
of τ inflates the Sybil cap by 1/τ** — a mechanism whose traces forge at a tenth
cost has a ten-times-larger adversary and no static audit reveals it. §5 gives
interfaces a reason to be neglected (they are stigmergic — grown, not specified)
and proposes cultivating rather than specifying them, which supplies GtG
Conjecture 5.2 the mechanism it lacked.*

**Prior art checked.** Paredes García, arXiv:2604.03997 (April 2026), formalises
ledger-state stigmergy as architectural patterns (State-Flag, Event-Signal,
Threshold-Trigger, Commit-Reveal) and explicitly does NOT treat incentives,
security, or trace forgery. Cited; this paper sits underneath it.

**Principal hazard, declined in §6:** sematectonic does NOT imply τ ≥ 1 — a facade
is sematectonic and forgeable. The entomological distinction is about what provides
the stimulus, not what counterfeiting costs. Borrowed suggestively, not as a load
bearer.

*Original plan entry follows.*

*Volume V (*What Cannot Be Helped*, order 15) names residue as the general answer
to the attestation problem, and per the program's convention each substrate gets a
volume plus a paper. This is that paper. Its brief tightens accordingly: it must
deliver the formal content the volume only names — in particular the biconditional
(no work without the trace, no trace without the work), whose second half the
volume explicitly calls a DESIGN OBLIGATION rather than a gift. A mechanism scoring
a residue an adversary can lay down more cheaply than the labour it evidences has
built a proxy. Formalising that cost gap is the paper's core.*

*Original plan entry follows.*

**Title** "What the Work Leaves" · **Subtitle** "Stigmergy, Residue, and the Formation of Interfaces"

**Thesis.** CP §4's *residue* (Def 4.3) is a stigmergic trace, and stigmergy — sixty
years of literature on coordination through environmental modification — generalises
adversary-positivity from a harvesting trick into a theory of how holarchies build
their own interfaces without a coordinator.

**Closes.** GtG §8.5 (adversary-positivity under nesting). Supplies the mechanism
Conjecture 5.2 lacks: how reticulation density gets *chosen* rather than imposed.

**Claims to establish.**
1. Grassé's stigmergy: coordination via traces left in a shared medium, with no direct
   agent-to-agent communication and no central plan.
2. Residue is stigmergic. Harvestable projections (Def 4.4) are exactly those whose
   attempts leave traces the next participant can read.
3. Interfaces in a holarchy are stigmergic constructions — grown by accumulated traces
   rather than specified in advance. This is why GtG locates every composition failure
   at interfaces: they are the part of the structure nobody designed.
4. K–B connection: inward (Barrow-axis) attestation is stigmergic by nature; the
   artifact *is* the trace. Outward attestation leaves no trace, which is why it needs
   an oracle. Same distinction, third derivation.
5. Design consequence: a mechanism can *cultivate* an interface rather than specify
   one — set the medium and the trace-reading rule, and let the reticulation find its
   density. Directly testable against Conjecture 5.2.

**Sources — to verify at draft time.**
- Grassé, 1959 (original termite work, *Insectes Sociaux*)
- Theraulaz & Bonabeau, *A Brief History of Stigmergy*, Artificial Life, 1999
- Heylighen, *Stigmergy as a Universal Coordination Mechanism*, 2016
- Bonabeau, Dorigo & Theraulaz, *Swarm Intelligence*, 1999

**Risks.** Stigmergy is a popular metaphor in distributed-systems writing and is often
used without content. The paper must make a claim that could be false — claim 5 is
that claim, and it is testable.

---

### P5 · Open games — `order: 18` — **v0.1 drafted** → `coutility.md`

*Thesis changed on contact with the literature. The plan expected composition to
be total while equilibrium failed to compose; the reverse is true — Ghani et al.
report the **Nash condition is itself compositional**. So the paper splits Gluing
the Gates' two failure modes: **coutility fixes Prop 4.1** (aggregation was never
a composition operation — read the backward leg of the lens and the gate
propagates), and **Prop 4.2 survives untouched** because the framework gates on
ADMISSIBILITY, a constraint-satisfaction condition on states, not on EQUILIBRIUM,
a fixed point of best responses. Prop 4.1 (this paper) shows the two predicates
are of different logical shape, via a trivial-strategy counterexample. §7.2 is the
high-payoff open problem: restate Goodhart-asymptotic security as an equilibrium
property and open games hand over compositionality free.*

*Original plan entry follows.*

**Title** "Coutility" · **Subtitle** "Open Games and the Composition Operation"

Ghani, Hedges, Winschel & Zahn's open games are morphisms in a symmetric monoidal
category, built from lenses, carrying **coutility** — utility a game returns to its
environment. That is the composition operation *Gluing the Gates* §7 explicitly
declined to supply. Conjecture worth testing: **a super-mechanism's gate should read
its constituents' coutility, not their utility** — which would make compositionality
a categorical property rather than a cohomological accident.

Sources verified: Ghani, Hedges, Winschel & Zahn, *Compositional Game Theory*,
LICS 2018, arXiv:1603.04641. Also *Bayesian open games* (arXiv:1910.03656) and the
probabilistic/mixed-strategy extension (arXiv:2009.06831).

Deferred behind P1 because the obstruction theory should be settled before the
composition operation is chosen.

---

### P12 · Signatures — `order: 19` — **v0.1 drafted** → `borrowed-again.md`

*"Borrowed Again" · "Post-Quantum Signatures and the Structure the Migration Keeps".
Added mid-session and drafted immediately, because it carries a correction to a
load-bearing sentence in Vol IV.*

**The correction.** Vol IV identifies the PQ migration with the founding operator —
"away from structured hardness that Shor unravels, toward unstructured and physical
hardness." The conceptual sorting stands; the empirical claim about the field does
not. NIST's **primary** signature standard is ML-DSA on Module-LWE/Module-SIS —
structure — and SLH-DSA, the one that fits the volume's description, is designated
a **backup** "in case ML-DSA proves vulnerable." FN-DSA is lattice over NTRU. Two of
three rest on algebraic structure. **The migration moves between structures, not
from structure to bulk.** Compensating find: NIST's stated reason for holding a
hash-only scheme in reserve *is* the volume's argument — the standards body ran the
sorting without the vocabulary, and got hedging rather than migration.

**The sorting runs inside the lattice family.** plain LWE → Module-LWE → Ring-LWE is
a gradient of increasing algebraic structure and increasing efficiency, and
Module-LWE exists precisely as a hedge against ring-structure attacks. **Efficiency
is bought with structure, and structure is what the volume calls borrowed.** Price of
derivation, measured: SLH-DSA 7,856–49,856 bytes vs ML-DSA 2,420–4,595 — two to ten
times the bandwidth, and the first number the program has attached to its own
preference for derived over borrowed.

**τ for a signature is two numbers.** τ ≈ 1 for "the holder of this key assented"
(that *is* unforgeability); τ ≈ 0 for anything broader — did the work, holds the
stake, is a distinct person. The gap is where mechanisms leak, and it means Vol IV
filed the signature layer as *plumbing* when the Sybil bound's hypotheses live there.

**The hybrid was the operator.** Kar-Coin's lattice-plus-hash straddles the program's
own line — borrowed half carries traffic, derived half carries the guarantee — and is
the only place in the corpus where the right answer preceded the argument for it.

*Open: §7.2 is the sharp one — the VDF repairs on offer (class groups, isogenies) are
ALSO structured, so the program's two most exposed components would both re-base onto
structure. Is an unstructured delay function possible at all? A negative answer would
be worth having explicitly.*

---

### P13 · The exclusion — `order: 20` — **v0.1 drafted 2026-08-14** → `independent-and-expensive.md`

*"Independent and Expensive" · "An Exclusion Principle for the Projections of One
Substrate". Not on the map; jumped the queue because it is open problem 4 of the
state doc — the reordered central question, assigned to no paper — and because
either outcome publishes. Answered: within one substrate, no projection pair
clears both requirements. Paid-DOF model: τ = size of a projection's claim on the
paid pool, ι = disjointness of claims; Theorem 3.3 τ₁ + ι·τ₂ ≤ 1; Theorem 3.4
Γ ≤ W at any K — **richness partitions the budget, nothing multiplies it**. PoW
is the escape, not a counterexample: a second pool = an anchor; a Combination
Proof of order K is K anchors wearing readings. Calibrated instrument
(`code/exclusion.py`, zero deviation on designed specimens); sheaf measurement:
the beacon-keyed generative anchor buys τ(persist) at exactly Prop 5.2's share
while ι(ker|persist) falls 1.000 → 0.000 — the dial that buys τ spends ι.
Unanticipated: stasis scores 9.1× honest persistence under the anchor, excluded
by admissibility not price — the beacon eats the signal (new §8.4). Amends CP
Prop 4.2(ii): strict publicity-positivity saturates at the pool. Conjecture R
gains a mechanism: readings cannot create paid DOF; only anchors can.*

**Consequences for the plan.** P6 inherits three constraints: ι must degenerate
where claims vanish, carry asymmetry, and reduce to claim-disjointness in the
set-model limit. P9's boundary is pre-drawn in §2 (Spence/Zahavi/Grafen/
Holmström cited as ancestors, not claimed) — P9 remains open as the *equilibrium*
harvest. New measurable next steps: the two-pool sheaf (§8.2, would exhibit the
first independent-and-expensive pair, at explicit price) and the graded model
(§8.1). *§8.2 and §8.4 discharged by P14; I&E → v0.2.*

---

### P14 · The second pool — `order: 21` — **v0.1 drafted 2026-09-06** → `the-second-pool.md`

*"The Second Pool" · "An Anchor Per Projection, and Whether the Reading Survives
It". The direct successor to P13: runs its §8.4 gate and then its §8.2 purchase,
in that order. The gate is a gauge argument the 9.135 already contained — under
induced maps the sheaf Laplacian is L_graph ⊗ I in the frame gauge, so an
eigenspace-overlap persistence reading measures the UNIFORMITY of frame motion
(Prop 3.1), and uniform motion is a time-dependent gauge (Cor 3.2): a network
rotating identically scores 1.000, as stasis does, so coherent change and no
change are one orbit. This closes PoC v0.5 §4.5's "score coherent change"
requirement in the negative for the whole class. Measured: honest excess over
the best anchor-only strategy, paired on the same free parts across ten seeds,
mean −0.046, one seed positive — nothing survives; the pinned-beacon control
shows the anchor removes 88% of the drift signal. The purchase: Gauge-Fixing
§4.2's delay chain modelled for the first time as a per-transition encoding
keyed to this epoch's beacon and the participant's own previous section; the
priced temporal reading is the gluing condition on the two-layer sheaf of
consecutive epochs (Prop 5.3: glues iff D_v = R_v(t)T_vR_v(t+1)ᵀ coincide), not
a value read, so Gauge-Fixing test (iv) holds by construction. Result: ι = 1.000
both ways at every positive (En, E_t), each τ its anchor's receipt share of the
joint budget to every decimal, sum = 1 − reconciliation share (0.699 / 0.367 /
0.127 at 1, 4, 16) — I&E §8.5's pool with a number. The chain LEAKS the beacon
(Prop 5.4: a follower transporting last epoch's frame carries this epoch's
beacon value free), so both gates are receipt-and-value and the grid is
arithmetic executed, said plainly. Empirical content: the cheapest forger of
the gluing reading is a follower who did no spatial work; of the overlap
reading, a frozen participant with a paid chain, admissible, at 9.13× honest —
the cult with a receipt. The gluing reading refuses the frozen participant on
gluing grounds (λ_min 0.183 vs 0.05) and carries nothing but its anchor
(S = 0 by construction). Prior art: PoSW/VDF/PoST/Filecoin/Chia cited as the
anchor's ancestors; Ateniese et al. 2020 the closest structure; Baig–Pietrzak
FC 2025 the same question qualitatively; Bittensor weight-copying the stasis
premium deployed. New instrument `code/two_pool.py` (calibration miniature +
seven sheaf checks, all pass; two first-pass errors recorded in its
docstring). Also this pass: CP → v0.5 (Prop 4.2(ii) amended in place, the
08-14 debt paid), I&E → v0.2.*

**Consequences for the plan.** A third way for richness to buy nothing: the
*idle* projection (ι = 1, τ > 0, evidences only its anchor) — MF Cor 5.4 gains
a case and the framework may need a third condition, *evidencing* (§9.5).
S&W §8.1 (a reading outside the induced-map class, restriction maps measured
at overlaps) is now the one door on both axes. ACF §8.5 (two disciplines) is
shown untested by two anchors of one discipline. Next: the budget across
levels (I&E §8.3 / this paper §9.3) — each level carrying two receipts,
GtG Prop 6.1 predicting the minimum. *§9.1 and §9.5 discharged by P15; Second
Pool → v0.2.*

---

### P15 · Evidencing — `order: 22` — **v0.1 drafted 2026-09-06** → `ones-own-anchor.md`

*"One's Own Anchor" · "Evidencing as Independence, and the Overlap as a Copy
Channel". Answers Second Pool §9.5 by subtraction: no third condition. In the
paid-DOF model with P = A ⊔ N (anchor work, native work) and π_A the receipt
check, a projection's native share is τ_N(π) = ι(π|π_A)·τ(π) (Prop 3.2) —
independence from one's OWN anchor — and the idle projection is ι(π|π_A) = 0.
CP Def 2.6 amended (Cor 3.3, CP → v0.6). Theorem 3.4: every declared-frame
reading has τ_N = 0, for ANY function of the declared objects, because the
honest configuration in that class costs exactly the anchor; Cor 3.5: a
Combination Proof of such readings is its anchors, Γ = |A|. The through-line
"the gap is bought entirely by the anchors" is now a property of the class.
Then the one reading outside it (S&W §8.1): restriction maps FITTED at
overlaps by Procrustes (Singer–Wu 2012 / Di Nino et al. 2024 — cited, not
claimed), gated on every edge's residual; frame-invariant, so ι(π_fit|π_A) = 1
by construction and the comparison is against the PUBLIC RECORD. Coalition
with no world model: interior = fiction (free), boundary must fit honest
data. Regime (a) public overlaps: the coalition copies its neighbours and
their noise, boundary residual (σ/√k)√(1−1/b) BELOW honest at every size,
zero with one source — the boundary is a subsidy (Waggoner–Chen 2014 in
sheaf form). Regime (b) commit-before-compare: stale coalition fails at
δ* = (σ/√k)√(tol²k/σ² − 1 − 1/b), measured 1.50 vs 1.58 and 1.75 vs 1.87;
above it the cheapest passing strategy derives boundary prompts only, so
e(C) = |∂C|/(2|E(C)| + |∂C|) (edge-local) or 1/|C| (shared), zero deviation.
On the seed-7 complex block coalitions of 16/32/64/128 have 3/2/3/2 boundary
edges (contiguous ranges 15–20); native cost per identity 12 → 1 vs honest
186: the Sybil cap is NOT a cap on a modular substrate, and GF §2's
spectral-gap target is measured failing on the program's own specimen
(λ₂ = 0.0038). Rotational innovation is free: the measured map's own
temporal gauge. What is evidenced: the world's innovation since the last
public record — information, not effort (Bara arXiv:2609.01873, concurrent,
five days old, cited). Instrument `code/evidencing.py`, 5 s, all six
predictions held.*

**Consequences for the plan.** The budget-across-levels paper (P16, next)
inherits a geometry: a coalition presenting as a holon pays a level's
boundary for a block's identities (MF §8.4, GtG "failures at interfaces"
priced). New design curve: expansion vs richness (§9.4) — the first curve the
residual reading makes measurable; raising λ₂ raises e(C) for every
coalition at the richness cost S&W §5.4 measured. ACF §8.2/§8.5 (content
anchoring) now has an instrument (§9.5). Peer prediction's multi-task repair
vs commitment (§9.2) is the unasked cross-literature question. Conjecture R:
eight.

---

### P16 · The budget across levels — `order: 23` — **v0.1 drafted 2026-09-07** → `the-budget-across-levels.md`

*"The Budget Across Levels" · "Receipts Sum, Interfaces Nest, and the Adversary
Picks the Level". Answers I&E §8.3, Second Pool §9.3 and OOA §9.3 together,
and MF §8.4 with them. The hierarchical complex is a holarchy by construction:
edges PARTITION by the merge that introduced them (|E_l| = 128, 117, 64, 32,
16, 8, 4, 2) and the interfaces between level-l holons NEST, I_l = E_{>l}.
Prop 3.1 receipts sum (disjoint pools per level); Prop 3.2 interfaces nest,
so the compositional holarchic mechanism's native budget is the finest
level's whatever the number of levels — a level-by-level sum overstates it
by sum|I_l|/|E| = 2.30 on the specimen; Prop 3.3 iota(Pi_l|Pi_0) =
|A_l|/(|A_l|+|I_l|), the receipt share. The sum-or-minimum dichotomy was
asked of the wrong pool: SUM for the pool that evidences nothing, UNION for
the pool that does. Prop 4.1: a level-j block's boundary lies entirely above
its level and halves per level EXACTLY (sum over blocks = 2|E_l|, a
double-counting identity), total 4(1 − 2^{j−8}). GtG Prop 6.1 priced on the
sheaf with the residual reading, 26 gates: AND over own-merge gates = every-
edge gate = 3, 2, 3, 2 (the published 12, 4, 3, 1 per identity reproduced);
OR over levels = 0 at every size (the coalition presents at or below its own
level); a level's MEAN gate prices only boundaries above theta ≈ 0.41 of the
level — the two largest blocks at the top two levels, within one derivation
of the arithmetic on marginal epochs — and the network mean prices nothing.
The boundary does not move with the level of presentation; receipts do, and
receipts are idle. MF §8.4's criterion (both sides controlled) is correct —
it is exactly "interior to the coalition" — and NOT a residual: naive
fiction glues at 0.000 against honest 0.203, a two-sided gate refuses it,
and a fabrication of honest scale plus honest-level noise (cost 0) sits at
0.199 inside honest's spread. Prior art: single-shard takeover (Buterin;
Hafid et al.; OmniLedger; Monoxide), Hirshleifer's weakest link, Douceur
Lemma 3, collusion-proofness (Yokoo; Zhang–Tang), cheap community cuts
(Viswanath 2012; Alvisi 2013; Conitzer 2010), Rowe's layered attestation,
Gaži–Kiayias–Zindros firewalls — cited, not claimed. New instrument
`code/holarchy.py`, ~1 s, every prediction held; one first-pass error (the
record-based fiction is zero on interior prompts, so the first mimic was
noise against noise and the fit over-absorbed). Six revisions: I&E → v0.3,
Second Pool → v0.3, OOA → v0.2, MF → v0.5, GtG → v0.3 (Cor 6.2's product
measured as one boundary), Gauge-Fixing → v0.3 (§2 target measured failing;
tests (iii) and (iv) recorded).*

**Consequences for the plan.** The evidencing budget of a holarchy is one
level's boundary; nesting buys receipts. Two design routes are now named and
unbuilt: beacon-assigned overlaps (sharding's remedy transposed — a random
cut grows with |C| and restores the cap, at the cost of the substrate's own
nesting; §9.1) and the audit at a price (§9.4). Depth-versus-span (GtG §8.3)
is a computation on a non-binary holarchy (§9.2). Reward across levels
(§9.5) is MF Thm 6.1's convexity on the level axis. Conjecture R not
invoked: no formalism was imported. Next by the journal's ranking:
Conjecture 3.1 (four sessions untouched), then the expansion-vs-richness
curve (OOA §9.4) which §9.1 here sharpens.

---

### P17 · The obstruction — `order: 24` — **v0.1 drafted 2026-09-07** → `the-obstruction-computed.md`

*"The Obstruction, Computed" · "Conjecture 3.1 on Gate Scenarios with
Spectral Gates". NGS §8.1, the top-ranked open problem for four journals,
done. The AMB obstruction is built on the SUPPORT of a model — free
Z-module on the possible local sections, relative Čech H^1 — and a gate
model IS a support: no distribution is chosen (Prop 3.1; NGS §8.2 confined
to the probabilistic grade, which a gate model does not have — two grades,
not three). The invariant is an integer linear system (Prop 3.2), solved
exactly over Z (Smith normal form, batched RHS per context) and Q; the
truth is brute-forced. Answer key first: Bell 14 sections / 0 obstructed;
Hardy 13 / 1 non-extending / 0 obstructed (the literature's miss); PR box
8/8/8; GtG Prop 4.2's affine cycle on a finite menu 9/9/9. Zero false
positives in 31,056 sections. Spectral gates: R^2 stalks, four-vector
menu, one internal edge per holon, Rayleigh-quotient gate at eps ∈ {0,1,2}
on triangles and squares. Prop 4.1: exact gates ⇒ bijective interfaces ⇒
strong iff composed rotation ≠ id ⇒ every section obstructed (orbit
argument; the Specker triangle's four-state cousin) — held on 8/8 trials.
Sweep (150 + 150): every strongly contextual model seen, not at every
section (0.878 / 0.750 — cohomologically logically but not strongly
contextual, Carù on the program's specimen); of 233 logically contextual
models 136 seen and 97 missed at every section; section rates 0.714 /
0.604. Z = Q on every section (prediction MISSED; ABKLM Prop 20 gives the
direction). Unpredicted: a miss is decided by the longest run of OPEN
gates — two in a row seen, three in a row missed — on both cycles (the
first reading, "one exact gate suffices", was wrong on the square).
Conjecture R ninth: the free module forgets the sign. **v0.2, same day:
the run-of-open-gates reading struck and replaced by Theorem 6.3 — on a
cyclic cover the obstruction is undirected reachability in the bundle
diagram with the section's layer removed (flow conservation; ring-
independent, hence Z = Q), extension is directed reachability, and a miss
needs a connected non-rectangular relation in the chain of non-incident
holons: exactly the eps = 1 tolerance gate. Verified on all 31,056
sections, 1,050 layers, 233 logical models. Design rule on cycles: no
tolerance gate in any chain.** Prior art: AB 2011,
AMB 2011, ABKLM 2015 (AvN ⇒ CSC; Z initial), Carù 2016/2018 (misses;
cyclic completeness), Abramsky databases/CSP, Zeng–Zahn 2015 (choice
theory, no cohomology), Ó Conghaile 2022, Felber et al. 2025, Hansen–Ghrist
— cited, not claimed. No mechanism-design antecedent found. Instrument
`code/contextuality.py`, ~40 s, exact arithmetic. NGS → v0.3 (§3
amended, §7 and §8.1 struck, §8.2 answered for the obstruction).*

**Consequences for the plan.** The four-journal debt is paid, and the
answer is the shape the corpus keeps finding: the invariant is a
certificate, not a test, and now with a rate. Next tools: Carù's cyclic
refinement (§8.1 of the paper) and a design rule "no three aggregate-gated
holons in a row" if §8.2's pattern proves. GtG Claim 4.3's affine
hypothesis is discharged in practice; not revised, since its hedge was the
correct reading. The program's own mechanism (371 contexts, continuous
stalks) is out of the instrument's reach and predicted seen wherever
contextual, having no open gates.

---

### P18 · The ring and the chord — `order: 25` — **v0.1 drafted 2026-09-07** → `the-ring-and-the-chord.md`

*"The Ring and the Chord" · "The Obstruction Off the Cycle, and What It
Sees There". TOC §9.2 measured. Three rings (Z by Smith normal form, Q by
exact elimination, Z_2 by bit-packed elimination) on covers with chords.
ANSWER KEY FAILED ON THE RING: Peres–Mermin (24/24) and GHZ (16/16) are
obstructed over Z and Z_2 and VANISH over Q at every section — explicit
families with coefficients ±1/2, confirmed by least squares at 1e-15. An
AvN argument is a parity argument; the integer obstruction on such a model
is 2-torsion; characteristic zero cannot see it (Prop 3.1). Random models
(400 per cover × 2 conditions) on (3,3,2), GHZ and PM covers: Z = Z_2 on
every one of ~60,000 sections (no odd torsion anywhere); Z ≠ Q only on
three strong parity-like (3,3,2) sections. DETECTION: under the
literature's NO-SIGNALLING condition the logical-grade rates are 0.074 /
0.049 / 0.012 with 154/203, 203/225, 168/172 models invisible; WITHOUT it
0.755 / 0.366 / 0.457 and every strong model seen — the mechanism (a node
absent from one layer zeroes its sums everywhere) stated before that run.
K4 HOLARCHY of four three-port star holons, binary menu, Rayleigh gate:
exact gates ⇒ strong iff mod-2 holonomy fails (8/8), obstructed in every
ring; with tolerance gates NO MISS — 7,056/7,056, 81/81 logical seen (the
prediction that misses occur FAILED). Gate models signal, and signalling
is what the invariant sees: the setting the invariant was built for is
where it is weakest. Conjecture R tenth (the ring forgets the
characteristic). Instrument `code/covers.py`, ~3 min, exact. TOC → v0.3
(Cor 6.4 complemented; §9.2 answered).*

**Consequences for the plan.** The program's mechanism (residual gates,
chords everywhere) is predicted cohomologically transparent — the obstacle
is size, not theory (§8.4). Designer's rule: compute over Z, never Q.
Open: odd torsion (§8.1, a mod-3 model would separate Z from Z_2), the
signalling theorem as a bound on the miss rate (§8.2), conservation on a
hypergraph (§8.3). The contextuality line now has three papers in one day
and should pause for the journal to catch up.

---

### P19 · Every basis at once — `order: 26` — **v0.1 drafted 2026-09-07** → `every-basis-at-once.md`

*"Every Basis at Once" · "The World as Hidden Variable, and the Cover the
Beacon Draws". Sam's question — a quantum-style measurement basis as the
oracular basis, chosen after commitment so a fiction cannot be consistent
in every basis — taken literally and divided. (a) Commitment makes every
participant non-contextual (Prop 3.1 = Fine 1982 with a commitment as
hidden variable; Brakerski et al. 2018 and Kalai et al. 2023 its
cryptographic form). Contextuality appears only without commitment, as the
ADAPTIVE copier (answers each partner with that partner's data) —
signalling; a self-consistency gate refuses it at zero cost (measured:
honest spread 0.000, adaptive 0.267 refused) and leaves the AVERAGING
copier (spread 0, residual 0.08 < honest 0.21), the one commitment was
needed for. NGS §6 closed: real, computable, dominated. (b) What the basis
buys is the COVER: a beacon-drawn, degree-preserving redraw each epoch
makes a block coalition's boundary the random cut (Alon–Chung mixing
lemma): block of 128 from 2 to 191 edges (formula 186), per-identity cost
1 → 96 against honest 186; the residual reading run at f = 1 confirms
(stale fails every epoch, deriving pays, e(C) = 0.518). Curve in f ∈ {0,
1/8, 1/4, 1/2, 1}: boundary linear; lambda_2 of the giant component
0.0038 → 0.049 (13× by f = 1/8) → 0.10, saturating; spectral dimension
1.68 → 2.06 → 2.56 (n = 1024: 1.59 → 2.02 → 2.58), R² 0.996 → 0.975.
Expansion and richness are one purchase with opposite signs; GF §2's
target is met at f = 1/8 and is a loose bound on the price (the cut). The
semantic cost — a beacon-drawn overlap is a prompt the stranger's model
has no reason to hold — named, not modelled. Two instrument errors
recorded (uniform redraw disconnected the graph; swap-rewiring left a
third untouched). Prior art: Fine; Kalai et al.; Toner–Bacon; the memory
loophole; CbD (human data signal by default — honest reporters are
consistently connected because they report the world); Elastico /
OmniLedger / RapidChain / Buterin; cuckoo rule; Alon–Chung; Watts–Strogatz,
Kleinberg, Donetti et al., Lazer–Friedman. No antecedent for no-signalling
as a copying detector, nor for the cut–dimension coupling. Instrument
`code/every_basis.py`, ~10 s. Revisions: BAL v0.2 (§9.1 built), OOA v0.3
(§9.4 measured), NGS v0.4 (§6 closed), GF v0.4 (§2 target met at a
price). Conjecture R eleventh.*

**Consequences for the plan.** The design space now has a knob (f) with
three numbers on it: cut linear, gap saturating, dimension leaving. Next:
the semantic cost as a model (§8.1) — derivation cost as a function of
hierarchical distance — which would give the curve a second axis and an
optimum; keeping nesting for derivation and redrawing only comparison
(§8.5). The contextuality line's positive residue is the spread as a
reading where commitment is unavailable (§8.4). Four papers in one day on
one line; the journal is now the next item, not another paper.

---

### P6 · Information geometry — `order: 27` — *planned* — **CRITICAL PATH, premise now OPEN**

*`code/iota_asymmetry.py` tried to settle whether ι is symmetric and could not.
ι(dim|ker) ≈ 0.08 is solid; ι(ker|dim) is unmeasured — two attack designs failed
(sparsification shatters the complex and contaminates the kernel proxy with
component count; degree-preserving rewiring keeps it connected but moves d_s only
8% of the way). So the metric-vs-divergence fork is unresolved and this paper
cannot yet claim either branch. Draft it as the fork plus the failed attempts, or
find a third attack design first.*

**Title** "The Metric on the Projections" · **Subtitle** "Fisher Information and the Richness Measure"

CP §7.1 conjectures ι will be "information-theoretic — a mutual-information-like
quantity between the optimal attack strategies for different projections." The
packing-number reading of Def 5.1 needs exactly a metric on projection space. Fisher
information is the candidate, and if it works, §7.1 and §7.3 close together as one
problem, which the corpus already suspects (CP §7.3, added v0.2).

**Watch:** ι is *asymmetric* (the fraction of π_j's fake-cost not recoverable from
having faked π_i). Fisher metrics are symmetric. Either a divergence (KL, Bregman) is
the right object rather than a metric, or the asymmetry must be quotiented — and the
asymmetry is meaningful (it encodes attack ordering), so quotienting loses content.
This tension is the paper's central problem, not an obstacle to it.

---

### P7 · Renormalization — `order: 28` — *planned*

**Title** "The Same Move at Every Scale" · **Subtitle** "Renormalization and the Program's Self-Similarity"

Vol IV's coda claims the operator "recurs at every layer it examines, from the
substrate of stake down to the hardness of the primitive that attests it." That is an
unformalised scale-invariance claim. RG is the formalism: the same question asked at
successive scales, with each scale's answer setting the next scale's parameters, and
**fixed points of the flow are what survive coarse-graining** — which would explain
why "derive, don't borrow" keeps reappearing rather than merely noting that it does.

K–B is the scale axis: Kardashev is the infrared limit, Barrow the ultraviolet. A
pure-outward coin has a *UV problem* (cannot resolve fine structure, hence the oracle
trap); a pure-inward coin has an *IR problem*. Closes GtG §8.3 (depth vs span).

Note the history: this was first proposed as a *rival* to the fractal/Mandelbrot
framing, then found to be the same thing — Douady–Hubbard renormalization is the
mechanism generating baby Mandelbrot sets. Both threads belong in this paper.

---

### C-tier — grounding papers, `order: 29+`, all *planned*

| # | title | thesis | note |
|---|---|---|---|
| P8 | "Nested Enterprises" | Ostrom's 8th design principle is literally nested enterprises; empirical evidence for which holarchic governance survives | Nobel-backed, and mostly ignored by crypto-adjacent work. Grounds GtG in observed institutions. |
| P9 | "The Handicap" | Costly signalling (Zahavi, Grafen, Spence) is fake-cost's mature cousin; connects Goodhart-asymptotic security to an existing equilibrium theory | Check whether Grafen's formalisation gives a fake-cost bound directly. |
| P10 | "Admissible Transformations" | Representational measurement theory (Stevens, Krantz et al.) formalises why scalarisation destroys information | Pairs with Omnium's five dimension kinds, which are a measurement-theoretic claim made without the literature. |
| P11 | "The Blanket and the Stalk" | Markov blankets formalise the Janus interface | **Risky.** FEP is contested; take only after P2, and only if the blanket ↔ restriction-map identification survives scrutiny. |

**Not papers.** Percolation theory (a mechanism for Conjecture 5.2's optimum — a
section in P4, not a paper). Thermodynamics of computation / Landauer bounds (deepens
Gauge-Fixing's dissipation anchor — a v0.2 of that paper, not a new one).

---

## 4. Drafting conventions

Technical papers follow `gauge-fixing-the-section-space.md`: front matter with
`eyebrow: "An Anthology · Paper · v0.x"`, `label: "Anthology · Paper"`, `version`,
`date`, an `## Abstract`, then `## N. Title` sections. Anthology essays follow the
Borges register instead — untitled opening, `{:.section-title}` italics, `---` glyph
breaks, a Coda.

Every paper carries a **"What Is Declined"** section. This is the corpus's
characteristic discipline and the reason its claims survive; it is not optional.

**Per-paper checklist.**
1. Read the sibling papers on the shared substrate before drafting — internal
   coherence is the quality bar, and a new paper must not contradict an existing one.
2. **Run a prior-art check before claiming novelty.** *Gluing the Gates* claimed a
   result that was contextuality under another name; the check caught it the same day
   and the citation went in before publication. Do this first, not last.
3. Verify every citation against the actual source. Titles, authors, years, venues.
4. Archive the superseded version (`_archive/<slug>/v<old>.md`) before editing.
5. Changelog entry with what changed and why — the changelog is where "was this ever
   published" is settled.
6. If a measurement is cited, it must be reproducible from `code/`.

**Assign `order:` at draft time, not now.** The numbers above are provisional and
the home page sorts by them.

---

## 5. Standing risks for this line

**Import without contact.** The failure mode of a harvest line is a paper that names
an outside theory, admires it, and changes nothing. Every entry above must close a
referenced open problem or state a claim that could be false. If a draft does neither,
it should be abandoned rather than published.

**Prior art.** Three of these topics (contextuality, open games, information geometry)
have active literatures where someone may already have done the work. Check first.

**The metaphor tax.** Holarchy, stigmergy, autopoiesis, and the free-energy principle
are all heavily abused outside their home fields. The corpus's ethic is explicitly
anti-flattery. Each of these enters as a definition doing work, or does not enter.

**The debts stay unpaid.** None of this discharges the security proof or the build,
and no paper in this line should imply otherwise.
