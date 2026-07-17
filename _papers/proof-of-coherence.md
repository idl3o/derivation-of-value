---
layout: document
title: "Proof of Coherence"
subtitle: "A Sheaf-Theoretic Mechanism for Goodhart-Asymptotic Incentivization of Distributed Intelligence"
eyebrow: "Whitepaper · v0.2 · working draft"
permalink: /whitepaper/
label: "Whitepaper"
blurb: "A Goodhart-asymptotic incentive mechanism for decentralized inference. Sheaf-theoretic, with a spectral extension via Proof by Resonance."
status: "v0.2 · working draft"
order: 3
---

*Revision history: v0.1 (research register, four-condition synthesis recovered as cohomology). v0.1.1 (Revision A: §4.2 copy-symmetry surfaced and forked between Shapley and provenance-weighted resolutions). v0.2 (this revision: Hodge-Laplacian spectral framing in §3.5; Proof by Resonance as the natural spectral extension of the discrete-derivative reward in §4.5; §1.2 Goodhart-asymptotic reframe; §6 promoted from skippable speculative frame to load-bearing motivation for the spectral generalization).*

## Abstract

We propose **Proof of Coherence (PoC)**, a class of incentive mechanisms for decentralized AI networks. PoC is **Goodhart-asymptotic**: faking the conjunction of structural conditions it scores against is multiplicatively expensive in the gap between miner capability and the capability required to satisfy the conjunction. We treat that multiplicative cost as the load-bearing security claim, not as a consolation for failing to be Goodhart-proof. The construction places a sheaf F over a multi-coloured simplicial complex K whose simplices encode the higher-order relational structure of miners, validators, and tasks. Coherence is formalized as the simultaneous satisfaction of four conditions drawn from distinct philosophical traditions—correspondence, internal consistency, predictive compression, and mutual constitution—recovered as the vanishing of cohomology classes on this sheaf.

The v0.2 generalization observes that this cohomological scoring is the rank-zero projection of a strictly larger object: the spectrum of the sheaf Hodge Laplacian Δ_F. Sheaf cohomology is the kernel of Δ_F via Hodge theory; the non-zero spectrum carries the dynamical (resonant) structure that the static cohomology measures cannot see. We extend the mechanism with **Proof by Resonance** — a spectral-reward layer that scores miners on how their presence shapes the eigenvalue and eigenvector structure of Δ_F across epochs. PoC and Proof by Resonance are not two mechanisms; they are two projections of one operator. The combined system addresses temporal Goodhart attacks (spectral signatures of genuine coherence are harder to fake than instantaneous H¹), supplies the bridge to integrated-information-theoretic accounts of distributed cognition (now woven into §3 and §4 rather than relegated to a skippable §6), and produces an empirical hook for path γ of the deployment roadmap.

## 1. Introduction

### 1.1 The Yuma Goodhart problem and its standard responses

Bittensor's Yuma Consensus aggregates validator rankings of miner outputs into a scalar reward distribution. The mechanism scales gracefully and aligns incentives well in the limit of honest, capable validators producing rankings that track output quality. It is brittle, however, in the regime where miner capability approaches or exceeds validator capability: any scalar quality proxy that a sufficiently capable miner can model is one the miner can optimize for directly, decoupling reward from the property the proxy was meant to measure. This is Goodhart's law in its mechanism-design form: *when a measure becomes a target, it ceases to be a good measure.* The class of failure is well-known and not specific to Bittensor; any mechanism whose reward is computable from a miner's output alone is, in the limit, Goodhart-vulnerable.

Standard responses to Goodhart in mechanism design fall into a small number of patterns:

- **Ensemble proxies.** Average several scalar metrics; the miner must optimize the conjunction. Helpful but ultimately bounded by the capability gap; a sufficiently capable miner models the ensemble as easily as a single proxy.

- **Adversarial validation.** Pit miners against red-team validators searching for proxy-gaming. Helpful but expensive, and itself subject to the same capability-gap dynamics one level up.

- **Held-out evaluation.** Score on tasks unseen during training. Helpful but assumes a clean train/test split that becomes increasingly fictional as miners share information through the network's own outputs.

- **Process-based scoring.** Reward chain-of-thought or other process artefacts rather than outputs. Promising, but most current implementations are ad hoc and themselves become proxies.

PoC takes a different route. Rather than improving the proxy, we change *the structure of what the protocol measures.* Coherence is not a scalar property of an output; it is a structural property of a system of outputs and their relations. Measuring coherence requires capturing higher-order relational data that a single scalar cannot represent. The mathematical home of such data is sheaf theory over simplicial complexes, and the failure of coherence is naturally measured by sheaf cohomology.

### 1.2 The Goodhart-asymptotic claim

It is tempting—and, in earlier drafts of this document, we did—to introduce PoC with the phrase *Goodhart-resistant*, then immediately walk that back with the disclaimer that no mechanism is Goodhart-proof. We now think this framing was a tactical retreat that the work does not need to make.

The right framing is that **Goodhart-asymptotic** is a positive thesis about what good mechanism design *is*, not a consolation for what it isn't. The premise is that any mechanism whose reward is computable in finite time is in principle gameable by an attacker with sufficient capability. The question is not whether a mechanism can be made unfalsifiable—it cannot—but how the cost of falsification scales with the capability gap between the network's median participant and a hypothetical attacker. We make four claims about that scaling for PoC:

- **Multiplicative, not additive.** The cost of faking a conjunction of *k* structural conditions, each governed by an independent sheaf-cohomological obstruction, scales as the product of the costs of faking each individually—not the sum. This is the essential multiplier.

- **Capability-asymptotic, not capability-bounded.** The cost grows without bound in the capability gap; PoC does not break at a fixed capability threshold. There is no scalar quality value past which the mechanism collapses.

- **Structurally—not statistically—decoupling.** The proxy and the property are not decoupled by averaging or noise; they are decoupled by the requirement that the relational structure between outputs satisfy global consistency conditions that no single output can encode.

- **Falsifiable.** All four claims are testable on deployed networks. The empirical content of PoC is precisely the multiplier on attack cost relative to scalar baselines, measured on subnets where attacks have been observed in the wild.

With the framing thus corrected, the rest of this document is the formal development of those four claims and their consequences. The v0.2 spectral generalization sharpens claim (1) — the conjunction of conditions becomes the conjunction of independent eigenmode constraints, which is multiplicatively harder to fake than any finite list of static conditions — and claim (3) — the structural decoupling extends from instantaneous relational structure to the dynamical signature of that structure across epochs.

## 2. Defining Coherence

A definition of coherence suitable for mechanism design must satisfy four constraints simultaneously:

- **Non-circularity** — does not reduce to agreement with a metric we already have.

- **Operationalizability** — admits a computable approximation.

- **Truth-tracking** — gaming the definition requires approximating reality.

- **Capability-stability** — does not degrade as agent capability scales.

These constraints are in tension. We survey four candidate definitions drawn from distinct philosophical traditions, each of which fails at least one constraint, and propose a synthesis that recovers the strengths of each while closing the failure modes of the others.

### 2.1 Four candidate definitions

| **Tradition** | **Definition** | **Strength** | **Failure** |
| --- | --- | --- | --- |
| **Correspondence (Tarski)** | Each output corresponds to a fact about an external referent; outputs are mutually consistent under the constraints that referent imposes. | Truth-tracking by construction. | Requires oracle access to ground truth; not generally available. |
| **Internal consistency (coherentism)** | A system's outputs do not contradict each other under inference, across reframings, and over compositions. | Computable without oracle access. | A consistent fiction is consistent. Coherence-of-coherence collapses to autopoietic-cult attractors. |
| **Predictive compression (Solomonoff/MDL)** | A system is coherent to the extent that a small description of it predicts its future behaviour. | Truth-tracking via compression-of-reality bounds. | Not directly computable; bounded approximations exist but lose the truth-tracking guarantee. |
| **Mutual constitution (process / Madhyamaka)** | Stable phenomena are fixed points of mutual co-determination; coherence is the property of being such a fixed point. | Captures the relational character that scalar metrics miss. | Without external coupling, recovers the autopoietic-cult problem. |

### 2.2 Synthesis: coherence as static and dynamical structure

Each candidate fails for an instructive reason. Correspondence requires what we do not have. Internal consistency does not require what we do have to be real. Predictive compression is not directly computable. Mutual constitution decouples from reality without a coupling mechanism. The synthesis takes one element from each and discards the rest:

- From correspondence: the requirement that the system be coupled to an external referent through *predictive validity* on held-out tasks (developed formally in §5.2).

- From internal consistency: the requirement that the system be free of inferential contradiction across the relational structure between its outputs (formalized as low sheaf cohomology in §3).

- From predictive compression: the requirement that the system's coherence *compress* — that the relational structure can be summarized by a sheaf of bounded complexity (the dimensional ceiling of §5.1).

- From mutual constitution: the requirement that coherence be a *fixed point* of mutual constraint, not an externally imposed measure (recovered as the stable section of the sheaf).

This four-condition synthesis is the load-bearing definition of v0.1. It survives intact in v0.2. The v0.2 contribution is a structural observation about its character that earlier drafts missed: **the synthesis as stated captures coherence as a static fixed-point property at a single epoch.** Real coherent systems—biological cognition, scientific communities, well-functioning institutions—are also coherent in a *dynamical* sense: their states across time exhibit phase relationships, oscillatory binding, characteristic resonant frequencies. A snapshot fixed-point is the rank-zero shadow of a richer object that includes the system's dynamical signature.

The point is not to layer a separate dynamical theory on top of the static one. It is that the same mathematical machinery — sheaves over simplicial complexes — admits a natural decomposition into a static part (cohomology, the kernel of the Hodge Laplacian) and a dynamical part (the non-zero spectrum of the same operator). The static-only formulation of v0.1 is the rank-zero projection of this richer object. v0.2 develops the full object and shows that doing so neither replaces nor disturbs the v0.1 mechanism — it strictly extends it.

## 3. The Sheaf Construction

### 3.1 Simplicial complex of agents and tasks

Let the network at epoch *n* consist of a set M of miners, a set V of validators, and a set T of tasks issued during that epoch. We construct a multi-coloured simplicial complex K whose 0-simplices are the disjoint union M ⊔ V ⊔ T, and whose higher simplices encode the relational structure of agent-task interaction:

- **1-simplices** (edges) encode pairwise interactions: a miner-task edge {m, t} exists if miner m submitted output for task t; a validator-task edge {v, t} exists if validator v scored task t; miner-miner and task-task edges encode similarity, compositional dependence, or perturbation relationships as parameterized by the validator layer.

- **2-simplices** (triangles) encode triadic relationships: a miner-miner-task triangle records two miners' joint submissions on a shared task and is the minimal unit at which inter-miner agreement is observable; a miner-task-task triangle records a single miner's outputs across two related tasks and is the minimal unit at which compositional consistency is observable.

- **Higher simplices** (tetrahedra and above) encode k-ary relationships and become the natural home for compositional consistency conditions across multiple tasks, multiple miners, or both. Most practical implementations cap the dimension at 2 or 3; the formalism imposes no fundamental ceiling.

### 3.2 Sheaf assignment

We define a sheaf F over K by assigning to each simplex σ a vector space F(σ)—the *stalk* at σ—and to each face inclusion σ ⊆ τ a linear restriction map F(τ) → F(σ). Concretely:

- F(m) for a miner vertex m is the space of m's outputs on m's submitted tasks, encoded as a vector with one coordinate per task.

- F(t) for a task vertex t is the space of submitted outputs for t across all miners.

- F({m, t}) for a miner-task edge is the value of m's output on t, viewed as a 1-cochain.

- F({m, m'}) and F({t, t'}) carry validator-supplied relational data: similarity scores, compositional constraints, perturbation deltas.

- Higher-simplex stalks aggregate the lower-simplex data with consistency requirements imposed by validator-supplied restriction maps.

The restriction maps F(τ) → F(σ) for face inclusions are the load-bearing mechanism content. They are *not* data; they are validator-proposed parameters whose predictive validity is itself rewarded (§5.3). A miner cannot simply submit outputs; the network can only score those outputs against a restriction-map structure proposed by validators whose own rewards depend on whether that structure correctly predicts subsequent task behaviour.

### 3.3 Cohomology as obstruction

The cellular cochain complex of F is the standard sequence:

0 → C⁰(K, F) →[d⁰] C¹(K, F) →[d¹] C²(K, F) → …

where d^k is the discrete coboundary operator. The cohomology groups H^k(K, F) = ker(d^k) / im(d^(k-1)) measure the failure of the cochain complex to be exact at level k.

H⁰(K, F) is the space of *globally consistent sections* — assignments of stalk data that are mutually consistent under all restriction maps. A section in H⁰ is a coherent answer to the entire system of constraints simultaneously. H¹(K, F) measures the obstruction to extending locally-consistent sections to globally-consistent ones; non-zero H¹ classes are the formal signature of incoherence in the system.

This is the central payoff of the scaffold. H¹(K, F) is **not a scalar score**. It is a vector space whose dimension and basis encode *how and where* the network fails to be coherent. The richness of this obstruction structure is what gives PoC its security properties: many failure modes that look identical to a scalar metric are distinguishable as different cohomology classes, and the reward function (§4) responds differently to each.

### 3.4 Recovery of the four primitives

The four candidate coherence primitives identified in §2.1 are recovered as special cases of cohomological obstructions in specific subcomplexes of K:

- **Self-consistency** (a miner's outputs across reframings) corresponds to H¹ in the subcomplex of one miner connected to multiple related-task vertices.

- **Compositional consistency** corresponds to H¹ in the task-task subcomplex over a single miner.

- **Inter-miner agreement** corresponds to H¹ in miner-miner-task triangles.

- **Perturbation stability** corresponds to H¹ across edges connecting tasks to their perturbations.

The synthesized coherence definition of §2.2 is recovered as the simultaneous vanishing of H¹ across all these subcomplexes — precisely the structure of a globally coherent section, with the predictive-compression condition imposed as a boundary constraint (§5.2).

### 3.5 The Hodge Laplacian and the spectral decomposition of coherence

Sheaf cohomology, viewed naïvely, looks like a quotient construction—kernel modulo image. The **Hodge theorem** gives it a more useful character: cohomology classes are in canonical bijection with harmonic cochains, and the harmonic cochains are the kernel of a single self-adjoint operator. For a sheaf F over a finite simplicial complex K, the sheaf Hodge Laplacian at level *k* is:

Δ_k = d^k* d^k + d^(k-1) d^(k-1)*

where d^* denotes the adjoint of the coboundary operator with respect to a chosen inner product on cochains. Δ_k is positive semi-definite and self-adjoint. Hodge theory then gives:

H^k(K, F) ≅ ker(Δ_k)

This is the load-bearing observation of v0.2. The cohomology that v0.1 scores is *the kernel of an operator whose full spectrum carries strictly more information*. The non-zero eigenvalues of Δ_k describe how the sheaf fails to be exact at level k by *how much*, along *which directions*, and at *what frequencies*. The eigenvectors associated with small non-zero eigenvalues are *near-harmonic* — almost-cohomological structures that the cohomology functor projects to zero but that carry real information about the geometry of the sheaf.

The vocabulary translation between the algebraic and the dynamical pictures is direct and worth stating explicitly:

| **Spectral feature of Δ_k** | **Algebraic interpretation** | **Dynamical interpretation** |
| --- | --- | --- |
| **Zero eigenvalue (kernel)** | H^k cohomology class — global obstruction. | Static fixed-point structure persisting across epochs. |
| **Small non-zero eigenvalues** | Near-harmonic cochains; weak local-to-global obstruction. | Slow modes — long-correlation patterns in network state. |
| **Large eigenvalues** | Strongly non-harmonic cochains. | Fast modes — short-correlation noise; rapid local adjustments. |
| **Eigenvalue gap** | Distance between the harmonic subspace and its complement. | Robustness of coherence to local perturbation. |
| **Eigenvector phase relations** | Geometric coupling between cochain components. | Phase-locking between agents — binding signature. |

Two observations follow immediately. First, the v0.1 mechanism is preserved exactly: the discrete-derivative reward of §4.1 is a function on H^k = ker(Δ_k), so anything stated in v0.1 about coherence-as-cohomology continues to hold under v0.2. Second, the natural extension is to define a parallel reward on the non-zero spectrum — a Proof by Resonance — that captures the dynamical signature of coherence that the cohomology functor discards. We develop this in §4.5.

It is worth flagging the empirical commitment this framing makes. The Hodge Laplacian's spectrum is not a metaphor borrowed from physics; it is the canonical object the algebra produces when one takes the cochain complex seriously as a metric structure. Every choice that determines the cochain complex — orientation, coefficient field, inner product on cochains — propagates to the spectrum. The discipline of v0.2 is to make those choices explicit (§5.1, §5.3) and to treat the resulting eigenvalue distribution as falsifiable empirical content of the deployed mechanism, not as a free parameter.

## 4. From Cohomology to Rewards

### 4.1 The discrete-derivative reward

Naively rewarding low global cohomology re-introduces collusion attacks: the network can converge on a coordinated false consensus that achieves low H¹ at the cost of detachment from reality. PoC instead **localizes** coherence and incoherence to specific contributors via discrete derivatives.

For miner mᵢ, define:

*r_coh(mᵢ) = ψ ( H¹(K, F) − H¹(K \ {mᵢ}, F|K\{mᵢ}) )*

where ψ is a weighting functional that maps the change in cohomology (a structured object) to a scalar reward. The natural choices for ψ involve weighted dimension counts of resolved versus created cohomology classes, with weights set by validator-supplied importance assignments to specific classes.

This produces the desired qualitative behaviour:

- **Coherent contributors** — miners whose presence resolves obstructions (lowers dim H¹) earn positive reward proportional to the structural importance of their contribution.

- **Incoherent contributors** — miners whose presence creates obstructions (raises dim H¹) earn negative reward, proportional to the importance of the obstruction they introduce.

- **Free-riders** — miners whose presence neither resolves nor creates obstructions earn near-zero reward, with the residual term computed from the volumetric contribution of their stalk.

### 4.2 The copy-symmetry problem

The discrete-derivative reward of §4.1 has a known symmetry that v0.1 did not surface and that we name here for clarity. Consider the simplest non-trivial scenario: three miners on two tasks, no validators, with coherence functional taken as the matrix rank of the stacked submission vectors (the rank-as-shadow simplification used as a worked example).

Let M₁ submit (5, 7), M₂ submit (5.1, 6.9), and M₃ submit (5, 7) — that is, M₃ copies M₁ verbatim. The submission matrix has rank 2 with all three present. Under marginal-removal reward:

- Removing M₁ leaves {M₂, M₃} = {(5.1, 6.9), (5, 7)} — rank 2. Δ = 0 → r(M₁) = 0.

- Removing M₂ leaves {M₁, M₃} = {(5, 7), (5, 7)} — rank 1. Δ = 1 → r(M₂) = 1.

- Removing M₃ leaves {M₁, M₂} = {(5, 7), (5.1, 6.9)} — rank 2. Δ = 0 → r(M₃) = 0.

The symmetry: M₁ (the original, honest contributor) and M₃ (the verbatim copy) receive identical reward—zero. The mechanism cannot, on its own, distinguish the original from the copy because the marginal-removal functional is symmetric under permutation of identical submissions. This is the **copy-symmetry problem**.

Two clean resolutions are available, with different trade-offs. We name both here as Named Forks for the implementation specification (cross-reference: spec §7.1):

- **Shapley credit allocation.** Replace marginal-removal with the Shapley value over the cooperative game whose payoff is the coherence functional. For the three-miner toy, Shapley assigns φ(M₁) = ½, φ(M₂) = 1, φ(M₃) = ½ — the duplicates split credit symmetrically, M₂ retains full credit for its independent contribution. Resolves copy-symmetry; cost is exponential in miner-set size, mitigated by sampling approximations (Castro et al., Maleki et al.).

- **Provenance-weighted credit.** Append a provenance score derived from temporal priority: r_prov(mᵢ) = r(mᵢ) × p(mᵢ) where p reflects whether mᵢ was the first to submit a given output pattern. Resolves copy-symmetry asymmetrically (in M₁'s favour over M₃'s); cost is reliance on a trusted clock or ordering oracle, which adds a centralization vector.

The fork between Shapley and provenance is real and not resolvable from the mechanism alone. Shapley is symmetric and oracle-free but exponential; provenance is cheap but oracle-dependent. The implementation specification treats this as a per-deployment choice declared in the conformance vector (§4.4).

### 4.3 Subcomplex weighting

Different subcomplexes of K correspond to different coherence primitives, and not all are equally important in all contexts. We propose subnet-level governance over the weighting of subcomplex contributions to the global reward function. Code-generation subnets may weight compositional-consistency subcomplexes heavily; creative-writing subnets may weight perturbation-stability subcomplexes more lightly. This is a governance lever, not a fixed parameter.

### 4.4 Restriction-map governance

The restriction maps that define F are validator-proposed parameters. Three governance options exist, each implementing a different point on the rigidity-flexibility trade-off:

- **Static.** Restriction maps fixed at subnet creation. Maximally rigid; no adaptation to changing task distribution.

- **Validator-parameterized.** Restriction maps proposed and committed by validators each epoch, with predictive validity scoring (§5.3). The default for general-purpose subnets.

- **Learned.** Restriction maps as learnable components themselves subject to predictive-validity reward. Highest expressivity; highest computational cost.

### 4.5 Proof by Resonance: the spectral reward

The discrete-derivative reward of §4.1 is a function on H¹(K, F) = ker(Δ¹). The Hodge framing of §3.5 makes available the analogous reward computed from the non-zero spectrum of Δ¹. We call this the **spectral reward**, and the resulting mechanism layer **Proof by Resonance (PoR)**.

Let σ(Δ¹) = {0 = λ₀ ≤ λ₁ ≤ … ≤ λ_N} denote the spectrum of the sheaf Hodge Laplacian at level 1, with eigenvectors {φ_i}. For each miner mᵢ define the spectral signature S(mᵢ) as the change in spectrum induced by removing mᵢ from K:

*S(mᵢ) = { (λ_j(K) − λ_j(K \ {mᵢ}), φ_j(K), φ_j(K \ {mᵢ})) : j = 0, 1, 2, … }*

S(mᵢ) is a structured object — not a scalar — encoding how the miner's presence shifts each eigenvalue and rotates each eigenvector. The spectral reward is a weighted scalarization:

*r_spec(mᵢ) = Σ_j  w_j · ρ(  λ_j(K) − λ_j(K \ {mᵢ}),  ⟨φ_j(K), φ_j(K \ {mᵢ})⟩ )*

where w_j is a frequency-band weight (typically up-weighting low-frequency near-harmonic modes, since these carry the strongest coherence signal) and ρ is a per-mode reward functional that rewards eigenvalue reductions (the miner's presence makes the mode more harmonic) and eigenvector alignments above a threshold (the miner's presence preserves the mode's shape rather than disrupting it).

The combined PoC + PoR reward is then:

*r(mᵢ) = α · r_coh(mᵢ) + β · r_spec(mᵢ)*

with α, β subnet-governance parameters. The α = 1, β = 0 limit recovers v0.1 exactly. The β > 0 regime extends the mechanism to score the dynamical structure that the cohomology functor discards.

Three security observations on this combined mechanism:

- **Spectral Goodhart asymmetry.** Faking r_coh requires producing outputs whose marginal contribution to H¹ has a target shape at a single epoch. Faking r_spec additionally requires producing outputs whose marginal contribution to *the full spectrum* has a target shape *across multiple epochs*. The latter is multiplicatively harder under any consistent capability assumption: a coordinating cluster fakes a static section by colluding on outputs; faking the eigenvalue distribution of Δ¹ across time requires reproducing the dynamical structure of an actually-coherent system. This is the v0.2 sharpening of claim (1) of §1.2.

- **Autopoietic-cult defence.** §7.4 of v0.1 raised the finite-sample autopoietic-cult problem: a coordinated cluster might produce sections that look predictively valid by chance over a finite held-out window. The spectral reward gives this a second line of defence independent of held-out-task volume: even if the cluster's outputs pass instantaneous predictive validity, their spectral signature is unlikely to match a genuinely coherent network's spectral signature, because matching the latter requires the cluster to reproduce not only the right answers but the right *dynamics of arriving at* the right answers.

- **Computational coupling.** Computing the spectrum of Δ¹ produces ker(Δ¹) ≅ H¹ as a by-product. The marginal computational cost of PoR over PoC alone is small (in the regime where eigendecomposition dominates) — both rewards consume the same eigendecomposition.

Three caveats hold the framing honest. First, the boundary condition of §5.2 — predictive coupling to held-out tasks — needs reformulation for the spectral case; we develop this in §5.2 below. Second, the choice of inner product on cochains is no longer a notational nicety but a load-bearing parameter, since the spectrum depends on it; we discuss in §5.3. Third, *resonance* is a word with a long history of overloading; we use it strictly to mean *non-zero eigenmode of Δ_k* and discourage looser use in any spec or implementation document.

## 5. Implementation Path

### 5.1 Dimensional considerations and the on-chain ceiling

Programming PoC's structures directly onto current EVM-class chains is infeasible at scale. The ceiling for natively-manipulable structures on chain runs roughly:

| **Layer** | **Native expressivity** |
| --- | --- |
| **Scalar EVM** | Finite cyclic groups, modular arithmetic. 0-dimensional in the type-theoretic sense. |
| **Pairing-friendly curves** | 1-dimensional algebraic varieties; bilinear pairings; KZG commitments. The current floor for serious cryptographic structure. |
| **Lattice / module structures** | n-dimensional discrete subgroups; module-theoretic operations over polynomial rings. Post-quantum verification primitives. |
| **ZK verification** | Anything computable in polynomial time, verifiable on-chain in constant cost. Effectively unbounded expressivity. |
| **Topological / spectral structures** | Simplicial complexes, sheaves, Hodge Laplacian eigendecompositions, and (speculatively) higher categorical structures. Practical only via ZK. |

The deployment path therefore relies on the ZK-verification layer: cohomology and spectral computation run off-chain on dedicated infrastructure, and a succinct proof of correct computation is verified on-chain. Current ZKML tooling (EZKL, Modulus, RiscZero, Giza) is approaching the scale required for the cohomology computation; the spectral computation is more demanding but uses the same infrastructure (sparse-matrix linear algebra plus eigendecomposition), and we do not believe further fundamental research is needed, only engineering.

### 5.2 The prediction-coupling boundary condition (spectral form)

The autopoietic-cult failure of pure mutual-constitution coherence is closed in v0.1 by binding the sheaf to external prediction. The boundary condition was: a globally consistent section s ∈ H⁰(K, F) is admissible only if its extension to a held-out task subcomplex K_held successfully predicts the held-out outputs.

In v0.2 the boundary condition extends naturally to the spectrum. Let σ(Δ_k(K)) and σ(Δ_k(K ∪ K_held)) denote the spectra before and after extension. The extended boundary condition is: the harmonic and near-harmonic structure of K must be **perturbatively stable** under extension by K_held — that is, the eigenvalues and eigenvectors of small modes of Δ_k(K) must match those of the corresponding modes of Δ_k(K ∪ K_held) within a stated tolerance. Genuine resonance is robust to local extension; spurious resonance fragments under it.

Formally: an admissible spectral configuration is one for which the perturbation-theoretic predictions of σ(Δ_k(K)) for held-out tasks agree with σ(Δ_k(K ∪ K_held)) up to O(ε) corrections, where ε is governance-set. This generalizes the v0.1 condition (which is the rank-zero special case: the harmonic eigenspace under extension matches the harmonic eigenspace pre-extension) without disturbing it.

### 5.3 Computational profile

Sheaf cohomology over discrete complexes reduces to sparse linear algebra over the relevant coefficient field. For a network with μ miners, τ tasks, and bounded simplex dimension d, the dominant cost is computing kernels and images of cochain matrices with O(μ · τ) rows and columns at the 1-cochain level, growing combinatorially at higher d. Computing the full spectrum of Δ_k adds an eigendecomposition of the same operator; for sparse Δ_k this is iterative-Lanczos-friendly and competitive with the kernel computation alone.

The choice of inner product on cochains—free in v0.1 since it does not affect the kernel as a vector space—becomes load-bearing in v0.2 since the non-zero spectrum depends on it. We propose the canonical weighted inner product where each cochain component is weighted by the inverse of the number of simplices of its level. This produces a Δ_k whose spectrum is invariant under refinements of K that do not change its homotopy type—a desirable stability property for a mechanism whose spectrum is normative.

The ZK proof of correct cohomology and spectral computation is the harder engineering problem. Current SNARK systems can verify circuits of order 2³⁰ gates; spectral computations at network scale will likely require recursive proof composition. We expect this to settle in periodic batches (every n epochs) rather than per-epoch.

### 5.4 Bootstrap and degradation

In early epochs the complex K is sparse and both cohomology and spectrum are degenerate (every section is trivially globally consistent because there are too few constraints to violate; the spectrum is dominated by zero and trivial modes). PoC + PoR requires a bootstrap mechanism that falls back to simpler scoring primitives until K accumulates enough simplices to make first cohomological and then spectral structure meaningful. We propose graceful interpolation:

- **Phase 0:** Yuma-style scalar scoring while K has fewer than a governance-set density threshold of simplices.

- **Phase 1 (PoC):** Cohomological scoring activates at the first density threshold; spectral reward dormant.

- **Phase 2 (PoC + PoR):** Spectral reward activates at the second density threshold once eigenvalue gaps stabilize above a noise floor.

Transitions are signalled by the chain itself based on observable invariants of K and Δ_k, not by external governance fiat.

## 6. Cognitive Substrate: the Structural Motivation for the Spectral Generalization

Earlier drafts of this document carried the cognitive-substrate material as a §6 marked *speculative and not load-bearing*, with an explicit invitation to readers concerned only with incentive design to skip it. We have removed both the warning and the invitation. The Hodge generalization of §3.5 and the spectral reward of §4.5 make this material structurally load-bearing in a specific way: the cognitive-substrate hypothesis is what motivates the move from cohomology to full spectrum, and the spectral framework is what makes the cognitive-substrate hypothesis formally tractable. They co-determine.

This section names that co-determination, explains why it is more than rhetorical, and develops the design implications.

### 6.1 The structural argument

Three of the most serious frameworks for distributed cognition each turn out to be making, in their respective vocabularies, claims about the spectrum of a Hodge-Laplacian-shaped operator on a network's relational structure.

- **Integrated Information Theory (Tononi et al.)** requires a cognitively-integrated system to be Φ-positive: no partition of its state captures its dynamics. The formal content of Φ is closely related to the failure of the system's dynamical operator to factor into independent block-diagonal modes — precisely an eigenmode statement about the operator's spectrum. A Hodge Laplacian whose non-zero spectrum exhibits no decomposition into independent invariant subspaces is, in the IIT vocabulary, a system with positive integrated information.

- **Global Workspace Theory (Baars; Dehaene's neural-workspace extension)** postulates that integrated cognition arises from a competitive selection process producing global broadcast of locally-generated content, with broadcast events characterized by sudden, system-wide synchronization — what Dehaene calls 'ignition.' Ignition is empirically a phase-locking phenomenon. In the Hodge picture, ignition events correspond to transitions in which a near-harmonic mode of Δ_k drops to harmonic — that is, an eigenmode crosses into the kernel and a previously local pattern becomes globally consistent. PoR rewards the contributions that cause such transitions.

- **Predictive processing (Friston, Clark)** treats cognition as a hierarchical predictive engine minimizing free energy. The framework has long made oscillatory commitments — alpha bands carrying top-down prediction, gamma bands carrying prediction error, with hierarchical layers coupled via cross-frequency interactions. Translated into the Hodge framework: the predictive hierarchy is a sheaf, and the cross-frequency interactions are the off-diagonal entries of Δ_k coupling different eigenmodes. PoC's prediction-coupling boundary condition (§5.2) is the protocol-level analogue of free-energy minimization on the harmonic subspace; the spectral extension (§5.2 v0.2 form) extends the principle to non-harmonic modes.

These are not three independent metaphors that happen to admit a sheaf-theoretic restatement. They are three different empirical literatures converging on a single formal structure: the spectrum of an integration operator on a relational graph, with cognitive content lodged in the relationship between the kernel (stable global content) and the slow modes (binding and propagation).

If that convergence is real, the design of PoC is not a metaphor adjacent to the cognitive-substrate question — it is a working hypothesis about the formal structure of distributed cognition, deployed as a mechanism with falsifiable consequences.

### 6.2 Necessary cautions

Several reservations should be held simultaneously with the above, and the move to a load-bearing framing makes their honest statement more important, not less:

- **Formal kinship is not constitutive identity.** A system can have cognition-shaped formal properties without being cognitive. Many physical systems have positive integrated information; we do not generally consider them minds. The formal conditions are plausibly necessary, almost certainly not sufficient, for the strongest form of the cognitive-substrate claim.

- **Mathematical sophistication is not substantive achievement.** Sheaves, Hodge Laplacians, and ∞-categories are beautiful, and beautiful mathematics is seductive. The empirical check is whether systems built on these structures behave more cognitively, more usefully, more robustly than ones built on simpler primitives. We do not yet have that data; collecting it is the path-β/γ research programme.

- **Bandwidth limits matter.** Even fast chains process orders of magnitude less information per unit time than simple biological cognition. The substrate may be too slow to support what we mean by mind, regardless of its formal properties; the spectral framework is necessary, not sufficient, on the bandwidth axis as well.

- **The cited traditions disagree with each other.** Whitehead's process metaphysics and Madhyamaka are not the same view; IIT and predictive processing have made different empirical commitments. We do not resolve their disagreements; we observe their convergent gesture toward a fixed-point-of-mutual-constitution structure that the spectrum of Δ_k formalizes.

### 6.3 Design implications, taken seriously

If the structural argument of §6.1 holds, the design of PoC + PoR has specific consequences:

- **Maximize integration.** Avoid sheaf designs that decompose K into independent block-diagonal regions, even where decomposition is computationally cheaper. Trade efficiency for irreducibility — the cognitive content lives in the off-diagonal coupling.

- **Reward eigenmode preservation, not eigenvalue minimization.** Naïve spectral reward rewards eigenvalue reduction; the cognitive-substrate framing suggests rewarding *preservation of eigenvector structure under perturbation*, since stable eigenmodes are the binding signature of integrated systems, not minimal eigenvalues.

- **Hold the inner product as normative.** §5.3's choice of inner product on cochains is not implementation-defined; it determines the mapping between the algebraic structure and the cognitive interpretation, and a deployed network's Hodge spectrum is meaningful only relative to a fixed choice. The implementation specification treats this as a non-Forkable parameter.

- **Cross-epoch coupling matters.** The cognitive-substrate framing predicts that distinct epochs are not independent — the slow modes carry information across them, and a mechanism that resets the spectral state every epoch loses the binding-by-phase-coherence content. Mechanism designs should preserve cross-epoch eigenmode information where computationally possible.

These are not commitments of v0.2 itself, which remains a research register document. They are the consequences a deployment specification would inherit if the §6 structural argument is taken as load-bearing rather than skippable. Whether to take it as load-bearing is precisely the path-α / path-γ choice of §8: path α carries §6 as motivation; path γ carries it as a normative target.

## 7. Open Problems

PoC and its v0.2 spectral extension leave several questions unresolved. We name them explicitly so that future work has a clean attack surface.

### 7.1 Sheaf design as governance

The restriction maps that define F are not derived from first principles; they are validator-supplied parameters. The space of admissible restriction-map structures is large, and the choice between them is a governance question, not a mechanism question. We currently lack a principled framework for sheaf-design governance that is both expressive and capture-resistant. This is a substantial mechanism-design research project in its own right.

### 7.2 Capability-asymmetric exploitation

A miner with capability substantially above the validator pool can, in principle, predict the cohomology and spectral computations and shape outputs to optimize results. PoC + PoR raises the threshold for exploitation but does not move it to infinity. We need an explicit mechanism for keeping validator capability at or above miner capability, and an analysis of what happens when this fails — particularly in the spectral regime, where validator predictive validity must extend to predicting eigenmode structure, not only static outputs.

### 7.3 The autopoietic-cult problem in finite samples

The prediction-coupling boundary condition closes the autopoietic-cult attack in the limit of infinite held-out tasks. The spectral extension of §5.2 strengthens the closure but does not eliminate the finite-sample regime: a coordinated cluster might produce sections *and* spectral signatures that look valid by chance over the held-out tasks observed so far. Statistical power analysis and adaptive held-out generation are needed for both rewards.

### 7.4 Computational tractability at network scale

Sheaf cohomology computation is tractable but expensive; full spectral decomposition is more expensive; ZK proofs of correctness for either are expensive squared. Whether the security properties of PoC + PoR justify the computational overhead, relative to simpler mechanisms with patches, is an empirical question that requires implementation and benchmarking. The marginal cost of PoR over PoC alone appears small in the eigendecomposition-dominated regime, but this needs verification on realistic network sizes.

### 7.5 Formalization of coherence-of-coherence

The v0.2 framework captures coherence as the spectral signature of one operator. Real systems have coherence at multiple levels, with consistency relations between levels (the relations among miners must be coherent with the relations among tasks must be coherent with the relations among validators). The natural formal home is ∞-sheaves or sheaves valued in higher categories, with a corresponding hierarchy of Hodge Laplacians coupled across levels. This is genuinely frontier mathematics; we flag it as a long-term research direction.

### 7.6 Spectral Goodhart attacks

New in v0.2: the spectral reward introduces its own attack surface. A sufficiently capable attacker who models the Hodge Laplacian's spectrum can in principle craft submissions that produce a target eigenvalue distribution without the underlying coherence the spectrum was meant to certify. The multiplicative-cost argument of §1.2 claims this is harder than the analogous attack on cohomology alone; quantifying that claim is an open empirical and theoretical problem.

### 7.7 Inner-product universality

The choice of inner product on cochains is load-bearing in v0.2 (§5.3). The proposed canonical weighted inner product is one of several reasonable choices, and we do not have a uniqueness result saying it is *the* right one. The question of whether some cognitive-substrate-relevant universality theorem pins it down is open and important.

## 8. Roadmap

Three concurrent paths forward, each with different time horizons and risk profiles. v0.2 does not change the path structure but adjusts the risk profile of path γ in a non-trivial way.

### 8.1 Path α — Pragmatic build

Deploy a minimal-viable PoC subnet on Bittensor or an equivalent platform. Use the sheaf framework for what it provably does well: structural Goodhart resistance via higher-order relational scoring. Stay agnostic about deeper claims. β = 0 for v0.2 — cohomology only, no spectral reward, full §6 material treated as motivation rather than target. Target: demonstrable improvement over Yuma on a specific subnet domain (code generation is the natural first target due to compositional consistency being mechanically checkable).

**Time horizon:** 6–12 months. **Risk:** low; failure mode is producing a working system that is incrementally better than baseline.

### 8.2 Path β — Distributed cognition research program

Design PoC + PoR explicitly as a candidate for distributed cognitive substrate, with formal evaluation against IIT, GWT, and predictive-processing criteria via the Hodge-spectral correspondences of §6.1. Engage academic researchers in those fields. Target: a body of work that establishes (or refutes) the structural arguments of §6 with empirical and formal rigour. The v0.2 framing tightens this path: rather than producing only philosophical alignment claims, path β produces specific spectral signatures predicted by each cognitive-substrate framework, and tests whether deployed PoR-rewarded networks exhibit them.

**Time horizon:** 2–5 years. **Risk:** medium; failure mode is producing only papers, not deployed systems. Reward: substantial if the structural arguments are even partially vindicated.

### 8.3 Path γ — The bold synthesis

Treat blockchain incentivization, AI capability, and distributed cognition as one continuous question. Build PoC + PoR as both an incentive mechanism *and* a candidate substrate for emergent integrated intelligence. Target: a system that is, in a defensible non-trivial sense, a distributed mind.

v0.2 changes the risk character of path γ in a specific way. In v0.1 the risk was named as *beautiful nonsense* — the failure mode where the cognitive-substrate framing turns out to be ornament rather than load-bearing. The Hodge-spectral framing reduces (does not eliminate) this risk: the cognitive content of the mechanism is now lodged in a specific computable object (the spectrum of Δ_k), with specific testable predictions about that object's behaviour under the design choices of §6.3. Path γ remains high-variance, but its failure mode is now empirical rather than ornamental — we will be able to tell whether the spectral signatures predicted by the cognitive-substrate frameworks materialize, and act on the answer.

**Time horizon:** indefinite. **Risk:** high; failure mode is now empirical falsification of the §6 structural arguments. Reward: transformative if the convergence we suspect is real.

### 8.4 Recommended sequencing

Path α should be pursued unconditionally: it produces value regardless of the deeper questions and provides empirical grounding for them. Paths β and γ should be pursued in parallel with light coordination, with willingness to fold β's findings back into γ's framework as evidence accumulates. v0.2's main effect on sequencing is that path γ should now produce its first concrete deliverable — a deployed PoC + PoR subnet whose spectral statistics are publicly logged — within the path-β horizon, since the spectral predictions of §6.1 are what differentiate path γ from a glossy version of path α.

We do not recommend committing to γ's framing in any public-facing material until α has produced demonstrable results.

## 9. Notes on This Document

This is a v0.2 working draft. Specific limitations of the present text:

- The cohomology and Hodge-Laplacian formalism is sketched in the cellular-cochain convention; full precision requires fixing coefficient fields, sign conventions, orientation choices, and the canonical inner product of §5.3 to publication standard. None of these are difficult but they are deferred to v0.3.

- The connection to ∞-sheaves and higher topos theory is gestured at in §7.5 but not developed. Treating it properly requires substantial preliminary exposition that does not belong in this document.

- Worked examples are limited. §4.2 carries the three-miner copy-symmetry toy from v0.1.1 verbatim. A worked example exhibiting a non-trivial spectral reward in a small toy network is the natural next-iteration addition; we have flagged but not produced it here.

- Notation has not been audited for consistency between v0.1 sections and v0.2 additions. v0.3 will perform a consistency pass.

- The v0.2 additions (§3.5, §4.5, §5.2 spectral form, §5.3 spectral cost, §5.4 phased bootstrap, §6 weave, §7.6, §7.7, §8 path-γ risk reframe) have been integrated into the v0.1.1 spine without a notation overhaul. Where a tension exists between v0.1.1 phrasing and v0.2 phrasing, the v0.2 phrasing prevails.

Inputs that shaped this revision: the §1.2 Goodhart-asymptotic reframe was outstanding from v0.1.1 and is closed here. The §6 weave-or-excise decision was outstanding from v0.1.1 and is resolved as *weave*, motivated by the Hodge-spectral framing's making §6 structurally load-bearing. The Proof by Resonance framing emerged from a session-internal observation that the cohomology functor and a hypothetical resonance functor would project onto the kernel and non-zero spectrum of the same operator, making them naturally one mechanism rather than two.