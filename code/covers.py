"""
Beyond the cycle: the obstruction on covers with chords, and the rings.

The Obstruction, Computed v0.2 proved that on a CYCLIC cover the Čech
obstruction of Abramsky, Mansfield and Barbosa is undirected reachability
in the bundle diagram, hence independent of the coefficient ring, and
declined to say anything about covers with chords (§9.2). This module goes
there. Three questions, each answerable by computation:

  (i)  Does ring-dependence occur? Abramsky, Barbosa, Kishida, Lal and
       Mansfield's Prop 20 gives one direction for every cover: a class
       vanishing over Z vanishes over every ring. The converse fails exactly
       where the Čech system has torsion — a solution mod 2 that does not
       lift, or a rational solution with no integer one. On a cyclic cover
       that never happens (the theorem). On a cover with chords the
       literature has no statement, and AMB's own machine checks were mod 2
       in the safe direction only (non-vanishing mod 2 implies non-vanishing
       over Z).
       A model with a Z-obstructed section whose Z_2 class vanishes would
       be a witness of contextuality that the mod-2 computation cannot
       see; a model with a Z-obstructed section whose Q class vanishes
       would be one that rational elimination cannot see.
  (ii) How does detection behave off the cycle: the same no-false-positive
       theorem, and what rates by grade.
  (iii) What a NON-CYCLIC holarchy looks like as a gate scenario, since
       two-port holons only ever make cycles: four three-port holons on K4,
       every holon in three interfaces, with a Rayleigh gate.

THE PRESHEAF ON A SIGNALLING MODEL. A gate model need not be possibilistically
no-signalling: the interface (u, v) may leave out admissible states of u
that another interface keeps. The Čech system is taken on the nerve with
the overlap's local sections the UNION of both sides' restrictions, which
is a presheaf whether or not the model signals, and it is what
contextuality.py has computed throughout. The abstract models of Part 2 are
generated no-signalling on single-measurement overlaps so that the
literature's setting is also covered.

THE ANSWER KEY (Part 1). Peres–Mermin square: rows even, two columns even,
one column odd — strongly contextual, obstructed at every section (AMB,
mod 2). GHZ, three parties: XXX even, XYY, YXY, YYX odd — strongly
contextual, obstructed at every section (AMB, mod 2). Both covers have
chords (every pair of contexts overlaps). A product model on the (3,3,2)
scenario with every section possible: nothing obstructed, everything
extends.

PREDICTIONS, STATED BEFORE RUNNING.
  1. Answer key: PM 24 of 24 sections obstructed over Z, Q and Z_2; GHZ
     16 of 16; the product model 0 of 36 and all extend. No false
     positive in any ring, ever. Prop 20 never violated: a Z-vanishing
     class vanishes over Q and over Z_2 on every section.
  2. Random no-signalling models on the (3,3,2), GHZ and PM covers: ring
     disagreement OCCURS — at least one section in the sweep obstructed
     over Z and vanishing over Z_2, and at least one obstructed over Z
     and vanishing over Q. This is the prediction most likely to fail; if
     no disagreement appears in the sweep the paper says so and the
     cyclic theorem's ring-independence is not known to be special.
  3. Detection rates by grade are below one in the logical grade on
     every cover, as on the cycles; every strongly contextual PM-cover
     and GHZ-cover model is seen.
  4. K4 holarchy with every gate exact: a global section exists iff the
     mod-2 holonomy vanishes on every cycle of K4 (three independent
     conditions), and when it does not the model is strong and every
     section is obstructed in every ring — a parity system, which is an
     all-versus-nothing argument and is witnessed (ABKLM Thm 21).
  5. K4 holarchy with a tolerance gate: misses occur; whether the ring
     matters there is (i) again, on the program's own kind of specimen.
  6. (Stated after 1–5 were run and before this one.) Gate models are
     signalling, and a state absent from one interface's support is a node
     with no edges in that layer, whose conservation forces its sums to
     zero everywhere: a route a formal family cannot use. Prediction:
     random models WITHOUT the no-signalling filter, on the same covers,
     are detected at a higher rate than the no-signalling ones, and the
     K4 holarchy's rate of one is the extreme of the same effect.

WHAT CAME BACK (recorded after running; the predictions above are as
stated before). 1 FAILED on the ring: Peres-Mermin and GHZ are obstructed
at every section over Z and over Z_2 and VANISH at every section over Q.
An independent solver (least squares on the same system, residual 1e-15)
agrees, and the rational families are explicit, with coefficients +-1/2:
the all-versus-nothing argument is a parity argument, the integer
obstruction on these models is 2-torsion, and a field of characteristic
zero cannot see it. Everything else in 1 held: no false positive in any
ring, Prop 20 never violated. 2 held for Q and failed for Z_2: three
sections of strong (3,3,2) models were obstructed over Z and vanishing
over Q; no section anywhere was obstructed over Z and vanishing over Z_2
— Z and Z_2 agreed on every one of some 60,000 sections, so mod-2
arithmetic was exact in both directions on every model here. 3 held, and
the rates on no-signalling models are far lower than on cycles: 0.074,
0.049 and 0.012 in the logical grade, with 154 of 203, 203 of 225 and
168 of 172 logical models invisible; every strong model seen. 4 held on
8 of 8. 5 FAILED: the K4 holarchy with tolerance gates has NO misses —
7,056 of 7,056 non-extending sections obstructed, all 81 logical and 7
strong models seen, all rings agreeing. 6, stated before its run, held
and explains 5: dropping the no-signalling filter raises the logical
rate from 0.074 to 0.755 on (3,3,2), 0.049 to 0.366 on the GHZ cover,
0.012 to 0.457 on the Peres-Mermin cover, and every strong signalling
model is seen. Signalling is what the invariant sees; the literature's
no-signalling setting is where it is weakest; and gate models signal.

Run:  python covers.py     (exact arithmetic; seeded; ~3 min)
"""
import sys
import itertools
import numpy as np
from contextuality import (Model, restrict, global_sections, extends, grade,
                           cech_system, integer_batch, rational_batch)

SEED = 40_000
TRIALS = 400


# ------------------------------------------------------------ mod-2 solve

def mod2_batch(A, Bs):
    """A x = b over Z_2 for each b in Bs: elimination on bit-packed rows,
    right-hand sides carried as extra bits."""
    n = len(A[0]) if A else 0
    k = len(Bs)
    rows = []
    for i, row in enumerate(A):
        v = 0
        for j, a in enumerate(row):
            if a % 2:
                v |= 1 << j
        for j, b in enumerate(Bs):
            if b[i] % 2:
                v |= 1 << (n + j)
        rows.append(v)
    r = 0
    for c in range(n):
        bit = 1 << c
        piv = next((i for i in range(r, len(rows)) if rows[i] & bit), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i] & bit:
                rows[i] ^= rows[r]
        r += 1
    mask = (1 << n) - 1
    out = []
    for j in range(k):
        bit = 1 << (n + j)
        out.append(all(not (rows[i] & bit) for i in range(r, len(rows))
                       if not (rows[i] & mask)))
    return out


def obstructions3(model, C0):
    """For every section of C0: (vanishes over Z, over Q, over Z_2)."""
    secs = sorted(model.S[C0])
    A, rhs = cech_system(model, C0)
    Bs = [rhs(s) for s in secs]
    if not A or not A[0]:
        ok = [all(v == 0 for v in b) for b in Bs]
        return dict(zip(secs, zip(ok, ok, ok)))
    return dict(zip(secs, zip(integer_batch(A, Bs), rational_batch(A, Bs),
                              mod2_batch(A, Bs))))


def audit3(model):
    globals_ = global_sections(model)
    rows = []
    for C in model.contexts:
        for s, (z, q, z2) in obstructions3(model, C).items():
            rows.append({"C": C, "s": s, "vZ": z, "vQ": q, "vZ2": z2,
                         "extends": extends(model, C, s, globals_)})
    return grade(model, globals_), rows, len(globals_)


def tally(rows, t):
    """Counts: sections, non-extending, obstructed per ring, false positives
    per ring, Prop-21 violations, and the disagreement patterns among
    non-extending sections."""
    for r in rows:
        t["sections"] += 1
        ne = not r["extends"]
        t["no_ext"] += ne
        for ring in ("Z", "Q", "Z2"):
            obs = not r["v" + ring]
            t["obs_" + ring] += obs and ne
            t["fp_" + ring] += obs and not ne
        if r["vZ"] and not (r["vQ"] and r["vZ2"]):
            t["prop21"] += 1
        if ne and not r["vZ"]:
            t["Z_only_vs_Q"] += r["vQ"]
            t["Z_only_vs_Z2"] += r["vZ2"]
            t["Q_obs_Z2_van"] += (not r["vQ"]) and r["vZ2"]
            t["Z2_obs_Q_van"] += (not r["vZ2"]) and r["vQ"]


KEYS = ("models", "sections", "no_ext", "obs_Z", "obs_Q", "obs_Z2", "fp_Z",
        "fp_Q", "fp_Z2", "prop21", "Z_only_vs_Q", "Z_only_vs_Z2",
        "Q_obs_Z2_van", "Z2_obs_Q_van", "seen", "missed")


def _print_tally(name, t):
    rate = t["obs_Z"] / t["no_ext"] if t["no_ext"] else float("nan")
    flag = ""
    if t["fp_Z"] or t["fp_Q"] or t["fp_Z2"]:
        flag += "  <-- FALSE POSITIVE"
    if t["prop21"]:
        flag += "  <-- PROP 20 VIOLATED"
    print(f"  {name:<16}{t['models']:>7}{t['sections']:>9}{t['no_ext']:>8}"
          f"{t['obs_Z']:>7}{t['obs_Q']:>7}{t['obs_Z2']:>7}{rate:>7.3f}"
          f"{t['Z_only_vs_Q']:>8}{t['Z_only_vs_Z2']:>8}{t['seen']:>6}"
          f"{t['missed']:>7}{flag}")


def _header():
    print(f"  {'grade':<16}{'models':>7}{'sections':>9}{'no ext':>8}"
          f"{'obs Z':>7}{'obs Q':>7}{'obs Z2':>7}{'rate':>7}"
          f"{'Z¬Q':>8}{'Z¬Z2':>8}{'seen':>6}{'missed':>7}")


# ------------------------------------------------------- part 1: the key

def _model(measurements, contexts, support_fn):
    O = {m: (0, 1) for m in measurements}
    sup = {}
    for C in contexts:
        sup[C] = {t for t in itertools.product((0, 1), repeat=len(C))
                  if support_fn(C, t)}
    return Model([(m, O[m]) for m in measurements], contexts, sup)


def peres_mermin():
    ms = [f"m{i}{j}" for i in range(3) for j in range(3)]
    rows = [tuple(f"m{i}{j}" for j in range(3)) for i in range(3)]
    cols = [tuple(f"m{i}{j}" for i in range(3)) for j in range(3)]
    odd = {cols[2]}
    return _model(ms, rows + cols,
                  lambda C, t: (sum(t) % 2) == (1 if C in odd else 0))


def ghz():
    ms = ["X1", "Y1", "X2", "Y2", "X3", "Y3"]
    ctx = [("X1", "X2", "X3"), ("X1", "Y2", "Y3"), ("Y1", "X2", "Y3"),
           ("Y1", "Y2", "X3")]
    return _model(ms, ctx, lambda C, t: (sum(t) % 2) == (0 if C == ctx[0]
                                                         else 1))


def scenario_332():
    ms = ["a1", "a2", "a3", "b1", "b2", "b3"]
    ctx = [(a, b) for a in ms[:3] for b in ms[3:]]
    return ms, ctx


def product_332():
    ms, ctx = scenario_332()
    return _model(ms, ctx, lambda C, t: True)


def _key_row(name, model, expect):
    g, rows, n_glob = audit3(model)
    t = dict.fromkeys(KEYS, 0)
    tally(rows, t)
    got = (g, t["no_ext"], t["obs_Z"], t["obs_Q"], t["obs_Z2"])
    flag = "" if got == expect else "  <-- stop reading"
    if t["fp_Z"] or t["fp_Q"] or t["fp_Z2"]:
        flag += "  <-- FALSE POSITIVE"
    print(f"  {name:<16}{g:<16}{len(rows):>9}{t['no_ext']:>8}{t['obs_Z']:>7}"
          f"{t['obs_Q']:>7}{t['obs_Z2']:>7}{n_glob:>9}{flag}")


def part_one_key():
    print("=" * 74)
    print("PART 1 — THE ANSWER KEY ON COVERS WITH CHORDS")
    print("=" * 74)
    print(f"  {'model':<16}{'grade':<16}{'sections':>9}{'no ext':>8}"
          f"{'obs Z':>7}{'obs Q':>7}{'obs Z2':>7}{'globals':>9}")
    _key_row("Peres-Mermin", peres_mermin(), ("strong", 24, 24, 24, 24))
    _key_row("GHZ", ghz(), ("strong", 16, 16, 16, 16))
    _key_row("product (3,3,2)", product_332(), ("non-contextual", 0, 0, 0, 0))


# ----------------------------------------------- part 2: random models

def _marginal_ok(sup, contexts, measurements):
    """No-signalling on single-measurement overlaps: each measurement's set
    of possible outcomes is the same in every context containing it."""
    for m in measurements:
        seen = None
        for C in contexts:
            if m in C:
                vals = {t[C.index(m)] for t in sup[C]}
                if seen is None:
                    seen = vals
                elif vals != seen:
                    return False
    return True


def random_model(measurements, contexts, rng, nosig=True):
    """Half the time: restrictions of a few random global assignments plus
    extra sections whose values are already possible (logical
    contextuality at most). Otherwise: random supports with every outcome
    possible everywhere (strong contextuality allowed)."""
    O = {m: (0, 1) for m in measurements}
    sup = {C: set() for C in contexts}
    if rng.random() < 0.5:
        for _ in range(int(rng.integers(1, 4))):
            g = {m: int(rng.integers(2)) for m in measurements}
            for C in contexts:
                sup[C].add(tuple(g[m] for m in C))
        possible = {m: {t[C.index(m)] for C in contexts if m in C
                        for t in sup[C]} for m in measurements}
        for C in contexts:
            for t in itertools.product((0, 1), repeat=len(C)):
                if rng.random() < 0.3 and all(
                        t[i] in possible[m] for i, m in enumerate(C)):
                    sup[C].add(t)
    else:
        while True:
            for C in contexts:
                sup[C] = {t for t in itertools.product((0, 1), repeat=len(C))
                          if rng.random() < 0.55}
                if not sup[C]:
                    sup[C].add(tuple(int(rng.integers(2)) for _ in C))
            if (not nosig) or _marginal_ok(sup, contexts, measurements):
                break
    return Model([(m, O[m]) for m in measurements], contexts, sup)


def part_two_random():
    print("\n" + "=" * 74)
    print(f"PART 2 — {TRIALS} RANDOM MODELS PER COVER, three rings, with"
          " and without the no-signalling filter")
    print("=" * 74)
    covers = {"(3,3,2)": scenario_332(),
              "GHZ cover": (ghz().X, ghz().contexts),
              "PM cover": (peres_mermin().X, peres_mermin().contexts)}
    for name, (ms, ctx) in covers.items():
        for nosig in (True, False):
            rng = np.random.default_rng(SEED + len(ms))
            t = {g: dict.fromkeys(KEYS, 0)
                 for g in ("non-contextual", "logical", "strong")}
            for _ in range(TRIALS):
                model = random_model(list(ms), list(ctx), rng, nosig)
                g, rows, _ = audit3(model)
                d = t[g]
                d["models"] += 1
                tally(rows, d)
                ne = [r for r in rows if not r["extends"]]
                if ne:
                    hit = any(not r["vZ"] for r in ne)
                    d["seen" if hit else "missed"] += 1
            print(f"\n  {name}, {'no-signalling' if nosig else 'signalling'}")
            _header()
            for g, d in t.items():
                _print_tally(g, d)
    print("\n  'Z¬Q': non-extending sections obstructed over Z whose class")
    print("  vanishes over Q; 'Z¬Z2': the same against Z_2. Either being")
    print("  nonzero is ring-dependence, which a cyclic cover cannot show.")


# ------------------------------------------ part 3: the K4 holarchy

MENU2 = 2      # unit vectors at 0° and 180°; declared maps 0 or 180°


def star_states(ks, eps):
    """Three-port holon: centre c and ports p1..p3 with declared maps k_i;
    a mismatch on an internal edge costs 4 (antipodal unit vectors), the
    Rayleigh quotient is energy over 4 vertices, and eps counts allowed
    mismatches."""
    out = []
    for st in itertools.product(range(MENU2), repeat=4):
        c = st[0]
        mism = sum(1 for i, k in enumerate(ks) if (st[i + 1] - c - k) % 2)
        if mism <= eps:
            out.append(st)
    return out


K4_EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def k4_model(holons, rot):
    """holons: list of (ks, eps). rot: rotation per K4 edge. Each holon's
    three ports are used by its three edges in order."""
    states = [star_states(ks, eps) for ks, eps in holons]
    slot = {h: 0 for h in range(4)}
    ports = {}
    for e in K4_EDGES:
        u, v = e
        ports[e] = (slot[u] + 1, slot[v] + 1)
        slot[u] += 1
        slot[v] += 1
    ctx, sup = [], {}
    for e, k in zip(K4_EDGES, rot):
        u, v = e
        pu, pv = ports[e]
        ctx.append(e)
        sup[e] = {(a, b) for a in states[u] for b in states[v]
                  if (a[pu] - b[pv] - k) % 2 == 0}
    return Model([(h, tuple(states[h])) for h in range(4)], ctx, sup)


def k4_holonomy_consistent(holons, rot):
    """With every gate exact, ports are c_h + k_{h,i}; a global section is
    a solution of six mod-2 equations in four centre bits."""
    slot = {h: 0 for h in range(4)}
    eqs = []
    for e, k in zip(K4_EDGES, rot):
        u, v = e
        ku = holons[u][0][slot[u]]
        kv = holons[v][0][slot[v]]
        slot[u] += 1
        slot[v] += 1
        eqs.append((u, v, (k + ku + kv) % 2))    # c_u + c_v = rhs
    for c in itertools.product(range(2), repeat=4):
        if all((c[u] + c[v]) % 2 == r for u, v, r in eqs):
            return True
    return False


def part_three_k4():
    print("\n" + "=" * 74)
    print("PART 3 — FOUR THREE-PORT HOLONS ON K4: a holarchy with chords")
    print("=" * 74)
    rng = np.random.default_rng(SEED + 4)
    print("  every gate exact:")
    print(f"  {'trial':>5}{'consistent':>11}  {'grade':<16}{'sections':>9}"
          f"{'no ext':>8}{'obs Z':>7}{'obs Q':>7}{'obs Z2':>7}")
    bad = 0
    for trial in range(8):
        holons = [([int(rng.integers(2)) for _ in range(3)], 0)
                  for _ in range(4)]
        rot = [int(rng.integers(2)) for _ in K4_EDGES]
        cons = k4_holonomy_consistent(holons, rot)
        g, rows, _ = audit3(k4_model(holons, rot))
        t = dict.fromkeys(KEYS, 0)
        tally(rows, t)
        pred = "non-contextual" if cons else "strong"
        wrong = (g != pred) or (g == "strong" and t["obs_Z"] != len(rows))
        bad += wrong
        print(f"  {trial:>5}{'y' if cons else 'N':>11}  {g:<16}{len(rows):>9}"
              f"{t['no_ext']:>8}{t['obs_Z']:>7}{t['obs_Q']:>7}{t['obs_Z2']:>7}"
              f"{'  <-- against prediction' if wrong else ''}")
    print(f"  rows against prediction: {bad}")
    print(f"\n  gates drawn from eps in (0, 1, 3) per holon, {TRIALS // 4}"
          f" models:")
    t = {g: dict.fromkeys(KEYS, 0)
         for g in ("non-contextual", "logical", "strong")}
    for _ in range(TRIALS // 4):
        holons = [([int(rng.integers(2)) for _ in range(3)],
                   int(rng.choice((0, 1, 3)))) for _ in range(4)]
        rot = [int(rng.integers(2)) for _ in K4_EDGES]
        g, rows, _ = audit3(k4_model(holons, rot))
        d = t[g]
        d["models"] += 1
        tally(rows, d)
        ne = [r for r in rows if not r["extends"]]
        if ne:
            d["seen" if any(not r["vZ"] for r in ne) else "missed"] += 1
    _header()
    for g, d in t.items():
        _print_tally(g, d)


# ------------------------------------------------------------------ main

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    part_one_key()
    part_two_random()
    part_three_k4()
