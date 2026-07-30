---
layout: document
title: "Coutility"
subtitle: "Open Games, and Which Half of Composition They Solve"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /coutility/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-07-30
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Gluing the Gates declined to supply a composition operation. Open games have one, and their Nash equilibrium condition is itself compositional — which is more than was expected and less than is needed. Coutility fixes the first of that paper's two failure modes and leaves the second exactly where it was, because the framework does not gate on equilibrium. It gates on admissibility, and admissibility is a constraint on states, not a fixed point of best responses."
status: "v0.1 · working draft"
order: 18
---

## Abstract

*Gluing the Gates* showed that conjunction-gated mechanisms fail to compose in two distinct ways — a super-mechanism aggregating its constituents' scores can pass while a constituent fails, and, more dangerously, every constituent gate can be satisfied while no globally admissible assignment exists — then declined to supply a composition operation, noting that nothing it offered was as strong as Canetti's universal composition theorem. This paper takes up the operation that exists. Ghani, Hedges, Winschel and Zahn's **open games** are morphisms of a symmetric monoidal category, built from lenses, composing sequentially by categorical composition and in parallel by monoidal product, and carrying **coutility** — the utility a game returns to its environment. Their reported distinctive feature is stronger than this program expected: the Nash equilibrium condition is *itself* compositional. Two consequences follow, and they point in opposite directions. **Coutility propagates a gate where aggregation destroys it**: a super-mechanism reading what its constituents return upward inherits their gates, so *Gluing the Gates* Proposition 4.1 describes an error of construction rather than a fact about composition, and the error has a name and a fix. But **Proposition 4.2 survives untouched**, because the framework does not gate on equilibrium. It gates on *admissibility* — a constraint-satisfaction condition on states — and the compositionality of a best-response fixed point says nothing about whether local constraint solutions glue. Open games hand the program the plumbing it lacked and leave the obstruction exactly where contextuality put it. The paper closes on the pattern this makes visible for the third time: formalisms imported into this program keep relocating its difficulties with precision rather than dissolving them.

---

## 1. The Operation That Was Declined

*Gluing the Gates* ends its declined-claims section with an admission: "Canetti's framework delivers arbitrary composition under a single strong hypothesis. Nothing here is that strong. This paper identifies an obstruction and states the condition for its vanishing; it does not exhibit a composition operation under which Combination Proofs are closed."

That was the right thing to say and it left an obvious question. Composition operations for mechanisms are not unknown. The paper itself cited Syrgkanis and Tardos, whose smooth mechanisms give efficiency guarantees that survive players participating in many mechanisms at once, and whose formulation — smoothness locally implies efficiency globally — was flagged there as already sheaf-shaped. If a composition operation exists in the neighbouring literature, the question is not whether to build one but whether an existing one carries the property this framework cares about.

This paper takes the most structurally explicit candidate and asks exactly that.

---

## 2. Open Games

Ghani, Hedges, Winschel and Zahn [1] give economic game theory a compositional foundation. An **open game** is a game played relative to an arbitrary environment rather than in isolation. It carries a set of strategies, a *play* function sending states forward into the environment, and — the component that gives this paper its title — a **coutility** function returning utility backward to that environment. The forward and backward passes together are a *lens*, and the paper's later development shows all open games can be built from lenses.

Open games are the morphisms of a symmetric monoidal category. They compose in two ways: by categorical composition, giving sequential-move games, and by monoidal product, giving simultaneous-move games. Ordinary games embed faithfully, in the strong sense of having the same Nash equilibria *and the same off-equilibrium best responses*.

The feature the authors single out as distinctive is the one that matters here, and it is stronger than this program had assumed when it declined to look: **the Nash equilibrium condition is itself compositional.** Equilibrium is not a global property computed on the assembled object and then hoped to relate to its parts. It is a property that composes.

Two limitations are stated in the original treatment and repaired later: games are deterministic with no chance element and players choose deterministically, and players have complete information. Bayesian open games [2] and the probabilistic extension [3] relax both. Neither limitation bears on what follows, which turns on the *kind* of property being composed rather than on its stochasticity.

---

## 3. Coutility Propagates a Gate

The first of *Gluing the Gates*' two failure modes turns out to be a mistake rather than a discovery, and open games name the mistake precisely.

That paper's Proposition 4.1 shows that a super-mechanism whose projection is an *aggregate* — π(s) = g({π^v_i(s_v)}) for g monotone and strictly increasing in at least two arguments — is not compositional, because strict monotonicity in two arguments admits a family of states along which one constituent's score falls below its own threshold while a compensating rise elsewhere keeps the aggregate above the super-threshold. A healthy majority carries a failing member, and the super-gate passes on a state where a constituent's gate does not.

Read through open games, this is an error of *what the super-mechanism reads*. An aggregate of constituent utilities reads what each sub-mechanism paid its own participants — a quantity internal to the sub-mechanism, and one that its own gate has already acted on. Coutility is different: it is what the sub-mechanism returns to its environment, which is to say what it hands upward.

**Claim 3.1.** If a sub-mechanism's conjunction-gate zeroes its reward, its coutility to the enclosing environment is likewise zeroed, and a super-mechanism gating on constituent *coutility* rather than on constituent *utility* inherits every constituent gate.

The claim is a design prescription with an argument behind it rather than a theorem, and the argument is structural: coutility is the backward leg of a lens, lens composition composes backward legs, and a super-gate placed on the composite's backward leg is therefore a condition on a quantity that already carries the sub-gates. Aggregation, by contrast, discards the backward structure and re-derives a number from forward data, which is precisely how the gate is lost.

So Proposition 4.1 does not say that conjunction-gating fails to compose. It says that *aggregation* fails to compose, and aggregation was never the composition operation — it was the absence of one. **A mechanism nesting Combination Proofs should compose them as open games and gate on coutility.** That is a concrete instruction the program did not have, and it costs nothing but the discipline of reading the right quantity.

---

## 4. Admissibility Is Not Equilibrium

The second failure mode is untouched, and understanding why is the paper's main contribution.

*Gluing the Gates* Proposition 4.2 exhibits a holarchy in which every constituent gate is satisfied and no global section of the gate sheaf exists — three holons on a cycle whose restriction maps compose to a non-identity scalar, each locally admissible, jointly admitting nothing. *No Global Section* then identified this as contextuality in Abramsky and Brandenburger's exact sense.

It is tempting to expect that a composition operation with a compositional equilibrium condition would dissolve this. It does not, and the reason is that the two results are about different predicates.

**Equilibrium** is a fixed point of best responses. It asks: given what everyone else is doing, does any player wish to deviate? It is a condition on *strategy profiles*, defined relative to a preference ordering, and it is exactly the sort of thing that composes well, because best-response reasoning is local by construction — each player's condition refers only to its own alternatives and its own view of the others.

**Admissibility** is a constraint-satisfaction condition. Conjunction-gating asks: does there exist an assignment of states to participants such that every projection clears its threshold *and* the interface conditions hold? It is a condition on *states*, and it is a global existence question. Nothing about it is a fixed point of anything.

**Proposition 4.1 (this paper).** The compositionality of an equilibrium predicate does not imply the compositionality of an admissibility predicate.

*Sketch.* The contextuality construction supplies the counterexample directly. Take the three-holon cycle; assign each holon a trivial strategy set, so that every profile is vacuously an equilibrium and the equilibrium condition composes trivially. Local admissibility holds at each holon and global admissibility fails. So a composition operation preserving equilibrium can preserve nothing about admissibility, since here it preserves an equilibrium condition that carries no information at all. ∎

The sketch is almost too easy, and that is the point: the two predicates are not merely different in emphasis, they are of different logical shape, and no amount of categorical machinery on one bears on the other.

**Which leaves the framework in an awkward and clarifying position.** Its security property is stated as a *cost* claim — the multiplicative expense of faking a conjunction — and gated as an *admissibility* claim. Neither is an equilibrium claim. So the most developed compositional theory in game theory composes exactly the thing this framework does not use.

---

## 5. Three Relocations

It is worth naming a pattern, because the program has now produced it three times and has not remarked on it.

*Volume V* found that residue does not solve the attestation problem; it relocates it, from "who will vouch for this claim" to "what does it cost to lay this trace" — and *Sign and Work* then had to define τ, because relocation is not resolution.

*No Global Section* found that the cohomological obstruction does not certify composition; it detects failure, and its silence licenses nothing. The invariant relocated the question from "do the gates glue" to "has anything told us they do not."

And here, open games relocate composition from an unsolved problem to a solved one *of the wrong kind*: the operation exists, is well-typed, and preserves the predicate the framework does not gate on.

Each import was worth making. Each made the difficulty sharper and none made it smaller. That is what a mature formalism does to an immature one, and the program should expect the next import to do the same rather than hoping otherwise.

---

## 6. What Is Declined

**That Claim 3.1 is proved.** It is a design prescription supported by a structural argument about lens composition. Establishing it properly requires exhibiting a Combination Proof as an open game — specifying strategy sets, play, and coutility for a conjunction-gated mechanism — and verifying that the gate transfers. That construction is not carried out here, and until it is, coutility is a recommendation and not a result.

**That the equilibrium claim has been verified.** §2 reports the compositionality of the Nash condition as the authors state it. This paper has not read the proof and does not depend on its details; Proposition 4.1 would hold for any composition operation preserving *any* equilibrium-shaped predicate.

**That admissibility could not be made to compose.** The result is that equilibrium-compositionality does not deliver it, not that nothing can. §7 states the route that might.

**That open games are the only candidate.** Syrgkanis and Tardos's smooth mechanisms compose an efficiency guarantee; Canetti's framework composes a simulation-based security notion. Whether either composes something closer to admissibility than equilibrium is unexamined here, and the second is the more promising, since simulation-based security is about what an adversary can *achieve* rather than about what a player *prefers*.

**Any claim about deployment.** Nothing here is built, and the recommendation of §3 has not been implemented in any mechanism.

---

## 7. Open Problems

**7.1. Exhibit a Combination Proof as an open game.** The concrete work Claim 3.1 needs: strategy sets, play function, coutility, and a demonstration that conjunction-gating survives composition when read off the backward leg. This is the paper's first debt and it is tractable.

**7.2. Can Goodhart-asymptotic security be restated as an equilibrium property?** This is the question with the largest payoff in the paper. The framework's security is a cost claim; equilibrium is a preference claim. If faking a conjunction could be characterised as a *deviation no player prefers* — rather than as an expense no player can meet — then the property would be equilibrium-shaped, and open games would hand the program compositionality for free. The obstacle is that fake-cost is denominated in capability, and capability is not a preference. But a restatement in terms of *strategies available at a capability level* may be within reach, and it would convert §4's negative into a positive.

**7.3. Does simulation-based composition fare better?** Canetti's notion quantifies over what an adversary can achieve, which is nearer to admissibility than equilibrium is. Whether a Combination Proof can be given an ideal functionality, and whether its gate survives universal composition, is unexamined and would be the strongest available result if it did.

**7.4. Coutility and the interface.** *Sign and Work* argued that interfaces in a holarchy are grown rather than specified, and that a mechanism might cultivate one. Coutility is precisely a quantity defined *at* an interface — what a game returns to its environment. Whether the trace gap τ of an interface can be expressed as a property of its coutility, tying the two papers together, is open and looks promising.

**7.5. What composes for the C-conditions?** The participation and tolerance conditions surfaced by the H⁰ duplication result are conditions on the *complex*, not on any reward. Whether they compose under nesting — whether a holarchy of participation-respecting sub-mechanisms respects participation — has not been asked, and the H⁰ result suggests connectivity behaves badly under composition.

---

## References

[1] N. Ghani, J. Hedges, V. Winschel, and P. Zahn. *Compositional Game Theory.* Proceedings of LICS 2018; arXiv:1603.04641, 2016.

[2] J. Bolt, J. Hedges, and P. Zahn. *Bayesian Open Games.* arXiv:1910.03656, 2019.

[3] *Compositional Game Theory with Mixed Strategies: Probabilistic Open Games Using a Distributive Law.* arXiv:2009.06831, 2020.

[4] V. Syrgkanis and É. Tardos. *Composable and Efficient Mechanisms.* arXiv:1211.1325, 2012; STOC 2013.

[5] R. Canetti. *Universally Composable Security: A New Paradigm for Cryptographic Protocols.* FOCS, 2001.
