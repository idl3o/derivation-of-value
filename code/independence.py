"""
An adversary in the loop: measuring conditional fake-cost between projections.

Combination Proofs §6 makes a specific, load-bearing, and until now untested
claim about the coherence substrate:

    "a colluding cluster of miners can fake the kernel by agreeing on outputs
     at an instant, but reproducing the spectral signature of genuine coherence
     requires reproducing the DYNAMICAL STRUCTURE of an actually coherent
     system, which the cluster has no shortcut to compute."

That is an independence claim in the sense of Definition 2.5, and the whole
multiplication claim rests on it. This script tries to break it.

ATTACK MODEL. The substrate starts fully frustrated — nobody has done the work
of building coherent world-models, so no global section exists. An adversary
controls a coalition of fraction f of the nodes and makes their frames mutually
consistent. This is exactly "agreeing on outputs at an instant": cheap, requiring
no modelling of the world, costing only coordination.

Two adversaries, of different capability (Definition 2.4's "rarer resource"):

    A1  naive           — coalition is a uniformly random subset.
    A2  structure-aware — coalition is a block aligned to the complex's own
                          nesting: the attacker knows the hierarchy and colludes
                          ALONG it rather than across it.

PROJECTIONS, all read off the same operator:

    pi_ker   approximate global sections, #{lambda < 0.05}   (Proof of Coherence)
    pi_dim   spectral dimension d_s                          (the new candidate)

MEASUREMENT. Both projections are normalised to PROGRESS in [0,1]: 0 at the
frustrated substrate, 1 at the honest one. Then for a mechanism whose
conjunction-gate sits at threshold tau (Definition 2.6),

    iota(tau) = 1 - (dim progress / ker progress) at the f where ker reaches tau

    iota -> 1   faking the kernel buys NOTHING toward the spectral dimension
                (independent; the conjunction genuinely multiplies)
    iota -> 0   faking the kernel hands you the dimension for free
                (not independent; the third projection buys nothing)

Definition 2.5 additionally requires the discrepancy to VANISH as substrate
depth grows, so iota is reported across depths and the trend is what matters.

--------------------------------------------------------------------------
A LIMIT OF THIS EXPERIMENT, WHICH BOUNDS WHAT IT CAN CONCLUDE.

§6's independence claim rests on a distinction in TIME: a coalition "agreeing
on outputs at an instant" versus reproducing "the dynamical structure of an
actually coherent system ... as the complex evolves epoch over epoch". This
toy has no time axis. The sheaf here is a single static snapshot, in which
agreeing at an instant and having genuinely done the work are indistinguishable
BY CONSTRUCTION — the adversary who makes a coalition internally consistent has
not faked coherence on that coalition, it has produced it.

So this script cannot refute §6 as §6 is stated. What it CAN establish is
whether the static spectral dimension is independent of the static kernel, and
that is a question worth settling on its own, because a cheap third projection
that needed no temporal machinery would have been worth having.
--------------------------------------------------------------------------

Run:  python independence.py
"""
import numpy as np

from complexes import hierarchical_modular, random_orthogonal
from spectral_richness import spectral_dimension

SOFT = 0.05
STALK = 3


def partial_coherent_laplacian(n, edges, rng, coalition, d=STALK):
    """Edges inside the coalition carry consistent frames; all others random O(d)."""
    frames = [random_orthogonal(d, rng) for _ in range(n)]
    L = np.zeros((n * d, n * d))
    I = np.eye(d)
    coal = coalition
    for u, v in edges:
        O = frames[u].T @ frames[v] if (u in coal and v in coal) \
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


def progress(s, base, honest):
    """Normalise each projection to [0,1]: 0 = frustrated, 1 = honest."""
    pk = s["ker"] / max(honest["ker"] - base["ker"], 1e-9)
    pd = (base["dim"] - s["dim"]) / max(base["dim"] - honest["dim"], 1e-9)
    return max(0.0, pk), max(0.0, pd)


def iota_at(rows, tau, min_reach=0.5):
    """
    Interpolate to the f where ker progress first reaches tau, and read the
    dim progress achieved there. iota = 1 - dim_progress/ker_progress.

    Returns None when the attack never gets pi_ker near tau under its own steam
    (max ker progress below `min_reach`*tau before f=1). An attack that achieves
    nothing has no conditional fake-cost to measure, and forcing a number out of
    it produces the meaningless negative values that A1 reported in the first
    version of this script.
    """
    interior = [r for r in rows if r[0] < 1.0]
    if not interior or max(pk for _, pk, _ in interior) < min_reach * tau:
        return None
    prev = None
    for f, pk, pd in rows:
        if pk >= tau:
            if prev is not None and pk > prev[1]:
                w = (tau - prev[1]) / (pk - prev[1])
                pd = prev[2] + w * (pd - prev[2])
            return 1.0 - pd / tau
        prev = (f, pk, pd)
    return None


def run_depth(depth, adversaries, f_grid, seed=7):
    n = 2 ** depth
    rng = np.random.default_rng(seed)
    _, edges = hierarchical_modular(depth, rng, cross_per_merge=2)

    base = score(np.linalg.eigvalsh(partial_coherent_laplacian(
        n, edges, np.random.default_rng(seed + 1), set())))
    honest = score(np.linalg.eigvalsh(partial_coherent_laplacian(
        n, edges, np.random.default_rng(seed + 2), set(range(n)))))
    print(f"\n  depth {depth} (n={n})")
    print(f"    frustrated : pi_ker={base['ker']:>4}  pi_dim={base['dim']:.3f}")
    print(f"    honest     : pi_ker={honest['ker']:>4}  pi_dim={honest['dim']:.3f}")

    out = {}
    for label, maker in adversaries:
        rows = []
        print(f"\n    {label}")
        print(f"      {'f':>7}{'pi_ker':>8}{'pi_dim':>9}"
              f"{'ker prog':>10}{'dim prog':>10}")
        for f in f_grid:
            size = max(1, int(round(f * n)))
            r = np.random.default_rng(seed + 100 + size)
            coal = maker(n, size, r)
            s = score(np.linalg.eigvalsh(
                partial_coherent_laplacian(n, edges, r, coal)))
            pk, pd = progress(s, base, honest)
            rows.append((f, pk, pd))
            print(f"      {f:>7.3f}{s['ker']:>8}{s['dim']:>9.3f}"
                  f"{pk:>10.3f}{pd:>10.3f}")
        out[label] = rows
    return out


if __name__ == "__main__":
    print("=" * 74)
    print("ADVERSARIAL TEST — is the spectral dimension independent of the kernel?")
    print("=" * 74)

    adversaries = [
        ("A1 naive (random subset)",
         lambda n, size, rng: set(int(x) for x in rng.choice(n, size, replace=False))),
        ("A2 structure-aware (aligned block)",
         lambda n, size, rng: set(range(size))),
    ]

    results = {}
    results[9] = run_depth(9, adversaries, [0.03, 0.06, 0.125, 0.25, 0.5, 1.0])
    results[10] = run_depth(10, adversaries, [0.03, 0.06, 0.125, 0.25, 0.5, 1.0])
    # depth 11 is a 6144x6144 eigendecomposition per point: aligned adversary only,
    # on the reduced grid that the iota thresholds actually need.
    results[11] = run_depth(11, adversaries[1:], [0.06, 0.125, 0.25, 0.5, 1.0])

    print(f"\n{'=' * 74}")
    print("INDEPENDENCE  iota(tau)  —  1 = kernel-faking buys nothing toward d_s")
    print("=" * 74)
    print(f"  {'adversary':>36}{'depth':>7}"
          + "".join(f"{'t=' + str(t):>9}" for t in (0.1, 0.25, 0.5)))
    for label in [a[0] for a in adversaries]:
        for depth in sorted(results):
            if label not in results[depth]:
                continue
            rows = results[depth][label]
            cells = ""
            for tau in (0.1, 0.25, 0.5):
                v = iota_at(rows, tau)
                cells += f"{v:>9.2f}" if v is not None else f"{'--':>9}"
            print(f"  {label:>36}{depth:>7}{cells}")

    print("\n  Definition 2.5 asks the discrepancy to vanish as substrate depth")
    print("  grows — i.e. iota should RISE toward 1 down each column.")
