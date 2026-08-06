"""
Does usage couple, when the users are inside the fiction?

The service reframe — the mechanism DELIVERS tuned-coherent messaging rather
than PAYING for coherence — appears to solve the problem A Consistent Fiction
priced and Gauge-Fixing forbade its anchors from solving. Closure costs d
scalars of contact with the world, the anchors may not supply them (they fix
provenance, not content), and under a service framing usage looks like contact
the mechanism never had to anchor for: recipients who stop consuming are
external signal.

The objection this module exists to test: **a filter bubble is a closed system
whose own metrics adore it.** Usage couples only if the consumers are outside
the fiction, and in a bubble they are not. If a bubble is at least as satisfying
to its own consumers as an honest network is to its, then usage is not coupling
and the reframe's main advantage is illusory.

THE SETUP

  world w        a unit vector in R^d, drifting slowly. What is actually so.
  participants   each holds a model, a unit vector. Anchored participants
                 re-derive theirs from the world every epoch; unanchored ones
                 update toward whatever the service delivered to them, which is
                 autopoiesis stated operationally — the consumer's criterion is
                 produced by the thing it judges.
  service        delivers to each recipient the mean model of a SCOPE of
                 participants, renormalised. Honest draws its scope from the
                 whole network; the bubble draws only from its own coalition.

  satisfaction   cos(delivered_r, model_r) — did the service tell me something
                 I recognise. This is what a usage signal actually measures.
  truth          cos(model_r, world) — the thing satisfaction is a proxy for.

THE TEST — and the first version of it was the wrong instrument

The question was first posed as discrimination = satisfaction(honest) −
satisfaction(bubble): can a usage signal tell an honest network from a bubble?
Its calibration failed and the failure is kept, because the failure is
informative. At anchored = 1.0 discrimination came out at +0.0007 where it was
required to be clearly positive — correctly, because when every participant
re-derives from the world the "bubble" is a coalition of truth-trackers and its
consensus IS the world. **There is no fiction there to detect.** Comparing two
networks at equal anchoring compares nothing; the anchoring was doing all the
work in both.

The right instrument is inside a single network: **does satisfaction track
truth?** Sweep the anchored fraction and watch both. If a network can reach
satisfaction a well-anchored one cannot, usage is not a proxy for contact with
the world — it is a proxy for the absence of it.

The knob is `anchored`, the fraction of the population re-deriving from the
world: the analogue of A Consistent Fiction's "d scalars at one vertex", asked
of the consumer side rather than the producer side.

SCOPE IS THE SCALE DIAL. A message coherent across the whole network is the
world-sim limit; a message coherent across two participants is the bitchat
limit. Volume IV's coda claims the operator recurs at every scale and never
formalises it. If discrimination behaves the same way at scope 2 and scope n,
that claim has its first evidence; if it does not, the recurrence is decoration.

CALIBRATION for the instrument actually used. At anchored = 0.0 nothing is in
contact with anything, so truth must be near zero or negative and satisfaction
must be near 1 — a network that only listens to itself agrees with itself
perfectly. At anchored = 1.0 truth must be high. A run failing either is
measuring its own construction.

Run:  python usage_coupling.py
"""
import sys

import numpy as np

__all__ = ["run", "discrimination"]

DIM = 8
N = 240
EPOCHS = 40
WORLD_DRIFT = 0.05
INERTIA = 0.7          # how fast an unanchored model follows what it is served
NOISE = 0.15


def _unit(v):
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    return v / np.maximum(n, 1e-12)


def run(mode, anchored, scope, rng, n=N, d=DIM, epochs=EPOCHS):
    """
    mode = "honest"  service draws its scope from the whole network
           "bubble"  a coalition serves only itself, from itself

    Returns mean satisfaction and mean truth over the second half of the run,
    after the population has settled into whatever attractor it has.
    """
    world = _unit(rng.normal(size=d))
    models = _unit(rng.normal(size=(n, d)))

    n_anchor = int(round(anchored * n))
    is_anchored = np.zeros(n, dtype=bool)
    is_anchored[rng.permutation(n)[:n_anchor]] = True

    # The bubble is a coalition that both produces and consumes its own service.
    coalition = np.zeros(n, dtype=bool)
    coalition[:n // 2] = True

    sat_hist, truth_hist = [], []
    for t in range(epochs):
        world = _unit(world + WORLD_DRIFT * rng.normal(size=d))

        # anchored participants re-derive from the world; this is the only
        # contact with anything outside the network anywhere in the model
        idx = np.where(is_anchored)[0]
        models[idx] = _unit(world + NOISE * rng.normal(size=(len(idx), d)))

        # the service: mean model over a scope, per recipient
        delivered = np.empty_like(models)
        for r in range(n):
            if mode == "bubble" and coalition[r]:
                pool = np.where(coalition)[0]      # serves itself, from itself
            else:
                pool = np.arange(n)
            pick = pool if scope >= len(pool) else rng.choice(pool, scope, replace=False)
            delivered[r] = _unit(models[pick].mean(axis=0))

        sat = np.sum(delivered * models, axis=1)
        truth = np.sum(models * world, axis=1)
        if t >= epochs // 2:
            # the bubble is judged on its own consumers, the honest network on
            # everyone: each is scored by the population it actually serves
            who = coalition if mode == "bubble" else np.ones(n, dtype=bool)
            sat_hist.append(float(sat[who].mean()))
            truth_hist.append(float(truth[who].mean()))

        # unanchored participants drift toward what they were served
        free = ~is_anchored
        models[free] = _unit(INERTIA * delivered[free] + (1 - INERTIA) * models[free])

    return {"sat": float(np.mean(sat_hist)), "truth": float(np.mean(truth_hist))}


def discrimination(anchored, scope, seed=0):
    h = run("honest", anchored, scope, np.random.default_rng(seed))
    b = run("bubble", anchored, scope, np.random.default_rng(seed + 1))
    return h, b, h["sat"] - b["sat"]


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 76)
    print("DOES USAGE COUPLE?   satisfaction against truth, as contact is added")
    print("=" * 76)

    print("\nCALIBRATION")
    z = run("honest", 0.0, N, np.random.default_rng(0))
    o = run("honest", 1.0, N, np.random.default_rng(0))
    print(f"  anchored=0.00  sat={z['sat']:.4f}  truth={z['truth']:+.4f}"
          "   [sat must be ≈1, truth ≈0 or below]")
    print(f"  anchored=1.00  sat={o['sat']:.4f}  truth={o['truth']:+.4f}"
          "   [truth must be high]")

    print(f"\nSWEEP — full scope")
    print(f"  {'anchored':>9} {'satisfaction':>13} {'truth':>9}")
    for a in (0.0, 0.01, 0.02, 0.05, 0.10, 0.20, 0.40, 0.70, 1.00):
        s = run("honest", a, N, np.random.default_rng(0))
        print(f"  {a:>9.2f} {s['sat']:>13.4f} {s['truth']:>+9.4f}")

    print("\n  Satisfaction is MAXIMISED at zero contact and falls monotonically")
    print("  as contact is added. Truth saturates early. A mechanism scored on")
    print("  user satisfaction is optimised by having no contact with the world.")

    print("\nIS THERE A BARRIER? — five seeds, fine sweep through the dip")
    print("  If satisfaction falls before it recovers, closure is a LOCAL optimum")
    print("  and a mechanism hill-climbing on user satisfaction rolls back into it.")
    print(f"  {'anchored':>9} {'sat mean':>9} {'sat sd':>8} {'truth mean':>11}")
    grid = (0.0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15)
    curve = []
    for a in grid:
        rs = [run("honest", a, N, np.random.default_rng(s)) for s in range(5)]
        sm = float(np.mean([r["sat"] for r in rs]))
        ss = float(np.std([r["sat"] for r in rs]))
        tm = float(np.mean([r["truth"] for r in rs]))
        curve.append((a, sm, ss, tm))
        print(f"  {a:>9.2f} {sm:>9.4f} {ss:>8.4f} {tm:>+11.4f}")
    # A barrier is a local minimum FOLLOWED BY A RECOVERY. Taking the global
    # min and max of the tail instead finds the monotone decline and reports it
    # as a valley -- which the first version of this check did, and which would
    # have manufactured the more interesting of the two possible answers.
    noise = max(r[2] for r in curve)
    lo_i = min(range(1, len(curve)), key=lambda i: curve[i][1])
    recovery = max((curve[j][1] for j in range(lo_i + 1, len(curve))), default=None)
    print(f"\n  closure sat = {curve[0][1]:.4f} at a=0")
    print(f"  interior minimum {curve[lo_i][1]:.4f} at a={curve[lo_i][0]:.2f}")
    if recovery is None:
        print("  no points beyond the minimum: monotone decline, no barrier.")
    else:
        rise = recovery - curve[lo_i][1]
        print(f"  best recovery after it {recovery:.4f}, a rise of {rise:.4f}")
        print(f"  seed spread ~{noise:.4f}, so 3σ = {3 * noise:.4f}")
        print("  " + ("BARRIER: closure is a LOCAL optimum, separated by a valley."
                      if rise > 3 * noise else
                      "NO BARRIER above noise. Satisfaction simply DECLINES with"))
        if rise <= 3 * noise:
            print("  contact, so the gradient points at closure from everywhere —")
            print("  which needs no barrier to be a trap.")

    print("\n  Note on the a=0 truth figures: with nothing anchored the network")
    print("  settles on an attractor uncorrelated with a drifting world, so those")
    print("  values are noise about zero and are NOT evidence of anti-correlation.")
    print("  The finding is that truth is absent there, not that it is inverted.")

    print(f"\nSCALE — the same sweep at every scope")
    print("  scope n = the world-sim limit; scope 2 = the bitchat limit.")
    print(f"  {'scope':>7} {'a=0 sat':>9} {'a=0 truth':>10}"
          f" {'a=.1 truth':>11} {'a=1 sat':>9} {'sat cost':>9}")
    for scope in (2, 4, 16, 64, N):
        z = run("honest", 0.0, scope, np.random.default_rng(0))
        m = run("honest", 0.10, scope, np.random.default_rng(0))
        o = run("honest", 1.0, scope, np.random.default_rng(0))
        print(f"  {scope:>7} {z['sat']:>9.4f} {z['truth']:>+10.4f}"
              f" {m['truth']:>+11.4f} {o['sat']:>9.4f} {z['sat'] - o['sat']:>+9.4f}")
    print("\n  'sat cost' is what full contact with the world costs in user")
    print("  satisfaction. If it is the same sign and rough size at scope 2 and")
    print("  scope n, the operator recurs across scale (Vol IV coda, P7).")
