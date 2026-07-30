---
layout: document
title: "Gluing the Gates"
subtitle: "Holarchy and the Obstruction to Composing Combination Proofs"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /gluing-the-gates/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-07-30
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Mechanisms nest, and the framework has no theory of nesting. Koestler's holon supplies the structure, cellular sheaves supply the mathematics it always lacked, and the obstruction to composing conjunction-gated mechanisms is a cohomology class — every department hitting its metrics while the firm fails turns out to be contextuality, in Abramsky's exact sense. Absent that gluing, a holarchy's security is the minimum over its levels rather than the product."
status: "v0.1 · working draft"
order: 11
---

## Abstract

Combination Proofs are defined for a mechanism and its participants. They are not defined for a mechanism whose participants are themselves mechanisms, and every deployment of consequence has that shape: miners inside subnets inside networks, agents inside firms inside economies. This paper supplies the missing composition theory. Its structural frame is Koestler's holon — the entity that is a whole looking down and a part looking up — and its central observation is that cellular sheaves are the mathematics holarchy has lacked since 1967: the stalk is the holon as whole, the restriction map is the holon as part, and a global section is the holarchy integrated. Three results follow. First, conjunction-gating does *not* survive nesting: a mechanism whose projections aggregate its constituents' scores can pass while a constituent fails, and — the more dangerous direction — every constituent can pass while the whole fails. Second, the obstruction is cohomological. When gate conditions are affine on stalks, local admissible assignments glue into a global one exactly when a class in H¹ of the gate sheaf vanishes, and dim H¹ counts the independent ways a holarchy can satisfy every local gate and no global one. Third, richness does not compose: measurement reports that ρ varies continuously with the density of couplings *between* levels while the levels themselves are unchanged, so ρ of a holarchy is not a function of the ρ of its holons. The three combine into the paper's claim: unless the gates glue, a holarchy's Goodhart-asymptotic security is the *minimum* over its levels rather than the product, because an adversary chooses which level to attack. The vanishing of H¹ is exactly what converts that minimum back into a product.

---

## 1. The Composition Problem

The framework states its claims for a mechanism M, a substrate 𝒮, and a set of participants who submit to M. It says nothing about what happens when a participant is not an agent but a mechanism.

This is not an exotic case. It is the ordinary one. A miner participates in a subnet which participates in a network. A validator set is a mechanism inside a consensus mechanism inside a protocol. A firm's department runs an incentive scheme, and the firm runs an incentive scheme over its departments, and the market runs one over firms. The framework's own worked instance — a coherence complex over miners, validators, and tasks — is already a system in which the entities being scored have internal structure the score does not see.

The framework's only compositional apparatus is Definition 5.2, the substrate order ≼. That relation asks whether every intrinsically verifiable projection of one substrate admits a refinement on another, and it answers a question about *substitutability*: which migrations between substrates preserve guarantees. It is a statement about upgrade paths between mechanisms, not about mechanisms stacked inside one another. Nothing in the framework as it stands rules on whether a Combination Proof of Combination Proofs is a Combination Proof.

Neighbouring fields have confronted their versions of this and answered them. Canetti's universally composable security framework [1] establishes a composition theorem strong enough that protocols proved secure in isolation remain secure under arbitrary composition, by way of a subroutine-substitution operation generalised from sequential algorithms to distributed protocols. In mechanism design, Syrgkanis and Tardos [2] identify a class of *smooth* mechanisms for which, in their formulation, smoothness locally at each mechanism implies efficiency globally, giving efficiency guarantees that survive players participating in many mechanisms at once.

Both results have the same shape, and the shape is worth naming: they are local-to-global theorems. They establish that a property verified on parts extends to a property of the whole, under stated conditions, and they are precise about the conditions because without them the extension fails. That is exactly what a sheaf is for, and the coincidence is not decorative — it is the hint this paper follows.

The question, then, is narrow and answerable. Let M be a mechanism whose participants are mechanisms M₁, …, M_m, each a Combination Proof on its own substrate. Under what conditions is M a Combination Proof? The answer is that the conditions are not automatic, that their failure has a specific and familiar signature, and that the obstruction to them is computable from data the framework already requires a mechanism to hold.

---

## 2. Holons, and the Mathematics They Lacked

Arthur Koestler introduced the *holon* in *The Ghost in the Machine* [3] and developed it into a numbered canon of self-regulating open hierarchic order [4]. The definition is that a holon is a member of "a multi-levelled hierarchy of semi-autonomous sub-wholes," displaying autonomous and dependent properties at once — what Koestler called the **Janus phenomenon** (his 1.4), after the god with two faces. Looking downward, a holon is a whole with its own integrity. Looking upward, it is a part subordinate to something larger. Neither face is the illusion.

A **holarchy** is the resulting structure: holons as nodes joined by channels of communication and control, characterised by *depth* — the number of levels — and *span*, the number of holons per level (2.1). Every holon carries two opposed tendencies (4.1): the **self-assertive**, its drive to "preserve and assert its individuality as a quasi-autonomous whole," and the **integrative**, its drive to "function as an integrated part of an (existing or evolving) larger whole." Holarchies are not pure trees. They **arborise** — branching vertically — and simultaneously **reticulate**, the branches interlocking horizontally into networks (6.1).

Koestler was also precise about failure, and his two pathologies are the two ways a holarchy can die. Under **excessive self-assertion** (9.4), an over-excited holon "assert[s] itself to the detriment of the whole" and monopolises functions that were not its own. Under **excessive integration** (9.5), weakened coordinating powers "erode their autonomy and individuality," and the holons regress into undifferentiated identification with the mass.

The concept has had a long practical career without a mathematics. Holonic manufacturing took it up as an architecture — the PROSA reference architecture of Van Brussel and colleagues [5] organises production control into product, resource, order, and staff holons, and remains the most-cited scheme in that literature — but the formalism there is object-oriented and architectural, not algebraic. Koestler gave systems theory a vocabulary and left it without a calculus.

**The claim of this section is that cellular sheaves are the missing calculus, and that this program has been writing holarchy theory for four documents without using the word.**

| Koestler | cellular sheaf 𝓕 over a complex K |
|---|---|
| holon as whole (self-assertive) | the stalk 𝓕(v) — its own internal state space |
| holon as part (integrative) | the restriction map F_{v◁e} — how it must present at an interface |
| the holarchy integrated | a global section |
| how many integrations exist | H⁰(K, 𝓕) |
| unresolved self-assertion | H¹(K, 𝓕), the obstruction to gluing |
| depth and span (2.1) | the complex's stratification and its branching |
| arborisation and reticulation (6.1) | the tree skeleton and the cross-edges over it |
| excessive self-assertion (9.4) | H⁰ = 0: no global section survives |
| excessive integration (9.5) | duplication-invariance: every stalk collapses to one value |

The identification is not merely notational, because the sheaf side of the table is quantitative where Koestler's side was not. Hansen and Ghrist [6] show that the sheaf Laplacian implements a consensus algorithm whose convergence rate is governed by spectral properties, and in their treatment of opinion dynamics on discourse sheaves [7] the sheaf Laplacian is precisely what "registers the discord in the system." Koestler's integrative tendency, which he could only describe, has a spectrum.

The final row of the table is worth dwelling on, because it is a retro-fit rather than a proposal. The negentropy paper's test suite demands that reward be *not invariant under duplication* of a section, on the reasoning that if a copy earns what the original earns then the identity gauge is unfixed and the cost argument leaks. Read holonically, duplication-invariance is Koestler's second pathology exactly: a holarchy in which no holon retains a distinguishing interior, every level collapsed into its neighbours. The program built a guard against excessive integration before it had a name for it.

---

## 3. Nesting

We fix notation for the composite object. Throughout, 𝒮 and its projections are as in the framework's §2, and K is a complex whose vertices index holons.

**Definition 3.1 (Holonic substrate).** A substrate 𝒮 is *holonic over K* if each vertex v of K is assigned a sub-substrate 𝒮_v, each edge e = {u, v} is assigned an *interface* substrate 𝒮_e together with maps 𝒮_u → 𝒮_e ← 𝒮_v recording how each holon's state is visible at the interface, and the state space of 𝒮 is the space of assignments s : v ↦ s_v ∈ 𝒮_v.

**Definition 3.2 (Induced mechanism).** Let M_v be a Combination Proof on 𝒮_v with projections π^v₁, …, π^v_{K_v}, gate thresholds t^v_i, and reward r_v. A mechanism M on 𝒮 is *induced* by {M_v} if each of M's projections is a function of the constituent scores {π^v_i(s_v)} and of the interface data alone.

**Definition 3.3 (Gate sheaf).** For a holonic substrate and induced mechanism, the *gate sheaf* 𝓖 assigns to each vertex v the subspace of 𝒮_v on which every constituent gate is satisfied — the states with π^v_i(s_v) ≥ t^v_i for all i — and to each edge the image of that subspace at the interface, with the restriction maps inherited from Definition 3.1.

A global section of 𝓖 is an assignment of states to holons that satisfies every local gate *and* agrees at every interface. That is the object the composition question is about.

**Definition 3.4 (Compositional mechanism).** An induced mechanism M is *compositional* if M's gate is satisfied precisely when 𝓖 admits a global section — that is, when local admissibility everywhere and interface agreement everywhere together imply, and are implied by, admissibility of the whole.

Compositionality is what one would like and is not what one gets for free. The remainder of the paper is about the gap.

---

## 4. Gates Do Not Glue

The framework's conjunction-gating condition — that reward vanish whenever any projection falls below its threshold — is what makes a Combination Proof a conjunction rather than a weighted sum, and it is the source of the multiplication claim. It does not survive nesting automatically, and it fails in both directions.

**Proposition 4.1 (Aggregation breaks the gate).** Let M be induced by {M_v} with a projection π defined by aggregation — π(s) = g({π^v_i(s_v)}) for g monotone in each argument and strictly increasing in at least two. Then M is not compositional.

*Sketch.* Strict monotonicity in two arguments gives, for any target value of π, a family of preimages along which one constituent's score falls while another's rises. Choose a member of that family in which the first constituent falls below its own threshold t^v_i. Its reward under M_v is zero by conjunction-gating, but its contribution to π is merely reduced, and the compensating rise elsewhere restores π above M's threshold. So M's gate passes on a state where a constituent's gate fails. ∎

This is the direction that is usually noticed, and it is the milder one. An aggregate score lets a healthy majority carry a failing member — which is sometimes what one wants, and is at any rate visible from above.

The other direction is not visible from above, and it is the one that matters.

**Proposition 4.2 (Local pass, global fail).** There exist holonic substrates and induced mechanisms in which every constituent gate is satisfied and no global section of 𝓖 exists.

*Sketch.* Take K a cycle of three holons with one-dimensional stalks and restriction maps that compose around the cycle to a non-identity scalar. Each holon independently admits states satisfying its gate; the interface conditions require agreement pairwise; and the composite around the cycle requires a state equal to a non-unit multiple of itself, which forces zero, which the gate excludes. Each holon is locally healthy. The holarchy admits nothing. ∎

Proposition 4.2 is the formal content of an observation that is otherwise anecdotal: every department hits its metrics and the firm fails. Nothing is wrong at any level. The incompatibility lives in the interfaces, which is precisely where no level is looking, because each level's gate reads its own stalk.

This structure is not new, and it is worth naming its home, because the mechanism-design reading of it appears to be the only novel part. Abramsky and Brandenburger [9] characterise quantum non-locality and contextuality *precisely* as the obstruction to extending local sections to a global one: a family of measurements each of which admits a consistent local assignment, with no assignment consistent across all of them. **Proposition 4.2 says that a non-compositional holarchy is contextual in exactly that sense.** The department that hits its metrics and the firm that fails stand in the same relation as the local measurement outcomes and the absent joint distribution, and they are obstructed by the same mathematics. A mechanism designer who finds every level healthy and the whole sick is looking at a Bell-type phenomenon in an economic system.

The obstruction has a name, and the literature that named it also supplies the caution.

**Claim 4.3 (The obstruction is cohomological).** Suppose the gate conditions are affine on the stalks — each admissible subspace is a coset of a linear subspace — so that 𝓖 is a sheaf of affine spaces over a sheaf of vector spaces 𝓖₀. Then a family of locally admissible states extends to a global section if and only if an associated Čech class in H¹(K, 𝓖₀) vanishes, and dim H¹(K, 𝓖₀) bounds the number of independent ways a holarchy can satisfy every local gate while admitting no global one.

We label this a claim rather than a proposition because the affine hypothesis does real work and we have not established how far it can be relaxed. For gates that are genuinely non-linear — a threshold on a spectral quantity is not affine — the correct object is a sheaf of sets, whose gluing obstruction is non-abelian and not measured by an H¹ in the ordinary sense. What can be said without the hypothesis is weaker and still useful: the obstruction is a property of the *interfaces*, it is invisible to any single level, and it is computable from data a mechanism already holds if it holds the interface maps at all.

The established literature also supplies a sharper caution than our hedging did. Abramsky, Mansfield and Barbosa [10] construct precisely such an invariant for the contextuality setting — a Čech class on an abelian presheaf derived from a model's support — and prove that the class vanishes when a global section exists, but that its non-vanishing is *sufficient and not necessary* for contextuality. There are obstructed families the cohomology does not see. We should expect the same asymmetry here, and state its consequence for design plainly: **a non-vanishing obstruction is grounds to redesign the interfaces, but a vanishing one is not a certificate that the gates glue.** The invariant is a detector of composition failure, not a proof of composition safety. That is a weaker guarantee than the phrasing of Claim 4.3 suggests, and the weaker reading is the one to build on.

Two consequences are worth stating.

**The design implication.** A super-mechanism should define its projections as *sections* rather than as *aggregates*. A projection that reads whether the constituents' states glue is compositional by construction; a projection that averages their scores is not, by Proposition 4.1. This is a sharper instruction than "measure the right thing," because it names the failure mode of the wrong thing.

**The limit of the guarantee.** The negentropy paper is careful that H¹ = 0 certifies coherence, not truth: a consistent fiction glues as well as a fact. The same caution applies here and should be stated in the same words. **H¹ = 0 certifies that the levels compose, not that any level is honest.** A holarchy of uniformly corrupt holons whose corruptions agree at every interface has vanishing obstruction and admits a global section. Compositionality and honesty are different guarantees, and this paper supplies only the first.

---

## 5. Richness Is a Property of the Holarchy, Not of the Holons

Definition 5.1 of the framework makes richness ρ the supremum, over collections of intrinsically verifiable projections, of the size of any pairwise approximately independent subset. It is stated for a substrate. The composition question asks what it does when substrates nest, and the natural guess — that a holarchy's richness is determined by its holons' — is false.

The evidence is measurement rather than argument. On a nested complex built to model holons modelling holons, the spectral dimension of the sheaf Laplacian varies continuously with the density of couplings *between* blocks while the blocks themselves are left unchanged: d_s runs 1.26, 1.62, 1.82, 1.95, 2.12, 2.23 as cross-links per merge go 1, 2, 3, 4, 6, 8. The holons are identical across that sweep. Only the reticulation changes, and richness moves by three-quarters of a dimension.

**Observation 5.1.** ρ of a holonic substrate is not a function of the ρ of its constituent substrates. Richness lives in the coupling between levels, not in the levels.

Koestler's vocabulary sharpens this into something usable. Arborisation and reticulation are his two structural principles (6.1), and they contribute differently: arborisation supplies *depth*, the number of levels a holarchy can sustain, while reticulation supplies *richness*, the number of independent projections its structure can carry. A pure tree is poor. A tree with cross-links is not.

But reticulation cannot simply be maximised, and the measurement says so. As coupling density rises the power law degrades — the fit that holds to a part in a thousand at moderate coupling loosens as the structure grows expander-like and the levels stop being distinguishable from one another. That is Koestler's second pathology arriving as a change in a fitted exponent: a holarchy so tightly integrated that it is no longer a holarchy, merely a mass.

**Conjecture 5.2 (Koestler's balance is measurable).** For a holonic substrate parameterised by reticulation density, there exists an interior optimum at which ρ is maximised subject to the spectral power law remaining clean — and this optimum is the formal content of Koestler's claim that health lies in the balance of the self-assertive and integrative tendencies rather than in the triumph of either.

The conjecture is stated in a form that can be refuted with the instrument that produced the sweep above, by scanning reticulation density on a fixed holon population and looking for an interior maximum of ρ against a monotone degradation of fit. If the optimum is at the boundary, the conjecture is wrong and Koestler's balance is not a richness statement.

---

## 6. Goodhart Across Levels

Manheim and Garrabrant [8] distinguish four mechanisms by which optimising a proxy breaks it: **regressional**, where the proxy differs from the target by noise that selection then exploits; **extremal**, where optimisation carries the system into a regime in which the proxy's relationship to the target no longer holds; **causal**, where intervening on the proxy fails to move the target because the correlation was not causal; and **adversarial**, where an agent manipulates the proxy directly.

The framework's Goodhart-asymptotic property is a claim about the fourth, and the composition question is what becomes of each under nesting. They do not fare alike.

*Regressional* Goodhart composes mildly. Independent noise across many holons partially averages, and a super-mechanism reading aggregates sees less of it than any constituent does — one of the few places where aggregation helps.

*Extremal* Goodhart compounds. Each level optimises its own proxy, and each level's optimisation carries the substrate further into the tail where the next level's proxy was never calibrated. A holarchy of locally well-behaved optimisers is a machine for reaching regimes none of them was specified in.

*Causal* Goodhart is where level-crossing bites hardest, because the interfaces are exactly where the causal structure is least documented. A super-mechanism intervening on a constituent's score is intervening through an interface it did not model.

*Adversarial* Goodhart admits the sharpest statement, and it is the paper's punchline.

**Proposition 6.1.** Let M be induced by {M_v} and let an adversary choose freely which level to attack. If M is not compositional, the Goodhart-asymptotic security of M is bounded above by the minimum over levels of the constituent securities, not by their product.

*Sketch.* Non-compositionality means, by Proposition 4.2's direction, that M's gate can be satisfied without every constituent's being satisfied, or that M's own gate reads a state its constituents' gates do not constrain. Either way there exists a level whose gate is the binding one for some attack, and the adversary selects it. The cost of the cheapest attack is the cost of defeating that single level. No conjunction across levels is enforced, so no multiplication across levels occurs. ∎

This is the composition analogue of the framework's own central asymmetry, and it inverts the framework's good news. Within a level, conjunction-gating makes fake-costs multiply. Across levels, absent compositionality, they do not even add — the adversary simply picks the weakest.

**Corollary 6.2.** If M is compositional — equivalently, under the hypothesis of Claim 4.3, if the gate sheaf's obstruction vanishes — then a successful attack must produce a global section, and so must defeat every level's gate simultaneously at every interface. The conjunction is restored, and with it the multiplication.

The vanishing of H¹ is therefore not a technical nicety. It is the precise condition under which a holarchy's security is the product of its levels rather than the minimum of them, and the whole practical content of the framework at scale rests on it.

---

## 7. What Is Declined

Several things this paper could have claimed and does not.

**A universal composition theorem.** Canetti's framework delivers arbitrary composition under a single strong hypothesis. Nothing here is that strong. This paper identifies an obstruction and states the condition for its vanishing; it does not exhibit a composition operation under which Combination Proofs are closed.

**Holarchy as a substrate.** The temptation is to stake holonic balance itself — to denominate value against a system's being neither fragmented nor totalised. That would be a new substrate and would need the treatment the program gives substrates, beginning with whether its projections admit intrinsic verifiers. This paper treats holarchy as *structure*: how mechanisms nest, not what they stake.

**Non-affine gates.** Claim 4.3 assumes affine gate conditions. The framework's own worked instance gates on a spectral quantity, which is not affine, and the honest position is that the cohomological statement is a model of the general case rather than the general case.

**Anything built.** The measurement reported in §5 is on a toy nested complex, not on a deployed one. The cycle in Proposition 4.2 is a construction, not an observation of a live system failing.

**Truth.** As §4 says in the negentropy paper's words: what is certified is that the levels compose, not that any level is honest.

---

## 8. Open Problems

**8.1. Relaxing affineness.** For gates that are threshold conditions on non-linear projections, the gluing obstruction lives in a non-abelian setting. Whether a useful invariant survives — an obstruction class, a bound on failure modes, anything computable — is the first thing this paper's central claim needs. The most promising route is the one the contextuality literature already took: work with a presheaf of *distributions* over the admissible sets rather than with the sets themselves, recovering an abelian object without linearising the gates [9, 10]. A parallel construction exists for distributed computing, where the cohomology of a task sheaf encodes the obstructions to solving a task [11]; whether a gate sheaf is a task sheaf in that sense is a concrete question with a concrete answer.

**8.2. Does ρ have a composition law at all?** Observation 5.1 says richness is not a function of constituent richness. It does not say richness is unconstrained. Bounds of the form ρ(M) ≤ F({ρ(M_v)}, reticulation) would convert the observation into a design tool.

**8.3. Depth versus span.** Koestler's two structural measures should have distinguishable consequences for the framework's quantities, and the sweep in §5 varied neither: it varied reticulation at fixed depth and span. What a holarchy gains from being deeper rather than wider is unmeasured.

**8.4. The interface as the verifiability boundary.** The framework's §7.2 asks which projections admit intrinsic verifiers. §4 here locates every composition failure at the interfaces. Whether interfaces are systematically harder to verify intrinsically than stalks — whether the verifiability boundary and the composition obstruction are the same boundary — would connect two open problems into one.

**8.5. Adversary-positivity under nesting.** The framework's §4 establishes conditions under which failed forgery subsidises the substrate it attacks. Whether residue harvested at one level is harvestable at the level above is unaddressed, and the answer plausibly depends on the same interface maps as everything else in this paper.

---

## References

[1] R. Canetti. *Universally Composable Security: A New Paradigm for Cryptographic Protocols.* FOCS, 2001. (Cryptology ePrint Archive 2000/067.)

[2] V. Syrgkanis and É. Tardos. *Composable and Efficient Mechanisms.* arXiv:1211.1325, 2012; STOC 2013.

[3] A. Koestler. *The Ghost in the Machine.* Hutchinson, 1967.

[4] A. Koestler. *Some General Properties of Self-Regulating Open Hierarchic Order.* Alpbach Symposium, 1968; published 1969. (Propositions cited by number.)

[5] H. Van Brussel, J. Wyns, P. Valckenaers, L. Bongaerts, and P. Peeters. *Reference Architecture for Holonic Manufacturing Systems: PROSA.* Computers in Industry 37(3), 255–274, 1998.

[6] J. Hansen and R. Ghrist. *Toward a Spectral Theory of Cellular Sheaves.* Journal of Applied and Computational Topology 3, 315–358, 2019.

[7] J. Hansen and R. Ghrist. *Opinion Dynamics on Discourse Sheaves.* SIAM Journal on Applied Mathematics 81(5), 2021.

[8] D. Manheim and S. Garrabrant. *Categorizing Variants of Goodhart's Law.* arXiv:1803.04585, 2018.

[9] S. Abramsky and A. Brandenburger. *The Sheaf-Theoretic Structure of Non-Locality and Contextuality.* New Journal of Physics 13, 113036, 2011. arXiv:1102.0264.

[10] S. Abramsky, S. Mansfield, and R. S. Barbosa. *The Cohomology of Non-Locality and Contextuality.* arXiv:1111.3620, 2011.

[11] *A Sheaf-Theoretic Characterization of Tasks in Distributed Systems.* arXiv:2503.02556.

Measurements cited in §5 are reproducible from `code/spectral_richness.py` in the program's repository.
