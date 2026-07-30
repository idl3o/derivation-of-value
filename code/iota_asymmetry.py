"""
Is iota symmetric?

CP §7.1 defines iota directionally — "the fraction of pi_j's fake-cost that is
NOT recoverable from having faked pi_i" — but never asks whether iota(j|i) and
iota(i|j) agree. The question is not idle. If iota is symmetric it is a candidate
METRIC on projection space, Definition 5.1 becomes a genuine packing number, and
the Fisher-information route to formalising richness is open. If it is asymmetric,
the right object is a DIVERGENCE, not a metric, and the asymmetry itself carries
content — it encodes which attack should be mounted first.

independence.py measured one direction only, using one attack. Measuring both
directions needs two attacks with different targets:

  Attack F (frames)    Make a coalition's frames mutually consistent.
                       Targets pi_ker: creates approximate global sections.

  Attack T (topology)  Sparsify the coalition's cross-links, leaving frames
                       frustrated. Targets pi_dim: the spectral dimension falls
                       with reticulation density (1.26 at cross=1, 2.23 at
                       cross=8), so an adversary can move d_s toward the honest
                       value by thinning the structure — spectral mimicry
                       without coherence.

Then for an attack targeting i and achieving progress p_i, the incidental
progress p_j gives

    iota(j | i) = 1 - p_j / p_i

the fraction of j NOT delivered for free by the i-attack. Comparing
iota(dim | ker) against iota(ker | dim) answers the question.

Run:  python iota_asymmetry.py
"""
import numpy as np

from complexes import hierarchical_modular, random_orthogonal
from spectral_richness import spectral_dimension

SOFT = 0.05
STALK = 3
DEPTH = 10


def build_laplacian(n, edges, rng, coherent_set, d=STALK):
    """Edges inside coherent_set get consistent frames; all others random O(d)."""
    frames = [random_orthogonal(d, rng) for _ in range(n)]
    L = np.zeros((n * d, n * d))
    I = np.eye(d)
    for u, v in edges:
        O = (frames[u].T @ frames[v]) if (u in coherent_set and v in coherent_set) \
            else random_orthogonal(d, rng)
        su, sv = u * d, v * d
        L[su:su + d, su:su + d] += I
        L[sv:sv + d, sv:sv + d] += I
        L[su:su + d, sv:sv + d] -= O
        L[sv:sv + d, su:su + d] -= O.T
    return L


def score(evals):
    ev = np.sort(evals)
    d_s, _ = spectral_dimension(ev)
    return {"ker": int(np.sum(ev < SOFT)), "dim": d_s}


def attack_frames(n, edges, rng, f):
    """Coalition = aligned block of size f*n, made frame-consistent."""
    coalition = set(range(max(1, int(f * n))))
    return edges, coalition


def components(n, edges):
    """Connected-component count, by union-find."""
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


def attack_topology_SPARSIFY_BROKEN(n, edges, rng, f):
    """
    RETAINED AS A RECORD OF A FAILED MEASUREMENT — do not use.

    Drops a fraction f of the edges inside an aligned block. It does lower d_s,
    but it also DISCONNECTS the complex, and every new component contributes its
    own near-zero eigenvalues. pi_ker (= #{lambda < SOFT}) counts those, so this
    attack appeared to "fake the kernel" with progress of 6.6 and 13.6 — i.e.
    far above the honest value, which is nonsense: an adversary cannot produce
    more global sections than a fully coherent substrate has. The measurement
    was of shattering, not of coherence. Same species of artefact as the
    degenerate-eigenvalue error in spectral_richness.distinct_levels.
    """
    block = set(range(n // 2))
    inside = [e for e in edges if e[0] in block and e[1] in block]
    outside = [e for e in edges if not (e[0] in block and e[1] in block)]
    keep = int(round((1.0 - f) * len(inside)))
    if keep < len(inside):
        idx = rng.permutation(len(inside))[:keep]
        inside = [inside[i] for i in sorted(idx)]
    return outside + inside, set()


def attack_topology(n, edges, rng, f):
    """
    Degree-preserving double-edge swaps confined to an aligned block, frames left
    frustrated. Rewiring changes the reticulation PATTERN — and so d_s — while
    holding edge count and degree sequence fixed, which keeps the complex
    connected and leaves pi_ker uncontaminated by shattering.
    """
    block = set(range(n // 2))
    inside = [e for e in edges if e[0] in block and e[1] in block]
    outside = [e for e in edges if not (e[0] in block and e[1] in block)]
    if len(inside) < 4:
        return edges, set()
    cur = list(inside)
    eset = set(cur)
    n_swaps = int(round(f * len(cur)))
    done = 0
    for _ in range(n_swaps * 12):
        if done >= n_swaps:
            break
        i, j = rng.integers(0, len(cur), 2)
        if i == j:
            continue
        (a, b), (c, d) = cur[i], cur[j]
        if len({a, b, c, d}) < 4:
            continue
        e1 = (min(a, c), max(a, c))
        e2 = (min(b, d), max(b, d))
        if e1 in eset or e2 in eset:
            continue
        eset.discard(cur[i]); eset.discard(cur[j])
        eset.add(e1); eset.add(e2)
        cur[i], cur[j] = e1, e2
        done += 1
    return outside + sorted(eset), set()


def progress(s, base, honest):
    pk = s["ker"] / max(honest["ker"] - base["ker"], 1e-9)
    pd = (base["dim"] - s["dim"]) / max(base["dim"] - honest["dim"], 1e-9)
    return max(0.0, pk), max(0.0, pd)


if __name__ == "__main__":
    n = 2 ** DEPTH
    rng = np.random.default_rng(7)
    _, edges = hierarchical_modular(DEPTH, rng, cross_per_merge=2)

    base = score(np.linalg.eigvalsh(build_laplacian(
        n, edges, np.random.default_rng(11), set())))
    honest = score(np.linalg.eigvalsh(build_laplacian(
        n, edges, np.random.default_rng(12), set(range(n)))))

    print("=" * 72)
    print("IS IOTA SYMMETRIC?")
    print("=" * 72)
    print(f"  frustrated : pi_ker={base['ker']:>4}  pi_dim={base['dim']:.3f}")
    print(f"  honest     : pi_ker={honest['ker']:>4}  pi_dim={honest['dim']:.3f}")

    results = {}
    for label, attack, target in (("F (frames)  -> targets pi_ker", attack_frames, "ker"),
                                  ("T (topology)-> targets pi_dim", attack_topology, "dim")):
        print(f"\n  Attack {label}")
        print(f"    {'intensity':>10}{'pi_ker':>8}{'pi_dim':>9}"
              f"{'ker prog':>10}{'dim prog':>10}{'comps':>7}")
        rows = []
        for f in (0.125, 0.25, 0.5, 0.75):
            r = np.random.default_rng(200 + int(1000 * f))
            e2, coal = attack(n, edges, r, f)
            comps = components(n, e2)
            s = score(np.linalg.eigvalsh(build_laplacian(n, e2, r, coal)))
            pk, pd = progress(s, base, honest)
            rows.append((f, pk, pd, comps))
            warn = "  <-- SHATTERED" if comps > 1 else ""
            print(f"    {f:>10.3f}{s['ker']:>8}{s['dim']:>9.3f}"
                  f"{pk:>10.3f}{pd:>10.3f}{comps:>7d}{warn}")
        results[target] = rows

    print("\n" + "=" * 72)
    print("DIRECTIONAL IOTA   iota(j|i) = 1 - progress_j / progress_i")
    print("=" * 72)

    def directional(rows, tgt_key, other_key, min_progress=0.25):
        """
        iota(other | tgt) from runs where the attack ACTUALLY WORKED.

        The guard is the point. An attack that moves its own target by 0.04
        yields a ratio dominated by noise, and reporting it as an iota estimate
        is how you manufacture a finding. Runs are admitted only if the attack
        reached min_progress on its own target AND left the complex connected.
        """
        vals = []
        for f, pk, pd, comps in rows:
            own = pk if tgt_key == "ker" else pd
            oth = pd if tgt_key == "ker" else pk
            if own >= min_progress and comps == 1:
                vals.append(1.0 - oth / own)
        return vals

    ik = directional(results["ker"], "ker", "dim")   # iota(dim | ker)
    idm = directional(results["dim"], "dim", "ker")  # iota(ker | dim)

    def show(name, vals):
        if not vals:
            print(f"  {name:<22} -- attack never achieved its target")
            return None
        m = float(np.mean(vals))
        print(f"  {name:<22} {m:>7.3f}   (samples: "
              + ", ".join(f"{v:.2f}" for v in vals) + ")")
        return m

    a = show("iota(dim | ker)", ik)
    b = show("iota(ker | dim)", idm)

    print()
    if a is None or b is None:
        print("  VERDICT: NOT MEASURED. One direction has no admissible run —")
        print("  the attack never moved its own target far enough to divide by,")
        print("  or it shattered the complex. Note that iota is DEFINITIONALLY")
        print("  directional (CP §7.1); what is unresolved is whether it is")
        print("  SUBSTANTIALLY asymmetric. Two attack designs have now failed:")
        print("  sparsification shatters, rewiring is too weak. That difficulty")
        print("  is itself weak evidence that d_s is hard to move without")
        print("  either doing the coherence work or destroying the substrate —")
        print("  but a failure to build an attack is not proof that none exists.")
    else:
        gap = abs(a - b)
        print(f"  |iota(dim|ker) - iota(ker|dim)| = {gap:.3f}")
        if gap < 0.15:
            print("  -> SYMMETRIC to within noise. iota is a metric candidate;")
            print("     Definition 5.1 is a genuine packing number.")
        else:
            print("  -> SUBSTANTIALLY ASYMMETRIC. The right object is a")
            print("     DIVERGENCE, not a metric, and the asymmetry encodes")
            print("     attack ordering.")
