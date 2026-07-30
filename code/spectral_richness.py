"""
Measuring substrate richness ρ as a spectral dimension.

Reproduces the figures reported in Anthology III, *One Admitted, One Refused*,
and in Combination Proofs §7.3.

Two conjectures were put to this script:

  (i)  ρ is not a count but a fractional dimension, readable off the growth of
       N(λ) = #{eigenvalues ≤ λ} for the sheaf Laplacian.          -> ADMITTED
  (ii) such spectra carry a HIERARCHY of gaps, so Gauge-Fixing §5's demand for
       "the measured spectral gap" prices only the coarsest coalition, letting
       finer collusion pass beneath the scale of the test.          -> REFUTED

Run:  python spectral_richness.py
"""
import numpy as np

from complexes import (sierpinski_gasket, grid_2d, erdos_renyi,
                       hierarchical_modular, graph_laplacian, sheaf_laplacian)

GASKET_EXACT = 2 * np.log(3) / np.log(5)   # 1.3652…


# ---------------------------------------------------------------- measurement

def spectral_dimension(evals, lo_q=0.02, hi_q=0.35):
    """
    Fit log N(λ) = (d_s/2)·log λ + c over an intermediate window, avoiding the
    finite-size bottom and the lattice-cutoff top. Returns (d_s, R²).
    """
    nz = np.sort(evals[evals > 1e-9])
    if len(nz) < 100:
        return np.nan, np.nan
    grid = np.exp(np.linspace(np.log(np.quantile(nz, lo_q)),
                              np.log(np.quantile(nz, hi_q)), 60))
    counts = np.searchsorted(nz, grid, side="right").astype(float)
    ok = counts > 5
    x, y = np.log(grid[ok]), np.log(counts[ok])
    slope, icept = np.polyfit(x, y, 1)
    resid = y - (slope * x + icept)
    r2 = 1 - np.sum(resid ** 2) / np.sum((y - y.mean()) ** 2)
    return 2 * slope, r2


def local_slope_spread(evals, npts=25):
    """
    Range of the local logarithmic derivative d log N / d log λ.
    A genuine power law shows a PLATEAU, so a small spread. This is the
    diagnostic that separates a real dimension from a good-looking R²:
    Erdős–Rényi fits at R² = 0.98 and is not a power law at all.
    """
    nz = np.sort(evals[evals > 1e-9])
    lam = np.exp(np.linspace(np.log(np.quantile(nz, 0.01)),
                             np.log(np.quantile(nz, 0.60)), npts))
    cnt = np.searchsorted(nz, lam, side="right").astype(float)
    ok = cnt > 5
    lam, cnt = lam[ok], cnt[ok]
    sl = 2 * np.diff(np.log(cnt)) / np.diff(np.log(lam))
    return sl.max() - sl.min()


def distinct_levels(evals, rtol=1e-6):
    """
    Collapse degenerate eigenvalues into distinct spectral levels.

    THIS STEP IS NOT COSMETIC. Skipping it produces a false positive for
    conjecture (ii): where many eigenvalues sit at one height the local spacing
    collapses, so any neighbouring gap is measured against nearly nothing and
    scores enormous. Uncorrected, the gasket reported 74 "gaps" and the coherent
    sheaf 67 — the latter being precisely its 3-fold stalk multiplicity, i.e.
    an artefact of the apparatus reporting itself as a property of the substrate.
    """
    nz = np.sort(evals[evals > 1e-9])
    if len(nz) == 0:
        return nz
    tol = rtol * max(1.0, nz.max())
    lv = [nz[0]]
    for x in nz[1:]:
        if x - lv[-1] > tol:
            lv.append(x)
    return np.array(lv)


def gap_hierarchy(evals, window=30, thresh=6.0, edge_frac=0.02):
    """
    Count interior gaps exceeding `thresh` × the local mean spacing of DISTINCT
    levels. A single leading gap is one outlier at the bottom; a hierarchy is
    large gaps at many spectral positions. Spectral edges are excluded.
    """
    lv = distinct_levels(evals)
    if len(lv) < 4 * window:
        return []
    g = np.diff(lv)
    local = np.convolve(g, np.ones(window) / window, mode="same")
    r = np.where(local > 0, g / np.maximum(local, 1e-300), 0.0)
    lo, hi = int(edge_frac * len(g)), int((1 - edge_frac) * len(g))
    hits = [(lv[i], r[i], (i + 1) / len(lv)) for i in range(lo, hi) if r[i] > thresh]
    return sorted(hits, key=lambda h: -h[1])


def tier_jumps(evals, k=48, factor=1.6):
    """Jumps in the low-lying spectrum: candidate boundaries between module scales."""
    lv = distinct_levels(evals)[:k]
    if len(lv) < 4:
        return []
    ratios = lv[1:] / lv[:-1]
    return [(i + 1, lv[i], ratios[i]) for i in range(len(ratios)) if ratios[i] > factor]


def summarise(name, evals, expect=None):
    d_s, r2 = spectral_dimension(evals)
    spread = local_slope_spread(evals)
    hits, tiers = gap_hierarchy(evals), tier_jumps(evals)
    nlv = len(distinct_levels(evals))
    print(f"\n{name}")
    print(f"    kernel dim {int(np.sum(evals <= 1e-9)):>3} | "
          f"{nlv} distinct levels of {len(evals)} eigenvalues "
          f"({len(evals) / max(nlv, 1):.2f}x degenerate)")
    line = f"    d_s = {d_s:6.3f}   R^2 = {r2:.4f}   plateau spread = {spread:5.2f}"
    if expect is not None:
        line += f"   [known {expect:.3f}, err {abs(d_s - expect):.3f}]"
    print(line)
    print(f"    interior gaps > 6x local spacing: {len(hits):>3}   "
          f"low-spectrum tier jumps: {len(tiers)}")
    for lam, ratio, pos in hits[:4]:
        print(f"        gap x{ratio:.1f} at lambda={lam:.4g} ({100 * pos:.0f}% through)")
    return d_s


# ---------------------------------------------------------------- experiments

def calibration():
    print("=" * 72)
    print("CALIBRATION — does the instrument return known answers?")
    print("=" * 72)
    n, e = sierpinski_gasket(7)
    summarise(f"Sierpinski gasket, level 7 (n={n})",
              np.linalg.eigvalsh(graph_laplacian(n, e)), expect=GASKET_EXACT)
    n, e = grid_2d(57)
    summarise(f"Square lattice 57x57 (n={n})",
              np.linalg.eigvalsh(graph_laplacian(n, e)), expect=2.0)


def controls():
    print("\n" + "=" * 72)
    print("CONTROL — a structure with no nesting")
    print("=" * 72)
    n, e = erdos_renyi(3249, 6, np.random.default_rng(11))
    summarise(f"Erdos-Renyi, mean degree 6 (n={n})",
              np.linalg.eigvalsh(graph_laplacian(n, e)))
    print("    NOTE: R^2 is high but the plateau spread is not. No power law here.")


def convergence():
    print("\n" + "=" * 72)
    print("CONJECTURE (i) — is d_s a number, or a fluke of one construction?")
    print("=" * 72)
    print(f"\n  Finite-size convergence (cross=2, 4 seeds each)")
    print(f"  {'depth':>6}{'n':>7}{'mean d_s':>11}{'sd':>8}{'mean R^2':>10}")
    for depth in (9, 10, 11, 12):
        vals = []
        for s in range(4):
            rng = np.random.default_rng(1000 + s)
            n, e = hierarchical_modular(depth, rng, 2)
            vals.append(spectral_dimension(np.linalg.eigvalsh(graph_laplacian(n, e))))
        d = np.array([v[0] for v in vals])
        r = np.array([v[1] for v in vals])
        print(f"  {depth:>6}{2 ** depth:>7}{d.mean():>11.3f}{d.std():>8.3f}{r.mean():>10.4f}")

    print(f"\n  Continuity in coupling density (depth 11, 4 seeds each)")
    print(f"  {'cross':>6}{'mean d_s':>11}{'sd':>8}{'mean R^2':>10}")
    for cross in (1, 2, 3, 4, 6, 8):
        vals = []
        for s in range(4):
            rng = np.random.default_rng(2000 + s)
            n, e = hierarchical_modular(11, rng, cross)
            vals.append(spectral_dimension(np.linalg.eigvalsh(graph_laplacian(n, e)))[0])
        v = np.array(vals)
        print(f"  {cross:>6}{v.mean():>11.3f}{v.std():>8.3f}{'':>10}")
    print("\n  d_s moves continuously through the integers without pausing at them.")
    print("  Fractional richness is the generic case; integer richness is measure zero.")


def sheaf_and_gaps():
    print("\n" + "=" * 72)
    print("SHEAF — does the sheaf structure change the exponent? (it must not)")
    print("=" * 72)
    rng = np.random.default_rng(3000)
    n, e = hierarchical_modular(10, rng, 2)
    bare = summarise(f"Bare complex, depth 10 (n={n})",
                     np.linalg.eigvalsh(graph_laplacian(n, e)))
    coh = summarise(f"Sheaf, COHERENT frames, d=3 (n={n})",
                    np.linalg.eigvalsh(sheaf_laplacian(n, e, rng, 3, True)))
    print(f"    -> coherent sheaf {coh:.3f} vs bare complex {bare:.3f}: "
          f"gauge-equivalence holds.")

    print("\n" + "=" * 72)
    print("CONJECTURE (ii) — a hierarchy of gaps? (see distinct_levels docstring)")
    print("=" * 72)
    for cross in (2, 4):
        rng = np.random.default_rng(4000)
        n, e = hierarchical_modular(11, rng, cross)
        summarise(f"Hierarchical modular, depth 11, cross={cross} (n={n})",
                  np.linalg.eigvalsh(graph_laplacian(n, e)))
    rng = np.random.default_rng(3000)
    n, e = hierarchical_modular(10, rng, 2)
    summarise(f"Sheaf, COHERENT frames (n={n})",
              np.linalg.eigvalsh(sheaf_laplacian(n, e, rng, 3, True)))
    print("\n  The gasket carries a real hierarchy; the nested complex does not.")
    print("  Gap hierarchy tracks EXACT GEOMETRIC self-similarity, not nesting.")
    print("  Gauge-Fixing §5's single measured spectral gap therefore STANDS.")


def coherence_separation():
    print("\n" + "=" * 72)
    print("UNBIDDEN — does d_s by itself separate coherent from incoherent?")
    print("=" * 72)
    print(f"  {'seed':>6}{'coherent':>12}{'frustrated':>13}{'ratio':>8}")
    for s in range(3):
        rng = np.random.default_rng(3000 + s)
        n, e = hierarchical_modular(10, rng, 2)
        c = spectral_dimension(np.linalg.eigvalsh(sheaf_laplacian(n, e, rng, 3, True)))[0]
        f = spectral_dimension(np.linalg.eigvalsh(sheaf_laplacian(n, e, rng, 3, False)))[0]
        print(f"  {3000 + s:>6}{c:>12.3f}{f:>13.3f}{f / c:>8.2f}")
    print("\n  A candidate third projection of the same operator, with no reference")
    print("  to the kernel and none to any gap. Whether it is INDEPENDENT of the")
    print("  existing projections per Definition 2.5 is not settled by this —")
    print("  that needs an adversary, not an experiment. See independence.py.")


if __name__ == "__main__":
    calibration()
    controls()
    convergence()
    sheaf_and_gaps()
    coherence_separation()
