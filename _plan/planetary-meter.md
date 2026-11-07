# The planetary meter — 2026-08-10

Working document. Not published to the site.

Feasibility audit for *The Involuntary Ledger* (order 21): channel by channel, what
instrument exists today, what it resolves, what it costs to trust, and what is missing.
The paper carries the theory and the claims; this document carries the numbers and the
verdicts. Discipline for the numbers: **every figure here has an instrument or a public
inventory attached, is order-of-magnitude unless an error bar is stated, and is marked
`~` when from memory of the public literature rather than from a source re-checked at
time of writing.** Nothing below is a measurement made by this program. The program's
own instruments (τ, the biconditional, channel independence) are applied at the end.

---

## 0. The quantity, and the target precision

The thing to be measured: planetary primary energy throughput.

- World primary energy: ~620 EJ/yr (~2023), i.e. **P ≈ 2×10¹³ W ≈ 20 TW** mean.
- Composition (~2023): fossil ~80%, of which the chemical channel sees essentially
  all; nuclear ~4% of primary (~9–10% of electricity, fleet ~370–400 GWe); modern
  renewables + hydro ~15% and growing.
- Kardashev coordinate: K = (log₁₀ P − 6)/10 ≈ **0.73** for Earth now.

Target precision, from the paper's §5 damping (σ_K ≈ 0.043·σ_P/P):

| σ_P/P | σ_K |
|---|---|
| 1% | 0.0004 |
| 5% | 0.002 |
| 10% | 0.004 |
| 50% | 0.018 |
| 100% (factor 2) | 0.03 |

Reading: **a denominator good to ±10% is already a rung coordinate good to ±0.004.**
No channel below needs laboratory precision. The feasibility bar is "which decade,
honestly," and the interesting questions are coverage, independence, and trust —
not significant figures.

Storage term (paper §2): reservoirs, stockpiled fuel, synthesized fuels held. Against
a 20 TW flow, year-scale storage swings are single-digit percent at most; bounded above
by the visible stock of stores. Carried as a line item, not a blocker.

---

## 1. Chemical channel — the working meter

**What it is.** Atmospheric CO₂ stock and growth; O₂/N₂ decline (APO); Δ¹⁴C dilution
as the fossil provenance mark; fuel-specific oxidative ratios (~1.17 coal, ~1.44 oil,
~1.95 gas) as the double-entry checksum.

**Instruments, existing.**
- Flask/in-situ networks: NOAA GGGRN + partners, ~100+ stations; Mauna Loa continuous
  since 1958. Single-measurement precision ~0.1 ppm on a ~420+ ppm column.
- O₂/N₂: Scripps O₂ program and successors, per-meg precision on a signal of
  ~tens of per meg per year decline.
- Δ¹⁴C: AMS radiocarbon on flask samples; urban-gradient fossil-CO₂ quantification is
  an established technique, and the bomb-spike's decay toward background (~2020s) has
  made the fossil dilution signal cleaner, not dirtier.
- Satellites: OCO-2/3, TROPOMI-class column sensors; useful for gradients and
  point-source plumes, not needed for the global stock.

**What it resolves.** Fossil CO₂ emissions ~37–38 GtCO₂/yr (~2023). Bottom-up
inventories carry ~±5% (OECD-style reporting) to ~±10%+ (weaker statistical systems);
top-down atmospheric growth is measured to much better than that, and the reconciliation
of the two is a mature literature (global carbon budgets close to ~±5–10% on the fossil
term). Converting emitted carbon to primary energy uses fuel-mix emission factors —
another few percent. **Verdict: the fossil ~80% of P is readable today at ~±5–10%
without asking any single institution to be honest**, which through the damping table
is σ_K ≈ 0.002–0.004 from this channel alone.

**Trust residue (declared in paper §4, priced here).** The flux inference runs through
the sink partition — airborne fraction ~44%, ocean and land uptake from models — and
the O₂ book needs the ocean's seasonal breathing corrected. The models are public,
multiply and independently implemented, and fight each other in the open; the honest
label is *community-refereed, not oracle-free*. Distance to fully checkable: publishable
as a reproducible pipeline (public flask data → public sink ensembles → P̂ with spread);
the spread across independent sink models IS the honest error bar.

**Known partial forgeries and their catches.**
- Calcination (cement): ¹⁴C-dead CO₂, no O₂ draw → fails the oxygen book. Also small
  (~4% of CO₂) and endothermic — the forger pays energy to fake energy.
- Sequestration (CCS): hides the carbon entry, not the oxygen draw — capture takes
  the exhaust, never the intake. O₂ book records combustion regardless.
- Biomass burning: ¹⁴C-modern → provenance mark separates it from the seam.

---

## 2. Thermal channel — universal and not yet sensitive

**What it is.** All use terminates as heat (paper §3). Two readings: point-source
(plumes, flares, urban heat flux) and aggregate (net planetary radiative books).

**The aggregate gap, stated numerically.**
- Anthropogenic dissipation: 20 TW / 5.1×10¹⁴ m² ≈ **0.04 W/m²**.
- CERES-class absolute calibration: ~1 W/m²-scale; stability better (~0.2–0.3 W/m²/decade).
- Earth's energy imbalance (from Argo ocean heat content + CERES anomalies):
  ~1.0–1.3 W/m², resolved to ~±0.1–0.2 — but dominated by the greenhouse term,
  ~30× the direct-heat signal.
- **Verdict: the aggregate thermal reading is currently blind** — the direct-dissipation
  term is not separable from the radiative-forcing term at today's absolute accuracy.
  The permanent channel awaits either ~1–2 orders of magnitude in absolute radiometric
  accounting or slow accumulation in ocean heat content with the greenhouse term
  independently constrained. Decadal at best. Priced, not assumed.

**Point-source feasibility, existing.**
- VIIRS Nightfire: per-flare radiant wattage retrieved globally, nightly — an existing,
  operational, per-facility *involuntary* energy meter for gas flaring.
- Thermal imaging of plants: large stations' plumes and cooling signatures resolvable
  from orbit; Climate TRACE-style per-facility inventories fuse imagery + ML for
  power-sector output.
- Urban anthropogenic heat flux: measured city-scale in the literature (tens of W/m²
  locally — 3 orders above the global mean, hence measurable).
- **Verdict: thermal is attribution-grade at point sources today**, aggregate-blind;
  its role now is cross-checking claims, not carrying the denominator.

---

## 3. Nuclear channel — sharpest per joule, shortest reach

**Physics, fixed.** ~2×10²⁰ ν̄/s per GWth; spectrum producible only by fission;
unshieldable. τ = 1 by physics: to fake the flux is to run the reactor.

**Demonstrated capability.**
- Per-reactor monitoring at ~10 m–km: done (SONGS demonstration; PROSPECT-class
  short-baseline detectors).
- Fleet-scale at ~10²–10³ km: **KamLAND (1 kt scintillator, ~180 km flux-weighted
  baseline) watched the Japanese reactor fleet's antineutrino flux fall after the
  post-2011 shutdown — a nation's fleet power history read by one instrument with no
  cooperation from the nation.** This is the single strongest existing proof-of-concept
  for the paper's thesis and should be cited as such.
- Remote-monitoring lineage (WATCHMAN-style Gd-doped water Cherenkov): designed for
  exactly the noncooperative-reactor problem; scaling law is brutal (flux ~ r⁻²,
  detector mass compensates linearly) but the engineering direction exists.

**Verdict.** Fleet-aggregate fission power per region: feasible with kiloton-class
detectors and patience (statistics integrate). Global fission census by neutrino
alone: the genuine moonshot piece — not required for the denominator (fission ~4% of P;
misstating it entirely moves K by ~0.002) but the channel where the *unforgeability*
per joule is best, so worth carrying for the conjunction.

---

## 4. Structural channel — coverage for what burns nothing

**What it is.** Orbital census of capture infrastructure: utility-scale solar, wind,
hydro, thermal stations. The inward-axis channel; certifies capacity, not throughput.

**Existing.** Public Sentinel/Landsat imagery; published ML censuses of global
utility-scale solar; dam and reservoir registries verifiable from imagery + altimetry;
GRACE-class gravimetry for reservoir mass. Anyone can re-run the census — the artifact
answers every observer.

**The model tax.** Capacity → generation needs capacity factors (irradiance, wind
climatology, dispatch) — public and physical, but modelled. Distributed generation
(rooftop) partially visible at high resolution; the tail is genuinely hard.

**Verdict.** Renewable primary (~15% of P, growing): bound above today by visible
capacity × physical capacity-factor ceilings to ~±20–30%; through the damping table
that mis-measurement contributes σ_K ≲ 0.002. Acceptable now; **must improve as the
share grows** — this is the crossover problem, next.

---

## 5. The crossover problem

The paper's §7 decline, as a schedule. Channel coverage of P:

| Channel | now | mid-century (indicative) |
|---|---|---|
| Chemical (fossil) | ~80% | shrinking — that is the point of the century |
| Nuclear (ν̄) | ~4% | single digits–teens |
| Structural (renewables) | ~15% | plurality → majority |
| Thermal (aggregate) | blind | the intended successor |

The involuntary ledger is sharpest for the energy regime being exited. The meter's
composition must migrate: **chemical-led now → structural-led mid-century → thermal-led
whenever the aggregate instrument exists.** A denominator mechanism should therefore
publish its channel weights per epoch and re-derive them from coverage, not freeze them.
(Design note for any future mechanism paper: frozen weights are a proxy; proxies are
eaten.)

---

## 6. The attribution ladder

The paper's §5 split, rung by rung. Feasibility of *who generated what*:

1. **Planet** — oracle-free now (this whole document). The denominator.
2. **Nation/region** — semi-feasible, model-laden: atmospheric inversions with dense
   regional networks + Δ¹⁴C urban gradients (fossil), fleet ν̄ (fission), imagery census
   (renewables). Errors ~±10–20% for well-instrumented regions. The relocation attack
   is live here (imports, relabelling) but *bounded* by the residues: a nation cannot
   claim combustion its airshed did not see.
3. **Facility** — feasible for large point sources today (Nightfire flares in W;
   plant plumes; per-reactor ν̄ at kilometres; per-site methane from GHGSat-class).
   Not feasible for distributed sources.
4. **Agent** — not feasible from residues. This is where the meter, and the oracle,
   survive. **The minting problem stands**; the residue channels can audit an agent's
   claim against its facility's physics but cannot replace the claim.

The honest summary: residues *compress* the oracle from "trust the meter" to "trust
the meter only where the ladder's bottom rung requires it, and audit it from the rungs
above." A compression, not an elimination — same species of result as the chemical
channel's community-refereed model.

---

## 7. The program's own instruments, applied

- **Biconditional (Vol V):** thermal passes both halves by law; chemical passes
  completeness for combustion and soundness up to the calcination/sequestration cases,
  both caught by double-entry; ν̄ passes both for fission; structural fails soundness
  alone (capacity without flow) and is admitted only in conjunction. Consistent with
  the paper's §3.
- **Trace gap:** τ = 1 (thermal, ν̄, by identity/physics); τ ≈ 1 (chemical — forging
  both books + isotope mark ≈ doing combustion); τ < 1 (structural alone — Potemkin
  capacity costs construction, not generation; disciplined only by cross-channel
  absence of downstream dissipation). Note the pattern against *Sign and Work*: the
  channels with τ pinned at 1 are the ones where the residue is *generative* (the
  physics produces it in the making), not an output constraint. Same species as the
  §5.2 result there.
- **Independence:** four different physics (radiation / stoichiometry / weak
  interaction / persistence). The paper asserts independence qualitatively; a real
  mechanism paper should test error *correlation* between channels (shared satellites,
  shared reanalysis products are common-mode risks — e.g. imagery feeding both
  structural census and thermal point-source work). Flagged as open.

---

## 8. Staged program

- **Stage 0 (now, paper-grade):** compute K̂ from public inventories, cross-checked
  against atmospheric growth + APO; publish the reconciliation and the error budget;
  state P̂ with the spread across independent sink models as the error bar. Everything
  needed is public. This is a document, not an instrument.
- **Stage 1 (replication rule):** the denominator is *accepted* only when N independent
  groups/instruments agree within stated error — the coherence layer's actual use-case,
  with local readings as sections and physical samples as the anchors. (The sheaf gets
  to glue something real.)
- **Stage 2 (instrument gaps, fundable):** APO network densification; Δ¹⁴C urban
  networks; per-facility IR radiometry beyond flares; kiloton-class ν̄ monitoring at
  regional baselines.
- **Stage 3 (the thermal endgame, decadal):** absolute radiometric accounting or
  OHC-accumulation separation of the direct-heat term. The aggregate thermal
  instrument is the moonshot inside the moonshot; everything else above is engineering.

---

## 9. What would kill it

Falsifiers, so this document can be wrong:

1. **Sink-model divergence unbounded** — if independent carbon/O₂ sink models cannot be
   made to converge within the stated spread, the chemical channel's error bar is
   open-ended and Stage 0's reconciliation fails.
2. **Crossover outruns the structural channel** — if the renewable share grows faster
   than imagery-census + capacity-factor precision improves, the meter's coverage
   degrades mid-century with the thermal successor still blind.
3. **Channel errors correlate** — if the §7 independence test finds common-mode error
   (shared platforms, shared reanalyses), the conjunction's multiplication claim
   deflates toward the single-channel bound.
4. **A cheap chemical forgery** — a process producing ¹⁴C-dead CO₂ *with* the matching
   O₂ draw at cost ≪ combustion would break the double-entry τ ≈ 1 claim. None is
   known; one would be decisive.
5. **The storage term surprises** — if year-scale energy storage ever becomes
   non-negligible against the flow (large-scale synthetic fuel banking), the
   throughput = dissipation identity needs its storage line item promoted.

None of these is currently in evidence; 2 and 3 are the ones to watch.
