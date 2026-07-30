# Changelog

Versioning convention:

- **Patch** (x.y.z) — typos, prose polish, single-paragraph clarifications, broken-citation fixes. No new claims, no structural change.
- **Minor** (x.y) — new sections, sharpened theorems, added worked examples, reframed claims that don't contradict the previous version.
- **Major** (x.0) — the document graduates from working draft. Claims would be defended to a hostile reader.

Each document carries its own version, tracked here and noted inside the document itself.

---

## 2026-07-30

### Paper — *No Global Section* — v0.1

`order: 13`. Contextuality as the general form of composition failure. Removes the weak point of *Gluing the Gates*: its cohomological criterion assumed gate conditions are affine on stalks, which **the program's own worked instance violates** — a threshold on a spectral quantity is not affine, so the theory was stated for a case the program does not have.

**The identification (§2).** Local sections everywhere with no global section is *contextuality*, characterised by Abramsky & Brandenburger for quantum non-locality. Definition 2.1 gives the translation: holons are measurements, interfaces are contexts, gate-satisfying states are outcomes. Claim 2.2 — non-compositionality *is* contextuality of the gate model. The departments stand to the firm as local measurement outcomes stand to an absent joint distribution.

**The route past affineness (§3, Conjecture 3.1).** Abramsky, Mansfield & Barbosa recover an abelian object by working with presheaves of **distributions over admissible outcomes** rather than the outcome sets themselves — linearity without linearising the constraints. Conjectured to transfer to gate scenarios. **This is the paper's load-bearing and unestablished claim**; §7 says so and §8.1 specifies the computation that would settle it. Named failure mode: in the quantum case the distributions are given by physics, whereas a designer would have to choose them, so the obstruction may be an artefact of the choice.

**Three strengths (§4).** *Gluing the Gates* had a binary; contextuality grades it. Probabilistic = frequencies irreconcilable across runs → recalibrate thresholds. Logical = some admissible local configuration extends to none globally → **the regime an adversary wants**, since it can steer there, satisfy its own gate honestly, and guarantee the whole fails → redesign interfaces. Strong = nothing extends → specification error, abandon the composition.

**What vanishing certifies (§5).** The established obstruction is *sufficient and not necessary*: there are contextual models cohomology does not see. So it is a **detector of composition failure, not a certificate of composition safety**. Names the pattern: the negentropy paper found H¹ = 0 certifies coherence and not truth; this is the same disappointment one level out, and vanishing cohomology is twice now weaker evidence than it looks.

§6 asks, marked explicitly as speculation, whether economic contextuality is *harvestable* the way quantum contextuality is a resource — the logical-contextuality configurations that an adversary can steer toward are also *distinguishing*. Declines any quantum claim about economic systems: the shared object is a sheaf-theoretic obstruction and nothing else.

### Paper — *The Multiplicity Freedom* — v0.1

`order: 12`. Sybil-asymptotic security as the provable fragment. The program had named this problem four times — Proof of Preservation's *multiplicity freedom*, Gauge-Fixing's *identity gauge*, Proof of Coherence §4.2's *copy-symmetry problem*, and the dissipation floor that exists to price identity minting — without once using the word Sybil.

**Why this fragment proves (§2).** Goodhart-asymptotic security is unproven because fake-cost rests on *capability*, which is a relation between an adversary's models and a substrate's structure and resists formalisation — hence Vol III's demand for an adversary in the loop. **Sybil cost is arithmetic.** Splitting a budget across N identities is division; it needs no model of anything. So this fragment yields to derivation, and proving it shrinks the unproven remainder.

**Three hypotheses, each an anchor already built (§3).** H1 duplication-non-invariance (without it a copy is free and cost is independent of N) = the identity gauge. H2 a positive resource floor (without it Γ = 0) = the dissipation floor, and Douceur's impossibility in the program's own notation. H3 graded independence ι. Three of the four forger freedoms Proof of Preservation enumerated appear here as hypotheses; the anchors were not designed as a Sybil proof, and naming the problem is what lets them be read as one.

**T1 (§4).** N ≤ ⌊C/Γ⌋ rewarded identities. **T2 (§5).** Γ = γ(1 + (K−1)ι), so conjunction-gating amplifies the floor by a factor scaling with order — and since K ≤ ρ, **richness bounds Sybil resistance and Goodhart resistance alike, the same ceiling for two properties**. Corollary 5.2: at ι = 0 richness buys *nothing*. Corollary 5.3: under compounding recoverability the amplification saturates at 1/(1−ι), so the cap never falls below C(1−ι)/γ however rich the substrate. The two recoverability models diverge by a factor of two at K = 8, and a mechanism designed on the optimistic one would have half the resistance its designer believed, invisibly.

**T3 (§6), the least expected.** The gate caps the fleet but does *not* disincentivise splitting within it — that needs f convex above the gate. Linear is exactly Sybil-neutral; **strictly concave is Sybil-positive**, and diminishing returns is the conventional anti-whale choice. A √v reward pays an adversary 2.83× for splitting into eight. The curve chosen to prevent concentration subsidises fragmentation.

Declines: that Douceur is escaped (he is quantified, not escaped — the floor's height is still set by the weakest honest participant); that convexity is costless (it buys Sybil resistance with an unpriced honest-concentration cost); and above all **that H1 holds anywhere** — no concrete mechanism in the program has been shown duplication-non-invariant, so every theorem is conditional on a property the program has demanded and never verified. §8.2 names settling it as small work with disproportionate payoff.

Proofs and verification: `code/sybil_bound.py`, `_plan/sybil-proof-notes.md`.

### Paper — *Gluing the Gates* — v0.1

New technical paper, `order: 11`. First entry of the "harvest an outside research topic into a paper" line; the topic is **holarchy**. Supplies the composition theory the framework has never had — Definition 5.2's ≼ orders substrates by *substitutability*, not by *nesting*, so nothing in Combination Proofs rules on whether a Combination Proof of Combination Proofs is one.

**The identification.** Koestler's holon (1967; SOHO canon 1969) is the entity that is a whole looking down and a part looking up — the Janus phenomenon (1.4). The concept has had a long practical career (PROSA holonic manufacturing, Van Brussel et al. 1998) with no algebra. Claim: **cellular sheaves are the mathematics holarchy has lacked** — stalk = holon as whole, restriction map = holon as part, global section = holarchy integrated, H⁰ = how many integrations exist, H¹ = unresolved self-assertion. Koestler's arborisation/reticulation (6.1) = tree skeleton / cross-edges; his two pathologies map exactly — excessive self-assertion (9.4) = H⁰ vanishes, excessive integration (9.5) = duplication-invariance. **Retro-fit worth noting: Gauge-Fixing §5's demand that reward not be duplication-invariant is a guard against Koestler's second pathology, built before the program had a name for it.** Hansen & Ghrist (2019, 2021) supply the quantitative side — the sheaf Laplacian implements consensus and "registers the discord", so the integrative tendency has a spectrum.

**Three results.** (1) *Conjunction-gating does not survive nesting.* Prop 4.1: aggregation-based projections let a healthy majority carry a failing constituent. Prop 4.2, the dangerous direction: every constituent gate satisfied and no global section exists — a 3-cycle with restriction maps composing to a non-identity scalar. This is the formal content of *every department hits its metrics and the firm fails*; the incompatibility lives in the interfaces, where no level is looking. (2) *The obstruction is cohomological* (Claim 4.3, affine-gate hypothesis): local admissible states glue iff a Čech class in H¹ of the gate sheaf vanishes, dim H¹ bounding the independent failure modes. Design implication: super-mechanism projections must be **sections, not aggregates**. Limit stated in the negentropy paper's own words — H¹ = 0 certifies that the levels *compose*, not that any level is *honest*. (3) *Richness does not compose* (Obs 5.1): d_s runs 1.26→2.23 as reticulation varies with the holons unchanged, so ρ of a holarchy is not a function of the ρ of its holons — richness lives in the coupling. Conjecture 5.2 makes Koestler's balance measurable as an interior optimum of ρ against degrading power-law fit, refutable with `code/spectral_richness.py`.

**The punchline (§6).** Against Manheim & Garrabrant's four Goodhart variants: regressional composes mildly, extremal compounds, causal bites hardest at interfaces, and adversarial gives Prop 6.1 — **if the mechanism is not compositional, a holarchy's Goodhart-asymptotic security is the MINIMUM over levels, not the product**, because the adversary picks which level to attack. Corollary 6.2: vanishing H¹ restores the conjunction and with it the multiplication. So the cohomological condition is what converts min back into product, and the framework's behaviour at scale rests on it.

**Prior-art check, and the resulting correction (same day, folded into v0.1 — never published).** No established sheaf-theoretic mechanism design exists, so that intersection is genuinely open. But two near-neighbours were missed on first draft and are now cited. (a) **Prop 4.2 is contextuality.** Abramsky & Brandenburger characterise non-locality/contextuality *precisely* as the obstruction to extending local sections to a global one — the same structure and the same Čech machinery. A holarchy where every level is healthy and the whole is sick stands to its levels as local measurement outcomes stand to an absent joint distribution. (b) **The invariant is weaker than Claim 4.3 implied.** Abramsky, Mansfield & Barbosa prove their cohomological obstruction vanishes when a global section exists but that non-vanishing is *sufficient and not necessary* for contextuality — there are obstructed families the cohomology cannot see. Claim 4.3 now states the consequence plainly: a non-vanishing obstruction is grounds to redesign the interfaces; a vanishing one is **not** a certificate that the gates glue. Detector of failure, not proof of safety. (c) §8.1 gains the concrete route past the affine hypothesis that the contextuality literature already took — presheaves of *distributions* over admissible sets rather than the sets themselves — plus the distributed-computing task-sheaf analogue.

Declined explicitly: a UC-style universal composition theorem; holarchy as a *substrate* (treated as structure only — the substrate reading remains available for a later volume); non-affine gates; anything built; truth. Cites Canetti 2001, Syrgkanis & Tardos 2012/13 (whose "smoothness locally implies efficiency globally" is already a local-to-global result, i.e. sheaf-shaped), Koestler 1967/69, Van Brussel et al. 1998, Hansen & Ghrist 2019/21, Manheim & Garrabrant 2018.

### Combination Proofs — v0.3 — adversary-positive security (§4)

Extends §4 from *publicity*-positive to *adversary*-positive. Its first half asked what happens when a mechanism is described; the new material asks what happens when it is attacked. The operator applied to the adversary: a mechanism that borrows its security from the assumption that attackers can be excluded is borrowing again; adversary-positivity derives it from the attackers' own expended effort.

**Definition 4.3 (Residue)** — the component of an attempted state that persists whether or not the mechanism admits the claim. **Definition 4.4 (Harvestable projection)** — π is harvestable if the residue of faking it is of the same kind as the residue of honest work on it. **Definition 4.5 (Adversary-positive)** — honest cost non-increasing in the volume of failed *forgery* (explicitly not liveness/censorship/availability, which leave no residue). **Proposition 4.6** — a Combination Proof with all projections harvestable is adversary-positive against forgery; rejection of the claim does not reverse the residue.

The load-bearing link: **harvestability sorts along exactly the §8 outward/inward line.** An outward projection measures a flow and is attested by report, so a rejected attempt leaves nothing — not harvestable. An inward projection measures a residue by construction: counterfeiting an atomically specified structure means placing the atoms, and the atoms persist regardless. *The oracle problem and the harvestability problem are the same problem seen from the two sides of an attempt.* Kar-coin's outward axis is therefore unharvestable, and this is now a third independent reason to rebalance it.

Four harvest channels, graded by distance from the substrate: (1) the attempt *is* the work — sharpens Goodhart-asymptotic from "the proxy resists gaming" to "gaming the proxy achieves the goal", and removes the mechanism's need to read intent; (2) local sections come free, so price only the gluing — grounded in `code/independence.py`, where the adversary produced internally consistent blocks and left the cocycle conditions undone, and where structural knowledge (not coalition size) was the binding resource; (3) failed attacks empirically sample ι, so the *attack record* joins the research literature as security accumulator (§4.2's corollary extended); (4) a successful attempt is an intrinsic capability certificate per Def 2.4.

**Remark 4.7** keeps the honesty: rewarding contributing attacks creates a new proxy — *appearing* to be one — and three of the four channels stand one level removed from the substrate and admit their own counterfeits. Only channel (1) bottoms out, because there the contribution is the substrate and no gap remains for a counterfeit to occupy.

### The Kardashev–Barrow rebalance — *Kar-Coin* v0.2, *Combination Proofs* v0.2, *Borrowed Hardness* v0.2

One finding, propagated across three documents. The civilisational-capacity substrate had been specified entirely on **outward** (Kardashev) coordinates — energy capture, information throughput, coordination depth, longevity, every one a magnitude, a *how much*. Barrow's descending complement to Kardashev (*Impossibility*, 1998; Type I-minus through Omega-minus, bulk matter → genes → molecules → atoms → nucleus → elementary particles → spacetime) supplies the missing **inward** coordinate: the grain at which a civilization can act.

The load-bearing claim is that the two families fall on opposite sides of Definition 2.3. An outward projection measures a *flow*, and a flow leaves nothing behind — so its verifier must consult a meter, an inspector, or a certificate, each an oracle outside protocol state. An inward projection measures a *residue* — fine-scale capability is evidenced by artifacts that persist and can be re-measured by anyone with a sufficient instrument, which is an intrinsic verifier in the exact required sense. Hence: **outward capacity is borrowed attestation, inward capacity is derived attestation**, and Volume IV's borrowed/derived sorting recurs one layer up, on capacity claims rather than on hardnesses. Kar-coin's unverifiability was not misfortune; it was the axis.

Independence across the families is strong, and asymmetric in the direction a mechanism wants: the two attacks share no machinery (spoofing a meter teaches nothing about counterfeiting an atomic lattice, and vice versa), while *genuine* inward mastery does imply outward command — exactly Barrow's own observation — and *faked* inward mastery implies nothing, having never placed the atoms. Real capacity propagates up the conjunction; counterfeit capacity does not. Balance is therefore load-bearing rather than aesthetic: a pure-outward coin rewards burning (the proof-of-work flaw at civilizational scale), a pure-inward coin rewards precision that commands nothing.

**Kar-Coin v0.2** — new section *The Ladder That Runs Inward*, between *Capacity Has Projections* and *The Long Horizon*. Does not discharge the substrate's unpaid debt; relocates it into a shaped design problem — how much outward magnitude can be made to *follow* from artifacts a civilization must leave behind, so the coin reads the flow through its residue rather than its report.

**Combination Proofs v0.2** — §8 civilisational-capacity substrate class split into outward/inward projection families, with the attestation asymmetry recorded and a general heuristic proposed for testing elsewhere (extensive projections tend to require attestation, intensive ones tend to supply it). First instance in the framework of the §7.2 verifiability boundary falling *within* a single substrate rather than between substrates.

**Borrowed Hardness v0.2** — the kar-coin audit paragraph said its durability gap "is not cryptographic; it is the oracle problem," which the above makes partly stale. Amended to record the narrowing, plus a new audit finding: the repair is durable in this volume's own sense and for its own reason — measuring where an atom sits is physics, not cryptography, so the inward axis crosses the quantum threshold for the same reason the astrophysical beacon does. It was never on loan.

Spine unchanged: this is a re-specification of an existing substrate plus a cross-cutting structural finding, not a new volume.

### Anthology, Volume III — *Admitted or Refused* — v0.2 · the first self-directed test

New section *One Admitted, One Refused*. The program's first conjecture about its own substrate, stated in two parts, handed to a machine, and returned with one part admitted and one refused. Second entry in the open ledger, and the first that was not a report on someone else's kernel.

**The conjecture.** Coherence complexes are assembled from world-models, and world-models nest (agents model agents modelling agents), so the complex is tiered rather than flat. Two consequences were proposed: (i) that richness ρ is not a count but a *fractional dimension*, readable off the growth of the sheaf Laplacian's eigenvalue counting function; (ii) that the spectrum carries a *hierarchy of gaps*, so Gauge-Fixing §5's demand for "the measured spectral gap" — definite article — would price only the coarsest coalition, letting many small colluding clusters pass beneath the scale the test reaches.

**Method, and the calibration discipline.** The instrument was validated before use against two structures with known answers: a Sierpiński gasket (d_s = 2log3/log5 ≈ 1.365 → measured 1.392) and a square lattice (exactly 2 → measured 2.098). The test complex was built as a hierarchical modular network — self-similar in construction *rule* only — explicitly not as a geometric fractal, so the answer could not be smuggled into the question.

**(i) ADMITTED.** Spectral dimension d_s ≈ 1.61, converged across depths 9–12 (n = 512→4096) with scatter falling from 0.054 to 0.007, R² ≈ 0.9994. Stronger than proposed: d_s varies *continuously* with coupling density (1.26, 1.62, 1.82, 1.95, 2.12, 2.23), passing through the integers without pausing. Fractional richness is therefore the generic case and integer richness the measure-zero exception — Definition 5.1's typing of ρ as ℕ ∪ {∞} excludes almost everything. Also noted: Def 5.1 is already a *packing number* in form, and §7.1's graded ι is exactly the separation scale a dimension reading needs, so §7.1 and §7.3 are plausibly one problem. Control: the coherent sheaf (d=3 stalks, consistent frames) returns 1.614 against the bare complex's 1.607 — gauge-equivalence confirmed, exponent is a property of the substrate not the apparatus.

**(ii) REFUTED.** The first pass appeared to find gap hierarchies everywhere; this was an artefact, and is recorded as one — degenerate eigenvalues collapse the local spacing, so any neighbouring gap measures against nearly nothing and looks enormous (it inflated the gasket to 74 spurious gaps and the coherent sheaf to 67, the latter being exactly the 3-fold stalk multiplicity). Corrected by collapsing to distinct spectral levels: the nested complex shows 3 modest gaps at sparsest coupling, **zero** at denser coupling, **zero** in the full sheaf — against the gasket's 18 across 5 scales. Gap hierarchy tracks *exact geometric* self-similarity, not nesting. The two properties had been conflated because they co-occur in the textbook example, which is a fractal; a coherence complex is not one. **Consequence: the Gauge-Fixing §5 spectral-gap test stands, vindicated by the objection it survived.**

**Unbidden result.** The same measurement separates coherent from incoherent substrates by itself: consistent frames give d_s ≈ 1.61, frustrated frames ≈ 2.6, a ~60% separation reproducible across every construction tried, with no reference to the kernel and none to any gap. A candidate third projection of Δ_𝓕 — the path §6 names for raising the mechanism's order K — and harder to counterfeit than its predecessors, since faking it means reproducing the whole density of states rather than a single number. Independence in the sense of Definition 2.5 is *not* established by this and would need an adversary, not an experiment.

**Combination Proofs v0.2** also carries this: §7.3 gains the measurement, the packing-number observation, the §7.1/§7.3 unification, and the refutation.

Stated limits, in the volume: a toy complex is not a deployed one; the nesting was built in by hand rather than observed; the incoherent case was made incoherent crudely by randomising frames, where a real adversary would be quieter. The security claim is untouched and still waits on a mechanism and an opponent.

---

## 2026-07-23

### Anthology, Volume IV — *Borrowed Hardness* — v0.1

Initial draft, and the closer of the arc visible from Volume I — the durability volume, with post-quantum as its principal lens (as the Vol. I coda promised). Pays the debt in the Vol. I regime-change claim ("quantum computers will not change what coherence is") by splitting durability into two layers: a substrate's *meaning* is quantum-invariant and durable for free, but its *attestation* is only as durable as its weakest cryptographic primitive, and the quantum computer is built to find that primitive. Central device: Shor (1994, dissolves *structured* hardness — factoring, discrete log) vs. Grover (1996, merely taxes *unstructured* hardness — hashing, physics); this asymmetry recovers the anthology's founding operator at the cryptographic layer — number-theoretic hardness is *borrowed* (dissolves when the machine tuned to its structure arrives, like staking capital), physical/hash hardness is *derived* (survives). The post-quantum migration IS the operator applied to hardness itself; the quantum adversary performs a sorting, not a new attack. Runs a substrate-by-substrate audit: coherence (math is quantum-invariant, only plumbing needs re-basing); negentropy — the sharp finding — the Gauge-Fixing VDF temporal anchor uses repeated squaring in RSA groups whose order Shor computes, making it the program's most quantum-fragile load-bearing piece (fix: class-group / isogeny VDFs, known but unproven); omnium (cheapest crossing, kernel is pure arithmetic); kar-coin (already PQ-hardened, but its real gap is the oracle problem, orthogonal to quantum). Closes on the meaning layer no machine reaches and the operator as the quantum adversary's confirmation rather than its casualty.

Placed at `order: 10`. Completes the visible spine (Vol. I names → Vol. II applies ×3 → Vol. III constructs → Vol. IV endures); the anthology stays open (security proof + build still owed, further substrates unnamed).

Path: `_papers/borrowed-hardness.md` · Permalink: `/anthology/borrowed-hardness/`

### Anthology, Volume III — *Admitted or Refused* — v0.1

Initial draft, and the opener of Volume III — the reserved "working examples" milestone. Marks the register turn from derivation (what value must be) to construction (what a mechanism does when switched on against an adversary). Title picks up the Volume I coda's definition of mathematics as objects "to be checked later against the world that admits or refuses them": Vol. III is where the checking begins. Core epistemic argument: a running mechanism is worth more than more prose because the program's claims are claims about *cost*, and cost is discovered only when an adversary can actually try to pay less — a test suite is a claim that has agreed in advance to be refuted. Reports honestly what already runs (the vectorised-money kernel: conservation as a runtime invariant, entropy-direction enforced as price, the acyclic interaction tensor = the omnium DAG condition, substrate-independence demonstrated by two economies on one kernel, ~hundreds of tests; omnium's Merkle/content-addressed ledger before it) and — the discipline — what it does NOT yet prove: the kernel establishes the *thermodynamics* (books can't be cooked by accident) but not the *Goodhart-asymptotic security* (books can't be cooked on purpose by a capable adversary), which needs a mechanism not yet built. Records the Gauge-Fixing §5 test suite as a challenge written before its respondent exists (no non-truthful global section; reward not duplication-invariant; measured spectral gap prices coalition mimicry; anchor consumed only as randomness/timing) — the seam between what's shown and what must be constructed. Unlike the other volumes it does not close: an open ledger that grows per construction. Coda forward-points to the security proof (adversary in the loop) and the closing durability/post-quantum volume.

Placed at `order: 9`. First Volume III entry; the volume is designed to stay open and accrue further working examples.

Path: `_papers/admitted-or-refused.md` · Permalink: `/anthology/admitted-or-refused/`

### Anthology, Volume II — *Kar-Coin* — v0.1

Initial draft. Third and final Volume II essay, completing the triptych (Proof of Preservation, Omnium, Kar-Coin) that applies the operator across the three derived substrates. Takes up the civilizational-capacity derivation named in Volume I — value denominated against a people's position on the Kardashev scale (Kardashev 1964; Type I/II/III by commanded energy), "the order of magnitude at which it can act." Load-bearing honesty: this is the grandest substrate and, minted naively against oracle-measured MWh and GPU-hours, the least intrinsically verifiable — it walks straight back into the useful-work trap Volume I diagnosed ("the verification problem is the consensus problem in another costume"), with the negentropy relocation attack returning "wearing a solar panel." Reads capacity as a rich vector of loosely independent competences (energy capture, information throughput, coordination depth, longevity) — the framework's civilisational-capacity Combination Proof, presumably the highest-ρ substrate in the program — while conceding each projection still needs an intrinsic verifier the construction hasn't yet supplied. Uses the substrate's long-horizon nature (capacity changes on civilizational timescales) to motivate the post-quantum requirement (Shor's algorithm, hybrid lattice/hash signatures) and hand the anthology to its closing durability volume. Grounded in the sibling `kar-coin` repo. Borges-register, matching Volumes I–II.

Placed at `order: 8`; technical companion is the external `kar-coin` repo. With this the Volume II triptych is complete (orders 5, 7, 8; the negentropy paper Gauge-Fixing at 6).

Path: `_papers/kar-coin.md` · Permalink: `/anthology/kar-coin/`

### Anthology, Volume II — *Omnium* — v0.1

Initial draft. The second Volume II essay, paired with *Proof of Preservation* under the Volume II banner: where Preservation stakes negentropy against the world, Omnium finds the same entropy law operating inside the monetary instrument itself. Takes up the multidimensional-value derivation named in Volume I ("money confessed at last to be a vector, scalarized only by the violence of accounting"). Argues the scalar price is a lossy projection of a vector Ω = (m, d₁…dₙ) whose coordinates — temporal, locality, purpose, provenance — were always real and pushed off-ledger into externality. Central proposal: value's dimensions fall into a closed grammar of five algebraic kinds (scalar, ordinal, set, chain, tag). Bridges to the paired essay via the entropy-direction rule (adding information cheap, erasure dear — the second law applied to value) and conservation of magnitude ("a system in which magnitude is not conserved is not an economy but a printing press"). Reads the substrate as the framework's multidimensional-value Combination Proof, and confronts the open independence question head-on: the working framework's partial answer is that full independence isn't required, only an acyclic (DAG) interaction graph; substrate richness ρ = the count of non-redundant dimensions surviving the quotient. Draws on the author's sibling repos `omnium` and `vectorised-money` (2,000-line zero-dependency kernel, human + compute economies, ~339 tests) — cited in the coda as the program's first working examples and a foretaste of the reserved Volume III. Borges-register, matching Volumes I–II; math rendered as Unicode prose per house convention (no MathJax).

Placed at `order: 7`, after the negentropy cluster (Proof of Preservation → Gauge-Fixing), its technical companion being the external `vectorised-money` repo rather than a paper in this collection.

Path: `_papers/omnium.md` · Permalink: `/anthology/omnium/`

### Anthology, Volume II — *Proof of Preservation* — v0.1

Initial draft. Takes up the negentropy derivation named but undeveloped in Volume I. Departs from the Volume I coda's provisional schedule, which slotted coherence "in full" as Volume II — that material already lives in the whitepaper, so the anthology jumps to the first genuinely unworked derivation; the entry's opening paragraph acknowledges the reordering in-register. Runs the Maxwell–Szilard–Landauer–Bennett resolution of the demon, then pivots on the point that carries the volume: Landauer certifies that free energy was *spent*, never that order was *made here, by this hand* — the relocation attack against any entropy boundary makes created order structurally unwitnessable. Reframes preservation as certified not by proof but by gauge-fixing: four shadows order casts (time, uniqueness, coherence, entry cost) composed as a conjunction that quotients away the forger's freedoms (backdating, grinding, duplication, free identity minting). Seats this as the essayistic front door to the companion paper *Gauge-Fixing the Section Space*, and reads the four-anchor construction as a Combination Proof on the negentropy substrate — publicity-positive, fake-cost multiplicative across anchors. Load-bearing correction to the substrate's own first temptation: negentropy is the least inflatable substrate in the program *and* the one that refuses to attest itself; honest value is built in that gap. Borges-register essayistic, matching Volume I. Coda points to omnium / vectorised-money and kar-coin as the remaining named derivations and to the post-quantum durability volume.

Placed at `order: 5` (immediately before its companion paper, mirroring the Volume I → whitepaper arc); *Gauge-Fixing the Section Space* bumped from `order: 5` to `order: 6` to seat the motivating essay ahead of the construction.

Path: `_papers/proof-of-preservation.md` · Permalink: `/anthology/proof-of-preservation/`

---

## 2026-07-17

### Repository — papers collection

Restructured the site so every document lives in a single `_papers/` Jekyll collection instead of scattered top-level folders. The home page now generates its contents list by looping over the collection (sorted by each paper's `order`), so adding a paper is a one-file operation — drop a Markdown file in `_papers/` with `label` / `blurb` / `status` / `order` front matter and it appears on the home page and gets its own page. Set `hidden: true` to publish a page while keeping it off the home list. All existing permalinks preserved (`/whitepaper/`, `/combination-proofs/`, `/onboarding/`, `/anthology/derivation-of-value-i/`), so no links break.

### Gauge-Fixing the Section Space — v0.1

Brought into the site. Previously uploaded with a non-existent `layout: paper` and never linked from the contents, so it did not render; switched to `layout: document`, given permalink `/gauge-fixing-the-section-space/`, and added to the collection. Composes four independent anchors — astrophysical randomness beacon, VDF chain, replication-style unique encoding, and a dissipation floor — as a conjunction that gauge-fixes the section space so only honest global sections survive the quotient.

Path: `_papers/gauge-fixing-the-section-space.md` · Permalink: `/gauge-fixing-the-section-space/`

---

## 2026-05-12

### Proof of Coherence — Whitepaper v0.2

First repo publish of the v0.2 working draft. Carries the v0.1 → v0.1.1 → v0.2 revision history forward: v0.1 (research register, four-condition synthesis recovered as cohomology); v0.1.1 (§4.2 copy-symmetry surfaced with Shapley / provenance-weighted forks); v0.2 (Hodge-Laplacian spectral framing in §3.5, Proof by Resonance as the spectral reward in §4.5, §1.2 Goodhart-asymptotic reframe, §6 cognitive-substrate material woven in as load-bearing motivation rather than skippable speculation). Source converted from docx with bold-spacing artifacts cleaned, "Status: Internal scaffolding" line removed for public publishing.

Path: `whitepaper/index.md` · Permalink: `/whitepaper/`

### Onboarding — v0.1

First repo publish. Companion to the working draft using the dog-and-stick framing to introduce Goodhart's law, the standard failure modes in decentralised AI scoring, and the relational shift that PoC enacts. Seven sections under italic quiet titles. Version pins to "v0.1 working draft" of the whitepaper removed in §7 and the leading note so the companion stays evergreen across whitepaper revisions; otherwise content preserved as written. The §7 list of "questions the draft doesn't yet settle" is partly out-of-date with respect to v0.2 (copy-symmetry now has named forks in §4.2; §6 weave-or-excise is resolved as weave); a v0.1.1 revision will catch this up when convenient.

Path: `onboarding/index.md` · Permalink: `/onboarding/`

### Combination Proofs — v0.1

Initial draft. Frames Combination Proofs as a property of mechanisms whose reward is gated on the conjunction of verifiably independent projections of a structural substrate. Establishes the multiplication claim (Proposition 3.1, informal) and the publicity-positive security claim (Proposition 4.2). Defines substrate richness ρ and the substrate order ≼. Reads PoC + Proof by Resonance as the worked instance at K = 2. Pins four open problems and sketches three unnamed substrate classes (civilisational capacity, multidimensional value, negentropy) as the program's near-term targets.

Path: `combination-proofs/index.md` · Permalink: `/combination-proofs/`

---

## 2026-05-11

### Anthology, Volume I — *Derivation of Value* — v0.1

Initial draft. Names the operator the anthology turns around: the move from staking contingent quantities (energy, capital) to staking what such quantities are derived from (structural agreement, negentropy, dimensional integrity). Borges-register essayistic. Seven sections under italic quiet titles. PoC seated as the worked example without becoming the whole essay; kar-coin, omnium, and Kryptonium named in a single rhythmic pass as instances of the operator.

Path: `anthology/derivation-of-value-i.md` · Permalink: `/anthology/derivation-of-value-i/`

### Repository

Initial scaffolding. Jekyll site with editorial stylesheet (EB Garamond, cream/ink/oxblood). Layouts for home and document pages. Placeholder pages for whitepaper and onboarding companion. CC BY 4.0 license. Static HTML preview included for offline viewing.
