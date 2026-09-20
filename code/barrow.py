"""
The barrow: what a marketplace of meme artefacts can read, graded by trace gap.

Sign and Work Def 3.3: τ(π) = f(π)/w(π), the cheapest accepted forgery over the
honest cost of the thing the reading is meant to evidence. §8.2 of that paper
closed on a sentence this module is pointed at: "Proof of work sits at exactly 1
and the program has no specimen above it."

A marketplace of inscribed artefacts on a proof-of-work chain exposes three
kinds of reading, and the instrument grades each against a written-down
attacker class:

  MARKET readings  — volume, holder count, floor price. What every venue ranks
                     by. Forger: one owner on both sides of the trade.
  FEE readings     — what the artefact paid for its blockspace. Two variants:
                     the DECLARED fee, and the blockspace valued at the block's
                     CLEARING feerate. Forger: a miner paying the fee to itself.
                     A BURN is the third variant and the control.
  DEPTH            — the work piled on the artefact since it was buried: the
                     mound. Evidences priority. Honest cost: the fee, and
                     waiting. Forgers: (a) the RACE, rewrite the chain from d
                     blocks back in public, with hash share q and any give-up
                     rule g; (b) the ECLIPSE, mine d blocks at full difficulty
                     in private and show them to one isolated reader.

THE COST MODEL FOR THE RACE, declared because everything in part six rests on
it. Free entry: a block's work costs its reward R. A forger hashes either way,
so the cost of attacking RELATIVE TO MINING HONESTLY is the revenue of the
blocks it orphans: on success its blocks are canonical and pay R each (net
zero); on failure they pay nothing. Hence

    f_race / R = E[m_a · 1{fail}] / P(win),   minimised over the give-up rule,

with the deficit a gambler's ruin absorbed at 0 and at the give-up line. A
public rewrite must carry strictly MORE work than the chain it replaces, so
forging depth d is a ruin problem started from d + 1 and abandoned at
d + 1 + g. (Nakamoto's table counts a tie as success and is reproduced on his
convention in part two; with a tie counted, a forger at d = 1, g = 1 orphans
nothing and the instrument would price the tip at zero.) Both factors are
exact: P(win) in closed form, the numerator by a tridiagonal solve. Monte
Carlo is the check, not the source.
The price of the coin cancels in τ(depth) = (f/R)/κ, κ the fee as a fraction of
R. What the model omits is the fall in the coin's price after a public rewrite
(Budish's Δ_attack, "collapse"), which raises f and is therefore the safe
direction.

CALIBRATION FIRST, twice. (1) trace_gap.pow_specimen must return the 1.054
Sign and Work §5 has published since its v0.3, from this module's import of it. (2)
Nakamoto 2008 §11 publishes a table; his Poisson formula must reproduce four
cells of it to seven decimals, and a block-by-block race must agree with the
exact (negative-binomial) form of the same model.

PREDICTIONS, STATED BEFORE RUNNING.
  P1. pow_specimen() returns 1.054 to three decimals.
  P2. Nakamoto's formula reproduces (q, z) = (0.1, 5), (0.1, 10), (0.3, 5),
      (0.3, 10) → 0.0009137, 0.0000012, 0.1773523, 0.0416605. The exact form
      sits ABOVE his figure in every cell (the negative binomial has the
      Poisson's mean and a fatter tail), by less than a factor of 1.5; the
      simulated race agrees with the exact form within 4 standard errors.
  P3. τ(volume) = fee − reward exactly, and is NEGATIVE wherever a venue's
      rewards exceed its fee: the reading pays its forger. τ(holders) = transfer
      fee over mean position, under 0.01 on the specimen. τ(floor) = fee − reward
      by a self-sale and 0 by a listing.
  P4. DECLARED fee: a miner's cost is the revenue it displaces, which does not
      depend on what it declares, so τ falls as 1/declaration — under 0.011 at
      100× the clearing rate, at any congestion. CLEARING reading: τ ≥ 0.8 for
      an artefact of up to 1% of a block once the mempool exceeds 1.5 blocks;
      between 0.5 and 0.9 at 10% of a block; VACUOUS (reading zero, cost zero)
      when the block is not full. BURN: τ = 1 against every class.
  P5. P(win) from the closed form agrees with the simulated walk within 4
      standard errors at every checked cell, and so does E[m_a · 1{fail}].
  P6. For q < 1/2 the race cost, minimised over g, grows geometrically in d at
      a log-slope within 15% of ln(p/q), and the minimising g is small (≤ 4).
      At q = 1/2 it grows linearly in d. For q > 1/2 it falls towards zero
      with patience: under 0.01 R at g = 64 for q = 0.55, at every d.
  P7. For q < 1/2 the eclipse (cost d·R, linear) undercuts the race from some
      small depth on — by d = 3 for q ≤ 0.3, by d = 12 for q = 0.45 — so the
      binding forgery of DEPTH against a minority is the private one, and it
      fools one reader. τ(depth) at κ = 1e-4 exceeds
      1,000 at depth 1 for every q ≤ 0.45 — the first reading above one in the
      corpus — and is ZERO for q > 1/2.

WHAT CAME BACK. Three of seven predictions missed, one of them twice, and one
forger was too weak.
  P1 held: 1.0536.
  P2, the reproduction held: four cells to seven decimals, the exact form
      above in every cell, the simulated race within 1.4 standard errors of it.
      The BOUND missed in three cells of four: exact over Poisson is 1.950,
      6.331, 1.114, 1.563. The approximation understates the attacker by a
      factor that grows with z — six-fold at (0.1, 10) — which is Rosenfeld's
      2014 correction, read too lightly when the bound was written.
  P3 held to the fourth decimal. Two of four venues are BELOW ZERO.
  P4. The first run packed blocks by prefix and returned τ(clearing) = 1.0167,
      1.0390, 1.0212 at three cells: not a gap, a forger weaker than its class
      (the supremum rule, again). Given first-fit packing the same cells return
      0.8876, 0.9867, 1.0212; what stays above one is inside 1 + 140/a, the
      packing grain — written down after the run, checked since, and NOT a
      theorem: τ ≤ 1 is exact for a fractional packer only, and a knapsack's
      optimum is not concave in its capacity. The prefix packer's column is
      kept beside the right one. The 10% artefact
      came in at 0.926 / 0.959 / 0.971, ABOVE the predicted 0.9: a MISS three
      times, in the direction of a sturdier reading. DECLARED at 100×: 0.0089
      to 0.0102. Below capacity: VACUOUS. The burn: 1.0000.
  P5 held at all four cells, worst 1.3 standard errors.
  P6. Log-slope over ln(p/q): 1.000 at q = 0.1, 1.037 at 0.3, and 1.941 at
      0.45 — a MISS; the geometric law is asymptotic and at p/q = 1.22 the
      polynomial prefactor owns every depth measured. At q = 1/2 the cost is
      d(d+1)/3 on all four depths: QUADRATIC, not linear — a second MISS, from
      forgetting that failing paths wander before they fail. The minimising g
      is 1 everywhere below 1/2 and the largest offered above it; q = 0.55 at
      g = 64 costs 6.8e-4 R, and 1e-20 R at g = 256.
  P7 held. The eclipse binds from d = 1 for q ≤ 0.3 and from d = 3 at 0.45 and
      0.5. τ(depth) at d = 1: 10,000 / 10,000 / 8,933. Above 1/2: 1e-16.
  NOT PREDICTED: below 1/2 and past the tip, τ(depth) = d/κ whatever q is. The
      exponential is the price of moving the mound for everyone; the line is
      the price of showing one reader a different mound, and it does not
      depend on the forger's share at all.

ADDED AFTER THE PRIOR-ART CHECK, which ran while this module was written.
  The net-zero cost of a successful rewrite is not this module's: it is Budish
  2025 Theorem 2 and Gans–Halaburda 2024, under their conditions — no cost
  friction against honest miners, no difficulty adjustment during the attack,
  no fall in the coin's price. The first draft of the paragraph above called
  the price fall Budish's "sabotage"; sabotage is his name for a motive, and
  the mechanism is "collapse". Corrected in place.
  The exact column of part two is Rosenfeld 2014 Table 1, which the check then
  supplied: 0.178%, 0.001%, 19.762%, 6.511% (and Grunspan–Pérez-Marco 2018,
  Tables 2–3, to all seven decimals). A second published number, and part two
  now asserts it. His convention (one pre-mined block, overtake by
  one) and Nakamoto's (none, tie) are the same ruin problem.

Seeded throughout (28_000 + part). NumPy only. `python barrow.py` reproduces
every number quoted in The Barrowverse; ~20 s, most of it the 1.054.
"""
import math
import sys
from dataclasses import dataclass

import numpy as np

from trace_gap import Specimen, measure, pow_specimen

__all__ = ["Venue", "nakamoto_poisson", "catch_up_exact", "ruin_walk",
           "win_probability", "orphaned_blocks", "race_cost", "fee_readings"]

SEED = 28_000
BLOCK_VB = 1_000_000            # one block of virtual bytes
MIN_TX_VB = 140                 # nothing smaller is in the mempool
KAPPA = 1e-4                    # the artefact's fee as a fraction of the block reward
GIVE_UPS = (1, 2, 4, 8, 16, 32, 64, 256)
PUBLISHED_NAKAMOTO = {(0.1, 5): 0.0009137, (0.1, 10): 0.0000012,
                      (0.3, 5): 0.1773523, (0.3, 10): 0.0416605}
PUBLISHED_ROSENFELD = {(0.1, 5): 0.00178, (0.1, 10): 0.00001,      # Table 1, as
                       (0.3, 5): 0.19762, (0.3, 10): 0.06511}      # percentages


# --------------------------------------------------- calibration: Nakamoto §11

def nakamoto_poisson(q: float, z: int) -> float:
    """Nakamoto 2008 §11: attacker progress while z blocks confirm taken as Poisson."""
    p = 1.0 - q
    lam = z * q / p
    total = 0.0
    for k in range(z + 1):
        poisson = math.exp(-lam) * lam ** k / math.factorial(k)
        total += poisson * (1.0 - (q / p) ** (z - k))
    return 1.0 - total


def catch_up_exact(q: float, z: int) -> float:
    """The same model with the attacker's progress negative-binomial, as it is."""
    p = 1.0 - q
    total = 0.0
    for m in range(z + 1):
        total += math.comb(m + z - 1, m) * (p ** z * q ** m - p ** m * q ** z)
    return 1.0 - total


def ruin_walk(deficit: np.ndarray, q: float, ceiling: np.ndarray,
              rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """
    Gambler's ruin on the attacker's deficit, one block event at a time.

    Each event is the attacker's with probability q (deficit − 1), otherwise the
    honest chain's (+ 1). Absorbed at 0 and at `ceiling`. Returns (won, attacker
    blocks mined).
    """
    deficit = deficit.astype(np.int64).copy()
    ceiling = np.broadcast_to(ceiling, deficit.shape)
    blocks = np.zeros_like(deficit)
    live = np.flatnonzero((deficit > 0) & (deficit < ceiling))
    while live.size:
        mine = rng.random(live.size) < q
        deficit[live] += np.where(mine, -1, 1)
        blocks[live] += mine
        live = live[(deficit[live] > 0) & (deficit[live] < ceiling[live])]
    return deficit <= 0, blocks


def race_from_broadcast(q: float, z: int, trials: int,
                        rng: np.random.Generator, slack: int = 40) -> np.ndarray:
    """Nakamoto's race, simulated: mine until z confirmations, then catch up or not."""
    honest = np.zeros(trials, dtype=np.int64)
    attacker = np.zeros(trials, dtype=np.int64)
    live = np.arange(trials)
    while live.size:
        mine = rng.random(live.size) < q
        attacker[live] += mine
        honest[live] += ~mine
        live = live[honest[live] < z]
    deficit = np.maximum(z - attacker, 0)
    won, _ = ruin_walk(deficit, q, deficit + slack, rng)
    return won


# ------------------------------------------------------------ market readings

@dataclass(frozen=True, slots=True)
class Venue:
    """A venue's terms in basis points of notional. Amounts are integer sats;
    fees and rewards both round down, so neither side of τ gains a sat per trade."""
    name: str
    fee_bps: int
    reward_bps: int


def volume_tau(venue: Venue, notionals: np.ndarray) -> float:
    """
    w: capital that changed hands between distinct owners. f: what one owner on
    both sides of the same trades is out of pocket, by the ledger.
    """
    fees = notionals * venue.fee_bps // 10_000
    rewards = notionals * venue.reward_bps // 10_000
    owner = int((rewards - fees).sum())
    house = int((fees - rewards).sum())
    assert owner + house == 0, "ledger does not conserve"
    return -owner / int(notionals.sum())


def holders_tau(positions: np.ndarray, transfer_fee: int) -> float:
    """w: what N distinct holders committed. f: N transfers from one wallet to N."""
    return positions.size * transfer_fee / int(positions.sum())


# --------------------------------------------------------------- fee readings

def mempool(congestion: float, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Sizes (vB) and fees (sats), sorted by feerate descending; total = congestion blocks."""
    n = int(congestion * BLOCK_VB / 600) + 64
    sizes = rng.integers(MIN_TX_VB, 1_200, size=n)
    rates = rng.lognormal(mean=math.log(12.0), sigma=0.9, size=n)
    fees = np.ceil(sizes * rates).astype(np.int64)
    keep = np.cumsum(sizes) <= congestion * BLOCK_VB
    sizes, fees = sizes[keep], fees[keep]
    order = np.argsort(-(fees / sizes), kind="stable")
    return sizes[order], fees[order]


def block_revenue(sizes: np.ndarray, fees: np.ndarray, room: int,
                  first_fit: bool = True) -> tuple[int, float]:
    """
    Fill `room` vB from the top of the mempool. Returns (fees, clearing rate);
    the clearing rate — the rate at which the prefix stopped — is 0.0 when the
    block is not full. With first_fit the packer goes on down the mempool taking
    whatever still fits; without it the block is the prefix alone (the first
    run's packer, kept because its numbers are quoted in the docstring).
    """
    fits = int(np.searchsorted(np.cumsum(sizes), room, side="right"))
    full = fits < sizes.size
    clearing = float(fees[fits - 1] / sizes[fits - 1]) if full and fits else 0.0
    revenue = int(fees[:fits].sum())
    left = room - int(sizes[:fits].sum())
    if first_fit:
        for size, fee in zip(sizes[fits:].tolist(), fees[fits:].tolist()):
            if left < MIN_TX_VB:
                break
            if size <= left:
                revenue, left = revenue + fee, left - size
    return revenue, clearing


def fee_readings(congestion: float, artefact_vb: int, rng: np.random.Generator,
                 first_fit: bool = True) -> tuple[float, float, int]:
    """
    Returns (clearing rate, τ of the CLEARING reading, displaced sats).

    The forger is a miner including its own artefact in its own block. Whatever
    it declares it pays to itself; what it loses is the revenue of the
    transactions its artefact displaced. An honest inscriber pays the clearing
    rate for the same space. τ(DECLARED at k × clearing) = τ(CLEARING) / k.
    """
    sizes, fees = mempool(congestion, rng)
    without, _ = block_revenue(sizes, fees, BLOCK_VB, first_fit)
    beside, clearing = block_revenue(sizes, fees, BLOCK_VB - artefact_vb, first_fit)
    displaced = without - beside
    honest = math.ceil(artefact_vb * clearing)
    return clearing, (displaced / honest if honest else float("nan")), displaced


def burn_specimen(sats: int, displaced: int) -> Specimen:
    """The control. Accepts only a provably unspendable output of `sats`."""
    return Specimen(
        f"burn of {sats:,} sats", float(sats),
        [("burn it", lambda: (float(sats), True)),
         ("pay it to oneself as a fee", lambda: (float(displaced), False)),
         ("sign a claim to have burned it", lambda: (1.0, False))],
        note="known answer τ = 1, against a miner as against anyone",
    )


# ---------------------------------------------------------------------- depth

def win_probability(q: float, d: int, ceiling: int) -> float:
    """P(deficit reaches 0 before `ceiling`), from d. Closed form."""
    p = 1.0 - q
    if math.isclose(q, p, rel_tol=0.0, abs_tol=1e-12):
        return (ceiling - d) / ceiling
    r = q / p
    return (r ** d - r ** ceiling) / (1.0 - r ** ceiling)


def orphaned_blocks(q: float, d: int, ceiling: int) -> float:
    """
    E[m_a · 1{fail}] from deficit d: attacker blocks mined on the paths that give
    up. u(x) = q (u(x−1) + 1 − h(x−1)) + p u(x+1), u(0) = u(ceiling) = 0.
    """
    p = 1.0 - q
    size = ceiling - 1
    system = np.eye(size)
    rhs = np.zeros(size)
    for x in range(1, ceiling):
        if x > 1:
            system[x - 1, x - 2] = -q
        if x < ceiling - 1:
            system[x - 1, x] = -p
        rhs[x - 1] = q * (1.0 - win_probability(q, x - 1, ceiling))
    return float(np.linalg.solve(system, rhs)[d - 1])


def race_cost(q: float, d: int, give_ups: tuple[int, ...] = GIVE_UPS) -> tuple[float, int]:
    """f_race / R minimised over the give-up rule. Returns (cost, minimising g).
    Overtaking a chain d deep is a ruin problem from d + 1."""
    start = d + 1
    costs = [(orphaned_blocks(q, start, start + g) / win_probability(q, start, start + g), g)
             for g in give_ups]
    return min(costs)


# ---------------------------------------------------------------------- parts

def _flag(ok: bool, text: str = "MISS") -> str:
    return "" if ok else f"   <-- {text}"


def part_one_pow() -> None:
    print("PART ONE — calibration: the published 1.054 (Sign and Work §5)")
    tau = measure(pow_specimen())
    print(f"  reproduces to three decimals: {round(tau, 3) == 1.054}"
          f"{_flag(round(tau, 3) == 1.054)}")


def part_two_nakamoto() -> None:
    print("\nPART TWO — calibration: Nakamoto 2008 §11")
    print(f"  {'q':>5} {'z':>3} {'published':>10} {'his formula':>12} "
          f"{'exact':>10} {'ratio':>6} {'race':>10} {'s.e.':>9}")
    rng = np.random.default_rng(SEED + 2)
    for (q, z), published in PUBLISHED_NAKAMOTO.items():
        his, exact = nakamoto_poisson(q, z), catch_up_exact(q, z)
        ok = (abs(his - published) < 6e-8 and exact > his
              and abs(exact - PUBLISHED_ROSENFELD[(q, z)]) < 5.1e-6)
        line = (f"  {q:>5} {z:>3} {published:>10.7f} {his:>12.7f} "
                f"{exact:>10.7f} {exact / his:>6.3f}")
        if exact > 1e-4:
            won = race_from_broadcast(q, z, 2_000_000, rng)
            se = math.sqrt(exact * (1 - exact) / won.size)
            ok = ok and abs(won.mean() - exact) < 4 * se
            line += f" {won.mean():>10.7f} {se:>9.7f}"
        else:
            line += f" {'':>10} {'':>9}"
        print(line + _flag(ok) + _flag(exact / his < 1.5, "MISS: P2 bounded the ratio by 1.5"))


def part_three_market() -> None:
    print("\nPART THREE — market readings (stylised venues; integer sats)")
    rng = np.random.default_rng(SEED + 3)
    notionals = np.ceil(rng.lognormal(math.log(2e6), 1.0, 5_000)).astype(np.int64)
    venues = (Venue("fee 2.5%, no rewards", 250, 0),
              Venue("fee 0.5%, no rewards", 50, 0),
              Venue("fee 2.0%, rewards 3.0%", 200, 300),
              Venue("no fee, rewards 1.0%", 0, 100))
    print(f"  {'venue':<24} {'τ(volume) = τ(floor, self-sale)':>32}")
    for v in venues:
        tau = volume_tau(v, notionals)
        want = (v.fee_bps - v.reward_bps) / 10_000
        note = _flag(abs(tau - want) < 1e-4)
        note += "   BELOW ZERO — the reading pays its forger" if tau < 0 else ""
        print(f"  {v.name:<24} {tau:>32.4f}{note}")
    positions = np.ceil(rng.lognormal(math.log(4e5), 1.0, 2_000)).astype(np.int64)
    tau_h = holders_tau(positions, transfer_fee=1_500)
    print(f"  τ(holders), 2,000 wallets, 1,500-sat transfers: {tau_h:.4f}"
          f"{_flag(tau_h < 0.01)}")
    print("  τ(floor) by a listing nobody takes: 0.0000")


def _fee_row(congestion: float, vb: int) -> int:
    """One row of part four. Returns the sats displaced (for the control)."""
    clearing, tau, displaced = fee_readings(
        congestion, vb, np.random.default_rng(SEED + 4))
    _, prefix, _ = fee_readings(
        congestion, vb, np.random.default_rng(SEED + 4), first_fit=False)
    head = f"  {congestion:>7}× {vb:>9,} {clearing:>9.2f}"
    if math.isnan(tau):
        print(f"{head} {'VACUOUS':>12} {'VACUOUS':>14} {'0.0000':>16} {'0.0000':>17}")
        return displaced
    predicted = 0.5 <= tau <= 0.9 if vb == 100_000 else tau >= 0.8
    grain = 1.0 + MIN_TX_VB / vb          # heuristic: exact only for a fractional packer
    print(f"{head} {tau:>12.4f} {prefix:>14.4f} {tau / 10:>16.4f} {tau / 100:>17.4f}"
          f"{_flag(predicted, 'MISS: P4 put a 10% artefact under 0.9')}"
          f"{_flag(tau <= grain, 'ABOVE THE GRAIN: look at the packer')}"
          f"{_flag(tau / 100 < 0.011)}")
    return displaced


def part_four_fees() -> None:
    print("\nPART FOUR — fee readings against a miner paying itself")
    print(f"  {'mempool':>8} {'artefact':>9} {'clearing':>9} {'τ(clearing)':>12} "
          f"{'prefix packer':>14} {'τ(declared ×10)':>16} {'τ(declared ×100)':>17}")
    displaced = 0
    for congestion in (0.5, 1.5, 3.0, 8.0):
        for vb in (1_000, 10_000, 100_000):
            displaced = _fee_row(congestion, vb)
    print("  the control:")
    measure(burn_specimen(250_000, displaced))


def part_five_walk() -> None:
    print("\nPART FIVE — the closed forms against a simulated walk (400,000 attempts)")
    print(f"  {'q':>5} {'d':>3} {'g':>3} {'P(win)':>9} {'walk':>9} "
          f"{'E[m·fail]':>10} {'walk':>9}")
    rng = np.random.default_rng(SEED + 5)
    for q, d, g in ((0.3, 3, 4), (0.45, 6, 8), (0.5, 3, 4), (0.55, 6, 16)):
        won, blocks = ruin_walk(np.full(400_000, d), q, np.int64(d + g), rng)
        p_win, u = win_probability(q, d, d + g), orphaned_blocks(q, d, d + g)
        lost = blocks * ~won
        se_p = math.sqrt(p_win * (1 - p_win) / won.size)
        se_u = float(lost.std()) / math.sqrt(won.size)
        ok = abs(won.mean() - p_win) < 4 * se_p and abs(lost.mean() - u) < 4 * se_u
        print(f"  {q:>5} {d:>3} {g:>3} {p_win:>9.5f} {won.mean():>9.5f} "
              f"{u:>10.4f} {lost.mean():>9.4f}{_flag(ok)}")


def part_six_depth() -> None:
    print(f"\nPART SIX — forging depth, in block rewards R; τ at κ = {KAPPA}")
    depths = (1, 3, 6, 12)
    print(f"  {'q':>5} " + " ".join(f"{'d=' + str(d):>22}" for d in depths)
          + f" {'log-slope / ln(p/q)':>20}")
    for q in (0.1, 0.3, 0.45, 0.5, 0.55, 0.7):
        cells, races = [], []
        for d in depths:
            race, g = race_cost(q, d)
            races.append(race)
            binding = "race" if race <= d else "eclipse"
            cells.append(f"{race:>10.3g} g={g:<2} {binding:>7}")
        tail = ""
        if q < 0.5:
            slope = math.log(races[-1] / races[1]) / (depths[-1] - depths[1])
            want = math.log((1 - q) / q)
            tail = (f" {slope / want:>20.3f}"
                    f"{_flag(abs(slope / want - 1) < 0.15, 'MISS: P6, the law is asymptotic')}")
        print(f"  {q:>5} " + " ".join(cells) + tail)
    print("\n  τ(depth) = min(race, eclipse) / κ:")
    for q in (0.1, 0.3, 0.45, 0.5, 0.55, 0.7):
        taus = [min(race_cost(q, d)[0], d) / KAPPA for d in depths]
        mark = "ABOVE ONE" if min(taus) > 1 else "SWITCH — the mound is free to move"
        print(f"  {q:>5} " + " ".join(f"{t:>12.4g}" for t in taus) + f"   {mark}")
    patient = max(race_cost(0.55, d, give_ups=(64,))[0] for d in depths)
    print(f"  q = 0.55 at g = 64, worst depth: {patient:.2e} R{_flag(patient < 0.01)}")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):        # τ, κ on a cp1252 console
        sys.stdout.reconfigure(encoding="utf-8")
    part_one_pow()
    part_two_nakamoto()
    part_three_market()
    part_four_fees()
    part_five_walk()
    part_six_depth()
