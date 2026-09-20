---
layout: document
title: "The Barrowverse"
subtitle: "Meme Artefacts, the Mound of Work, and a Reading Above One"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /the-barrowverse/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-09-20
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "The corpus has held one position favourable to Bitcoin since Sign and Work, and held it as a measurement: proof of work is the calibration object at a trace gap of one, and the program has no specimen above it. This paper takes the favourable position at full scope and points it at the least promising object available — a marketplace of meme artefacts, assets whose only world is their own record. The market's native readings are signs: volume, holders and floor grade at or below zero, and below zero means the reading pays its forger. A venue on a proof-of-work chain has three readings that are not signs. Blockspace valued at the clearing rate grades at one under congestion and is vacuous without it. A burn grades at one and builds nothing. And depth — the work piled on an artefact since it was buried — grades at d/κ, ten thousand per block on the specimen: the first reading above one the corpus has measured. It is above one because it is a free ride. Socially the mound is proof of work's one again; the inscriber's gap is that one divided by the share of the mound the inscriber paid for. The favourable position breaks in four places, all recorded: the declared fee is a sign; the mound is free to move above one half of the hashrate, and the chain cannot see where one half is; the distance to one half is a flow while what is buried is a stock; and who reads the mound, and what counts as an artefact under it, are conventions. Kar-Coin is amended."
status: "v0.1 · working draft"
order: 28
---

*v0.1 · working draft. Answers* Sign and Work *§8.2 outside the coherence setting and amends the second ladder of* Kar-Coin*. Instrument `code/barrow.py`, calibrated on the published 1.054 and on two published tables before any new number was read.*

## Abstract

*Sign and Work* defined the trace gap τ — the cost of forging a reading over the cost of earning it — calibrated the instrument on proof of work at τ = 1, and closed on the remark that the program had no specimen above it. Twelve papers later the corpus's through-line is that whatever gap a mechanism has is bought by its anchor, and the only anchor the corpus has ever calibrated against is the one Bitcoin stakes. This paper adopts the position that follows, favourable to Bitcoin and at full scope, and lets an instrument break it where it breaks. The object is a marketplace of meme artefacts: inscriptions and the tokens issued through them, the most purely reflexive assets there are, chosen because nothing else about them can be read. Three kinds of reading are graded against written-down forgers. **Market readings** — volume, holder count, floor — are signs: τ equals the venue's fee less its rewards, 0.025 to −0.010 on four stylised venues, and a negative gap means the reading pays its forger, which the empirical literature found on LooksRare before this paper had a symbol for it. **Fee readings** split. The declared fee is a sign, because a miner pays it to itself and loses only the revenue it displaced: τ falls as the reciprocal of the declaration, 0.0089 to 0.0102 at a hundred times the clearing rate. The same blockspace valued at the block's clearing rate grades at 0.89 to 1.02, within a packing grain of one, and is vacuous in a block that is not full. A burn grades at exactly one and builds nothing. **Depth** — the work above the artefact — evidences priority, costs its honest owner a fee of κ block rewards, and is forged two ways: by a public race, whose cost relative to honest mining is the revenue of orphaned blocks over the probability of winning, exponential in depth below half the hashrate, d(d+1)/3 at exactly half and zero above it; or by mining d blocks in private for one eclipsed reader, which costs d rewards whatever the forger's share. Below one half the private forgery binds from the first or third block, and **τ(depth) = d/κ — 10,000 per block at κ = 10⁻⁴**, the first reading above one in the corpus. It is a free ride, and saying so is the result: against the whole mound the private forgery costs exactly what the mound cost, so the social gap is proof of work's one, and the inscriber's gap is that one divided by the inscriber's share of the bill. Summed over every artefact under the mound the gap is the reciprocal of their share of the block reward — 1.08 in the one block where fees were nearly all of it — and returns to one as the subsidy ends. The zero-cost majority rewrite is Budish's and Gans and Halaburda's; the non-rival anchor is Auer's; the burn's rationale is Roughgarden's; none is claimed. Four predictions missed and one forger was too weak, all on record. *Kar-Coin*'s sentence that nothing of a flow remains to be examined has had a counterexample in Volume I since the anthology began, and is amended.

---

## 1. The Position Already Held

The corpus has been favourable to Bitcoin for six weeks without saying so, and it has been favourable in the only way it permits itself: as a number.

*Sign and Work* §5, since its v0.3, opens by calibrating its instrument. A ratio of two costs is worth nothing until it returns a known answer to a known question, and the question with a known answer is proof of work: the reading rule accepts a nonce whose hash clears a target, no shortcut to the search is known, forging costs what earning costs, τ = 1 by construction. The instrument returned 1.054 over four hundred trials. §8.2 of the same paper then asked whether any substrate admits a reading above one and recorded the state of the evidence in a sentence: "Proof of work sits at exactly 1 and the program has no specimen above it."

The papers since have narrowed what stands beside it. *Sign and Work* §5.3: coherence never contributes to the trace gap; whatever gap a mechanism has is bought by its anchor. *Independent and Expensive* Remark 3.7: proof of work is not a counterexample to the exclusion but the escape from it — a second pool of paid work, which is what an anchor is — and a Combination Proof of order K is K anchors wearing readings. *One's Own Anchor* Theorem 3.4 promoted the through-line to a property of the class: every reading of declared frames has native share zero. Volume I had said at the outset that energy is verifiable by the chain by virtue of being a chain — "the proof of work *is* the verification" — and *Proof of Preservation* that dissipation is self-verifying, "a hash whose cost follows from thermodynamics with no witness required." Set side by side, these say that the program spent its papers since discovering that readings cannot create paid degrees of freedom and only anchors can, while the one anchor it trusted enough to calibrate against was the first derivation's.

This paper adopts the favourable position at full scope. The position was adopted before the instrument was written and is recorded as adopted, not as found. What the discipline of the corpus supplies is the other half: predictions fixed in a docstring before the run, an instrument free to return an absurdity, and a section at the end for what is declined. The position breaks in four places (§6, §7.4, §7.5, §8.2) and the breaks are part of the result.

The object is chosen to give the position nothing to lean on. A meme artefact — an inscription, or a fungible token issued through one — has no cash flow, no use and no referent; the asset's world is its own record. In the language of *A World with Memory* §3, the pool a reading could evidence is the entropy of the world given the public record, and for an asset with no world outside the record that pool is, to a first approximation, empty. A marketplace of such assets is the null specimen of the whole program: whatever a venue can honestly read there, it reads from the chain and not from the asset.

The name is the mound. A barrow is what is raised over a burial, and the longer it stands the more of it there is; an artefact on a proof-of-work chain is buried under every block mined since. John Barrow's inward ladder [33], which *Kar-Coin* set beside Kardashev's, is the other sense, taken up in §9. The ear will also hear *borrow*, and is not wrong to.

---

## 2. Prior Art, and the Boundary of the Claim

The check was run while the instrument was being written and changed what is claimed. Almost every component is someone else's.

**The race.** The probability that a minority attacker catches up from z blocks behind is Nakamoto's [1], with Rosenfeld's correction [2] that the attacker's progress is negative-binomial and not Poisson, and Grunspan and Pérez-Marco's closed form and proof that the approximation understates from the second confirmation on [3]. That a majority always succeeds is in all three.

**The zero-cost majority.** That a successful rewrite pays for itself out of the block rewards of the rewritten chain is Budish's Theorem 2 [4] — present in the 2025 version and, by its own footnote, absent from the 2018 working paper — stated under three conditions: no cost friction against honest miners, no difficulty adjustment during the attack, no fall in the coin's value. Gans and Halaburda [5] generalise it and, with fees, find the net cost can be slightly negative. Moroz et al. [6], Auer [7] and Bonneau [8] are credited by Budish for the same intuition. §7's cost model is theirs. Optimal strategies richer than the one-parameter give-up rule used here are computed by Sompolinsky and Zohar [9] and by Gervais et al. [10] as decision processes, the second with mining cost in units of the block reward. Sompolinsky and Zohar warn that bounding an attack by forgone rewards has "erred in considering only limited attack scenarios, and in fact it is easy to show that attacks may not cost the attacker at all": a double-spender of any share can mine ahead in private and spend only when luck has already put it in front. That route is closed to the forger of §7 for a reason that is the one respect in which priority is harder to forge than payment — a backdated artefact does not exist before it is made, so its forger cannot mine ahead and always starts from behind. Selfish mining (Eyal and Sirer [11]) raises a minority's revenue; what it does to a race from behind is not computed here.

**The non-rival anchor.** Auer [7] names it the tragedy of the common chain: fees buy security for every transaction in the block equally while each fee is paid individually, a classical free-rider problem. §7.3's account of why depth grades above one is that passage read from the free rider's side. Budish's flow-against-stock argument [4] is the matching objection from the attacker's side and is taken up in §7.5.

**The eclipse.** Heilman et al. [12]. **Timestamping by hash chain** is Haber and Stornetta's [13]; on Bitcoin, Todd's [14], who observes that one transaction timestamps an unbounded number of messages.

**The burn.** Roughgarden's analysis of EIP-1559 [15], Key Takeaway 5: base-fee revenue "must be burned or otherwise withheld from the block's miner, as otherwise the miner could collude with users off-chain to costlessly simulate a first-price auction." §6's declared-fee result is that sentence in this program's units, and *otherwise withheld* names a third repair — paying the fee forward to later blocks — which §6 records and does not measure. Proof of burn is Stewart's proposal, formalised by Karantias, Kiayias and Zindros [16]; Counterparty issued its token by burning about 2,125 BTC to an address with no known key between 2 January and 3 February 2014 [17].

**The market readings.** That rewarded wash trading is profitable — a negative trace gap in all but name — was measured by La Morgia et al. [18]: reward exploitation on LooksRare succeeded in over 80% of operations at a mean gain above a million dollars. Niu et al. [19] put the wash share of LooksRare's volume at 94.5% and X2Y2's at 84.2%; von Wachter et al. [20] measure the unrewarded kind. Cong et al. [21] is the centralised-exchange ancestor.

**Artefacts on Bitcoin.** Coloured coins (Rosenfeld [22]), Counterparty and the Rare Pepe cards issued on it from September 2016 [23], inscriptions (Rodarmor [24]; the ordinal-numbers BIP draft was closed unmerged in March 2026), BRC-20 and Runes. That blockspace demand from artefacts contributes to the security budget is said in the ordinals handbook itself and measured by Bertucci [25].

**The ancestors of τ.** Szabo's *unforgeable costliness* [26] is the idea of a gap of one, twenty years before the corpus gave it a symbol. *Independent and Expensive* §2 already cites Spence, Zahavi and Grafen [27] as the ancestors of the quantity; the later signalling literature's emphasis on the differential cost of cheating over the equilibrium cost of honesty is the reading τ formalises.

**What is claimed.** The grading of a marketplace's readings on one instrument in one unit. The clearing-rate reading. The observation that below half the hashrate the binding forgery of depth is the private one, that its price is independent of the forger's share, and that the public race is therefore the price of a different thing. The identification of the reading above one as Auer's free ride measured from inside, with the social gap at one and the aggregate gap the reciprocal of the artefacts' share of the reward. The amendment to *Kar-Coin*. No mechanism is built.

---

## 3. Three Kinds of Reading

An **artefact** is data committed to a proof-of-work chain by a transaction: bytes, a block height, a fee. A **venue** ranks artefacts by readings. *Sign and Work* Definitions 3.1–3.3 apply unchanged: w(π) is what the honest party expends on the thing π is meant to evidence, f(π) the cheapest accepted forgery over a written-down attacker class, τ = f/w; and the direction of error is that paper's — measured τ is at least true τ, a low value exhibits a forgery and settles the matter, a high value is the absence of evidence.

**Definition 3.1 (market readings).** *Volume* evidences that capital changed hands between distinct owners; w is the notional traded. *Holder count* evidences that distinct parties committed capital; w is the sum of positions. *Floor* evidences that a distinct buyer paid the price; w is the price. The forger is one owner on every side.

**Definition 3.2 (fee readings).** The *declared fee* is the fee field of the artefact's transaction. The *clearing reading* is the artefact's size times the block's clearing rate — the feerate at which the block's packing stopped — and is zero in a block that is not full. The *burn* is the value of a provably unspendable output in the artefact's transaction. All three evidence that the artefact's owner gave something up for the space; w is what an owner who is not a miner gives up. The forger is a miner including its own artefact in its own block.

**Definition 3.3 (depth).** The *depth* of an artefact is the number of blocks from its own to the tip. It evidences priority: that the artefact existed no later than its block. The honest owner's cost is the fee, κ in units of the block reward R, and waiting. Two forgers are written down. The *race* rewrites the chain in public from d blocks back, with hash share q and a rule for giving up. The *eclipse* mines d blocks at full difficulty in private and shows them to one isolated reader.

Priority is read by height. A reading of priority from header timestamps is cheaper to forge than any rewrite, since a majority can hold back the median time without breaking a rule — an observation recorded by the OpenTimestamps project — and is not considered further.

---

## 4. Calibration

Two published numbers before any new one, which is the corpus's rule.

**The 1.054.** `barrow.py` imports `trace_gap.pow_specimen` unchanged and it returns 1.0536.

**Nakamoto's table.** Nakamoto's formula reproduces four cells of his §11 table to seven decimals. The exact form of the same model — the attacker's progress while z blocks confirm is negative-binomial — sits above his figure in every cell, and a block-by-block race of two million trials agrees with the exact form within 1.4 standard errors:

| q | z | published [1] | exact | exact / published | simulated race |
|---|---|---|---|---|---|
| 0.1 | 5 | 0.0009137 | 0.0017818 | 1.950 | 0.0018235 ± 0.0000298 |
| 0.1 | 10 | 0.0000012 | 0.0000079 | 6.331 | — |
| 0.3 | 5 | 0.1773523 | 0.1976173 | 1.114 | 0.1977115 ± 0.0002816 |
| 0.3 | 10 | 0.0416605 | 0.0651067 | 1.563 | 0.0651200 ± 0.0001745 |

**A prediction missed here.** The docstring bounded the ratio of exact to published by 1.5, on the reasoning that the two distributions share a mean. They do; the tail is where a catch-up lives, and the approximation understates the attacker by a factor that grows with z, six-fold at ten confirmations against a tenth of the hashrate. This is Rosenfeld's correction, read too lightly when the bound was written. The prior-art check then supplied the published values: Rosenfeld's Table 1 — 0.178%, 0.001%, 19.762%, 6.511% — and Grunspan and Pérez-Marco's Tables 2 and 3, which print the exact column above to all seven decimals. The instrument now asserts the first: a third published number, acquired by missing a prediction about the second.

---

## 5. The Market Readings Are Signs

**Proposition 5.1.** On a venue charging a fee φ and paying rewards ρ, both as fractions of notional: τ(volume) = φ − ρ. With a transfer fee g and mean position s̄, τ(holders) = g/s̄. τ(floor) = φ − ρ by a self-sale and 0 by a listing nobody takes.

*Proof.* One owner on both sides of a trade is out of pocket the fee and in pocket the reward, and nothing else moves; the ledger conserves. N wallets funded from one cost N transfers. A listing costs nothing. ∎

Measured on five thousand trades in integer sats, against four stylised venues:

| venue | τ(volume) |
|---|---|
| fee 2.5%, no rewards | 0.0250 |
| fee 0.5%, no rewards | 0.0050 |
| fee 2.0%, rewards 3.0% | **−0.0100** |
| no fee, rewards 1.0% | **−0.0100** |

and τ(holders) = 0.0023 for two thousand wallets at a 1,500-sat transfer.

These are *Sign and Work*'s τ ≈ 0 regime — marker-based stigmergy, the pheromone laid without foraging — and Proposition 4.1 of that paper prices them: a gap of τ inflates the adversary's fleet by 1/τ, so a venue ranking by volume at a 2.5% fee faces an adversary forty times the size it believes, and at a 0.5% fee two hundred times.

The negative rows are outside that proposition's domain, and the instrument flags them rather than clipping them: **BELOW ZERO — the reading pays its forger.** A gap below zero is not a weak reading. It is a subsidy to forgery, and the inflation factor is not large but undefined, because the forger's budget grows with use. The venues are stylised and nothing here is an empirical claim about any of them; the empirical claim is La Morgia et al.'s [18], and it has the sign the proposition gives it. In January 2022 LooksRare charged 2%, paid trading rewards of over twenty million dollars a day, and some 87% of its first $9.5 billion of volume was wash [28].

None of this is about Bitcoin. It is the background against which a venue on any chain chooses what to rank by, and it is why the remaining sections ask what else there is.

---

## 6. Paying for Space: the Fee, the Clearing Rate and the Burn

An artefact pays for its blockspace, and what it paid looks like the obvious costly reading. It is two readings, and the obvious one is a sign.

**Proposition 6.1 (the declared fee).** A miner including its own artefact in its own block loses the revenue of the transactions the artefact displaced, whatever fee it declares. For a declaration of k times the clearing rate, τ(declared) = τ(clearing)/k.

*Proof.* The declared fee is paid by the miner to the miner. The block's other revenue falls by what no longer fits. ∎

**Proposition 6.2 (the clearing reading).** Let the block be full and packed fractionally. Then τ(clearing) ≤ 1, with τ(clearing) → 1 as the demand curve flattens over the displaced stretch. In a block that is not full the reading is zero and so is the forger's cost.

*Proof.* Every displaced byte pays at most the clearing rate, and exactly the artefact's size is displaced. An honest owner pays the clearing rate on that size. With room to spare nothing is displaced. ∎

A real packer places whole transactions, and the optimum of a knapsack is not concave in its capacity, so the integer reading departs from the proposition by a *packing grain* of the order of m/a, m the smallest transaction in the mempool. The grain is checked on every cell below and is not proved.

The mempool is lognormal and stylised; congestion is its size in blocks.

| mempool | artefact (vB) | clearing (sat/vB) | τ(clearing) | prefix packer | τ(declared ×100) |
|---|---|---|---|---|---|
| 0.5× | any | 0 | VACUOUS | VACUOUS | 0 |
| 1.5× | 1,000 | 8.01 | 0.8876 | 1.0167 | 0.0089 |
| 1.5× | 10,000 | 8.12 | 0.9867 | 1.0390 | 0.0099 |
| 1.5× | 100,000 | 9.31 | 0.9264 | 0.9337 | 0.0093 |
| 3.0× | 1,000 | 17.99 | 1.0212 | 1.0212 | 0.0102 |
| 3.0× | 10,000 | 18.12 | 1.0001 | 0.9862 | 0.0100 |
| 3.0× | 100,000 | 19.57 | 0.9590 | 0.9598 | 0.0096 |
| 8.0× | 1,000 | 34.82 | 0.9257 | 0.9257 | 0.0093 |
| 8.0× | 10,000 | 34.91 | 0.9984 | 0.9526 | 0.0100 |
| 8.0× | 100,000 | 36.79 | 0.9709 | 0.9680 | 0.0097 |

**A forger too weak, on record.** The first run packed blocks by prefix — fill from the top of the mempool and stop at the first transaction that does not fit — and returned 1.0167, 1.0390 and 1.0212 at three cells. A clearing reading above one would have been this paper's headline, and it was a forger weaker than its class: a real miner goes on down the mempool taking what fits. Given first-fit packing the same cells return 0.8876, 0.9867 and 1.0212. What remains above one is inside the packing grain, 1 + m/a, which was written down after the run and is checked in the code since; the first packer's column is printed beside the right one. This is the supremum rule of *The Multiplicity Freedom* v0.4 again, and the first time the corpus has had to apply it to a number that erred in the welcome direction.

**A prediction missed.** The docstring put a 10%-of-a-block artefact between 0.5 and 0.9 on the expectation that a large artefact eats well down the demand curve. It came in at 0.926, 0.959 and 0.971. The reading is sturdier for large artefacts than predicted, on this mempool.

**The burn** is the control and returns 1.0000 against every class, a miner included, because a provably unspendable output is paid to nobody.

**The first break in the favourable position.** Bitcoin pays fees to the miner, so the fee field of a Bitcoin transaction is a sign; Ethereum burns its base fee, and that burn is natively a reading at one against the block's proposer, for the reason Roughgarden gave [15]. On this reading the other chain is better at the protocol layer and the paper says so. What Bitcoin offers is a repair at the venue: read the clearing rate and not the declaration, or require a burn. Both repairs have a cost the table shows. The clearing reading exists only under congestion — in a block with room it is vacuous, in exactly the sense *Sign and Work* Proposition 5.1 found equality only where the score stops meaning anything. And the declared fee is a sign in the other direction too: fees paid out of band to a miner understate what was given up.

**What each reading builds.** A fee at the clearing rate is a transfer to miners and raises the mound. A burn is a transfer to every holder and raises nothing. *Kar-Coin* called proof of work "a mechanism that rewards burning," and of the three readings here it is the burn the phrase fits without remainder: a venue that ranks by burn is a handicap contest, sound and idle. The costly-signalling literature [27] is its theory and nothing here adds to it.

---

## 7. The Mound

### 7.1 The race

The cost model is declared because every number in this section rests on it, and it is not this paper's (§2). Under free entry a block's work costs its reward R. A forger hashes either way, so the cost of attacking *relative to mining honestly* is the revenue of the blocks it orphans: on success its blocks are canonical and pay R each; on failure they pay nothing. A public rewrite must carry strictly more work than the chain it replaces, so forging depth d is a gambler's ruin on the forger's deficit started from d + 1, absorbed at zero and at a give-up line d + 1 + g.

**Proposition 7.1.** Under the model, f_race/R = min over g of u(d+1)/h(d+1), where h(x) = (rˣ − rᴺ)/(1 − rᴺ) with r = q/p and N = d + 1 + g is the probability of winning from a deficit of x, and u solves u(x) = q(u(x−1) + 1 − h(x−1)) + p·u(x+1) with u(0) = u(N) = 0.

*Proof.* h is the classical ruin probability. u(x) is the expected number of forger's blocks on paths that give up: a forger's block adds one to the count on every failing continuation. The expected orphaned revenue per attempt over the probability of success is the expected cost per success. ∎

Both factors are exact, the second by a tridiagonal solve; a simulated walk of 400,000 attempts agrees with each at four cells, worst 1.3 standard errors. In block rewards:

| q | d = 1 | d = 3 | d = 6 | d = 12 | minimising g |
|---|---|---|---|---|---|
| 0.1 | 8.9 | 918 | 6.7 × 10⁵ | 3.6 × 10¹¹ | 1 |
| 0.3 | 2.07 | 29.3 | 477 | 8.0 × 10⁴ | 1 |
| 0.45 | 0.893 | 6.54 | 31 | 217 | 1 |
| 0.5 | 0.667 | 4 | 14 | 52 | 1 |
| 0.55 | 1.3 × 10⁻²⁰ | 2.2 × 10⁻²⁰ | 3.0 × 10⁻²⁰ | 3.7 × 10⁻²⁰ | 256 |
| 0.7 | 10⁻⁹³ | 10⁻⁹³ | 10⁻⁹³ | 10⁻⁹³ | 256 |

Below one half the cheapest forger gives up the moment it falls one block further behind and starts again; above, it never gives up.

**Two predictions missed.** The docstring predicted a log-slope in d within 15% of ln(p/q) for every q below one half. It is 1.000 of that at q = 0.1, 1.037 at 0.3, and 1.941 at 0.45: the geometric law is asymptotic, and at p/q = 1.22 a polynomial prefactor owns every depth measured. And it predicted linear growth at exactly one half. The cost there is d(d+1)/3 on all four depths — quadratic — because failing paths wander before they fail and the orphans accumulate on the way. Neither miss moves a conclusion; both are errors about a model the docstring's author had just written down.

### 7.2 The eclipse

A reader cut off from the network validates what it is shown. Showing it an artefact at depth d takes d blocks at full difficulty, never published and so never rewarded:

> f_eclipse = d · R, whatever q is.

The cost of the isolation itself is unpriced here and is not small [12]. Against a forger below one half the eclipse undercuts the race from the first block at q ≤ 0.3 and from the third at q = 0.45 and 0.5. The prediction was that it would, by d = 3 and d = 12; it held with room.

This was not predicted and is the section's finding: **below one half and past the tip, the price of forging depth does not depend on the forger's share at all.** The exponential of §7.1 is the price of moving the mound for everyone. The line is the price of showing one reader a different mound. *Kar-Coin* wrote of the self-attesting artefact that it "will return the same answer to every party that queries it"; that clause is the expensive one, and a venue that reads the chain for itself and for its users buys only the cheap one.

### 7.3 The gap, and whose it is

**Proposition 7.2 (the mound's gap).** Under the cost model, against a forger of share q < 1/2, τ(depth) = min(f_race, d)/κ, which exceeds one whenever the fee is below two thirds of a block reward; past the crossover τ(depth) = d/κ.

At κ = 10⁻⁴ — a fee of some thirty thousand sats against the present reward — τ at depths 1, 3, 6, 12 is 10,000, 30,000, 60,000, 120,000 for q = 0.1 and 0.3, and begins at 8,933 for q = 0.45. The price of the coin cancels: fee and reward are both in it. **This is the corpus's first reading above one**, and *Sign and Work*'s caution governs it entirely. A high measured τ certifies nothing. The class here grew by two forgeries during drafting — the eclipse, and §8.2's — each cheaper than the last, and a third would be cheaper again.

What the instrument can say is why the number is large, and the reason deflates it. The honest owner paid κR for a reading whose forgery costs dR because everyone else under the mound paid too, and the holders paid most of all. This is Auer's tragedy of the common chain [7] measured from the free rider's seat.

**Corollary 7.3 (the social gap is one).** Against the eclipse, forging d blocks of mound costs d blocks of work. The ratio of the forgery to what the mound cost *everyone* is 1: the calibration object, returned. The inscriber's gap is that one divided by the inscriber's share of the bill, κ/d.

**Corollary 7.4 (the aggregate gap).** One private forgery backdates every artefact in it. Summed over all artefacts under the mound, whose fees are a share α of the block reward, τ = 1/α.

For a collection of k artefacts the gap is d/(kκ), which for ten thousand items at κ = 10⁻⁴ is d itself. For the whole population it is the reciprocal of what artefacts contribute. In block 840,000 taken alone, where a new token protocol launched at the halving and fees were 37.626 BTC against a subsidy of 3.125, the aggregate gap was 1.083 if every fee in it was an artefact's, and higher otherwise. As the subsidy ends, and to the extent artefacts are who pays, **the aggregate reading returns to one**. The reading above one is a transfer from the holders who fund the subsidy and the payers of monetary fees to whoever buries something under their mound — real, measurable, and temporary on the halving schedule.

This answers *Sign and Work* §8.2 in a form that paper would recognise. No work here is more expensive to forge than to do. A reading exceeds one exactly when its earning is shared and its forging, for the forger's purpose, is not; and *Sign and Work* §5.3 holds without amendment — the gap is bought entirely by the anchor, and the artefact's content appears only in the denominator, where at κ = 10⁻⁴ it barely appears at all. The meme contributes nothing. It was never going to.

### 7.4 The switch

Above one half the race costs nothing net — 6.8 × 10⁻⁴ R at a give-up line of 64 for q = 0.55, 10⁻²⁰ R at 256 — and τ(depth) is zero. The instrument prints **SWITCH — the mound is free to move**. This is Budish's Theorem 2 [4] and holds under its conditions, which depth strains. Overtaking from d + 1 behind takes (d + 1)/(q − p) block events in expectation; the theorem needs no difficulty adjustment in that time, so it covers depths to about 2016(2q − 1) blocks — two hundred at q = 0.55, a day and a half of mound — and past that this paper has no number. Within it the mound costs a majority time and visibility and nothing else. A rewrite of a day at q = 0.55 is ten days of public, unmistakable work, and the fall in the coin's price that would follow is the term the model omits in the safe direction.

**The second break.** The gap of §7.3 is conditional on a fact the chain cannot see. Hash share is not on the chain. Pool shares are read from tags that pools write into their own blocks — signed claims, the canonical τ ≈ 0 reading of *Sign and Work* §3. By those tags the two largest pools mined 43.7% of blocks in the month to 20 September 2026 [29]; by block template, one of them and the pools that share its templates were near 40% through 2024 on their own [30], so the largest two template-issuers plausibly exceed one half already. Pools are not owners of hashrate, and miners can leave them. But the condition under which the mound reads above one is attested by a reading at zero, and the favourable position does not survive that sentence intact.

### 7.5 Flow against stock

**The third break** is Budish's, and nothing here repairs it. The switch's distance in money is a flow — the reward per block times the coin's price, which hashrate follows — and what lies under the mound is a stock. The more that is buried under one mound the larger the prize for moving it, so the anchor's non-rivalry in production is rivalry in attack incentive. *Volume I* said of proof of stake that "the circle is small but it closes"; for proof of work the circle is larger and also closes. What cancels is the price in τ *below* the switch. What does not cancel is how far away the switch is.

Artefacts' fees are part of the flow. That they fund the mound that attests them is true, is said by their own handbook [24] and measured [25], and is subject to Auer's result in full: each artefact's fee buys depth for every artefact equally, so each under-pays.

---

## 8. The Barrow Reading

### 8.1 What a venue can rank by

A venue on a proof-of-work chain has three readings that are not signs — depth, space at the clearing rate, and burn — and the thesis of this paper, so far as it is a thesis about marketplaces, is that it should rank by those and display the rest. Issue by burn, as Counterparty did in 2014, or by fee at the clearing rate; rank by depth; show volume, holders and floor as what they are. The pools are disjoint — hash for depth, coin for space or burn — so by the argument of *Independent and Expensive* Remark 3.7 the conjunction is independent in both directions and its cost is the sum; this is asserted from that remark and not measured.

What the conjunction evidences is *priority* and *sacrifice*: when the thing was buried and what was given up to bury it. It evidences nothing else. It cannot tell a good meme from a bad one, a living market from a dead one, or a collection from its copy one block younger, except by the block. For an asset whose world is its own record these two are, on the account of *A World with Memory*, the only variables outside the record there were; the barrow reading reads both and the rest of the asset is not there to be read. A venue ordered this way is a field of barrows ordered by seniority and by the size of the offering. Most of what is under them is dead — in the weeks measured in early 2025, fewer than one launched token in a hundred so much as completed its launch curve [31] — and the dead remain, exactly as attested as the living.

### 8.2 The fourth break: the reader, and the artefact

A venue that reads depth through an indexer's interface has replaced the reading with a signed claim about it, at τ ≈ 0. *Sign and Work* §4 said it of a lattice: τ is a property of the reading, and a mechanism that measures and a mechanism that accepts a certificate have the same substrate and wildly different gaps. The instrument fine enough to read the mound is a commodity computer, which is the favourable fact; whether a venue uses one on its users' behalf is not something its users can read from the venue, which is the other.

And what counts as an artefact is not consensus. Which sat an inscription rides, how inscriptions are numbered, what a BRC-20 balance is: these are conventions of indexing software that the chain does not enforce and that have been revised. Inscriptions the first indexer did not recognise were later admitted and numbered from minus one downwards, and from block 824,544 numbered positively again, without retroaction [24]. BRC-20's author describes the standard as "off-chain balance states" [35]; a balance is what an indexer computes, and the chain records only that some bytes were inscribed [36]. The bytes and their depth are under the mound. The artefact's identity is over it.

---

## 9. What the Earlier Volumes Must Now Say

The full scope of the position reaches two sentences of the anthology.

***Kar-Coin*, the second ladder.** "A flow is invisible the moment it has passed. Nothing of the megawatt-hour remains to be examined; there is only the record of it, and a record is a report, and a report requires a reporter. Every rung of the outward ladder must therefore be attested by something standing outside the mechanism and asked to be honest." Volume I had already exhibited the counterexample — "the proof of work *is* the verification" — and *Proof of Preservation* had called dissipation self-verifying. A hash under a target is the residue of a flow. It attests an expected count of operations and, through the efficiency of the best machine, a floor on the energy; the first is a fact of the protocol and the second an empirical one. *Kar-Coin* closed on a design question — "how much of a civilization's outward magnitude can be made to *follow* from the artifacts it must leave behind, so that the coin reads the flow through its residue rather than through its report" — and called it hard. It has one solved instance, which is the oldest mechanism in the anthology, and the essay's dichotomy of ladders is a dichotomy with an exception on the outward side. The instrument that reads the residue is cheap, which was the essay's other demand. *Kar-Coin* is amended to v0.4 with a note saying so.

The same essay's phrase for proof of work, "a mechanism that rewards burning," stands for the burn of §6 and stands for proof of work as a rule of issue. What it omitted is what the burning buys: a reading at one for everyone under it, non-rival, and by §7.3 above one for each of them. The magnitude is not paid for irrespective of what it accomplishes. It accomplishes the mound, and the corpus has leaned on it since *Gauge-Fixing* §4.4, whose dissipation floor is proof of work.

**Volume I, the third derivation.** "This is the move that escapes the first two derivations. The substrate is no longer an asset whose value the network borrows from outside itself." *Sign and Work* §5.3, *Independent and Expensive* Remark 3.7 and *One's Own Anchor* Theorem 3.4 together leave that sentence supported by no result: the third derivation's gap is bought by its anchors, and the anchor of record is the first derivation's. Volume I is the naming volume and carries no version. It is not revised here; the sentence is recorded as unsupported, and the restatement is work for a volume and not for a paper.

---

## 10. What Is Declined

**That the position was found.** It was adopted, in advance, and is recorded as adopted. The instrument was free to break it and did so in four places.

**That Bitcoin's value is derived.** τ grades attestation. It says a record cost what it says it cost, and nothing about what the record is worth. The charge that Bitcoin is itself an asset whose only world is its own record is not answered by anything in this paper.

**That τ(depth) > 1 certifies anything.** Measured τ bounds true τ from above. Two cheaper forgeries were added to the class while the paper was drafted.

**That the reading above one is a gift.** It is a free ride on the subsidy and on monetary fees, it is Auer's tragedy seen from inside, and in aggregate it is the reciprocal of what artefacts pay.

**That the cost model is this paper's, or settled.** It is Budish's and Gans and Halaburda's, under free entry, rentable or owned hash at no friction, static difficulty and no price response. The give-up rule has one parameter where the literature's decision processes [9, 10] have a state, so one half is where the switch is in this model and an upper bound on where it is. The cost of an eclipse is unpriced.

**That the switch's location is known.** §7.4.

**That the mempool or the venues are empirical.** Both are stylised. The clearing reading's value depends on the flatness of the demand curve over the displaced stretch, which a real mempool need not supply.

**That Ethereum loses.** On the fee reading it wins at the protocol layer. The depth of a finalised checkpoint under proof of stake is a different object and is not graded here.

**That inscriptions are a good use of blockspace.** The argument takes as a premise that blockspace demand funds the mound, which is one side's premise in a dispute this paper does not adjudicate. The relaxation of data-carrier relay policy in Bitcoin Core 30.0 [32] is noted as the dispute's current state.

**That the marketplace is not extractive.** Launch curves pay early holders out of late ones. No reading here prices that, and the service line's capture adversary is the place it would be priced.

**That the conjunction's independence was measured.** Asserted from *Independent and Expensive* Remark 3.7.

**That anything is built, or that the name is a product's.**

---

## 11. Open Problems

**11.1. Above one, for work.** Every reading above one found here is a shared earning against an unshared forgery, and what it evidences is priority. *Sign and Work* §8.2's question survives in its sharper form: whether any reading above one evidences *work* or *contact*, or whether non-rivalry of the anchor is the only route and priority the only cargo.

**11.2. The null specimen, measured.** §1 asserts that a meme asset's pool is empty. *A World with Memory* §8.4 observed that a world's innovation given its record is measurable from a record alone. A memecoin's price record is free and public; fitting that paper's φ to one would turn the assertion into a number, and would be the corpus's first contact with a deployed record of any kind.

**11.3. Where the switch is.** With state-dependent strategies for a race from behind [9, 10], with selfish mining in the background [11], with Budish's collapse term, and with difficulty adjustment for deep mounds. The present model is the friendliest to the attacker above one half and among the least friendly below it.

**11.4. The mound as the corpus's anchor.** *Gauge-Fixing* §4 takes a dissipation floor and a beacon as separate anchors. Block hashes are a beacon of known bias cost: discarding a block costs its reward, so an outcome of probability p is pruned for p/(1 − p) rewards [34]. Whether the mound can serve as both, and what *The Second Pool*'s receipt-and-value separation says about a beacon whose value the miner chooses among, is open.

**11.5. The clearing reading on real blocks.** Proposition 6.2 is a bound on a relaxation; the grain's proof, its slack on a real mempool, and the fraction of blocks in which the reading is vacuous, are a day's work against public data.

**11.6. Time as a price.** Above the switch the mound costs a majority nothing and takes (d + 1)/(q − p) blocks. The program has no unit for that, and its delay functions (*Borrowed Again* §7.2) are the nearest thing it has to one.

**11.7. Finality as depth.** The trace gap of a finalised proof-of-stake checkpoint, in the same units.

---

## References

[1] S. Nakamoto. *Bitcoin: A Peer-to-Peer Electronic Cash System.* 2008. §11.

[2] M. Rosenfeld. *Analysis of Hashrate-Based Double Spending.* arXiv:1402.2009, 2014.

[3] C. Grunspan, R. Pérez-Marco. *Double Spend Races.* International Journal of Theoretical and Applied Finance 21(8), 1850053, 2018. arXiv:1702.02867.

[4] E. Budish. *Trust at Scale: The Economic Limits of Cryptocurrencies and Blockchains.* Quarterly Journal of Economics 140(1), 1–62, 2025. (Working paper: *The Economic Limits of Bitcoin and the Blockchain*, NBER WP 24717, 2018, which does not contain Theorem 2.)

[5] J. S. Gans, H. Halaburda. *"Zero Cost" Majority Attacks on Permissionless Proof of Work Blockchains.* Management Science 70(6), 4155–4165, 2024.

[6] D. J. Moroz, D. J. Aronoff, N. Narula, D. C. Parkes. *Double-Spend Counterattacks: Threat of Retaliation in Proof-of-Work Systems.* arXiv:2002.10736, 2020.

[7] R. Auer. *Beyond the Doomsday Economics of "Proof-of-Work" in Cryptocurrencies.* BIS Working Papers 765, 2019.

[8] J. Bonneau. *Why Buy When You Can Rent? Bribery Attacks on Bitcoin-Style Consensus.* FC 2016 Workshops, LNCS 9604, 19–26, 2016.

[9] Y. Sompolinsky, A. Zohar. *Bitcoin's Security Model Revisited.* arXiv:1605.09193, 2016.

[10] A. Gervais, G. O. Karame, K. Wüst, V. Glykantzis, H. Ritzdorf, S. Čapkun. *On the Security and Performance of Proof of Work Blockchains.* ACM CCS 2016, 3–16.

[11] I. Eyal, E. G. Sirer. *Majority Is Not Enough: Bitcoin Mining Is Vulnerable.* Financial Cryptography 2014, LNCS 8437, 436–454.

[12] E. Heilman, A. Kendler, A. Zohar, S. Goldberg. *Eclipse Attacks on Bitcoin's Peer-to-Peer Network.* USENIX Security 2015, 129–144.

[13] S. Haber, W. S. Stornetta. *How to Time-Stamp a Digital Document.* Journal of Cryptology 3(2), 99–111, 1991.

[14] P. Todd. *OpenTimestamps: Scalable, Trust-Minimized, Distributed Timestamping with Bitcoin.* 15 September 2016. The median-time observation of §3 is issue 147 of the project's client.

[15] T. Roughgarden. *Transaction Fee Mechanism Design for the Ethereum Blockchain: An Economic Analysis of EIP-1559.* arXiv:2012.00854, 2020.

[16] I. Stewart. *Proof of Burn.* Bitcoin Wiki, 2012. K. Karantias, A. Kiayias, D. Zindros. *Proof-of-Burn.* Financial Cryptography 2020, LNCS 12059, 523–540.

[17] Counterparty. *What Is XCP*, project documentation; burn totals per the project's forum FAQ, 23 May 2015: 2,124.63 BTC.

[18] M. La Morgia, A. Mei, A. M. Mongardini, E. N. Nemmi. *A Game of NFTs: Characterizing NFT Wash Trading in the Ethereum Blockchain.* IEEE ICDCS 2023, 13–24.

[19] Y. Niu, X. Li, H. Peng, W. Li. *Unveiling Wash Trading in Popular NFT Markets.* WWW 2024 Companion. arXiv:2403.10361.

[20] V. von Wachter, J. R. Jensen, F. Regner, O. Ross. *NFT Wash Trading: Quantifying Suspicious Behaviour in NFT Markets.* FC 2022 Workshops, LNCS 13412, 299–311, 2023.

[21] L. W. Cong, X. Li, K. Tang, Y. Yang. *Crypto Wash Trading.* Management Science 69(11), 6427–6454, 2023.

[22] M. Rosenfeld. *Overview of Colored Coins.* 4 December 2012.

[23] J. Bailey. *A Brief History of Rare Pepe.* Right Click Save.

[24] C. Rodarmor. *Inscribing Mainnet.* 20 January 2023; *Ordinal Theory Handbook*, docs.ordinals.com, including its page on inscription numbers and the jubilee at block 824,544.

[25] L. Bertucci. *Bitcoin Ordinals: Determinants and Impact on Total Transaction Fees.* Research in International Business and Finance 70, 102338, 2024.

[26] N. Szabo. *Shelling Out: The Origins of Money.* 2002; *Bit Gold.* 2005.

[27] M. Spence. *Job Market Signaling.* Quarterly Journal of Economics 87(3), 355–374, 1973. A. Zahavi. *Mate Selection — A Selection for a Handicap.* Journal of Theoretical Biology 53(1), 205–214, 1975. A. Grafen. *Biological Signals as Handicaps.* Journal of Theoretical Biology 144(4), 517–546, 1990.

[28] A. Hayward. Decrypt, 28 January 2022, citing CryptoSlam: $8.3 billion of $9.5 billion.

[29] mempool.space mining-pool API, trailing month, read 20 September 2026: Foundry USA 1,159 of 4,537 blocks (25.5%), AntPool 823 (18.1%).

[30] b10c. *Bitcoin Mining Centralization in 2025.* 15 April 2025.

[31] Y. Yun. Cointelegraph, 14 March 2025, citing Dune: graduation under 1% for four consecutive weeks from 17 February 2025; best week on record 1.67%.

[32] Bitcoin Core 30.0 release notes, 10 October 2025.

[33] J. D. Barrow. *Impossibility: The Limits of Science and the Science of Limits.* Oxford University Press, 1998.

[34] J. Bonneau, J. Clark, S. Goldfeder. *On Bitcoin as a Public Randomness Source.* IACR ePrint 2015/1015.

[35] domo (pseud.). *brc-20 experiment.* GitBook, March 2023.

[36] M. Qi, Q. Wang, Z. Wang, L. Zhong, T. Zhu, S. Chen, W. Knottenbelt. *BRC20 Pinning Attack.* arXiv:2410.11295, 2024.

Propositions verified and measurements reproducible from `code/barrow.py`, which imports the calibration specimen of `code/trace_gap.py` unchanged and reproduces that module's published 1.054, four cells of Nakamoto's table and four of Rosenfeld's before reading a new number.
