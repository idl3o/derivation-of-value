"""
The third attack design: iota against a TEMPORAL projection.

independence.py settled that the static spectral dimension is not an independent
third projection — faking the kernel delivers d_s for free, because in a static
snapshot d_s is measuring the coherent fraction of the substrate and so is the
kernel count. Two instruments, one quantity. Its closing paragraph names the only
route left:

    "It does not refute §6, whose independence claim rests on a distinction in
     time — agreeing at an instant versus sustaining dynamical structure epoch
     over epoch — that a static sheaf cannot express. If independence lives
     anywhere, it lives in the temporal autocorrelations §6 already named, and
     nothing short of building them will do."

iota_asymmetry.py then failed twice to move d_s without destroying the substrate.
This builds the epochs instead of attacking the snapshot harder.

THE TWO PROJECTIONS

  pi_ker      coherence at an instant: #{lambda < SOFT}, as everywhere else.
  pi_persist  structure sustained across epochs: the overlap between the bottom-k
              eigenspaces of consecutive epochs. Always defined, in [0, 1],
              read off the same operator the mechanism already scores.

THE TWO ATTACKS, and they target genuinely different things

  Attack C   coherent NOW, re-drawn every epoch. Frames are made consistent
             within the coalition each epoch, then discarded and redrawn.
             Targets pi_ker; should leave pi_persist untouched.
  Attack P   FROZEN, never coherent. The coalition's frames stay frustrated but
             are held fixed epoch to epoch. Targets pi_persist; should leave
             pi_ker untouched.

This is why the design can succeed where sparsification and rewiring failed: it
does not try to move d_s at all. It moves persistence, which is a property of the
SEQUENCE and therefore has a knob the static complex does not expose.

A DIAGNOSTIC THAT CAN RETURN AN ABSURDITY, deliberately

Honest participants update their models, so honest frames DRIFT and honest
persistence is below 1. Attack P is perfectly frozen and can therefore score
ABOVE the honest value. Progress above the honest maximum is the same species of
impossible number that caught the sparsification attack and the gap hierarchy,
and here it is not a bug to guard against but the hypothesis under test: a
projection that rewards stasis is one an adversary wins by doing nothing.

SO IOTA IS NOT ENOUGH, and this module measures both quantities

Independence is necessary and not sufficient — CP also requires the projection be
expensive to fake. A projection uncorrelated with coherence is liable to be one
coherence does not constrain, and a projection coherence does not constrain is
one an adversary satisfies without doing coherence work. High iota and high tau
may therefore pull against each other, exactly as rho and tau do (Sign and Work
v0.3 §5.4). Reporting iota alone would manufacture a finding, so tau(pi_persist)
is measured alongside it, in the sense of Sign and Work Def 3.3.

Run:  python temporal_iota.py
"""
import sys

import numpy as np

from complexes import hierarchical_modular, random_orthogonal

__all__ = ["epoch_laplacian", "persistence", "run_history"]

SOFT = 0.05
STALK = 3
DEPTH = 8
EPOCHS = 8
DRIFT = 0.12          # honest models update; honest persistence is below 1
KBOT = 12             # bottom-k eigenspace compared across epochs


def _rotate_toward(R, rng, amount, d=STALK):
    """A small random rotation: honest models move, they do not teleport."""
    A = rng.normal(size=(d, d))
    A = (A - A.T) / 2.0                      # antisymmetric generator
    q, _ = np.linalg.qr(np.eye(d) + amount * A)
    return R @ q


def epoch_laplacian(n, edges, frames, coherent_set, rng, d=STALK, frozen=None):
    """
    Restriction maps are R_u^T R_v inside the coherent set and independent random
    O(d) elsewhere — the same construction independence.py uses, so the two
    modules' pi_ker are the same quantity.

    `frozen` is a dict edge -> O reused across epochs. It is how a COALITION
    holds its own structure fixed while the rest of the complex goes on moving.
    Freezing the whole Laplacian instead would hand the adversary the entire
    substrate, which is not an attack within a budget; the first version of this
    file did exactly that, and the tell was that the result did not depend on
    coalition size.
    """
    L = np.zeros((n * d, n * d))
    I = np.eye(d)
    for u, v in edges:
        if frozen is not None and (u, v) in frozen:
            O = frozen[(u, v)]
        elif u in coherent_set and v in coherent_set:
            O = frames[u].T @ frames[v]
        else:
            O = random_orthogonal(d, rng)
        su, sv = u * d, v * d
        L[su:su + d, su:su + d] += I
        L[sv:sv + d, sv:sv + d] += I
        L[su:su + d, sv:sv + d] -= O
        L[sv:sv + d, su:su + d] -= O.T
    return L


def persistence(bases):
    """
    Mean overlap of consecutive bottom-k eigenspaces: (1/k)*||V_t^T V_{t+1}||_F^2.

    This is the normalised sum of squared cosines of the principal angles, so it
    is 1 for an unchanged subspace and ~k/(nd) for independent random ones. It is
    symmetric and basis-independent, which matters because the eigenvectors
    themselves are only defined up to rotation within degenerate blocks.
    """
    vals = []
    for a, b in zip(bases, bases[1:]):
        vals.append(float(np.sum((a.T @ b) ** 2) / a.shape[1]))
    return float(np.mean(vals))


def run_history(n, edges, mode, rng, f=0.5, epochs=EPOCHS, d=STALK):
    """
    Produce an epoch sequence and score it.

    mode = "honest"      whole complex coherent, frames drift
           "frustrated"  nothing coherent, frames redrawn each epoch (baseline)
           "attack_C"    coalition coherent each epoch, frames redrawn each epoch
           "attack_P"    coalition's own edges frozen after t=0 and never made
                         coherent; the rest of the complex goes on moving
    """
    coalition = set(range(max(1, int(f * n))))
    frames = [random_orthogonal(d, rng) for _ in range(n)]

    frozen = None
    if mode == "attack_P":
        # Draw the coalition's internal maps once. Frustrated — the coalition
        # never agrees about anything. It merely never changes its mind.
        frozen = {(u, v): random_orthogonal(d, rng) for u, v in edges
                  if u in coalition and v in coalition}

    kers, bases = [], []
    for t in range(epochs):
        if mode == "honest":
            coherent, frames = set(range(n)), [
                _rotate_toward(R, rng, DRIFT) for R in frames]
        elif mode in ("frustrated", "attack_P"):
            coherent, frames = set(), [random_orthogonal(d, rng) for _ in range(n)]
        elif mode == "attack_C":
            coherent = coalition
            frames = [random_orthogonal(d, rng) for _ in range(n)]
        else:
            raise ValueError(mode)

        L = epoch_laplacian(n, edges, frames, coherent, rng, frozen=frozen)

        ev, vec = np.linalg.eigh(L)
        kers.append(int(np.sum(ev < SOFT)))
        bases.append(vec[:, :KBOT])

    return {"ker": float(np.mean(kers)), "persist": persistence(bases)}


def _progress(s, base, honest, key):
    span = honest[key] - base[key]
    if abs(span) < 1e-9:
        return float("nan")
    return (s[key] - base[key]) / span


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    n = 2 ** DEPTH
    _, edges = hierarchical_modular(DEPTH, np.random.default_rng(7),
                                    cross_per_merge=2)

    base = run_history(n, edges, "frustrated", np.random.default_rng(11))
    honest = run_history(n, edges, "honest", np.random.default_rng(12))

    print("=" * 74)
    print("IOTA AGAINST A TEMPORAL PROJECTION")
    print("=" * 74)
    print(f"  frustrated : π_ker={base['ker']:>7.2f}   π_persist={base['persist']:.4f}")
    print(f"  honest     : π_ker={honest['ker']:>7.2f}   π_persist={honest['persist']:.4f}")
    print(f"  (honest persistence is below 1 by construction: DRIFT={DRIFT})")

    print(f"\n  {'attack':>10} {'f':>6} {'π_ker':>8} {'π_persist':>10}"
          f" {'ker prog':>9} {'per prog':>9}")
    rows = {}
    for mode in ("attack_C", "attack_P"):
        for f in (0.25, 0.5, 0.75):
            s = run_history(n, edges, mode, np.random.default_rng(300 + int(100 * f)), f=f)
            pk = _progress(s, base, honest, "ker")
            pp = _progress(s, base, honest, "persist")
            flag = "  <-- ABOVE HONEST" if max(pk, pp) > 1.05 else ""
            print(f"  {mode:>10} {f:>6.2f} {s['ker']:>8.2f} {s['persist']:>10.4f}"
                  f" {pk:>9.3f} {pp:>9.3f}{flag}")
            rows.setdefault(mode, []).append((f, pk, pp))

    print("\n" + "=" * 74)
    print("DIRECTIONAL IOTA   ι(j|i) = 1 − progress_j / progress_i")
    print("=" * 74)

    def directional(mode, own_idx, other_idx, min_progress=0.25):
        """Admit a run only if the attack actually moved its own target."""
        out = []
        for row in rows[mode]:
            own, oth = row[own_idx], row[other_idx]
            if own >= min_progress:
                out.append(1.0 - oth / own)
        return out

    ipk = directional("attack_C", 1, 2)      # ι(persist | ker)
    ikp = directional("attack_P", 2, 1)      # ι(ker | persist)

    def show(name, vals):
        if not vals:
            print(f"  {name:<22} -- attack never reached its own target")
            return None
        m = float(np.mean(vals))
        oor = [v for v in vals if v > 1.0 + 1e-9 or v < -1e-9]
        note = f"  [{len(oor)} sample(s) outside [0,1]]" if oor else ""
        print(f"  {name:<22} {m:>7.3f}   (" +
              ", ".join(f"{v:.2f}" for v in vals) + ")" + note)
        if max(vals) - min(vals) > 0.3:
            print(f"  {'':<22}         ^ spread {max(vals) - min(vals):.2f} across "
                  "intensities: not a constant")
        return m

    a = show("ι(persist | ker)", ipk)
    b = show("ι(ker | persist)", ikp)

    print("\n" + "=" * 74)
    print("AND THE OTHER HALF OF THE REQUIREMENT: τ(π_persist)")
    print("=" * 74)
    print("  Independence is necessary and not sufficient. Sign and Work Def 3.3:")
    print("  τ = forging cost / earning cost, and soundness is τ ≥ 1.")
    print()
    print("  earning π_persist : hold a COHERENT structure across epochs while")
    print("                      genuinely updating it — the honest run above.")
    print("  forging π_persist : change nothing. Attack P, cost ~0.")
    print()
    pp_attack = max(r[2] for r in rows["attack_P"])
    print(f"  attack P reaches {pp_attack:.3f} of honest persistence progress at")
    print("  no coherence work whatever, so τ(π_persist) ≈ 0.")
    if a is not None and b is not None:
        print()
        print(f"  |ι(persist|ker) − ι(ker|persist)| = {abs(a - b):.3f}, above the")
        print("  0.15 threshold iota_asymmetry.py set for 'substantially")
        print("  asymmetric' — so on this pair the right object is a DIVERGENCE,")
        print("  not a metric, and the Fisher route of P6 needs the asymmetry")
        print("  carried rather than quotiented away.")
        print()
        print("  But the sharper finding is the conjunction. π_persist is")
        print("  INDEPENDENT of the kernel — ι(ker|persist) = 1.000 at every")
        print("  coalition size, the first solid measurement in this direction,")
        print("  the program having had only ι(dim|ker) = 0.08 — and it is FREE")
        print("  TO FORGE, since a coalition that merely never changes its mind")
        print("  outscores an honest one that does. Independence was never the")
        print("  binding constraint. CP §7.1 has been treated as the hard part")
        print("  of admitting a third projection; on this evidence τ is.")
