"""
Settling H1 — does any reward scheme actually resist duplication?

Every theorem in *The Multiplicity Freedom* is conditional on H1, and no concrete
mechanism in the program has been shown to satisfy it. Proof of Coherence §4.2
names two candidate resolutions to the copy-symmetry problem — Shapley credit
allocation and provenance-weighting — declares the fork "not resolvable from the
mechanism alone", and leaves it. It has sat since v0.1.1.

WHAT H1 ACTUALLY NEEDS. The Sybil paper states H1 as "a copy does not earn what
the original earns", which is a claim about INDIVIDUAL earnings. Theorem 4.1 does
not use that. It uses: expenditure on distinct identities is additive, i.e. an
adversary cannot pay once and earn many times. The precise property is about
GROUP TOTALS:

    (H1') For an adversary owning an original and N-1 duplicates of it, the SUM
          of the group's rewards does not exceed what the original earns alone.

H1' is what the counting argument needs and it is not the same statement. This
script tests H1', plus two adjacent properties a usable scheme also needs:

    GRIEF   can an attacker reduce an HONEST miner's reward by copying it?
    SPLIT   can an adversary gain by presenting one contribution as several?

Setting is §4.2's own toy: miners submit vectors, the coherence functional is the
rank of the stacked submission matrix.

Run:  python h1_duplication.py
"""
import itertools

import numpy as np

TOL = 1e-9


def rank(vectors):
    if not vectors:
        return 0
    return int(np.linalg.matrix_rank(np.array(vectors, dtype=float), tol=1e-8))


# ------------------------------------------------------------------ schemes

def marginal_removal(subs):
    """r(i) = v(all) - v(all without i). The v0.1 scheme."""
    full = rank(list(subs.values()))
    out = {}
    for i in subs:
        rest = [v for k, v in subs.items() if k != i]
        out[i] = full - rank(rest)
    return out


def shapley(subs):
    """Exact Shapley value over the rank game. Exponential; fine for toys."""
    keys = list(subs)
    n = len(keys)
    phi = {k: 0.0 for k in keys}
    fact = [np.math.factorial(i) if hasattr(np, "math") else None for i in range(n + 1)]
    import math
    fact = [math.factorial(i) for i in range(n + 1)]
    for i in keys:
        others = [k for k in keys if k != i]
        for r in range(len(others) + 1):
            w = fact[r] * fact[n - r - 1] / fact[n]
            for S in itertools.combinations(others, r):
                base = rank([subs[k] for k in S])
                with_i = rank([subs[k] for k in S] + [subs[i]])
                phi[i] += w * (with_i - base)
    return phi


def _first_flags(subs, order):
    seen, p = {}, {}
    for i in sorted(subs, key=lambda k: order[k]):
        sig = tuple(np.round(subs[i], 8))
        p[i] = 0.0 if sig in seen else 1.0
        seen.setdefault(sig, i)
    return p


def provenance_literal(subs, order):
    """
    §4.2 EXACTLY AS WRITTEN: r_prov(i) = r(i) * p(i), with r the marginal-removal
    reward computed on the FULL submission set.

    §4.2 claims this "resolves copy-symmetry asymmetrically (in M1's favour over
    M3's)". It does not. Marginal removal has already driven r(M1) to zero
    BECAUSE the copy is present, so multiplying by p = 1 rescues nothing:
    0 x 1 = 0. The provenance factor can only redistribute a reward that still
    exists, and by the time it is applied there is none.
    """
    base = marginal_removal(subs)
    p = _first_flags(subs, order)
    return {i: base[i] * p[i] for i in subs}


def provenance(subs, order):
    """
    The repaired form: exclude later copies from the coherence functional
    ENTIRELY, then score the surviving set. Provenance filters the input rather
    than scaling the output.
    """
    base = marginal_removal(subs)
    seen = {}
    p = {}
    for i in sorted(subs, key=lambda k: order[k]):
        sig = tuple(np.round(subs[i], 8))
        p[i] = 0.0 if sig in seen else 1.0
        seen.setdefault(sig, i)
    # a first-submitter's reward is computed as if its later copies were absent
    out = {}
    for i in subs:
        if p[i] == 0.0:
            out[i] = 0.0
        else:
            kept = {k: v for k, v in subs.items() if p.get(k, 1.0) == 1.0}
            out[i] = (rank(list(kept.values()))
                      - rank([v for k, v in kept.items() if k != i]))
    return out


SCHEMES = {"marginal": lambda s, o: marginal_removal(s),
           "shapley": lambda s, o: shapley(s),
           "prov-literal": provenance_literal,
           "prov-filtered": provenance}


# ------------------------------------------------------------------ tests

def test_h1(n_copies):
    """Adversary owns M1 plus n_copies-1 verbatim duplicates. M2 is honest."""
    solo = {"M1": [5, 7], "M2": [5.1, 6.9]}
    subs = {"M2": [5.1, 6.9]}
    adv = []
    for c in range(n_copies):
        k = f"A{c}"
        subs[k] = [5, 7]
        adv.append(k)
    order = {k: i for i, k in enumerate(["M1", "M2"])}
    order_dup = {"M2": 0, **{k: i + 1 for i, k in enumerate(adv)}}
    rows = {}
    for name, fn in SCHEMES.items():
        base = fn(solo, order)["M1"]
        got = sum(fn(subs, order_dup)[k] for k in adv)
        rows[name] = (base, got)
    return rows


def test_grief():
    """Honest M1 submits first; attacker copies it. Does M1 lose reward?"""
    honest = {"M1": [5, 7], "M2": [5.1, 6.9]}
    copied = {"M1": [5, 7], "M2": [5.1, 6.9], "X": [5, 7]}
    o1 = {"M1": 0, "M2": 1}
    o2 = {"M1": 0, "M2": 1, "X": 2}
    rows = {}
    for name, fn in SCHEMES.items():
        rows[name] = (fn(honest, o1)["M1"], fn(copied, o2)["M1"])
    return rows


def test_split():
    """
    Adversary has ONE genuinely independent direction. Does presenting it as two
    identities that jointly span the same space pay more than presenting it once?
    """
    one = {"H": [1, 0, 0], "A": [0, 1, 0]}
    two = {"H": [1, 0, 0], "A1": [0, 0.6, 0], "A2": [0, 0.4, 0]}
    o1 = {"H": 0, "A": 1}
    o2 = {"H": 0, "A1": 1, "A2": 2}
    rows = {}
    for name, fn in SCHEMES.items():
        rows[name] = (fn(one, o1)["A"], fn(two, o2)["A1"] + fn(two, o2)["A2"])
    return rows


if __name__ == "__main__":
    print("=" * 74)
    print("H1'  — adversary's GROUP TOTAL under N-way duplication")
    print("      pass = total never exceeds what the original earns alone")
    print("=" * 74)
    print(f"  {'scheme':<12}{'solo':>8}" + "".join(f"{'N=' + str(n):>10}" for n in (1, 2, 3, 4, 5)))
    verdict = {}
    for name in SCHEMES:
        cells, solo, ok = "", None, True
        for n in (1, 2, 3, 4, 5):
            base, got = test_h1(n)[name]
            solo = base
            cells += f"{got:>10.3f}"
            if got > base + 1e-6:
                ok = False
        verdict[name] = ok
        print(f"  {name:<12}{solo:>8.3f}{cells}   {'PASS' if ok else 'FAIL'}")

    print("\n" + "=" * 74)
    print("GRIEF — can an attacker cut an HONEST miner's reward by copying it?")
    print("=" * 74)
    print(f"  {'scheme':<12}{'M1 alone':>10}{'M1 copied':>12}   effect")
    for name, (a, b) in test_grief().items():
        eff = "unharmed" if abs(a - b) < 1e-6 else f"loses {100*(a-b)/max(a,1e-9):.0f}%"
        print(f"  {name:<12}{a:>10.3f}{b:>12.3f}   {eff}")

    print("\n" + "=" * 74)
    print("SPLIT — does presenting one direction as two identities pay?")
    print("=" * 74)
    print(f"  {'scheme':<12}{'as one':>10}{'as two':>10}   effect")
    for name, (a, b) in test_split().items():
        eff = "neutral" if abs(a - b) < 1e-6 else (
            "SPLITTING PAYS" if b > a else "splitting punished")
        print(f"  {name:<12}{a:>10.3f}{b:>10.3f}   {eff}")

    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    for name in SCHEMES:
        print(f"  {name:<12} H1' {'satisfied' if verdict[name] else 'VIOLATED'}")
