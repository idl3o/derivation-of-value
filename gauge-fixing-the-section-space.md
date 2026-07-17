---
layout: paper
title: "Gauge-Fixing the Section Space"
subtitle: "Anchoring Architectures for Negentropy-Attested Mechanisms"
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-07-17
license: "CC BY 4.0"
---

# Gauge-Fixing the Section Space
### Anchoring Architectures for Negentropy-Attested Mechanisms
*Derivation of Value — v0.1*

---

## Abstract

A mechanism that pays for order must first answer a question older than mechanisms: how does one certify that order was made, and made *here*, and made *by this hand*? Cryptography, it turns out, can certify none of these directly. It certifies dissipation, sequence, uniqueness, and coherence — four shadows that order casts, never the thing itself. This paper argues that the correct response is not to search for a proof of negentropy, which does not exist, but to compose anchors so that each eliminates one gauge freedom of the adversary, until the only global sections surviving the quotient are honest ones. The sheaf-cohomological consistency layer is retained as the correct gluing formalism; its known blindness — that H¹ = 0 certifies coherence, not truth — is repaired not by strengthening the cohomology but by engineering the forger's section to be non-glueable by construction. Four anchors are specified: an astrophysical randomness beacon, a verifiable delay function chain, replication-style unique encoding, and a thin dissipation floor. Their composition is a conjunction, not a hope.

---

## 1. What Cryptography Can Attest

Every proof system in the cryptographic canon — hash puzzles, succinct arguments, verifiable functions — proves statements about bitstrings and computation. The only physical quantity such a system can certify is dissipation, and only as a lower bound, by way of Landauer. Proof-of-work succeeds because its predicate is self-verifying and its physical correlate follows from thermodynamics without a witness.

Note the direction of the arrow. One can prove that free energy was *spent*. One cannot prove that order was *created somewhere*, because entropy accounting requires a boundary, and the boundary is precisely the adversary's free parameter. For any control volume within which entropy appears to fall, there exists a redrawing under which the export of disorder is hidden. The predicate

> *P: ΔS < 0, attributable to agent X, within boundary B*

is not self-certifying, and the second law guarantees a relocation attack against B. This failure precedes any choice of mathematical machinery. It is not a flaw in the sheaf formalism; it is a fact about what proofs are.

The consequence is architectural. No single certificate of "negentropy harvested" will be found, because none exists. What exists instead is a family of certifiable *shadows* — elapsed sequence, physical uniqueness, mutual coherence, entry cost — and the design problem is to arrange these shadows so that only genuine order can cast all of them at once.

## 2. Coherence Is Not Truth

Suppose negentropy claims arrive as heterogeneous local measurements: oracle feeds, validator observations, instrument attestations. The correct formalization of their mutual consistency is a cellular sheaf 𝓕 over the nerve of the measurement cover. Local sections must agree on overlaps; H⁰(𝓕) is the space of globally consistent assignments; H¹(𝓕) measures the obstruction to gluing.

This construction performs a genuine security reduction. "Trust each oracle" becomes "trust that no coalition can lie consistently across all overlaps," and the reduction is quantitative: the cost of a consistent coalition lie scales with the spectral gap of the sheaf Laplacian over the cover. A sparse nerve yields a small gap and a cheap coalition; an expander-like nerve prices mimicry at the spectrum. The design target for the gluing layer is therefore stated in one line: *maximize the Laplacian spectral gap of the measurement cover.*

But the reduction certifies coherence, not truth. A coordinated fabrication is a perfectly good global section; the sheaf condition is satisfied by any consistent lie, and cohomology is blind to the difference, being functorial under substitution of sections. Duplicated sections glue as well as honest ones. Prior work in this anthology established the same theorem in different clothing: copy-symmetry is intrinsic to any state-functional reward, and spectral mimicry is structurally unavoidable at the consistency layer. Cohomology detects torsion *between* views; it cannot manufacture asymmetry between an honest section and its forgery.

## 3. Copy-Symmetry as Gauge Freedom

It clarifies matters to name the adversary's degrees of freedom as gauge freedoms of the section space:

1. **Temporal gauge** — a section may be fabricated at any time and backdated; nothing in its content records when it came to be.
2. **Grinding gauge** — a section may be optimized against known challenges before they are posed.
3. **Identity gauge** — a section may be duplicated; informational content does not individuate its bearer.
4. **Multiplicity gauge** — identities themselves may be minted freely; the coalition bound of §2 is vacuous if membership is costless.

An honest section is one produced by a real observer, in real time, in response to a real challenge, exactly once. Each clause of that sentence names one gauge freedom. The anchoring problem is therefore not certification but *gauge-fixing*: quotient the section space by four symmetries so that the surviving equivalence classes are honest by elimination.

## 4. The Four Anchors

### 4.1 The Beacon (fixing the grinding gauge)

Pulsar timing arrays and the stellar orbits of Sgr A* furnish randomness that is unbiasable, unpredictable, and globally observable — public entropy, delivered by photons that no coalition can hurry. Their correct role is *challenge source*, not measurement. Each epoch's challenges are seeded from the beacon; fabricated sections cannot be precomputed against challenges that do not yet exist.

The inversion should be stated plainly, since an earlier design intuition ran the other way: the cosmos supplies entropy *to* the mechanism; it does not certify negentropy *within* it. There is an apophatic structure here worth preserving in the margin — the anchor works precisely by being what the system cannot say about itself.

### 4.2 The Delay Chain (fixing the temporal gauge)

Verifiable delay functions — Wesolowski or Pietrzak constructions — certify elapsed sequential time: the one resource that cannot be parallelized, purchased in bulk, or retroactively fabricated. Each section carries a VDF chain rooted in the epoch beacon; the chain is a certificate of *having-been-there*.

This resolves, in the affirmative and toward provenance, the fork left open at §4.2 of the Proof of Coherence whitepaper. Copy-symmetry is at bottom a statement that two sections are indistinguishable *now*. A delay chain renders indistinguishability-now irrelevant: the mimic can copy a state but cannot copy a history. Provenance without sequentiality is merely signatures, which coalitions forge; provenance with sequentiality is physics.

### 4.3 Unique Encoding (fixing the identity gauge)

The underweighted anchor, and the one that lets cohomology do real security work. Replication-style proofs solved an isomorphic problem: rendering two copies of identical data cryptographically distinct. A slow, sequentially dependent encoding — SDR-style, or a verifiable delay encoding — binds each section to a unique physical instantiation, keyed to the validator's identity and the epoch beacon, *before* the section enters the sheaf.

The consequence is structural rather than economic: a mimicked section, lacking the correct encoding key, fails to satisfy the restriction maps and therefore *glues inconsistently by construction*. The forger's section is engineered to be non-glueable. What was previously an economic argument against mimicry becomes a cohomological obstruction — H¹ is made to see what it is natively blind to, not by strengthening the cohomology but by preparing its inputs.

### 4.4 The Dissipation Floor (fixing the multiplicity gauge)

A thin proof-of-work or capacity floor prices the creation of identities, and does nothing else. It is forbidden from moonlighting as a certificate of order; it exists so that the spectral-gap coalition bound of §2 quantifies over identities that cost something. Stake could serve, but stake is endogenous — circular at bootstrap for a mechanism whose token value presupposes the mechanism working. Exogenous burn is cleaner at genesis and may be retired by governance once the identity set has thermalized.

## 5. Composition

The anchors compose in sequence, each closing exactly the residual surface of the last:

> beacon seeds challenge → delay chain certifies the response took real time → unique encoding certifies it took *distinct* time per identity → sheaf certifies the responses cohere across overlaps → dissipation floor prices entry into the cover.

The security claim is a conjunction. An adversary must simultaneously predict unpredictable photons, parallelize the unparallelizable, individuate the identical, corrupt an expander, and pay for the privilege. Each anchor alone is circumventable; the design discipline is that no anchor is ever asked to certify beyond its competence, since an anchor stretched past its competence becomes a proxy, and proxies are eaten.

**Test suite.** A concrete implementation should verify: (i) that the anchored sheaf admits no non-truthful global sections under the stated adversary — generically it will admit them if any anchor is removed; (ii) that reward is *not* invariant under section duplication — if invariant, the identity gauge is unfixed; (iii) the Laplacian spectral gap of the deployed cover, and the derived coalition cost bound; (iv) that the physical anchor is consumed as randomness and timing, never cited as a certificate of order.

## 6. What Is Declined

Two familiar anchors are declined by name.

*Trusted execution environments* import a corporate root of trust into a mechanism whose reason for existing is the absence of one. The attestation key is a throne, and thrones are captured.

*Pure stake-slashing* is circular at bootstrap, and the autopoietic-cult result of prior work indicates that social-consensus layers pollute the section space rather than purify it: a sufficiently coherent cult is, to any endogenous judge, indistinguishable from a truth.

The four anchors retained are all either physics or mathematics. For a mechanism that would call itself negentropy-anchored, that is the only acceptable taste.

## 7. Coda: The Internal Reframe

One honest alternative deserves its paragraph. If negentropy is defined internally — as order of the ledger's own state, compressibility of the section space itself — the attribution problem of §1 dissolves, since the boundary is now the system. But Goodhart returns in full force: any computable proxy for Kolmogorov order is directly optimizable, and matter-as-verb cuts both ways. A mechanism that rewards the appearance of order will be consumed by whatever form games it fastest. The external anchoring of §4 is chosen not because it is elegant but because it is the only known arrangement in which the thing rewarded and the thing measured are held apart by physics rather than by hope.

---

*Published under the Derivation of Value anthology. Licensed CC BY 4.0.*
