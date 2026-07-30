---
layout: document
title: "Sign and Work"
subtitle: "Stigmergy, Sematectonic Traces, and the Cost of Forging a Residue"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /sign-and-work/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-07-30
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Volume V named residue and left one half of its security argument as a design obligation it could not discharge. This is the discharge. Grassé's word for coordination-by-trace splits along exactly the line the volume drew — stigma against ergon, sign against work — and the seam has a price: the trace gap τ, the ratio of forging a residue to earning it. It inflates the Sybil bound by 1/τ, and it is where every stigmergic mechanism either holds or leaks."
status: "v0.1 · working draft"
order: 16
---

## Abstract

Volume V staked value on residue — what an action leaves rather than what it asserts — and rested the case on a biconditional: no work without the trace, and no trace without the work. It established the first half and conceded the second as a *design obligation* rather than a property of residue as such, since a mechanism scoring a trace an adversary can lay more cheaply than the labour it evidences has merely built another proxy. This paper discharges the concession, and the discharge comes from the discipline that has studied coordination-by-trace since 1959. Grassé's coinage — *stigma*, sign, plus *ergon*, work — names two things that Theraulaz and Bonabeau later separated: **sematectonic** stigmergy, where the structure under construction is itself the stimulus, and **marker-based** stigmergy, where a distinct signal such as a pheromone carries it. That separation is Volume V's line drawn in entomology sixty-seven years earlier, and it has the security consequence the volume needed: a pheromone trail can be laid without foraging, and a half-built column cannot be left without building. We define the **trace gap** τ as the ratio of the cost of forging a trace to the cost of earning it, show that Volume V's soundness clause is exactly τ ≥ 1, and prove that a trace-based projection with gap τ inflates the Sybil cap of *The Multiplicity Freedom* by a factor of 1/τ — so the volume's design obligation acquires a price in units the program already uses. We decline the tempting identification: sematectonic construction does not *guarantee* τ ≥ 1, since a structure may be cheap to mimic at the surface, and the gap between "the stimulus is the work product" and "the stimulus cannot be had without the work" is precisely where mechanism design lives.

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

## 5. Interfaces Are Grown, Not Specified

One further consequence, which returns the paper to *Gluing the Gates*.

That paper located every composition failure at the **interfaces** of a holarchy, and observed that interfaces are where no level is looking, because each level's gate reads its own stalk. It did not say why interfaces should be structurally neglected rather than merely inconvenient.

Stigmergy answers it. An interface between holons is not designed by either of them and not by anything above them; it is what accumulated interaction has worn into place — the path across the grass, at the seam between two subsystems. Interfaces are stigmergic constructions, which is precisely why nobody specified them and precisely why nobody is auditing them.

This suggests a design move the program has not had: rather than *specifying* an interface, a mechanism may **cultivate** one. Fix the medium — what traces participants can leave at a boundary — and fix the reading rule, and let the interface find its own density of use. The reticulation optimum conjectured in *Gluing the Gates* §5.2 becomes, on this reading, not a parameter to be tuned but an equilibrium to be reached, and the conjecture acquires a mechanism it previously lacked.

Two cautions. First, cultivation surrenders control: an interface that grows may grow somewhere unwanted, and the composition obstruction of *No Global Section* lives exactly at interfaces, so a cultivated interface is a cultivated place for contextuality to appear. Second, everything in §3 applies with more force at a boundary than in a stalk — a cultivated interface whose traces have low τ is an invitation, not a structure.

Note finally that the architectural vocabulary for ledger-mediated stigmergy already exists. Paredes García [4] gives a state-transition formalism for indirect coordination grounded in distributed-ledger state, with base patterns for flags, event signals, and threshold triggers. That work is about coordination *patterns* and does not treat incentives, forgery resistance, or the cost of laying a trace against the cost of earning it. The present paper is meant to sit underneath it: the patterns describe how ledger-state stigmergy is arranged, and τ describes whether any of the arrangements can be trusted.

---

## 6. What Is Declined

**That sematectonic implies τ ≥ 1.** It does not, and the temptation to say so is the paper's principal hazard. Theraulaz and Bonabeau's distinction concerns what *provides the stimulus*, not what it costs to counterfeit. A structure can be cheap to mimic at the surface — a facade is sematectonic and forgeable — and a marker can in principle be made expensive. Sematectonic construction *tends* toward higher τ because the stimulus is the work product, but the implication is not automatic, and the gap between "the stimulus is the work product" and "the stimulus cannot be had without the work" is exactly where mechanism design happens. We are borrowing an entomological distinction for a purpose Grassé did not intend, and the borrowing is suggestive rather than load-bearing.

**That τ is measurable.** It inherits every imprecision of Definition 2.4. Both w and f are relative to an attacker class, and the framework declines to fix the resource in which they are denominated. τ is a ratio of two quantities the program cannot compute, which makes it useful for comparison and design and not for certification.

**That any mechanism here achieves τ ≥ 1.** None is built and none is measured. The paper supplies a target and an inflation factor for missing it.

**Denial, again.** As in Volume V: traces answer forgery. A participant who withholds work leaves no trace to examine, and stigmergic coordination is if anything *more* exposed to withdrawal than direct coordination, since there is no channel on which absence would be noticed.

**That cultivation is safe.** §5 proposes it and immediately notes it surrenders control at exactly the locus where composition failures live.

---

## 7. Open Problems

**7.1. Measure τ for one projection.** The program has an instrument for adversarial measurement and has used it twice. Estimating f and w for a concrete trace-based projection — even to an order of magnitude, even for a toy — would convert §3 from a definition into a finding.

**7.2. Is τ ≥ 1 attainable, or only approachable?** A trace that costs *more* to forge than to earn seems to require that forgery reproduce the work and then some. Whether that is achievable without an oracle, or whether τ = 1 is a supremum, is open and decides how strong the strong regime of §3 really is.

**7.3. Does τ compose?** *Gluing the Gates* showed richness does not compose. If an interface's trace gap is some function of the gaps of the holons it joins, a holarchy's security could be bounded by the weakest trace in it — which, combined with Proposition 6.1 of that paper, would make nesting doubly penalised.

**7.4. Cultivated interfaces and Conjecture 5.2.** Does an interface whose medium and reading rule are fixed, and whose density is left free, converge to the reticulation optimum that conjecture predicts? This is simulable with the machinery already in `code/`.

**7.5. Quantitative versus qualitative.** Theraulaz and Bonabeau's second distinction — intensity-modulated versus structurally-triggered response — appears to track the framework's own division between scalar substrates, which admit one projection up to monotone transformation, and structural substrates, which admit many. If that mapping holds it would give the framework's §5 a sixty-year empirical literature, and it has not been checked.

---

## References

[1] P.-P. Grassé. *La reconstruction du nid et les coordinations interindividuelles chez* Bellicositermes natalensis *et* Cubitermes sp. *La théorie de la stigmergie.* Insectes Sociaux 6, 41–80, 1959.

[2] G. Theraulaz and E. Bonabeau. *A Brief History of Stigmergy.* Artificial Life 5(2), 97–116, 1999.

[3] F. Heylighen. *Stigmergy as a Universal Coordination Mechanism I: Definition and Components.* Cognitive Systems Research 38, 4–13, 2016. (Part II: *Varieties and Evolution*, same volume.)

[4] F. Paredes García. *Ledger-State Stigmergy: A Formal Framework for Indirect Coordination Grounded in Distributed Ledger State.* arXiv:2604.03997, 2026.
