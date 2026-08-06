# code

Working examples for the *Derivation of Value* program.

The anthology's third volume argues that a claim about cost cannot be settled by
an essay, because the essay is written by the one making the claim and read by no
adversary — and that a test which could go red is a claim that has agreed, in
advance, to be refuted. This directory is where the program keeps that promise.
Everything here is runnable, seeded, and reproduces the figures quoted in the
prose. Where a measurement was wrong on the first pass, the correction is in the
code and named in the docstring rather than quietly repaired.

## Contents

| file | what it does |
|---|---|
| `complexes.py` | Substrate constructions and their Laplacians — sheaf and scalar. |
| `spectral_richness.py` | Measures richness ρ as a spectral dimension. Tests two conjectures; admits one, refutes the other. |
| `independence.py` | Puts an adversary in the loop and measures conditional fake-cost between projections (Definition 2.5). |
| `trace_gap.py` | Measures the trace gap τ = f/w (*Sign and Work* Def 3.3). Calibrates against two known answers, then puts a ceiling on τ for the coherence reading. |
| `temporal_iota.py` | The third attack design. Builds the epochs this directory said would be needed, and measures ι and τ together against a temporal projection. |

```
pip install -r requirements.txt
python spectral_richness.py
python independence.py
python trace_gap.py
python temporal_iota.py
```

Pure NumPy, no GPU, a few minutes on a laptop. Every figure is seeded, so the
numbers in the essays are the numbers these scripts print.

## What has been established, and what has not

`spectral_richness.py` put two conjectures to a machine.

**Admitted — richness is a fractional dimension.** The eigenvalue counting
function N(λ) of the sheaf Laplacian on a nested complex grows as a power law
with exponent d_s/2, d_s ≈ 1.61, converged in system size (n = 512 → 4096, scatter
falling 0.054 → 0.007) and fitting to R² ≈ 0.999. The exponent moves *continuously*
with coupling density — 1.26, 1.62, 1.82, 1.95, 2.12, 2.23 — passing through the
integers without pausing at them. So fractional richness is the generic case and
integer richness the measure-zero exception, and Definition 5.1's typing of ρ as
ℕ ∪ {∞} excludes almost everything.

**Refuted — there is no hierarchy of gaps.** The first pass appeared to find one
everywhere. It was an artefact: where many eigenvalues sit at the same height the
local spacing collapses, so any neighbouring gap is measured against nearly
nothing and scores enormous. Uncorrected, the gasket reported 74 gaps and the
coherent sheaf 67 — the latter being exactly its 3-fold stalk multiplicity, the
apparatus reporting itself as a property of the substrate. Corrected (see
`distinct_levels`), the nested complex shows at most one isolated gap against the
gasket's eighteen across five scales. Gap hierarchy tracks *exact geometric*
self-similarity, not nesting. **Gauge-Fixing §5's single measured spectral gap
therefore stands**, vindicated by the objection it survived.

## The adversarial result

`independence.py` puts a coalition in the loop and asks whether the spectral
dimension is independent of the kernel in the sense of Definition 2.5 — because a
projection that is not independent buys the mechanism nothing, however hard it
looks to counterfeit.

**Unstructured collusion is worthless.** A uniformly random coalition achieves
essentially nothing on either projection at any size below the whole network — at
f = 0.5 it reaches 1.4% of the honest kernel score. A random subset of a sparse
complex has almost no internal edges to agree along. The binding resource is not
coalition *size* but knowledge of the hierarchy: Definition 2.4's "rarer resource
of capability", showing up as the difference between an attack that does nothing
and one that works.

**Against a structure-aware coalition, the two projections move together.**
Colluding along the nesting rather than across it, kernel progress and dimension
progress track each other closely from f = 0.25 upward, and at the threshold where
a conjunction-gate would plausibly sit (τ = 0.5) ι ≈ 0 at every depth tested
(−0.14, −0.06, −0.04 for depths 9, 10, 11). Faking the kernel delivers the
spectral dimension for free. Nor does ι rise toward 1 with substrate depth, which
is what Definition 2.5 demands; at lower thresholds it is dominated by noise and
non-monotone.

The reason is visible in the numbers rather than inferred: d_s at f = 0.5 sits
almost exactly midway between its frustrated and honest values. The spectral
dimension is behaving as a volume-weighted average over coherent and incoherent
regions — which means that in a static snapshot it is measuring the *coherent
fraction of the substrate*, and so is the count of approximate sections. Two
instruments, one quantity. Hence ι ≈ 0.

**What this does and does not settle.** It does not refute §6, whose independence
claim rests on a distinction in time — agreeing at an instant versus sustaining
dynamical structure epoch over epoch — that a static sheaf cannot express. What it
settles is narrower and still useful: the static spectral dimension is *not* an
independent third projection, and the cheap route to a higher-order Combination
Proof is closed. If independence lives anywhere, it lives in the temporal
autocorrelations §6 already named, and nothing short of building them will do.

## The trace gap

`trace_gap.py` measures τ = f/w, the ratio of forging cost to earning cost. Before
this the program had one τ, measured on the unconstrained H⁰ projection, and it came
out at 0.

**The instrument can only overestimate.** f is a *minimum over an attacker class*
(Def 3.2) and this code minimises only over strategies someone wrote down. A strategy
nobody thought of is cheaper than every strategy here, so **measured τ ≥ true τ**,
always. A low τ is a real finding — it exhibits a forgery, and exhibiting one settles
the matter. A high τ is the absence of evidence. τ detects and does not certify,
which is the same shape as the cohomological invariant in *No Global Section*, and
was not anticipated when the file was started.

**Calibration.** Proof of work returns **τ = 1.054** against a known answer of 1
(400 trials, geometric search length, ~5% standard error). A signed claim of work
returns 1/w. The first pass returned **2.74** on proof of work, by comparing the
attacker's cost on a single search against the honest mean over eight; search length
has standard deviation equal to its mean, so one draw is not an expectation. The bug
is named in the docstring and kept, because the calibration specimen is the only
reason it was visible — the same estimator would otherwise have gone on to report
the coherence numbers below with nothing to indicate anything was wrong.

**One anchor buys nothing.** For the coherence reading, the forger's cheapest
accepted trace is *all frames equal* — a perfectly coherent, entirely contentless
configuration, at cost zero. Pinning one vertex does not change this, because the
coherent connection is gauge-invariant under R_v ↦ R_v Q: the forger rotates the
whole fiction to meet the anchor, for free. τ stays at 0. *A Consistent Fiction*
prices structural coupling at d scalars at one vertex, once — that closes the fiction
space, and it does **not** open a trace gap. Two different jobs at two different
prices, and the corpus had only costed the first.

**The ceiling, and it is below one.** With every vertex anchored, the forger still
never pays for a cycle: a spanning tree meets every vertex constraint, and the
cycle-closing edges are pure honest surplus. Measured across cycle ranks, exactly:

| cross-edges/merge | \|E\| | b₁ | measured τ | (n−1)/\|E\| |
|---|---|---|---|---|
| 1 | 255 | 0 | 1.0000 | 1.0000 |
| 2 | 359 | 104 | 0.7103 | 0.7103 |
| 3 | 463 | 208 | 0.5508 | 0.5508 |
| 5 | 618 | 363 | 0.4126 | 0.4126 |
| 8 | 803 | 548 | 0.3176 | 0.3176 |

So **τ ≤ 1 − b₁/|E|** for this reading, at any anchoring level. Equality at b₁ = 0 —
a tree — where a connection is coherent automatically because there is no cycle to
frustrate, and the score is therefore vacuous. **τ ≥ 1 and a non-vacuous coherence
score are incompatible.** Volume V's soundness clause is not merely unmet here; for
this reading it is unreachable, and the shortfall is exactly the cycle rank, which is
the thing that makes coherence mean anything.

Because the instrument overestimates τ, a negative result of this shape is the kind
it *can* establish: a cheaper forgery would only lower the ceiling.

**ρ and τ trade off on one knob.** Coupling density is a single parameter and both
quantities are functions of it. Same complex, both measured:

| cross-edges/merge | \|E\| | d_s | τ ceiling |
|---|---|---|---|
| 1 | 511 | 1.255 | 1.0000 |
| 2 | 733 | 1.693 | 0.6971 |
| 3 | 924 | 1.877 | 0.5530 |
| 5 | 1249 | 2.098 | 0.4091 |
| 8 | 1623 | 2.281 | 0.3148 |

The d_s column reproduces `spectral_richness`'s coupling sweep (1.26 … 2.23) and is
read as ordinal only — the plateau-spread diagnostic does not clear these as power
laws at n = 512. The τ column does not depend on it.

Via *Sign and Work* Prop 4.1, a gap of τ inflates the adversary's fleet by 1/τ. So
richness bought at the coupling knob is paid for in Sybil resistance: at
cross_per_merge = 8, an adversary 3.2× larger than the bound in *The Multiplicity
Freedom* assumes. **Richness and trace gap pull in opposite directions, and the
corpus has been maximising both.** *Requisite Richness* supplies ρ a floor from the
adversary; this supplies a ceiling from the same adversary, by a different route,
and substrate selection is squeezed from both sides.

### The anchor was modelled wrong, and the correction is the interesting part

Everything above anchors the **output**: publicly-known frames the configuration must
match. Gauge-Fixing §4.4 forbids an anchor cited as a certificate of order, and test
item (iv) says to check for exactly that. So the ceiling result is not a result about
Gauge-Fixing's mechanism. It is **§5 test (i) executed with anchor 4.3 removed**, and
it returns what §5 predicts — "generically it will admit them if any anchor is
removed" — with a price attached, which the paper does not have. Open problem 9 said
that test suite has no respondent. It now has a partial one.

The general principle the ceiling was the signature of:

> **Satisfying a public constraint is constraint satisfaction, never work.** τ derived
> from any *output* constraint is bounded by that constraint's satisfaction cost,
> which is structurally unrelated to its generation cost.

§4.3 constrains production instead: a slow sequentially dependent encoding keyed to
identity and beacon, applied *before* a section enters the sheaf — "H¹ is made to see
what it is natively blind to, not by strengthening the cohomology but by preparing its
inputs." `generative_specimen` models that. `rank` is how many of each frame's d
columns the world determines rather than the participant choosing; `encoding` is the
cost of producing one admissible section, which nobody escapes.

**Rank is a switch, not a dial.** Predicted before measuring: discontinuous at rank 1,
flat after, because the global gauge R_v ↦ R_v Q dies the moment any column is pinned
at *every* vertex. Measured, at encoding = 4:

| rank | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| τ | 0.0000 | 0.4874 | 0.4874 | 0.4874 |

Identical to four decimals for every rank ≥ 1. **Pinning one column at every vertex
buys the entire available gap; pinning more buys nothing.** The output-anchor sweep
climbed steadily with anchor count, so these are genuinely different objects and the
count sweep was the wrong coordinate.

**And τ < 1 strictly, at any encoding cost.** Sweeping the encoding at rank 1 tracks
n·E/(n·E + |E|·c) to four decimals:

| encoding | 0 | 1 | 4 | 16 | 64 | 256 | 1024 |
|---|---|---|---|---|---|---|---|
| τ | 0.0000 | 0.1920 | 0.4874 | 0.7918 | 0.9383 | 0.9838 | 0.9959 |

It approaches 1 and never arrives. The shortfall is exactly the reconciliation term —
the coherence content. So the two routes converge on one statement:

> **Coherence never contributes to the trace gap.** Whatever τ a mechanism has comes
> from its anchor; the coherence term appears only in the denominator. τ ≥ 1 is
> reachable only by driving the coherence contribution to zero — either b₁ = 0, where
> the score is vacuous, or encoding ≫ reconciliation, where the mechanism is measuring
> its anchor.

Volume V's soundness clause is not merely unmet by a coherence reading. It is
unreachable by one, and both derivations say the shortfall *is* the part that makes
coherence mean anything.

The ρ/τ trade-off survives the correction and gets cleaner: τ = n·E/(n·E + |E|·c) is
monotone decreasing in |E|, so richness costs trace gap under both anchor models.

**What this does not settle.** The honest cost model is the load-bearing assumption in
both halves — above, w proportional to edges reconciled; here, an honest surplus of
|E|·c on top of the encoding. If reconciliation is *redundant* once the world
determines the frames (at rank = d it arguably is), that surplus is double-counted and
τ rises. This is the joint to attack first. Note also that at high encoding the
"forger" has paid for every observation, which by Cor 3.5 means they did the work —
S&W §3's τ ≈ 1 regime behaving as described, not a failure of the model. One substrate
family throughout. And τ is a property of the *reading*: a mechanism scoring cycle
agreement directly, rather than reading dim ker off a spectrum, is not covered by any
of this and is the obvious place to look for a reading with a better gap.

## The third attack design

`independence.py` closed with a claim about what would be needed: independence, if it
lives anywhere, lives in the temporal autocorrelations, "and nothing short of building
them will do." `iota_asymmetry.py` then failed twice to move d_s on a static complex —
sparsification shatters, rewiring is too weak. `temporal_iota.py` builds the epochs
instead of attacking the snapshot harder, and it works: both attacks move their own
target and leave the other alone, which is what neither previous design achieved.

**The projections.** π_ker is the usual #{λ < ε}. **π_persist** is the overlap between
the bottom-k eigenspaces of consecutive epochs — the normalised sum of squared cosines
of the principal angles, so 1 for an unchanged subspace, basis-independent, and always
defined. Honest frames *drift*, so honest persistence is below 1 by construction.

**The attacks.** *C* makes a coalition coherent each epoch and redraws its frames every
epoch: targets π_ker. *P* freezes the coalition's own restriction maps after the first
epoch and never makes them coherent: targets π_persist. The coalition is never made
coherent under *P* — it merely never changes its mind.

| attack | f | π_ker | π_persist | ker prog | persist prog |
|---|---|---|---|---|---|
| C | 0.25 | 6.00 | 0.0594 | 0.333 | 0.240 |
| C | 0.50 | 9.00 | 0.0408 | 0.500 | 0.070 |
| C | 0.75 | 15.00 | 0.0308 | 0.833 | −0.022 |
| P | 0.25 | 0.00 | 0.2158 | 0.000 | **1.672** |
| P | 0.50 | 0.00 | 0.2944 | 0.000 | **2.391** |
| P | 0.75 | 0.00 | 0.6096 | 0.000 | **5.277** |

**ι(ker \| persist) = 1.000** at every coalition size. Faking persistence delivers
*nothing* toward the kernel. This is the first solid measurement in this direction —
the program had only ι(dim \| ker) = 0.08 — and it is the answer `independence.py`
predicted would require epochs to obtain.

**ι(persist \| ker) = 0.723**, but the samples run 0.28, 0.86, 1.03 across attack
intensity, a spread of 0.75. **It is not a constant.** CP §7.1 treats ι as a scalar
parameter and *The Multiplicity Freedom*'s T2 uses it as one in Γ = γ(1 + (K−1)ι); on
three data points with a monotone trend that is suggestive rather than established, but
it is the first evidence that ι may not be well-defined independently of the attack
that measures it. The asymmetry, 0.277, clears the 0.15 threshold `iota_asymmetry.py`
set: **on this pair the right object is a divergence, not a metric**, and P6's Fisher
route must carry the asymmetry rather than quotient it away.

**The absurdity fired, and it was built to.** Honest models update, so honest
persistence is 0.1425; a coalition that changes nothing reaches 0.6096, which is
**5.3× the honest progress**. Progress above the honest maximum is the same species of
impossible number that caught the sparsification attack and the gap hierarchy — except
here it is the hypothesis under test rather than a bug. A projection that rewards
stasis is one an adversary wins by doing nothing.

*(The first version of this attack froze the entire Laplacian rather than the
coalition's own edges, handing the adversary the whole substrate. The tell was that the
result did not vary with coalition size. Corrected in place and named in the
docstring.)*

**The finding is the conjunction, not either half.** π_persist is independent of the
kernel *and* free to forge — τ(π_persist) ≈ 0, since holding still costs nothing and
outscores honest updating. So:

> **Independence was never the binding constraint.** CP §7.1 has been treated as the
> hard part of admitting a third projection. On this evidence τ is the hard part, and
> the search for a third projection has been running under one of the two requirements.

The conjecture this suggests, on two data points and therefore weak: **ι and τ pull
against each other.** A projection independent of coherence is one coherence does not
constrain, and a projection coherence does not constrain is one an adversary can
satisfy without doing coherence work. The static spectral dimension failed on ι and
inherited coherence's τ; the temporal projection passes ι and has no τ at all. If the
tension is real, substrate selection is constrained on a third axis as well as the two
that `trace_gap.py` found.

## Two disciplines this code tries to keep

**Calibrate the instrument before trusting it.** A method that reads a dimension
off a spectrum is worth nothing until it returns known answers to known questions.
So it is pointed first at a Sierpiński gasket, whose spectral dimension is
2·log3/log5 ≈ 1.365, and a square lattice, whose dimension is exactly 2. It returns
1.392 and 2.098. Only then is it turned on anything unknown.

**Do not smuggle the answer into the question.** The nested complex is a
hierarchical modular network — self-similar in its *construction rule* only. It is
deliberately not a geometric fractal. Had it been one, any anomalous dimension
found in it would have been placed there by the experimenter.

A third discipline is worth stating because this code does not yet keep it: a high
R² is not evidence of a power law. The Erdős–Rényi control fits at R² ≈ 0.97 and
has no spectral dimension at all. The diagnostic that catches it is the *plateau
spread* of the local logarithmic derivative, which is reported alongside every fit.

## Limits

A toy complex is not a deployed one. The nesting is a hypothesis about coherence
networks, built in by hand here rather than observed in a running network. The
incoherent case is made incoherent crudely, by randomising frames, where a real
adversary would be quieter and cleverer. None of this touches the
Goodhart-asymptotic security claim, which still waits on a mechanism and an
opponent.

## License

CC BY 4.0, as with the rest of the program.
