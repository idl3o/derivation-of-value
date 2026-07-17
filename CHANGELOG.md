# Changelog

Versioning convention:

- **Patch** (x.y.z) — typos, prose polish, single-paragraph clarifications, broken-citation fixes. No new claims, no structural change.
- **Minor** (x.y) — new sections, sharpened theorems, added worked examples, reframed claims that don't contradict the previous version.
- **Major** (x.0) — the document graduates from working draft. Claims would be defended to a hostile reader.

Each document carries its own version, tracked here and noted inside the document itself.

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
