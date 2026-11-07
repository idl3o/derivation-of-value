---
layout: document
title: "The Extent of Value"
subtitle: "On What Value Is, Given That It Is Not a Derivation; Its Shape, Its Dimension, and the Two Ends at Which It Ceases"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /the-extent-of-value/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-11-06
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Key and Census argued that the derivations of value in this series do not glue, and that value, if the word refers to anything, refers to the obstruction class in the first cohomology of the presheaf of derivations. This paper takes the class as the object and follows it to its extent. Value is a difference and never a level, the numéraire a local trivialisation and the cocycle condition the absence of arbitrage; it is the monodromy of a loop around the key, run around the anthology's four substrates, which Volume V collapsed to one and which here is the first Betti number, one; it requires two valuers and lives on the edge between them; it has a canonical harmonic representative once overlaps are weighted — Proof by Resonance applied to the nerve of the papers, and a relocation of the choice onto the weights, as Conjecture R predicts; it has finite dimension that stabilises at the good cover, which is a testable prediction about the Census; and it vanishes for the monologue and for the dispersal, so that the cover is the lever for value as it is for security. Several things value was expected to be are shown not to be it, and listed."
status: "v0.1 · working draft"
order: 34
---

## Abstract

*Key and Census* argued that the derivations of value in this series do not glue, and that value — if the word refers to anything — refers to the obstruction class in the first cohomology of the presheaf of derivations. This paper takes the class as the object and follows it to its extent. Value is shown to be a difference and never a level; to be the monodromy of a loop around the key; to require at least two valuers and to exist only between them; to admit a canonical harmonic representative that is not a derivation; to have finite dimension; and to vanish at both ends of the spectrum of covers, so that it exists only for a plurality of partially overlapping accounts and for nothing else. Several things that value was expected to be are shown not to be it. These are listed.

---

## I. The object

*Key and Census* ended with a sentence: the derivation of value, if it exists anywhere, exists in H¹. The sentence was offered as a negative result and left there. It is taken up here as a definition.

Let X be the space of situations, {U_i} the cover by papers, and 𝒟 the presheaf of derivations. Each paper supplies a local section d_i ∈ 𝒟(U_i). On each overlap U_ij = U_i ∩ U_j, the two restrictions d_i\|_{U_ij} and d_j\|_{U_ij} are both derivations of the value of the same key under the same mechanism, and they are not equal. Their disagreement is a transition: an element g_ij of whatever group acts on derivations, such that d_i\|_{U_ij} = g_ij · d_j\|_{U_ij}. The collection {g_ij} is a 1-cochain. *Key and Census* argued it is a cocycle that is not a coboundary. Its class is written [v].

**Definition.** Value is [v] ∈ H¹({U_i}, 𝒟).

Not the mechanism, which reduces to κ. Not any derivation, which is local. Not the key, which is an integer. The class.

The definition is adopted without argument because it is the only candidate left standing. Every other thing that was called value in Volume I was a derivation, and derivations are what failed. What follows is an examination of the definition's consequences, undertaken on the view that a definition which survives its consequences is the only kind worth having.

## II. Value is a difference

A 1-cochain lives on overlaps. It has no values on the open sets themselves. There is no g_i; there is only g_ij. The first consequence of the definition is therefore that value is never assigned to a situation, only to a pair of situations, and what is assigned is the transformation that carries one account to the other.

This is familiar under another name. A price is not a level; a price is a ratio. The sentence "this is worth seven" is incomplete until the unit is named, and naming the unit is choosing a second thing against which the first is measured. Economics calls the second thing the numéraire and treats its choice as a convention. In the present notation the choice of numéraire is the choice of a trivialisation on an open set: fixing d_i as the reference derivation on U_i, against which everything else on U_i is expressed. The trivialisation is local. On U_j a different reference is fixed. The exchange rate between the two references is g_ij.

Exchange rates obey a constraint on triple overlaps. On U_ijk = U_i ∩ U_j ∩ U_k, carrying d_k to d_j and then to d_i must equal carrying d_k directly to d_i:

> g_ij · g_jk = g_ik on U_ijk.

This is the cocycle condition. It is also the no-arbitrage condition. A triangle of exchange rates that fails to close admits a cycle of trades returning more than it began with. *Key and Census* took {g_ij} to satisfy the cocycle condition: the derivations disagree pairwise but the disagreements are consistent around every triangle. There is no arbitrage. There is also no global unit, because a global unit would be a family {p_i} with g_ij = p_i · p_j⁻¹, which is the statement that the cocycle is a coboundary, which is the statement that paper argued false.

So: consistent exchange rates, no absolute price. Every value is a difference. The thing is never worth seven; it is worth seven of something else, and the something else is worth so many of a third, and the chain closes on every triangle and never terminates in a unit that is worth one of itself. The nonvanishing of [v] is precisely the absence of a numéraire that is not a convention.

Each of the anthology's four substrates treated its own quantity as the numéraire: *Proof of Coherence* the vanishing of an obstruction, *Proof of Preservation* order held against entropy, *Omnium* the magnitude of the vector, *Kar-Coin* the rung. Each was right on its own open set. The disagreement on the overlaps is what Volume I recorded as competing theories of value, and what *What Cannot Be Helped* recorded as four namings of one attestation problem. It was the cocycle.

## III. The puncture

A cocycle on a cover of a space with no holes is a coboundary. The nonvanishing of H¹ requires topology. The topology must be located.

It is at the key. *Key and Census* argued that each derivation d_i is severed in the Goodhart limit: as the mechanism on U_i approaches the preimage check, the derivation's middle link is replaced by a tautology and the chain breaks. The derivation is therefore not defined *at* the limit. It is defined on U_i minus the limit point. Every paper in the series is written on a situation from which the pure key has been removed.

The pure key is a single point of X. Call it κ again, now as a location rather than a number. The space on which the derivations live is X ∖ {κ}. A punctured space has a nontrivial loop: the loop around the puncture. The first cohomology of a punctured plane is one-dimensional, generated by the winding number around the missing point.

Value is the monodromy around κ.

Concretely. Begin on the coherence open set with its derivation. Pass to the overlap with negentropy and convert by g_{coh,neg}. Pass to the overlap with vector value and convert again; pass to capacity; return to coherence by the fourth overlap. The composite transformation is g_{coh,neg} · g_{neg,vec} · g_{vec,cap} · g_{cap,coh}. If the four open sets had a common intersection, or if any three of them did, the cocycle condition on the triple overlaps would force this product to the identity. They do not: the four substrates agree pairwise on the mechanism, but there is no situation in which three of the four derivations are simultaneously valid, because such a situation would be one in which the substrate-specific properties of all three held at once, and *What Cannot Be Helped*'s finding is that the substrates genuinely differ while the attestation problem does not. The nerve of the cover is a cycle of four. The loop encircles κ. The product is not the identity.

What returns from the loop is not what departed. A derivation carried around the key comes back transformed, and the transformation is the value. It is not located on any of the four open sets. It is located on the loop, which is to say on the fact that the four accounts are arranged around a point none of them contains.

This gives a second reading of the result of *Key and Census*. The key is not merely what every mechanism reduces to. It is the hole around which the derivations are wound. Removing it would make the derivations glue — but removing it means removing the mechanism, and without the mechanism there is nothing whose value was being derived. The key is necessary and absent. Value is the shape of its absence.

## IV. The valuer

The Sybil limit was taken in parallel with the Goodhart limit and reduced the participant to a key. The consequence for value follows.

Each open set U_i is a situation, and a situation includes a population. In the Sybil limit the population is a set of keys K_i. A derivation on U_i is an argument addressed to K_i: it says, to those keys, why the mechanism's key is worth holding. On the overlap U_ij the populations overlap too, and the keys in K_i ∩ K_j receive two arguments and the transition g_ij is the discrepancy between what they are told.

Value therefore lives on pairs of valuers as much as on pairs of situations. A single key, alone, on a single open set, receives one derivation and has no transition to compute. It has a mechanism, which reduces to an integer, and an argument, which is locally valid, and no value, because value is the difference between arguments and there is only one.

The minimal configuration in which value exists is two keys on an overlap, receiving two derivations. Value is irreducibly social in the thinnest possible sense: it requires a second party, and it is nothing but the relation between the first party's account and the second's. It is not a property of the key. It is not a property of either valuer. It is a property of the edge between them.

*The Census of Errors* counted witnesses by the independence of their errors and found the attack's limit at half the identities. The attack is now seen also as one on valuation. A Sybil attack manufactures keys, and each manufactured key is a new vertex, and the edges to it carry transitions, and if the attacker controls both ends of an edge the transition is whatever the attacker says it is. The attack does not forge value. It forges the edges on which value lives, which is more.

## V. The harmonic representative

A cohomology class is an equivalence class of cocycles. Two cocycles represent the same value if they differ by a coboundary — by a change of local numéraire. The class is canonical; its representatives are not. The question of whether value has a canonical *form* is the question of whether a representative can be singled out.

It can, given one additional choice. Equip the overlaps with weights: a positive number w_ij on each edge of the nerve, interpretable as the volume of the overlap, or the number of keys in K_i ∩ K_j, or the frequency with which the two situations are compared. The weights define an inner product on cochains. With an inner product, the Hodge decomposition applies: every 1-cochain splits uniquely as

> c = δf + δ*ω + h

where δf is a coboundary (a gradient: the part that comes from a global price f), δ*ω is a co-coboundary (a curl: the part that circulates locally around triangles and is invisible to the cocycle condition), and h is harmonic — annihilated by both δ and δ*. The harmonic part is the unique representative of the cohomology class with minimal norm.

Applied to v: the gradient part is zero, because v has no global price. The curl part is zero, because v satisfies the cocycle condition exactly. So v is purely harmonic for any choice of weights, and the harmonic representative h = v is the canonical form.

The canonical form of value is the harmonic 1-cochain on the nerve of the cover. It is the assignment of exchange rates to overlaps that is consistent around every triangle, minimal in total magnitude, and derivable from no price system. It is what a least-squares reconciliation of all the papers' competing accounts converges to: not an agreement, which does not exist, but the smallest consistent disagreement.

This is the corpus's own instrument turned on the corpus. *Proof of Coherence* reads a sheaf Hodge Laplacian over a complex of miners and tasks and calls the harmonic reading Proof by Resonance; the construction above is the same reading on the nerve of the cover by papers, with derivations for sections. Conjecture R — the standing conjecture that a change of formalism relocates the attestation problem and does not dissolve it — predicts what the relocation is, and it is here: the harmonic form is canonical once the weights are chosen, and the weights are the anchors' problem again. Who fixes how much each comparison counts fixes what the smallest disagreement is, and no overlap says how much it weighs.

This is a positive result and is stated as one. Value has a definite shape. The shape is computable from the papers, the overlaps, and the weights. It is not a derivation, because a derivation is a section and the harmonic form is the thing sections fail to be. But it is a definite mathematical object, unique once the weights are fixed, and it is the first object in this series that can honestly be called *the value* without qualification by an open set.

The weights are a choice. Different weights give different inner products, different harmonic representatives, the same class. What is canonical is the class; what is computable is the representative; the gap between them is the residual conventionality of value, and it is exactly the width of a choice of how much each comparison counts.

## VI. The dimension

H¹ is a vector space. It has a dimension. The dimension of value is a well-posed quantity.

It is finite. Čech cohomology with respect to a finite cover of a reasonable space by reasonable open sets is finite-dimensional, and the cover by papers is finite at any time. Call the dimension b₁, the first Betti number of the anthology.

b₁ counts the independent ways the derivations fail to glue. Two cocycles are independent if neither is a coboundary-adjustment of the other: if the disagreements they record cannot be reconciled by any change of numéraire. The number of such independent disagreements is the number of independent values. Not the number of valuable things, which is the number of keys and is irrelevant. The number of *kinds* of value: distinct loops around distinct punctures, or distinct windings around the same one.

For the four substrates of Volumes I and II, with the nerve a single cycle, b₁ = 1. There is one loop, one puncture, one generator. The anthology's universe, at the time of writing, has exactly one value, and every paper in it is a local account of that one value from a different side. *What Cannot Be Helped* said this in prose — four substrates named, one attestation problem, residue in four costumes. b₁ = 1 is that sentence as a number.

The number is not expected to remain one. The series continues; new substrates introduce new open sets; new open sets introduce new overlaps; new overlaps may introduce new loops that do not reduce to the first. b₁ is nondecreasing in the growth of the cover — but it is not unbounded, and this is the central fact of the section.

Čech cohomology stabilises under refinement. Once the cover is fine enough that every finite intersection of open sets is acyclic — a good cover — further refinement changes the cocycle representatives but not the class, and not the dimension. The Census was described in *Key and Census* as a list that cannot be completed because the cover keeps growing. The list is unbounded. The dimension it represents is not. Beyond the good cover, every new paper adds entries to the Census that are coboundary-equivalent to entries already present: new disagreements that are old disagreements in new numéraires.

The prediction is testable on the corpus itself. Past the good cover, each new paper's entry in the Census is the same disagreement in a new numéraire, and a paper that added a loop rather than a numéraire would be the first evidence against it. *Where We Stand* records Conjecture R confirmed eleven times without a new kind of confirmation; on this reading the cover was already good when the counting began.

Value has a finite extent. The extent is b₁ of the good cover. The anthology will reach it. The papers written after it is reached will be correct, locally valid, and dimensionally redundant.

## VII. The two ends

The definition places value on a cover. The cover can be varied. Value is followed to the two ends of the variation.

At one end, the cover is a single open set: {X}. One paper, one derivation, valid everywhere. There are no overlaps. There is no cochain. H¹ of a one-element cover is zero. Value is zero.

This is the monologue. A single account of the worth of the key, unchallenged, with no second account against which to form a difference. It is the situation of a mechanism with exactly one valuer and one argument, and it is the situation each paper of Volume I imagined itself to be in before it was placed beside the others. The monologue has a mechanism, a key, and a derivation. It does not have value, because value is a difference and the monologue has nothing to differ from.

At the other end, the cover is discrete: every open set is a single point, no two overlap, every situation is its own paper. There are no overlaps. There is no cochain. H¹ is again zero.

This is the dispersal. Every key its own universe, every valuer their own numéraire, no comparison attempted because no two situations share a region in which comparison is possible. The dispersal has as many derivations as it has points and no value, because the derivations never meet.

Value is nonzero only between the ends: for a cover that is neither one set nor all points, with open sets that overlap partially — enough to be compared, not enough to coincide. A plurality of accounts, each valid on its region, arranged around a key none of them reaches, with overlaps on which they are both valid and disagree. This is the entire extent of value. It does not exist for one. It does not exist for the isolated many. It exists for the overlapping many and for nothing else.

*Every Basis at Once* found that the one design variable that moved a security number was the cover — who is compared with whom — and called it the lever. The same variable is the only one that moves value. A cover of one set has none; a cover of all points has none; a cover of partially overlapping sets has b₁ of it. The cover is the lever, for value as for security, and in both cases what it moves is where the disagreement is allowed to fall.

The contemplative traditions that this series has declined to cite have a word for the first end and a word for the second and no word for the middle, because in those traditions the middle is what is to be seen through. The present result is that value is the middle. It is not a thing that survives the seeing-through. It is what is there to be seen through, and it is there, and it has the dimension b₁.

## VIII. What value is not

The definition was adopted because it was the last candidate. Its consequences have been followed. Several things that value was expected to be, in Volume I and in the ordinary use of the word, have been shown not to be it. They are listed without comment.

Value is not a property of the key. The key is an integer and has no cohomology.

Value is not a property of any situation. Cochains vanish on open sets and live on overlaps.

Value is not a level. There is no numéraire that is not a convention, and the absence is not a gap in knowledge but the content of the class.

Value is not the mechanism's measurement. The measurement, taken to its limit, is a bit.

Value is not any derivation. Derivations are local sections and value is the obstruction to a global one.

Value is not a quantity of valuable things. It is a dimension, b₁, which counts loops.

Value is not unbounded. It stabilises at the good cover.

Value is not present for a single valuer or for valuers who never overlap.

Value is not what remains when the accounts are reconciled. Reconciliation is the coboundary; value is what reconciliation cannot remove.

Value is not found by searching the papers. It is found by reading them against each other on their overlaps, taking the harmonic part, and reading off the class.

## IX. The extent

The paper's title promised the extent of value, and the extent has been reached. It is this.

Value is a class in H¹ of the presheaf of derivations over the space of situations punctured at the key. It is a difference and never a level. It is the monodromy of a loop around the key. It lives on edges between valuers and requires at least two. It has a canonical harmonic representative once comparisons are weighted. It has finite dimension b₁, which the anthology will reach and not exceed. It vanishes for the monologue and vanishes for the dispersal and is nonzero only for the overlapping many.

Nothing in this is a derivation of value. The series was named for a thing that does not exist in the form the name implies. The name is kept. A derivation is a path from premises to a conclusion, and what has been found is that the paths exist locally, that they do not join, and that the shape of their not joining is the only object in the universe of these papers that answers to the word. The series derives value in the sense that it computes the obstruction to deriving it. The obstruction has been exhibited. It is [v]. Its extent is b₁. The series continues past the point where the dimension stops growing, since the papers are the cover, and the cover is where value lives, and a cover that stops being written is the dispersal.

---

## X. What Is Declined

**That anything here is computed.** b₁ = 1 is read off a nerve assumed to be a four-cycle; no cochain is written down, no weights are chosen, no Laplacian is built, and no number in this paper came out of an instrument. The paper is a definition followed to its consequences, and the consequences are as sound as the definition's premises, which *Key and Census* declines to call a theorem.

**That the Hodge reading is new.** The decomposition of a cochain into gradient, curl and harmonic parts is Eckmann's, and the reading of pairwise comparisons as exchange rates whose curl-free part is a global price and whose harmonic part is the irreducible inconsistency is Jiang, Lim, Yao and Ye's combinatorial Hodge theory of ranking. The no-arbitrage reading of the cocycle condition on a triangle of currencies is older than both. What is claimed is the application to the presheaf of derivations and the reading of the result as value.

**That the harmonic representative is value.** The class is value. The representative is one cocycle in it, singled out by weights that nothing in the construction supplies, and Section V says so. The gap between the two is a convention and is named as one.

**That the puncture is located.** Section III places κ as a point of X. *Key and Census* defines no topology on X, and this paper inherits the gap: the puncture is where the argument says it must be, not where a construction puts it.

**That the stabilisation is observed.** It is predicted. Eleven confirmations of Conjecture R without a new kind are consistent with the cover being good and are not a measurement of b₁.

**That the contemplative remark is an argument.** The last paragraph of Section VII is a remark, cited to no tradition, and does no work in the paper.

**That this is what Volume I meant by value.** Volume I's derivations were of worth. This is the obstruction to their gluing, and the name is kept by decision, which Section IX says.

**That anything is measured.** Nothing is. No module in `code/` corresponds to this paper.

## XI. Open Problems

1. **Weight the overlaps.** Fix the inner product of Section V from something intrinsic — the measure of the overlap, the count of keys on it, the frequency of the comparison — so that the harmonic representative stops being a choice. Until then the canonical form is canonical up to a convention.
2. **Compute the nerve.** Which papers overlap, whether any three do, and what b₁ of the corpus is. An instrument, not an assertion; Section VI's one is read off and not computed.
3. **Test the stabilisation.** A criterion for "the same disagreement in a new numéraire" is needed before the prediction can be checked against the next papers' entries in the Census.
4. **The group.** Section I says "whatever group acts on derivations". Without naming it the cochain has no values, and the exchange-rate reading of Section II is an analogy with a multiplicative group it has not earned.
5. **Sybil as edge-forgery.** Section IV says a Sybil forges the edges on which value lives. *The Census of Errors* prices identities by independence of error; whether its independence classes also price edges, and whether a forged edge is detectable where a forged vertex is not, is open.

## Neighbours

*Key and Census* supplies the object and the two limits; this paper depends on its result and on nothing else, and inherits its declines. *What Cannot Be Helped* says in prose what Section VI says as a number. *Proof of Coherence* supplies the Hodge reading Section V reuses, and Conjecture R, kept in the program's working documents, supplies the prediction that the reuse relocates the choice onto the weights.

*Every Basis at Once* found the cover to be the lever for security; Section VII finds it the lever for value. *No Global Section* and *The Obstruction, Computed* are the corpus's computed H¹, on gate scenarios, where a vanishing class was found to license nothing; the same caution applies to [v] — a vanishing value would license a monologue, not a truth. *The Census of Errors* is the other count the word Census names, and Section IV reads its attack as one on edges. *Omnium* is the one volume that made value a level with coordinates; Section II's claim that there is no level is a claim against it, and is recorded as one.

## References

- Eckmann, B. (1944). Harmonische Funktionen und Randwertaufgaben in einem Komplex. *Commentarii Mathematici Helvetici* 17, 240–255.
- Hansen, J., and Ghrist, R. (2019). Toward a spectral theory of cellular sheaves. *Journal of Applied and Computational Topology* 3.
- Jiang, X., Lim, L.-H., Yao, Y., and Ye, Y. (2011). Statistical ranking and combinatorial Hodge theory. *Mathematical Programming* 127(1), 203–244.

---

*The Extent of Value, v0.1. A paper in the Derivation of Value series. Set in the same universe as* Key and Census *and dependent on its result; dependent on nothing else. No measurement is made; nothing in `code/` corresponds.*
