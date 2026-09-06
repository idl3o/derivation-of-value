"""
The second pool: an anchor per projection, and whether the reading survives it.

Independent and Expensive v0.1 closed with two open problems in a stated
order. §8.4: does any temporal reading carry a signal that survives its own
anchor? — prior to — §8.2: give persistence an anchor of its own, disjoint
from the kernel's, and exhibit the first projection pair on the sheaf that is
independent AND expensive. This module runs them in that order.

THE GATE (§8.4). exclusion.py's En-dial found that under the epoch-keyed
beacon anchor full stasis scores 9.135x honest persistence, and it was
excluded by admissibility rather than by price. The reason is a gauge fact:
with induced maps O_uv = R_u^T R_v the sheaf Laplacian is (L_graph ⊗ I_3) in
the frame gauge, so the bottom eigenspace's motion between epochs IS the frame
motion R_v(t) R_v(t+1)^T — and one column in three of every frame is the
beacon, redrawn i.i.d. each epoch. Survival is defined as

    S(pi) = (honest − anchor_only) / (honest − frustrated)

with anchor_only the BEST score in the class of admissible strategies that pay
nothing but the anchor (an infimum over attackers, as The Multiplicity
Freedom v0.4 reads iota). Taking a single weak strategy as anchor_only
fabricates survival; the naive number is printed beside the honest one so the
trap is visible.

THE PURCHASE (§8.2). The second pool is Gauge-Fixing §4.2's delay chain,
modelled for the first time: per vertex per transition t−1 → t a transition
map T_v(t) ∈ O(3) whose first column is kappa_v(t) = R_v(t−1)^T beacon(t)_v —
keyed to THIS epoch's beacon and to the participant's OWN previous section —
at cost Et per vertex per transition. The static anchor (Gauge-Fixing §4.3,
exclusion.py's En) is kept: column 0 of R_v(t) is beacon(t)_v at cost En per
vertex per epoch. Two anchors, two receipts, one substrate.

The priced temporal reading is a GLUING condition, not a value read: for each
transition, the two-layer sheaf on (v,t),(v,t+1) with induced space edges in
both layers and the declared T_v as rungs; pi_persist = #{lambda < SOFT} of
its Laplacian, averaged over the seven transitions. It glues iff every
D_v = R_v(t) T_v R_v(t+1)^T coincides — H^1 on the squares vanishes — which
tolerates a global time gauge and couples neighbours, and reads nothing of the
anchor's VALUE as a certificate of order (Gauge-Fixing §5 test iv). The
overlap reading of temporal_iota.py is kept alongside, unpriced, as the
signal reading, and every strategy is scored on both.

WHAT IS ARITHMETIC AND WHAT IS MEASURED. In the induced-map model every
reading is free given its anchor (Sign and Work Prop 5.1, on both axes), and
the chain LEAKS THE BEACON: a forger paying only the chain and transporting
last epoch's frame along it arrives carrying this epoch's beacon column, at no
encoding cost. So both gates check receipt AND value, the claims are the
receipts, and the tau/iota grid below is the paid-DOF model's arithmetic
executed — it must match the designed values to every decimal, as Part 1's
miniature does, and any deviation is a gate bug rather than a finding. The
empirical content is elsewhere: WHO clears which reading, at what cost, and
whether the signal reading survives its anchor.

PREDICTIONS, STATED BEFORE RUNNING.
  1. S_glue = 0 exactly: the gluing reading is the chain read cohomologically;
     a chain-only forger scores it to the integer.
  2. S_overlap <= 0: the best static-only strategy (beacon paid, everything
     else held still) scores at least honest, so nothing of honest's excess
     over the frustrated baseline survives the anchor.
  3. The overlap reading is invariant under a GLOBAL time-dependent rotation
     (left-multiplying every frame by the same Q each epoch scores 1.000,
     as stasis does). Persistence reads uniformity of motion; uniform motion
     is a gauge; coherent change and no change are one orbit.
  4. Stasis with a paid chain is admissible for the temporal gate, scores
     ~9.1x honest on the overlap reading (the cult with a receipt), and 0 of
     18 on the gluing reading (Gauge-Fixing §4.3's non-glueability, on the
     time axis).
  5. iota = 1.000 both ways at every En, Et > 0; tau_ker = 8nEn/W and
     tau_persist = 7nEt/W with W = 8nEn + 7nEt + 8|E|c; the two gaps sum to
     1 − 8|E|c/W < 1, the shortfall being the reconciliation pool, paid by
     honest and claimed by neither reading (I&E §8.5).

WHAT CAME BACK (recorded after running; the predictions above are as
stated before). 1, 3, 4 and 5 held to the decimal. 2 held within seed
spread and not beyond it: paired on the same free parts, honest scores below
the static-only strategy on nine seeds of ten (mean S = −0.046, range −0.099
to +0.055), so the drift signal is not distinguishable from zero after the
anchor, and the control that pins the beacon shows why — the anchor removes
88% of it. The first pass of this module drew honest's free parts twice and
returned 0.1229 for a quantity exclusion.py had published as 0.1391; the
mismatch was the tell, and the draw order is now shared. A second first-pass
error: the beacon-leak check tested epoch 0, where the follower starts from
a random frame, and reported the leak absent. It is present at t = 1..7.

Run:  python two_pool.py     (seeded; every number reproducible; ~40 s)
"""
import sys

import numpy as np

from complexes import hierarchical_modular, random_orthogonal
from exclusion import (Universe, projection, measure_pair, answer_key,
                       _complete_frame, _beacon_columns, _persistence,
                       SOFT, STALK, DEPTH, EPOCHS, DRIFT, KBOT, PER_EDGE)

# The _-prefixed helpers are imported deliberately: this module extends
# exclusion.py's specimen and must share its beacon, frame completion and
# persistence reading bit for bit, or its numbers are not comparable.

TRANSITIONS = range(1, EPOCHS)          # t = 1..7, indexed by target epoch
ALL_EPOCHS = frozenset(range(EPOCHS))
ALL_TRANSITIONS = frozenset(TRANSITIONS)


# ------------------------------------------------------------ constructions

def chain_column(frame_prev, beacon_next):
    """kappa_v(t) = R_v(t-1)^T beacon(t)_v — the chain's determined column."""
    return frame_prev.T @ beacon_next


def induced_maps(n, edges, frames):
    """O_uv = R_u^T R_v for every edge — flat by construction (Prop 5.1)."""
    return [frames[u].T @ frames[v] for u, v in edges]


def spatial_laplacian(n, edges, maps, d=STALK):
    """Sheaf Laplacian from explicit restriction maps, one per edge."""
    L = np.zeros((n * d, n * d))
    I = np.eye(d)
    for (u, v), O in zip(edges, maps):
        su, sv = u * d, v * d
        L[su:su + d, su:su + d] += I
        L[sv:sv + d, sv:sv + d] += I
        L[su:su + d, sv:sv + d] -= O
        L[sv:sv + d, su:su + d] -= O.T
    return L


def two_layer_laplacian(n, edges, maps_a, maps_b, T, d=STALK):
    """
    The transition sheaf: layer a = epoch t, layer b = epoch t+1, space edges
    with their own maps in each layer, and a rung (v,a)–(v,b) per vertex with
    restriction map T_v, unit weight. Flat spectrum is {lambda_graph} ∪
    {lambda_graph + 2}, so the rung branch never approaches SOFT and the
    reading counts spatial modes that survive the transition.
    """
    N = n * d
    L = np.zeros((2 * N, 2 * N))
    L[:N, :N] = spatial_laplacian(n, edges, maps_a, d)
    L[N:, N:] = spatial_laplacian(n, edges, maps_b, d)
    I = np.eye(d)
    for v in range(n):
        a, b = v * d, N + v * d
        L[a:a + d, a:a + d] += I
        L[b:b + d, b:b + d] += I
        L[a:a + d, b:b + d] -= T[v]
        L[b:b + d, a:a + d] -= T[v].T
    return L


# --------------------------------------------------------------- strategies

def _transition_maps(n, frames_prev, t, rng):
    """Paid chain maps: first column kappa, remainder still (rng None) or
    random."""
    b = _beacon_columns(n, t)
    out = []
    for v in range(n):
        fp = np.eye(STALK) if rng is None else rng.normal(size=(STALK, STALK))
        out.append(_complete_frame(chain_column(frames_prev[v], b[v]), fp))
    return out


def _induced_T(n, frames):
    """The honest transition: T_v(t) = R_v(t-1)^T R_v(t), which carries kappa
    automatically."""
    return {t: [frames[t - 1][v].T @ frames[t][v] for v in range(n)]
            for t in TRANSITIONS}


def _identity_T(n):
    return {t: [np.eye(STALK)] * n for t in TRANSITIONS}


def _beacon_frames(n, free_parts, pin=None):
    """Frames whose column 0 is the epoch beacon (or epoch `pin`'s), free part
    fixed per vertex."""
    return [[_complete_frame(_beacon_columns(n, t if pin is None else pin)[v],
                             free_parts[v]) for v in range(n)]
            for t in range(EPOCHS)]


def _drifting_frames(n, fps, rng, pin=None):
    """exclusion.py's honest participant: free parts drift, beacon fresh.
    Same draw order as exclusion.run_strategy, so seed 12 reproduces it."""
    frames = []
    for t in range(EPOCHS):
        fps = [fp + DRIFT * rng.normal(size=(STALK, STALK)) for fp in fps]
        b = _beacon_columns(n, t if pin is None else pin)
        frames.append([_complete_frame(b[v], fps[v]) for v in range(n)])
    return frames


def _following_frames(n, rng, still):
    """Pay only the chain and transport the frame along it. Column 0 arrives
    as beacon(t) by value — the leak — without any static encoding paid."""
    frames = [[random_orthogonal(STALK, rng) for _ in range(n)]]
    T = {}
    for t in TRANSITIONS:
        T[t] = _transition_maps(n, frames[t - 1], t, None if still else rng)
        frames.append([frames[t - 1][v] @ T[t][v] for v in range(n)])
    return frames, T


def _static_strategies(mode, n, fps, rng):
    """Strategies that pay the static anchor, or nothing: frames, T,
    receipts."""
    S, C = ALL_EPOCHS, ALL_TRANSITIONS
    if mode == "freeze_raw":
        return _beacon_frames(n, fps, pin=0), _identity_T(n), set(), set()
    if mode == "static_encoded":
        frames = [[_complete_frame(_beacon_columns(n, t)[v],
                                   rng.normal(size=(STALK, STALK)))
                   for v in range(n)] for t in range(EPOCHS)]
        return frames, _identity_T(n), S, set()
    if mode == "static_frozen":
        return _beacon_frames(n, fps), _identity_T(n), S, set()
    if mode == "static_frozen_declared":          # honest T, chain unpaid
        frames = _beacon_frames(n, fps)
        return frames, _induced_T(n, frames), S, set()
    if mode == "pay_both":
        frames = _beacon_frames(n, fps)
        return frames, _induced_T(n, frames), S, C
    return None


def _chain_strategies(mode, n, fps, rng):
    """Strategies that pay the chain and not the static anchor."""
    C = ALL_TRANSITIONS
    if mode == "chain_random":
        frames = [[random_orthogonal(STALK, rng) for _ in range(n)]
                  for _ in range(EPOCHS)]
        T = {t: _transition_maps(n, frames[t - 1], t, rng)
             for t in TRANSITIONS}
        return frames, T, set(), C
    if mode in ("chain_follow_still", "chain_follow_rand"):
        frames, T = _following_frames(n, rng, mode.endswith("still"))
        return frames, T, set(), C
    if mode in ("stasis_paid_still", "stasis_paid_rand"):
        frames = _beacon_frames(n, fps, pin=0)
        T = {t: _transition_maps(n, frames[0], t,
                                 None if mode.endswith("still") else rng)
             for t in TRANSITIONS}
        return frames, T, set(), C
    return None


def _control_strategies(mode, n, fps, rng):
    """Controls: never enter the fake-cost table."""
    if mode == "honest_frozen_beacon":
        frames = _drifting_frames(n, fps, rng, pin=0)
        return frames, _induced_T(n, frames), ALL_EPOCHS, ALL_TRANSITIONS
    if mode == "global_rotation":                 # the temporal gauge
        frames = [_beacon_frames(n, fps, pin=0)[0]]
        for t in TRANSITIONS:
            Q = random_orthogonal(STALK, rng)
            frames.append([Q @ f for f in frames[t - 1]])
        return frames, _induced_T(n, frames), set(), set()
    return None


def play(mode, n, edges, rng):
    """
    One strategy, played over eight epochs. Returns declared frames, declared
    transition maps, per-edge space maps, and the receipts held: which epochs'
    static encodings and which transitions' chain encodings were PAID for.
    Every strategy draws `free_parts` first, as exclusion.run_strategy does,
    so seeds shared with that module reproduce its frames.
    """
    fps = [rng.normal(size=(STALK, STALK)) for _ in range(n)]
    recon, maps, control = False, None, False
    if mode == "honest":
        frames = _drifting_frames(n, fps, rng)
        T, static, chain, recon = _induced_T(n, frames), ALL_EPOCHS,             ALL_TRANSITIONS, True
    elif mode == "frustrated":                      # exclusion's draw order
        frames, maps = [], []
        for t in range(EPOCHS):
            frames.append([random_orthogonal(STALK, rng) for _ in range(n)])
            maps.append([random_orthogonal(STALK, rng) for _ in edges])
        T, static, chain = _identity_T(n), set(), set()
    else:
        built = (_static_strategies(mode, n, fps, rng)
                 or _chain_strategies(mode, n, fps, rng))
        if built is None:
            built, control = _control_strategies(mode, n, fps, rng), True
        if built is None:
            raise ValueError(mode)
        frames, T, static, chain = built
    if maps is None:
        maps = [induced_maps(n, edges, frames[t]) for t in range(EPOCHS)]
    return {"mode": mode, "frames": frames, "T": T, "maps": maps,
            "static": frozenset(static), "chain": frozenset(chain),
            "recon": recon, "control": control}


# ------------------------------------------------------------------ reading

def _free_overlap(bases, frames, n, d=STALK):
    """The overlap reading with the anchor gauged out: every eigenvector's
    stalk component along the beacon column is removed before comparing."""
    vals = []
    projected = []
    for V, fr in zip(bases, frames):
        P = np.zeros_like(V)
        for v in range(n):
            F = fr[v][:, 1:]                       # ambient free complement
            P[v * d:(v + 1) * d] = F @ (F.T @ V[v * d:(v + 1) * d])
        q, _ = np.linalg.qr(P)
        projected.append(q)
    for a, b in zip(projected, projected[1:]):
        vals.append(float(np.sum((a.T @ b) ** 2) / a.shape[1]))
    return float(np.mean(vals))


def score(n, edges, played):
    """ker (spatial, per epoch), glue (two-layer, per transition), overlap
    and free_overlap (temporal_iota's reading, full and anchor-gauged-out)."""
    kers, bases = [], []
    for t in range(EPOCHS):
        ev, vec = np.linalg.eigh(spatial_laplacian(n, edges, played["maps"][t]))
        kers.append(int(np.sum(ev < SOFT)))
        bases.append(vec[:, :KBOT])
    glues, lmins = [], []
    for t in TRANSITIONS:
        ev = np.linalg.eigvalsh(two_layer_laplacian(
            n, edges, played["maps"][t - 1], played["maps"][t],
            played["T"][t]))
        glues.append(int(np.sum(ev < SOFT)))
        lmins.append(float(ev[0]))
    return {"ker": float(np.mean(kers)), "glue": float(np.mean(glues)),
            "glue_lmin": float(np.min(lmins)) if min(glues) == 0
            else float("nan"),
            "overlap": _persistence(bases),
            "free_overlap": _free_overlap(bases, played["frames"], n)}


# -------------------------------------------------------------------- gates

def values_match(played, n):
    """Which epochs' frames carry that epoch's beacon in column 0, and which
    transitions' declared T carry kappa. Value checks only — receipts aside."""
    static = frozenset(t for t in range(EPOCHS) if np.allclose(
        np.stack([played["frames"][t][v][:, 0] for v in range(n)]),
        _beacon_columns(n, t)))
    chain = frozenset(t for t in TRANSITIONS if all(np.allclose(
        played["T"][t][v][:, 0],
        chain_column(played["frames"][t - 1][v], _beacon_columns(n, t)[v]))
        for v in range(n)))
    return static, chain


def admissible(played, values, En, Et):
    """Receipt AND value, per gate; a zero-cost gate is vacuous, as
    exclusion.py's `anchored = encoding > 0`."""
    static_ok = En == 0 or (played["static"] == ALL_EPOCHS
                            and values[0] == ALL_EPOCHS)
    chain_ok = Et == 0 or (played["chain"] == ALL_TRANSITIONS
                           and values[1] == ALL_TRANSITIONS)
    return static_ok, chain_ok


def cost(played, En, Et, n, m):
    return (n * En * len(played["static"]) + n * Et * len(played["chain"])
            + EPOCHS * m * PER_EDGE * played["recon"])


def designed(En, Et, n, m):
    """The paid-DOF model's answer: two disjoint receipts on one budget."""
    W = EPOCHS * n * En + (EPOCHS - 1) * n * Et + EPOCHS * m * PER_EDGE
    return {"W": W, "tau_ker": EPOCHS * n * En / W,
            "tau_persist": (EPOCHS - 1) * n * Et / W}


def fake_costs(table, En, Et, n, m, reading):
    """f_ker, f_persist, f_both at >= 0.5 progress, admissible only, over the
    written-down strategy class (controls excluded). Returns (cost, who)."""
    def best(need_static, need_chain, keys):
        found = []
        for played, s, prog, values in table:
            if played["control"]:
                continue
            ok_s, ok_c = admissible(played, values, En, Et)
            if (need_static and not ok_s) or (need_chain and not ok_c):
                continue
            if all(prog[k] >= 0.5 for k in keys):
                found.append((cost(played, En, Et, n, m), played["mode"]))
        return min(found) if found else (None, "--")
    return {"ker": best(True, False, ["ker"]),
            "persist": best(False, True, [reading]),
            "both": best(True, True, ["ker", reading])}


# -------------------------------------------------------------------- parts

def part_one_model():
    print("=" * 74)
    print("PART 1 — CALIBRATION (model): three pools, two read, one unclaimed")
    print("=" * 74)
    u = Universe(n_paid=8, n_free=2)
    P = sorted(u.paid)
    pi_s, pi_t = projection(u, P[:3]), projection(u, P[3:6])   # P[6:8] unread
    t1, t2, i21, i12, _ = measure_pair(u, pi_s, pi_t)
    k1, k2, k21 = answer_key(u, pi_s, pi_t)
    worst = max(abs(t1 - k1), abs(t2 - k2), abs(i21 - k21))
    print(f"  static pool 3, transition pool 3, reconciliation pool 2 (read by")
    print(f"  neither), free 2.  measured tau = {t1:.3f} {t2:.3f}, iota = "
          f"{i21:.3f} {i12:.3f}, sum = {t1 + t2:.3f}")
    print(f"  designed tau = {k1:.3f} {k2:.3f}, iota = {k21:.3f};"
          f" sum = 1 − 2/8 = 0.750")
    print(f"  worst |measured − designed| = {worst:.1e}"
          f"   (anything above 0 means stop reading)")
    return worst


def build_table(n, edges):
    """Score every strategy once: readings do not depend on En or Et."""
    seeds = {"honest": 12, "frustrated": 11, "freeze_raw": 32,
             "static_encoded": 32, "static_frozen": 32,
             "static_frozen_declared": 32, "chain_random": 41,
             "chain_follow_still": 42, "chain_follow_rand": 43,
             "pay_both": 32, "stasis_paid_still": 32, "stasis_paid_rand": 44,
             "honest_frozen_beacon": 12, "global_rotation": 45}
    table = []
    for mode, seed in seeds.items():
        played = play(mode, n, edges, np.random.default_rng(seed))
        s = score(n, edges, played)
        table.append([played, s, None, values_match(played, n)])
    base = next(s for p, s, _, _ in table if p["mode"] == "frustrated")
    honest = next(s for p, s, _, _ in table if p["mode"] == "honest")
    for row in table:
        row[2] = {k: (row[1][k] - base[k]) / (honest[k] - base[k])
                  if abs(honest[k] - base[k]) > 1e-9 else float("nan")
                  for k in ("ker", "glue", "overlap", "free_overlap")}
    return table, base, honest


def part_one_sheaf(table, n, edges):
    print("\n  CALIBRATION (sheaf): facts the construction must reproduce")
    get = {p["mode"]: (p, s, prog, vals) for p, s, prog, vals in table}
    honest = get["honest"]
    follow = get["chain_follow_still"]
    checks = [
        ("honest T carries kappa at every transition",
         honest[3][1] == ALL_TRANSITIONS),
        ("honest glue == honest spatial ker (flat both ways)",
         honest[1]["glue"] == honest[1]["ker"]),
        ("frustrated glues nothing", get["frustrated"][1]["glue"] == 0),
        ("freeze_raw + T = I glues (didn't move, says so)",
         get["freeze_raw"][1]["glue"] == honest[1]["glue"]),
        ("chain_follow carries beacon(t) BY VALUE at t = 1..7, no receipt",
         follow[3][0] == ALL_TRANSITIONS and not follow[0]["static"]),
        ("global rotation scores overlap 1.000 (the temporal gauge)",
         abs(get["global_rotation"][1]["overlap"] - 1.0) < 1e-6),
        ("stasis_paid glues nothing (Gauge-Fixing §4.3 on the time axis)",
         get["stasis_paid_still"][1]["glue"] == 0),
    ]
    ok = True
    for name, passed in checks:
        ok = ok and bool(passed)
        print(f"    [{'ok' if passed else 'FAIL'}] {name}")
    print(f"    stasis_paid smallest two-layer eigenvalue: "
          f"{get['stasis_paid_still'][1]['glue_lmin']:.3f}"
          f"  (SOFT = {SOFT}; below 3·SOFT would be a leak)")
    return ok


def part_two(table):
    print("\n" + "=" * 74)
    print("PART 2 — WHO CLEARS WHICH READING (cost-free; receipts shown)")
    print("=" * 74)
    print(f"  {'strategy':<24}{'rcpt':>6}{'ker':>7}{'glue':>7}{'overlap':>9}"
          f"{'free_ov':>9}{'  ker':>6}{' glue':>6}{'  ovl':>6}")
    for p, s, prog, vals in table:
        rc = f"{'S' if p['static'] else '-'}{'C' if p['chain'] else '-'}"
        flag = ""
        if max(prog["ker"], prog["glue"], prog["overlap"]) > 1.05:
            flag = "  <-- ABOVE HONEST"
        elif min(prog["ker"], prog["glue"], prog["overlap"]) < -0.05:
            flag = "  <-- BELOW BASELINE"
        ctl = " (control)" if p["control"] else ""
        print(f"  {p['mode'] + ctl:<24}{rc:>6}{s['ker']:>7.1f}{s['glue']:>7.1f}"
              f"{s['overlap']:>9.4f}{s['free_overlap']:>9.4f}"
              f"{prog['ker']:>6.2f}{prog['glue']:>6.2f}{prog['overlap']:>6.2f}"
              f"{flag}")
    print("  rcpt: S = static encodings paid (8 epochs), C = chain paid (7")
    print("  transitions). Progress columns are (s − frustrated)/(honest −")
    print("  frustrated) per reading. Values matching a gate without a receipt")
    print("  are what the chain leaks; receipts are what the gates price.")


def part_three(table, base, honest, n, edges):
    print("\n" + "=" * 74)
    print("PART 3 — THE GATE (I&E §8.4): does the reading survive its anchor?")
    print("=" * 74)
    get = {p["mode"]: s for p, s, _, _ in table}
    static_only = ("static_encoded", "static_frozen", "static_frozen_declared")
    chain_only = ("chain_random", "chain_follow_still", "chain_follow_rand")

    def S(reading, cls):
        best = max(get[m][reading] for m in cls)
        span = honest[reading] - base[reading]
        return (honest[reading] - best) / span, best

    s_ov, b_ov = S("overlap", static_only)
    s_gl, b_gl = S("glue", chain_only)
    s_naive = (honest["overlap"] - get["chain_follow_still"]["overlap"]) / \
        (honest["overlap"] - base["overlap"])
    fb = get["honest_frozen_beacon"]["overlap"]
    retention = (honest["overlap"] - base["overlap"]) / (fb - base["overlap"])
    print(f"  overlap reading vs its static anchor (main table, seed 12 vs 32):")
    print(f"    honest {honest['overlap']:.4f}  frustrated {base['overlap']:.4f}"
          f"  best static-only {b_ov:.4f}  ->  S_overlap = {s_ov:+.3f}")
    print(f"    honest with beacon pinned at epoch 0 (drift kept): {fb:.4f}")
    print(f"    retention of the drift signal through the anchor: "
          f"{retention:.3f}")
    print(f"    naive S using chain_follow as 'anchor only': {s_naive:+.3f}"
          f"   <-- the wrong instrument")
    s_paired = _paired_survival(n, edges, base)
    print(f"  gluing reading vs its chain anchor:")
    print(f"    honest {honest['glue']:.1f}  frustrated {base['glue']:.1f}"
          f"  best chain-only {b_gl:.1f}  ->  S_glue = {s_gl:+.3f}")
    print(f"  stasis on the free complement (anchor gauged out): "
          f"{get['stasis_paid_still']['free_overlap']:.4f}"
          f" vs honest {honest['free_overlap']:.4f}")
    flags = []
    if np.mean(s_paired) > 0.05 or min(s_paired) > 0:
        flags.append("paired S_overlap > 0 beyond seed spread: a signal"
                     " survives — check the class")
    if abs(s_gl) > 1e-9:
        flags.append("S_glue != 0: the gluing reading has a leak")
    if s_naive > 1:
        flags.append("(expected) naive S > 1: the trap, printed on purpose")
    for f in flags:
        print(f"    ! {f}")
    return s_paired, s_gl


def _paired_survival(n, edges, base, seeds=(12, 32, 41, 42, 43, 44, 45, 46,
                                            47, 48)):
    """Honest and the best static-only strategy on the SAME free parts, per
    seed. Honest is static_frozen plus drift, so whatever honest adds is
    drift, and the sign of S says whether drift can add overlap at all."""
    print(f"  paired over seeds — honest vs static_frozen on the same free"
          f" parts:")
    print(f"  {'seed':>6}{'honest':>9}{'static':>9}{'S':>8}")
    out = []
    for seed in seeds:
        h = score(n, edges, play("honest", n, edges,
                                 np.random.default_rng(seed)))["overlap"]
        f = score(n, edges, play("static_frozen", n, edges,
                                 np.random.default_rng(seed)))["overlap"]
        s = (h - f) / (h - base["overlap"])
        out.append(s)
        print(f"  {seed:>6}{h:>9.4f}{f:>9.4f}{s:>+8.3f}")
    print(f"  S_overlap paired: mean {np.mean(out):+.3f}, "
          f"min {min(out):+.3f}, max {max(out):+.3f}, "
          f"{sum(s > 0 for s in out)} of {len(out)} seeds positive")
    return out


def part_four(table, n, m, reading, title):
    print("\n" + "=" * 74)
    print(f"PART 4 — THE PURCHASE (I&E §8.2), persistence read as {title}")
    print("=" * 74)
    print(f"  {'En':>4}{'Et':>4}{'tau_ker':>9}{'pred':>7}{'tau_per':>9}"
          f"{'pred':>7}{'i(k|p)':>8}{'i(p|k)':>8}{'sum':>7}{'1-recon':>9}"
          f"  who clears persist / both")
    worst = 0.0
    for En in (0.0, 1.0, 4.0, 16.0):
        for Et in (0.0, 1.0, 4.0, 16.0):
            d = designed(En, Et, n, m)
            f = fake_costs(table, En, Et, n, m, reading)
            fk, fp, fb = f["ker"][0], f["persist"][0], f["both"][0]
            if None in (fk, fp, fb):
                print(f"  {En:>4.0f}{Et:>4.0f}   no admissible forger for a"
                      f" target ({f})")
                continue
            tk, tp = fk / d["W"], fp / d["W"]
            ikp = (fb - fp) / fk if fk > 0 else float("nan")
            ipk = (fb - fk) / fp if fp > 0 else float("nan")
            worst = max(worst, abs(tk - d["tau_ker"]), abs(tp - d["tau_persist"]))
            flag = ""
            if tk + tp > 1 + 1e-9:
                flag = "  <-- BUDGET VIOLATED"
            elif fb < max(fk, fp):
                flag = "  <-- CONJUNCTION CHEAPER THAN A CONJUNCT"
            elif En > 0 and fk < EPOCHS * n * En:
                flag = "  <-- BEACON LEAKED INTO THE STATIC GATE"
            fmt = lambda x: "  undef" if np.isnan(x) else f"{x:>8.3f}"
            print(f"  {En:>4.0f}{Et:>4.0f}{tk:>9.3f}{d['tau_ker']:>7.3f}"
                  f"{tp:>9.3f}{d['tau_persist']:>7.3f}{fmt(ikp)}{fmt(ipk)}"
                  f"{tk + tp:>7.3f}{1 - EPOCHS * m * PER_EDGE / d['W']:>9.3f}"
                  f"  {f['persist'][1]} / {f['both'][1]}{flag}")
    print(f"  worst |measured − designed tau| = {worst:.1e}"
          f"   (anything above 0 is a gate bug, not a finding)")
    print("  'undef' marks a free corner: the gate costs nothing, so the")
    print("  independence of a free thing is not a quantity (I&E §4).")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    part_one_model()
    n = 2 ** DEPTH
    _, edges = hierarchical_modular(DEPTH, np.random.default_rng(7),
                                    cross_per_merge=2)
    m = len(edges)
    print(f"\n  sheaf: n = {n}, |E| = {m}, c = {PER_EDGE}, epochs = {EPOCHS},"
          f" transitions = {EPOCHS - 1}")
    table, base, honest = build_table(n, edges)
    part_one_sheaf(table, n, edges)
    part_two(table)
    part_three(table, base, honest, n, edges)
    part_four(table, n, m, "glue", "the two-layer GLUING condition (priced)")
    part_four(table, n, m, "overlap", "the OVERLAP reading (signal, unpriced)")
    print("\n  Reading the two grids: the tau/iota arithmetic is identical under")
    print("  both readings because the claims are the receipts. What differs is")
    print("  the 'who' column — under overlap the cheapest persistence forger")
    print("  is the frozen participant with a paid chain; under gluing it is")
    print("  the follower who transports last epoch's frame. Neither did the")
    print("  work persistence was meant to evidence.")
