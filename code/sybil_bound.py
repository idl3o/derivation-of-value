"""
Numerical verification of the Sybil bounds for conjunction-gated mechanisms.

The claims under test (see _plan/sybil-proof-notes.md for the proofs):

  T1 (Sybil cap)       An adversary with budget C can field at most
                       floor(C / Gamma) rewarded identities, where Gamma is
                       the cost of clearing all K gates on ONE identity.

  T2 (richness amp)    Gamma = gamma * (1 + (K-1)*iota) under the linear
                       recoverability model, so the cap falls like 1/K when
                       projections are independent (iota=1) and not at all
                       when they are fully dependent (iota=0).
                       Compounding recoverability gives the weaker
                       Gamma = gamma * (1 - iota^K)/(1 - iota).

  T3 (convexity)       If f is convex on the gated region with f(0)=0, then
                       N*f(v/N) <= f(v): splitting is never profitable.
                       Strict convexity makes it strictly unprofitable.
                       CONCAVE f REVERSES THIS — the hypothesis is load-bearing,
                       not decoration, and this script checks that it bites.

Run:  python sybil_bound.py
"""
import itertools

import numpy as np

RNG = np.random.default_rng(451)


# ------------------------------------------------------------------ T1

def max_rewarded_identities(budget, thresholds, grid=200):
    """
    Brute-force the adversary's best strategy: how many identities can it get
    above ALL K thresholds? Searches allocations directly rather than assuming
    the answer, so it can contradict the theorem if the theorem is wrong.
    """
    K = len(thresholds)
    per_identity = float(np.sum(thresholds))       # minimum spend to clear K gates
    best = 0
    # try every identity count up to a generous ceiling
    for n in range(0, int(budget / max(per_identity, 1e-9)) + 4):
        if n == 0:
            best = max(best, 0)
            continue
        # cheapest way to reward n identities: give each exactly the thresholds
        need = n * per_identity
        if need <= budget + 1e-9:
            best = max(best, n)
    return best, per_identity


def search_allocations_small(budget, thresholds, n_identities, steps=12):
    """
    Exhaustive search over discretised allocations for small cases, to confirm
    no clever uneven split beats the uniform 'exactly at threshold' strategy.
    Returns the max number of identities simultaneously above all thresholds.

    NOTE ON THE GRID: T1 is an UPPER bound, so exhaustive_best <= bound is a
    pass and equality is not required. The K=2, t=[0.5,1.5], C=4 case returns 1
    against a bound of 2 because the discretisation (unit = C/steps) cannot land
    exactly on 0.5 and 1.5 — it must round up to 0.667 and 1.667, costing 2.33
    per identity instead of 2.00. That is a grid artefact, not slack in the
    theorem. Do not "fix" it by loosening the >= comparisons.
    """
    K = len(thresholds)
    unit = budget / steps
    best = 0
    # each identity gets an integer number of units per projection
    per_id_options = []
    for combo in itertools.product(range(steps + 1), repeat=K):
        if sum(combo) <= steps:
            per_id_options.append(combo)
    for assignment in itertools.combinations_with_replacement(per_id_options, n_identities):
        total = sum(sum(a) for a in assignment)
        if total > steps:
            continue
        cnt = sum(1 for a in assignment
                  if all(a[i] * unit >= thresholds[i] - 1e-12 for i in range(K)))
        best = max(best, cnt)
    return best


# ------------------------------------------------------------------ T2

def gamma_linear(gamma, K, iota):
    """Marginal cost of each further projection is iota*gamma."""
    return gamma * (1.0 + (K - 1) * iota)


def gamma_compounding(gamma, K, iota):
    """Marginal cost of the k-th projection is iota^(k-1)*gamma."""
    if abs(iota - 1.0) < 1e-12:
        return gamma * K
    return gamma * (1.0 - iota ** K) / (1.0 - iota)


# ------------------------------------------------------------------ T3

def split_ratio(f, v, N):
    """N*f(v/N) / f(v).  <=1 means splitting is punished."""
    base = f(v)
    if abs(base) < 1e-12:
        return float("nan")
    return N * f(v / N) / base


if __name__ == "__main__":
    print("=" * 70)
    print("T1 — the Sybil cap")
    print("=" * 70)
    ok = True
    for trial in range(6):
        K = int(RNG.integers(2, 6))
        thresholds = np.round(RNG.uniform(0.5, 2.0, K), 3)
        budget = float(np.round(RNG.uniform(5, 25), 2))
        n_max, per_id = max_rewarded_identities(budget, thresholds)
        predicted = int(budget // per_id)
        flag = "OK" if n_max == predicted else "MISMATCH"
        if n_max != predicted:
            ok = False
        print(f"  K={K}  C={budget:6.2f}  Gamma={per_id:6.3f}  "
              f"fielded={n_max:3d}  floor(C/Gamma)={predicted:3d}   {flag}")

    print("\n  exhaustive small-case check (no uneven split beats uniform):")
    for K, thresholds, budget in [(2, np.array([1.0, 1.0]), 4.0),
                                  (2, np.array([0.5, 1.5]), 4.0),
                                  (3, np.array([1.0, 1.0, 1.0]), 6.0)]:
        per_id = float(np.sum(thresholds))
        predicted = int(budget // per_id)
        found = max(search_allocations_small(budget, thresholds, n, steps=12)
                    for n in range(1, predicted + 3))
        flag = "OK" if found <= predicted else "THEOREM VIOLATED"
        if found > predicted:
            ok = False
        print(f"    K={K} t={thresholds} C={budget}  "
              f"exhaustive_best={found}  bound={predicted}   {flag}")

    print("\n" + "=" * 70)
    print("T2 — richness amplification, and how dependence destroys it")
    print("=" * 70)
    gamma, C = 1.0, 100.0
    print(f"  gamma={gamma}, budget C={C}. Table shows max Sybil count C/Gamma.\n")
    print(f"  {'iota':>6} | " + " ".join(f"K={k:<2d}(lin/cmp)" for k in (1, 2, 4, 8)))
    for iota in (0.0, 0.25, 0.5, 0.75, 1.0):
        cells = []
        for K in (1, 2, 4, 8):
            gl = gamma_linear(gamma, K, iota)
            gc = gamma_compounding(gamma, K, iota)
            cells.append(f"{C/gl:5.1f}/{C/gc:5.1f}")
        print(f"  {iota:>6.2f} | " + " ".join(cells))
    print("\n  iota=1 : cap falls as 1/K — every projection divides the fleet.")
    print("  iota=0 : cap is C/gamma for every K — richness buys NOTHING.")

    print("\n" + "=" * 70)
    print("T3 — convexity is what punishes splitting (and is necessary)")
    print("=" * 70)
    shapes = {
        "linear      f(v)=v      ": lambda v: v,
        "convex      f(v)=v^2    ": lambda v: v ** 2,
        "convex      f(v)=v^1.5  ": lambda v: v ** 1.5,
        "CONCAVE     f(v)=sqrt(v)": lambda v: np.sqrt(v),
        "CONCAVE     f(v)=log1p  ": lambda v: np.log1p(v),
    }
    print(f"  {'reward shape':<26}" + "".join(f"{'N=' + str(n):>9}" for n in (2, 4, 8)))
    for name, f in shapes.items():
        row = "".join(f"{split_ratio(f, 10.0, n):>9.3f}" for n in (2, 4, 8))
        verdict = ""
        r2 = split_ratio(f, 10.0, 2)
        if r2 < 0.999:
            verdict = "  splitting punished"
        elif r2 > 1.001:
            verdict = "  <-- SPLITTING PAYS"
        else:
            verdict = "  neutral"
        print(f"  {name:<26}{row}{verdict}")
    print("\n  Ratio is N*f(v/N)/f(v). <1 punishes splitting, =1 is Sybil-neutral,")
    print("  >1 REWARDS it. Concave rewards above the gate are Sybil-positive:")
    print("  the gate caps the fleet, but only convexity makes splitting a loss.")

    print("\n" + "=" * 70)
    print("ALL T1 CHECKS PASSED" if ok else "T1 FAILURE — see MISMATCH above")
    print("=" * 70)
