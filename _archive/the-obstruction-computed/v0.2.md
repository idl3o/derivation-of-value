---
layout: document
title: "The Obstruction, Computed"
subtitle: "Conjecture 3.1 on Gate Scenarios with Spectral Gates"
eyebrow: "An Anthology · Paper · v0.2"
permalink: /the-obstruction-computed/
anthology: "Derivation of Value"
version: "v0.2"
date: 2026-09-07
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "No Global Section rested its quantitative content on a conjecture it did not test: that the cohomological obstruction of Abramsky, Mansfield and Barbosa applies to gate scenarios with no affine hypothesis on the gates. It does, and no distribution has to be chosen for it, because the obstruction is computed on the support alone and a gate model is a support. Built on an answer key the literature settled — Bell extends everywhere, Hardy's one non-extending section is missed, the PR box is obstructed at every section — the instrument is then pointed at holons with a threshold on a spectral quantity for a gate. Every strongly contextual gate model is seen; two in five logically contextual ones are invisible to the invariant at every section; the integers and the rationals never disagree; and what decides a miss is how many open gates sit in a row. A vanishing class licenses nothing, now with a rate attached. v0.2 replaces the first reading of what decides a miss with a theorem: on a cyclic cover the obstruction is undirected reachability in the bundle diagram with the section's layer removed, extension is directed reachability, the two differ only through a relation in the chain that is connected without being a union of complete bipartite blocks, and the obstruction is independent of the coefficient ring."
status: "v0.2 · working draft"
order: 24
---

## Abstract

*No Global Section* identified composition failure in nested mechanisms with contextuality in the sense of Abramsky and Brandenburger, and conjectured that the cohomological obstruction Abramsky, Mansfield and Barbosa built for that setting applies to gate scenarios — holons as measurements, interfaces as contexts, gate-admissible states as outcomes — with no assumption that the gates are affine. The conjecture was load-bearing and untested, and the paper worried that a mechanism designer would have to choose the distributions the construction seemed to need. This paper computes it. The obstruction is computed on the *support* of a model, the local sections that are possible, and a gate model is a support: no distribution enters, the probabilistic grade of contextuality is simply unavailable to a gate model, and the logical and strong grades are all it has. The invariant is an integer linear system — formal integer combinations of local sections at every context, agreeing on every overlap, fixed to the indicator of the section in question — solved exactly here over the integers by Smith normal form and over the rationals by elimination. The instrument is calibrated first on the models whose grade the literature settled: the Bell model, possibilistically non-contextual, has nothing obstructed; the Hardy model's one non-extending section has vanishing obstruction, the standard miss; the PR box is obstructed at every section; and *Gluing the Gates* Proposition 4.2's affine cycle, on a finite menu, is obstructed at every section. Zero false positives in some thirty thousand sections. It is then pointed at holons with a threshold on a spectral quantity for a gate — the Rayleigh quotient of a declared internal connection, a sublevel set of a quadratic form on a product of circles — on triangles and squares, with the truth brute-forced. With every gate exact, each interface is a bijection of port states, the triangle is strongly contextual exactly when the rotation composed around it is not the identity, and every section is then obstructed, by an orbit argument stated before running. With looser gates, of 233 logically contextual gate models 136 are seen by at least one section and 97 are invisible to the invariant at every section; the section-level rate is 0.71 on triangles and 0.60 on squares; every strongly contextual model is seen but not at every section, so the program's strong gate models are cohomologically logically contextual and not all cohomologically strongly contextual, which is Carù's observation on the program's specimen. The integers and the rationals never disagree, and the literature says why. What decides a miss was first read as the longest run of open gates around the cycle; v0.2 replaces the reading with a theorem. On a cyclic cover the compatibility condition is flow conservation on the bundle diagram, so the obstruction of a section vanishes exactly when its two ends are joined by an undirected path avoiding its own layer, over any coefficient ring — which is why the integers and the rationals never disagreed — while the section extends exactly when they are joined by a directed one. The walk passes through the chain of holons not incident to the layer, and undirected and directed reach through a relation coincide exactly when the relation is a disjoint union of complete bipartite blocks: a bijection is, the complete relation is, and the one gate in between is connected without being either. So a layer is miss-free exactly when its chain has no such holon, and the rule holds on every one of the sweep's 1,050 layers and 233 logically contextual models. The conjecture holds in the form stated, the affine hypothesis of *Gluing the Gates* is discharged in practice, and *No Global Section* §5's "a vanishing class licenses nothing" now carries a rate. The prior art is drawn — the construction is Abramsky's group's, its misses are theirs and Carù's, and its export to databases, constraint satisfaction and revealed preference precedes this — and what is claimed is the application to gate scenarios, the observation that no distribution is needed, and the measurements.

---

## 1. The Computation

*No Global Section* §3 stated one conjecture and rested on it. *Gluing the Gates* had located the obstruction to composing conjunction-gated mechanisms in the first Čech cohomology of a gate sheaf, under the hypothesis that gate conditions are affine on stalks, and the program's own worked instance — a threshold on a spectral quantity — is not affine. The contextuality literature, *No Global Section* observed, had faced the same difficulty and passed it by working with an abelian presheaf derived from a model's support rather than with the sets of admissible states themselves; Conjecture 3.1 said the same construction applies to gate scenarios. §7 declined to claim it established. §8.1 asked for the computation, on a small scenario with genuinely non-affine gates, and said it was a computation and not a research programme. §8.2 worried that the designer would have to choose the distributions. The plan's own risk note put it more sharply: the contextuality setting is probabilistic and gates are deterministic thresholds.

This paper is the computation, and it returns three things.

The first is that the worry was misplaced, and for a reason worth stating exactly. The obstruction of Abramsky, Mansfield and Barbosa [2] is built on the *support* of an empirical model — at each context, the set of local sections that are possible — and on the free ℤ-module over that set. Probabilities never enter the construction; they enter only the *probabilistic* grade of contextuality, which asks whether observed frequencies can be reproduced by a global distribution. A gate model is a support. Its contexts are interfaces, its local sections are the admissible joint states of the holons meeting there, and it has no frequencies. So a gate model has two grades of contextuality, logical and strong, and not three, and the obstruction applies to it with no choice made anywhere (§3).

The second is that the invariant behaves on gate scenarios exactly as the literature says it behaves on quantum ones: it never fires falsely, it fires on every section of every strongly contextual model the program can build with exact gates, and it misses. Of the logically contextual gate models in the sweep, two in five are invisible to it at every section (§5). *No Global Section* §5 said that a vanishing class licenses nothing. It now says so with a rate.

The third is structural, and v0.2 states it as a theorem where v0.1 read it off two tables. On a cyclic cover the obstruction is undirected reachability in the bundle diagram with the section's own layer removed, and extension is directed reachability (§6). A miss is a walk that has to reverse, and a reversal changes a junction value only through a relation that is connected without being a union of complete bipartite blocks. The gate specimen has exactly one such relation, the intermediate gate, and a layer is miss-free exactly when the chain of holons not incident to it contains none (§§5–6). The first reading — a run of open gates — ~~was the rule~~ was that theorem's shadow on two cycles, and is struck in §5.

The conjecture holds in the form stated. Everything below is exact arithmetic, calibrated on an answer key before the program's own scenarios are touched, with the predictions stated in `code/contextuality.py` before running and the one that failed recorded.

---

## 2. Prior Art, and the Boundary of the Claim

The construction is not this paper's, and neither are its limits; both are drawn here so that §§3–5 claim only the application.

Abramsky and Brandenburger [1] characterise non-locality and contextuality as the obstruction to extending a compatible family of local sections to a global one, grade it into probabilistic, logical and strong — Bell below Hardy below GHZ — and prove that every no-signalling model has a global distribution with *negative* probabilities, so the obstruction is in the sign, not the arithmetic. Abramsky, Mansfield and Barbosa [2] build the Čech invariant computed here: the support presheaf, the free ℤ-module functor, the relative presheaf for a chosen context, and the proposition that the class of a section vanishes exactly when the section extends to a compatible family of formal combinations. They compute it for the PR box, GHZ, the Peres–Mermin square and the eighteen-vector Kochen–Specker model, all detected at every section, and for the Hardy model, where the section (a₁, b₁) ↦ (0, 0) extends to no global assignment and the obstruction nevertheless vanishes by an explicit family with a negative coefficient. They call that a *false positive*, since the invariant falsely certifies extendability; read as a detector of contextuality it is a false negative, and this paper says *miss* and glosses it once. Abramsky, Barbosa, Kishida, Lal and Mansfield [3] prove the invariant witnesses every all-versus-nothing argument, that the integers are the most sensitive coefficient ring — a vanishing class over ℤ vanishes over every ring — and list the Specker triangle among the models ℤ-cohomology detects. Carù [4] refutes the conjecture that symmetry and connectedness make the invariant complete for strong contextuality, on a two-party, two-measurement, four-outcome model that is strongly contextual and not cohomologically contextual at any section, and shows the higher Čech groups add nothing for no-signalling models; Carù [5] gives an iterated refinement complete for cyclic scenarios, on arXiv only.

The framework has left physics before, by its authors' hands: to relational databases, where the failure of a universal relation is the absence of a global section [6]; to robust constraint satisfaction [7]; and, by Zeng and Zahn [8], to revealed-preference theory, where budgets are contexts, choices are outcomes, the weak axiom is placed against no-signalling, and the cohomology is not computed. Ó Conghaile [9] carries the Čech obstruction into constraint satisfaction and structure isomorphism. In a separate, cellular-sheaf tradition, Felber, Hummes Flores and Rincon Galeana [10] characterise solvable distributed tasks as global sections, and Hansen and Ghrist [11] read consensus as a sheaf Laplacian's kernel; neither cites the obstruction. No application to mechanism design, incentives, organisations or nested admissibility was found.

For the theorem of §6 the nearest prior work is drawn separately. That a global section on a cycle is a closed path through every fibre once is explicit in [3] — a *univocal* closed path — and in Abramsky's later exposition; Santos and Amaral [12] state its possibilistic contrapositive on n-cycles as a blocked chain of implications. Carù [5] reads a compatible family for the free-module presheaf as a path in the planar bundle diagram with +1 on segments traversed left to right and −1 on those traversed right to left, and observes that a Z-shaped path "appears to be" what is responsible for most known misses; his thesis [13] draws the Hardy miss as a twisted loop. Montanhano [14] locates the same culprit in the negative coefficient and removes it by passing to semi-fields, at the price of a different invariant. Mansfield [15] proves the ℤ-obstruction complete for Kochen–Specker models on a closed chain of contexts, by perfect matchings. None of these states that on a cyclic cover the obstruction *is* undirected reachability, none states the ring-independence that follows, and Carù chooses ℤ₂ for his completeness proof and calls the ring choice crucial. Theorem 6.3 makes his Theorem 7.7 ring-independent as a statement, since his joint models on a cyclic cover are cyclic covers.

What is claimed. That a gate scenario's model is a support and the obstruction applies to it with no distribution chosen, so that gate models carry two grades and not three (Proposition 3.1). That the invariant is an integer linear system solvable exactly, one matrix per context (Proposition 3.2). That with exact gates the cyclic holarchy is strongly contextual exactly when its composed rotation is not the identity, and is then obstructed at every section (Proposition 4.1). That on a cyclic cover the obstruction vanishes exactly when the section's ends are joined by an undirected path avoiding its layer, over any ring, while extension is a directed path, so that a miss is exactly a reversal and lives only through a relation that is not a union of complete bipartite blocks (§6) — the biconditional and its ring-independence, which the informal reversal reading of [5, 13, 14] and the chain-model completeness of [15] and [5] come close to and do not state. And the measurements: the answer key reproduced, the detection rates by grade, the agreement of ℤ and ℚ, and the theorem verified on every section. The construction, its misses, and its exports are cited, not claimed.

---

## 3. The Construction on a Gate Scenario

`code/contextuality.py`, Part 1. A *possibilistic empirical model* is a set of measurements X, a set of outcomes O_m for each, a cover of contexts C ⊆ X, and at each context a support S(C) ⊆ Π_{m∈C} O_m of local sections. A section s ∈ S(C) *extends* if some global assignment g ∈ Π_m O_m has g\|_C = s and g\|_{C′} ∈ S(C′) for every context. The model is *strongly contextual* if no global assignment exists, *logically contextual* if some section does not extend, and possibilistically non-contextual otherwise [1].

**Definition 3.1 (gate model).** For a holonic substrate and induced mechanism in the sense of *Gluing the Gates* Definitions 3.1–3.3, the gate model has holons as measurements, each holon's gate-admissible states as its outcomes, interfaces as contexts, and at each interface the support of admissible joint states that agree there. This is *No Global Section* Definition 2.1 with the distributions removed.

**Proposition 3.1 (no distribution is chosen).** The obstruction of [2] is defined on the support presheaf S alone: F(C) is the free ℤ-module on S(C), restriction is extended linearly, and for s ∈ S(C₀) the class γ(s) in the relative Čech H¹ vanishes iff s extends to a compatible family {r_i ∈ F(C_i)} with r₀ = s ([2], Proposition 4.3). A gate model supplies S(C) directly. So the construction applies to a gate model with no probabilities and no choice, and *No Global Section* §8.2's question — which distributions — is confined to the probabilistic grade, which a gate model does not have. ∎

**Proposition 3.2 (the invariant is an integer linear system).** Let the unknowns be integer coefficients a^i_t, one per local section t of each context C_i ≠ C₀. For each pair of contexts and each assignment u on their overlap, the coefficients of sections restricting to u must sum equally on both sides, with C₀'s side fixed to the indicator of s. γ(s) = 0 iff the system has an integer solution. *This is [2]'s compatibility condition written out; [2] solves it by hand for the PR box and by machine mod 2 for the larger models, and [3] Proposition 21 shows ℤ is the most sensitive ring, since a vanishing class over ℤ vanishes over every ring.* ∎

The instrument solves the system exactly over ℤ by Smith normal form, with the row operations applied to every section of the context as a batched right-hand side, and over ℚ by rational elimination, no floating point anywhere; it brute-forces the global assignments so that every section's truth is known; and a section that is obstructed and extends is a false positive, which the theorem forbids and which the instrument flags as a solver error.

**The answer key.** Four models whose grade the literature settled, run before anything of the program's:

| model | grade | sections | non-extending | obstructed, ℤ | obstructed, ℚ | globals |
|---|---|---|---|---|---|---|
| Bell/CHSH | non-contextual | 14 | 0 | 0 | 0 | 8 |
| Hardy | logical | 13 | 1 | **0** | 0 | 5 |
| PR box | strong | 8 | 8 | 8 | 8 | 0 |
| affine cycle (*Gluing the Gates* Prop 4.2) | strong | 9 | 9 | 9 | 9 | 0 |

The Bell model's support has a global section, so nothing is obstructed and nothing should be; the invariant is blind by construction to probabilistic contextuality. Hardy's one non-extending section has vanishing obstruction, the miss [2] records by an explicit family. The PR box is obstructed at every section, as [2] shows by forcing all coefficients equal and then 1 = 0. And *Gluing the Gates*' affine specimen — x_u = 2x_v around a triangle, on the menu {1, 2, 4, 8}, each holon admitting any nonzero value, the cycle composing to x = 8x — is strongly contextual and obstructed at every section; the affine case is the case Claim 4.3 of that paper covered, and the invariant that needs no affineness agrees with it there. False positives: zero.

---

## 4. Spectral Gates

`code/contextuality.py`, Part 2. Stalks ℝ², and a menu of four unit vectors at 0°, 90°, 180° and 270°, closed under rotation by a quarter turn, so a declared restriction map R_k is a rotation and acts on the menu by an index shift. A holon is one internal edge with a declared rotation, its two vertices its two ports, and its state a menu vector at each. Its gate is the **Rayleigh-quotient gate**: the section's Dirichlet energy under the declared internal connection, x^T L x / x^T x, at or below a threshold ε. That is a threshold on a spectral quantity, not affine — the sublevel set of a quadratic form on a product of circles — and it is the kind of gate *Proof of Coherence* reads. A quarter-turn mismatch on the internal edge costs 1 per vertex and a half-turn 2, so ε = 0 admits the four exactly-transported states, ε = 1 admits twelve, and ε = 2 admits all sixteen: the gate open. An interface (u, p_u, v, p_v, k) requires x_u[p_u] = R_k x_v[p_v]. Holons sit on a triangle or a square, each interface joining one holon's second port to the next holon's first.

**Proposition 4.1 (exact gates).** With ε = 0 at every holon, each holon's admissible set is the graph of a bijection between its ports, so each interface's support is the graph of a bijection between the port states of the holons it joins, and the model has a global section iff the rotation composed once around the cycle is the identity. When it is not, every local section is obstructed over ℤ. *Proof.* A compatible family assigns to each context a coefficient per section; agreement at a holon between its two contexts identifies the coefficient functions through the bijection, so around the cycle the coefficients at any one context must be constant on the orbits of the composed permutation. A non-identity rotation of the four menu states is fixed-point-free, so every orbit has more than one element, and the indicator of s is not constant on the orbit of s. ∎

| trial | composed rotation | grade | sections | non-extending | obstructed, ℤ | obstructed, ℚ |
|---|---|---|---|---|---|---|
| 0 | 2 | strong | 12 | 12 | 12 | 12 |
| 1 | 1 | strong | 12 | 12 | 12 | 12 |
| 2 | 3 | strong | 12 | 12 | 12 | 12 |
| 3–6 | 1, 1, 1, 3 | strong | 12 | 12 | 12 | 12 |
| 7 | 0 | non-contextual | 12 | 0 | 0 | 0 |

Eight seeded triangles, no row against the prediction. The Specker triangle of [3] is the two-state instance of this proposition; the program's is the four-state one, and its cohomology sees it for the same reason.

---

## 5. The Sweep

`code/contextuality.py`, Parts 3–4. One hundred and fifty triangles and one hundred and fifty squares, every holon's ε drawn from {0, 1, 2} and every rotation drawn uniformly, seeded. For each model: the grade, brute-forced; every section's extendability; every section's obstruction over ℤ and over ℚ.

| cycle | grade | models | sections | non-extending | obstructed ℤ | rate | ℤ ≠ ℚ | models seen | missed | false pos. |
|---|---|---|---|---|---|---|---|---|---|---|
| triangle | non-contextual | 4 | 588 | 0 | 0 | — | 0 | — | — | 0 |
| triangle | logical | 139 | 12,504 | 4,224 | 3,016 | **0.714** | 0 | 94 | **45** | 0 |
| triangle | strong | 7 | 164 | 164 | 144 | 0.878 | 0 | 7 | 0 | 0 |
| square | non-contextual | 54 | 9,112 | 0 | 0 | — | 0 | — | — | 0 |
| square | logical | 94 | 8,624 | 2,212 | 1,336 | **0.604** | 0 | 42 | **52** | 0 |
| square | strong | 2 | 64 | 64 | 48 | 0.750 | 0 | 2 | 0 | 0 |

*Rate* is the fraction of non-extending sections the ℤ-obstruction sees; a model is *seen* if at least one of its non-extending sections is obstructed and *missed* if none is. Four things are in the table.

**No false positive, in 31,056 sections.** The theorem holds and the solver is right.

**Every strongly contextual model is seen, and not at every section.** Nine strong models, all seen; but 20 of their 228 sections have vanishing obstruction. In [3]'s terms the program's strong gate models are cohomologically *logically* contextual and not all cohomologically *strongly* contextual — the gap Carù [4] exhibited on a four-outcome square, here on the program's own holons with looser gates than Proposition 4.1's. Where every gate is exact the two coincide (§4).

**Two in five logically contextual models are invisible.** Of 233, 97 have vanishing obstruction at every non-extending section: a mechanism designer computing the invariant on them would find nothing, and every one of them has an admissible local configuration no global configuration contains — the regime *No Global Section* §4 called the one an adversary wants. §5 of that paper said a vanishing class licenses nothing. The rate is 42%.

**ℤ and ℚ never disagree.** The prediction was that they would, on a few sections, with ℤ the stronger; they agreed on all 31,056. The direction was the literature's ([3] Proposition 21: ℤ detects whatever any ring detects), and the equality is what these scenarios returned. The prediction is recorded as missed.

**What decides a miss.** Binning the logically contextual models by how many of their holons have an exact gate:

| cycle | exact gates | models | seen | missed | section rate |
|---|---|---|---|---|---|
| triangle | 0 | 45 | 0 | **45** | 0.000 |
| triangle | 1 | 72 | 72 | 0 | 0.901 |
| triangle | 2 | 22 | 22 | 0 | 1.000 |
| square | 1 | 44 | 0 | **44** | 0.000 |
| square | 2 | 38 | 30 | 8 | 0.854 |
| square | 3 | 12 | 12 | 0 | 1.000 |

The first reading of the triangle rows — one exact gate suffices — was wrong, and the square rows say so: one exact gate there leaves every model missed. ~~What the two cycles share is the length of the longest run of *open* gates around the cycle. Two in a row is seen; three in a row is missed.~~ **Struck in v0.2.** That was the shadow on two cycles of the theorem in §6: a layer is miss-free exactly when the chain of holons not incident to it contains no ε = 1 holon, and a logical model is seen exactly when some such layer has a non-extending section. On the triangle a chain is one holon, so the rule reads "some holon is not at ε = 1 and its opposite layer has a non-extending section"; on the square a chain is two adjacent holons, so it reads "two adjacent holons are not at ε = 1". Binned by exact gates, those look like a run length. The rule as stated agrees on all 233 logically contextual models (§6), and the run length does not survive a third cycle.

---

## 6. The Theorem on Cycles

`code/contextuality.py`, Part 5. The sweep's two unexplained regularities — ℤ and ℚ never disagreeing, and visibility binning by exact gates — have one cause, and it is a theorem about cyclic covers rather than about gates.

**Definition 6.1 (section graph).** For a cyclic cover (below), the *section graph* has a node for each pair (overlap, assignment) — an overlap of consecutive contexts and an assignment of outcomes to its measurements — and, for each context C and each local section t ∈ S(C), an edge from t's restriction to C's overlap with its predecessor to t's restriction to its overlap with its successor; edges are grouped in *layers* by context. When overlaps are single measurements, as in every scenario computed here, the nodes are (measurement, outcome) pairs and the graph is the bundle diagram of the contextuality literature with its sections drawn as edges.

**Definition 6.2 (cyclic cover).** Contexts C₀, …, C_{n−1}, consecutive ones overlapping and non-consecutive ones disjoint — Carù's cyclic scenario [5], a chordless cycle of contexts — each context oriented from its overlap with its predecessor to its overlap with its successor. A local section s of C_i then has a *tail* at its restriction to the predecessor overlap and a *head* at its restriction to the successor overlap.

**Theorem 6.3 (the obstruction on a cyclic cover is reachability).** Let R be any commutative ring with 1 ≠ 0. On a cyclic cover, the obstruction γ_R(s) of a section s of C_i vanishes if and only if head(s) and tail(s) are joined by an *undirected* path in the section graph with the layer C_i removed.

*Proof.* A compatible family assigns an element of R to every edge of every layer. The compatibility condition at the overlap of consecutive contexts, for each assignment u on it, says that the coefficients of the earlier layer's edges ending at u sum to the coefficients of the later layer's edges starting there: conservation of an R-valued flow at every node. Non-consecutive contexts share nothing and impose nothing. Fixing C_i's coefficients to the indicator of s makes s a unit edge from tail(s) to head(s) and zeroes the rest of its layer, so γ_R(s) = 0 iff the other n − 1 layers carry an R-flow of unit demand from head(s) to tail(s). If an undirected path exists, assign +1 to its edges traversed with their orientation and −1 against, and 0 elsewhere: a unit flow, over any ring. Conversely, let a unit flow exist and let U be the set of nodes reachable from head(s) in the undirected support of the flow. Summing conservation over U, every edge crossing the boundary of U carries zero flow, so the net flow into U from outside is 0; but the unit edge s enters U at head(s) from tail(s), so if tail(s) ∉ U the net inflow is 1, and 1 = 0 in R. Hence tail(s) ∈ U. ∎

**Corollary 6.4 (ring independence).** On a cyclic cover γ_ℤ, γ_ℚ and γ_{ℤ₂} vanish together. *This is why §5's prediction that ℤ and ℚ would differ was missed: on these covers they cannot.* [3] Proposition 21 gives one direction for every cover; the theorem gives both for cyclic ones.

**Proposition 6.5 (extension is directed reachability).** On a cyclic cover a global section is a closed walk through every layer once in orientation, so s extends iff head(s) and tail(s) are joined by a *directed* path avoiding C_i that traverses the remaining layers in cyclic order. ∎

A *miss* is therefore an undirected path where no directed one exists: a walk that reverses. Where it can reverse is a property of the relations along the way.

**Corollary 6.6 (where a miss can live).** Removing layer C_i leaves a path of layers through the n − 2 measurements not in C_i — the *chain*. Write A_h ⊆ J_h × J_{h+1} for the relation a measurement h in the chain induces between the outcome-values on its two sides, in the gate models the admissible (port-0, port-1) pairs of holon h. Directed reach through A_h of a set S ⊆ J_h is A_h(S); undirected reach is the union of the connected components of A_h's bipartite graph that meet S. These coincide for every S iff every component of A_h is complete bipartite — A_h is a disjoint union of complete bipartite blocks, *rectangular*. So a layer whose chain consists of rectangular relations has no miss; and if some relation in the chain is connected on all values, every section in the layer has vanishing obstruction, extending or not. ∎

On the specimen the three gates are the three cases. ε = 0 is a bijection, one-by-one blocks. ε = 2 is the complete relation, one block. ε = 1 — port-1 within a quarter turn of the transported port-0, three values of four — is connected and not rectangular: it is the one gate through which a walk can arrive at a junction value by one route and leave by another, which is the Z-shaped combination of the Hardy family. Hence:

**Proposition 6.7 (the rule, on the specimen).** A layer has a miss iff its chain contains an ε = 1 holon and the layer has a non-extending section; a layer whose chain contains an ε = 1 holon has every section vanishing; a logically contextual model is seen iff some layer has an ε-1-free chain with a non-extending section.

| cycle | sections | undirected = vanishes | directed = extends | ε-1-free chains: layers / misses | ε = 1 chains: layers / obstructed | logical models / rule agrees |
|---|---|---|---|---|---|---|
| triangle | 13,256 | 13,256 | 13,256 | 281 / **0** | 169 / **0** | 139 / **139** |
| square | 17,800 | 17,800 | 17,800 | 259 / **0** | 341 / **0** | 94 / **94** |

Every count is exact. Theorem 6.3 and Proposition 6.5 are verified on all 31,056 sections of the sweep and on the four models of the answer key; Corollary 6.6's two halves — no miss through rectangular chains, no obstruction through a connected non-rectangular one — hold on all 1,050 layers; and Proposition 6.7 agrees with the brute force on all 233 logically contextual models. The exact-gate bins of §5 fall out: on the triangle a chain is one holon, on the square two adjacent ones, and "a run of open gates" was the count of ε = 1 holons in a chain seen through the wrong variable.

**What the theorem says to a designer.** On a cyclic holarchy the invariant is a graph search, not a cohomology computation; a miss is a reversal; and the gates that permit a reversal are the ones that relate their two sides by a connected, non-rectangular relation — a gate that admits *some* but not *all* of the transported values. A gate that is exact, or a gate that is open, cannot hide a miss. The gate that can is the one a designer would call a *tolerance*.

---

## 7. What the Conjecture Bought

***No Global Section*.** Conjecture 3.1 holds in the form stated: the construction applies, with no affine hypothesis, and detects — with the literature's misses. §3's worry that the designer would have to choose the distributions is resolved by Proposition 3.1: nothing is chosen, because nothing probabilistic enters. §4's three grades become two for a gate model, which is a sharpening rather than a loss — the probabilistic grade described a mechanism *miscalibrated across runs*, and a gate model, having no runs, cannot be. §5's "a vanishing class licenses nothing" has a rate: two in five — and on a cyclic cover, a criterion: the class vanishes on a non-extending section exactly where a walk can reverse through a tolerance gate (§6). §8.1 is struck; §8.2 is answered for the obstruction and remains open for whatever a designer might want frequencies for; §8.3, grading a real mechanism, has its first instances — the program's cyclic holarchies with spectral gates are overwhelmingly *logically* contextual, strongly so only when the gates are exact and the geometry frustrated.

***Gluing the Gates*.** Claim 4.3's affine hypothesis is discharged in practice. The obstruction that needs no affineness agrees with Claim 4.3 on the affine specimen (§3) and computes on the spectral one (§§4–5). The caution that paper's v0.2 added — detector, not certificate — is now the measured behaviour, and the design implication survives: a projection defined as a *section* rather than an aggregate is compositional by construction, and the invariant is what a designer runs on the aggregate case to find out whether it happens to glue anyway.

**The holarchies of the corpus.** *The Budget Across Levels* priced the program's nested complex with a residual gate at every edge; the gate scenario of that mechanism has 371 contexts and a continuous state space, and this instrument does not reach it. What the sweep says about it is indirect: a cycle of holons with a residual gate at every interface is a cycle with no open gate, which is the regime in which every strongly contextual model is seen. The reading is *section-shaped*, in *Gluing the Gates*' sense, and section-shaped readings are the ones the invariant serves.

**Conjecture R, a ninth time.** *No Global Section* imported Čech cohomology to pass a non-abelian gluing problem into an abelian one. The difficulty relocated exactly as the conjecture predicts: the free module forgets that a sheaf of sets does not allow linear combinations of sections, and every miss in §5 is a formal family with a negative coefficient that the sheaf of sets would refuse. What the formalism does not supply is the sign — and Theorem 6.3 says exactly where the sign is lost: at a reversal, through a relation whose components are not rectangles.

---

## 8. What Is Declined

**That the construction is new.** It is [2]'s, and the misses are [2]'s and [4]'s. The framework's export to non-physical settings is [6–9]. What is claimed is its application to gate scenarios and what came back.

**That the affine hypothesis was needed.** *Gluing the Gates* was right to hedge Claim 4.3 and *No Global Section* right to route around it; this paper only shows the route is passable. Nothing here says the affine-case H¹ and the support-presheaf H¹ coincide in general.

**~~That the run-of-open-gates rule is a theorem.~~ Struck in v0.2: it was not a rule, and the theorem that replaces it (§6) is not the same statement.** What is declined now is that Theorem 6.3 is unanticipated — Carù's ±1 path reading of a compatible family [5] is its picture, and Mansfield's chain result [15] its special case — and that it reaches non-cyclic covers. Its proof uses that consecutive contexts share one measurement and non-consecutive ones nothing, so that compatibility is conservation at a node; a cover with three contexts through one measurement, or two contexts sharing two, is a different system, and the flow argument does not apply as written.

**That the instrument reaches the program's mechanism.** It enumerates. The seed-7 complex with residual gates has 371 contexts and continuous stalks, and a Čech system on it is not a computation this module can do. Carù's refinement [5], complete for cyclic covers, is the right next tool for the cycles and not for the complex.

**That ℤ = ℚ is a finding.** It is Corollary 6.4: on a cyclic cover the obstruction is ring-independent. It was predicted the other way and recorded as missed, and the theorem is the correction.

**That the probabilistic grade is meaningless for mechanisms.** It is unavailable to a gate *model*. A mechanism observed over many epochs has frequencies, and a designer who chose to score them would recover the third grade and with it *No Global Section* §8.2's question. That is a different object from the gate model and this paper does not build it.

**That contextuality is a resource.** *No Global Section* §6 is untouched. Nothing here makes a contextuality-derived projection expensive to counterfeit, and §6.1 of that paper already said why it would probably not be.

---

## 9. Open Problems

**9.1. The refinement on the cycles.** Carù's iterated joint-model invariant [5] is complete for chordless cyclic covers. On those covers Proposition 6.5 answers extension outright by a directed search, so the refinement's interest there is what it costs: how many iterations of joining adjacent sections it takes to turn an undirected path into a directed one, on the program's scenarios, and whether that number is the length of the longest run of tolerance gates in a chain.

**9.2. ~~The rule, stated.~~ Stated and proved on cyclic covers — §6, this version.** The residue is the non-cyclic case: whether a cover in which contexts overlap in more than one measurement, or a measurement lies in more than two contexts, has an analogue of Theorem 6.3 — conservation on a hypergraph rather than a graph — and whether rectangularity is still the criterion. The design rule on cycles is already usable: *no tolerance gate in any chain*, which is to say every gate exact or open.

**9.3. The mechanism itself.** A gate scenario for the seed-7 complex with residual gates, on a discretised state space, and a solver that does not enumerate. The prediction from §5 is that it is seen wherever it is contextual, since it has no open gates; that prediction is worth the computation.

**9.4. Frequencies.** A mechanism scored over epochs has frequencies; whether a designer should compute the probabilistic grade on them, and what a global distribution over admissible states would mean for a mechanism that is never in two states at once, is *No Global Section* §8.2's residue.

**9.5. Contextuality and the verifiability boundary.** *No Global Section* §8.5 and *Gluing the Gates* §8.4, unchanged: whether the projections that resist intrinsic verification are the ones whose gate scenarios are contextual. The instrument can now grade a gate scenario; it cannot yet grade a projection.

---

## References

[1] S. Abramsky, A. Brandenburger. *The Sheaf-Theoretic Structure of Non-Locality and Contextuality.* New Journal of Physics 13, 113036, 2011. arXiv:1102.0264.

[2] S. Abramsky, S. Mansfield, R. S. Barbosa. *The Cohomology of Non-Locality and Contextuality.* QPL 2011, EPTCS 95, 1–14, 2012. arXiv:1111.3620.

[3] S. Abramsky, R. S. Barbosa, K. Kishida, R. Lal, S. Mansfield. *Contextuality, Cohomology and Paradox.* CSL 2015, LIPIcs 41. arXiv:1502.03097.

[4] G. Carù. *On the Cohomology of Contextuality.* QPL 2016, EPTCS 236, 21–39, 2017. arXiv:1701.00656.

[5] G. Carù. *Towards a Complete Cohomology Invariant for Non-Locality and Contextuality.* arXiv:1807.04203, 2018.

[6] S. Abramsky. *Relational Databases and Bell's Theorem.* In In Search of Elegance in the Theory and Practice of Computation, Springer LNCS 8000, 13–35, 2013. arXiv:1208.6416.

[7] S. Abramsky, G. Gottlob, P. G. Kolaitis. *Robust Constraint Satisfaction and Local Hidden Variables in Quantum Mechanics.* IJCAI 2013, 440–446.

[8] W. Zeng, P. Zahn. *Contextuality and the Weak Axiom in the Theory of Choice.* Quantum Interaction 2015, Springer LNCS 9535, 2016. arXiv:1512.02668.

[9] A. Ó Conghaile. *Cohomology in Constraint Satisfaction and Structure Isomorphism.* MFCS 2022, LIPIcs 241. arXiv:2206.15253.

[10] S. Felber, B. Hummes Flores, H. Rincon Galeana. *A Sheaf-Theoretic Characterization of Tasks in Distributed Systems.* arXiv:2503.02556, 2025.

[11] J. Hansen, R. Ghrist. *Opinion Dynamics on Discourse Sheaves.* SIAM Journal on Applied Mathematics 81(5), 2033–2060, 2021. arXiv:2005.12798.

[12] M. P. Santos, B. Amaral. *On Possibilistic Conditions to Contextuality and Nonlocality.* Quantum 5, 515, 2021. arXiv:2011.04111.

[13] G. Carù. *Logical and Topological Contextuality in Quantum Mechanics and Beyond.* DPhil thesis, University of Oxford, 2019.

[14] S. B. Montanhano. *Characterization of Contextuality with Semi-Module Čech Cohomology and Its Relation with Cohomology of Effect Algebras.* arXiv:2104.11411, 2021.

[15] S. Mansfield. *The Mathematical Structure of Non-Locality and Contextuality.* DPhil thesis, University of Oxford, 2013.

Propositions verified and measurements reproducible from `code/contextuality.py`, which imports nothing from the other modules: the models are finite, the arithmetic is exact, and the truth is enumerated.
