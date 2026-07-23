---
layout: document
title: "Borrowed Hardness"
subtitle: "Volume IV"
eyebrow: "An Anthology · Volume IV"
permalink: /anthology/borrowed-hardness/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-07-23
license: "CC BY 4.0"
label: "Anthology · Volume IV"
blurb: "The durability volume. The quantum adversary does not pose a new problem — it reveals which of the program's hardnesses were borrowed. A substrate-by-substrate audit of what survives the machine, and the operator recovered one last time at the cryptographic layer."
status: "v0.1 · working draft"
order: 10
---

The first volume made a promise it did not keep, and this volume is the keeping. It said that a staked structural property survives regime change because its meaning is not borrowed — that quantum computers, when they arrive, will not change what coherence is, and the end of fiat will not alter the second law. Every word of that is true and it is not the whole truth, because a mechanism is never only its substrate. It is a substrate *and an attestation of it*, and while the substrate's meaning may be beyond the reach of any machine, the attestation is only ever as durable as the cryptographic primitive it rests on. The quantum computer is a machine built, more than for anything else, to find that primitive and dissolve it. Durability, it turns out, comes in two layers, and only the lower one is free.

---

*Two Machines*
{:.section-title}

There are, for our purposes, exactly two quantum algorithms, and the difference between them is the argument of this volume.

The first is Shor's, from 1994: a method that factors integers and computes discrete logarithms in polynomial time on a quantum computer. It is catastrophic and it is specific. Everything that secures the present internet by the difficulty of factoring or of the discrete logarithm — RSA, Diffie–Hellman, the elliptic-curve signatures under every blockchain now running — falls to it completely, not by degree but by kind. A 256-bit elliptic curve does not become a weaker curve. It becomes arithmetic.

The second is Grover's, from 1996: a method that searches an unstructured space of size N in about √N steps. It is universal and it is mild. Against a hash function, against a symmetric cipher, against any hardness that comes from sheer bulk with no structure to exploit, Grover offers a quadratic speedup and nothing more — it halves the effective security, turning a 256-bit hash into the equivalent of a 128-bit one, and the response is simply to double the parameter and continue. Grover is a tax. Shor is a solvent.

The asymmetry is the whole story. Shor devastates hardness that comes from *structure* — the multiplicative structure of the integers, the group structure of a curve — because a quantum computer is precisely a machine that can be tuned to a structure and made to resonate with it. Grover barely dents hardness that comes from *the absence of structure*, because there is nothing for the machine to tune itself to. A hash is hard because it is a mess; a mess has no seam; and Grover, finding no seam, is reduced to searching, only faster.

---

*Borrowed and Derived, Again*
{:.section-title}

The reader who has come this far will hear the operator turning underneath, because it is the same one, at a layer the anthology had not yet examined.

Number-theoretic hardness is *borrowed* hardness. RSA is difficult because factoring is difficult, and factoring is difficult because of a structure — deep, elegant, and, as it turns out, exploitable by the right machine. The security was real, and it was on loan. It held for exactly as long as no one built the device that trades in that particular structure, and Shor is that device. This is, at the cryptographic layer, precisely the move the first volume diagnosed in proof of stake: a quantity whose value is borrowed from a market the protocol assumes will persist. Number-theoretic hardness borrows its difficulty from the assumption that the structure it rests on will never be efficiently inverted — and that assumption is a market that quantum computing has come to make.

Hash hardness, and physical hardness, are *derived*. They rest on no exploitable structure — only on bulk, on the second law, on the irreducible cost of sequential time. A machine cannot tune itself to what has no structure to tune to, and so these hardnesses are taxed by Grover but never dissolved by Shor. The anthology's founding move — from a borrowed quantity to a derived substrate — is, read at the level of cryptographic primitives, exactly the post-quantum migration the field is now undertaking: away from structured hardness that Shor unravels, toward unstructured and physical hardness that Grover can only make more expensive. The quantum adversary introduces no new problem to the program. It performs a sorting. It walks through every construction and separates the hardnesses that were borrowed from the hardnesses that were derived, and it dissolves the first kind, and it leaves the second kind standing, more costly and intact.

---

*The Audit*
{:.section-title}

So run the machine down the substrates and mark, in each, where it bites.

*Coherence* is the easy case, and instructively so. Its scoring is mathematics — the dimension of a kernel, the spectrum of a Hodge Laplacian, the vanishing or not of a cohomology class. Mathematics is quantum-invariant; a Hodge decomposition reads the same on any hardware ever to be built, because it is a fact about a vector space and not a computation anyone must be prevented from performing. The exposure is entirely in the plumbing — the commitments that bind a miner to its output, the signatures that bind an identity to a stake, the hashes that fix the simplicial complex against tampering. Re-base those on lattice signatures and hash-based commitments and proof of coherence crosses the quantum threshold with its property untouched. The one subtlety worth naming is the capability gap: the mechanism is Goodhart-*asymptotic*, its security living in the distance between what a miner can do and what faking the conjunction would require, and a quantum adversary raises the floor under both. But that shifts a parameter; it does not break a property. The coherence of many models is not a number-theoretic assumption. It is a structural fact, and structural facts do not factor.

*Negentropy* is where the machine draws blood, and honesty requires naming the wound precisely. The anchoring construction fixed the adversary's four freedoms with four anchors, and they do not all fare alike. The astrophysical beacon is physics — pulsars keep their time regardless of what we build, and Shor has no purchase on a star. The dissipation floor is proof of work, Grover-taxed and surviving with adjusted difficulty. The unique encoding is sequential hashing, Grover-weakened and parameter-hardened, and it holds. But the delay chain is the exposure, and it is real and load-bearing. The verifiable delay functions that certify elapsed sequential time are built from repeated squaring in a group whose order must be hard to know — and in the RSA groups first reached for, the order is exactly the quantity Shor computes, which collapses the whole sequential labour to a shortcut and turns a certificate of having-waited into a thing that can be forged instantly. The temporal gauge — the anchor that fixes backdating, that makes provenance more than a signature — is the single most quantum-fragile load-bearing piece in the program. The repair is known: square instead in the class group of an imaginary quadratic field, where no efficient quantum algorithm for the order is known, or move to an isogeny-based delay. But the repair is not free, and it is not *proven* quantum-secure, only unbroken; and a durability volume that failed to mark the temporal anchor as the place the negentropy construction is thinnest would be exactly the flattery the program forbids.

*Omnium* is the cheapest crossing. Its kernel is conservation and a product space — pure arithmetic, invariant to its core — and its only cryptographic exposure is where it touches a chain: Merkle proofs that Grover merely taxes, transfer signatures a lattice scheme replaces. The value-vector depends on almost nothing that was borrowed, and so it carries across the threshold at almost no cost.

*Kar-coin*, alone of the four, was built post-quantum from its first page — hybrid lattice-and-hash signatures, the migration its founding concern rather than an afterthought. And yet its durability gap is the widest of all, because it is not cryptographic. It is the oracle problem the capacity volume named: the spoofed meter, the relabelled joule, the institution asked to vouch. No quantum machine makes a false energy claim more or less true. Kar-coin hardened, with great care, the layer that was easy to see, and inherited whole the layer that was hard. That is its own kind of lesson about where durability is actually won.

---

*What the Machine Cannot Reach*
{:.section-title}

Beneath every attestation lies the substrate itself, and the substrate is where the machine stops.

Coherence is a property of the relations among many models of the world, and it will be that on any hardware, in any century, under any adversary, because it is not a computation to be outrun but a structure to be exhibited. Negentropy is the distance between a system and its thermal grave, and the second law is not a cryptographic assumption awaiting its Shor — it is the most tested regularity in physics, and no machine has ever been permitted to violate it, quantum or otherwise. The order of magnitude at which a civilization can act is simply what it is. This is the exact and defensible form of the claim the first volume made too quickly: the substrate is durable *by derivation*, automatically, for free, because its meaning was never on loan; the attestation is durable only *by engineering*, and must be re-based, primitive by primitive, onto hardness that was derived rather than borrowed. The good news the audit delivers is that in every case the engineering has a known direction, even where the labour is undone and even where — as at the negentropy construction's temporal anchor — the direction leads somewhere not yet proven safe. The program is not immune to the machine. It is, substrate by substrate, *re-basable* against it, which is the most any honest mechanism can claim and more than most can.

---

*Coda*
{:.section-title}

This volume closes the arc that was visible from the first — the operator named, applied across three substrates, handed to a machine, and now held up to the sharpest reader it will ever have. It does not close the anthology. The first volume's coda said the volumes beyond these had shapes not yet drawn, and they still do: the security proof the third volume left open, the construction the third volume specified and did not yet build, the substrates the program has not yet learned to name. But the spine now stands complete, and it stands in a shape the author did not fully see at the outset and can see now — that the same single move recurs at every layer it examines, from the substrate of stake down to the hardness of the primitive that attests it.

The universe spends itself. Borrowed hardness dissolves the moment the machine tuned to its structure is switched on. What does not dissolve is what was never borrowed — physical law, raw bulk, the irreducible cost of sequential time, the structural properties a ledger can measure by being many witnesses checking each other across the very time the machine cannot fold. To derive value has meant, throughout, to stake the underived; and the quantum adversary, which the anthology feared it would have to answer as an objection, turns out to be the operator's best confirmation, a device that goes through the world separating the borrowed from the derived and hands back, refined and intact, exactly the substrates the program was built to name. It was written, from its first sentence, to be read by that machine. The reading has begun, and the anthology proceeds — toward the constructions it still owes, and the century it was made to survive.
