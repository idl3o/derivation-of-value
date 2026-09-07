---
layout: document
title: "The Ring and the Chord"
subtitle: "The Obstruction Off the Cycle, and What It Sees There"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /the-ring-and-the-chord/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-09-07
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "On a cyclic cover the cohomological obstruction is a graph search and the coefficient ring does not matter. Off the cycle both statements fail, and they fail on the literature's own answer key: the Peres–Mermin square and the GHZ model are obstructed at every section over the integers and mod 2 and vanish at every section over the rationals, because an all-versus-nothing argument is a parity argument and the integer obstruction on such a model is 2-torsion. On random no-signalling models with chords the invariant is nearly blind, seeing one logically contextual model in five, ten or forty; drop the no-signalling condition and it sees most of them, and on a holarchy of four three-port holons with tolerance gates it sees every one. Gate models signal, and signalling is what the invariant sees. The setting the literature built the invariant for is the setting in which it is weakest."
status: "v0.1 · working draft"
order: 25
---

## Abstract

*The Obstruction, Computed* §6 proved that on a cyclic cover the Čech obstruction of Abramsky, Mansfield and Barbosa is undirected reachability in the bundle diagram, hence independent of the coefficient ring, and declined to say anything about covers with chords. This paper goes there, with three questions the corpus's instruments can answer: whether the ring matters, how detection behaves, and what a non-cyclic holarchy looks like as a gate scenario. The ring matters, and it matters on the answer key. The Peres–Mermin square and the GHZ model — the models the literature uses to show the invariant working — are obstructed at every section over ℤ and over ℤ₂ and vanish at every section over ℚ, by explicit rational families with coefficients ±½ confirmed by a second solver: an all-versus-nothing argument is a parity argument, the integer obstruction on such a model is 2-torsion, and a field of characteristic zero cannot see it. In some sixty thousand sections across random models on three chorded covers and a holarchy, ℤ and ℤ₂ never disagreed, so the literature's mod-2 machine checks were exact in both directions on every model here, and ℤ and ℚ disagreed only on all-versus-nothing structures. Detection off the cycle depends on something the cyclic theorem had no room to show. On random *no-signalling* models — the literature's setting — the invariant sees one logically contextual model in four on the (3,3,2) cover, one in ten on the GHZ cover and one in forty on the Peres–Mermin cover, section rates of 0.07, 0.05 and 0.01 against the cycles' 0.6 to 0.7. Drop the no-signalling condition and the rates rise to 0.76, 0.37 and 0.46, with every strongly contextual model seen. A holarchy of four three-port holons on K4 with Rayleigh-quotient gates — every holon in three interfaces, so the cover has chords — is strongly contextual exactly when its mod-2 holonomy fails on some cycle, is then obstructed at every section in every ring, and with tolerance gates shows no miss at all: 7,056 of 7,056 non-extending sections obstructed, all 81 logically contextual models seen. The mechanism is stated before the last measurement and held: a state absent from one interface's support is a node with no edges in that layer, and conservation at such a node zeroes its sums everywhere, which is a route a formal family cannot use. Gate models signal, since an interface may drop admissible states of a holon that another keeps, and signalling is what the invariant sees. What is claimed is the rational vanishing on the answer key, the ring accounting across the covers, the signalling mechanism and its measurement, and the K4 holarchy; the invariant, its misses and the models are cited.

---

## 1. Off the Cycle

On a cyclic cover — contexts in a ring, consecutive ones overlapping, no chords — the obstruction is a graph search. *The Obstruction, Computed* §6 proved it: the compatibility condition is flow conservation on the bundle diagram, so a section's class vanishes exactly when its ends are joined by an undirected path avoiding its own layer, over any ring, and the section extends exactly when the path is directed. Three things followed and were measured: the integers and the rationals never disagree, a miss is a reversal, and a reversal needs a tolerance gate in the chain. That paper declined to say any of it off the cycle, where a measurement can lie in three contexts and compatibility is conservation on a hypergraph.

This paper takes the three questions the theorem leaves open, in the order an instrument can answer them. The first is whether the ring matters once the cover has chords: Abramsky, Barbosa, Kishida, Lal and Mansfield [2] prove one direction for every cover — a class that vanishes over ℤ vanishes over every ring — and the converse fails exactly where the Čech system has torsion. The second is how detection behaves once a formal family has more than one route around. The third is what a holarchy with chords looks like as a gate scenario, since two-port holons only ever make cycles.

The answers, in the order they came. The ring matters, and it matters first on the models the literature uses to show the invariant working: the Peres–Mermin square and the GHZ model are obstructed at every section over ℤ and ℤ₂ and vanish at every section over ℚ (§3). Detection off the cycle is not one number but two, and the difference between them is whether the model signals: on the literature's no-signalling models the invariant sees almost nothing in the logical grade, and on signalling models — which gate models are — it sees most of it, and on the K4 holarchy all of it (§§4–5). The mechanism is a node with no edges in a layer, and it was stated as a prediction before the measurement that confirmed it.

Everything is exact arithmetic, calibrated on an answer key before the program's own scenarios are touched, with the predictions stated in `code/covers.py` before running and the two that failed recorded.

---

## 2. Prior Art, and the Boundary of the Claim

The invariant, the models and the one-directional ring result are the literature's; the boundary is drawn so that §§3–5 claim only what lies past it.

Abramsky, Mansfield and Barbosa [1] define the obstruction over the free ℤ-module on a model's support and verify it on the PR box by hand and on GHZ, the Peres–Mermin square and the eighteen-vector Kochen–Specker model by machine, in mod-2 arithmetic, noting for GHZ that the class does not vanish "even if we use ℤ/2ℤ as the coefficient group". Abramsky, Barbosa, Kishida, Lal and Mansfield [2] define the invariant over any commutative ring, prove that a ring homomorphism carries vanishing to vanishing (Proposition 20), so that ℤ is the most sensitive ring, and prove that every all-versus-nothing argument over a ring R is witnessed by the obstruction over R (Theorem 21); their AvN arguments are systems of linear equations over ℤ₂, and the paper remarks that the first implication of Theorem 21 reverses when R is a field. Carù [3, 4] gives the known misses and the completeness result on cyclic covers, choosing ℤ₂ for the proof. Abramsky and Brandenburger [5] prove that every no-signalling model has a global distribution with signed real weights; that is a statement about the full outcome space, not the support, and it does not by itself say what the rational obstruction on the support does. §2 of *The Obstruction, Computed* records the framework's exports and the absence of any mechanism-design application.

The rational vanishing of §3 is, on the evidence of the sweep, an unremarked corollary. Every published computation of the GHZ, Peres–Mermin and Kochen–Specker obstructions was done in mod-2 arithmetic and carried to ℤ by descent along ℤ → ℤ₂ [1]; Proposition 20 of [2] carries vanishing along any ring homomorphism, so the rational obstruction is formally the weakest of the characteristic-zero ones, and neither paper instantiates R = ℚ or remarks that the descent has no counterpart for it. Montanhano [6] is the nearest antecedent: negative coefficients "allow the Z sections, causing the known violations", and real coefficients give a trivial obstruction for every no-signalling model — but the section he takes is the probability vector of a context rather than a single local section, the argument leans on [5]'s signed-measure theorem, which concerns the full outcome space and not the support, and neither GHZ, the square nor ℚ is named. Carù's thesis [7] records that the only cohomological miss known on a non-cyclic cover is [1]'s Kochen–Specker specimen, and reduces the invariant to the one-skeleton of the nerve; no source counts how often the invariant detects logical contextuality on a chorded cover, and none discusses the no-signalling condition as the variable.

What is claimed. That the Peres–Mermin square and GHZ have vanishing rational obstruction at every section, with explicit families (§3) — as a statement, since as a fact it is the unremarked corollary above, and an independent rank computation in the sweep's own report returned the same 0 of 16 and 0 of 24. That across some sixty thousand sections on three chorded covers and a holarchy, ℤ and ℤ₂ never disagreed and ℤ and ℚ disagreed only on all-versus-nothing structures (§4). That detection on no-signalling models with chords is an order of magnitude below the cycles', and that the no-signalling condition is the cause: the same covers without it are seen at three to forty times the rate, and the mechanism — a node with no edges in a layer — was stated before that measurement (§4). That a holarchy of three-port holons on K4 is a gate scenario with chords, strongly contextual exactly when its mod-2 holonomy fails, obstructed at every section in every ring when it is, and free of misses with tolerance gates (§5). And that gate models signal, so that the setting the invariant was built for is the one in which it is weakest (§6).

---

## 3. The Answer Key, and the Rationals

`code/covers.py`, Part 1. Three models whose grade the literature settled, computed over three rings: the integers by Smith normal form, the rationals by exact elimination, ℤ₂ by elimination on bit-packed rows; every section's extendability brute-forced; a false positive in any ring flagged as a solver error.

The Peres–Mermin square: nine measurements in a three-by-three grid, six contexts (rows and columns), outcomes 0 and 1, every row even, two columns even and one odd. Strongly contextual by parity — the row constraints sum to 0 and the column constraints to 1 over the same nine values. GHZ: three parties with measurements X and Y each, contexts XXX, XYY, YXY, YYX, the first even and the other three odd. Strongly contextual, the same way. A product model on the (3,3,2) scenario — three measurements a side, all nine pairs as contexts, every joint outcome possible — as the non-contextual control.

| model | grade | sections | non-extending | obstructed ℤ | obstructed ℚ | obstructed ℤ₂ | globals |
|---|---|---|---|---|---|---|---|
| Peres–Mermin | strong | 24 | 24 | 24 | **0** | 24 | 0 |
| GHZ | strong | 16 | 16 | 16 | **0** | 16 | 0 |
| product (3,3,2) | non-contextual | 36 | 0 | 0 | 0 | 0 | 64 |

The prediction was that all three rings would obstruct every section of the two contextual models. Two thirds of it held. Over the rationals the obstruction vanishes at every section of both.

**Proposition 3.1 (the rationals do not see the square, or GHZ).** For every local section s of the Peres–Mermin model and of the GHZ model, γ_ℚ(s) = 0, while γ_ℤ(s) ≠ 0 and γ_{ℤ₂}(s) ≠ 0.

*Proof, by exhibition.* For GHZ with s = (0, 0, 0) at XXX, the family r_{XYY} = ½·(0,0,1) + ½·(0,1,0) − ½·(1,0,0) + ½·(1,1,1), r_{YXY} = (0,0,1), r_{YYX} = (0,1,0) agrees with s and with each other on every overlap; every coefficient is ±½ or 1. For the square with s = (0,0,0) at the first row, r_{row 2} = (0,0,0), r_{row 3} = ½·(0,0,0) + ½·(0,1,1) + ½·(1,0,1) − ½·(1,1,0), and the three columns (0,0,0), (0,0,0), (0,0,1). The instrument finds a rational family for every section of both models by exact elimination, and a second solver — least squares on the same system, residual 10⁻¹⁵ — agrees. Non-vanishing over ℤ and ℤ₂ is [1]'s mod-2 computation, reproduced. ∎

The families say why. The all-versus-nothing argument for either model is a parity argument — sum the constraints and 0 = 1 mod 2 — and a parity argument is a statement over ℤ₂. Over ℤ it survives as 2-torsion: the Čech system's Smith form has a diagonal entry 2 dividing a right-hand side 1, which is the AvN contradiction in another notation. Over a field of characteristic zero, 2 is a unit, the family divides by it, and the contradiction is gone. Theorem 21 of [2] says every AvN argument over R is witnessed over R; the AvN arguments of these models are over ℤ₂, and nothing in that theorem reaches ℚ. Nothing in this paper says the rationals see *no* contextuality — §4's strong (3,3,2) models are sometimes seen over ℚ — only that they see none of the parity kind, which is the kind the literature's flagship models exhibit.

---

## 4. Random Models on Three Chorded Covers

`code/covers.py`, Part 2. Four hundred random possibilistic models on each of three covers, twice: once *no-signalling* on single-measurement overlaps — each measurement's possible outcomes the same in every context containing it, the setting of [1, 2, 5] — and once without that condition. The (3,3,2) cover, nine pair-contexts on a complete bipartite nerve; the GHZ cover, four three-measurement contexts every two of which overlap; the Peres–Mermin cover, six three-measurement contexts on a three-by-three grid. Half the models are built from a few random global assignments with extra sections added, the other half from random supports; every section's obstruction over ℤ, ℚ and ℤ₂; every section's extendability. *Rate* is the fraction of non-extending sections the ℤ-obstruction sees; *seen* and *missed* count contextual models with at least one obstructed section and none; *ℤ¬ℚ* counts non-extending sections obstructed over ℤ whose class vanishes over ℚ, *ℤ¬ℤ₂* the same against ℤ₂.

| cover | condition | grade | models | non-extending | obstructed ℤ | rate | ℤ¬ℚ | ℤ¬ℤ₂ | seen | missed |
|---|---|---|---|---|---|---|---|---|---|---|
| (3,3,2) | no-signalling | logical | 203 | 1,447 | 107 | **0.074** | 0 | 0 | 49 | **154** |
| (3,3,2) | no-signalling | strong | 8 | 189 | 73 | 0.386 | **3** | 0 | 5 | 3 |
| (3,3,2) | signalling | logical | 58 | 425 | 321 | **0.755** | 0 | 0 | 43 | 15 |
| (3,3,2) | signalling | strong | 170 | 3,339 | 3,104 | 0.930 | 0 | 0 | 170 | 0 |
| GHZ cover | no-signalling | logical | 225 | 834 | 41 | **0.049** | 0 | 0 | 22 | **203** |
| GHZ cover | signalling | logical | 227 | 1,040 | 381 | **0.366** | 0 | 0 | 103 | 124 |
| GHZ cover | signalling | strong | 12 | 178 | 83 | 0.466 | 0 | 0 | 12 | 0 |
| PM cover | no-signalling | logical | 172 | 605 | 7 | **0.012** | 0 | 0 | 4 | **168** |
| PM cover | signalling | logical | 202 | 1,278 | 584 | **0.457** | 0 | 0 | 138 | 64 |
| PM cover | signalling | strong | 9 | 197 | 112 | 0.569 | 0 | 0 | 9 | 0 |

Non-contextual models on every cover and under both conditions: nothing obstructed, in any ring. No false positive in any ring, in 2,400 models. Proposition 20 of [2] never violated: no ℤ-vanishing class failed to vanish over ℚ or ℤ₂. Four things are in the table.

**The rings, off the cycle.** ℤ and ℤ₂ agreed on every section of every model. The prediction was that they would disagree somewhere; they did not, and with §3 the reading is that on these covers the integer obstruction's torsion, where it has any, is 2-torsion — which ℤ₂ sees — and never odd torsion, which it would not. ℤ and ℚ disagreed on three sections, all in strongly contextual no-signalling (3,3,2) models built of correlations and anti-correlations: parity structures, the (3,3,2) cousins of the square. Off the cycle the ring matters exactly where the model is a parity argument, and nowhere else in the sweep.

**No-signalling is where the invariant is blind.** Under the literature's condition the logical-grade rates are 0.074, 0.049 and 0.012 — against 0.71 and 0.60 on the cycles of *The Obstruction, Computed* — and three logically contextual models in four, nine in ten and forty in forty-one are invisible at every section. The three covers order themselves by how many routes a formal family has around: the (3,3,2) nerve is K₃,₃, the GHZ nerve is K₄ on three-outcome-per-context supports, the Peres–Mermin nerve is K₃,₃ on eight-outcome contexts, and the more routes, the more misses.

**Signalling is what the invariant sees.** The prediction, stated before this measurement and after the others: a state absent from one context's support but present in another's is a node with no edges in the first layer, conservation at that node forces the sums of the layers that do contain it to zero, and that is a route a formal family cannot take. Without the no-signalling filter the same covers are seen at 0.755, 0.366 and 0.457 in the logical grade and every strongly contextual model is seen. The condition that makes an empirical model physically meaningful is the condition under which the invariant is weakest.

**The strong grade is seen and not at every section.** Every strongly contextual signalling model on every cover is seen, at section rates of 0.93, 0.47 and 0.57; five of eight no-signalling strong (3,3,2) models are seen and three missed entirely. Cohomologically logically contextual and not cohomologically strongly, again, and on the no-signalling side sometimes neither.

---

## 5. Four Holons on K4

`code/covers.py`, Part 3. Two-port holons make cycles and nothing else. A holarchy with chords needs a holon with three interfaces, and the specimen is the smallest one: four three-port holons on the complete graph K4, every holon in three of the six interfaces, so the cover's nerve is the octahedron and every pair of interfaces at a holon overlaps there. A holon is an internal star — a centre and three port vertices, each internal edge with a declared map — on a binary menu, unit vectors at 0° and 180°, so declared maps are the identity or the half turn. Its gate is the Rayleigh-quotient gate as before: a mismatched internal edge costs 4, the quotient is the energy over four vertices, and ε counts the mismatches allowed: ε = 0 admits the two exactly-transported states, ε = 1 admits eight, ε = 3 admits all sixteen. An interface requires the two ports to agree up to its declared half turn.

**Proposition 5.1 (exact gates).** With ε = 0 at every holon, each port is the centre plus the internal edge's declared map, so an interface is a mod-2 linear equation in two centre bits, and a global section exists iff the six equations in four unknowns are consistent — iff the mod-2 holonomy vanishes on every cycle of K4, three independent conditions. When it does not, no global section exists, every interface still has admissible pairs, the model is strongly contextual, and its contradiction is a system of ℤ₂-linear equations with no solution: an all-versus-nothing argument, witnessed at every section over ℤ₂ and hence over ℤ ([2], Theorem 21 and Proposition 20). ∎

| trial | holonomy consistent | grade | sections | non-extending | obstructed ℤ / ℚ / ℤ₂ |
|---|---|---|---|---|---|
| 0, 1, 2, 5, 6 | no | strong | 12 | 12 | 12 / 12 / 12 |
| 3, 4, 7 | yes | non-contextual | 12 | 0 | 0 / 0 / 0 |

Eight seeded trials, no row against the prediction — and the rationals see these, because the K4 parity system with two-element supports is small enough that its contradiction is not only mod 2: with two states per holon the Čech system has no room for a half.

Then one hundred holarchies with ε drawn from {0, 1, 3} per holon:

| grade | models | sections | non-extending | obstructed ℤ | rate | ℤ¬ℚ | ℤ¬ℤ₂ | seen | missed |
|---|---|---|---|---|---|---|---|---|---|
| non-contextual | 12 | 4,992 | 0 | 0 | — | 0 | 0 | — | — |
| logical | 81 | 14,052 | 7,056 | **7,056** | **1.000** | 0 | 0 | 81 | **0** |
| strong | 7 | 258 | 258 | 258 | 1.000 | 0 | 0 | 7 | 0 |

The prediction was that misses would occur. None did. Every non-extending section of every one of 88 contextual holarchies is obstructed, in every ring. On the cycle a tolerance gate was exactly where a miss lived; on K4 the tolerance gates are there — 81 logical models are logical because of them — and the invariant sees through every one. §4's mechanism says why: a gate model signals. An ε = 1 holon has eight admissible states, and which of them appear in a given interface's support depends on that interface's map and the neighbour's states; a state that one interface drops and another keeps is a node with an empty layer, and the three interfaces at a holon pin its coefficient sums to each other three ways. With four holons each in three contexts, there is no route around.

---

## 6. What the Chord Bought

***The Obstruction, Computed*.** Its §9.2 asked whether the reachability theorem reaches non-cyclic covers. It does not, in either of its consequences: the ring matters off the cycle (§3), and a miss is no longer a reversal through a tolerance gate but the absence of a signalling node to stop a formal family (§§4–5). Its Corollary 6.4, ring-independence on cycles, now has its complement: off the cycle the ring that matters is the one the model's contradiction lives in, and for parity models that is ℤ₂, not ℚ.

***No Global Section*.** §5 said a vanishing class licenses nothing. Under the literature's own no-signalling condition it licenses almost nothing *and detects almost nothing*: on chorded covers the logical grade is seen at a few percent. The paper's grading survives; its invariant, on no-signalling models with chords, is close to inert. And the same section's "H¹ = 0 does not even certify that the levels compose" gains a converse for mechanisms: gate models signal, so for them the invariant is far better than the literature's setting would suggest. The obstruction is a poor test of physics and a good test of gates.

**The rings, for a designer.** Compute over ℤ. ℤ₂ agreed with ℤ on every section here and is cheaper, but §3 says the agreement is the absence of odd torsion, not a theorem; ℚ is blind to every parity argument and should not be used at all. The literature's mod-2 machine checks were, on every model here, exact in both directions.

**The holarchies of the corpus.** *The Budget Across Levels* priced a holarchy in which a block coalition has two to four boundary edges and every interface carries a residual gate. That gate scenario has chords everywhere — every holon of the seed-7 complex is in several interfaces — and its gates, being residual thresholds, are tolerances. §5 says that is the regime in which the invariant sees everything, for the reason that interfaces select states. The prediction stands sharper than before: the program's own mechanism is cohomologically transparent, and the obstacle to computing it is size, not theory.

**Conjecture R, a tenth time.** The free module forgets the sign; over ℚ it also forgets parity. The formalism relocated the difficulty into the coefficient ring, and what the formalism does not supply is the characteristic.

---

## 7. What Is Declined

**That the rational vanishing is new as a fact.** Proposition 20 of [2] and the mod-2 machine checks of [1] put the pieces in one place, Montanhano [6] states the thesis for a different object, and an expert would expect a parity contradiction to vanish over ℚ. What is claimed is the computation and its statement: the literature's two flagship models are invisible to the rational invariant at every section, with the families written down. The remark in [2] that an implication of its Theorem 21 reverses over a field concerns the outcome ring — ℤ₂ is a field — and not the coefficient characteristic.

**That ℤ = ℤ₂ is a theorem.** It is the absence of odd torsion in some sixty thousand sections on four covers. A model whose contradiction is a mod-3 argument would separate them, and none was built.

**That the covers are general.** Three covers and one holarchy, all small, all binary-outcome. The (3,3,2) and Peres–Mermin nerves are K₃,₃ and the GHZ and K4 nerves are K₄ and the octahedron; a cover with a measurement in four contexts, or overlaps of two measurements, was not computed.

**That the random models are representative.** Half are extensions of random global sets and half random supports; both are conventions. The rates are the rates of these generators, and the *comparison* between the no-signalling and signalling halves is the finding, not the rates themselves.

**That signalling is a virtue.** A signalling empirical model is unphysical in the setting the invariant was built for. A gate model signals for a structural reason — an interface selects the states that agree across it — and the paper says only that the invariant sees that structure, not that a designer should introduce signalling to be seen.

**That the K4 result is a theorem.** One hundred holarchies with one menu and one gate family had no miss. The mechanism is stated and consistent with §4; whether a three-port holarchy with a richer menu, or a holon in four interfaces, admits a miss is not known.

**That the instrument reaches the program's mechanism.** It still enumerates. §6's prediction that the seed-7 complex with residual gates is cohomologically transparent is a prediction.

---

## 8. Open Problems

**8.1. Odd torsion.** Build a model whose contradiction is a mod-3 argument — three-outcome measurements with a ternary parity — and measure whether ℤ and ℤ₂ separate there, as §3's reading says they must. That would make the designer's rule "compute over ℤ" a demonstrated necessity rather than a precaution.

**8.2. The signalling theorem.** §4's mechanism is a proof sketch: a node with no edges in a layer zeroes its sums in every layer. Whether it can be made into a bound on the miss rate in terms of how much a model signals — how many (measurement, outcome) nodes are absent from some context's support — is the quantitative form.

**8.3. Conservation on a hypergraph.** The cyclic theorem's flow argument fails off the cycle because a section is a hyperedge on all its overlaps. Whether a section's class has a combinatorial characterisation on a general cover — a hyperflow, a matroid condition — is the question *The Obstruction, Computed* §9.2 asked and this paper only measured.

**8.4. The mechanism itself.** §6's prediction, now with a mechanism behind it. A solver that does not enumerate, on the seed-7 complex with residual gates discretised.

**8.5. What a designer computes.** On a cycle, a graph search; on a chorded gate scenario, a Smith normal form over ℤ that sees everything a coalition can do to the gates. Whether the second is cheap enough to run per epoch on a deployed holarchy, and what it certifies when it vanishes there — nothing, still, but a nothing that §5 says is rarely wrong — is the question that would make the invariant a tool.

---

## References

[1] S. Abramsky, S. Mansfield, R. S. Barbosa. *The Cohomology of Non-Locality and Contextuality.* QPL 2011, EPTCS 95, 1–14, 2012. arXiv:1111.3620.

[2] S. Abramsky, R. S. Barbosa, K. Kishida, R. Lal, S. Mansfield. *Contextuality, Cohomology and Paradox.* CSL 2015, LIPIcs 41. arXiv:1502.03097.

[3] G. Carù. *On the Cohomology of Contextuality.* QPL 2016, EPTCS 236, 21–39, 2017. arXiv:1701.00656.

[4] G. Carù. *Towards a Complete Cohomology Invariant for Non-Locality and Contextuality.* arXiv:1807.04203, 2018.

[5] S. Abramsky, A. Brandenburger. *The Sheaf-Theoretic Structure of Non-Locality and Contextuality.* New Journal of Physics 13, 113036, 2011. arXiv:1102.0264.

[6] S. B. Montanhano. *Characterization of Contextuality with Semi-Module Čech Cohomology and Its Relation with Cohomology of Effect Algebras.* arXiv:2104.11411, 2021.

[7] G. Carù. *Logical and Topological Contextuality in Quantum Mechanics and Beyond.* DPhil thesis, University of Oxford, 2019.

Propositions verified and measurements reproducible from `code/covers.py`, which imports the models, the Čech system and the integer and rational solvers of `code/contextuality.py` unchanged and adds the mod-2 solver, the answer key with chords, the random generators and the K4 holarchy.
