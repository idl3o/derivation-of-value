"""
H1 on the cohomological functional — does duplication add section space?

The H1 result (PoC §4.2.1, Sybil paper v0.2) was measured on §4.2's RANK toy,
where duplicates are exactly redundant because rank is a matroid rank function.
The real mechanism scores H^0 — global sections of the sheaf, the kernel of the
sheaf Laplacian — and a duplicated stalk with consistent restriction maps might
ADD section space rather than being absorbed.

It matters in three places at once:
  * Sybil T1 needs duplication-boundedness. If H^0 grows with N, it fails.
  * Volume V's biconditional needs "no trace without the work". A duplicate that
    adds score without adding work is a trace laid for free.
  * Sign and Work's trace gap tau would be below 1 for such a projection.

Three duplication modes, because "duplicate" is ambiguous and the answer differs:

  integrated  the copy attaches to the SAME neighbours as the original
  bridged     the copies form their own cluster, joined to the honest network
              by a single edge (the structure-aware coalition of independence.py)
  isolated    the copies chain into ONE component of their own
  scattered   each copy is its OWN component — the degenerate case, and the
              one that decides whether H1 survives at all

And two readings of the score, because every real implementation uses the second:

  EXACT       dim ker to machine precision
  APPROXIMATE #{lambda < eps} — what any deployed mechanism actually computes

Run:  python h1_cohomological.py
"""
import numpy as np

from complexes import random_orthogonal

D = 3            # stalk dimension
EPS = (1e-9, 1e-3, 1e-2, 5e-2)


def sheaf_laplacian(n, edges, frames, d=D):
    """Coherent sheaf: O_uv = R_u^T R_v, so global sections exist."""
    L = np.zeros((n * d, n * d))
    I = np.eye(d)
    for u, v in edges:
        O = frames[u].T @ frames[v]
        su, sv = u * d, v * d
        L[su:su + d, su:su + d] += I
        L[sv:sv + d, sv:sv + d] += I
        L[su:su + d, sv:sv + d] -= O
        L[sv:sv + d, su:su + d] -= O.T
    return L


def components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    return len({find(i) for i in range(n)})


def honest_network(n_honest, rng):
    """A small connected honest complex with consistent frames."""
    edges = [(i, i + 1) for i in range(n_honest - 1)]
    for _ in range(n_honest // 2):                    # a few chords
        u, v = rng.integers(0, n_honest, 2)
        if u != v:
            edges.append((min(int(u), int(v)), max(int(u), int(v))))
    frames = [random_orthogonal(D, rng) for _ in range(n_honest)]
    return sorted(set(edges)), frames


def with_duplicates(n_honest, edges, frames, n_copies, mode, rng):
    """
    Adversary owns vertex 0 and adds n_copies duplicates of it: same frame,
    attached according to `mode`. Returns (n, edges, frames, adversary_ids).
    """
    edges = list(edges)
    frames = list(frames)
    orig = 0
    neighbours = [v for (u, v) in edges if u == orig] + \
                 [u for (u, v) in edges if v == orig]
    ids = []
    for c in range(n_copies):
        new = n_honest + c
        ids.append(new)
        frames.append(frames[orig].copy())            # verbatim duplicate
        if mode == "integrated":
            for nb in neighbours:
                edges.append((min(new, nb), max(new, nb)))
        elif mode == "bridged":
            if c == 0:
                edges.append((min(orig, new), max(orig, new)))
            else:
                prev = ids[c - 1]
                edges.append((min(prev, new), max(prev, new)))
        elif mode == "isolated":
            if c > 0:
                prev = ids[c - 1]
                edges.append((min(prev, new), max(prev, new)))
        elif mode == "scattered":
            pass          # each copy is its own component, touching nothing
        else:
            raise ValueError(mode)
    return n_honest + n_copies, sorted(set(edges)), frames, ids


def dims(n, edges, frames):
    ev = np.linalg.eigvalsh(sheaf_laplacian(n, edges, frames))
    return {e: int(np.sum(ev < e)) for e in EPS}


def marginal_credit(n_honest, edges0, frames0, n_copies, mode, rng):
    """
    The adversary group's marginal contribution to the score:
        v(everyone) - v(everyone except the adversary's copies)
    computed at each epsilon. This is the §4.1 marginal-removal reward,
    aggregated over the group, i.e. exactly what Sybil T1 needs bounded.
    """
    n, edges, frames, ids = with_duplicates(
        n_honest, edges0, frames0, n_copies, mode, rng)
    full = dims(n, edges, frames)
    keep = [i for i in range(n) if i not in set(ids)]
    remap = {old: new for new, old in enumerate(keep)}
    e_sub = [(remap[u], remap[v]) for (u, v) in edges
             if u in remap and v in remap]
    f_sub = [frames[i] for i in keep]
    sub = dims(len(keep), e_sub, f_sub)
    return {e: full[e] - sub[e] for e in EPS}, full, components(n, edges)


if __name__ == "__main__":
    rng = np.random.default_rng(19)
    N_HONEST = 24
    edges0, frames0 = honest_network(N_HONEST, rng)

    base = dims(N_HONEST, edges0, frames0)
    print("=" * 78)
    print(f"H1 ON H^0 — honest network n={N_HONEST}, stalk d={D}, "
          f"components={components(N_HONEST, edges0)}")
    print("=" * 78)
    print(f"  honest dim ker: " + "  ".join(f"eps={e:<7g} {base[e]:>3d}" for e in EPS))
    print(f"  (coherent connected sheaf should give exactly d = {D})")

    for mode in ("integrated", "bridged", "isolated", "scattered"):
        print(f"\n{'-' * 78}\nmode = {mode}")
        print(f"  {'copies':>7}{'comps':>7}" +
              "".join(f"{'ker@' + f'{e:g}':>13}" for e in EPS) +
              "   adversary marginal credit")
        for nc in (0, 1, 2, 4, 8):
            if nc == 0:
                print(f"  {0:>7}{components(N_HONEST, edges0):>7}" +
                      "".join(f"{base[e]:>13d}" for e in EPS) + "        —")
                continue
            r = np.random.default_rng(100 + nc)
            credit, full, comps = marginal_credit(
                N_HONEST, edges0, frames0, nc, mode, r)
            cred = " ".join(f"{credit[e]:+d}" for e in EPS)
            print(f"  {nc:>7}{comps:>7}" +
                  "".join(f"{full[e]:>13d}" for e in EPS) + f"    [{cred}]")

    print("\n" + "=" * 78)
    print("READING THE TABLE")
    print("=" * 78)
    print("  A coherent connected sheaf has dim H^0 = d exactly, and d per")
    print("  COMPONENT. So the exact column tests whether duplication creates")
    print("  section space, and the loose-epsilon columns test whether it creates")
    print("  APPROXIMATE sections — which is what a deployed mechanism scores.")
    print()
    print("  H1 holds iff adversary marginal credit does not grow with copies.")
    print("  If it grows at loose epsilon but not at machine precision, then")
    print("  duplication is neutral in theory and profitable in practice, and")
    print("  the gap is a numerical tolerance rather than a theorem.")
