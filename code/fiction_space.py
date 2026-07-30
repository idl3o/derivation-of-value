"""
How much room does a coherent network have to be consistently wrong?

Proof of Coherence §2 lists, among the failure modes of coherentism, that "a
consistent fiction is consistent" and that coherence-of-coherence "collapses to
autopoietic-cult attractors". The program named that failure mode and never
measured it. This does.

Hansen and Ghrist showed the sheaf Laplacian implements a consensus algorithm:
gradient flow on the Dirichlet energy x^T L x drives any initial assignment
toward ker L, the global sections. So a coherence-maximising network is a
dynamical system, and the question is WHERE it lands.

  FICTION SPACE   the set of distinct outcomes that are all perfectly coherent.
                  If it is a single point, coherence picks out one world and
                  maximising it is the same as finding that world. If it has
                  dimension, coherence does not determine content, and a network
                  can converge on any point in it while scoring perfectly.

  STRUCTURAL      Maturana and Varela's term for the contact with an outside
  COUPLING        that keeps a closed system from being purely self-referential.
                  Here: how many scalars must be pinned to something external
                  before the fiction space collapses to a point?

The second question is the design question, because Gauge-Fixing's anchors fix
PROVENANCE — who produced a section and when — and say nothing about its
CONTENT. If content-anchoring is what collapses the fiction space, then the
program's anchors, however well built, do not address closure at all.

Run:  python fiction_space.py
"""
import numpy as np

from complexes import random_orthogonal

D = 3


def build(n, rng, connected=True, extra=None):
    """Connected coherent sheaf: O_uv = R_u^T R_v, so dim ker = d per component."""
    edges = [(i, i + 1) for i in range(n - 1)] if connected else []
    if extra:
        edges += extra
    frames = [random_orthogonal(D, rng) for _ in range(n)]
    L = np.zeros((n * D, n * D))
    I = np.eye(D)
    for u, v in set(edges):
        O = frames[u].T @ frames[v]
        su, sv = u * D, v * D
        L[su:su + D, su:su + D] += I
        L[sv:sv + D, sv:sv + D] += I
        L[su:su + D, sv:sv + D] -= O
        L[sv:sv + D, su:su + D] -= O.T
    return L, frames


def kernel_dim(L, tol=1e-8):
    return int(np.sum(np.linalg.eigvalsh(L) < tol))


def consensus(L, x0, steps=60000, eta=0.05):
    """Gradient flow on the Dirichlet energy — the sheaf consensus dynamic."""
    x = x0.copy()
    for _ in range(steps):
        x = x - eta * (L @ x)
    return x


def kernel_basis(L, tol=1e-8):
    w, V = np.linalg.eigh(L)
    return V[:, w < tol]


def ground(L, vertex, k):
    """
    Pin k of the d scalars at one vertex to an external reference, by adding a
    large penalty on those coordinates. This is structural coupling made
    concrete: contact with something the network did not produce.
    """
    Lg = L.copy()
    for j in range(k):
        idx = vertex * D + j
        Lg[idx, idx] += 1e6
    return Lg


if __name__ == "__main__":
    rng = np.random.default_rng(5)
    N = 20
    L, frames = build(N, rng)

    print("=" * 76)
    print(f"FICTION SPACE — coherent sheaf, n={N}, stalk d={D}, connected")
    print("=" * 76)
    k = kernel_dim(L)
    print(f"  dim ker L = {k}   (= d, the whole space of perfectly coherent states)")

    print("\n  Consensus from random starts — does it converge somewhere unique?")
    B = kernel_basis(L)
    outcomes = []
    for s in range(5):
        r = np.random.default_rng(50 + s)
        x = consensus(L, r.normal(size=N * D))
        outcomes.append(x)
        outside = np.linalg.norm(x - B @ (B.T @ x))
        print(f"    start {s}: |Lx| = {np.linalg.norm(L @ x):.2e}   "
              f"outside ker = {outside:.2e}   |x| = {np.linalg.norm(x):7.4f}")

    # Rank must be measured on the projections INTO ker, with a tolerance above
    # the residual. Otherwise incomplete convergence is counted as extra
    # dimensions: the first version of this script reported five outcomes
    # spanning five dimensions inside a three-dimensional kernel, which is
    # impossible, and the impossibility is what exposed the error.
    P = np.array([B.T @ x for x in outcomes])
    span = np.linalg.matrix_rank(P, tol=1e-6 * max(float(np.linalg.norm(P)), 1.0))
    print(f"\n    All five are global sections, and their kernel components span "
          f"{span} dimensions —")
    print(f"    exactly dim ker = {k}, which they exhaust. Five different worlds,")
    print(f"    each perfectly coherent. Coherence did not choose between them;")
    print(f"    the initial condition did.")

    print("\n" + "=" * 76)
    print("STRUCTURAL COUPLING — what does it cost to close the fiction space?")
    print("=" * 76)
    print(f"  {'scalars pinned':>16}{'at vertices':>13}{'dim fiction space':>20}")
    for kk in range(0, D + 1):
        Lg = ground(L, 0, kk) if kk else L
        print(f"  {kk:>16}{1 if kk else 0:>13}{kernel_dim(Lg):>20}")
    print("\n  Pinning d scalars AT A SINGLE VERTEX collapses it completely.")
    print("  Not d per vertex, not a fraction of the network — d numbers, once.")
    print("  Because a global section of a connected coherent sheaf is determined")
    print("  by its value at any one point: fix x_v and you have fixed all of x.")

    print("\n" + "=" * 76)
    print("DOES COUPLING SCALE WITH THE NETWORK, OR WITH ITS COMPONENTS?")
    print("=" * 76)
    for n_comp in (1, 2, 4):
        blocks = []
        per = N // n_comp
        edges = []
        for c in range(n_comp):
            base = c * per
            edges += [(base + i, base + i + 1) for i in range(per - 1)]
        r = np.random.default_rng(77)
        Lc, _ = build(N, r, connected=False, extra=edges)
        need = 0
        Lg = Lc
        for c in range(n_comp):
            Lg = ground(Lg, c * per, D)
            need += D
        print(f"  {n_comp} component(s): dim ker = {kernel_dim(Lc):>2}  ->  "
              f"pinning {need} scalars ({n_comp} x d, one vertex each) "
              f"leaves {kernel_dim(Lg)}")
    print("\n  Coupling required scales with COMPONENTS, not with size. A network")
    print("  ten times larger needs no more contact with the world. A network that")
    print("  has split in two needs twice as much.")
