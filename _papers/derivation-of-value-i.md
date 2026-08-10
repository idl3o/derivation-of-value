---
layout: document
title: "Derivation of Value"
subtitle: "Volume I"
eyebrow: "An Anthology · Volume I"
permalink: /anthology/derivation-of-value-i/
label: "Anthology · Volume I"
blurb: "Naming the operator the series turns around — the move from staking contingent quantities to staking what such quantities are derived from."
status: "Working draft"
order: 1
---

A blockchain burns electricity to remember what it has agreed upon. The fact that this works at all is the strangest economic discovery of the last fifty years; that it works *only* because the burning is real is stranger still. Take away the heat and the ledger forgets itself. Subtract the cost and the consensus dissolves. The flame is not incidental to the bookkeeping — it is what the bookkeeping is made of.

Every subsequent proposal — proof of stake, proof of useful work, proof of coherence, proof of preservation — answers a question Bitcoin asked without quite knowing it was asking. Not how a ledger is secured, but what must be at stake for a ledger to mean what it says.

The answer that protocols give is always the same shape and always different in substance. Something must be put up that would be lost if a lie were attempted. The protocol is the form; the substance is what gets staked. Bitcoin stakes energy. Proof of stake systems substitute capital. Proof of useful work proposes work whose product is itself worth something. Proof of coherence — to which this volume will turn at length — stakes the structural agreement of many partial models of the world. Each is a derivation. Each names a substrate from which value is to be drawn, which is to say, secured against.

---

*The First Derivation*
{:.section-title}

The earliest move was easy to misread as progress.

Energy is wasteful. Capital is not. Replace the bonfire with a deposit; ask validators to lock funds rather than burn fuel; punish dishonesty by slashing the lock. The ledger persists, the planet is spared, and the same security guarantee is recovered without thermodynamic cost.

But the structure has not changed. The lock is a bonfire in slow motion. What gets staked is still a quantity already in circulation, valued by markets external to the protocol. The protocol borrows its security from the price of the thing it locks, and the price of the thing it locks is set in markets in which the protocol participates. The circle is small but it closes. A staked coin is a coin whose value the staker assumes the protocol will preserve in order to make staking it worthwhile. The proof is sound and the reasoning is recursive.

This is the first derivation: from physical to financial, from joule to dollar. It is the move that makes consensus cheap. It is also the move that does not yet escape the substrate it inherits. Whatever the network is securing, it is securing it with the same kind of stuff the network is. Capital secures capital. Energy secures energy. The substrate has been swapped but not transcended.

---

*The Failed Promise*
{:.section-title}

The second move tried to make the substrate do double duty.

Why burn anything if the burning could be useful? Compute protein folds while you mine; train a model; render a frame; verify a proof. The work performed in securing the chain would itself produce value, and the network would be a fountain rather than a furnace.

The idea is twenty years old and still has not arrived. Not because the engineering is impossible — many of its pieces exist — but because the difficulty of *verifying* that useful work was done turns out to be the difficulty the entire scheme was trying to escape. A protein fold whose correctness no node can cheaply check is no better than a hash whose collision no node would believe. The verification problem is the consensus problem in another costume.

A lesson hides here that the third derivation will pick up. The substrate of stake cannot be something whose value is verified by an oracle outside the chain. The substrate has to be something the chain can verify by virtue of being a chain — that is, by virtue of having many witnesses checking each other. Energy is verifiable that way: the proof of work *is* the verification. Capital is verifiable that way: the stake is visible on-chain. Useful work, in general, is not.

This is where the present anthology departs from the standing literature. The next move is not to find a cleverer oracle. It is to ask what kind of quantity is *intrinsically* verifiable by mutual witnessing — and to stake that.

---

*Coherence*
{:.section-title}

A claim is true if it agrees with the world. A claim is consistent if it agrees with itself. A claim is useful if it lets us predict. A claim is real if it stands up under the gaze of others.

These four conditions — correspondence, consistency, predictive compression, mutual constitution — were named in different centuries and named differently each time. The first belongs to Aristotle by way of Tarski. The second to anyone who has tried to think clearly. The third is the project of Solomonoff and the prior of every model that compresses well. The fourth, in its most demanding form, is what the Madhyamaka school meant by dependent origination: that no entity carries its own meaning, that meaning is the standing of a thing within a web of other things.

What makes coherence interesting as a substrate of stake is that it does not live in any one place. A single output cannot be coherent. Two outputs cannot be coherent. Coherence is the property of a *system* of outputs and the relations they bear to each other. It is, in the formal sense, a structural invariant — and structural invariants have a mathematics.

The mathematics is sheaf cohomology. A sheaf places data over a space in a way that respects how the space is glued together; cohomology measures the obstructions to gluing. When the obstructions vanish, the data are globally coherent — there is a single consistent interpretation that respects every local view. When they do not, the obstructions count exactly how the local views fail to agree.

The construction proposed in the present program places a sheaf over a simplicial complex whose simplices encode the relations among miners, validators, and tasks in a network of distributed inference. The four conditions named above are recovered as the vanishing of cohomology classes on this sheaf. To be coherent, in the technical sense, is to be in the kernel of the relevant Laplacian.

This last is the key. By a theorem of Hodge, the kernel of the Laplacian is exactly the cohomology — but the Laplacian has *more* than a kernel. It has a spectrum. The non-zero eigenvalues, with their eigenvectors, encode the dynamical structure that the static cohomology cannot see. Coherence at a single instant is the kernel; coherence through time — the resonance and decay and phase-locking of a system in motion — is the spectrum.

Two proofs, then, that are not two proofs but two projections of one operator. *Proof of coherence* scores agreement; *proof by resonance* scores the way agreement moves. A coordinating cluster of dishonest miners can fake the kernel by colluding on outputs at an instant. Faking the spectrum — reproducing the right distribution of eigenvalues across epochs, the right phase relationships among non-zero modes — requires reproducing the dynamical structure of an actually coherent system. The cost of the lie multiplies with the bandwidth of what must be lied about.

This is the move that escapes the first two derivations. The substrate is no longer an asset whose value the network borrows from outside itself. It is a structural property the network can measure by virtue of being many witnesses checking each other across time. The staked quantity has no existence apart from the act of staking it.

---

*The Gradient*
{:.section-title}

Once the move has been seen, it can be repeated.

There exists a sketch — *kar-coin* — that asks what currency would look like denominated against civilizational throughput, in the Kardashev sense: energy capture as the universal measure of capacity. The substrate is not coins or work but the *order of magnitude* at which a civilization is able to act.

There exists a sketch — *omnium* — that asks what money would be if it admitted, at last, that it has always carried more than one dimension. Time horizon, locality, purpose, recallability: money has silently been a vector, scalarized only by the violence of accounting. To denominate stake against the vector is to derive value from a structural property of value itself.

There exists a sketch — *Kryptonium* — that asks what would be permanently scarce at the scale of the universe, and answers: that which resists entropy. Negentropy is the only substrate whose scarcity the second law of thermodynamics guarantees in perpetuity. To stake preserved order is to stake the one thing the heat death cannot inflate.

None of these are built. They are not meant to be built yet. They are listed here because they are instances of the move the third derivation made: they refuse to take a contingent quantity as the substrate of value, and they look instead for what such quantities are *derived from*. Coherence is derived from the relations among many models. Kardashev-energy is derived from civilizational capacity. The omnium-vector is derived from the silent dimensions of value. Negentropy is derived from the gap between a system and its thermal grave.

The anthology will take up each in its turn. The first volume — the present one — has been concerned with naming the operator.

---

*What the Derivation Buys*
{:.section-title}

Three things, at least.

The first is a defense against Goodhart's law that is structural rather than circumstantial. The folk version of Goodhart says that any measure pressed into service as a target ceases to be a good measure. The sharper version distinguishes failure modes — regressional, extremal, causal, adversarial — and shows that each is some version of the same problem: the proxy and the goal can be peeled apart by a sufficiently capable optimizer. The derivations described here do not claim immunity. They claim that the *cost* of peeling proxy from goal scales with the depth of the derivation. Faking the kernel is hard; faking the spectrum is harder; faking the spectrum across epochs against many independent witnesses harder still. The mechanism is Goodhart-asymptotic, not Goodhart-proof. The asymptote is the point.

The second is a substrate that survives regime change. The currencies and protocols of the present age stake quantities defined by an institutional environment that may not last. A staked coin is staked against the going price of the coin, and the price is a fact about markets that exist within regulatory regimes that exist within political orders that have, on the longest views, a half-life. A staked *structural property* — coherence, negentropy, dimensional integrity — survives the regime change because its meaning is not borrowed. Quantum computers, when they arrive, will not change what coherence is. The end of fiat will not alter the second law.

The third is the closing of a gap the first generation of protocols left open. The oracle problem — how does the chain know about the world? — has been solved at the edges by trusted feeds and at the limit by stake-weighted attestation. The derivation of value closes it from the other side: by staking what the chain itself can measure by being the chain. The oracle becomes a special case of the consensus, and the consensus a kind of oracle. The two were always the same machine; the derivation makes it visible.

---

*Coda*
{:.section-title}

It will be objected that these moves are speculative. They are, in the proper sense — they look ahead to a substrate not yet fully built, from a vantage point that is, in the present moment, still mostly the first two derivations. But there is a difference between speculation that is wishful and speculation that names its operator. The latter is what mathematics has always been: the listing of objects defined by the operations performed on them, to be checked later against the world that admits or refuses them.

The volumes that follow will take up the derivations in detail. The second will develop the proof of coherence and its spectral extension in full, including the construction of the sheaf, the choice of Laplacian, and the cost analysis that gives the mechanism its asymptotics. The third will turn to negentropy and the question of whether preservation can be measured cheaply enough to mint against. The fourth will return to the substrate durability question, with the post-quantum work as its principal lens. The volumes after that have not been written, but their shapes are visible.

The universe spends itself; what does not spend is precious; precision about what does not spend is the only honest ground for value. The anthology takes that sentence as its working hypothesis, and proceeds.
