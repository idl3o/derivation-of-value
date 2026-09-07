"""
The budget across levels: what nesting does to a security budget.

Independent and Expensive §8.3 asked whether a holarchy's pool is the SUM of
its levels' pools or the MINIMUM; The Second Pool §9.3 said each level would
carry its own receipts and Gluing the Gates Prop 6.1 predicts the minimum;
One's Own Anchor §9.3 asked whether a coalition presenting as a holon pays
the holon's boundary or its constituents'. This module answers all three on
the paid-DOF model and then on the program's own specimen, with the residual
reading of evidencing.py — the one reading with a native share.

THE HOLARCHY. The hierarchical complex (complexes.hierarchical_modular,
seed 7, depth 8) is a holarchy by construction: level-j holons are the
aligned blocks of 2^j leaves, and every edge was introduced by exactly one
merge, at the level l where its endpoints first share a block. So the edges
PARTITION by merge level, E = E_1 ⊔ … ⊔ E_8, and the interfaces BETWEEN
level-l holons NEST, I_l = E_{>l}, with I_0 = E the leaf level's. A level-l
mechanism admits level-l holons as identities, each holding a receipt (an
anchor pool A_l, disjoint per level by construction), and reads either its
own merges E_l (does each holon glue internally) or the interfaces I_l
(do the holons glue to each other).

THEOREM (receipts sum, interfaces nest). Anchor pools are disjoint across
levels and sum. Native pools do not: a derivation on an edge serves every
level that reads that edge, and every level reads a subset of the leaf
level's edges. The compositional holarchic mechanism — every level's gate,
conjoined — has native budget k·m·|E|, the finest level's, however many
levels it has. Nesting adds anchor pools, which evidence nothing (One's Own
Anchor Thm 3.4), and adds no native pool. The independence between a level-l
gate and the leaf gate is exactly the level's receipt share,
    iota(Pi_l | Pi_0) = |A_l| / (|A_l| + |I_l|).

PROP 6.1, PRICED. A coalition C that is a level-j block has its whole
boundary at merge levels above j: |∂C ∩ E_l| = 0 for l ≤ j, and averaged
over the level-j blocks exactly 2^{j+2−l} for l > j (each such edge has one
endpoint in each of two blocks), summing to 4(1 − 2^{j−8}). Under the
conjunction of every level's own-merge gate the coalition derives every
boundary edge — the SUM over levels is the every-edge gate of One's Own
Anchor, k·m·|∂C|. Under a mechanism the adversary can satisfy at ONE level
of its choosing (Gluing the Gates' non-compositional case), the coalition
presents at any level l ≤ j and derives nothing: the MIN over levels is
zero. The boundary is the same set of edges at every level of presentation;
what presenting coarse saves is receipts, and receipts are idle.

MF §8.4's CRITERION. "A refinement is Sybil when the adversary controls both
sides of an interface." Both sides controlled = the edge is interior to C =
fiction, free (One's Own Anchor Prop 6.2). It is not checkable from
residuals: the naive fiction glues BETTER than honesty (interior residual
zero against honest's (sigma/sqrt k)·sqrt 2), a two-sided gate catches
that, and the coalition defeats the two-sided gate by adding honest-level
noise to its own interior sections, which costs nothing.

PREDICTIONS, STATED BEFORE RUNNING.
  1. Miniature (brute-force attacker of exclusion.py, sets never seen):
     f(conjunction of interface gates) = sum|A_l| + |I_0| = 13, against the
     naive per-level sum 17; iota(Pi_1|Pi_0) = 0.400, iota(Pi_2|Pi_0) = 0.500;
     conjunction of merge gates = |I_0| = 6; OR over interface gates = 2,
     OR over merge gates = 1. Zero deviation on every row.
  2. Specimen: |E_l| = 128, 117, 64, 32, 16, 8, 4, 2; a level-by-level sum
     of interface work overstates the native budget by sum_l |I_l| / |E| =
     2.30; mean block boundary at level l is 2^{j+2−l} (3.75, 3.5, 3.0 total
     at j = 4, 5, 6 — the numbers One's Own Anchor published).
  3. Sheaf, delta = 3 (above the step), first block at j = 4..7:
     every-edge gate derives 3, 2, 3, 2 edges (per identity 12, 4, 3, 1 —
     published); own-merge gate at l ≤ j derives 0 and passes; AND over
     own-merge gates = every-edge; OR over own-merge gates = 0; between-
     holons gate at the top (l = 7) derives 0, 0, 1, 2; the per-level MEAN
     gate needs derivations only where the boundary is more than
     theta = (tol − r_h)/(r_stale − r_h) ≈ 0.41 of |E_l|: 2 at l = 8 for
     j = 7; 1 at l = 7 and 1 at l = 8 for j = 6; none for j = 4, 5. The
     whole-network mean passes every coalition at zero.
  4. Interior: naive fiction residual < 1e-8 on every interior edge; a
     two-sided gate at half honest's level refuses it; the mimic (interior
     noise at sigma/sqrt k, cost 0) sits inside honest's spread and passes.

WHAT CAME BACK (recorded after running; the predictions above are as
stated before). 1, 2 and 4 held to the decimal, 2 exactly rather than in
expectation — the per-level boundary averaged over blocks is a double-
counting identity, not a sample mean. 3 held on every "all" gate (sum of
own-merge gates = every edge = 3, 2, 3, 2; OR = 0 at every size; top
between-holons gate 0, 0, 1, 2). The per-level mean gates came in at 0.86,
0.86 and 1.43 derivations per epoch against the arithmetic's 1, 1 and 2:
on the marginal epochs the realised stale residual sat just under the
threshold, so the count is the arithmetic's to within one derivation on
about one epoch in seven, and the mean gate prices nothing below |C| = 64.
One first-pass error: the record-based fiction is ZERO on the coalition's
interior prompts (no honest neighbour ever published them), so the first
mimic was pure noise against pure noise, and a Procrustes fit with no
signal over-absorbs — 0.172 against honest's 0.203, outside the spread.
The fiction must have honest scale; with a random fabrication of unit scale
plus honest-level noise the mimic sits at 0.199 inside [0.16, 0.24].

Run:  python holarchy.py     (seeded; every number reproducible; ~1 s)
"""
import sys
import numpy as np
from exclusion import Universe, projection, cheapest_accepted, measure_pair
from evidencing import (D, M, SIGMA, K, TOL, HONEST_SEED, COALITION_SEED,
                        world_path, procrustes_residual, boundary,
                        coalition_sections, estimate_from_record, _setup,
                        _honest)
from exclusion import EPOCHS, DEPTH

DELTA_UNITS = 3.0
MIMIC_SEED = 51
BLOCK_LEVELS = (4, 5, 6, 7)
R_LOW = 0.5 * SIGMA / np.sqrt(K) * np.sqrt(2.0)     # two-sided gate's floor


# ------------------------------------------------------------- structure

def edge_level(u, v):
    """The merge level that introduced (u, v): the smallest l at which the
    endpoints share an aligned block of 2^l leaves."""
    lvl = 0
    while (u >> lvl) != (v >> lvl):
        lvl += 1
    return lvl


def levels_of(edges):
    return np.array([edge_level(u, v) for u, v in edges])


def block(j, which=0):
    return set(range(which * 2 ** j, (which + 1) * 2 ** j))


# ------------------------------------------------------- part 1: the sets

def _nested_universe():
    """Three holon levels. Receipts A_0, A_1, A_2 disjoint; interfaces
    I_0 ⊃ I_1 ⊃ I_2 nested; merges J_l = I_{l-1} \\ I_l partition I_0."""
    u = Universe(13, 2)
    A = {0: frozenset(range(0, 4)), 1: frozenset({4, 5}), 2: frozenset({6})}
    I = {0: frozenset(range(7, 13)), 1: frozenset({7, 8, 9}),
         2: frozenset({7})}
    J = {1: I[0] - I[1], 2: I[1] - I[2], 3: I[2]}
    return u, A, I, J


def _any_of(gates):
    def accepts(produced):
        return any(g(produced) for g in gates)
    return accepts


def part_one_model():
    print("=" * 74)
    print("PART 1 — THE MINIATURE: receipts sum, interfaces nest")
    print("=" * 74)
    u, A, I, J = _nested_universe()
    pi = {l: projection(u, A[l] | I[l]) for l in (0, 1, 2)}
    merge = {l: projection(u, J[l]) for l in (1, 2, 3)}
    rows = [
        ("interface gate, level 0 (leaves)", [pi[0]], len(A[0]) + len(I[0])),
        ("interface gate, level 1", [pi[1]], len(A[1]) + len(I[1])),
        ("interface gate, level 2", [pi[2]], len(A[2]) + len(I[2])),
        ("AND of interface gates", [pi[0], pi[1], pi[2]],
         sum(map(len, A.values())) + len(I[0])),
        ("OR of interface gates (adversary picks)",
         [_any_of(list(pi.values()))],
         min(len(A[l]) + len(I[l]) for l in pi)),
        ("AND of merge gates", list(merge.values()), len(I[0])),
        ("OR of merge gates (adversary picks)",
         [_any_of(list(merge.values()))], min(map(len, J.values()))),
    ]
    naive = sum(len(A[l]) + len(I[l]) for l in pi)
    print(f"  {'gate':<42}{'measured':>10}{'designed':>10}{'dev':>7}")
    worst = 0.0
    for name, fns, designed in rows:
        f = cheapest_accepted(u, fns)
        worst = max(worst, abs(f - designed))
        print(f"  {name:<42}{f:>10.0f}{designed:>10.0f}{f - designed:>7.0f}")
    print(f"  naive per-level sum of interface gates = {naive} against the"
          f" AND's {rows[3][2]}: overcount {naive / rows[3][2]:.2f}x")
    for l in (1, 2):
        _, _, i_l0, i_0l, _ = measure_pair(u, pi[0], pi[l])
        designed = len(A[l]) / (len(A[l]) + len(I[l]))
        worst = max(worst, abs(i_l0 - designed))
        print(f"  iota(Pi_{l} | Pi_0) = {i_l0:.3f}  designed |A_{l}|/(|A_{l}|"
              f"+|I_{l}|) = {designed:.3f};  iota(Pi_0 | Pi_{l}) = {i_0l:.3f}")
    print(f"  worst deviation = {worst:.1e}"
          + ("" if worst == 0 else "  <-- stop reading"))
    print("  The conjunction pays every receipt once and the leaf level's")
    print("  interfaces once; the OR pays the cheapest level. Independence")
    print("  between levels is the receipt share, and receipts are idle.")


# --------------------------------------------------- part 2: the specimen

def part_two_specimen(n, edges, lv):
    print("\n" + "=" * 74)
    print("PART 2 — THE SPECIMEN: edges by merge level, boundaries by level")
    print("=" * 74)
    sizes = [int(np.sum(lv == l)) for l in range(1, DEPTH + 1)]
    nested = [int(np.sum(lv > l)) for l in range(0, DEPTH)]
    print(f"  |E_l|, l = 1..8:   {sizes}   (sum {sum(sizes)} = |E| ="
          f" {len(edges)})")
    print(f"  |I_l|, l = 0..7:   {nested}")
    print(f"  sum_l |I_l| / |E| = {sum(nested) / len(edges):.2f}: a level-by-"
          f"level sum of interface work overstates the native budget by that"
          f" factor")
    print(f"\n  {'j':>3}{'blocks':>7}{'mean |dC|':>10}{'designed':>9}   "
          f"mean |dC ∩ E_l| for l = j+1..8  (designed 2^(j+2-l))")
    for j in BLOCK_LEVELS:
        per_level = np.zeros(DEPTH + 1)
        blocks = n // 2 ** j
        for w in range(blocks):
            C = block(j, w)
            _, bd = boundary(edges, C)
            for i in bd:
                per_level[lv[i]] += 1
        per_level /= blocks
        designed = 4 * (1 - 2 ** (j - DEPTH))
        by_l = "  ".join(f"{per_level[l]:.2f}/{2 ** (j + 2 - l):.2f}"
                         for l in range(j + 1, DEPTH + 1))
        below = per_level[:j + 1].sum()
        print(f"  {j:>3}{blocks:>7}{per_level.sum():>10.2f}{designed:>9.2f}   "
              f"{by_l}   below j: {below:.0f}")
    print("  A block's boundary lies entirely above its own level and halves")
    print("  per level, exactly: every edge at merge level l > j has one")
    print("  endpoint in each of two level-j blocks, so the blocks'")
    print("  boundaries at level l sum to 2|E_l|. The first block at each")
    print("  level has the boundaries One's Own Anchor published: 3, 2, 3, 2.")


# ------------------------------------------------------ part 3: the gates

def _gate_list(lv):
    """(name, family, level, read indices, kind)."""
    E = len(lv)
    gates = [("every edge", "all", 0, np.arange(E), "all")]
    for l in range(1, DEPTH + 1):
        gates.append((f"own merges l={l}", "merge", l, np.flatnonzero(lv == l),
                      "all"))
    for l in range(0, DEPTH):
        gates.append((f"between level-{l} holons", "between", l,
                      np.flatnonzero(lv > l), "all"))
    for l in range(1, DEPTH + 1):
        gates.append((f"mean over merges l={l}", "mean", l,
                      np.flatnonzero(lv == l), "mean"))
    gates.append(("mean over the network", "mean", 0, np.arange(E), "mean"))
    return gates


def derive_edges(edges, cols, C, G, G_hat, k, rng, which):
    """Derive the prompts of the listed edges from the world (k re-derivations
    each), edge-local prompts; returns the patched estimate and the count."""
    G_hat = G_hat.copy()
    for i in which:
        G_hat[:, cols[i]] = G[:, cols[i]] + SIGMA / np.sqrt(k) * \
            rng.normal(size=(D, M))
    return G_hat, len(which)


def _needed(gate, r_stale, r_full, bd_read):
    """How many boundary edges in the gate's read set must be derived: all of
    them for an every-edge gate; for a mean gate, greedily the worst first
    until the mean clears, using the residuals the full derivation gave."""
    _, _, _, read, kind = gate
    if kind == "all":
        return list(bd_read)
    order = sorted(bd_read, key=lambda i: -r_stale[i])
    r = r_stale.copy()
    chosen = []
    while r[read].mean() >= TOL and order:
        i = order.pop(0)
        r[i] = r_full[i]
        chosen.append(i)
    return chosen


def _run_block(n, edges, cols, frames, lv, j, gates, delta_units=DELTA_UNITS):
    """Coalition = first level-j block, commit regime, delta above the step.
    Returns per-gate totals over the scored epochs and the honest residual."""
    m_total = M * len(edges)
    delta = delta_units * SIGMA / np.sqrt(K)
    G = world_path(m_total, delta)
    rng = np.random.default_rng(HONEST_SEED)
    crng = np.random.default_rng(COALITION_SEED)
    C = block(j)
    inside, bd = boundary(edges, C)
    bd_set = set(bd)
    tot = {g[0]: {"derived": 0, "stale_pass": True, "pass": True}
           for g in gates}
    record, honest_r = None, []
    for t in range(EPOCHS):
        A, B = _honest(edges, cols, G[t], frames, K, rng, False, n)
        honest_r.append(procrustes_residual(A, B)[bd].mean())
        if record is None:
            record = (A, B)
            continue
        G_hat, _ = estimate_from_record(edges, cols, C, record[0], record[1],
                                        frames, m_total,
                                        np.sqrt(1 - delta ** 2))
        r_stale = procrustes_residual(*coalition_sections(edges, cols, C, A, B,
                                                          G_hat, frames))
        G_full, _ = derive_edges(edges, cols, C, G[t], G_hat, K, crng, bd)
        r_full = procrustes_residual(*coalition_sections(edges, cols, C, A, B,
                                                         G_full, frames))
        for g in gates:
            name, _, _, read, kind = g
            bd_read = [i for i in read if i in bd_set]
            chosen = _needed(g, r_stale, r_full, bd_read)
            r = r_stale.copy()
            r[chosen] = r_full[chosen]
            ok = (r[read] < TOL).all() if kind == "all" \
                else r[read].mean() < TOL
            ok_stale = (r_stale[read] < TOL).all() if kind == "all" \
                else r_stale[read].mean() < TOL
            tot[name]["derived"] += len(chosen)
            tot[name]["pass"] &= bool(ok)
            tot[name]["stale_pass"] &= bool(ok_stale)
        record = (A, B)
    return tot, float(np.mean(honest_r)), len(bd), len(inside)


def _print_block(j, tot, gates, bd_mask, honest_r):
    scored = EPOCHS - 1
    size = 2 ** j
    print(f"\n  block j = {j} (|C| = {size}, |dC| = {int(bd_mask.sum())},"
          f" honest boundary r = {honest_r:.4f})")
    print(f"  {'gate':<28}{'reads':>6}{'dC∩read':>9}{'derive/ep':>11}"
          f"{'per identity':>14}{'stale':>7}{'pass':>6}")
    for name, fam, l, read, kind in gates:
        d = tot[name]["derived"] / scored
        bd_in = int(bd_mask[read].sum())
        print(f"  {name:<28}{len(read):>6}{bd_in:>9}{d:>11.2f}"
              f"{K * M * d / size:>14.2f}"
              f"{'y' if tot[name]['stale_pass'] else 'N':>7}"
              f"{'y' if tot[name]['pass'] else 'N':>6}")
    merges = [tot[g[0]]["derived"] / scored for g in gates if g[1] == "merge"]
    between = [tot[g[0]]["derived"] / scored for g in gates
               if g[1] == "between"]
    means = [tot[g[0]]["derived"] / scored for g in gates
             if g[1] == "mean" and g[2] > 0]
    every = tot["every edge"]["derived"] / scored
    print(f"  AND over own-merge gates = {sum(merges):.2f}  (every edge"
          f" {every:.2f});  OR over own-merge gates = {min(merges):.2f};"
          f"  OR over between-holon gates = {min(between):.2f};"
          f"  AND over per-level means = {sum(means):.2f}")
    flag = "" if abs(sum(merges) - every) < 1e-9 else "  <-- SUM != EVERY EDGE"
    print(f"  sum over levels = {sum(merges):.2f}, min over levels ="
          f" {min(merges):.2f}{flag}")


def part_three_gates(n, edges, cols, frames, lv):
    print("\n" + "=" * 74)
    print(f"PART 3 — THE GATES, delta = {DELTA_UNITS:.0f} sigma/sqrt k, "
          f"commit regime, edge-local prompts")
    print("=" * 74)
    print(f"  tol = {TOL:.3f}; a mean gate at level l needs derivations only"
          f" where |dC ∩ E_l| / |E_l| exceeds"
          f" (tol − r_h)/(r_stale − r_h)")
    gates = _gate_list(lv)
    for j in BLOCK_LEVELS:
        tot, honest_r, _, _ = _run_block(n, edges, cols, frames, lv, j, gates)
        _, bd = boundary(edges, block(j))
        bd_mask = np.zeros(len(edges), dtype=bool)
        bd_mask[bd] = True
        _print_block(j, tot, gates, bd_mask, honest_r)
    print("\n  The every-edge gate is the sum over levels of the own-merge")
    print("  gates, exactly. A mechanism the adversary satisfies at one level")
    print("  of its choosing is defeated at zero by presenting at or below")
    print("  the coalition's own level. The boundary does not move with the")
    print("  level of presentation; only the receipts do.")


# --------------------------------------------------- part 4: the interior

def part_four_interior(n, edges, cols, frames):
    print("\n" + "=" * 74)
    print("PART 4 — MF §8.4's CRITERION: both sides controlled, from"
          " residuals")
    print("=" * 74)
    j = 6
    C = block(j)
    m_total = M * len(edges)
    delta = DELTA_UNITS * SIGMA / np.sqrt(K)
    G = world_path(m_total, delta)
    rng = np.random.default_rng(HONEST_SEED)
    mrng = np.random.default_rng(MIMIC_SEED)
    inside, bd = boundary(edges, C)
    A0, B0 = _honest(edges, cols, G[0], frames, K, rng, False, n)
    A, B = _honest(edges, cols, G[1], frames, K, rng, False, n)
    G_hat, cnt = estimate_from_record(edges, cols, C, A0, B0, frames, m_total,
                                      np.sqrt(1 - delta ** 2))
    G_fic = np.where(cnt > 0, G_hat, mrng.normal(size=G_hat.shape))
    Ac, Bc = coalition_sections(edges, cols, C, A, B, G_fic, frames)
    r_h = procrustes_residual(A, B)
    r_naive = procrustes_residual(Ac, Bc)
    noise = SIGMA / np.sqrt(K)
    Am, Bm = Ac.copy(), Bc.copy()
    Am[inside] += noise * mrng.normal(size=(len(inside), D, M))
    Bm[inside] += noise * mrng.normal(size=(len(inside), D, M))
    r_mimic = procrustes_residual(Am, Bm)
    print(f"  |C| = {2 ** j}, interior edges {len(inside)}, two-sided gate:"
          f" {R_LOW:.3f} < r < {TOL:.3f}")
    print(f"  {'sections on the interior':<34}{'mean r':>9}{'min r':>9}"
          f"{'max r':>9}{'two-sided':>11}{'cost':>6}")
    for name, r in (("honest", r_h), ("naive fiction", r_naive),
                    ("fiction + honest-level noise", r_mimic)):
        ri = r[inside]
        ok = bool(((ri > R_LOW) & (ri < TOL)).all())
        print(f"  {name:<34}{ri.mean():>9.4f}{ri.min():>9.1e}{ri.max():>9.4f}"
              f"{'passes' if ok else 'refused':>11}{0:>6}")
    print(f"  honest interior residual designed (sigma/sqrt k) sqrt 2"
          f" sqrt(1 − 1/m) = {noise * np.sqrt(2) * np.sqrt(1 - 1 / M):.4f}")
    print("  The fiction glues better than honesty; the two-sided gate sees")
    print("  that; and the coalition buys honest-level disagreement with its")
    print("  own noise for nothing. Both sides controlled is not a residual.")


# ------------------------------------------------------------------ main

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    part_one_model()
    n, edges, cols, _, frames = _setup(shared=False)
    lv = levels_of(edges)
    part_two_specimen(n, edges, lv)
    part_three_gates(n, edges, cols, frames, lv)
    part_four_interior(n, edges, cols, frames)
