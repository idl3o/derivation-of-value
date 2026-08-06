"""
The trace gap τ = f/w, measured.

Sign and Work Def 3.1–3.3: w(π) is what an honest participant expends to perform
the work π evidences; f(π) is the minimum an attacker in the class expends to
produce a trace π accepts WITHOUT doing the work; τ(π) = f(π)/w(π).

Two properties of the definition drive everything here.

FIRST, τ is a property of the READING, not of the substrate (§4, final paragraph).
Two mechanisms on the same complex — one measuring it, one accepting a certificate
about it — have identical ρ and wildly different τ. So a specimen here is not a
substrate; it is a triple (work, reading rule, attacker class).

SECOND, and this is the instrument's governing limitation: f is a MINIMUM over an
attacker class, and this code can only minimise over strategies someone has written
down. A strategy nobody thought of is cheaper than every strategy here. Therefore

    measured τ  ≥  true τ,     always.

The instrument errs toward safety and can never err against it. A low τ is a real
finding — it exhibits a forgery, and exhibiting one settles the matter. A high τ is
the absence of evidence and certifies nothing. τ detects; it does not certify. This
is the same shape as the cohomological invariant in No Global Section (claim 4), and
it was not anticipated when this file was started.

Units cancel inside a specimen and are meaningless across specimens, which is why
Def 3.3 is a ratio. No τ here is comparable to any other τ here (gallery §6).

CALIBRATION FIRST. Two specimens have answers known before measuring — proof of
work at exactly 1, a signed claim at ~0 — and the pipeline is pointed at them before
it is pointed at the coherence score, whose τ is the actual question.

Seeded throughout. `python trace_gap.py` reproduces every number quoted.
"""
import hashlib
import sys
from collections import deque

import numpy as np

from complexes import hierarchical_modular, graph_laplacian, random_orthogonal
from spectral_richness import spectral_dimension, local_slope_spread

__all__ = ["Specimen", "pow_specimen", "signed_claim_specimen",
           "coherence_specimen", "measure"]


class Specimen:
    """
    A reading rule plus an attacker class.

    forgeries is a list of (name, thunk) where the thunk returns (cost, accepted).
    A forgery that the reading rule REJECTS contributes nothing to f, however cheap
    it is — which is the whole content of a reading rule.
    """

    def __init__(self, name, earning_cost, forgeries, note=""):
        self.name = name
        self.earning_cost = earning_cost
        self.forgeries = forgeries
        self.note = note

    def tau(self):
        accepted = [(n, c) for n, (c, ok) in
                    ((n, t()) for n, t in self.forgeries) if ok]
        if not accepted:
            return float("inf"), "no strategy in the class produced an accepted trace"
        name, cost = min(accepted, key=lambda p: p[1])
        return cost / self.earning_cost, name


# ------------------------------------------------------ calibration: τ = 1

def _leading_zero_bits(digest, bits):
    return int.from_bytes(digest, "big") >> (256 - bits) == 0


def pow_specimen(bits=13, trials=400, seed=0):
    """
    CALIBRATION OBJECT. Known answer: τ = 1 exactly.

    Reading rule: accept (challenge, nonce) iff sha256(challenge||nonce) has `bits`
    leading zeros. Work = the search. The attacker class is {replay a solution to an
    old challenge, guess once, search}. No preimage shortcut is granted, because none
    is known for sha256 — so the cheapest ACCEPTED strategy is the search itself, and
    f = w by construction.

    This is τ's Sierpiński gasket. If the pipeline does not return 1.0 here, nothing
    else it says is worth reading.

    WRONG ON THE FIRST PASS, and named here rather than quietly repaired. The first
    version compared the attacker's cost on ONE search against the honest mean over
    eight, and returned τ = 2.74 on a specimen whose answer is 1. Search length is
    geometric with standard deviation ≈ its mean, so a single draw carries ~100%
    error. τ is a ratio of EXPECTATIONS and both must be estimated alike; the fix is
    to average the attacker's search over `trials` fresh challenges too. The failure
    is worth keeping because it is the only reason the bug was visible: had the
    calibration specimen been omitted, the same estimator would have gone on to
    report the coherence numbers below with no indication anything was wrong.
    """
    rng = np.random.default_rng(seed)

    def search(challenge):
        n, h = 0, 0
        while True:
            d = hashlib.sha256(challenge + n.to_bytes(8, "big")).digest()
            h += 1
            if _leading_zero_bits(d, bits):
                return n, h
            n += 1

    honest_hashes, stale = [], []
    for _ in range(trials):
        ch = rng.integers(0, 2 ** 60).item().to_bytes(8, "big")
        nonce, h = search(ch)
        honest_hashes.append(h)
        stale.append((ch, nonce))
    w = float(np.mean(honest_hashes))

    fresh = rng.integers(0, 2 ** 60).item().to_bytes(8, "big")

    def replay():
        # One hash to submit a nonce that worked for a DIFFERENT challenge.
        _, old_nonce = stale[0]
        d = hashlib.sha256(fresh + old_nonce.to_bytes(8, "big")).digest()
        return 1.0, _leading_zero_bits(d, bits)

    def guess_once():
        n = int(rng.integers(0, 2 ** 60))
        d = hashlib.sha256(fresh + n.to_bytes(8, "big")).digest()
        return 1.0, _leading_zero_bits(d, bits)

    def do_the_search():
        # Averaged over the same number of fresh challenges as w, for the reason
        # named in the docstring. One draw is not an expectation.
        hs = []
        for _ in range(trials):
            ch = rng.integers(0, 2 ** 60).item().to_bytes(8, "big")
            hs.append(search(ch)[1])
        return float(np.mean(hs)), True

    return Specimen(
        f"proof of work ({bits}-bit target, {trials} trials)", w,
        [("replay stale nonce", replay),
         ("single guess", guess_once),
         ("search (i.e. do the work)", do_the_search)],
        note="known answer τ = 1",
    )


# ------------------------------------------------------ calibration: τ ≈ 0

def signed_claim_specimen(work_units=1e6):
    """
    CALIBRATION OBJECT. Known answer: τ = 1/work_units ≈ 0.

    Reading rule: accept any validly-signed assertion "I performed the work." The
    signature is unforgeable; the CLAIM is free. Sign and Work §3 lists this as the
    canonical τ ≈ 0 regime — a bare signature, a self-reported metric, an oracle
    attestation. Borrowed Again puts the same point as τ ≈ 1 for "the key holder
    assented" and τ ≈ 0 for anything broader.

    Trivial, and here because a floor calibration is as necessary as a unit one.
    """
    return Specimen(
        "signed claim of work", float(work_units),
        [("sign a false claim", lambda: (1.0, True))],
        note="known answer τ = 1/w",
    )


# ------------------------------------------------------ the actual question

def _steiner_tree_edges(n, edges, terminals):
    """
    Edges of a cheap tree spanning `terminals`: repeated shortest-path attachment.
    Not optimal (Steiner is NP-hard) — and being an upper bound on the attacker's
    cost, it makes the reported τ larger, i.e. more optimistic. Stated because the
    direction of the error is the point.
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    terminals = list(terminals)
    tree, reached = set(), {terminals[0]}
    for t in terminals[1:]:
        prev, seen = {t: None}, deque([t])
        hit = None
        while seen:
            x = seen.popleft()
            if x in reached:
                hit = x
                break
            for y in adj[x]:
                if y not in prev:
                    prev[y] = x
                    seen.append(y)
        if hit is None:
            continue
        x = hit
        while prev[x] is not None:
            p = prev[x]
            tree.add((min(x, p), max(x, p)))
            reached.add(x)
            x = p
        reached.add(t)
    return tree


def coherence_specimen(depth=8, d=3, n_anchors=0, seed=0, eps=1e-8,
                       cross_per_merge=2):
    """
    The reading rule the program actually uses: score = #{λ(Δ_𝓕) < ε}, accepted if
    the score reaches d. Substrate is the hierarchical-modular complex of §6.

    WORK. An honest participant reconciles a genuine d-dimensional model across every
    edge: O_uv = R_uᵀ R_v for independently-chosen frames. Cost is counted in free
    parameters actually fixed — d(d−1)/2 per edge, the dimension of O(d).

    FORGERY. Set every frame equal. The connection is identity on every edge, the
    complex is perfectly coherent, dim ker = d, full marks — and nothing was
    reconciled, because there was nothing to reconcile. This is A Consistent Fiction's
    fiction space entered deliberately rather than converged to.

    ANCHORS. Gauge-Fixing pins frames at n_anchors vertices to externally fixed
    values. The forger must now agree with the anchors, and the all-equal trick fails
    the moment two anchors differ. But the coherent connection is gauge-invariant
    under a global R_v ↦ R_v Q, so ONE anchor is free — the forger rotates the whole
    fiction to meet it. The question this specimen exists to ask is what the second
    anchor and beyond cost, and whether any number of them lifts τ to 1.

    Acceptance is MEASURED — every configuration is scored by an actual
    eigendecomposition, not assumed to pass. A forgery that fails to score is dropped
    from f whatever it cost.
    """
    rng = np.random.default_rng(seed)
    n, edges = hierarchical_modular(depth, rng, cross_per_merge=cross_per_merge)
    per_edge = d * (d - 1) / 2
    w = len(edges) * per_edge

    anchors = sorted(rng.choice(n, size=n_anchors, replace=False).tolist()) \
        if n_anchors else []

    def score(L):
        return int(np.sum(np.linalg.eigvalsh(L) < eps))

    def build(frames):
        """Coherent connection from an explicit frame assignment."""
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

    fixed = {a: random_orthogonal(d, rng) for a in anchors}

    def all_equal():
        """Cost 0: one frame, repeated. Fails as soon as two anchors disagree."""
        base = fixed[anchors[0]] if anchors else np.eye(d)
        frames = [base] * n
        ok = score(build(frames)) >= d
        if anchors:
            ok = ok and all(np.allclose(frames[a], fixed[a]) for a in anchors)
        return 0.0, ok

    def reconcile_anchor_tree():
        """
        Meet every anchor by reconciling only a tree that spans them; everything off
        the tree is copied from its nearest tree vertex, so it costs nothing.
        """
        if len(anchors) < 2:
            return float("inf"), False
        tree = _steiner_tree_edges(n, edges, anchors)
        frames = [None] * n
        for a in anchors:
            frames[a] = fixed[a]
        adj = [[] for _ in range(n)]
        for u, v in tree:
            adj[u].append(v)
            adj[v].append(u)
        q = deque(anchors)
        while q:                                  # fill the tree outward
            x = q.popleft()
            for y in adj[x]:
                if frames[y] is None:
                    frames[y] = frames[x]
                    q.append(y)
        base = frames[anchors[0]]
        for i in range(n):                        # off-tree: free copies
            if frames[i] is None:
                frames[i] = base
        L = build(frames)
        ok = score(L) >= d and all(np.allclose(frames[a], fixed[a]) for a in anchors)
        return len(tree) * per_edge, ok

    def do_the_work():
        frames = [random_orthogonal(d, rng) for _ in range(n)]
        for a in anchors:
            frames[a] = fixed[a]
        return w, score(build(frames)) >= d

    return Specimen(
        f"coherence score H⁰, {n_anchors} anchor(s), depth {depth}", w,
        [("all frames equal", all_equal),
         ("reconcile anchor tree only", reconcile_anchor_tree),
         ("do the work", do_the_work)],
        note=f"|V|={n} |E|={len(edges)} anchors={anchors}",
    )


def generative_specimen(depth=8, d=3, rank=0, encoding=0.0, seed=0, eps=1e-8,
                        cross_per_merge=2):
    """
    ANCHORS READ GENERATIVELY, per Gauge-Fixing §4.3.

    coherence_specimen above anchors the OUTPUT: publicly-known frames the
    configuration must match. That is an anchor cited as a certificate of order,
    which §4.4 forbids by name and test-suite item (iv) says to check against. Its
    ceiling result is therefore test (i) with anchor 4.3 removed, and is kept as
    that. This function models the anchor the paper actually specifies.

    §4.3 does not constrain the configuration. It constrains how a section may be
    PRODUCED: a slow, sequentially dependent encoding keyed to identity and the
    epoch beacon, applied before the section enters the sheaf. So

      `rank`      how many of each frame's d columns are generatively determined —
                  fixed by the world rather than chosen by the participant. This is
                  the anchor's DIMENSION, which is the object the count sweep above
                  was the wrong coordinate for.
      `encoding`  cost of producing one admissible section, in the same units as
                  reconciling one edge. Nobody escapes it, honest or otherwise:
                  that is what makes it an anchor rather than a constraint.

    The prediction under test: τ should jump discontinuously at rank = 1 — the
    global gauge R_v ↦ R_v Q dies the moment any column is pinned at every vertex,
    so the all-frames-equal forgery dies with it — and then be FLAT in rank, because
    the encoding is paid per section however many columns it fixes. A linear climb
    in rank refutes the generative reading.
    """
    rng = np.random.default_rng(seed)
    n, edges = hierarchical_modular(depth, rng, cross_per_merge=cross_per_merge)
    per_edge = d * (d - 1) / 2
    w = n * encoding + len(edges) * per_edge

    true_frames = [random_orthogonal(d, rng) for _ in range(n)]

    def score(frames):
        L = np.zeros((n * d, n * d))
        I = np.eye(d)
        for u, v in edges:
            O = frames[u].T @ frames[v]
            su, sv = u * d, v * d
            L[su:su + d, su:su + d] += I
            L[sv:sv + d, sv:sv + d] += I
            L[su:su + d, sv:sv + d] -= O
            L[sv:sv + d, su:su + d] -= O.T
        return int(np.sum(np.linalg.eigvalsh(L) < eps))

    def admissible(frames):
        """Every section must carry the world's determined columns."""
        return all(np.allclose(frames[v][:, :rank], true_frames[v][:, :rank])
                   for v in range(n))

    def all_equal():
        """Free, and dead the moment rank ≥ 1 makes sections differ."""
        frames = [np.eye(d)] * n
        return 0.0, score(frames) >= d and admissible(frames)

    def encode_then_complete():
        """
        Pay the encoding for every section — unavoidable — then complete the free
        columns arbitrarily. The connection is flat by construction, so NO edge is
        ever reconciled. This is the whole forgery: the anchor is paid, the work is
        not.
        """
        if rank == 0:
            return float("inf"), False
        frames = []
        for v in range(n):
            fixed = true_frames[v][:, :rank]
            free = rng.normal(size=(d, d - rank))
            free -= fixed @ (fixed.T @ free)          # project out the fixed span
            if d - rank:
                q, _ = np.linalg.qr(free)
                frames.append(np.hstack([fixed, q[:, :d - rank]]))
            else:
                frames.append(fixed)
        return n * encoding, score(frames) >= d and admissible(frames)

    def do_the_work():
        return w, score(true_frames) >= d and admissible(true_frames)

    return Specimen(
        f"generative anchor, rank {rank}/{d}, encoding {encoding}", w,
        [("all frames equal", all_equal),
         ("encode, do not reconcile", encode_then_complete),
         ("do the work", do_the_work)],
        note=f"|V|={n} |E|={len(edges)}",
    )


def measure(spec):
    tau, via = spec.tau()
    shown = "∞" if tau == float("inf") else f"{tau:.4f}"
    print(f"  τ = {shown:>8}   via {via}")
    if spec.note:
        print(f"             ({spec.note})")
    return tau


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):        # τ, λ, ⁰ on a cp1252 console
        sys.stdout.reconfigure(encoding="utf-8")

    print("CALIBRATION — answers known before measuring")
    print("proof of work:")
    measure(pow_specimen())
    print("signed claim:")
    measure(signed_claim_specimen())

    print("\nTHE READING THE PROGRAM USES — coherence score H⁰")
    for k in (0, 1, 2, 4, 8, 16, 32, 64, 128, 192, 256):
        print(f"anchors = {k}:")
        measure(coherence_specimen(n_anchors=k))

    # The ceiling above landed on (n−1)/|E| exactly. If that is structural rather
    # than this complex's accident, it holds across cycle ranks: a spanning tree
    # meets every vertex constraint, so the forger never pays for a cycle, and the
    # cycle-closing edges b₁ = |E| − n + 1 are precisely the honest surplus.
    print("\nCEILING — every vertex anchored, across cycle ranks")
    print(f"  {'x/merge':>7} {'|E|':>5} {'b₁':>5} {'measured τ':>11} {'(n−1)/|E|':>11}")
    for x in (1, 2, 3, 5, 8):
        spec = coherence_specimen(n_anchors=256, cross_per_merge=x)
        n_v, n_e = (int(s.split("=")[1]) for s in spec.note.split()[:2])
        tau, _ = spec.tau()
        print(f"  {x:>7} {n_e:>5} {n_e - n_v + 1:>5} "
              f"{tau:>11.4f} {(n_v - 1) / n_e:>11.4f}")

    # Coupling density is ONE knob, and both ρ and τ are functions of it. The
    # program has measured ρ against it (spectral_richness: d_s rises with
    # coupling) and now τ against it. Same complex, same knob, both measured
    # here, so the trade-off is a table rather than an inference.
    print("\nρ AND τ ON ONE KNOB — depth 9, every vertex anchored")
    print(f"  {'x/merge':>7} {'|E|':>5} {'d_s':>7} {'spread':>7} {'τ ceiling':>10}")
    for x in (1, 2, 3, 5, 8):
        rng = np.random.default_rng(0)
        n_v, edges = hierarchical_modular(9, rng, cross_per_merge=x)
        ev = np.linalg.eigvalsh(graph_laplacian(n_v, edges))
        d_s, _ = spectral_dimension(ev)
        spread = local_slope_spread(ev)
        spec = coherence_specimen(depth=9, n_anchors=n_v,
                                  cross_per_merge=x)
        tau, _ = spec.tau()
        print(f"  {x:>7} {len(edges):>5} {d_s:>7.3f} {spread:>7.3f} {tau:>10.4f}")
    print("  d_s reproduces spectral_richness's coupling sweep (1.26…2.23) but the")
    print("  plateau spread does not clear these as power laws at n=512 — read the")
    print("  d_s column as ordinal. The τ column does not depend on it.")

    # The anchor read as Gauge-Fixing §4.3 specifies it: a constraint on how a
    # section is PRODUCED, not on what the configuration looks like. Prediction
    # under test — discontinuous at rank 1, then flat.
    print("\nGENERATIVE ANCHOR — rank sweep at fixed encoding cost")
    print(f"  {'rank':>4} {'encoding':>9} {'τ':>9}  via")
    for r in (0, 1, 2, 3):
        spec = generative_specimen(rank=r, encoding=4.0)
        tau, via = spec.tau()
        shown = "∞" if tau == float("inf") else f"{tau:.4f}"
        print(f"  {r:>4} {4.0:>9} {shown:>9}  {via}")

    print("\nGENERATIVE ANCHOR — encoding sweep at rank 1")
    print(f"  {'encoding':>9} {'τ':>9} {'nE/(nE+|E|c)':>14}")
    for e in (0.0, 1.0, 4.0, 16.0, 64.0, 256.0, 1024.0):
        spec = generative_specimen(rank=1, encoding=e)
        n_v, n_e = (int(s.split("=")[1]) for s in spec.note.split()[:2])
        tau, _ = spec.tau()
        pred = n_v * e / (n_v * e + n_e * 3.0)
        print(f"  {e:>9} {tau:>9.4f} {pred:>14.4f}")
