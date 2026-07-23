# Changelog

Versioning convention:

- **Patch** (x.y.z) — typos, prose polish, single-paragraph clarifications, broken-citation fixes. No new claims, no structural change.
- **Minor** (x.y) — new sections, sharpened theorems, added worked examples, reframed claims that don't contradict the previous version.
- **Major** (x.0) — the document graduates from working draft. Claims would be defended to a hostile reader.

Each document carries its own version, tracked here and noted inside the document itself.

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
