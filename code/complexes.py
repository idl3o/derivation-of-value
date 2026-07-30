"""
Complexes and Laplacians for the spectral-richness measurements.

Objects follow Combination Proofs §6: a sheaf 𝓕 over a coloured simplicial
complex K, scored by the sheaf Hodge Laplacian Δ_𝓕. We work at the 1-skeleton,
so Δ_𝓕 = δᵀδ with δ the sheaf coboundary; ker Δ_𝓕 ≅ H⁰(K, 𝓕) = global sections.

All randomness is passed in explicitly. Every reported figure is reproducible
from the seeds in spectral_richness.py.
"""
import numpy as np

__all__ = [
    "sierpinski_gasket", "grid_2d", "erdos_renyi", "hierarchical_modular",
    "graph_laplacian", "sheaf_laplacian",
]


# --------------------------------------------------------------- complexes

def sierpinski_gasket(level):
    """
    Level-n Sierpiński gasket graph, exact integer coordinates. |V| = 3(3ⁿ+1)/2.

    CALIBRATION OBJECT ONLY. Its spectral dimension is known analytically
    (2·log3/log5 ≈ 1.3652), so it tells us whether the measurement pipeline
    can be trusted before the pipeline is pointed at anything unknown.
    """
    verts = {(0, 0), (1, 0), (0, 1)}
    edges = {((0, 0), (1, 0)), ((0, 0), (0, 1)), ((1, 0), (0, 1))}
    for n in range(1, level + 1):
        s = 2 ** (n - 1)
        nv, ne = set(), set()
        for ox, oy in [(0, 0), (s, 0), (0, s)]:
            nv |= {(x + ox, y + oy) for (x, y) in verts}
            for (a, b) in edges:
                p, q = (a[0] + ox, a[1] + oy), (b[0] + ox, b[1] + oy)
                ne.add((p, q) if p < q else (q, p))
        verts, edges = nv, ne
    idx = {v: i for i, v in enumerate(sorted(verts))}
    return len(verts), [(idx[a], idx[b]) for a, b in edges]


def grid_2d(side):
    """Square lattice. Second calibration object: spectral dimension exactly 2."""
    edges = []
    for r in range(side):
        for c in range(side):
            i = r * side + c
            if c + 1 < side:
                edges.append((i, i + 1))
            if r + 1 < side:
                edges.append((i, i + side))
    return side * side, edges


def erdos_renyi(n, mean_degree, rng):
    """Control: no nesting of any kind. Expander-like; carries no spectral dimension."""
    target = int(n * mean_degree / 2)
    seen = set()
    while len(seen) < target:
        u, v = rng.integers(0, n, 2)
        if u != v:
            seen.add((min(int(u), int(v)), max(int(u), int(v))))
    return n, sorted(seen)


def hierarchical_modular(depth, rng, cross_per_merge=2):
    """
    The nested-models coherence complex: 2^depth leaves, and at every level each
    pair of sibling blocks is joined by `cross_per_merge` random cross-edges.

    This operationalises the claim that world-models nest — agents model agents
    modelling agents — so the complex is tiered rather than flat. It is
    self-similar in its CONSTRUCTION RULE only. It is deliberately NOT a
    geometric fractal: if it were, any anomalous dimension found in it would
    have been smuggled into the question rather than discovered in the answer.
    """
    n = 2 ** depth
    edges = set()
    for lvl in range(1, depth + 1):
        block = 2 ** lvl
        for start in range(0, n, block):
            half = block // 2
            for _ in range(cross_per_merge):
                u = int(rng.integers(start, start + half))
                v = int(rng.integers(start + half, start + block))
                edges.add((min(u, v), max(u, v)))
    return n, sorted(edges)


# --------------------------------------------------------------- Laplacians

def graph_laplacian(n, edges):
    """Scalar case: stalks ℝ¹, all restriction maps the identity."""
    L = np.zeros((n, n))
    for u, v in edges:
        L[u, u] += 1.0
        L[v, v] += 1.0
        L[u, v] -= 1.0
        L[v, u] -= 1.0
    return L


def random_orthogonal(d, rng):
    q, r = np.linalg.qr(rng.normal(size=(d, d)))
    return q * np.sign(np.diag(r))


def sheaf_laplacian(n, edges, rng, d=3, coherent=True):
    """
    Cellular sheaf with ℝᵈ stalks and O(d) restriction maps.

    coherent=True   O_uv = R_uᵀ R_v for random frames R. Consistent around every
                    cycle, so global sections exist and dim H⁰ = d. This is the
                    honest distribution of §6 — local sections genuinely glue.
    coherent=False  independent random O(d) per edge: a frustrated connection,
                    no global section, ker Δ_𝓕 = 0. The incoherent substrate.

    Note the coherent case is gauge-equivalent to (graph Laplacian) ⊗ I_d, so
    its spectrum is the scalar spectrum with every level d-fold degenerate.
    That degeneracy is exactly what corrupts a naive gap statistic — see
    spectral_richness.distinct_levels.
    """
    frames = [random_orthogonal(d, rng) for _ in range(n)] if coherent else None
    L = np.zeros((n * d, n * d))
    I = np.eye(d)
    for u, v in edges:
        O = frames[u].T @ frames[v] if coherent else random_orthogonal(d, rng)
        su, sv = u * d, v * d
        L[su:su + d, su:su + d] += I
        L[sv:sv + d, sv:sv + d] += I
        L[su:su + d, sv:sv + d] -= O
        L[sv:sv + d, su:su + d] -= O.T
    return L
