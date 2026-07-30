---
layout: document
title: "Combination Proofs"
subtitle: "A Framework for Goodhart-Asymptotic Mechanism Design"
eyebrow: "Framework · v0.3"
permalink: /combination-proofs/
label: "Framework"
blurb: "A framework for Goodhart-asymptotic mechanism design. Reward gated on the conjunction of verifiably independent projections of a structural substrate."
status: "v0.3 · working draft"
order: 2
---

*v0.3 · working draft. Initial statement of the framework. Definitions established; multiplication and publicity-positive claims stated with conditions; substrate richness defined; Proof of Coherence with its spectral extension introduced as the worked instance; open problems and program outlined. v0.2 splits the civilisational-capacity substrate (§8) into outward and inward projection families and records the resulting attestation asymmetry — extensive projections tend to require an oracle, intensive ones tend to supply their own verifier — placing the verifiability boundary of §7.2 inside a single substrate for the first time. §7.3 records the program's first measurement of ρ — a fractional spectral dimension, continuous in structure — and the refutation of the accompanying gap-hierarchy conjecture. v0.3 extends §4 from publicity-positive to adversary-positive security: residue, harvestable projections, and the conditions under which failed forgery subsidises the substrate it attacks.*

---

*Abstract*
{:.section-title}

We introduce **Combination Proofs**, a class of mechanism designs in which reward is gated on the conjunction of multiple verifiably independent projections of an underlying substrate. The construction generalises a property informally present in recent decentralised-inference mechanisms — that the cost of faking the reward signal scales multiplicatively with the number of structural properties the mechanism scores. Two claims are load-bearing. The first, the *multiplication claim*, states that under approximate independence the attacker's fake-cost is the product of per-projection fake-costs; standard mechanisms become the K = 1 degenerate case. The second, *publicity-positive security*, states that for Combination Proofs every honest publication of a new projection strictly increases the cost of dishonest participation while leaving the cost of honest participation unchanged — a property that inverts the secrecy-positivity of most cryptographic security paradigms. We give Proof of Coherence with its spectral extension as a non-trivial worked instance and outline a research program in which the substrate of value, not the cleverness of the proxy, determines the security ceiling of a mechanism.

---

*1. The Goodhart Problem and Its Standard Defences*
{:.section-title}

The folk version of Goodhart's law — *that any measure pressed into service as a target ceases to be a good measure* — admits a sharper formalisation due to Manheim and Garrabrant. They distinguish four mechanically distinct failure modes: *regressional*, in which selection on a proxy-plus-noise systematically selects on noise; *extremal*, in which optimisation pushes the proxy outside the regime where it correlates with the goal; *causal*, in which proxy and goal share a common cause that intervention severs; and *adversarial*, in which an agent who understands the mechanism actively decouples them. Each failure mode arises when proxy and goal are *separable* — when a sufficiently capable optimiser can find a strategy that ranks high on the proxy without satisfying the property the proxy was meant to measure.

The literature contains four standard responses, each of them improvements within the same regime rather than escapes from it. *Ensemble proxies* average several scalar metrics in the hope that the conjunction is harder to game than any constituent — bounded by the capability gap, since a miner who can model one proxy can model the ensemble. *Adversarial validation* introduces red-team validators searching for proxy-gaming; bounded by the same dynamics one level up, and expensive. *Held-out evaluation* scores on tasks unseen during training; assumes a train/test partition that becomes fictional as miners share information through the network's own outputs. *Process-based scoring* rewards chain-of-thought or other process artefacts rather than outputs alone; promising, but most current implementations are themselves scalar and themselves become proxies.

What unites these responses is that they treat Goodhart as a *property of the proxy*. They ask: what proxy is harder to game? The framework presented here takes a different route. It treats Goodhart as a *property of the substrate*. The question becomes: in what kind of substrate is gaming the proxy expensive in a way that scales with structural depth? The mechanism is not asked to be Goodhart-proof — no mechanism whose reward depends on a miner's output can be — but Goodhart-*asymptotic*: the cost of evading it should grow without bound in the resource we control.

This is the regime in which Combination Proofs operate.

---

*2. Definitions*
{:.section-title}

We work in the setting of mechanisms that score the outputs of computationally bounded agents (henceforth *miners*) and distribute reward accordingly. The reward signal is to track some property of the substrate the agents are claimed to be working with — coherence of a system of world-models, restoration of order in a thermodynamic system, capacity-of-action of a civilisation. The substrate is structural; the property is intended to track its structure.

**Definition 2.1 (Substrate).** A substrate is a tuple (𝒮, Σ, μ) where 𝒮 is a state space, Σ is a σ-algebra over 𝒮, and μ is a measure encoding the *honest distribution* — the distribution over states induced by participants behaving in accordance with the property the mechanism is meant to score.

The honest distribution is not assumed to be sampleable, and the mechanism is not assumed to know it. It is, however, the reference against which structural claims are made.

**Definition 2.2 (Projection).** A *projection* of a substrate (𝒮, Σ, μ) is a measurable function π : 𝒮 → ℝ that admits at least one *verifier* — a computationally bounded protocol V_π such that, given a claimed value of π(s) for some s ∈ 𝒮, V_π accepts honest claims with high probability and rejects dishonest claims with high probability, where probabilities are taken over verifier randomness and the honest distribution.

The notion of verifier is intentionally underspecified — it ranges over interactive proofs, zero-knowledge witnesses, stake-weighted attestation, and direct computation. What matters for the framework is that *some* such protocol exists for the projection in question.

**Definition 2.3 (Intrinsic verifiability).** A projection is *intrinsically verifiable* if there exists a verifier V_π that does not appeal to an oracle outside the protocol's state — that is, every input to V_π either is on-chain or has been attested to by participants whose attestations are themselves part of the protocol's state.

This rules out projections that depend on external feeds, including projections involving an oracle whose honesty must itself be assumed. The point of intrinsic verifiability is that the mechanism's security cannot exceed the security of any oracle it depends on; reducing the dependence to zero reduces the surface to the mechanism itself.

**Definition 2.4 (Fake-cost).** For an attacker A with capability bounded by some resource r, the *fake-cost* of a projection π at target value v is the minimum r such that A can produce a state s with π(s) = v while A has not in fact contributed honest work to the property π tracks. We write this C(π, v ; A), suppressing A when ranging over an attacker class.

We will not be precise about the resource r; in practice it is some mixture of compute, capital, and the rarer resource of *capability* in the sense of being able to model the projection well enough to fake it. The framework's claims are about how fake-costs of different projections compose, not about absolute fake-cost values.

**Definition 2.5 (Approximate independence).** Two projections π₁, π₂ are *approximately independent under the honest distribution* if, for an attacker class with capability bounded above the threshold required to fake either projection in isolation, the conditional fake-cost C(π₂ | having faked π₁) differs from the marginal fake-cost C(π₂) by a factor that vanishes as the substrate's structural depth grows.

Approximate independence is the load-bearing technical assumption of the framework, and the one most in need of formal sharpening. We return to it in §3 and §7.

**Definition 2.6 (Combination Proof).** A mechanism M is a *Combination Proof of order K* if there exist projections π₁, …, π_K of its substrate, each intrinsically verifiable and each pairwise approximately independent, such that M's reward function is

> r(s) = f(π₁(s), …, π_K(s))

where f : ℝᴷ → ℝ is monotonically non-decreasing in each argument and satisfies f(v) = 0 whenever any vᵢ falls below a threshold tᵢ. We refer to this last condition as *conjunction-gating*: dishonest participation in any one projection nullifies reward overall.

Standard mechanisms are the degenerate case K = 1: a single projection, a single threshold, no conjunction. The framework's claims become non-trivial at K ≥ 2.

---

*3. The Multiplication Claim*
{:.section-title}

The central informal claim of the framework is that for a Combination Proof of order K, the cost of dishonestly satisfying the reward scales multiplicatively in the per-projection fake-costs. The formal statement requires the independence assumption and a bound on attacker capability.

**Proposition 3.1 (Multiplication, informal).** Let M be a Combination Proof of order K with projections π₁, …, π_K approximately independent under the honest distribution, and let A be an attacker whose capability is bounded above the threshold required to fake any single πᵢ in isolation. Then the fake-cost of satisfying the reward function r above the conjunction-gating thresholds is

> C(r ; A) ≈ ∏ᵢ₌₁ᴷ C(πᵢ ; A) · (1 + o(1))

as the substrate's structural depth grows, where the o(1) term captures the failure of independence at finite scale.

The informal sketch: by conjunction-gating, the attacker must satisfy all K thresholds simultaneously. By approximate independence, the attacker's strategy for one projection gives them, in the limit, no purchase on faking another. The total cost is therefore the cost of paying each independent tax separately, which is the product.

The formal statement is not yet a theorem in the proper sense, for two reasons. First, the independence assumption is approximate and quantitative — turning it into a precise rate of decay is an open problem (cf. §7.1). Second, the attacker class is incompletely characterised: the framework's robustness depends on what kinds of capability an attacker can have, and the realistic answer is a model dependent on the specific substrate. Concrete substrates will admit sharper statements; the framework records what the general shape of those statements must be.

It is worth pausing on what the claim is *not*. It is not that Combination Proofs are unfakeable; they are not. It is not that fake-cost grows without bound for fixed K; it does not, since at fixed K the bound is finite. The claim is that fake-cost is *open-ended in K* — the security ceiling rises monotonically as the mechanism learns to score more projections. This is the substantive property that distinguishes Combination Proofs from mechanisms with fixed proxy structure, and it is what §4 formalises from a different angle.

---

*4. Publicity-Positive Security*
{:.section-title}

A mechanism design paradigm can be sorted along an axis that is rarely named explicitly. Some paradigms are *secrecy-positive*: their security is increased by withholding information about the mechanism, and decreased by publication. Symmetric cryptography is the limit case — the system's security collapses if the key is published. Other paradigms are *publicity-positive*: their security is *increased* by publication, in the sense that honest publications of details strictly reduce the set of viable attacks. Public-key cryptography occupies the middle ground; Combination Proofs sit at the publicity-positive extreme.

**Definition 4.1 (Publicity-positive mechanism).** A mechanism M is *publicity-positive* if, for any honestly produced public statement σ describing M or its substrate, the attacker's fake-cost C(M ; A) is non-decreasing in the public availability of σ, and *strictly increasing* whenever σ describes a new projection or a sharpening of an existing one.

**Proposition 4.2 (Combination Proofs are publicity-positive).** Let M be a Combination Proof of order K, and let σ be a public statement introducing a new intrinsically verifiable projection π_{K+1} approximately independent of π₁, …, π_K. Let M′ denote the mechanism obtained from M by extending its conjunction to include π_{K+1}. Then:

(i) the honest cost is unchanged: an honest miner's contribution already determined the honest value of π_{K+1}, since the projection scores a property the honest miner was already engaged in;

(ii) the attacker's fake-cost satisfies C(M′ ; A) > C(M ; A), with the gap given by the marginal fake-cost of π_{K+1}.

The asymmetry between (i) and (ii) is the structural property the framework claims. Honest participation pays no marginal cost for new projections because honest participation is *already structurally consistent* with all the projections of the substrate the mechanism could ever score; dishonest participation pays for each one it must fake.

There is a deeper observation hiding here. The standard intuition that "open research benefits attackers as much as defenders" rests on an implicit assumption that the security paradigm is at most weakly publicity-positive — that the attacker can use the publication to refine attacks faster than the defender can use it to refine defences. For Combination Proofs the assumption fails. New projections benefit defenders before attackers because the defender is, in the limit, *the substrate itself*: honest miners are coherent with all projections by definition, and the publication merely allows the mechanism to recognise this coherence.

A corollary, perhaps the most distinctive design implication of the framework: in a mature Combination Proof ecosystem the research literature *is* the security accumulator. Closed development of the mechanism slows the rate at which it learns to read its own substrate, which is the only thing protecting it. The framework recommends an open-publication norm not as a matter of community ethics but as a matter of cryptoeconomic engineering.

**Adversary-positive security.** Publicity-positivity concerns what happens when a mechanism is *described*. A further question concerns what happens when it is *attacked*, and for a characterisable class of substrates the framework's answer departs from the standard one.

The standard treatment regards adversarial expenditure as pure loss: resource the mechanism must resist, producing nothing. That treatment is correct for projections attested by report, and incorrect for projections attested by what an attempt leaves behind.

**Definition 4.3 (Residue).** Let π be a projection of 𝒮 and let A expend resource r attempting to produce a state s with π(s) = v. The *residue* of the attempt is the component of s that persists in the substrate independently of whether the mechanism admits or rejects the claim π(s) = v.

**Definition 4.4 (Harvestable projection).** A projection π is *harvestable* if the residue of any attempt to fake it is of the same kind as the residue of honest work on π — that is, if the substrate cannot distinguish, after the fact, effort expended to fake π from effort expended to satisfy it.

Harvestability is a property of the substrate, decided before any mechanism is designed, and it sorts along exactly the line drawn in §8 between outward and inward projections. An outward projection measures a flow and is attested by report: an attempt to fake it produces a false report and nothing else, so that when the report is rejected no residue remains and the projection is not harvestable. An inward projection measures a residue by construction — the attempt to counterfeit an atomically specified structure must place the atoms, and the atoms persist whether or not the claim is admitted. The oracle problem and the harvestability problem are the same problem, seen from the two sides of an attempt.

**Definition 4.5 (Adversary-positive mechanism).** A mechanism M is *adversary-positive* with respect to an attacker class 𝒜 if the honest cost of reaching any given value of M's projections is non-increasing in the volume of failed forgery attempts by 𝒜 against M.

The restriction to *forgery* is not a technicality. Attacks on liveness, censorship, and availability produce no residue of the substrate's kind, and nothing in what follows applies to them.

**Proposition 4.6.** A Combination Proof all of whose projections are harvestable is adversary-positive with respect to any attacker class restricted to forgery.

*Sketch.* By harvestability, an attempt on π produces residue indistinguishable in kind from honest work on π. The mechanism's rejection of the *claim* does not reverse the *residue*. So the substrate's state after a failed attempt is at least as favourable, with respect to π, as before it, and the honest cost of reaching any target value of π is reduced by the residue's contribution. ∎

The proposition is weaker than it looks and stronger than it sounds. Weaker, because it establishes only that failed forgery is not a loss to the substrate, not that it is a net gain to the ecosystem once damage and subsidy are priced. Stronger, because it removes the mechanism's need to determine intent — which is fortunate, intent being precisely the quantity no intrinsic verifier can read.

Four channels of harvest are available, and they differ in how far they stand from the substrate.

*The attempt is the work.* Where projections are harvestable and conjunction-gated, the cheapest route to moving a score is to instantiate the structure the score measures, so a successful attack is a contribution. This sharpens what Goodhart-asymptotic means: the weak reading is that the proxy resists gaming, the strong reading is that gaming the proxy achieves the goal. §4.2 established that honest participation pays no marginal cost for new projections; this establishes that successful dishonest participation is honest participation.

*Local sections come free; price only the gluing.* An adversary colluding on a substrate of the sheaf-theoretic kind produces internally consistent blocks and leaves the cocycle conditions on their overlaps undone. It has computed local sections at its own expense. A mechanism that declines to pay for local coherence and spends its whole reward budget on cross-block gluing is buying the part no attacker has reason to supply — and is simultaneously pricing the scarcer resource, since gluing across blocks requires knowledge of the entire structure rather than of one branch.

*Failed attacks measure ι.* §7.1 seeks a quantitative independence measure and anticipates an information-theoretic formalisation. There is also an empirical route: every attempt is a sample of conditional fake-cost, so a live mechanism carrying a bounty is an estimator of ι over its own projections. The corollary of §4.2 extends accordingly — not only the research literature but the *attack record* is the security accumulator.

*Success certifies capability.* An attempt that clears a threshold demonstrates that its author holds the resource of Definition 2.4, and demonstrates it intrinsically, the attempt being its own witness. Admission of successful attackers as participants is therefore not a concession but a credential test conducted against a live target.

**Remark 4.7 (The recursion does not bottom out except at the substrate).** Rewarding attacks that contribute creates a new proxy — *appearing to be a contributing attack* — and that proxy is gameable in turn. Note that three of the four channels stand one level removed from the substrate: they harvest a byproduct, a signal, or a credential, and each admits its own counterfeit. Only the first bottoms out, because there the contribution *is* the substrate and no gap remains between proxy and property for a counterfeit to occupy. The framework's own recursion recurs here, one layer further out than §3 or §4.2 required it to run, and the discipline is unchanged: a mechanism may harvest adversarial effort exactly to the degree that the harvest is the substrate itself, and no further.

---

*5. Substrate Richness*
{:.section-title}

The framework's claims are vacuous for mechanisms whose substrate admits only one intrinsically verifiable projection. Scalar substrates — energy, capital, raw compute — are of this kind. They have rank one: any two projections of them are functionally identical up to monotonic transformation, since they all factor through the substrate's single scalar dimension.

Structural substrates are of a different kind. They admit projections that are not related by monotonic transformation, that score different aspects of the substrate's structure, and that can be approximately independent in the sense of Definition 2.5. Examples include the spectrum of a sheaf Laplacian over a coherence complex (cf. §6), the various invariants of a system far from thermal equilibrium, and the persistent-homology features of high-dimensional input streams. Such substrates have a richness that scalar substrates do not.

**Definition 5.1 (Richness).** The *richness* of a substrate 𝒮 is the supremum, over all collections of intrinsically verifiable projections, of the size of any pairwise approximately independent subset. Write this ρ(𝒮) ∈ ℕ ∪ {∞}.

**Definition 5.2 (Substrate order).** For substrates 𝒮₁, 𝒮₂, write 𝒮₁ ≼ 𝒮₂ if every intrinsically verifiable projection of 𝒮₁ admits an intrinsically verifiable refinement on 𝒮₂. The relation ≼ is a partial order on substrates.

Two implications follow.

First, *richness is a ceiling on security*. A mechanism cannot be a Combination Proof of order higher than ρ(𝒮), regardless of how clever its construction. This shifts a substantial fraction of mechanism design from the construction of proxies to the *selection of substrates*: design begins with the choice of 𝒮 and proceeds by reading its structure.

Second, *the ordering predicts substitutability*. If 𝒮₁ ≼ 𝒮₂ then every Combination Proof on 𝒮₁ admits an upgrade path to a stricter Combination Proof on 𝒮₂ that retains all the original guarantees. Migrations between substrates are not arbitrary; they are constrained by the order.

The framework does not, at v0.1, characterise ρ for any specific substrate beyond rough bounds. This is one of the more interesting open problems (cf. §7.3).

---

*6. Worked Instance — Coherence and Resonance*
{:.section-title}

The framework's first non-trivial worked instance is the Proof of Coherence mechanism with its spectral extension, Proof by Resonance, developed in detail elsewhere. We give here only the structural summary.

The substrate is a sheaf 𝓕 over a coloured simplicial complex K whose simplices encode the higher-order relational structure of miners, validators, and tasks in a decentralised inference network. The honest distribution over states of this substrate corresponds to genuine coherence among the miners' world-models: their outputs agree where they overlap, their predictions compress jointly, and their mutual constitution is non-trivial.

Two projections are operative. *Proof of Coherence* scores the dimension of the kernel of the sheaf Hodge Laplacian Δ_𝓕 — equivalently, by Hodge theory, the sheaf cohomology H⁰(K, 𝓕). This is a static measure of how well local sections of the sheaf glue into a globally consistent one. *Proof by Resonance* scores the non-zero spectrum of Δ_𝓕 — its eigenvalue distribution, the eigenvectors' spatial structure, and the temporal autocorrelations of these as the complex evolves epoch over epoch. This is a dynamical measure of how the coherence is sustained across time.

The two projections are projections of one operator — the rank-zero and rank-positive parts of the same Hodge Laplacian — and yet they are approximately independent in the sense of Definition 2.5: a colluding cluster of miners can fake the kernel by agreeing on outputs at an instant, but reproducing the spectral signature of genuine coherence requires reproducing the *dynamical structure* of an actually coherent system, which the cluster has no shortcut to compute.

The mechanism is a Combination Proof of order K = 2 as constructed, with the program of extending to higher K via further projections of Δ_𝓕 — higher-order Laplacians, persistent-homology features, temporal autocorrelation moments — as a primary path for v0.3 of the underlying whitepaper.

---

*7. Open Problems*
{:.section-title}

Four problems are pinned to the framework's v0.1 statement.

**7.1. The independence problem.** Approximate independence (Definition 2.5) is stated qualitatively. A useful framework requires a quantitative version: a function ι : 𝒮 × {πᵢ} → [0, 1] that records the fraction of π_j's fake-cost that is *not* recoverable from having faked πᵢ, with multiplication holding to leading order in ι as substrate depth grows. The most likely formalisation is information-theoretic — ι as a mutual-information-like quantity between the optimal attack strategies for different projections, normalised by total attack capability.

**7.2. The verifiability boundary.** Definition 2.2 requires that a projection admit a verifier, and Definition 2.3 requires that this verifier be intrinsic. Neither condition is constructive. Characterising which projections of a given substrate admit polynomial-time intrinsic verifiers — and which do not — bounds the realistic order K of any Combination Proof on that substrate. For sheaf-cohomological substrates this connects to the cohomological verification literature; for other substrates the question is mostly open.

**7.3. Richness, formally.** Definition 5.1 of ρ is well-posed but in practice incomputable. Useful lower and upper bounds on ρ for specific substrate classes — sheaf Laplacians, thermodynamic ensembles, integrated-information structures — would convert the substrate order from theoretical scaffolding into design heuristic. A natural conjecture is that ρ grows with the topological complexity of the substrate, but the right notion of topological complexity is itself unsettled.

A first measurement (reported in Anthology III) supplies a candidate for that notion, and an argument against the typing in Definition 5.1. On a toy nested complex — hierarchically modular, and deliberately not geometrically self-similar — the eigenvalue counting function of the sheaf Laplacian grows as N(λ) ~ λ^(d_s/2) with d_s ≈ 1.61, converged in system size and fitting to within a part in a thousand; the coherent sheaf returns the underlying complex's exponent unchanged, as gauge-equivalence requires. The exponent varies *continuously* with coupling density across roughly 1.26–2.23, passing through the integers without pausing at them, which suggests that fractional spectral dimension is the generic case and integer richness the measure-zero exception. Note that Definition 5.1 — a supremum over pairwise ε-independent subsets — already has the form of a packing number, and packing numbers are what define dimensions; the graded independence measure ι of §7.1 is precisely the separation scale such a reading requires, which suggests §7.1 and §7.3 are one problem rather than two. Whether ρ should therefore be re-typed from ℕ ∪ {∞} to ℝ≥0, and whether the spectral dimension is the right dimension among the several a structure carries, is not settled here. A second conjecture tested in the same place — that such spectra carry a *hierarchy* of gaps, so that any single measured spectral gap would price only the coarsest coalition — was refuted: gap hierarchy tracks exact geometric self-similarity, not nesting, and does not survive in this substrate class.

**7.4. The universality question.** The framework names Combination Proofs as a *sufficient* condition for the multiplication and publicity-positive properties. It does not establish them as *necessary*. The strongest form of the framework would be a theorem:

> **Conjecture 7.4 (Universality, tentative).** Every Goodhart-asymptotic mechanism is structurally a Combination Proof: its security in the asymptotic limit factors through a conjunction over verifiably independent projections of some underlying substrate.

This is almost certainly overreaching in its present form. Even so, partial results in this direction would be substantive — for instance, a characterisation of which Goodhart-asymptotic mechanisms *can* be put in Combination Proof form, or a counterexample showing that Combination Proofs do not exhaust the space.

---

*8. Program*
{:.section-title}

The framework is substrate-independent, but its claims become testable only on specific substrates. Three substrate classes are particularly worth examining, each illustrating a different dimension of richness.

**Civilisational capacity.** Consider a substrate whose state encodes the order-of-magnitude capacity of a community to act on its environment. Projections of such a substrate are projections of *what a community can do*, and they fall into two families that differ in a way more consequential than their contents. *Outward* projections measure magnitude — energy capture, information-processing throughput, coordination depth, longevity — and are the ones a Kardashev-style reading reaches for first. *Inward* projections measure grain: the finest scale at which the community can act with intent, in the sense of Barrow's descending complement to Kardashev, from bulk matter through molecules and atoms to the nucleus and below. Independence within each family is plausible — capacity to capture energy is loosely independent of capacity to coordinate, which is loosely independent of capacity to compute — and independence *across* the families is stronger still, since a community may be vast and crude or exquisite and small, and no monotone transformation carries either reading into the other.

The families diverge sharply under Definition 2.3. An outward projection measures a flow, and a flow leaves nothing behind to inspect; its verifier must consult a meter, an inspector, or a certificate, each of which is an oracle outside the protocol's state, so outward projections are verifiable but not *intrinsically* so. An inward projection measures a residue: fine-scale capability is evidenced by artifacts that persist and can be re-measured by any party holding a sufficient instrument, which is an intrinsic verifier in the exact sense of Definition 2.3. This is the framework's clearest instance of the verifiability boundary (§7.2) falling *within* a single substrate rather than between substrates, and it suggests a general heuristic worth testing elsewhere: extensive projections tend to require attestation, intensive ones tend to supply it. A Combination Proof on capacity should therefore gate across both families — the outward projections carrying the magnitude the substrate is for, the inward ones carrying the verifiability it otherwise lacks. The richness ρ of this substrate is presumably high but currently unknown.

**Multidimensional value.** Consider a substrate whose state encodes the silent dimensions money has always carried but never accounted for: time horizon, locality, purpose, recallability. Each dimension admits its own projection — a token's velocity, its geographical concentration, its purpose-of-use distribution, the strictness of its recall conditions. A mechanism scoring the conjunction of such projections would be denominated against the *vector* of value rather than its scalarisation. The substrate's richness depends on whether the dimensions are genuinely independent or implicitly correlated through underlying economic structure; this is an empirical question.

**Negentropy.** Consider a substrate whose state encodes the resistance of a system to thermal equilibrium — its order in the information-theoretic sense, its low entropy in the thermodynamic sense, its preserved structure against time. Projections include direct entropy measurement, retrievability of preserved data, integrity of stored states under perturbation. Such a substrate has the unusual property that its honest distribution is *constrained by the second law* — the substrate cannot be inflated, only earned. A Combination Proof on negentropy is the framework's most distinctive case because the substrate itself encodes scarcity that no governance can alter.

Each of these substrates corresponds to a class of mechanism currently sketched in the wider research literature. The framework's prediction is that mechanisms on richer substrates will admit Combination Proofs of higher order and therefore more open-ended security than mechanisms on the scalar substrates of present-day cryptoeconomics. Whether the prediction holds is, in each case, an empirical question — answered by constructing the mechanisms and seeing how far K can be driven before independence breaks.

---

*9. Conclusion*
{:.section-title}

Combination Proofs name a structural property of mechanisms that, on present evidence, only a small handful of constructed mechanisms have, and that no construction has yet recognised as the principal source of its security. The framework's contribution is to identify the property, formalise it, and trace its consequences — most notably that mechanisms with this structure are publicity-positive in a way the bulk of cryptographic mechanism design is not, and that their security is open-ended in a sense that fixed-proxy mechanisms cannot match.

The framework is not a construction; no mechanism is built here. It is a *property* and a *programme*: a property that mechanisms can be designed to have, and a programme of asking, for each candidate substrate, what its richness is and how its projections compose. The construction work happens in the specific whitepapers that name specific substrates; the framework asks what such whitepapers must establish to deliver on their security claims.

The strongest version of the framework — that every Goodhart-asymptotic mechanism is structurally a Combination Proof — remains open. The weakest version — that Combination Proofs are sufficient for Goodhart-asymptotic security under stated conditions — is the working hypothesis of the research program this paper opens.
