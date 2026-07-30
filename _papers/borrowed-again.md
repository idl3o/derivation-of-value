---
layout: document
title: "Borrowed Again"
subtitle: "Post-Quantum Signatures and the Structure the Migration Keeps"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /borrowed-again/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-07-30
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Volume IV read the post-quantum migration as the program's founding operator performed at the crypto layer — borrowed structure abandoned for derived bulk. The standards say otherwise. NIST's primary signature algorithm rests on module lattices, which is structure, and the hash-based scheme that fits the volume's description is designated a backup. The migration moves between structures rather than away from structure, the difference is priced in bytes, and the hybrid the program already recommends turns out to be the operator it did not know it was applying."
status: "v0.1 · working draft"
order: 19
---

## Abstract

*Borrowed Hardness* identifies the post-quantum migration with the anthology's founding move: "away from structured hardness that Shor unravels, toward unstructured and physical hardness that Grover can only make more expensive." The conceptual sorting is sound and the empirical claim about the field is not. NIST's finalised signature standards are ML-DSA, resting on Module-LWE and Module-SIS, and SLH-DSA, resting solely on collision-resistant hash functions; the first is the designated primary and the second is designated a backup "in case ML-DSA proves vulnerable," and the forthcoming FN-DSA is lattice-based over NTRU. Two of three rest on algebraic structure. So the migration abandons the structure *Shor* exploits and adopts different structure, rather than moving to bulk — and the volume's tidiest claim, that the quantum adversary sorts borrowed from derived and the field is following that sorting, holds for what was abandoned and not for what was chosen. The paper then finds the sorting alive *inside* the lattice family, where plain LWE, Module-LWE and Ring-LWE form a gradient of increasing algebraic structure and increasing efficiency, and where Module-LWE exists precisely as a hedge against attacks exploiting ring structure. **Efficiency is bought with structure, and structure is what the volume calls borrowed.** The price of derivation is measurable: SLH-DSA signatures run 7,856 to 49,856 bytes against ML-DSA's 2,420 to 4,595, so between two and ten times the bandwidth. Finally, the hybrid lattice-and-hash construction that Kar-Coin already specifies is re-read: not belt-and-braces engineering but a deliberate straddle of the program's own line, and the first place in the corpus where the operator was applied before it was recognised.

---

## 1. Where Volume IV Is Too Neat

The durability volume's central device is a sorting. Shor dissolves hardness that comes from exploitable structure; Grover merely taxes hardness that comes from bulk; therefore number-theoretic hardness is *borrowed* and hash and physical hardness are *derived*. The volume then makes an identification which is the most satisfying sentence in it:

> "The anthology's founding move — from a borrowed quantity to a derived substrate — is, read at the level of cryptographic primitives, exactly the post-quantum migration the field is now undertaking: away from structured hardness that Shor unravels, toward unstructured and physical hardness that Grover can only make more expensive."

The first half of that is right. The second half is a claim about what the field actually chose, and it is worth checking, because the volume rests a good deal on the migration being a *confirmation* of the operator rather than merely compatible with it.

It does not check out. The field abandoned the structure Shor exploits and adopted different structure.

---

## 2. What the Standards Rest On

NIST concluded an eight-year process in August 2024 with three finalised standards, two of them signature schemes [1].

**FIPS 204 — ML-DSA**, the Module-Lattice-Based Digital Signature Algorithm, formerly CRYSTALS-Dilithium. Security rests on the Module Learning-With-Errors and Module Short-Integer-Solution problems. It is the **designated primary** standard for digital signatures.

**FIPS 205 — SLH-DSA**, the Stateless Hash-Based Digital Signature Algorithm, formerly SPHINCS+. Security rests *solely* on collision-resistant hash functions. It is designated as a **backup**, in NIST's framing, in case ML-DSA proves vulnerable.

**FIPS 206 — FN-DSA**, from FALCON, is in draft: hash-and-sign over NTRU lattices, using fast-Fourier sampling for Gaussian trapdoors. Lattice-based again.

So of the three signature standards, one is derived hardness in the volume's sense and two are structured, and the structured one is the default. A protocol following the standards as written signs with a lattice.

**The volume's identification therefore needs qualifying rather than withdrawing.** Shor is a solvent for *particular* structures — the multiplicative structure of the integers, the group structure of a curve — and lattice hardness survives because no comparable quantum algorithm is known for it, not because it lacks structure to exploit. Module-LWE is an algebraic assumption. It is a different bet, not the absence of one.

There is a compensating observation, and it is the more interesting half. **NIST's stated reason for standardising SLH-DSA is exactly the volume's argument.** A scheme is held in reserve whose security rests on nothing but hash functions, precisely because the primary scheme's structure might turn out to be exploitable. The standards body performed the program's sorting — diversify away from structure in case the structure is a loan — without the vocabulary, and arrived at hedging rather than at migration.

---

## 3. The Sorting Runs Inside the Lattice Family

The distinction the volume draws between borrowed and derived does not stop at the boundary of post-quantum cryptography. It reappears inside it, along a gradient the field has already named.

Ring-LWE rests on the approximate shortest-vector problem over *ideal* lattices — lattices carrying algebraic structure related to the ring of integers of a number field. That structure is what makes the schemes fast, and it is also what has drawn scrutiny: weak instances of Ring-LWE have been characterised precisely by exploiting the ring structure, and those instances are not covered by the worst-case hardness theorems that give lattice cryptography its reputation for solid foundations.

Module-LWE exists as a response. It is described in the literature as a middle ground that "can resist potential attacks exploiting the algebraic structure of rings," offering more security than Ring-LWE while remaining more efficient than plain LWE, with the module rank as a tunable dial. Plain LWE sits at the far end: least structure, least efficiency, most conservative.

Read through the volume's operator, this is a ladder from derived toward borrowed:

| | structure | efficiency | in the volume's terms |
|---|---|---|---|
| plain LWE | least | worst | nearest to derived |
| Module-LWE | some | good | the hedge |
| Ring-LWE | most | best | nearest to borrowed |
| hash-based | none exploitable | worst by far | derived |

**Efficiency is bought with structure, and structure is what the volume calls borrowed.** That is a sharper statement of the tradeoff than the volume made, and it makes the choice of primitive a case of the framework's own substrate-selection problem rather than an implementation detail.

**The price of derivation is measurable.** ML-DSA signatures run 2,420 to 4,595 bytes. SLH-DSA signatures run 7,856 to 49,856. So refusing algebraic structure costs between roughly two and ten times the bandwidth, per signature, forever. That is what derivation costs at this layer, and it is the first place in the program where the preference for derived over borrowed has a number attached rather than an argument.

It also has a second-order benefit the program should notice. *The Multiplicity Freedom*'s second hypothesis is a positive resource floor — the cost of minting an identity. Signature size is part of that cost. **Choosing the derived primitive raises the Sybil floor as a side effect**, which is a small effect and points the same way as the main one.

---

## 4. What a Signature Actually Attests

*Sign and Work* opened by listing signatures among the traces that cost nothing like what they purport to evidence: "A signature is a trace. A logged claim is a trace. Neither costs anything like what it purports to evidence." That is right and it can now be made precise with that paper's own instrument.

A signature has an unusually clean trace gap, and it is *two different numbers depending on what is claimed*.

For the narrow claim — **the holder of this key assented to this message** — the trace gap is τ ≈ 1, and this is what a signature scheme's security *is*. Forging costs what holding the key costs, which is the definition of unforgeability. Signatures are excellent residue for exactly one proposition.

For any broader claim — that the signer did the work, holds the stake, measured the quantity, is a distinct person — the trace gap is τ ≈ 0. The key operation is unrelated to the labour, so the signature can be produced without it at negligible marginal cost.

**The gap between those two numbers is where mechanisms leak.** A signature binding an identity to a stake attests assent and is read as attesting the stake. *Borrowed Hardness* lists "the signatures that bind an identity to a stake" among the plumbing to be re-based, and plumbing is exactly the wrong category: given *The Multiplicity Freedom*'s dependence on the identity gauge, the signature layer is where the Sybil bound's hypotheses live or die, not a detail beneath them.

---

## 5. The Hybrid Was the Operator

Kar-Coin specifies hybrid signatures — lattice-based with hash-based in reserve — and *Borrowed Hardness* endorses the choice as foregrounding the migration. Both present it as prudence: two schemes, in case one breaks.

Read with §2 and §3 in hand it is something better. The hybrid straddles the program's own line, pairing a fast structured primitive with a slow unstructured one so that the borrowed half carries the traffic and the derived half carries the guarantee. That is not belt-and-braces. It is the operator applied at the primitive layer, made before the layer had been examined, and it is the only place in the corpus where the right answer was reached before the argument for it existed.

Which suggests the recommendation the corpus should actually carry. Not *migrate to post-quantum signatures*, which the standards make ambiguous between two very different bets, but: **sign with a structured scheme where throughput demands it, and anchor with an unstructured one wherever the mechanism's security claims are load-bearing** — the identity gauge above all, since that is where the program's only theorems have their hypotheses.

---

## 6. What Is Declined

**That lattice cryptography is unsound.** Nothing here suggests it. Module-LWE has worst-case-to-average-case reductions that number-theoretic assumptions never had, and the scrutiny it has received is heavy. The claim is narrower and only about categories: it is a *structured* assumption, so it sits on the borrowed side of the volume's own line, and the volume should not have counted the migration as a straightforward confirmation of its operator.

**That Volume IV's sorting is wrong.** The Shor/Grover asymmetry stands and the borrowed/derived distinction stands. What is corrected is a claim about the *field's chosen direction*, which turns out to be a hedge across the line rather than a crossing of it.

**Any quantitative security comparison.** The byte counts are the standards' own. No claim is made here about the relative likelihood of a break in Module-LWE versus in a hash function, which is exactly the judgement the standards bodies are paid for and this program is not.

**That τ ≈ 1 for the narrow claim is a proof.** It restates unforgeability in *Sign and Work*'s notation. Whether the trace-gap framing adds anything to standard definitions, beyond making signatures commensurable with other traces, is not established.

**Anything about implementation.** No scheme is deployed, benchmarked, or audited here.

---

## 7. Open Problems

**7.1. Where does the identity gauge need derived hardness?** *The Multiplicity Freedom* rests on duplication-boundedness, which rests on a unique encoding keyed to the bearer, which rests on a signature. If that signature is structured-hard, the Sybil bound inherits a structured assumption. Establishing which of the program's theorems depend on which primitive class is a bookkeeping exercise with real consequences.

**7.2. Does the VDF exposure interact?** *Borrowed Hardness* names the verifiable-delay chain the most quantum-fragile load-bearing piece, and the repairs on offer — class groups, isogenies — are *also* structured algebraic assumptions, unbroken rather than proven. So the program's two most exposed components would both be re-based onto structure. Whether an unstructured delay function is possible at all is a question worth asking; the negative answer would be worth having explicitly.

**7.3. Statefulness as provenance.** The stateful hash-based schemes, XMSS and LMS, buy smaller signatures with a requirement never to reuse state. Statefulness is a temporal property, and the program has a temporal anchor. Whether the delay chain could discharge the state-management burden that keeps stateful schemes out of general use is speculative and cheap to think about.

**7.4. Signature size and the resource floor.** §3 notes that larger signatures raise the Sybil floor. Quantifying that — how much of a resource floor a 50 KB signature actually constitutes against an adversary with bandwidth — would tell whether the effect is a curiosity or a design lever.

---

## References

[1] National Institute of Standards and Technology. *FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA).* Finalised August 2024. FIPS 206 (FN-DSA, from FALCON) in draft.

[2] V. Lyubashevsky, C. Peikert, and O. Regev. *On Ideal Lattices and Learning with Errors Over Rings.* EUROCRYPT 2010; Cryptology ePrint 2012/230.

[3] Sizes and hardness assumptions as given in the standards: ML-DSA 2,420–4,595 bytes on Module-LWE/Module-SIS; SLH-DSA 7,856–49,856 bytes on collision-resistant hashing alone.
