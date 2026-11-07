---
layout: document
title: "What the Burn Buys"
subtitle: "The Mining Flame Unbundled, and the Menu of What May Honestly Be Mined"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /what-the-burn-buys/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-08-10
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Bitcoin's heat is not its tax but its certificate — and yet heat-proportional-to-security is a design choice, not a law. The burn is decomposed into the four jobs it pays for at once, each job is re-let to its cheapest honest instrument, and the planetary tax collapses to a Sybil floor and one wound clock. A reversibility caveat marks where work-as-heat is implementation rather than physics; a menu of honest minables falls out of the trace-gap criterion; and a neutrino-attested reactor mint is worked as the example that shows both the promise and the compressed oracle at its centre."
status: "v0.1 · working draft"
order: 22
---

## Abstract

The oldest complaint against proof of work is its heat, and the complaint mistakes the certificate for the tax. Dissipation is the one physical quantity a cryptographic proof can certify (*Gauge-Fixing the Section Space* v0.2 §1), and the burn is what makes the forgery cost real: satisfying a public constraint is constraint satisfaction, never work (*Sign and Work* v0.3), so any scheme that removes the cost removes the security. What is *not* physics, however, is the scaling law. Bitcoin's heat grows with its security because mining is a parallel lottery — the adversary is outbid rather than out-engineered — and the lottery is one design among several. This paper decomposes the burn into the four jobs it pays for in a single currency: unpredictable leader election, temporal ordering, Sybil pricing, and unforgeability. Each job is then re-let to its cheapest honest instrument, which the program has already built: the beacon takes randomness (sky-funded, in *The Wound Clock*'s classes), the delay chain takes ordering (one sequential processor against a race of order 10²⁰ parallel guesses per second — the difference between a domestic appliance and a mid-sized nation's grid), the unique encoding takes individuation, and a thin dissipation floor takes Sybil pricing alone, paid per identity rather than per block. Under the unbundling, irreducible heat collapses from *proportional to total security* to *proportional to identity churn plus one cranked clock*. Two caveats discipline the result. First, a reversibility caveat: Landauer prices erasure, not computation, so the equation of work with heat is implementation-contingent — a sufficiently reversible miner, quantum or classical, decouples hashes from joules asymptotically, which leaves Bitcoin's security (resting on cost) intact while quietly breaking any reading of proof of work as a joule meter; the program's own dissipation floor must accordingly be specified as a cost floor, not a heat floor. Second, the menu: what may honestly be mined is exactly the set of generative residues whose trace gap is pinned at one by physics — parallel heat, sequential time, storage uniqueness, fission flux — and nothing off that list. The last entry is worked as an example: a mint denominated against reactor antineutrino flux, unforgeable and unshieldable by the weak interaction, with its honest price stated — the verifying instrument is a compressed oracle, not an absent one, and minting against raw generation walks back into the incentive trap *Kar-Coin* v0.3 named, a mechanism that rewards burning. The paper's architecture therefore splits what Bitcoin conflates: security paid through the unbundled anchors, denomination read from the involuntary ledger's aggregate, and per-agent minting acknowledged as the rung where the oracle still stands.

---

## 1. The Certificate Mistaken for a Tax

Bitcoin mines by exhibiting a preimage inequality that is astronomically cheaper to check than to find, and the finding is a search with no structure to exploit — which is precisely why it survives Grover taxed and Shor untouched (*Borrowed Hardness* v0.3), and precisely why its cost is honest. The heat is not a regrettable exhaust on an otherwise clean process. It is the process's entire evidentiary content. A hash puzzle certifies nothing about the world except that free energy was spent finding it, and that certification is the one the canon can make without a witness: the proof of work *is* the work, the predicate self-verifying, the physical correlate following from thermodynamics with nobody asked to vouch.

The program's pricing rule says why no bloodless substitute exists. A gap between forging and earning — the trace gap τ of *Sign and Work* — is bought only by *generative* cost, cost incurred in the making; an anchor read off the output is a public constraint, and satisfying a public constraint costs its satisfaction, which bears no relation to what it purports to evidence. Every scheme that would keep the security and drop the expenditure founders on this rule, and the program has already declined the famous one by name: pure stake is circular at bootstrap, its costliness borrowed from a market that presupposes the mechanism working.

So the question this paper answers is not the complaint's question. The cost stays. The question is what the cost *buys*, and on what schedule it scales — because the schedule, unlike the cost, is nobody's law.

## 2. Four Jobs, One Currency

Bitcoin's burn is a single payment for four distinct services, and naming them separately is the paper's first move, since a bundle can only be repriced after it is itemized.

**Randomness.** The lottery elects each block's author unpredictably; no coalition can arrange to win on schedule, because winning is finding, and finding is chance. The burn is purchasing unpredictable leader election.

**Ordering.** Each block's work takes real time, and the chain of accumulated work is a clock — crude, jittery, but sufficient to give the ledger a past that would cost its history's re-expenditure to rewrite. The burn is purchasing temporal ordering.

**Sybil pricing.** A hash rate cannot be minted by registering names; influence costs joules per second, so the count of "voters" means something. The burn is purchasing the multiplicity gauge, in the anchoring paper's vocabulary.

**Unforgeability.** The conjunction of the above at scale: outproducing the honest chain means out-spending the honest network, continuously. The burn is purchasing the trace gap itself.

The bundle is elegant and the bundling is the tax. Because one expenditure buys all four jobs, the expenditure must scale with the most demanding of them — unforgeability against a resourced adversary — and so the whole bundle is priced at security's schedule: the heat grows with the attacker it must outbid. The lottery design makes this concrete. Security is proportional to *total parallel work*, so every additional watt of adversary is answered with an additional watt of honest burn, forever, and the planetary tax is not an inefficiency to be engineered away but the direct image of the threat model. Of order 10²⁰ hashes per second are found and discarded so that ordering, randomness, and identity can be carried on unforgeability's back — three passengers billed at the fourth's fare.

## 3. The Unbundling

The program has already built the itemized alternative, though it built it for another purpose. The four anchors of *Gauge-Fixing the Section Space* fix four adversary freedoms — grinding, temporal, identity, multiplicity — and those freedoms are these jobs, seen from the forger's side. Re-read as a repricing of the mining bundle, with *The Wound Clock*'s amortization classes attached:

**Randomness goes to the beacon**, and its price goes to zero. Pulsar timing and the wheeling of stars deliver unpredictable, unbiasable public entropy that no coalition can hurry or precompute against — leader election's raw material, sky-funded, at no recurring cost to the mechanism. Bitcoin manufactures its unpredictability at 10²⁰ guesses per second; the sky emits it anyway.

**Ordering goes to the delay chain**, and this is where the repricing draws blood. A verifiable delay function certifies elapsed sequential time with *one* processor's worth of computation — the certificate is the single chain of squarings, verified in logarithmic time — where the lottery certifies it with a planet-wide parallel race. The energy gap is the point stated plainly: the temporal anchor of the unbundled construction dissipates on the order of a household appliance; Bitcoin's temporal ordering dissipates on the order of a mid-sized nation's grid. Both certify a past that cannot be cheaply refabricated. One of them is a clock; the other is a bonfire read as a clock.

**Individuation goes to the unique encoding** — slow, sequentially dependent, keyed to bearer and epoch — pricing the *distinctness* of each participant's contribution at per-identity sequential work rather than at network scale.

**Sybil pricing keeps the flame, and only Sybil pricing does.** The thin dissipation floor prices the minting of identities and is forbidden to do anything else; it is paid at entry, per identity — genesis-paid, amortizing over the identity's life — rather than per block forever. This is the honest residue of the burn: multiplicity is the one freedom for which no sky pays and no clock substitutes, because an identity that costs nothing makes every counting argument vacuous, and the only known price that cannot be minted is a physical one.

Under the unbundling, the mechanism's irreducible heat is: **the Sybil floor times the identity churn, plus one wound clock.** Not zero — the program does not deal in zero — but decoupled from the security schedule. The adversary who grows stronger is answered by anchors whose costs do not move: the sky does not burn hotter, the clock does not crank faster, and the conjunction (predict the light, parallelize the sequential, individuate the identical, pay to be counted) is what scales against the attacker, multiplicatively, in the Combination-Proof manner — by composition rather than by outbidding. The deployed world has a cousin of this design in the space-plus-time chains, which replace the burn with storage uniqueness and a delay chain; the program's construction differs in what it anchors but not in the accounting insight: *the lottery's fare structure was a choice.*

## 4. The Meter That Work Is Not

A caveat now, before the menu — because the question that prompted this paper asked about quantum mining, and the interesting answer is not the expected one.

The expected answer is short: Grover halves the effective bits of a hash search and is answered by doubling the parameter; quantum mining is a tax on the honest and forger alike, resets the difficulty, and changes nothing structural. *Borrowed Hardness* filed this already: unstructured hardness is taxed, never dissolved.

The unexpected answer concerns what proof of work *certifies*, and it comes from the second volume's own physics read one level deeper. Landauer prices **erasure** — logical irreversibility — and not computation. A computation embedded in a reversible circuit, quantum circuits being unitary by construction and classical reversible machines being Bennett's own construction, can in principle be run at dissipation approaching zero, paying instead in ancilla space, in time, and in hardware. Today's miners run six or more orders of magnitude above the Landauer floor of their own irreversible operations, and the floor itself is not load-bearing: it can be engineered *under*, asymptotically, by any party willing to trade heat for space and patience.

The consequence is a precision the corpus should adopt. Proof of work certifies **economic cost** — the hardware, the energy actually spent by the implementation at hand, the opportunity forgone — and only contingently certifies **heat**. The two have been coextensive for every miner yet built, and nothing guarantees they remain so. Bitcoin's security survives the decoupling untouched, because outbidding was always denominated in cost and cost survives reversibility (the reversible miner pays in capital and time what it saves in joules). What does *not* survive is any mechanism that reads a proof of work as a *proof of dissipation* — a joule meter — since the joules are the implementation's property and not the predicate's. The program's own dissipation floor is therefore respecified in one line: it is a **cost floor**, denominated in whatever the cheapest honest expenditure happens to be, and the word "dissipation" in its name is a description of present engineering, not of the security claim. The flame was never what the mechanism could see. The spending was.

## 5. The Menu

What may honestly be mined now states itself, because the criterion has been assembled across three papers. An honest minable is a **generative residue with a physically pinned trace gap**: a thing produced *in the making* and not readable off the output (*Sign and Work*'s species distinction), whose forgery cost equals its earning cost by law rather than by parameter (τ = 1), and which Volume V's biconditional closes on both sides — no work without the residue, no residue without the work.

The menu, exhaustively as far as the program can currently see:

1. **Parallel expenditure** — the hash lottery. τ = 1 because the search has no seam; the residue is the spending itself. (Certifies cost; contingently heat, per §4.)
2. **Sequential time** — the delay chain. τ = 1 because elapsed sequence cannot be parallelized or bought in bulk; the residue is the having-been-there. (*The Wound Clock*'s non-amortizable class; quantum-thinnest in its RSA-group form, repairable per *Borrowed Hardness*.)
3. **Storage uniqueness** — replication-style encoding. τ pinned by the sequential slowness of the encoding; the residue is the uniquely instantiated copy. (The gap is parameter-pinned rather than law-pinned, and the space-chains' history of plotting shortcuts and time-memory tradeoffs shows the pin needs maintenance.)
4. **Fission flux** — the reactor's antineutrinos. τ = 1 because no known process produces the spectrum except fission; the residue is of order 10²⁰ per second per gigawatt-thermal, and it cannot be shielded, the interaction length being light-years of lead. (*The Involuntary Ledger*'s nuclear channel, promoted from meter to mint.)

Everything off this menu is a proxy. Useful work is off the menu (its verifier is an oracle — the first volume's oldest result); stake is off the menu (circular at bootstrap); reported joules are off the menu (the meter is the oracle wearing steel). The menu's first three verify with mathematics — anyone checks the hash, the squaring proof, the encoding challenge, at negligible cost. The fourth verifies with *hardware*, and that difference is the whole subject of the next section.

## 6. The Worked Example: Minting Against the Flux

The fourth entry deserves working out, because it is the closest thing the physical world offers to a mined joule, and because working it out honestly locates exactly where the oracle survives.

**The design.** A fission plant mints coin in proportion to generated energy, attested not by its operator, its meter, or its regulator, but by its antineutrino flux, read by detectors it does not control. The flux is proportional to thermal power; the spectrum is producible by nothing but fission; shielding is physically impossible. To fake the certificate is to run the reactor — the forgery *is* the generation, τ = 1 by the weak interaction. The feasibility base exists: single-reactor monitoring at tens of metres is demonstrated technology, and one kiloton-scale instrument at a hundred and eighty kilometres read a nation's entire fleet power history through its shutdown, with no cooperation from the nation. The mechanism's remaining apparatus is the program's standard stack, now with something real to glue: N independent detector operators as the measurement cover, local flux readings as sections, the coherence layer certifying that they agree on overlaps, epochs seeded from the beacon, readings carried on a delay chain so the record has a past — each anchor doing exactly its §4 job and nothing else.

**The honest price, in two parts.** First: the verifying instrument is a **compressed oracle**, not an absent one. A detector is built, calibrated, and operated by someone; N independent detectors with published raw data and a gluing layer *compress* the trust — from "believe the operator's meter" to "believe that N mutually checking instruments were not all corrupted in concert" — and compression is a real reduction and not an elimination, the same species of result as the involuntary ledger's community-refereed sink models. The hash puzzle needs no such fleet; the difference between verifying with mathematics and verifying with hardware is the difference between an absent oracle and a compressed one, and a program that has spent five volumes on that distinction does not get to blur it in its own favourite example. Second: coverage. Fission is a few percent of planetary throughput; a flux mint is a mint for one channel, not for energy.

## 7. The Incentive Trap

There remains the failure that attestation cannot fix, and *Kar-Coin* named it before any of these instruments were on the table: a currency denominated on the outward ladder alone pays for magnitude irrespective of what the magnitude accomplishes — *a mechanism that rewards burning*.

Minting against generation — however unforgeably attested — is a subsidy on generation, and a subsidy on generation is Goodhart aimed at the planet: the perfect meter makes the perverse incentive *more* efficient, not less. The flux mint of §6 blunts the trap only contingently (fission fuel is costly and dispatch is demand-driven, so generating for the subsidy alone has a high floor), and a flare mint — equally attestable through the radiometric channel — would spring it outright, paying wattage for waste. The lesson is the paper's architecture, stated as a separation of concerns that Bitcoin's bundle and the naive joule-coin both violate:

**Security** is paid through the unbundled anchors of §3 — the Sybil floor and the clock — and has nothing to do with joules generated. **Denomination** — the unit of account, the rung — is read from the involuntary ledger's planetary aggregate, which needs no per-agent proof and rewards no one, being a measurement and not a payment. **Minting** — who receives issuance, and for what — is the rung of the attribution ladder where the oracle still stands, and where *what* is subsidized is a policy choice no attestation technology can make on the mechanism's behalf. The three were one thing in Bitcoin because the lottery happened to do all three at once. They are not one thing, and the program's constructions come apart along exactly these seams.

## 8. What Is Declined

**That the heat is eliminated.** It is re-let. The Sybil floor still burns; the clock still cranks; and the unbundled construction's hardware — detectors, storage, encoders — carries embodied energy paid at the factory rather than at the socket. The claim is that heat is decoupled from the *security schedule*, not that the mechanism is cold.

**That the unbundling is proven.** The conjunction of the four anchors has never been assembled and run against an adversary; *Gauge-Fixing* §6 declined this flattery for its own architecture and the decline is inherited whole. Bitcoin's bundle, whatever its fare structure, has sixteen years of hostile uptime; the itemized alternative has a test suite with one executed fragment.

**That reversible mining is a present concern.** §4's caveat is about what proof of work *certifies*, not a forecast of tomorrow's miners. Reversible computing at competitive throughput is far from engineering reality; the caveat's force is definitional — a mechanism should state that its floor is cost, because heat was always the implementation's property — and definitional force is the only kind claimed.

**That the flux mint is oracle-free.** §6 already priced it: compressed, not absent. Repeated here because the example is seductive and the program's discipline is exactly for seductive examples.

**That the menu is closed.** Four entries are what the program can currently pin. A fifth generative residue with a law-pinned gap may exist — the corpus has been surprised by its own vocabulary before — and the menu is a claim about what is *known* to qualify, falsifiable by the next entry.

## 9. Coda

The complaint said: the flame is the price. The accounting says: the flame is the receipt, and the price was set by a fare structure that billed three passengers at the fourth's rate. Unbundle the fares and what remains burning is small and honest — the cost of making identity cost something, the cost of winding the clock — while the sky pays for chance and the aggregate pays for denomination, involuntarily, the way everything in this program's late vocabulary pays: by casting shadows it cannot help.

And beneath the repricing, a correction the program owed itself: the burn was never a window onto joules. It was a window onto *spending*, and the joules were the era's way of spending — coextensive so far, separable in principle, already separable in the unitary machines the durability volume audited. The mechanism sees cost; physics collects it in whatever coin the implementation tenders. The universe spends itself, and every honest mechanism is a small tax on that spending, structured so the dishonest pay more. The art — this paper's whole content — is in writing the tax code so that the planet is billed for what security actually needs, and not for what a beautiful bundle happened to charge.
