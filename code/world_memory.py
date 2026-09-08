"""
A world with memory: the pool is the entropy of the world given the record.

One's Own Anchor §9.1 left the residual reading with one open question about
the world it evidences. Its world was AR(1) — memoryless — so the innovation
given the public record was the whole one-step drift, and the coalition's
best input was last epoch's record. A world with momentum is extrapolable:
the innovation given the record is the extrapolation error, smaller, and the
coalition the predecessor wrote down (last record, decayed) was the WEAKEST
attacker in the record-only class. Supremum over attackers, again.

THE WORLD. G(t) = G(t−1) + Δ(t), Δ(t) = φ Δ(t−1) + sqrt(1−φ²) δ ξ(t). The
one-step drift has variance δ² at every φ; the fraction of it that is
predictable from the past is φ², and the innovation given the exact past is
q = (1−φ²) δ². At φ = 0 this is a random walk with the AR(1) world's one-step
error, so the predecessor's step must reproduce there.

THE ATTACKERS, all with no channel to the world but the public record:
  naive        — last record (the predecessor's coalition);
  extrapolate  — last record plus φ times the last difference;
  kalman       — the conditional mean of G(t) given every record so far,
                 the optimal predictor in the Gaussian linear class. Its
                 one-step error v_pred is the steady state of a Riccati
                 recursion with record noise s/b, s = σ²/k, b sources; it
                 is at least q and tends to q as b → ∞.
The residual gate is unchanged: every edge below tol = 1.5 σ sqrt(2/k).

THE THEOREM, in the model. The predicting coalition's boundary residual² is
(v_pred + s)(1 − 1/m), so it passes iff v_pred < v* = tol²/(1−1/m) − s,
which on the specimen is 3.8 s. Two consequences.
  (i) The pool. What the reading can claim is bounded by the world's
      innovation given the record; a world with memory shrinks the pool by
      (1 − φ²) at fixed drift, and the coalition's native share is a step
      in that innovation, |∂C|-share above v*, zero below.
  (ii) The resolution. v* is proportional to s = σ²/k, the honest
      derivation variance. To refuse the predictor on a world of innovation
      q the mechanism must demand k ≥ k* = 3.8 σ²/q re-derivations per
      prompt from EVERY honest participant: the price of evidencing scales
      as the inverse of the world's innovation, and a fully predictable
      world costs everything to evidence and evidences nothing.
Information form: two honest neighbours share, beyond the record,
I = −½ log(1 − (q/(q+s))²) per entry, which is (q/s)²/2 when q ≪ s. That is
all any gate at overlaps has to see, and the residual gate sees it at
resolution s.

PREDICTIONS, STATED BEFORE RUNNING (s = 0.0225, δ = 3 sqrt(s) = 0.45,
block coalition of 128, tol² = 4.5 s, v* = 3.80 s; Riccati values from the
same recursion, computed before the module was run):
  1. Calibration. The imported instrument's step reproduces at δ = 1.50
     (edge-local) and 1.75 (shared) in units of sqrt(s). This module's naive
     attacker on the momentum world at φ = 0 fails first at the same δ in
     both prompt models: the random walk has the AR(1) world's one-step
     error.
  2. Three attackers at φ = 0.9. Naive: residual² ≈ 9 s + s(1 + 1/b), fails
     both. Extrapolate: q + s(1 + ((1+φ)² + φ²)/b) = 2.75 s shared (passes),
     7.1 s edge-local (fails). Kalman: v_pred = 1.74 s shared (passes),
     4.14 s edge-local (fails, by 0.3 s). Zero derivations wherever it
     passes.
  3. The sweep in φ ∈ {0, 0.5, 0.8, 0.9, 0.95, 0.99}, Kalman. Shared: fails
     at 0 and 0.5, passes from 0.8 (v_pred 3.27 s, margin 0.5 s — the
     closest call in the module). Edge-local: fails through 0.9, passes at
     0.95 (2.99 s) and 0.99 (1.53 s). e(C) is the predecessor's 0.0054
     (edge-local) or 1/128 (shared) wherever the predictor fails and 0
     wherever it passes. BELOW HONEST — the predictor's residual under
     honest's own — at φ = 0.95 and 0.99 with shared prompts (v_pred < s)
     and nowhere edge-local.
  4. The resolution sweep at φ = 0.95, δ fixed absolute, k ∈ {1, …, 64},
     tol scaling with k. Shared: the predictor passes up to k = 16 and
     fails from k = 32 (k* = 3.8 σ²/q = 17.3). Edge-local: passes up to
     k = 4, fails from k = 8 (the record's noise is on the mechanism's
     side). Honest passes every edge at every k by construction of tol.
  5. Fresh prompts. If every epoch's prompts are new — no record on any
     column the coalition must fit — the predictor has nothing to predict
     from: its error is the world's whole variance, it fails at every φ,
     and the coalition pays the predecessor's boundary share (0.0054
     edge-local, 1/128 shared) at φ = 0.9 and 0.99 alike. The memory bound
     is a bound on RECORDED prompts; Every Basis at Once §8.1's semantic
     cost is what fresh prompts cost honesty, and it is not modelled here.
  6. Flags. A predicted pass that fails, or the reverse, prints MISS; a
     coalition below honest prints BELOW HONEST and is not an error but the
     finding: in a world the record predicts better than a fresh
     derivation, the fiction is a better model of the world than honesty.

WHAT CAME BACK. Four MISS flags on the first run, all one error: the
predictions above use the MEAN boundary residual where the gate takes the
MAX over every gated edge-epoch, and near the threshold the spread decides.
Per-edge residual² is (v + s)(1 − 1/m) χ²_ν/ν with ν = dm − 3 = 45, so the
max over N gated samples sits at the (1 − 1/N) quantile, c_N² ≈ 1.45 for
N = 40, and the threshold is v*_N = tol²/((1 − 1/m) c_N²) − s ≈ 2.3 s, not
3.8 s. With that constant: the calibration step lands on the predecessor's
grid point only when scored on the predecessor's window (seven epochs; over
twenty the edge-local max crosses one grid step earlier); edge-local
φ = 0.95 fails (2.99 s > 2.4 s) and shared φ = 0.8 fails (3.27 s), both
predicted to pass; k* becomes 2.3 σ²/q = 10.5, so the shared predictor
fails from k = 16, not 32, and edge-local from k = 4, not 8. Every mean
residual matched its prediction to the third decimal; only the pass calls
at the edge moved. The mean-based constant is kept in the printout beside
the corrected one, and the flags are computed against the corrected one.
BELOW HONEST fired where predicted (shared, φ ≥ 0.95) and additionally in
the resolution sweep at shared k ≤ 4, where v_pred < s by the same rule.

Run:  python world_memory.py     (seeded; every number reproducible; ~20 s)
"""
import math
import sys

import numpy as np

from evidencing import (D, M, SIGMA, K, TOL, WORLD_SEED, HONEST_SEED,
                        COALITION_SEED, _setup, _honest, _coalition_run,
                        procrustes_residual, boundary, coalition_sections,
                        estimate_from_record, derive_boundary)

EPOCHS_MEM = 24                      # long enough for the filter to settle
SCORE_FROM = 4                       # epochs scored (transient excluded)
S = SIGMA ** 2 / K
DELTA_ABS = 3 * np.sqrt(S)           # the predecessor's δ = 3 row, absolute
PHIS = (0.0, 0.5, 0.8, 0.9, 0.95, 0.99)
KS = (1, 2, 4, 8, 16, 32, 64)
DELTA_UNITS = (1.0, 1.25, 1.5, 1.75, 2.0)
BLOCK = 128


# ------------------------------------------------------------------ world

def momentum_world(m_total, delta, phi, epochs=EPOCHS_MEM):
    """G(t) = G(t−1) + Δ(t), Δ(t) = φ Δ(t−1) + sqrt(1−φ²) δ ξ(t); Δ(0)
    stationary. Seeds in the world's family, disjoint from the beacon's."""
    G = [np.random.default_rng(WORLD_SEED).normal(size=(D, m_total))]
    Dl = delta * np.random.default_rng(WORLD_SEED + 999).normal(
        size=(D, m_total))
    for t in range(1, epochs):
        xi = np.random.default_rng(WORLD_SEED + t).normal(size=(D, m_total))
        Dl = phi * Dl + np.sqrt(1 - phi ** 2) * delta * xi
        G.append(G[-1] + Dl)
    return G


# ----------------------------------------------------------------- filter

def riccati_steady(phi, delta, s, b, steps=500):
    """Steady-state one-step prediction variance of g under the Kalman
    filter with record noise s/b. Returns (v_pred, q)."""
    q = (1 - phi ** 2) * delta ** 2
    F = np.array([[1.0, phi], [0.0, phi]])
    Q = q * np.ones((2, 2))
    H = np.array([[1.0, 0.0]])
    P = np.array([[s / b, 0.0], [0.0, delta ** 2]])
    for _ in range(steps):
        Pm = F @ P @ F.T + Q
        Kg = Pm @ H.T / (H @ Pm @ H.T + s / b)
        P = (np.eye(2) - Kg @ H) @ Pm
    return float((F @ P @ F.T + Q)[0, 0]), q


class KalmanCoalition:
    """Per-column Kalman filter on the public record, vectorised over the
    columns the coalition has at least one honest source for. State per
    column (g, Δ); covariance per column, since b varies by column."""

    def __init__(self, phi, delta, s, m_total):
        self.phi, self.delta, self.s = phi, delta, s
        self.x = np.zeros((2, D, m_total))
        self.P = np.zeros((3, m_total))          # P00, P01, P11 per column
        self.seen = np.zeros(m_total, bool)

    def update(self, y, cnt):
        """Absorb one epoch's record: y (D, m_total) frame-aligned mean of
        cnt sources per column (cnt = 0 → no observation)."""
        obs = cnt > 0
        new = obs & ~self.seen
        self.x[0][:, new] = y[:, new]
        self.P[0, new] = self.s / cnt[new]
        self.P[2, new] = self.delta ** 2
        self.seen |= new
        old = obs & ~new
        if not old.any():
            return
        r = self.s / cnt[old]
        P00, P01, P11 = self.P[:, old]
        Sg = P00 + r
        k0, k1 = P00 / Sg, P01 / Sg
        innov = y[:, old] - self.x[0][:, old]
        self.x[0][:, old] += k0 * innov
        self.x[1][:, old] += k1 * innov
        self.P[0, old] = P00 - k0 * P00
        self.P[1, old] = P01 - k0 * P01
        self.P[2, old] = P11 - k1 * P01

    def predict(self):
        """Advance the state one epoch; return the predicted G(t)."""
        phi, q = self.phi, (1 - self.phi ** 2) * self.delta ** 2
        P00, P01, P11 = self.P
        self.x[0] = self.x[0] + phi * self.x[1]
        self.x[1] = phi * self.x[1]
        n00 = P00 + 2 * phi * P01 + phi ** 2 * P11 + q
        n01 = phi * P01 + phi ** 2 * P11 + q
        n11 = phi ** 2 * P11 + q
        self.P = np.stack([n00, n01, n11])
        return self.x[0].copy()


# --------------------------------------------------------------- one run

def _normal_quantile(p, lo=-10.0, hi=10.0):
    """Inverse standard normal CDF by bisection on math.erf (NumPy only)."""
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if 0.5 * (1 + math.erf(mid / math.sqrt(2))) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def max_ratio_sq(n_samples, dof=D * M - 3):
    """c_N²: the (1 − 1/N) quantile of χ²_ν/ν (Wilson–Hilferty), the factor
    by which the max of N gated residuals² exceeds their mean."""
    z = _normal_quantile(1 - 1 / n_samples)
    return (1 - 2 / (9 * dof) + z * math.sqrt(2 / (9 * dof))) ** 3


def v_star(tol, s, n_samples=None):
    """Pass threshold on the predictor's error: mean-based when n_samples is
    None (the docstring's first prediction), max-based otherwise."""
    c2 = 1.0 if n_samples is None else max_ratio_sq(n_samples)
    return tol ** 2 / ((1 - 1 / M) * c2) - s


def _predictor(mode, kf, records, phi):
    """The coalition's estimate of G(t) from the record under one strategy."""
    if mode == "naive":
        return records[-1]
    if mode == "extrapolate":
        return records[-1] + phi * (records[-1] - records[-2])
    return kf.predict()


def run_memory(shared, phi, delta, C, mode, k=K, epochs=EPOCHS_MEM,
               score_from=SCORE_FROM, fresh=False):
    """One coalition strategy against the momentum world. Returns mean
    honest and coalition boundary residuals over scored epochs, pass flags
    for the predictor and for the derive-the-boundary strategy, and the
    derive strategy's native cost. With fresh=True every epoch's prompts
    are new columns, so the record never covers a column being fitted."""
    n, edges, cols0, m_total, frames = _setup(shared)
    s = SIGMA ** 2 / k
    tol = 1.5 * SIGMA * np.sqrt(2 / k)
    width = m_total * (epochs if fresh else 1)
    G = momentum_world(width, delta, phi, epochs)
    rng = np.random.default_rng(HONEST_SEED)
    crng = np.random.default_rng(COALITION_SEED)
    _, bd = boundary(edges, C)
    kf = KalmanCoalition(phi, delta, s, width)
    records, hr, cr = [], [], []
    out = {"pred": True, "derive": True, "cost_derive": 0.0, "honest_ok": True}
    for t in range(epochs):
        cols = [c + t * m_total for c in cols0] if fresh else cols0
        G_seen = G[t][:, cols[0]] if shared else G[t]   # shared: one block
        A, B = _honest(edges, cols, G_seen, frames, k, rng, shared, n)
        r_h = procrustes_residual(A, B)
        out["honest_ok"] = out["honest_ok"] and bool(np.all(r_h < tol))
        if t >= 2:
            G_hat = _predictor(mode, kf, records, phi)
            Ac, Bc = coalition_sections(edges, cols, C, A, B, G_hat, frames)
            r_c = procrustes_residual(Ac, Bc)
            if t >= score_from:
                hr.append(r_h[bd].mean())
                cr.append(r_c[bd].mean())
                out["pred"] = out["pred"] and bool(np.all(r_c < tol))
                G_d, cost = derive_boundary(edges, cols, C, G[t], G_hat, k,
                                            crng)
                Ad, Bd = coalition_sections(edges, cols, C, A, B, G_d, frames)
                out["derive"] = out["derive"] and bool(
                    np.all(procrustes_residual(Ad, Bd) < tol))
                out["cost_derive"] += cost
        elif mode == "kalman":
            kf.predict() if t == 1 else None
        y, cnt = estimate_from_record(edges, cols, C, A, B, frames, width)
        records.append(y)
        if mode == "kalman":
            kf.update(y, cnt)
    out["honest_r"], out["coalition_r"] = float(np.mean(hr)), float(np.mean(cr))
    out["boundary"], out["b"] = len(bd), (n - len(C)) if shared else 1
    out["scored"] = epochs - score_from
    out["n_gated"] = len(bd) * out["scored"]
    return out


def _predicted_residual(v_pred, s):
    return np.sqrt((v_pred + s) * (1 - 1 / M))


def _flags(out, predicted_pass):
    f = []
    if out["pred"] != predicted_pass:
        f.append("MISS")
    if out["coalition_r"] < out["honest_r"]:
        f.append("BELOW HONEST")
    if not out["honest_ok"]:
        f.append("HONEST REFUSED")
    return "  <-- " + ", ".join(f) if f else ""


# ------------------------------------------------------------------ parts

def part_one_calibration():
    print("=" * 74)
    print("PART 1 — CALIBRATION: the predecessor's step, twice")
    print("=" * 74)
    for shared in (False, True):
        label = "shared" if shared else "edge-local"
        first_old = first_new = None
        for du in DELTA_UNITS:
            old = _coalition_run(shared, du, set(range(BLOCK)), "commit")
            new = run_memory(shared, 0.0, du * np.sqrt(S), set(range(BLOCK)),
                             "naive", epochs=8, score_from=1)
            if not old["stale"] and first_old is None:
                first_old = du
            if not new["pred"] and first_new is None:
                first_new = du
        print(f"  {label:<11} first failing δ (units sqrt s): imported"
              f" instrument {first_old}, this module at φ = 0 {first_new}"
              f"{'' if first_old == first_new else '  <-- MISS'}")
    print("  The random walk at φ = 0 has the AR(1) world's one-step error;")
    print("  the step is where the predecessor put it, on the predecessor's")
    print("  scoring window. The gate is a max, and a longer window moves a")
    print("  near-threshold call by one grid step.")


def part_two_attackers():
    print("\n" + "=" * 74)
    print("PART 2 — THREE ATTACKERS AT φ = 0.9: the predecessor's coalition"
          " was the weakest")
    print("=" * 74)
    phi = 0.9
    n_gated = 2 * (EPOCHS_MEM - SCORE_FROM)
    print(f"  δ = {DELTA_ABS:.3f} = 3 sqrt(s), block of {BLOCK}, tol = "
          f"{TOL:.3f}; v*: mean-based {v_star(TOL, S) / S:.2f} s, max over"
          f" {n_gated} gated edge-epochs {v_star(TOL, S, n_gated) / S:.2f} s")
    print(f"  {'prompts':<11}{'attacker':<13}{'honest r':>9}{'coal. r':>9}"
          f"{'predicted':>10}{'v_pred/s':>9}{'pass':>6}{'derive':>8}")
    for shared in (False, True):
        b = (256 - BLOCK) if shared else 1
        for mode in ("naive", "extrapolate", "kalman"):
            out = run_memory(shared, phi, DELTA_ABS, set(range(BLOCK)), mode)
            if mode == "naive":
                v = DELTA_ABS ** 2 + S / b
            elif mode == "extrapolate":
                v = (1 - phi ** 2) * DELTA_ABS ** 2 + \
                    S * ((1 + phi) ** 2 + phi ** 2) / b
            else:
                v, _ = riccati_steady(phi, DELTA_ABS, S, b)
            pp = v < v_star(TOL, S, out["n_gated"])
            print(f"  {'shared' if shared else 'edge-local':<11}{mode:<13}"
                  f"{out['honest_r']:>9.4f}{out['coalition_r']:>9.4f}"
                  f"{_predicted_residual(v, S):>10.4f}{v / S:>9.2f}"
                  f"{'y' if out['pred'] else 'N':>6}"
                  f"{'y' if out['derive'] else 'N':>8}{_flags(out, pp)}")
    print("  Same drift per epoch as the predecessor's δ = 3 row, which its")
    print("  coalition failed at every prompt model. The record predicts most")
    print("  of it, and the optimal predictor passes at zero derivations")
    print("  wherever the record is clean enough to read the momentum.")


def part_three_sweep():
    print("\n" + "=" * 74)
    print("PART 3 — THE POOL: innovation given the record, and the step in it")
    print("=" * 74)
    n, edges, _, _, _ = _setup(shared=False)
    deg = np.zeros(n)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    C = set(range(BLOCK))
    print(f"  {'prompts':<11}{'φ':>5}{'q/s':>7}{'v_pred/s':>9}{'I_pair':>8}"
          f"{'honest r':>9}{'coal. r':>9}{'pred.':>7}{'pass':>6}"
          f"{'e(C)':>8}{'per id':>8}")
    for shared in (False, True):
        b = (256 - BLOCK) if shared else 1
        for phi in PHIS:
            out = run_memory(shared, phi, DELTA_ABS, C, "kalman")
            v, q = riccati_steady(phi, DELTA_ABS, S, b)
            pp = v < v_star(TOL, S, out["n_gated"])
            rho = q / (q + S)
            i_pair = -0.5 * np.log(1 - rho ** 2)
            w_C = K * M * (sum(deg[x] for x in C) if not shared else len(C)) \
                * out["scored"]
            cost = 0.0 if out["pred"] else out["cost_derive"]
            e = cost / w_C
            per_id = cost / out["scored"] / len(C)
            print(f"  {'shared' if shared else 'edge-local':<11}{phi:>5.2f}"
                  f"{q / S:>7.2f}{v / S:>9.2f}{i_pair:>8.3f}"
                  f"{out['honest_r']:>9.4f}{out['coalition_r']:>9.4f}"
                  f"{_predicted_residual(v, S):>7.3f}"
                  f"{'y' if out['pred'] else 'N':>6}{e:>8.4f}{per_id:>8.1f}"
                  f"{_flags(out, pp)}")
    n_gated = 2 * (EPOCHS_MEM - SCORE_FROM)
    print(f"  pass iff v_pred < v*_N = {v_star(TOL, S, n_gated) / S:.2f} s"
          f" (max over {n_gated} gated edge-epochs; mean-based"
          f" {v_star(TOL, S) / S:.2f} s)")
    print("  The drift is 3 sqrt(s) in every row. What moves is the fraction")
    print("  of it the record predicts. The coalition's share is a step in the")
    print("  innovation given the record, and past φ = 0.95 with shared")
    print("  prompts the record is a better model of the world than a fresh")
    print("  derivation: the predictor sits below honest.")


def part_four_resolution():
    print("\n" + "=" * 74)
    print("PART 4 — THE RESOLUTION: k* = c σ² / q, the price of evidencing")
    print("=" * 74)
    phi = 0.95
    q = (1 - phi ** 2) * DELTA_ABS ** 2
    n_gated = 2 * (EPOCHS_MEM - SCORE_FROM)
    c_mean = 4.5 / (1 - 1 / M) - 1
    c_max = 4.5 / ((1 - 1 / M) * max_ratio_sq(n_gated)) - 1
    print(f"  φ = {phi}, δ = {DELTA_ABS:.3f} absolute, q = {q:.5f}; k* (b → ∞)"
          f" = c σ²/q: mean-based c = {c_mean:.1f} → {c_mean * SIGMA ** 2 / q:.1f},"
          f" max-based c = {c_max:.1f} → {c_max * SIGMA ** 2 / q:.1f}")
    print(f"  {'prompts':<11}{'k':>4}{'s':>8}{'tol':>7}{'v_pred':>8}{'v*_N':>8}"
          f"{'honest r':>9}{'coal. r':>9}{'pass':>6}{'honest ok':>10}")
    for shared in (False, True):
        b = (256 - BLOCK) if shared else 1
        for k in KS:
            s = SIGMA ** 2 / k
            tol = 1.5 * SIGMA * np.sqrt(2 / k)
            out = run_memory(shared, phi, DELTA_ABS, set(range(BLOCK)),
                             "kalman", k=k)
            v, _ = riccati_steady(phi, DELTA_ABS, s, b)
            vs = v_star(tol, s, out["n_gated"])
            print(f"  {'shared' if shared else 'edge-local':<11}{k:>4}"
                  f"{s:>8.4f}{tol:>7.3f}{v:>8.4f}{vs:>8.4f}"
                  f"{out['honest_r']:>9.4f}{out['coalition_r']:>9.4f}"
                  f"{'y' if out['pred'] else 'N':>6}"
                  f"{'y' if out['honest_ok'] else 'N':>10}"
                  f"{_flags(out, v < vs)}")
    print("  The gate's resolution is the honest derivation variance σ²/k.")
    print("  Refusing the predictor on a world of innovation q costs every")
    print("  honest participant k ≥ c σ²/q derivations per prompt; a")
    print("  predictable world is expensive to evidence in proportion to how")
    print("  little there is to evidence.")


def part_five_fresh():
    print("\n" + "=" * 74)
    print("PART 5 — FRESH PROMPTS: the bound is on recorded prompts")
    print("=" * 74)
    n, edges, _, _, _ = _setup(shared=False)
    deg = np.zeros(n)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    C = set(range(BLOCK))
    inside, bd = boundary(edges, C)
    print(f"  {'prompts':<11}{'φ':>5}{'record':>8}{'honest r':>9}"
          f"{'coal. r':>9}{'pass':>6}{'e(C)':>8}{'designed':>10}")
    for shared in (False, True):
        b = (256 - BLOCK) if shared else 1
        for phi in (0.9, 0.99):
            for fresh in (False, True):
                out = run_memory(shared, phi, DELTA_ABS, C, "kalman",
                                 fresh=fresh)
                w_C = K * M * (sum(deg[x] for x in C) if not shared
                               else len(C)) * out["scored"]
                cost = 0.0 if out["pred"] else out["cost_derive"]
                designed = 1 / len(C) if shared else \
                    len(bd) / (2 * len(inside) + len(bd))
                v, _ = riccati_steady(phi, DELTA_ABS, S, b)
                pp = (not fresh) and v < v_star(TOL, S, out["n_gated"])
                print(f"  {'shared' if shared else 'edge-local':<11}{phi:>5.2f}"
                      f"{'none' if fresh else 'full':>8}"
                      f"{out['honest_r']:>9.4f}{out['coalition_r']:>9.4f}"
                      f"{'y' if out['pred'] else 'N':>6}{cost / w_C:>8.4f}"
                      f"{designed:>10.4f}{_flags(out, pp)}")
    print("  A prompt with no record cannot be predicted from one. Rotating")
    print("  the prompts restores the pool at any memory, at the semantic")
    print("  cost Every Basis at Once §8.1 named and did not price.")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    part_one_calibration()
    part_two_attackers()
    part_three_sweep()
    part_four_resolution()
    part_five_fresh()
