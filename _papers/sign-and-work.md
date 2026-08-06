---
layout: document
title: "Sign and Work"
subtitle: "Stigmergy, Sematectonic Traces, and the Cost of Forging a Residue"
eyebrow: "An Anthology · Paper · v0.3"
permalink: /sign-and-work/
anthology: "Derivation of Value"
version: "v0.3"
date: 2026-08-06
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Volume V named residue and left one half of its security argument as a design obligation it could not discharge. This is the discharge. Grassé's word for coordination-by-trace splits along exactly the line the volume drew — stigma against ergon, sign against work — and the seam has a price: the trace gap τ, the ratio of forging a residue to earning it. v0.3 measures it. Two ceilings, reached by unrelated routes, agree: coherence never contributes to the trace gap. Whatever τ a mechanism has comes from its anchor, and the coherence term appears only in the denominator."
status: "v0.3 · working draft"
order: 16
---

## Abstract

Volume V staked value on residue — what an action leaves rather than what it asserts — and rested the case on a biconditional: no work without the trace, and no trace without the work. It established the first half and conceded the second as a *design obligation* rather than a property of residue as such, since a mechanism scoring a trace an adversary can lay more cheaply than the labour it evidences has merely built another proxy. This paper discharges the concession, and the discharge comes from the discipline that has studied coordination-by-trace since 1959. Grassé's coinage — *stigma*, sign, plus *ergon*, work — names two things that Theraulaz and Bonabeau later separated: **sematectonic** stigmergy, where the structure under construction is itself the stimulus, and **marker-based** stigmergy, where a distinct signal such as a pheromone carries it. That separation is Volume V's line drawn in entomology sixty-seven years earlier, and it has the security consequence the volume needed: a pheromone trail can be laid without foraging, and a half-built column cannot be left without building. We define the **trace gap** τ as the ratio of the cost of forging a trace to the cost of earning it, show that Volume V's soundness clause is exactly τ ≥ 1, and prove that a trace-based projection with gap τ inflates the Sybil cap of *The Multiplicity Freedom* by a factor of 1/τ — so the volume's design obligation acquires a price in units the program already uses. We decline the tempting identification: sematectonic construction does not *guarantee* τ ≥ 1, since a structure may be cheap to mimic at the surface, and the gap between "the stimulus is the work product" and "the stimulus cannot be had without the work" is precisely where mechanism design lives. **This version measures the gap.** Because f is a minimum over a written-down attacker class, an instrument can only ever overestimate it, so τ detects and does not certify — and ceilings are therefore exactly the result it can establish. Two are established here, by unrelated routes. Where the anchor constrains the mechanism's *output*, the forger need only satisfy a public constraint, which is constraint satisfaction rather than work, and τ ≤ 1 − b₁/|E| — with equality only where the cycle rank vanishes and the score is vacuous. Where the anchor constrains *production*, in the manner *Gauge-Fixing* §4.3 specifies, the anchor's rank turns out to be a switch and not a dial — one determined column at every vertex buys the entire available gap and further columns buy nothing — and τ approaches 1 without attaining it, the shortfall being exactly the reconciliation term. Both routes give one conclusion: **coherence never contributes to the trace gap**, which appears only in the denominator, so Volume V's soundness clause is unattainable for a coherence reading rather than merely unmet. This answers §8.2 of the previous version in the negative for this class of reading, and supplies richness a ceiling to set against *Requisite Richness*'s floor.

---

## 1. The Debt

Volume V ended by naming what it could not discharge.

Its security argument was a biconditional. *No work without the trace* — completeness, a record with no gaps for a forger to occupy. *No trace without the work* — soundness, since the only route to the trace runs through the labour. The volume observed that both halves are needed and that they are different claims, then conceded the second: "the biconditional's second half is a design obligation, not a gift. A mechanism that scores a residue an adversary can produce more cheaply than the labour it is meant to evidence has built a proxy and will watch it be eaten."

That concession is the whole of the volume's exposure. Residue was offered as the general answer to the attestation problem on the strength of being involuntary — the walker does not choose to leave the path — but involuntariness is a property of *some* traces and not of traces as a category. A signature is a trace. A logged claim is a trace. Neither costs anything like what it purports to evidence.

So the volume named a substrate whose security depends on a quantity it did not define. This paper defines it.

---

## 2. Grassé's Word Comes Apart

The concept is older than the program by six decades and its literature has already made the distinction the volume needed.

Pierre-Paul Grassé, studying nest reconstruction in *Bellicositermes natalensis*, published in 1959 the account of coordination that would carry his coinage [1]. Termites build without a plan, without instructions, and without communicating with one another. Each deposits material where material has already been deposited; the deposit changes the local environment; the changed environment stimulates the next deposit. The structure is directed by none of them and produced by all of them. Grassé named the principle *stigmergie*, from *stigma* — sign, mark — and *ergon* — work.

The word contains two things, and Theraulaz and Bonabeau [2] separated them. In **sematectonic** stigmergy the stimulus is the work product itself: a half-built column invites its own completion, and there is nothing to read but the building. In **marker-based** stigmergy the stimulus is a distinct signal deposited alongside the work — a pheromone trail, which is not the foraging but a sign of it. They further distinguish *quantitative* stigmergy, where the intensity of a stimulus modulates the response, from *qualitative*, where structurally different configurations trigger different responses altogether.

**The first distinction is Volume V's line.** A marker is an *assertion*: separable from the action, and therefore producible without it. A sematectonic structure is a *residue*: it is what the work made, and it is not separable from the work because it *is* the work.

The security consequence follows immediately and was always implicit in the biology. An adversary who wishes to redirect an ant colony need not forage; it need only lay pheromone, and the literature on ant-trail manipulation is a literature on exactly that. An adversary who wishes a half-built column to exist must build half a column. Same coordination mechanism, opposite exposure — and the difference is not in the agents, the medium, or the protocol, but in whether the thing being read is the work or a sign of it.

That the entomologists drew this line in 1959, and that the program rediscovered it in four vocabularies without noticing, is worth stating plainly rather than presenting as convergence. The mapping is:

| Volume V | Grassé, after Theraulaz & Bonabeau |
|---|---|
| assertion — separable, forgeable, needs a voucher | marker-based stigmergy |
| residue — inseparable, involuntary, self-attesting | sematectonic stigmergy |
| the attestation problem | which of the two a mechanism reads |

The remaining sections make the second row quantitative, because as stated it is still a dichotomy, and real traces are not dichotomous.

---

## 3. The Trace Gap

Fix an attacker class in the sense of Definition 2.4 of the framework, and a projection π scored on a trace.

**Definition 3.1 (earning cost).** Write *w(π)* for the resource an honest participant expends in performing the work that π is meant to evidence.

**Definition 3.2 (forging cost).** Write *f(π)* for the minimum resource an attacker in the class expends to produce a trace that π accepts, *without* performing the work.

**Definition 3.3 (trace gap).** The *trace gap* of π is τ(π) = f(π)/w(π) ∈ [0, ∞).

The definition is deliberately a ratio rather than a difference, because what a mechanism needs to know is not how much forgery costs but how it compares to honesty. A trace expensive to forge in absolute terms is worthless if the work it evidences is more expensive still.

**A remark on the direction of error, which governs everything measurable about τ.** Definition 3.2 makes *f* a *minimum* over an attacker class. Any instrument computing it minimises only over strategies someone has written down, and a strategy nobody has thought of is cheaper than every strategy enumerated. Therefore

> measured τ ≥ true τ, always.

τ errs toward safety and cannot err against it. A *low* measured τ is a real finding, because it exhibits a forgery and exhibiting one settles the matter; a *high* measured τ is the absence of evidence and certifies nothing. So τ is a detector and not a certificate — which is the same shape *No Global Section* found in the cohomological invariant, arrived at independently and for an unrelated reason. The practical consequence is that **ceilings are what this quantity can establish**, and §5 establishes two.

**Proposition 3.4.** Volume V's soundness clause — no trace without the work — holds for π exactly when τ(π) ≥ 1.

*Proof.* Immediate from the definitions: τ ≥ 1 says forging costs at least as much as earning, so no attacker in the class prefers the forgery, and every accepted trace was either earned or produced at no saving. ∎

The proposition is trivial and its value is that it makes the volume's concession *measurable*. "Design obligation" becomes "keep τ above one," which is a target rather than an exhortation, and which a specific mechanism either meets or does not.

Three regimes are worth naming.

**τ ≈ 0.** The trace is nearly free. This is marker-based stigmergy and it is also what a bare signature, a self-reported metric, and an oracle attestation are: the sign costs nothing resembling the thing signified. Volume V's warning applies in full — such a projection is a proxy, and will be eaten.

**τ ≈ 1.** Forging costs what earning costs. The attacker is indifferent, and — this is the interesting part — an attacker who proceeds anyway has *done the work*, which is the condition under which the framework's harvest results apply.

**τ > 1.** Forging costs more than earning. Rare, and worth pursuing where available: it means the cheapest route to the score is honesty, which is the strong reading of Goodhart-asymptotic the framework has been reaching for.

**Corollary 3.5.** If τ(π) ≥ 1 then π is harvestable in the sense of Definition 4.4 of the framework.

*Sketch.* At τ ≥ 1 the attacker saves nothing by forging, so any attempt that produces an accepted trace expended at least w — that is, performed work of the kind the projection evidences. The residue of the attempt is therefore of the same kind as the residue of honest work, which is harvestability. ∎

So Volume V's biconditional and the framework's adversary-positivity are the same condition, approached from opposite ends. That was suspected in the volume's section on the adversary and is now a consequence rather than an observation.

---

## 4. What the Gap Costs

The trace gap connects to the program's one set of theorems, and the connection puts a number on Volume V's obligation.

*The Multiplicity Freedom* bounds an adversary's fleet at N ≤ ⌊C/Γ⌋, where Γ is the expenditure required to clear every gate on one identity. That derivation assumed each projection's threshold is reached by doing the work. If instead the projection is trace-based with gap τ < 1, an attacker reaches the threshold at cost τ·w rather than w.

**Proposition 4.1 (gap inflation).** Let M be a Combination Proof whose projections are trace-based with uniform gap τ. Then the Sybil cap becomes

> N ≤ ⌊ C / (τ·Γ) ⌋ = (1/τ) · ⌊C/Γ⌋

so a trace gap of τ inflates the adversary's fleet by a factor of 1/τ.

*Proof.* Substitute the attacker's effective per-projection cost τγᵢ for γᵢ throughout the derivation of Theorem 4.1 of that paper; Γ scales linearly in the per-projection costs, and the bound is C/Γ. ∎

The consequence is worth stating in plain terms. A mechanism whose traces can be forged at a tenth the cost of earning them does not have a somewhat weaker Sybil bound. It has a **ten times larger adversary**, and the resource floor it believed it had — the dissipation floor that, in *Proof of Preservation*'s phrase, "prices the minting of identities and does nothing else" — has been silently divided by ten. Nothing in a static audit reveals this, because the mechanism's own measurements are of the trace, and the trace is exactly what was cheap.

This also sharpens where the trace gap must be defended. τ is not a property of a substrate in the way richness is; it is a property of *the reading*, of what the mechanism accepts as evidence. Two mechanisms on the same substrate, one scoring a lattice by measuring it and the other by accepting a certificate about it, have wildly different τ and identical ρ.

---

## 5. What the Anchor Pays For

The previous version supplied a definition and one measurement, which came out at the worst possible value. This section supplies the measurements (`code/trace_gap.py`, seeded and reproducible). The result is not the number but its shape: in every arrangement tested, **the trace gap is bought entirely by the anchor, and the coherence content appears only in the denominator.**

**Calibration first.** A ratio of two costs is worth nothing until it returns a known answer to a known question. Proof of work is the object with a known answer: the reading rule accepts a nonce whose hash clears a target, no shortcut to the search is known, so forging costs exactly what earning costs and τ = 1 by construction. The instrument returns **1.054** across four hundred trials. A signed claim of work — the canonical τ ≈ 0 regime of §3 — returns 1/w. Only then is the instrument turned on the coherence score. (The first pass returned 2.74 on proof of work, comparing the attacker's cost on a single search against the honest mean over eight; search length is geometric with standard deviation equal to its mean, so one draw is not an expectation. The failure is recorded because the calibration object is the only reason it was visible.)

### 5.1 Anchors that constrain the output

Take the reading the framework actually uses: a cellular sheaf with ℝᵈ stalks and O(d) restriction maps, scored by the count of Laplacian eigenvalues below tolerance, accepted when the count reaches d. Suppose the mechanism anchors by pinning frames at chosen vertices to publicly known values.

The forger's cheapest accepted trace is **every frame equal**. The connection is then the identity on every edge, the complex is perfectly coherent, the score is full, and nothing whatever was reconciled — because there was nothing to reconcile. This is *A Consistent Fiction*'s fiction space, entered deliberately rather than converged upon, and it costs nothing.

Pinning *one* vertex does not disturb it. The coherent connection is gauge-invariant under R_v ↦ R_v Q, so the forger rotates the entire fiction to meet the anchor for free, and τ remains 0. This is worth stating against that paper's own result: closure is escapable at d scalars of contact at one vertex, once — and that purchase closes the *fiction space* while opening *no trace gap at all*. Two jobs at two prices, and only the first had been costed.

Pinning every vertex does not lift τ to 1 either. A spanning tree meets every vertex constraint, so the forger never pays for a cycle, and the cycle-closing edges are pure honest surplus. Measured across cycle ranks on a hierarchical-modular complex of 256 vertices, the agreement is exact:

| cross-edges per merge | \|E\| | b₁ | measured τ | (n−1)/\|E\| |
|---|---|---|---|---|
| 1 | 255 | 0 | 1.0000 | 1.0000 |
| 2 | 359 | 104 | 0.7103 | 0.7103 |
| 3 | 463 | 208 | 0.5508 | 0.5508 |
| 5 | 618 | 363 | 0.4126 | 0.4126 |
| 8 | 803 | 548 | 0.3176 | 0.3176 |

**Proposition 5.1 (output-anchor ceiling).** For a coherence reading scored as dim ker, under any set of publicly fixed frames, τ ≤ (n−1)/|E| = 1 − b₁/|E|.

*Proof.* Any assignment of frames to vertices induces a flat connection, since O_uv = R_uᵀR_v telescopes to the identity around every cycle; so the score is constant on the whole image of the frame-assignment map, and the forger's only task is to meet the pinned values. A spanning tree determines every frame from any set of vertex constraints. The forger therefore reconciles at most n−1 edges where the honest participant reconciles |E|. ∎

Equality holds exactly at b₁ = 0 — a tree — where a connection is coherent automatically because there is no cycle to frustrate, and the score is therefore vacuous.

The principle the ceiling is a signature of is more general than the sheaf:

> **Satisfying a public constraint is constraint satisfaction, never work.** A trace gap derived from an *output* constraint is bounded by that constraint's satisfaction cost, which is structurally unrelated to its generation cost.

Two consequences for *Gauge-Fixing*. First, the arrangement measured here is that paper's own §5 test (i) — "that the anchored sheaf admits no non-truthful global sections under the stated adversary" — executed with anchor §4.3 removed, and it returns what §5 predicts, "generically it will admit them if any anchor is removed," now with a price attached. Second, and less comfortably, §4.4's rule that an anchor is "forbidden from moonlighting as a certificate of order" reads as ascetic taste and is nothing of the kind: it is the difference between a τ whose ceiling lies below one and a τ that can approach it. This is the third occasion on which a condition of the program's that looked like hygiene turned out to be load-bearing.

### 5.2 Anchors that constrain production

*Gauge-Fixing* §4.3 does not constrain the configuration. It constrains how a section may be *produced* — a slow, sequentially dependent encoding keyed to identity and the epoch beacon, applied before the section enters the sheaf — so that "H¹ is made to see what it is natively blind to, not by strengthening the cohomology but by preparing its inputs." Model this with two parameters: the **rank** of the anchor, meaning how many of each frame's d columns the world determines rather than the participant choosing, and the **encoding cost** of producing one admissible section, which nobody escapes.

Rank was predicted before measurement to be discontinuous at 1 and flat thereafter, since the global gauge dies the moment any column is pinned at *every* vertex. At encoding cost 4:

| rank | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| τ | 0.0000 | 0.4874 | 0.4874 | 0.4874 |

Identical to four decimals for every rank ≥ 1. **The anchor's rank is a switch and not a dial: one determined column at every vertex buys the entire available gap, and further columns buy nothing.** The output-anchor arrangement of §5.1 climbs steadily with the *number* of anchored vertices, so the two are different objects and the count was the wrong coordinate.

Sweeping the encoding cost at rank 1 tracks n·E/(n·E + |E|·c) to four decimals — 0.1920, 0.4874, 0.7918, 0.9383, 0.9838, 0.9959 at encoding costs 1 through 1024 — approaching 1 and never arriving.

**Proposition 5.2 (generative-anchor limit).** Under an encoding cost E per section and a reconciliation cost c per edge, τ = nE/(nE + |E|c), which is strictly less than 1 whenever c > 0 and |E| > 0, and tends to 1 as E/c → ∞.

*Proof.* Both parties pay nE, since an admissible section cannot be had for less. The forger, holding admissible sections, declares the connection they induce, which is flat by the argument of Proposition 5.1, and so reconciles nothing. The honest participant reconciles |E| edges. ∎

The proposition is conditional on the cost model — in particular on reconciliation being genuine additional work on top of producing sections — and §7 declines it accordingly.

### 5.3 The two results are one

Proposition 5.1 gives τ = 1 only at b₁ = 0, where the score is vacuous. Proposition 5.2 gives τ → 1 only as E/c → ∞, where the coherence term vanishes against the anchor. Two unrelated routes, one conclusion:

> **Coherence never contributes to the trace gap.** Whatever gap a mechanism has is bought by its anchor; the coherence content enters only in the denominator. τ ≥ 1 is reachable solely by driving the coherence contribution to zero — either the cycle rank, where the score stops meaning anything, or the cost share, where the mechanism is measuring its anchor and calling it coherence.

Volume V's soundness clause is therefore not merely unmet by a coherence reading. It is **unattainable** by one, and both derivations locate the shortfall in precisely the part that makes coherence mean anything. §8.2 of the previous version asked whether τ ≥ 1 is attainable or only approachable; for this class of reading the answer is *only approachable*, and the reason is structural rather than incidental.

### 5.4 Richness is paid for in trace gap

Coupling density is one parameter and both quantities are functions of it. Measured on the same complex: the spectral dimension rises 1.255 → 2.281 across the coupling sweep, reproducing the figures of *Requisite Richness*'s substrate, while the trace-gap ceiling falls 1.000 → 0.315. Under Proposition 5.2 the same monotonicity holds directly, since τ = nE/(nE + |E|c) decreases in |E|.

By Proposition 4.1 a gap of τ inflates the adversary's fleet by 1/τ. So richness purchased at the coupling knob is **paid for in Sybil resistance** — at the dense end of the sweep, an adversary 3.2 times larger than *The Multiplicity Freedom* assumes. *Requisite Richness* supplies ρ a floor set by the adversary; this supplies a ceiling set by the same adversary along an unrelated route, and substrate selection is constrained from both sides rather than one.

---

## 6. Interfaces Are Grown, Not Specified

One further consequence, which returns the paper to *Gluing the Gates*.

That paper located every composition failure at the **interfaces** of a holarchy, and observed that interfaces are where no level is looking, because each level's gate reads its own stalk. It did not say why interfaces should be structurally neglected rather than merely inconvenient.

Stigmergy answers it. An interface between holons is not designed by either of them and not by anything above them; it is what accumulated interaction has worn into place — the path across the grass, at the seam between two subsystems. Interfaces are stigmergic constructions, which is precisely why nobody specified them and precisely why nobody is auditing them.

This suggests a design move the program has not had: rather than *specifying* an interface, a mechanism may **cultivate** one. Fix the medium — what traces participants can leave at a boundary — and fix the reading rule, and let the interface find its own density of use. The reticulation optimum conjectured in *Gluing the Gates* §5.2 becomes, on this reading, not a parameter to be tuned but an equilibrium to be reached, and the conjecture acquires a mechanism it previously lacked.

Two cautions. First, cultivation surrenders control: an interface that grows may grow somewhere unwanted, and the composition obstruction of *No Global Section* lives exactly at interfaces, so a cultivated interface is a cultivated place for contextuality to appear. Second, everything in §3 applies with more force at a boundary than in a stalk — a cultivated interface whose traces have low τ is an invitation, not a structure.

Note finally that the architectural vocabulary for ledger-mediated stigmergy already exists. Paredes García [4] gives a state-transition formalism for indirect coordination grounded in distributed-ledger state, with base patterns for flags, event signals, and threshold triggers. That work is about coordination *patterns* and does not treat incentives, forgery resistance, or the cost of laying a trace against the cost of earning it. The present paper is meant to sit underneath it: the patterns describe how ledger-state stigmergy is arranged, and τ describes whether any of the arrangements can be trusted.

---

## 7. What Is Declined

**That sematectonic implies τ ≥ 1.** It does not, and the temptation to say so is the paper's principal hazard. Theraulaz and Bonabeau's distinction concerns what *provides the stimulus*, not what it costs to counterfeit. A structure can be cheap to mimic at the surface — a facade is sematectonic and forgeable — and a marker can in principle be made expensive. Sematectonic construction *tends* toward higher τ because the stimulus is the work product, but the implication is not automatic, and the gap between "the stimulus is the work product" and "the stimulus cannot be had without the work" is exactly where mechanism design happens. We are borrowing an entomological distinction for a purpose Grassé did not intend, and the borrowing is suggestive rather than load-bearing.

**That τ is measurable in the sense that would certify anything.** The previous version declined measurability outright; that was too strong, and the correction is stated rather than quietly made. τ is computable *given an explicit attacker class*, and §5 computes it. But f is a minimum over that class, so what is computed is an upper bound and nothing else — measured τ ≥ true τ, always. The instrument can refute a claim of safety and can never establish one. Everything in §5 is therefore stated as a ceiling, and a cheaper forgery would only lower it.

**That the cost model of §5.2 is settled.** Proposition 5.2 assumes an honest surplus of |E|·c *on top of* the per-section encoding — that is, that reconciliation is genuine additional work rather than redundant once the world determines the frames. At full rank it is arguable that it is redundant, in which case the surplus is double-counted and τ rises. This is the load-bearing joint in both halves of §5 and the first place the results should be attacked.

**That the τ ≈ 1 regime of §5.2 is a failure of the model.** At high encoding cost the attacker has paid for every observation, which by Corollary 3.5 means the work was done. That is §3's τ ≈ 1 regime behaving exactly as described, not an artefact.

**That §5 covers coherence readings in general.** It covers *one* reading — dim ker of a declared connection — on one substrate family. A mechanism scoring cycle agreement directly, rather than reading a kernel dimension off a spectrum, is untouched by any of it, and is the obvious place to look for a reading with a better gap. The conclusion of §5.3 is asserted for the reading measured and conjectured beyond it.

**That any mechanism here achieves τ ≥ 1.** None is built, and §5 now indicates that for a coherence reading none can.

**Denial, again.** As in Volume V: traces answer forgery. A participant who withholds work leaves no trace to examine, and stigmergic coordination is if anything *more* exposed to withdrawal than direct coordination, since there is no channel on which absence would be noticed.

**That cultivation is safe.** §6 proposes it and immediately notes it surrenders control at exactly the locus where composition failures live.

---

## 8. Open Problems

**8.1. ~~Measure τ for more projections.~~ Partly discharged; the residue is sharper.** The previous version's open problem asked for τ on the spectral projection and on a participation-constrained H⁰. §5 supplies the second and a ceiling covering both, and what remains is narrower and harder: **is there a coherence reading whose trace gap is not bought entirely by its anchor?** §5.3's conclusion is established for dim ker of a declared connection. A reading that scores cycle agreement directly — where the restriction maps are measured at overlaps rather than induced by declared frames — is not covered by Proposition 5.1's telescoping argument, and is the one place a better gap could hide. If it does not hide there, the conclusion generalises and coherence-based attestation is bounded in a way the framework has not admitted.

**8.2. ~~Is τ ≥ 1 attainable, or only approachable?~~ Answered for coherence readings: only approachable.** Propositions 5.1 and 5.2 both put 1 out of reach except in the degenerate limits, and the shortfall is the coherence content in each case. The question survives *outside* the coherence setting, and its interesting form is now Volume V's: does any substrate admit a reading with τ > 1, or is every trace at best as expensive to forge as to earn? Proof of work sits at exactly 1 and the program has no specimen above it.

**8.3. What raises the encoding's share honestly?** Proposition 5.2 says τ rises with E/c, so a mechanism can approach soundness by making its anchor expensive relative to its coherence work. This is a *perverse* route to a target — the mechanism ends up measuring its anchor — and the question is whether it has a non-perverse form. If not, the design consequence is stark: the coherence layer should be priced as a coordination device rather than an attestation one.

**8.4. Does τ compose?** *Gluing the Gates* showed richness does not compose. If an interface's trace gap is some function of the gaps of the holons it joins, a holarchy's security could be bounded by the weakest trace in it — which, combined with Proposition 6.1 of that paper, would make nesting doubly penalised. §5.4's finding that τ falls with coupling density makes this more pressing, not less.

**8.5. Cultivated interfaces and Conjecture 5.2.** Does an interface whose medium and reading rule are fixed, and whose density is left free, converge to the reticulation optimum that conjecture predicts? This is simulable with the machinery already in `code/`.

**8.6. Quantitative versus qualitative.** Theraulaz and Bonabeau's second distinction — intensity-modulated versus structurally-triggered response — appears to track the framework's own division between scalar substrates, which admit one projection up to monotone transformation, and structural substrates, which admit many. If that mapping holds it would give the framework's §5 a sixty-year empirical literature, and it has not been checked.

---

## References

[1] P.-P. Grassé. *La reconstruction du nid et les coordinations interindividuelles chez* Bellicositermes natalensis *et* Cubitermes sp. *La théorie de la stigmergie.* Insectes Sociaux 6, 41–80, 1959.

[2] G. Theraulaz and E. Bonabeau. *A Brief History of Stigmergy.* Artificial Life 5(2), 97–116, 1999.

[3] F. Heylighen. *Stigmergy as a Universal Coordination Mechanism I: Definition and Components.* Cognitive Systems Research 38, 4–13, 2016. (Part II: *Varieties and Evolution*, same volume.)

[4] F. Paredes García. *Ledger-State Stigmergy: A Formal Framework for Indirect Coordination Grounded in Distributed Ledger State.* arXiv:2604.03997, 2026.
