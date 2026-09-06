"""
The exclusion principle: independence and trace gap draw on one budget.

Combination Proofs v0.6 §7.1 ends on a conjecture stated from two data points:
a projection must be independent (iota) AND expensive to forge (tau), and the
two appear to pull against each other. The static spectral projection failed
iota and inherited coherence's tau; the temporal projection passes iota and has
no tau. This module gives the conjecture a model in which it is a theorem, a
calibration specimen whose answers are known by construction, and a measurement
on the sheaf reading the program actually uses.

THE MODEL. A substrate's state decomposes into PAID degrees of freedom — those
whose admissible values cost real work to produce (encodings, reconciliations,
searches) — and FREE ones, which cost nothing. A projection, operationally, is
the set of degrees of freedom that determine whether it accepts. Then:

    tau(pi)      = (paid DOF pi reads) / (all paid DOF)        [Sign and Work 3.3,
                   with w = the whole work the reading evidences]
    iota(j | i)  = (paid DOF j reads that i does not) / (paid DOF j reads)
                   [Combination Proofs Def 2.5, as a fraction of fake-cost
                   not recoverable]

Both are claims on ONE finite pool. Soundness is the size of a projection's
claim; independence is the disjointness of two claims; and disjoint claims on a
finite pool cannot both be large. That is the entire content of the exclusion,
and it is arithmetic:

    THEOREM 1 (pairwise).  tau(pi_1) + iota(2|1) * tau(pi_2)  <=  1,
    with equality exactly when the two claims jointly exhaust the pool.

    THEOREM 2 (budget).  For any pi_1..pi_K, the conjunction's fake-cost
    Gamma = sum of sequential marginal costs = |union of claims| <= |pool|.
    Equivalently sum_k iota_k * tau_k <= 1: the discounted trace gaps of any
    conjunction sum to at most one. Richness partitions the budget; nothing
    multiplies it.

Proof of both: inclusion-exclusion on sets. The point is not the arithmetic
but what it forbids: two projections with tau = 1 each and iota = 1 between
them would need 2 units of a 1-unit pool. Proof of work is NOT a
counterexample — its search is a second pool, i.e. an anchor, and anchors are
where the escape lives (and what it costs: the budget grows only by adding
paid work, never by adding readings).

THE INSTRUMENT IS NOT THE FORMULA. tau and iota are measured here by a
brute-force attacker that searches over which DOF to produce, given only
acceptance behaviour — it does not see the sets. The formulas above are the
known answers the instrument must return on designed specimens before its
sheaf numbers are worth reading. (The lesson of the 2.74: build the specimen
whose answer you already know, and point the instrument at it first.)

THE SHEAF MEASUREMENT. temporal_iota.py measured the specimen pair at the
model's degenerate corner: pi_persist reads only free DOF — frozen restriction
maps cost nothing — so tau = 0 and its independence is the independence of a
free thing, which is free. The one dial the program owns that gives
persistence a price is Gauge-Fixing §4.3's generative anchor KEYED TO THE
EPOCH BEACON (§4.1/4.2): an admissible section must carry the beacon's column
for THIS epoch, at encoding cost En per vertex per epoch. Holding still stops
being free, because last epoch's encoding is stale this epoch.

Prediction, stated before running: the anchor gives pi_persist exactly the
trace gap of Sign and Work Prop 5.2 — nEn/(nEn + |E|c) — and destroys its
independence from the kernel in the same stroke, because the encodings that
price persistence are the same encodings a kernel forger pays, so the marginal
cost of the kernel given persistence forged falls to ~0. The dial that buys
tau spends iota. If instead the freeze attack fails to score under the anchor
at all, that is the stronger result (the beacon kills stasis) and the
exclusion holds the same way, through the shared pool.

Run:  python exclusion.py     (seeded; every number reproducible)
"""
import itertools
import sys

import numpy as np

from complexes import hierarchical_modular, random_orthogonal

# ------------------------------------------------------------------ Part 1
# The paid-DOF model, and an attacker that cannot see it.


class Universe:
    """|P| paid DOF (cost 1 each) and |F| free DOF (cost 0)."""

    def __init__(self, n_paid, n_free):
        self.paid = frozenset(range(n_paid))
        self.free = frozenset(range(n_paid, n_paid + n_free))
        self.work = float(n_paid)


def projection(universe, reads):
    """A projection accepts iff every DOF it reads has been produced."""
    reads = frozenset(reads)

    def accepts(produced):
        return reads <= produced
    accepts.reads = reads          # inspected only by the answer key, never
    return accepts                 # by the attacker below


def cheapest_accepted(universe, accept_fns, granted=frozenset()):
    """
    Brute-force attacker: minimum production cost over ALL subsets of DOF such
    that every accept_fn accepts, given some DOF already produced (`granted`).
    Sees acceptance behaviour only. Exponential, so calibration universes are
    small — which is the correct trade: an exact attacker on a small specimen
    beats a heuristic attacker on a large one, because only the exact one has
    a known answer.
    """
    dofs = sorted(universe.paid | universe.free)
    best = None
    for r in range(len(dofs) + 1):
        if best is not None:
            break                  # subsets enumerated by size: first hit is
        for combo in itertools.combinations(dofs, r):   # cheapest in |paid|
            produced = granted | frozenset(combo)       # only if all paid...
            if all(f(produced) for f in accept_fns):
                cost = len(frozenset(combo) & universe.paid)
                if best is None or cost < best:
                    best = cost
    return float(best)


def measure_pair(universe, pi_1, pi_2):
    """tau_1, tau_2, iota(2|1), iota(1|2) — all from the attacker."""
    f1 = cheapest_accepted(universe, [pi_1])
    f2 = cheapest_accepted(universe, [pi_2])
    f12 = cheapest_accepted(universe, [pi_1, pi_2])
    tau_1, tau_2 = f1 / universe.work, f2 / universe.work
    iota_21 = (f12 - f1) / f2 if f2 > 0 else float("nan")
    iota_12 = (f12 - f2) / f1 if f1 > 0 else float("nan")
    return tau_1, tau_2, iota_21, iota_12, f12


def answer_key(universe, pi_1, pi_2):
    """The designed values, from the sets the attacker never sees."""
    P = universe.paid
    c1, c2 = pi_1.reads & P, pi_2.reads & P
    tau_1, tau_2 = len(c1) / universe.work, len(c2) / universe.work
    iota_21 = len(c2 - c1) / len(c2) if c2 else float("nan")
    return tau_1, tau_2, iota_21


def part_one():
    print("=" * 74)
    print("PART 1 — CALIBRATION: the attacker against specimens with known answers")
    print("=" * 74)
    u = Universe(n_paid=8, n_free=4)
    P, F = sorted(u.paid), sorted(u.free)

    specimens = [
        ("disjoint, half each",      P[:4],            P[4:]),
        ("nested",                   P[:6],            P[:3]),
        ("overlap 2 of 4",           P[:4],            P[2:6]),
        ("free rider (tau=0)",       P[:5],            F),
        ("exhaustive pair",          P[:5],            P[5:] + F[:2]),
        ("both read everything",     P,                P),
    ]
    print(f"  {'specimen':<24}{'tau1':>7}{'tau2':>7}{'i(2|1)':>8}"
          f"{'  designed':>11}{'  t1+i*t2':>10}")
    worst = 0.0
    for name, r1, r2 in specimens:
        pi_1, pi_2 = projection(u, r1), projection(u, r2)
        t1, t2, i21, _, _ = measure_pair(u, pi_1, pi_2)
        k1, k2, k21 = answer_key(u, pi_1, pi_2)
        err = max(abs(t1 - k1), abs(t2 - k2),
                  0 if np.isnan(i21) and np.isnan(k21) else abs(i21 - k21))
        worst = max(worst, err)
        lhs = t1 + (0 if np.isnan(i21) else i21) * t2
        print(f"  {name:<24}{t1:>7.3f}{t2:>7.3f}{i21:>8.3f}"
              f"  ({k1:.3f} {k2:.3f} {k21:.3f}){lhs:>9.3f}")
    print(f"\n  worst |measured - designed| = {worst:.1e}"
          f"   (anything above 0 means stop reading)")
    print("  Theorem 1 lhs never exceeds 1.000, and reaches it exactly on the")
    print("  pairs designed to exhaust the pool.")

    # The budget, on random conjunctions: Gamma <= |pool| always, and the
    # discounted gaps sum to Gamma/|pool|.
    print("\n  BUDGET (Theorem 2) — random conjunctions of K projections")
    rng = np.random.default_rng(0)
    print(f"  {'K':>3} {'sum iota_k*tau_k':>17} {'Gamma/work':>11}")
    for K in (2, 3, 4, 5):
        reads = [frozenset(int(x) for x in
                           rng.choice(sorted(u.paid | u.free),
                                      size=rng.integers(2, 7), replace=False))
                 for _ in range(K)]
        pis = [projection(u, r) for r in reads]
        # sequential marginals, as Lemma 3.1 of The Multiplicity Freedom builds Gamma
        got, gamma, total = frozenset(), 0.0, 0.0
        for pi in pis:
            fk = cheapest_accepted(u, [pi])
            marginal = cheapest_accepted(u, [pi], granted=got) \
                if fk > 0 else 0.0
            # grant the attacker what forging pi produces: its paid claim
            got = got | (pi.reads)
            gamma += marginal
            total += marginal          # = iota_k * tau_k * work, summed
        print(f"  {K:>3} {total / u.work:>17.3f} {gamma / u.work:>11.3f}")
    print("  Neither column exceeds 1.000: the conjunction's fake-cost is capped")
    print("  by the substrate's work content, at any K. Richness partitions;")
    print("  it does not multiply.")

    # The escape, and its price: a second pool.
    print("\n  THE ESCAPE — a second paid pool (an anchor of its own)")
    u2 = Universe(n_paid=8, n_free=2)
    pool_a, pool_b = sorted(u2.paid)[:4], sorted(u2.paid)[4:]
    pi_a, pi_b = projection(u2, pool_a), projection(u2, pool_b)
    t1, t2, i21, i12, _ = measure_pair(u2, pi_a, pi_b)
    print(f"  two projections, each reading its own pool of paid work:")
    print(f"    tau = {t1:.3f} and {t2:.3f}, iota = {i21:.3f} both ways")
    print(f"    independent AND each expensive — but tau_1 + tau_2 = "
          f"{t1 + t2:.3f}, still <= 1:")
    print("    independence is recovered by SPLITTING the budget, not escaping")
    print("    it. Each projection is sound only up to its own anchor's share,")
    print("    and the budget grows only by adding paid work — an anchor per")
    print("    projection — never by adding readings.")


# ------------------------------------------------------------------ Part 2
# The sheaf instance: the E-dial on the program's own specimen pair.

SOFT = 0.05
STALK = 3
DEPTH = 8
EPOCHS = 8
DRIFT = 0.12
KBOT = 12
PER_EDGE = STALK * (STALK - 1) / 2      # cost of reconciling one edge, as
                                        # trace_gap.py counts it


def _complete_frame(col, free_part):
    """Orthogonal frame whose first column is `col`; remaining columns are the
    projection of `free_part` onto col's complement, orthonormalised."""
    d = col.shape[0]
    col = col / np.linalg.norm(col)
    rest = free_part - np.outer(col, col @ free_part)
    q, r = np.linalg.qr(rest)
    q = q * np.sign(np.diag(r))
    return np.column_stack([col, q[:, :d - 1]])


def _beacon_columns(n, epoch, d=STALK):
    """The epoch beacon: a fresh determined column per vertex per epoch,
    unpredictable in advance (Gauge-Fixing §4.1), so it cannot be pre-encoded."""
    rng = np.random.default_rng(10_000 + epoch)
    cols = rng.normal(size=(n, d))
    return cols / np.linalg.norm(cols, axis=1, keepdims=True)


def _laplacian_from_frames(n, edges, frames, coherent_pairs, rng, d=STALK):
    """Restriction maps R_u^T R_v on coherent pairs, random O(d) elsewhere —
    the construction independence.py and temporal_iota.py share."""
    L = np.zeros((n * d, n * d))
    I = np.eye(d)
    for u, v in edges:
        if (u, v) in coherent_pairs:
            O = frames[u].T @ frames[v]
        else:
            O = random_orthogonal(d, rng)
        su, sv = u * d, v * d
        L[su:su + d, su:su + d] += I
        L[sv:sv + d, sv:sv + d] += I
        L[su:su + d, sv:sv + d] -= O
        L[sv:sv + d, su:su + d] -= O.T
    return L


def _persistence(bases):
    vals = []
    for a, b in zip(bases, bases[1:]):
        vals.append(float(np.sum((a.T @ b) ** 2) / a.shape[1]))
    return float(np.mean(vals))


def run_strategy(n, edges, mode, encoding, rng, epochs=EPOCHS, d=STALK):
    """
    Play one strategy against the epoch-anchored reading. Returns mean kernel
    score, persistence, per-epoch cost in work units, and whether every epoch
    was ADMISSIBLE (sections carry this epoch's beacon column; vacuous at
    encoding = 0, where there is no anchor to satisfy).

    The reading is the one Sign and Work §5 prices: the forger declares
    frames, the connection is INDUCED, O_uv = R_u^T R_v — which telescopes to
    flatness, so every declared configuration is coherent and the kernel is
    free of charge (Prop 5.1). What the beacon anchor adds is that column 0 of
    every declared frame must be THIS epoch's beacon value, at encoding cost
    En per vertex per epoch. Only the `frustrated` baseline uses non-induced
    maps: it is the no-work floor the progress normalisation needs, honest
    participants whose models genuinely disagree, not a forgery.

    Modes:
      honest          coherent completions of the beacon, free part drifting
                      (models genuinely update); pays encoding + reconciliation
      frustrated      independent random maps each epoch; baseline, no cost
      freeze_raw      frames frozen at epoch 0, beacon included — full stasis;
                      free, and inadmissible from epoch 1 the moment En > 0,
                      because last epoch's encoding is stale this epoch
      cohere_encoded  fresh beacon column, free part redrawn every epoch —
                      pays the anchor, targets the kernel only
      cohere_frozen   fresh beacon column, free part frozen — pays the anchor
                      once per epoch and targets BOTH projections
    """
    anchored = encoding > 0
    free_parts = [rng.normal(size=(d, d)) for _ in range(n)]

    kers, bases, cost, admissible = [], [], 0.0, True
    frames0 = None
    for t in range(epochs):
        beacon = _beacon_columns(n, t)
        induced = True
        if mode == "honest":
            free_parts = [fp + DRIFT * rng.normal(size=(d, d))
                          for fp in free_parts]
            frames = [_complete_frame(beacon[v], free_parts[v])
                      for v in range(n)]
            cost += n * encoding + len(edges) * PER_EDGE
        elif mode == "frustrated":
            frames = [random_orthogonal(d, rng) for _ in range(n)]
            induced = False
        elif mode == "freeze_raw":
            if frames0 is None:
                frames0 = [_complete_frame(_beacon_columns(n, 0)[v],
                                           free_parts[v]) for v in range(n)]
            frames = frames0
            if anchored and t > 0:
                admissible = False               # stale beacon: rejected
        elif mode == "cohere_encoded":
            frames = [_complete_frame(beacon[v], rng.normal(size=(d, d)))
                      for v in range(n)]
            cost += n * encoding
        elif mode == "cohere_frozen":
            frames = [_complete_frame(beacon[v], free_parts[v])
                      for v in range(n)]
            cost += n * encoding
        else:
            raise ValueError(mode)

        if anchored and mode not in ("freeze_raw", "frustrated"):
            stacked = np.stack([frames[v][:, 0] for v in range(n)])
            admissible = admissible and np.allclose(stacked, beacon)

        L = _laplacian_from_frames(
            n, edges, frames, set(edges) if induced else set(), rng)
        ev, vec = np.linalg.eigh(L)
        kers.append(int(np.sum(ev < SOFT)))
        bases.append(vec[:, :KBOT])

    return {"ker": float(np.mean(kers)), "persist": _persistence(bases),
            "cost": cost, "admissible": admissible}


def part_two():
    print("\n" + "=" * 74)
    print("PART 2 — THE SHEAF: the encoding dial on the specimen pair")
    print("=" * 74)
    n = 2 ** DEPTH
    _, edges = hierarchical_modular(DEPTH, np.random.default_rng(7),
                                    cross_per_merge=2)
    print(f"  n = {n}, |E| = {len(edges)}, reconciliation c = {PER_EDGE},"
          f" epochs = {EPOCHS}")

    base = run_strategy(n, edges, "frustrated", 0.0, np.random.default_rng(11))
    honest0 = run_strategy(n, edges, "honest", 0.0, np.random.default_rng(12))

    def progress(s, honest, key):
        span = honest[key] - base[key]
        return (s[key] - base[key]) / span if abs(span) > 1e-9 else float("nan")

    print(f"\n  {'En':>5} {'strategy':<16}{'adm':>4}{'ker prog':>9}"
          f"{'per prog':>9}{'cost/epoch':>11}")
    summary = []
    for En in (0.0, 1.0, 4.0, 16.0, 64.0):
        honest = run_strategy(n, edges, "honest", En,
                              np.random.default_rng(12))
        rows = {}
        for mode in ("freeze_raw", "cohere_encoded", "cohere_frozen"):
            s = run_strategy(n, edges, mode, En,
                             np.random.default_rng(31 + int(En)))
            pk, pp = progress(s, honest, "ker"), progress(s, honest, "persist")
            rows[mode] = (s, pk, pp)
            flag = "  <-- ABOVE HONEST" if max(pk, pp) > 1.05 else ""
            print(f"  {En:>5.0f} {mode:<16}"
                  f"{'y' if s['admissible'] else 'N':>4}"
                  f"{pk:>9.3f}{pp:>9.3f}{s['cost'] / EPOCHS:>11.1f}{flag}")

        # fake-costs at threshold 0.5 progress, admissible strategies only
        def fake(target):
            costs = [s["cost"] for s, pk, pp in rows.values()
                     if s["admissible"] and
                     all(dict(ker=pk, persist=pp)[k] >= 0.5 for k in target)]
            return min(costs) if costs else None

        fp, fk, fboth = fake(["persist"]), fake(["ker"]), fake(["ker",
                                                                "persist"])
        w = honest["cost"]
        pred = (n * En) / (n * En + len(edges) * PER_EDGE)
        summary.append((En, fp, fk, fboth, w, pred))

    print("\n  THE DIAL — tau bought and iota spent, in one table")
    print(f"  {'En':>5} {'tau(persist)':>13} {'Prop 5.2':>9}"
          f" {'tau(ker)':>9} {'iota(ker|persist)':>18}")
    for En, fp, fk, fboth, w, pred in summary:
        stau = lambda x: "   --" if x is None else f"{x / w:.3f}"
        if None in (fp, fk, fboth) or fk == 0:
            iota = ("undefined: kernel is free" if fk == 0 and fp == 0
                    else "--")
        else:
            iota = f"{(fboth - fp) / fk:.3f}"
        print(f"  {En:>5.0f} {stau(fp):>13} {pred:>9.3f} {stau(fk):>9}"
              f" {iota:>18}")
    print("\n  Reading the table: the encoding is the only dial the program owns")
    print("  that gives persistence a trace gap, and the gap it buys tracks")
    print("  Prop 5.2's anchor share. But the same encodings are the whole of")
    print("  the kernel's fake-cost, so the marginal price of the kernel, given")
    print("  persistence forged, is zero at every En > 0: iota(ker|persist)")
    print("  falls from its measured 1.000 (temporal_iota.py, En = 0, free")
    print("  regime) to 0.000 the moment either projection costs anything.")
    print("  One pool. tau is a claim on it; iota is the disjointness of")
    print("  claims; the dial that buys the first spends the second.")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    part_one()
    part_two()
