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

```
pip install -r requirements.txt
python spectral_richness.py
python independence.py
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
