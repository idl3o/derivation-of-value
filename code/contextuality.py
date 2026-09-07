"""
Conjecture 3.1 of No Global Section, computed: the cohomological obstruction
of Abramsky, Mansfield and Barbosa on gate scenarios with non-affine gates.

THE CONJECTURE. No Global Section §3 conjectured that the presheaf-of-
distributions construction of Abramsky, Mansfield and Barbosa (AMB, 2011)
applies
to GATE SCENARIOS — holons as measurements, interfaces as contexts, gate-
admissible states as outcomes — and yields a Čech obstruction to a globally
admissible assignment with no affine hypothesis on the gates. §8.1 asked for
the computation on a small scenario with genuinely non-affine gates. §8.2
worried that the designer would have to CHOOSE the distributions. The plan's
risk note was sharper: the contextuality setting is probabilistic and gates
are deterministic thresholds.

THE CONSTRUCTION, as computed here. AMB's obstruction uses only the SUPPORT
of an empirical model: S(C) = the local sections possible at context C. The
abelian presheaf is the free Z-module F(C) = Z[S(C)], restriction extended
linearly, and for a local section s at context C_0 the class gamma(s) in
the relative Čech H^1 vanishes iff s extends to a COMPATIBLE FAMILY of
formal Z-combinations r_i in F(C_i), r_0 = s, agreeing on every pairwise
overlap. That is an integer linear system: unknown integer coefficients on
the local sections of every other context; for each pair of contexts and
each assignment u on their overlap, the coefficients of sections restricting
to u must sum equally on both sides, with C_0's side fixed to the indicator
of s. Solved exactly here over Z (Smith normal form) and over Q (rational
elimination), no floating point, one matrix per context with every section
of that context as a right-hand side. A gate scenario supplies S(C)
directly — the admissible joint states at an interface — and no
distribution is chosen anywhere. The probabilistic grade of NGS §4 needs
frequencies a gate model does not have; the logical and strong grades need
only the support, and so does the obstruction.

THE ANSWER KEY (Part 1), from the literature, before anything of the
program's is measured. Bell/CHSH: possibilistically non-contextual — every
local section extends to a global one — so no section may be obstructed (a
false positive here means stop reading). Hardy: logically contextual — the
section (a1,b1) = (0,0) extends to no global assignment — and AMB record the
obstruction VANISHING for it: the standard false negative. PR box: strongly
contextual, every local section obstructed. Gluing the Gates Prop 4.2's
affine cycle (x_u = 2 x_v around a triangle, finite menu): strong, and by
hand every section is obstructed.

THE GATE SCENARIOS (Parts 2–3). Stalks R^2, a menu of four unit vectors
closed under rotation by 90°, so declared maps are rotations R_k and act on
the menu by index shift. A holon is one internal edge with a declared
rotation, its two vertices its two ports, and a state is a menu vector per
vertex. Its gate is the RAYLEIGH-QUOTIENT gate: the section's Dirichlet
energy x^T L x / x^T x under the declared internal connection at or below
eps — a threshold on a spectral quantity, not affine, the sublevel set of a
quadratic form on a product of circles. A 90° mismatch costs 1 per vertex
and a 180° mismatch 2, so eps = 0 admits the 4 exactly-transported states,
eps = 1 admits 12, and eps = 2 admits all 16 (gate open). An interface
(u, p_u, v, p_v, k) requires x_u[p_u] = R_k x_v[p_v]. Holons sit on a
triangle or a square. Everything is enumerable, so the truth — which local
sections extend, whether any global section exists — is brute-forced and
the obstruction compared against it.

PREDICTIONS, STATED BEFORE RUNNING.
  1. Answer key reproduced: Bell 0 of 14 sections obstructed and all
     extend; Hardy 1 of 13 non-extending, 0 obstructed; PR 8 of 8
     obstructed, none extend; affine cycle 9 of 9 obstructed, none extend.
     No false positive anywhere, ever (gamma(s) ≠ 0 implies s does not
     extend, a theorem).
  2. eps = 0 at every holon makes each interface's support the graph of a
     bijection between port states, so the triangle is strong iff the
     rotation composed around it is not the identity, and in that case
     EVERY section is obstructed over Z: the compatible-family condition
     forces the coefficients to be constant on orbits of a fixed-point-free
     permutation, and an indicator is not. Detected, over Z and over Q.
  3. Looser gates (eps > 0) make the supports non-bijective, and logically
     contextual models appear. The false negative transfers: some non-
     extending sections have vanishing obstruction. The detection rate in
     the logical grade is below one; in the strong grade it is high but
     need not be one (AMB's cohomology witnesses all AvN arguments, and
     strong contextuality without an AvN argument exists).
  4. Z and Q agree on most sections and not all; where they differ the
     Z obstruction is the stronger (a rational family with no integer one).
  5. Nothing here needed a distribution. NGS §8.2's worry is confined to
     the probabilistic grade, which gate models do not have.

A NOTE ON WORDS. Abramsky, Mansfield and Barbosa call a vanishing class on
a section that does not extend a "false positive" — the obstruction falsely
certifies extendability. Read as a detector of contextuality, the same
event is a false negative: the detector did not fire. This module and the
paper say MISS, and gloss it once.

WHAT CAME BACK (recorded after running; the predictions above are as
stated before). 1 and 2 held exactly: the answer key to the section, zero
false positives in 30,000-odd sections, the bijective triangle strong iff
the composite rotation is not the identity and then obstructed at every
section. 3 held: of 233 logically contextual gate models across the two
sweeps, 136 were seen by at least one section and 97 missed entirely; the
section-level rate was 0.714 on triangles and 0.604 on squares. Every
strongly contextual model was seen, but not at every section (0.878 and
0.750), so the program's strong gate models are cohomologically logically
contextual and not all cohomologically strongly contextual — Carù's
observation, on the program's specimen. 4 MISSED: Z and Q agreed on every
one of the sections; the literature explains why (Z is initial among
rings, so Z-vanishing implies Q-vanishing, and the converse held here
throughout). 5 held. Part 4, unpredicted, and the first reading of it was
wrong: on triangles every logical model with no exact gate was missed and
every one with an exact gate was seen, which read as "one bijection
suffices"; on squares one exact gate left every model missed, two saw 30
of 38, three saw all. What the two cycles share is the length of the
longest run of OPEN gates: two in a row is seen, three in a row is
missed. The obstruction needs the formal family to be forced through a
bijection often enough that the Z-shaped cancellations of the Hardy
family have no room.

SECOND PASS, PREDICTIONS STATED BEFORE RUNNING PART 5. On a cyclic cover
the Čech system is flow conservation on the bundle diagram (nodes =
(measurement, outcome), edges = local sections in layers), with the fixed
context a unit source and sink. So:
  6. gamma(s) = 0 iff head(s) and tail(s) are joined by an UNDIRECTED path
     avoiding s's layer — on every section, and over any ring, which is
     why Z and Q never differed; and s extends iff joined by a DIRECTED
     path (the gate models orient every layer h -> h+1).
  7. A walk from head to tail passes through the n − 2 holons not incident
     to the layer, in order: the CHAIN. Undirected and directed reach
     through a relation coincide iff the relation is a disjoint union of
     complete bipartite blocks; a bijection (eps = 0) and the complete
     relation (eps = 2) are, the eps = 1 relation is connected and not.
     So a layer whose chain has no eps = 1 holon has no miss, and a layer
     whose chain has one has every section vanishing.
  8. Hence a logical model is seen iff some layer has an eps-1-free chain
     with a non-extending section. On the triangle that is "some exact
     holon"; on the square, "two adjacent exact holons". The run-of-open-
     gates reading of Part 4 was the shadow of this on two cycles.

WHAT CAME BACK, SECOND PASS. 6, 7 and 8 held on every count: undirected
reachability equalled the vanishing of the obstruction on all 31,056
sections and directed reachability equalled extension on all of them; the
540 layers whose chain has no eps = 1 holon carried no miss, the 510
layers whose chain has one carried no obstruction, and the model-level
rule agreed on all 233 logically contextual models. The theorem is a
two-line flow argument, and it makes the obstruction on a cyclic cover
independent of the coefficient ring.

Run:  python contextuality.py     (exact arithmetic; seeded; ~1 min)
"""
import sys
import itertools
from fractions import Fraction
import numpy as np

SEED = 30_000
MENU = 4                      # unit vectors at 0°, 90°, 180°, 270°
EPS_GRID = (0.0, 1.0, 2.0)    # energy per vertex: exact / one 90° / open
N_INT = 2                     # one internal edge 0 - 1, ports 0 and 1
TRIALS = 150


# ----------------------------------------------------------------- models

class Model:
    """A possibilistic empirical model: measurements, outcomes per
    measurement, contexts (tuples of measurements), and the support at each
    context as a frozenset of outcome tuples aligned with the context."""

    def __init__(self, outcomes, contexts, support):
        self.X = tuple(m for m, _ in outcomes)
        self.O = dict(outcomes)
        self.contexts = [tuple(c) for c in contexts]
        self.S = {tuple(c): frozenset(support[tuple(c)]) for c in contexts}

    def sections(self):
        return [(C, s) for C in self.contexts for s in sorted(self.S[C])]


def restrict(t, C, U):
    return tuple(t[C.index(m)] for m in U)


def global_sections(model):
    out = []
    for g in itertools.product(*(model.O[m] for m in model.X)):
        if all(restrict(g, model.X, C) in model.S[C] for C in model.contexts):
            out.append(g)
    return out


def extends(model, C, s, globals_):
    return any(restrict(g, model.X, C) == s for g in globals_)


def grade(model, globals_):
    if not globals_:
        return "strong"
    if any(not extends(model, C, s, globals_) for C, s in model.sections()):
        return "logical"
    return "non-contextual"


# ------------------------------------------------------ exact linear algebra

def rational_batch(A, Bs):
    """A x = b over Q for each b in Bs: exact elimination, rank test."""
    n = len(A[0]) if A else 0
    M = [[Fraction(v) for v in row] + [Fraction(b[i]) for b in Bs]
         for i, row in enumerate(A)]
    rows, r = len(M), 0
    for c in range(n):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = 1 / M[r][c]
        M[r] = [v * inv for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [vi - f * vr for vi, vr in zip(M[i], M[r])]
        r += 1
    return [all(M[i][n + j] == 0 for i in range(r, rows))
            for j in range(len(Bs))]


def _pivot(M, k, rows, cols):
    best = None
    for i in range(k, rows):
        for j in range(k, cols):
            if M[i][j] != 0 and (best is None or abs(M[i][j]) < best[0]):
                best = (abs(M[i][j]), i, j)
    return best


def _swap_to(M, Y, k, i, j):
    M[k], M[i] = M[i], M[k]
    Y[k], Y[i] = Y[i], Y[k]
    for row in M:
        row[k], row[j] = row[j], row[k]


def _snf_step(M, Y, k, rows, cols):
    """Reduce row k and column k against the pivot at (k, k); row
    operations are mirrored on the right-hand sides Y. True when clean."""
    clean = True
    for i in range(k + 1, rows):
        q = M[i][k] // M[k][k]
        if q:
            M[i] = [a - q * b for a, b in zip(M[i], M[k])]
            Y[i] = [a - q * b for a, b in zip(Y[i], Y[k])]
        if M[i][k] != 0:
            clean = False
    for j in range(k + 1, cols):
        q = M[k][j] // M[k][k]
        if q:
            for i in range(rows):
                M[i][j] -= q * M[i][k]
        if M[k][j] != 0:
            clean = False
    return clean


def integer_batch(A, Bs):
    """A x = b over Z for each b in Bs: Smith normal form with the row
    operations applied to every right-hand side; column operations only
    reparametrise x. Solvable iff each diagonal entry divides its
    right-hand side and every zero row has zero right-hand side."""
    rows = len(A)
    cols = len(A[0]) if A else 0
    M = [list(map(int, row)) for row in A]
    Y = [[int(b[i]) for b in Bs] for i in range(rows)]
    k = 0
    while k < min(rows, cols):
        p = _pivot(M, k, rows, cols)
        if p is None:
            break
        _swap_to(M, Y, k, p[1], p[2])
        while not _snf_step(M, Y, k, rows, cols):
            p = _pivot(M, k, rows, cols)
            _swap_to(M, Y, k, p[1], p[2])
        k += 1
    out = []
    for j in range(len(Bs)):
        ok = True
        for i in range(rows):
            d = M[i][i] if i < cols else 0
            if (d == 0 and Y[i][j] != 0) or (d != 0 and Y[i][j] % d != 0):
                ok = False
                break
        out.append(ok)
    return out


# ------------------------------------------------------- the obstruction

def cech_system(model, C0):
    """Overlap-agreement equations with context C0's coefficients
    substituted out. Columns: (context ≠ C0, local section). Returns A and
    a function giving the right-hand side for a section s of C0."""
    cols = [(C, t) for C in model.contexts if C != C0
            for t in sorted(model.S[C])]
    idx = {ct: i for i, ct in enumerate(cols)}
    A, spec = [], []
    for i, Ci in enumerate(model.contexts):
        for Cj in model.contexts[i + 1:]:
            U = tuple(m for m in Ci if m in Cj)
            if not U:
                continue
            values = {restrict(t, Ci, U) for t in model.S[Ci]} | \
                     {restrict(t, Cj, U) for t in model.S[Cj]}
            for u in sorted(values):
                row = [0] * len(cols)
                for C, sign in ((Ci, 1), (Cj, -1)):
                    if C == C0:
                        continue
                    for t in model.S[C]:
                        if restrict(t, C, U) == u:
                            row[idx[(C, t)]] += sign
                c0 = 1 if Ci == C0 else (-1 if Cj == C0 else 0)
                A.append(row)
                spec.append((U, u, c0))

    def rhs(s):
        return [-c0 * (1 if c0 and restrict(s, C0, U) == u else 0)
                for (U, u, c0) in spec]
    return A, rhs


def obstructions(model, C0):
    """For every section s of C0: (vanishes over Z, vanishes over Q)."""
    secs = sorted(model.S[C0])
    A, rhs = cech_system(model, C0)
    Bs = [rhs(s) for s in secs]
    if not A or not A[0]:
        ok = [all(v == 0 for v in b) for b in Bs]
        return dict(zip(secs, zip(ok, ok)))
    return dict(zip(secs, zip(integer_batch(A, Bs), rational_batch(A, Bs))))


def audit(model):
    """Every local section: does it extend, does its obstruction vanish
    over Z and over Q. Returns the grade, the rows, and the global count."""
    globals_ = global_sections(model)
    rows = []
    for C in model.contexts:
        for s, (z, q) in obstructions(model, C).items():
            rows.append({"C": C, "s": s, "vanish_Z": z, "vanish_Q": q,
                         "extends": extends(model, C, s, globals_)})
    return grade(model, globals_), rows, len(globals_)


# ------------------------------------------------------ part 1: answer key

def _bipartite(supports):
    X = ("a1", "a2", "b1", "b2")
    ctx = [("a1", "b1"), ("a1", "b2"), ("a2", "b1"), ("a2", "b2")]
    return Model([(m, (0, 1)) for m in X], ctx, {c: supports[c] for c in ctx})


def bell_model():
    full = {(0, 0), (0, 1), (1, 0), (1, 1)}
    return _bipartite({("a1", "b1"): {(0, 0), (1, 1)}, ("a1", "b2"): full,
                       ("a2", "b1"): full, ("a2", "b2"): full})


def hardy_model():
    full = {(0, 0), (0, 1), (1, 0), (1, 1)}
    return _bipartite({("a1", "b1"): full, ("a1", "b2"): full - {(0, 0)},
                       ("a2", "b1"): full - {(0, 0)},
                       ("a2", "b2"): full - {(1, 1)}})


def pr_model():
    even = {(0, 0), (1, 1)}
    odd = {(0, 1), (1, 0)}
    return _bipartite({("a1", "b1"): even, ("a1", "b2"): even,
                       ("a2", "b1"): even, ("a2", "b2"): odd})


def affine_cycle_model():
    """Gluing the Gates Prop 4.2 on a finite menu: x_u = 2 x_v around a
    triangle, menu {1, 2, 4, 8}. Each holon locally admits any nonzero
    value; the cycle composes to x = 8x."""
    menu = (1, 2, 4, 8)
    X = ("h1", "h2", "h3")
    ctx = [("h1", "h2"), ("h2", "h3"), ("h3", "h1")]
    sup = {c: {(2 * y, y) for y in menu if 2 * y in menu} for c in ctx}
    return Model([(m, menu) for m in X], ctx, sup)


def _print_audit(name, model, expect):
    g, rows, n_glob = audit(model)
    n_ne = sum(not r["extends"] for r in rows)
    obs_z = sum(not r["vanish_Z"] for r in rows)
    obs_q = sum(not r["vanish_Q"] for r in rows)
    fp = sum(r["extends"] and not r["vanish_Z"] for r in rows)
    flag = "" if (g, n_ne, obs_z) == expect else "  <-- stop reading"
    if fp:
        flag += "  <-- FALSE POSITIVE"
    print(f"  {name:<14}{g:<16}{len(rows):>9}{n_ne:>9}{obs_z:>8}{obs_q:>8}"
          f"{n_glob:>9}{flag}")
    return fp


def part_one_answer_key():
    print("=" * 74)
    print("PART 1 — THE ANSWER KEY: models whose grade the literature"
          " settled")
    print("=" * 74)
    print(f"  {'model':<14}{'grade':<16}{'sections':>9}{'no ext.':>9}"
          f"{'obs. Z':>8}{'obs. Q':>8}{'globals':>9}")
    fps = 0
    fps += _print_audit("Bell/CHSH", bell_model(), ("non-contextual", 0, 0))
    fps += _print_audit("Hardy", hardy_model(), ("logical", 1, 0))
    fps += _print_audit("PR box", pr_model(), ("strong", 8, 8))
    fps += _print_audit("affine cycle", affine_cycle_model(), ("strong", 9, 9))
    print("  Bell extends everywhere and nothing is obstructed; Hardy's one")
    print("  non-extending section is the literature's false negative; the PR")
    print("  box and the affine cycle are obstructed at every section.")
    print(f"  false positives: {fps}")


# ------------------------------------------------- gate scenario builder

def _energy(state, internal):
    """Dirichlet energy of a menu section under declared rotations R_k on
    the internal edges: |x_u − R_k x_v|² is 0, 2 or 4 by the index gap."""
    e = 0.0
    for (u, v, k) in internal:
        gap = (state[u] - state[v] - k) % MENU
        e += (0.0, 2.0, 4.0, 2.0)[gap]
    return e


def admissible_states(internal, eps, n_int=N_INT):
    return [st for st in itertools.product(range(MENU), repeat=n_int)
            if _energy(st, internal) / n_int <= eps + 1e-12]


def gate_model(holons, interfaces):
    """holons: list of (internal edges, eps). interfaces: list of
    (u, p_u, v, p_v, k) requiring x_u[p_u] = R_k x_v[p_v]. Outcomes at a
    holon are its admissible states; the support at an interface is the
    admissible pairs that agree there."""
    states = [admissible_states(internal, eps) for internal, eps in holons]
    X = tuple(range(len(holons)))
    outcomes = [(h, tuple(states[h])) for h in X]
    ctx, sup = [], {}
    for (u, pu, v, pv, k) in interfaces:
        C = (u, v)
        ctx.append(C)
        sup[C] = {(a, b) for a in states[u] for b in states[v]
                  if a[pu] == (b[pv] + k) % MENU}
    return Model(outcomes, ctx, sup)


def cycle_scenario(rng, n_holons, eps_choices, bijective=False):
    """Holons on an n-cycle; one internal edge 0-1 with a random rotation;
    interfaces from port 1 of h to port 0 of h+1."""
    holons = []
    for _ in range(n_holons):
        internal = [(0, 1, int(rng.integers(MENU)))]
        eps = 0.0 if bijective else float(rng.choice(eps_choices))
        holons.append((internal, eps))
    interfaces = [(h, 1, (h + 1) % n_holons, 0, int(rng.integers(MENU)))
                  for h in range(n_holons)]
    return holons, interfaces


def composite_rotation(holons, interfaces):
    """Total rotation transported once around the cycle, mod 4."""
    total = 0
    for (internal, _), (_, _, _, _, k) in zip(holons, interfaces):
        total += sum(kk for _, _, kk in internal) + k
    return total % MENU


# ------------------------------------------------- part 2: the triangle

def part_two_triangle():
    print("\n" + "=" * 74)
    print("PART 2 — THE TRIANGLE WITH eps = 0: bijective interfaces")
    print("=" * 74)
    print(f"  {'trial':>5}{'composite':>10}  {'grade':<16}{'sections':>9}"
          f"{'no ext.':>9}{'obs. Z':>8}{'obs. Q':>8}")
    rng = np.random.default_rng(SEED)
    flags = 0
    for trial in range(8):
        holons, ifs = cycle_scenario(rng, 3, EPS_GRID, bijective=True)
        comp = composite_rotation(holons, ifs)
        g, rows, _ = audit(gate_model(holons, ifs))
        n_ne = sum(not r["extends"] for r in rows)
        oz = sum(not r["vanish_Z"] for r in rows)
        oq = sum(not r["vanish_Q"] for r in rows)
        predicted = "strong" if comp else "non-contextual"
        bad = (g != predicted) or (g == "strong" and oz != len(rows)) \
            or (g == "non-contextual" and oz != 0)
        flags += bad
        print(f"  {trial:>5}{comp:>10}  {g:<16}{len(rows):>9}{n_ne:>9}"
              f"{oz:>8}{oq:>8}{'  <-- against prediction' if bad else ''}")
    print("  With every gate at eps = 0 each interface is a bijection of port")
    print("  states, the model is strong exactly when the rotation composed")
    print("  around the triangle is not the identity, and then every section")
    print("  is obstructed: the family must be constant on the orbits of a")
    print("  fixed-point-free permutation and an indicator is not.")
    print(f"  rows against prediction: {flags}")


# ------------------------------------------------------ part 3: the sweep

def _tally(t, g, rows):
    t[g]["models"] += 1
    ne = [r for r in rows if not r["extends"]]
    t[g]["sections"] += len(rows)
    t[g]["no_ext"] += len(ne)
    t[g]["obs_Z"] += sum(not r["vanish_Z"] for r in ne)
    t[g]["obs_Q"] += sum(not r["vanish_Q"] for r in ne)
    t[g]["fp"] += sum(not r["vanish_Z"] for r in rows if r["extends"])
    t[g]["disagree"] += sum(r["vanish_Z"] != r["vanish_Q"] for r in rows)
    t[g]["seen"] += bool(ne) and any(not r["vanish_Z"] for r in ne)
    t[g]["missed"] += bool(ne) and not any(not r["vanish_Z"] for r in ne)


def part_three_sweep():
    print("\n" + "=" * 74)
    print(f"PART 3 — THE SWEEP: {TRIALS} triangles and {TRIALS} squares, eps"
          f" drawn from {EPS_GRID} per holon")
    print("=" * 74)
    keys = ("models", "sections", "no_ext", "obs_Z", "obs_Q", "fp",
            "disagree", "seen", "missed")
    for n_holons in (3, 4):
        rng = np.random.default_rng(SEED + n_holons)
        t = {g: dict.fromkeys(keys, 0)
             for g in ("non-contextual", "logical", "strong")}
        for _ in range(TRIALS):
            holons, ifs = cycle_scenario(rng, n_holons, EPS_GRID)
            g, rows, _ = audit(gate_model(holons, ifs))
            _tally(t, g, rows)
        print(f"\n  {n_holons}-cycle of holons")
        print(f"  {'grade':<16}{'models':>7}{'sections':>9}{'no ext.':>9}"
              f"{'obs. Z':>8}{'obs. Q':>8}{'rate Z':>8}{'Z≠Q':>6}"
              f"{'models seen':>12}{'missed':>8}{'FP':>4}")
        for g, d in t.items():
            rate = d["obs_Z"] / d["no_ext"] if d["no_ext"] else float("nan")
            print(f"  {g:<16}{d['models']:>7}{d['sections']:>9}"
                  f"{d['no_ext']:>9}{d['obs_Z']:>8}{d['obs_Q']:>8}"
                  f"{rate:>8.3f}{d['disagree']:>6}{d['seen']:>12}"
                  f"{d['missed']:>8}{d['fp']:>4}"
                  + ("  <-- FALSE POSITIVE" if d["fp"] else ""))
    print("\n  'rate Z' is the fraction of non-extending sections the Z")
    print("  obstruction sees; 'models seen' counts contextual models with at")
    print("  least one obstructed section, 'missed' those with none. A false")
    print("  positive anywhere means the solver is wrong, not the theorem.")


# ------------------------------------------- part 4: what the misses share

def _misses_by_exact_gates(n_holons):
    """The same models as Part 3 (same seed): logical-grade models binned
    by how many holons have eps = 0."""
    rng = np.random.default_rng(SEED + n_holons)
    by = {k: {"seen": 0, "missed": 0, "rate_n": 0, "rate_d": 0}
          for k in range(n_holons + 1)}
    for _ in range(TRIALS):
        holons, ifs = cycle_scenario(rng, n_holons, EPS_GRID)
        g, rows, _ = audit(gate_model(holons, ifs))
        if g != "logical":
            continue
        k = sum(1 for _, eps in holons if eps == 0.0)
        ne = [r for r in rows if not r["extends"]]
        hit = sum(not r["vanish_Z"] for r in ne)
        by[k]["seen" if hit else "missed"] += 1
        by[k]["rate_n"] += hit
        by[k]["rate_d"] += len(ne)
    return by


def part_four_misses():
    print("\n" + "=" * 74)
    print("PART 4 — THE LOGICAL GRADE BY HOW MANY GATES ARE EXACT")
    print("=" * 74)
    for n_holons in (3, 4):
        by = _misses_by_exact_gates(n_holons)
        print(f"\n  {n_holons}-cycle of holons")
        print(f"  {'exact gates':>12}{'models':>8}{'seen':>6}{'missed':>8}"
              f"{'section rate':>14}")
        for k, d in by.items():
            n = d["seen"] + d["missed"]
            rate = d["rate_n"] / d["rate_d"] if d["rate_d"] else float("nan")
            print(f"  {k:>12}{n:>8}{d['seen']:>6}{d['missed']:>8}"
                  f"{rate:>14.3f}")
    print("  Binned by exact gates the pattern reads as a run length; Part 5")
    print("  says what it is: a layer is miss-free iff the chain of holons")
    print("  not incident to it contains no eps = 1 holon.")


# --------------------------------------- part 5: the theorem on cycles

def section_graph(model):
    """Cyclic covers only. Nodes (measurement, outcome); each local section
    of a context is an edge from the context's first measurement's node to
    its second's, kept in layers by context. This is the bundle diagram."""
    layers = {}
    for C in model.contexts:
        assert len(C) == 2
        layers[C] = [((C[0], t[0]), (C[1], t[1])) for t in sorted(model.S[C])]
    return layers


def reachable(layers, skip, start, directed):
    """Nodes reachable from start without using the layer `skip`, along
    edges in their direction (directed) or either way (undirected)."""
    adj = {}
    for C, es in layers.items():
        if C == skip:
            continue
        for a, b in es:
            adj.setdefault(a, []).append(b)
            if not directed:
                adj.setdefault(b, []).append(a)
    seen, stack = {start}, [start]
    while stack:
        x = stack.pop()
        for y in adj.get(x, ()):
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return seen


def chain_of(layer, n_holons):
    """The holons NOT incident to a layer (u, u+1): the chain a walk from
    the section's head to its tail must pass through, in cyclic order."""
    u = layer[0]
    return [(u + 2 + i) % n_holons for i in range(n_holons - 2)]


def _layer_audit(model, holons, rows):
    """Per layer: does undirected reachability equal the obstruction, does
    directed reachability equal extension, is the chain free of eps = 1
    holons, and how many sections do not extend / are obstructed / vanish."""
    layers = section_graph(model)
    n = len(holons)
    out = []
    for C in model.contexts:
        chain_eps = [holons[h][1] for h in chain_of(C, n)]
        d = {"C": C, "z_free": all(e != 1.0 for e in chain_eps),
             "sections": 0, "no_ext": 0, "obs": 0, "und_ok": 0, "dir_ok": 0}
        for r in rows:
            if r["C"] != C:
                continue
            head, tail = (C[1], r["s"][1]), (C[0], r["s"][0])
            und = tail in reachable(layers, C, head, directed=False)
            dr = tail in reachable(layers, C, head, directed=True)
            d["sections"] += 1
            d["no_ext"] += not r["extends"]
            d["obs"] += not r["vanish_Z"]
            d["und_ok"] += (und == r["vanish_Z"])
            d["dir_ok"] += (dr == r["extends"])
        out.append(d)
    return out


def part_five_theorem():
    print("\n" + "=" * 74)
    print("PART 5 — THE THEOREM ON CYCLES: reachability, and the chain")
    print("=" * 74)
    for n_holons in (3, 4):
        rng = np.random.default_rng(SEED + n_holons)
        tot = {"sections": 0, "und_ok": 0, "dir_ok": 0,
               "free_layers": 0, "free_miss": 0, "z_layers": 0, "z_obs": 0,
               "logical": 0, "rule_ok": 0}
        for _ in range(TRIALS):
            holons, ifs = cycle_scenario(rng, n_holons, EPS_GRID)
            model = gate_model(holons, ifs)
            g, rows, _ = audit(model)
            seen = any(not r["vanish_Z"] for r in rows if not r["extends"])
            predicted_seen = False
            for d in _layer_audit(model, holons, rows):
                tot["sections"] += d["sections"]
                tot["und_ok"] += d["und_ok"]
                tot["dir_ok"] += d["dir_ok"]
                if d["z_free"]:
                    tot["free_layers"] += 1
                    tot["free_miss"] += d["no_ext"] - d["obs"]
                    predicted_seen |= d["no_ext"] > 0
                else:
                    tot["z_layers"] += 1
                    tot["z_obs"] += d["obs"]
            if g == "logical":
                tot["logical"] += 1
                tot["rule_ok"] += (seen == predicted_seen)
        print(f"\n  {n_holons}-cycle: {tot['sections']} sections;"
              f" undirected reach == obstruction vanishes on"
              f" {tot['und_ok']}; directed reach == extends on"
              f" {tot['dir_ok']}")
        print(f"  layers whose chain has no eps = 1 holon:"
              f" {tot['free_layers']} — non-extending sections not"
              f" obstructed there: {tot['free_miss']}")
        print(f"  layers whose chain has an eps = 1 holon: {tot['z_layers']}"
              f" — sections obstructed there: {tot['z_obs']}")
        print(f"  logical models: {tot['logical']}; seen iff some eps-1-free"
              f" chain has a non-extending section: {tot['rule_ok']} agree")
    print("  On a cyclic cover the obstruction is undirected reachability in")
    print("  the bundle diagram with the section's layer removed, extension")
    print("  is directed reachability, and the two differ only through a")
    print("  relation in the chain that is connected without being a union")
    print("  of complete bipartite blocks: here, exactly the eps = 1 holon.")


# ------------------------------------------------------------------ main

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    part_one_answer_key()
    part_two_triangle()
    part_three_sweep()
    part_four_misses()
    part_five_theorem()
