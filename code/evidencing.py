"""
Evidencing: independence from one's own anchor, and what a measured map reads.

The Second Pool §9.5 found an IDLE projection — independent of its fellow
(iota = 1), expensive (tau > 0), and evidencing nothing but its anchor — and
asked whether the framework needs a third condition on projections beyond
independent and expensive. This module answers that in the set model and then
builds the one reading the corpus has left outside the induced-map class.

EVIDENCING IS NOT A THIRD CONDITION. Partition the paid pool P = A ⊔ N:
anchor work A (encodings, chains, searches — imported paid work) and native
work N (reconciliation, derivation — the work the substrate exists to do).
Let pi_A be the projection that reads exactly A: the receipt check. Then the
native share of a projection — its marginal fake-cost for a forger who already
holds every anchor receipt, over the budget — is

    tau_N(pi) = (f(pi_A ∧ pi) − f(pi_A)) / W = iota(pi | pi_A) · tau(pi),

by Combination Proofs Def 2.5 read against the projection's OWN anchor. The
idle projection is iota(pi | pi_A) = 0. Independence was always the condition;
it had only ever been demanded against the other projections.

THEOREM (induced-map readings evidence nothing). In the declared-frame model
the honest configuration itself costs exactly the anchor: free parts are free,
drift is free, and the reconciliation charge touches no declared object. A
forger holding the anchor therefore produces a configuration with honest's
exact distribution at no native cost, so ANY function of declared frames,
maps or Laplacians — spatial kernel, two-layer gluing, eigenspace overlap,
monotone or not — has tau_N = 0, and a Combination Proof of K such readings
has Gamma = |A| exactly. No spectral argument is needed. (Sign and Work
Prop 5.1, Second Pool Prop 5.3 and Cor 3.2 are instances.)

THE ONE READING OUTSIDE THE CLASS (Sign and Work §8.1). Restriction maps
MEASURED at overlaps rather than induced from declared frames. A section is
data: vertex v's outputs on the prompts of its incident edges, X_v^e ∈ R^{3×m}.
On edge (u,v) the map is the orthogonal Procrustes fit O = argmin ‖X_u − O X_v‖
and the reading is the RESIDUAL after the fit — the only quantity a declared
frame cannot set, since the fit absorbs every frame. The gate is H^0 at
tolerance: EVERY edge's residual below tol. (An edge count cannot see a
four-edge boundary in 371; a Laplacian built from fitted maps telescopes and
falls back into the induced class.)

THE WORLD AND THE WORK. A world G(t) ∈ R^{3×M}, AR(1) with per-entry
innovation delta: G(t) = sqrt(1−delta²) G(t−1) + delta ξ(t), seeded from a
family disjoint from the beacon's so no anchor holder can compute it. Honest
v derives X_v^e = R_v^T (G[:, cols_e] + (sigma/sqrt k) eps) — k re-derivations
averaged, cost k per prompt: the native work, priced as noise level.
Two prompt models: SHARED (every edge the same m prompts — one derivation
serves the network) and EDGE-LOCAL (each edge its own m prompts).

THE FORGER is a coalition C with no model of the world. Interior edges of C
are the fiction space — a consistent fabrication, free. Boundary edges must
fit honest neighbours. Two regimes:
  (a) PUBLIC — honest overlap data visible before the coalition commits; it
      copies. Prediction: boundary residual (sigma/sqrt k) sqrt(1 − 1/b) for b
      sources, BELOW honest's (sigma/sqrt k) sqrt 2 at every b, zero at b = 1.
      The boundary is a subsidy, not a cost.
  (b) COMMIT-BEFORE-COMPARE — the coalition commits before this epoch's
      reveal; its best input is last epoch's public record, scaled by the
      AR(1) decay. Prediction: residual² = delta² + (sigma²/k)(1 + 1/b), so
      it passes iff delta < delta* = (sigma/sqrt k) sqrt(tol² k/sigma² − 1 − 1/b),
      a step; above the step the cheapest passing strategy derives the
      boundary edges' prompts and fabricates the interior, at cost k·m·|∂C|
      (edge-local) or k·m once (shared).

PREDICTIONS, STATED BEFORE RUNNING.
  1. Miniature: measured tau_N = iota(pi|pi_A)·tau exactly, four specimens.
  2. Frame invariance: rerandomising every frame leaves residuals unchanged
     to 1e-12 — the anchor is invisible to this reading by construction, so
     iota(pi_fit | pi_A) = 1 and the interesting comparison is against the
     PUBLIC RECORD, not the anchor.
  3. Regime (a): coalition boundary residual below honest at every block
     size; ABOVE HONEST fires on every row.
  4. Regime (b): pass/fail steps at delta* as computed; rotational
     innovation (G(t) = Q G(t−1)) is free at any rate — the reading's own
     temporal gauge, the left O(3) action on the world.
  5. Evidencing share of a coalition, edge-local: e(C) = |∂C| / (2|E(C)| + |∂C|)
     with block boundaries 3.75, 3.5, 3.0, 2.0 at sizes 16, 32, 64, 128 on the
     seed-7 complex — bounded by 4 at every size, so the native cost PER
     IDENTITY falls as 1/|C| and the Sybil cap is not a cap on a modular
     complex. Shared prompts: e(C) = 1/|C| at every size.
  6. Whole network C = V: zero in both regimes, both prompt models.

WHAT THIS IS AND IS NOT. What the residual reading evidences is the world's
innovation relative to the public record — information, not effort — and
native work is priced only because derivation is the model's sole channel to
that innovation. The step in delta restates Sign and Work's rule that
satisfying a public constraint is never work, with the world as the
constraint. What is not a restatement: that the measured-map reading has a
gap not bought by its anchor (§8.1 answered), that the gap lives on the
coalition boundary alone, that on the program's own specimen the boundary is
at most four edges at any coalition size (Gauge-Fixing §2's spectral-gap
bound, measured at lambda_2 = 0.0038), and that publishing overlaps before
commitment inverts the boundary's sign.

Run:  python evidencing.py     (seeded; every number reproducible; ~5 s)
"""
import sys

import numpy as np

from complexes import hierarchical_modular, random_orthogonal
from exclusion import (Universe, projection, measure_pair, cheapest_accepted,
                       answer_key, DEPTH, EPOCHS, STALK)

D = STALK
M = 16                              # prompts per edge (or per network, shared)
SIGMA = 0.3                         # single-derivation noise
K = 4                               # design re-derivations
TOL = 1.5 * SIGMA * np.sqrt(2 / K)  # honest max over ~3000 edge-epochs clears
WORLD_SEED = 20_000                 # disjoint from the beacon's 10_000 + t
DELTAS = (0.0, 0.5, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0)   # units of sigma/sqrt k
BLOCKS = (16, 32, 64, 128)
INDEPENDENT_SEED, HONEST_SEED, FRAME_SEED, COALITION_SEED = 11, 12, 5, 41


# ------------------------------------------------------------------ world

def world_path(m_total, delta, epochs=EPOCHS, rotational=False):
    """AR(1) world, unit-scale entries, innovation delta per entry; or a
    purely rotational world G(t) = Q_t G(t-1) for the gauge calibration."""
    G = [np.random.default_rng(WORLD_SEED).normal(size=(D, m_total))]
    for t in range(1, epochs):
        rng = np.random.default_rng(WORLD_SEED + t)
        if rotational:
            G.append(random_orthogonal(D, rng) @ G[-1])
        else:
            G.append(np.sqrt(1 - delta ** 2) * G[-1]
                     + delta * rng.normal(size=(D, m_total)))
    return G


def edge_columns(edges, shared):
    """Column indices per edge: identical (shared) or disjoint (edge-local)."""
    if shared:
        return [np.arange(M)] * len(edges), M
    return [np.arange(i * M, (i + 1) * M) for i in range(len(edges))], \
        M * len(edges)


# ---------------------------------------------------------------- reading

def procrustes_residual(A, B):
    """Batched orthogonal Procrustes over edges: A, B of shape (E, 3, m).
    Returns per-edge RMS residual per entry after the best O(3) fit."""
    U, _, Vt = np.linalg.svd(A @ np.transpose(B, (0, 2, 1)))
    O = U @ Vt
    return np.sqrt(np.sum((A - O @ B) ** 2, axis=(1, 2)) / (D * A.shape[2]))


def honest_pair(edges, cols, G, frames, k, rng, sigma=SIGMA):
    """Honest endpoint sections on every edge: (A, B) of shape (E, 3, m)."""
    A = np.empty((len(edges), D, M))
    B = np.empty((len(edges), D, M))
    noise = sigma / np.sqrt(k) if k else 0.0
    for i, ((u, v), c) in enumerate(zip(edges, cols)):
        A[i] = frames[u].T @ (G[:, c] + noise * rng.normal(size=(D, M)))
        B[i] = frames[v].T @ (G[:, c] + noise * rng.normal(size=(D, M)))
    return A, B


def shared_honest_pair(edges, G, frames, k, rng, n, sigma=SIGMA):
    """Shared prompts: ONE noisy section per vertex, sliced onto every edge."""
    noise = sigma / np.sqrt(k) if k else 0.0
    X = [frames[v].T @ (G + noise * rng.normal(size=(D, M))) for v in range(n)]
    A = np.stack([X[u] for u, v in edges])
    B = np.stack([X[v] for u, v in edges])
    return A, B, X


# ------------------------------------------------------------- coalitions

def boundary(edges, C):
    inside = [i for i, (u, v) in enumerate(edges) if u in C and v in C]
    bd = [i for i, (u, v) in enumerate(edges) if (u in C) != (v in C)]
    return inside, bd


def coalition_sections(edges, cols, C, A, B, G_hat, frames):
    """Overwrite the coalition's endpoint sections with a consistent fiction
    drawn from its estimate G_hat of the world. Interior edges glue exactly;
    boundary edges fit G_hat against the honest neighbour."""
    A, B = A.copy(), B.copy()
    for i, ((u, v), c) in enumerate(zip(edges, cols)):
        if u in C:
            A[i] = frames[u].T @ G_hat[:, c]
        if v in C:
            B[i] = frames[v].T @ G_hat[:, c]
    return A, B


def estimate_from_record(edges, cols, C, A_rec, B_rec, frames, m_total,
                         scale=1.0):
    """The coalition's world estimate from a public record (A_rec, B_rec):
    on each prompt block, the frame-aligned mean of every HONEST endpoint
    that published on it (aligning is free; the fit is frame-invariant)."""
    acc = np.zeros((D, m_total))
    cnt = np.zeros(m_total)
    for i, ((u, v), c) in enumerate(zip(edges, cols)):
        if u not in C:
            acc[:, c] += frames[u] @ A_rec[i]
            cnt[c] += 1
        if v not in C:
            acc[:, c] += frames[v] @ B_rec[i]
            cnt[c] += 1
    with np.errstate(invalid="ignore", divide="ignore"):
        G_hat = np.where(cnt > 0, acc / np.maximum(cnt, 1), 0.0)
    return scale * G_hat, cnt


def derive_boundary(edges, cols, C, G, G_hat, k, rng, sigma=SIGMA):
    """Regime (b) above the step: derive the boundary edges' prompts from the
    world (k re-derivations each) and keep the fiction elsewhere. Returns the
    patched estimate and the native cost k·m per distinct prompt block."""
    G_hat = G_hat.copy()
    done = set()
    cost = 0.0
    _, bd = boundary(edges, C)
    for i in bd:
        key = int(cols[i][0])
        if key in done:
            continue
        done.add(key)
        G_hat[:, cols[i]] = G[:, cols[i]] + sigma / np.sqrt(k) * \
            rng.normal(size=(D, M))
        cost += k * M
    return G_hat, cost


# ------------------------------------------------------------------ parts

def part_one_miniature():
    print("=" * 74)
    print("PART 1 — MINIATURE: tau_N = iota(pi | pi_A) · tau, on the attacker")
    print("=" * 74)
    u = Universe(n_paid=8, n_free=2)
    P, F = sorted(u.paid), sorted(u.free)
    A_pool, N_pool = P[:3], P[3:]
    pi_A = projection(u, A_pool)
    specimens = [("reads the anchor only (idle)", A_pool),
                 ("anchor + two native", A_pool + N_pool[:2]),
                 ("two native, unanchored", N_pool[:2]),
                 ("anchor + free (the trap)", A_pool + F)]
    print(f"  {'projection':<32}{'tau':>6}{'i(pi|A)':>9}{'i·tau':>7}"
          f"{'tau_N':>7}{'designed':>10}")
    worst = 0.0
    for name, reads in specimens:
        pi = projection(u, reads)
        _, tau, iota, _, f12 = measure_pair(u, pi_A, pi)
        f_A = cheapest_accepted(u, [pi_A])
        tau_N = (f12 - f_A) / u.work
        designed = len(set(reads) & set(N_pool)) / u.work
        worst = max(worst, abs(tau_N - iota * tau), abs(tau_N - designed))
        print(f"  {name:<32}{tau:>6.3f}{iota:>9.3f}{iota * tau:>7.3f}"
              f"{tau_N:>7.3f}{designed:>10.3f}")
    print(f"  worst |tau_N − iota·tau|, |tau_N − designed| = {worst:.1e}"
          f"   (anything above 0 means stop reading)")
    print("  Evidencing is independence from one's own anchor. The idle")
    print("  projection is iota(pi | pi_A) = 0; the trap reads more and")
    print("  evidences nothing.")


def _setup(shared):
    n = 2 ** DEPTH
    _, edges = hierarchical_modular(DEPTH, np.random.default_rng(7),
                                    cross_per_merge=2)
    cols, m_total = edge_columns(edges, shared)
    frames = [random_orthogonal(D, np.random.default_rng(FRAME_SEED + v))
              for v in range(n)]
    return n, edges, cols, m_total, frames


def _honest(edges, cols, G, frames, k, rng, shared, n):
    if shared:
        A, B, _ = shared_honest_pair(edges, G, frames, k, rng, n)
        return A, B
    return honest_pair(edges, cols, G, frames, k, rng)


def part_two_calibration():
    print("\n" + "=" * 74)
    print("PART 2 — CALIBRATION: objects with known residuals")
    print("=" * 74)
    n, edges, cols, m_total, frames = _setup(shared=False)
    G = world_path(m_total, 0.0)[0]
    rng = np.random.default_rng(HONEST_SEED)
    rows = []
    for k, label in ((0, "honest, k → ∞ (no noise)"), (1, "honest, k = 1"),
                     (K, f"honest, k = {K} (design)"), (16, "honest, k = 16")):
        A, B = honest_pair(edges, cols, G, frames, k, rng)
        r = procrustes_residual(A, B)
        pred = 0.0 if k == 0 else SIGMA * np.sqrt(2 / k) * np.sqrt(1 - 1 / M)
        rows.append((label, r.mean(), r.max(), pred, int((r < TOL).sum())))
    A, B = honest_pair(edges, cols, G, frames, K, rng)
    C = set(range(n))
    Af, Bf = coalition_sections(edges, cols, C, A, B, G, frames)
    r = procrustes_residual(Af, Bf)
    rows.append(("whole-network fiction", r.mean(), r.max(), 0.0,
                 int((r < TOL).sum())))
    rng_i = np.random.default_rng(INDEPENDENT_SEED)
    Ai = rng_i.normal(size=A.shape)
    Bi = rng_i.normal(size=B.shape)
    r = procrustes_residual(Ai, Bi)
    rows.append(("two independent datasets", r.mean(), r.max(), float("nan"),
                 int((r < TOL).sum())))
    print(f"  tol = {TOL:.3f}   {'object':<28}{'mean r':>8}{'max r':>8}"
          f"{'predicted':>10}{'pass':>6}/{len(edges)}")
    for label, mean, mx, pred, npass in rows:
        print(f"  {'':<13}{label:<28}{mean:>8.4f}{mx:>8.4f}{pred:>10.4f}"
              f"{npass:>6}")
    # frame invariance: the anchor lives in the frames; the fit cannot see it
    A2 = np.stack([random_orthogonal(D, np.random.default_rng(900 + i)) @ A[i]
                   for i in range(len(edges))])
    B2 = np.stack([random_orthogonal(D, np.random.default_rng(1900 + i)) @ B[i]
                   for i in range(len(edges))])
    dev = np.max(np.abs(procrustes_residual(A2, B2) - procrustes_residual(A, B)))
    print(f"  frame invariance: max |Δr| after rerandomising every frame ="
          f" {dev:.1e}   (iota(pi_fit | pi_A) = 1 by construction)")
    # the count-reading trap
    _, bd = boundary(edges, set(range(128)))
    print(f"  count-reading trap: a coalition of 128 failing ALL {len(bd)}"
          f" boundary edges still passes {len(edges) - len(bd)}/{len(edges)}"
          f" = {(len(edges) - len(bd)) / len(edges):.3f} of edges; the gate"
          f" is H^0 at tolerance, every edge")


def _coalition_run(shared, delta_units, C, regime, k=K, rotational=False):
    """One coalition strategy set against one world. Returns honest and
    coalition boundary residuals per epoch, pass flags, and native costs."""
    n, edges, cols, m_total, frames = _setup(shared)
    delta = delta_units * SIGMA / np.sqrt(k)
    G = world_path(m_total, delta, rotational=rotational)
    rng = np.random.default_rng(HONEST_SEED)
    crng = np.random.default_rng(COALITION_SEED)
    inside, bd = boundary(edges, C)
    honest_r, stale_r, out = [], [], {"stale": True, "public": True,
                                      "derive": True, "cost_derive": 0.0}
    record = None
    for t in range(EPOCHS):
        A, B = _honest(edges, cols, G[t], frames, k, rng, shared, n)
        r_h = procrustes_residual(A, B)
        honest_r.append(r_h[bd].mean() if bd else 0.0)
        if regime != "public" and record is None:
            record = (A, B)             # epoch 0: nothing to commit against
            continue
        src = (A, B) if regime == "public" else record
        scale = 1.0 if (regime == "public" or rotational)             else np.sqrt(1 - delta ** 2)
        G_hat, _ = estimate_from_record(edges, cols, C, src[0], src[1],
                                        frames, m_total, scale)
        Ac, Bc = coalition_sections(edges, cols, C, A, B, G_hat, frames)
        r_c = procrustes_residual(Ac, Bc)
        stale_r.append(r_c[bd].mean() if bd else 0.0)
        key = "public" if regime == "public" else "stale"
        out[key] = out[key] and bool(np.all(r_c < TOL))
        if regime != "public":
            G_d, cost = derive_boundary(edges, cols, C, G[t], G_hat, k, crng)
            Ad, Bd = coalition_sections(edges, cols, C, A, B, G_d, frames)
            out["derive"] = out["derive"] and bool(
                np.all(procrustes_residual(Ad, Bd) < TOL))
            out["cost_derive"] += cost
        record = (A, B)
    out["honest_r"] = float(np.mean(honest_r))
    out["coalition_r"] = float(np.mean(stale_r))
    out["boundary"], out["inside"] = len(bd), len(inside)
    out["k"], out["m"], out["n_edges"] = k, M, len(edges)
    return out


def part_three_public():
    print("\n" + "=" * 74)
    print("PART 3 — REGIME (a), PUBLIC OVERLAPS: the boundary as a subsidy")
    print("=" * 74)
    print(f"  {'prompts':<11}{'|C|':>5}{'|∂C|':>6}{'honest r':>10}"
          f"{'coalition r':>13}{'predicted':>11}{'pass':>6}")
    for shared in (False, True):
        for size in BLOCKS:
            out = _coalition_run(shared, 0.0, set(range(size)), "public")
            b = (256 - size) if shared else 1
            pred = SIGMA / np.sqrt(K) * np.sqrt(max(0.0, 1 - 1 / b)) * \
                np.sqrt(1 - 1 / M)
            flag = "  <-- ABOVE HONEST" if out["coalition_r"] < out["honest_r"] \
                else ""
            print(f"  {'shared' if shared else 'edge-local':<11}{size:>5}"
                  f"{out['boundary']:>6}{out['honest_r']:>10.4f}"
                  f"{out['coalition_r']:>13.4f}{pred:>11.4f}"
                  f"{'y' if out['public'] else 'N':>6}{flag}")
    print("  Zero derivations. The coalition copies its neighbours' data and")
    print("  their noise with it; with one source it copies exactly. Publishing")
    print("  overlaps before commitment turns the boundary from a cost into a")
    print("  subsidy.")


def part_four_commit():
    print("\n" + "=" * 74)
    print("PART 4 — REGIME (b), COMMIT BEFORE COMPARE: the step in the world's"
          " innovation")
    print("=" * 74)
    print(f"  delta in units of sigma/sqrt k = {SIGMA / np.sqrt(K):.3f};"
          f" tol = {TOL:.3f}")
    for shared in (False, True):
        size = 128
        C = set(range(size))
        b = (256 - size) if shared else 1
        dstar = np.sqrt(max(0.0, TOL ** 2 * K / SIGMA ** 2 - 1 - 1 / b))
        print(f"\n  {'shared' if shared else 'edge-local'} prompts, |C| = {size}:"
              f" predicted step at delta* = {dstar:.2f}")
        print(f"  {'delta':>7}{'honest r':>10}{'stale r':>9}{'predicted':>11}"
              f"{'stale':>7}{'derive':>8}{'cost_derive':>13}")
        first_fail = None
        for du in DELTAS:
            out = _coalition_run(shared, du, C, "commit")
            delta = du * SIGMA / np.sqrt(K)
            pred = np.sqrt(delta ** 2 + SIGMA ** 2 / K * (1 + 1 / b)) * \
                np.sqrt(1 - 1 / M)
            if not out["stale"] and first_fail is None:
                first_fail = du
            print(f"  {du:>7.2f}{out['honest_r']:>10.4f}"
                  f"{out['coalition_r']:>9.4f}{pred:>11.4f}"
                  f"{'y' if out['stale'] else 'N':>7}"
                  f"{'y' if out['derive'] else 'N':>8}"
                  f"{out['cost_derive']:>13.0f}")
        print(f"  first delta at which the stale coalition fails: "
              f"{first_fail}  (predicted {dstar:.2f})")
    out = _coalition_run(False, 3.0, set(range(128)), "commit",
                         rotational=True)
    print(f"\n  rotational world, edge-local, |C| = 128: stale r ="
          f" {out['coalition_r']:.4f} vs honest {out['honest_r']:.4f},"
          f" passes: {'y' if out['stale'] else 'N'}")
    print("  A rotational innovation is absorbed by the fit at any rate: the")
    print("  measured-map reading has a temporal gauge of its own, the left")
    print("  O(3) action on the world.")


def part_five_table():
    print("\n" + "=" * 74)
    print("PART 5 — THE EVIDENCING SHARE OF A COALITION, above the step")
    print("=" * 74)
    n, edges, _, _, _ = _setup(shared=False)
    deg = np.zeros(n)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    L = np.zeros((n, n))
    for u, v in edges:
        L[u, u] += 1; L[v, v] += 1; L[u, v] -= 1; L[v, u] -= 1
    lam2 = np.linalg.eigvalsh(L)[1]
    print(f"  lambda_2 of the complex = {lam2:.4f}")
    print(f"  {'prompts':<11}{'coalition':<16}{'|C|':>5}{'|∂C|':>6}"
          f"{'Cheeger':>9}{'e(C) meas':>11}{'designed':>10}{'per identity':>14}")
    worst = 0.0
    for shared in (False, True):
        for size in BLOCKS:
            for kind in ("block", "contiguous"):
                if kind == "block":
                    C = set(range(size))
                else:
                    C = set(range(37, 37 + size))
                out = _coalition_run(shared, 3.0, C, "commit")
                w_C = K * M * (sum(deg[v] for v in C) if not shared
                               else len(C)) * (EPOCHS - 1)   # epochs scored
                e_meas = out["cost_derive"] / w_C if out["derive"] else \
                    float("nan")
                if shared:
                    designed = 1 / len(C)
                else:
                    designed = out["boundary"] / (2 * out["inside"]
                                                  + out["boundary"])
                per_id = out["cost_derive"] / (EPOCHS - 1) / len(C)
                cheeger = lam2 * len(C) * (1 - len(C) / n) / 2
                if not np.isnan(e_meas):
                    worst = max(worst, abs(e_meas - designed))
                print(f"  {'shared' if shared else 'edge-local':<11}"
                      f"{kind:<16}{len(C):>5}{out['boundary']:>6}"
                      f"{cheeger:>9.2f}{e_meas:>11.4f}{designed:>10.4f}"
                      f"{per_id:>14.1f}")
    out = _coalition_run(False, 3.0, set(range(n)), "commit")
    print(f"  whole network C = V, edge-local: cost_derive = "
          f"{out['cost_derive']:.0f}, boundary {out['boundary']}")
    print(f"  worst |measured − designed e(C)| = {worst:.1e}")
    print("  Block coalitions of the program's own complex have at most four")
    print("  boundary edges at any size: the native cost per identity falls as")
    print("  1/|C|, and the Sybil cap is not a cap on a modular complex.")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    part_one_miniature()
    part_two_calibration()
    part_three_public()
    part_four_commit()
    part_five_table()
