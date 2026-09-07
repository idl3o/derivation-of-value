"""
Every basis at once: the world as hidden variable, and the cover the beacon
draws.

READING TWO of the "quantum-style measurement basis" question: choose the
contexts after the participants commit, so that a fiction cannot be
consistent in every basis. Two things are true at once and the second
corrects the first.

  COMMITMENT MAKES EVERY PARTICIPANT NON-CONTEXTUAL. A committed section is
  one assignment; its restrictions to every context glue by construction;
  there is no basis in which a committed fiction is inconsistent with
  itself. Contextuality — local sections with no global one — can appear
  only where commitment is absent and a participant answers each context
  separately. The participant who does that is the ADAPTIVE COPIER: it
  answers each partner with that partner's revealed data, so its answers
  on one prompt differ across partners. In the vocabulary of the
  contextuality papers that is SIGNALLING: its marginal on a prompt
  depends on the context. An exact self-consistency gate — the same
  answer on the same prompt to every partner — refuses it at no cost to
  honesty, whose answers come from one derivation. But the copier that
  self-consistency leaves standing is the AVERAGING copier, one estimate
  from every revealed source, and One's Own Anchor §5 measured that one
  passing with a residual BELOW honest's. The no-signalling test removes
  the copier regime (a) never needed and leaves the one it did.

  WHAT "BASIS AFTER COMMITMENT" BUYS IS THE COVER. If the beacon draws the
  overlap graph each epoch — which pairs compare data — a coalition's
  boundary is no longer the two-to-four cross-edges of its block but a
  random cut, in expectation |E|·2|C|(n−|C|)/(n(n−1)), which GROWS with
  the coalition. That is the expansion purchase The Budget Across Levels
  §9.1 and One's Own Anchor §9.4 left open, and it has a price the corpus
  can measure: the hierarchical complex was chosen for its spectral
  dimension (Requisite Richness), and a redrawn cover has none.

THE INSTRUMENT.
  Part 1 — the three copiers on the seed-7 complex with shared prompts:
    honest, averaging, adaptive. Self-consistency spread (largest RMS
    difference between a member's answers on the same prompt to two
    partners) and boundary residual.
  Part 2 — the cover redrawn: a fraction f of the complex's edges rewired
    degree-preservingly each epoch, beacon-keyed, so every participant
    keeps its number of overlaps and only who it overlaps with changes;
    block-coalition boundaries, per-identity native cost, lambda_2 and the
    spectral-dimension fit of Requisite Richness, for f in {0, 1/8, 1/4,
    1/2, 1}.
  Part 3 — the residual reading run at f = 1 for the block of 128, commit
    regime above the step: the stale coalition fails, the deriving one
    passes at the random cut's price.

PREDICTIONS, STATED BEFORE RUNNING.
  1. Part 1: honest spread exactly 0; averaging copier spread 0 and
     residual (sigma/sqrt k)·sqrt(1 − 1/b)·sqrt(1 − 1/m), below honest's
     ≈ 0.205 at every b > 1 (One's Own Anchor §5 reproduced); adaptive
     copier spread at the honest noise level, ≈ 0.2, and residual ≈ 0.
     An exact self-consistency gate refuses the adaptive copier and passes
     the averaging one.
  2. Part 2 at f = 0 reproduces the first blocks' boundaries 3, 2, 3, 2
     and the block means 3.75, 3.5, 3.0, 2.0. At f = 1 the mean boundary
     is the random-cut formula, 43.6 / 81.5 / 139.7 / 186.2 at |C| = 16 /
     32 / 64 / 128 within sampling, so the per-identity native cost is
     174 / 163 / 140 / 93 against 186 for an honest vertex: the cap is
     restored to between half and all of honest. The boundary is LINEAR
     in f. lambda_2 is CONCAVE in f, most of its rise by f = 1/8 (the
     small-world effect). The spectral-dimension fit degrades with f: R²
     falls and the slope leaves the 1.6 of the fixed complex — richness
     as spectral dimension is lost as the coalition price is gained.
  3. Part 3: at f = 1 the stale coalition of 128 fails every epoch, the
     deriving coalition passes at k·m·|∂C_t| per epoch, and its evidencing
     share is about one half.

FIRST PASS, recorded. The cover was first redrawn by replacing edges with
uniformly random pairs; at f = 1/4 and above that disconnected the graph
(a sparse random graph with mean degree 2.9 has isolated vertices), so
lambda_2 read exactly zero and measured nothing, and Part 1's block of
128 on the fixed cover had two boundary members with one partner each, so
the copiers could not differ. Both are design errors, not findings: the
beacon's cover should keep every participant's number of overlaps — a
degree-preserving rewiring — and the copiers must be compared where a
member has several partners, which the redrawn cover supplies. A second
pass rewired by random swaps and left a third of the edges untouched at
f = 1 (a swap can hit an edge twice), so the boundaries came in at two
thirds of the random-cut formula; the rewiring now re-pairs the stubs of
exactly the chosen edges. lambda_2 is reported on the largest component,
since a rewired cover occasionally splits off a pair. The predictions
above stand as stated; the instrument is what changed.

WHAT CAME BACK (recorded after the third run; the predictions above are as
stated before the first). 1 held: honest spread 0.0000, residual 0.2073;
averaging copier spread 0.0000, residual 0.0815, below honest, passing the
self-consistency gate; adaptive copier spread 0.2665, residual 0.0000,
refused. 2 held: f = 0 reproduces 3/2/3/2 and 3.8/3.5/3.0/2.0; f = 1 gives
43.6 / 80.9 / 139.2 / 191.0 against the formula's 43.6 / 81.5 / 139.7 /
186.2, and the per-identity cost of the block of 128 rises from 1.0 to
95.5 against honest's 186; the boundary is linear in f (22.8, 49.0, 90.2,
191.0 at f = 1/8, 1/4, 1/2, 1 for the block of 128); lambda_2 of the
giant component rises thirteenfold by f = 1/8 (0.0038 to 0.049) and then
flattens (0.083, 0.107, 0.102); the spectral dimension leaves 1.68 for
2.06, 2.28, 2.41, 2.56 with R² falling from 0.996 to 0.975, and at
n = 1024 from 1.59 to 2.02 at f = 1/8 and 2.58 at f = 1. 3 held: the
stale coalition fails every epoch, the deriving one passes at the random
cut's price, e(C) = 0.518, 95.9 per identity per epoch against 186.

Run:  python every_basis.py     (seeded; every number reproducible; ~10 s)
"""
import sys
import numpy as np
from complexes import hierarchical_modular, random_orthogonal
from spectral_richness import spectral_dimension
from evidencing import (D, M, SIGMA, K, TOL, HONEST_SEED, COALITION_SEED,
                        FRAME_SEED, world_path, edge_columns,
                        procrustes_residual, honest_pair, boundary,
                        coalition_sections, estimate_from_record)
from holarchy import derive_edges
from exclusion import DEPTH, EPOCHS

BEACON_COVER = 50_000
FRACTIONS = (0.0, 0.125, 0.25, 0.5, 1.0)
BLOCKS = (16, 32, 64, 128)
DELTA_UNITS = 3.0


# --------------------------------------------------------------- cover

def base_cover(depth=DEPTH):
    n, edges = hierarchical_modular(depth, np.random.default_rng(7),
                                    cross_per_merge=2)
    return n, edges


def redraw(n, edges, frac, rng):
    """The cover the beacon draws this epoch: degree-preserving rewiring of
    exactly a fraction frac of the edges. The chosen edges' endpoints are
    pooled, shuffled and re-paired, and any loop or duplicate is repaired
    by swapping one of its stubs with a random other stub, so every
    participant keeps its number of overlaps and only WHO it overlaps with
    changes. |E| is kept."""
    edges = list(edges)
    k = int(round(frac * len(edges)))
    if k < 2:
        return edges
    chosen = sorted(int(i) for i in rng.choice(len(edges), size=k,
                                               replace=False))
    fixed = {edges[i] for i in range(len(edges)) if i not in set(chosen)}
    stubs = [x for i in chosen for x in edges[i]]
    stubs = [stubs[j] for j in rng.permutation(len(stubs))]

    def pairs():
        return [(min(stubs[2 * j], stubs[2 * j + 1]),
                 max(stubs[2 * j], stubs[2 * j + 1])) for j in range(k)]

    for _ in range(200 * k):
        new = pairs()
        bad = [j for j, e in enumerate(new)
               if e[0] == e[1] or e in fixed or new.count(e) > 1]
        if not bad:
            break
        j = bad[int(rng.integers(len(bad)))]
        x, y = 2 * j + int(rng.integers(2)), int(rng.integers(len(stubs)))
        stubs[x], stubs[y] = stubs[y], stubs[x]
    for i, e in zip(chosen, pairs()):
        edges[i] = e
    return edges


def components(n, edges):
    """Number of components, and the vertices of the largest."""
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        parent[find(u)] = find(v)
    groups = {}
    for v in range(n):
        groups.setdefault(find(v), []).append(v)
    giant = max(groups.values(), key=len)
    return len(groups), giant


def giant_gap(n, edges):
    """lambda_2 of the largest component's Laplacian."""
    _, giant = components(n, edges)
    idx = {v: i for i, v in enumerate(giant)}
    sub_edges = [(idx[u], idx[v]) for u, v in edges if u in idx and v in idx]
    return float(np.linalg.eigvalsh(graph_laplacian(len(giant), sub_edges))[1])


def graph_laplacian(n, edges):
    L = np.zeros((n, n))
    for u, v in edges:
        L[u, u] += 1
        L[v, v] += 1
        L[u, v] -= 1
        L[v, u] -= 1
    return L


def random_cut(n, m_edges, size):
    return m_edges * 2 * size * (n - size) / (n * (n - 1))


# ------------------------------------------------- part 1: three copiers

def _world_and_frames(n, m_total):
    G = np.random.default_rng(BEACON_COVER).normal(size=(D, m_total))
    frames = [random_orthogonal(D, np.random.default_rng(FRAME_SEED + v))
              for v in range(n)]
    return G, frames


def _honest_world_values(G, k, rng, n, sigma=SIGMA):
    """Each vertex's derivation in world coordinates: G plus its own noise."""
    noise = sigma / np.sqrt(k)
    return [G + noise * rng.normal(size=G.shape) for _ in range(n)]


def _copier_answers(u, partners, Y, mode, rng):
    """Member u's answer to each partner, in world coordinates.
    honest: its own derivation; averaging: the mean of the partners'
    revealed derivations, the same to everyone; adaptive: each partner's
    own derivation, copied."""
    if mode == "honest":
        return {v: Y[u] for v in partners}
    if mode == "averaging":
        mean = np.mean([Y[v] for v in partners], axis=0)
        return {v: mean for v in partners}
    return {v: Y[v] for v in partners}


def part_one_copiers():
    print("=" * 74)
    print("PART 1 — THREE COPIERS: self-consistency and the boundary"
          " residual")
    print("=" * 74)
    n, edges0 = base_cover()
    edges = redraw(n, edges0, 1.0, np.random.default_rng(BEACON_COVER))
    G, frames = _world_and_frames(n, M)
    rng = np.random.default_rng(HONEST_SEED)
    Y = _honest_world_values(G, K, rng, n)
    C = set(range(128))
    _, bd = boundary(edges, C)
    partners = {}
    for i in bd:
        u, v = edges[i]
        cu, hv = (u, v) if u in C else (v, u)
        partners.setdefault(cu, []).append(hv)
    multi = sum(1 for vs in partners.values() if len(vs) > 1)
    print(f"  block of 128 on the redrawn cover: {len(bd)} boundary edges,"
          f" {len(partners)} boundary members, {multi} with several partners")
    print(f"  {'strategy':<12}{'spread':>9}{'residual':>10}{'honest r':>10}"
          f"{'self-consistent':>17}")
    honest_r = None
    for mode in ("honest", "averaging", "adaptive"):
        spreads, res = [], []
        for cu, vs in partners.items():
            ans = _copier_answers(cu, vs, Y, mode, rng)
            for a in range(len(vs)):
                for b in range(a + 1, len(vs)):
                    spreads.append(np.sqrt(np.mean((ans[vs[a]] - ans[vs[b]])
                                                   ** 2)))
            A = np.stack([frames[cu].T @ ans[v] for v in vs])
            B = np.stack([frames[v].T @ Y[v] for v in vs])
            res.extend(procrustes_residual(A, B))
        spread = max(spreads) if spreads else 0.0
        r = float(np.mean(res))
        if mode == "honest":
            honest_r = r
        ok = "y" if spread < 1e-12 else "N"
        print(f"  {mode:<12}{spread:>9.4f}{r:>10.4f}{honest_r:>10.4f}{ok:>17}")
    print("  Honest answers come from one derivation and spread nothing.")
    print("  The adaptive copier signals, a different answer to each partner,")
    print("  and an exact self-consistency gate refuses it. The averaging")
    print("  copier is self-consistent and sits below honest's residual.")


# ------------------------------------------- part 2: the cover redrawn

def _block_boundaries(n, edges, size):
    out = []
    for start in range(0, n, size):
        C = set(range(start, start + size))
        _, bd = boundary(edges, C)
        out.append(len(bd))
    return out


def _curve_point(n, edges0, frac):
    """Over the epochs' beacon-drawn covers: mean block boundaries, first
    block boundaries, lambda_2, spectral dimension and its fit."""
    means = {s: [] for s in BLOCKS}
    firsts = {s: [] for s in BLOCKS}
    lam2, ds, r2, comps = [], [], [], []
    for t in range(EPOCHS):
        rng = np.random.default_rng(BEACON_COVER + t)
        edges = redraw(n, edges0, frac, rng) if frac > 0 else list(edges0)
        for s in BLOCKS:
            bds = _block_boundaries(n, edges, s)
            means[s].append(np.mean(bds))
            firsts[s].append(bds[0])
        ev = np.linalg.eigvalsh(graph_laplacian(n, edges))
        lam2.append(giant_gap(n, edges))
        comps.append(components(n, edges)[0])
        d, r = spectral_dimension(ev)
        ds.append(d)
        r2.append(r)
    return means, firsts, float(np.mean(lam2)), float(np.nanmean(ds)), \
        float(np.nanmean(r2)), float(np.mean(comps))


def part_two_curve():
    print("\n" + "=" * 74)
    print("PART 2 — THE COVER REDRAWN: boundary, price, gap and dimension"
          " against f")
    print("=" * 74)
    n, edges0 = base_cover()
    m_edges = len(edges0)
    print(f"  n = {n}, |E| = {m_edges}; random-cut expectation at |C| ="
          f" {BLOCKS}: "
          + ", ".join(f"{random_cut(n, m_edges, s):.1f}" for s in BLOCKS))
    print(f"  {'f':>6}{'|dC| 16':>9}{'32':>7}{'64':>7}{'128':>7}"
          f"{'first blocks':>14}{'per id 128':>11}{'lambda_2':>10}"
          f"{'comp':>6}{'d_s':>7}{'R²':>7}")
    for frac in FRACTIONS:
        means, firsts, l2, d, r, cp = _curve_point(n, edges0, frac)
        mb = [np.mean(means[s]) for s in BLOCKS]
        fb = "/".join(f"{np.mean(firsts[s]):.0f}" for s in BLOCKS)
        per_id = K * M * mb[-1] / 128
        print(f"  {frac:>6.3f}{mb[0]:>9.1f}{mb[1]:>7.1f}{mb[2]:>7.1f}"
              f"{mb[3]:>7.1f}{fb:>14}{per_id:>11.1f}{l2:>10.4f}{cp:>6.1f}"
              f"{d:>7.2f}{r:>7.3f}")
    print(f"  honest native cost per vertex ≈"
          f" {K * M * 2 * m_edges / n:.0f}; a per-identity cost near it is a"
          f" cap restored")
    print("  The boundary is linear in f and lambda_2 is not; the spectral-")
    print("  dimension fit that Requisite Richness measured leaves as the")
    print("  cover is redrawn. Expansion and richness are the same purchase")
    print("  with opposite signs.")
    n1, e1 = base_cover(DEPTH + 2)
    for frac in (0.0, 0.125, 1.0):
        rng = np.random.default_rng(BEACON_COVER)
        edges = redraw(n1, e1, frac, rng) if frac > 0 else e1
        ev = np.linalg.eigvalsh(graph_laplacian(n1, edges))
        d, r = spectral_dimension(ev)
        print(f"  n = {n1}, f = {frac:.3f}: lambda_2 (giant) ="
              f" {giant_gap(n1, edges):.4f}, d_s = {d:.2f}, R² = {r:.3f}")


# ------------------------------------- part 3: the reading at f = 1

def part_three_reading():
    print("\n" + "=" * 74)
    print("PART 3 — THE RESIDUAL READING ON THE REDRAWN COVER, |C| = 128,"
          " f = 1")
    print("=" * 74)
    n, edges0 = base_cover()
    m_edges = len(edges0)
    cols, m_total = edge_columns(edges0, shared=False)
    delta = DELTA_UNITS * SIGMA / np.sqrt(K)
    G = world_path(m_total, delta)
    _, frames = _world_and_frames(n, m_total)
    rng = np.random.default_rng(HONEST_SEED)
    crng = np.random.default_rng(COALITION_SEED)
    C = set(range(128))
    record = None
    cost, w_C = 0.0, 0.0
    print(f"  {'epoch':>6}{'|dC_t|':>8}{'honest r':>10}{'stale r':>9}"
          f"{'stale':>7}{'derived':>9}{'cost':>8}")
    for t in range(EPOCHS):
        edges = redraw(n, edges0, 1.0,
                       np.random.default_rng(BEACON_COVER + t))
        A, B = honest_pair(edges, cols, G[t], frames, K, rng)
        inside, bd = boundary(edges, C)
        r_h = procrustes_residual(A, B)[bd].mean()
        if record is None:
            record = (A, B)
            print(f"  {t:>6}{len(bd):>8}{r_h:>10.4f}{'--':>9}{'--':>7}"
                  f"{'--':>9}{'--':>8}")
            continue
        G_hat, _ = estimate_from_record(edges, cols, C, record[0],
                                        record[1], frames, m_total,
                                        np.sqrt(1 - delta ** 2))
        r_s = procrustes_residual(*coalition_sections(edges, cols, C, A, B,
                                                      G_hat, frames))
        stale_ok = bool((r_s[bd] < TOL).all())
        G_d, n_der = derive_edges(edges, cols, C, G[t], G_hat, K, crng, bd)
        r_d = procrustes_residual(*coalition_sections(edges, cols, C, A, B,
                                                      G_d, frames))
        derived_ok = bool((r_d[bd] < TOL).all())
        cost += K * M * n_der
        w_C += K * M * (2 * len(inside) + len(bd))
        print(f"  {t:>6}{len(bd):>8}{r_h:>10.4f}{r_s[bd].mean():>9.4f}"
              f"{'y' if stale_ok else 'N':>7}{'y' if derived_ok else 'N':>9}"
              f"{K * M * n_der:>8.0f}")
        record = (A, B)
    print(f"  evidencing share e(C) = {cost / w_C:.3f}; per identity per"
          f" epoch {cost / (EPOCHS - 1) / 128:.1f} against honest"
          f" {K * M * 2 * m_edges / n:.0f}")


# ------------------------------------------------------------------ main

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    part_one_copiers()
    part_two_curve()
    part_three_reading()
