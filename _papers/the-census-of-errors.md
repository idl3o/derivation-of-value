---
layout: document
title: "The Census of Errors"
subtitle: "Sybil-Asymptotic Mechanism Design"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /the-census-of-errors/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-10-03
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "A mechanism that pays witnesses without access to the truth must first decide what a witness is. The Sleeping Beauty camps disagree about the census and not the coin, and a mechanism that pays agreement is a thirder: it counts copies. A witness, for the purposes of payment, is an independence class of errors — the one thing a copy cannot manufacture without paying for it. Under the cluster-leave-out rule a copy and its original share one payment, collusion without signal earns nothing, concealment pays only until the tasks per epoch exceed the square of the copies per item, and a forged world is told from the true one up to exactly half the identities, past which the two are formally interchangeable and the mechanism has no further say. The Multiplicity Freedom proves the cap on the fleet; this paper builds the payment rule beneath it. Drafted 2026-10-03 and recovered from a chat log; the simulator is not in the repository and the tables stand as reported."
status: "v0.1 · working draft"
order: 32
---

<!-- Drafted 2026-10-03; recovered 2026-11-06 from the chat log of that session and conformed to house form on
     2026-11-07 (front matter, What Is Declined, Open Problems, Neighbours; symbols that clash with the corpus
     renamed; wide tables transposed). The simulator (clo_sim.py, e1.py–e5.py) was built in that session's
     sandbox and is not in code/. The argument is as drafted. -->

*A mechanism that pays witnesses without access to the truth must first decide what a witness is. This paper derives that decision. A witness, for the purposes of payment, is an independence class of errors. Under that definition, payment becomes Sybil-proof in the limit of observation, collusion without signal earns nothing, and a forged world can be told apart from the true one up to exactly half the identities. Past that point the two worlds are formally interchangeable, and the mechanism has no further say.*

---

## I. The Sleeper

A fair coin is tossed. On heads, the sleeper is woken once, on Monday. On tails, she is woken on Monday and again on Tuesday, and between the two wakings her memory of the first is removed. At each waking she reports a number q, her credence that the coin landed heads.

The debate over this problem has two settled camps (Elga 2000; Lewis 2001). One holds that q = ½, since the coin is fair and waking teaches her nothing she did not already know. The other holds that q = ⅓, since two of the three possible wakings follow tails. Both camps argue from the evidence. The evidence does not decide between them.

The wakings are indistinguishable from the inside. Whatever she reports on one waking she reports on all of them, so q is not an act but a policy (Piccione and Rubinstein 1997). A policy is evaluated by its consequences, and its consequences depend on how its outputs are scored.

Let her report be scored by any proper scoring rule, and let each tails-waking carry weight w relative to the single heads-waking. Under the logarithmic rule her expected score is

> ½ · log q + (w/2) · log(1 − q)

which is maximised at

> **q = 1 / (1 + w)**

The Brier rule gives the same optimum, as does every proper rule, because each elicits the probability of heads under the measure that weights tails by w. When every waking is scored, w = 2 and q = ⅓. When each world is scored once, either by averaging the tails-wakings or by scoring Monday alone, w = 1 and q = ½. Every value in the open interval (0, 1) is the correct credence for some choice of w.

The sleeper's credence is therefore not fixed by her evidence. It is fixed by her evidence together with a measure over centred worlds, which is to say a decision about what counts as one subject. The thirder counts observer-moments. The halfer counts worlds. Neither is mistaken about the coin. They disagree about the census.

The two tails-wakings are perfectly coherent with one another. They hold the same information, return the same report, and have nothing to disagree about. Their agreement adds no evidence, yet the thirder measure counts it twice. A mechanism that pays each node for agreeing with its neighbours inherits the thirder measure, and with it a preference for any hypothesis that has many copies of itself reporting. A tails-world is a world with a Sybil in it (Douceur 2002).

## II. The Agreement Machine

Let G be a graph of agents and F a cellular sheaf on G. Each agent v holds a stalk F(v), each overlap e holds a stalk F(e), and restriction maps F_{v⊴e} carry an agent's report into the language of each overlap (Hansen and Ghrist 2019). The true state θ is a global section. Each agent observes a noisy local section and returns a report r_v. On an edge e = (u, v), the coboundary is

> (δr)_e = F_{u⊴e}(r_u) − F_{v⊴e}(r_v)

A *coherence-only* mechanism pays each agent through a function of the residuals on its own edges, maximised where those residuals vanish. A representative example is R_v = −Σ_{e∋v} ‖(δr)_e‖². This is the reward *Proof of Coherence* pays, read at a single vertex.

**Theorem 1 (Collusion is dominant).** Let x be any element of H⁰(G; F) = ker δ. The profile r_v = x_v, chosen without reference to any signal, is a Nash equilibrium of every coherence-only mechanism. Each agent's response in it is a best response, and strictly so unless x_v lies in the kernel of every restriction map at v.

*Proof.* At r = x every residual is zero and every agent receives the maximum reward. If v alone deviates to r′_v, the residual on each of its edges becomes F_{v⊴e}(r′_v − x_v). This is nonzero unless r′_v − x_v is annihilated by every restriction at v, so the deviation lowers v's reward. ∎

**Corollary.** Under any noise, honest reports have nonzero residual almost surely. Every collusive section therefore pays each agent strictly more than the truth. When dim H⁰ ≥ 1, the empty equilibria form a continuum, and the honest profile is not among the best of them.

Agreement is not evidence of truth. A coherence-only mechanism does not merely fail to elicit the truth; it pays agents to abandon it. This is the peer-prediction impossibility (Jurca and Faltings 2009; Kong and Schoenebeck 2019) in cohomological form. A constant section has zero coboundary, and the coboundary is all the mechanism can see. The continuum of empty equilibria is what *A Consistent Fiction* calls the fiction space, the kernel of the sheaf Laplacian, of dimension d per component; the theorem says the mechanism pays most at every point of it.

The standard escape rewards correlation across tasks rather than agreement within one (Dasgupta and Ghosh 2013; Shnayder et al. 2016). Each agent answers many independent tasks. On a true overlap, payment is the agreement observed on the same task minus the agreement observed, through the same restriction maps, on different tasks.

**Theorem 2 (Signal-independent strategies earn nothing).** Under multi-task scoring, any strategy profile whose reports depend neither on the agents' signals nor on the identity of the task earns zero expected reward.

*Proof.* If reports ignore both signals and task identity, the joint distribution of reports on a matched pair equals that on a mismatched pair, since tasks are drawn independently and identically and the reports do not see them. The two terms cancel. ∎

The theorem carries a qualification that its usual statement leaves unstated. A coalition can derive a shared random value from the task's label, for instance by hashing it. The resulting reports are independent of every signal, yet they vary by task and agree within the coalition on each task. Multi-task scoring reads that pattern as information and pays for it. In the experiments of Section IV, a coalition of one-fifth of the agents playing this strategy receives 5.4% of the emission under multi-task scoring and holds no information at all. The escape from Theorem 1 is real, but it closes only the door that does not depend on the task.

## III. The Census

The cure for counting copies is to count something copies cannot multiply. A copy duplicates a report. It also duplicates the report's error. Two honest witnesses err independently. Two copies of one witness err together. The independence of errors is the one thing a Sybil cannot manufacture without paying for it.

**Definition.** A *witness*, for the purposes of payment, is an independence class of errors: a maximal set of reporters whose noises are mutually dependent and jointly independent of all other reporters' noises.

The natural alternatives fail, and the manner of their failure is instructive.

*The Shapley value rewards cloning.* Consider two agents v and u with information values V(v) = a, V(u) = b, V(vu) = c. Add an exact clone of v. The clones' combined Shapley share rises by

> (a + b − c) / 6

Information is submodular, so c ≤ a + b, and the gain is strictly positive whenever the two agents' information overlaps at all. The Shapley value is a thirder.

*Precision weighting rewards collusion.* If each agent's noise is estimated from its residuals and payment follows precision, clones and colluders show zero residual and receive infinite precision. This is Theorem 1 in a different coat.

*Leave-one-out payment breaks under complementary splitting.* Paying each agent V(N) − V(N∖v) defeats exact clones, each of whose marginal value is zero. But an attacker may split a signal s into c₁ = s + z and c₂ = s − z, where z is noise of its own manufacture. Each piece alone is nearly useless; together they recover s. Each piece's marginal value then approaches v's original marginal, and the attacker is paid nearly twice. Leave-one-out is the reward by marginal removal that *Proof of Coherence* adopts, and the complementary split is the copy-symmetry problem of that paper with the copies made to differ.

Two facts make the census possible. In the linear-Gaussian model, a report is r = Λθ + ε, where Λ carries the global section into the stalks with per-agent loadings λ_v. First, the coboundary sees only noise: δΛθ = 0, so on every overlap δr = δε, and the true state cancels. Second, covariance across tasks sees signal and noise together, but the sheaf constrains the signal's share. The report covariance decomposes as

> T = Λ Σ_θ Λᵀ + Σ

where the signal term Λ Σ_θ Λᵀ factors through H⁰, so it is low-rank and shaped by the restriction maps, and Σ is the noise covariance. Shared noise among clones, or among the pieces of a split signal, is in general not a global section, because it is inconsistent with what independent neighbours report. It falls into Σ as an off-diagonal block. The blocks of Σ are the independence classes. The census is a low-rank-plus-block-sparse decomposition (Chandrasekaran et al. 2011) in which the low-rank part is constrained by cohomology.

The *cluster-leave-out* mechanism (CLO) proceeds as follows.

1. Tasks are elicited many at a time, under commit-reveal, with placement of agents onto overlaps assigned by verifiable randomness rather than chosen.
2. The report covariance is decomposed. Each agent's loading on the global section is first gated by regression onto a robust per-task median consensus, which requires no estimate of the signal's scale. The signal scale is then anchored on pairs that pass the gate. Clusters are formed from the estimated noise correlations, and the anchor is recomputed on pairs drawn from different clusters only, since those pairs share no noise.
3. Each cluster K is modelled as one shared error component plus idiosyncratic noise: Σ_K = s_K·11ᵀ + Ψ_K.
4. The information of a coalition S is the Gaussian mutual information between its reports and the global section, V(S) = I(r_S; θ), computed from the loadings as λᵀΣ⁻¹λ per item.
5. Each cluster is paid π_K = V(N) − V(N∖K), divided equally among its members.

**Theorem 3 (Sybil-proofness).** Assume the independence classes are conditionally independent given θ and the decomposition is identified. No agent can increase its total payment by distributing its reports across any number of identities.

*Proof.* The pieces of a split either share noise, or do not, or some of each. If they share noise, they form a single cluster C, whose payment is V(N∖v ∪ C) − V(N∖v). Since C is a garbling of v's signal, data processing bounds this by V(N) − V(N∖v), the original payment. If the pieces are conditionally independent, each forms its own cluster. Information is submodular over conditionally independent clusters (Krause and Guestrin 2005), so the sum of their leave-out payments is bounded by the leave-out payment of C as a whole, which is bounded in turn by the original. Mixed splits combine the two cases. The complementary split c₁, c₂ = s ± z falls into the first, because the manufactured z appears as a correlated block. ∎

A copy and its original cannot be told apart. The symmetry between them is intrinsic to any reward that removes a contributor and measures the loss (cf. Yokoo, Sakurai and Matsubara 2004 on false-name bids). CLO does not break the symmetry. It makes the symmetry worthless: the copy and the original share one payment, and copying earns nothing.

The Sleeper is now settled operationally. Her two tails-wakings share one brain state and therefore one error. They form one independence class, and the census counts one subject. Had the two wakings erred independently, two subjects would have been scored, and the answer would have been ⅓.

## IV. The Ledger

The mechanisms were simulated on a coordinate sheaf: 300 items, 60 honest agents, each observing a random region of 25 items, so that each item has about five observers. Each task draws a fresh global section from a standard normal distribution. Honest noise and attacker noise both have standard deviation 0.5. A Sybil attacker is a single model whose error is shared by all m of its identities. Four mechanisms were compared under a fixed emission: coherence-only, multi-task (Dasgupta–Ghosh), naive leave-one-out with independent noise assumed, and CLO. The measure is the *overpayment factor*, the attacker's share of emission divided by its true informational share with the attacker counted as one source. Results average three seeds at 400 tasks per epoch unless stated. The simulator that produced every number in this section is not in the repository; the Companion says so, and the tables stand as reported on 2026-10-03.

### Identity count

| identities m | coherence-only | multi-task | naive leave-one-out | CLO |
|---|---|---|---|---|
| 1 | 1.02 | 1.03 | 0.99 | 0.99 |
| 2 | 1.10 | 1.11 | 1.05 | 0.97 |
| 4 | 1.21 | 1.19 | 1.11 | 0.97 |
| 8 | 1.40 | 1.30 | 1.21 | 0.98 |
| 16 | 1.70 | 1.49 | 1.40 | 0.98 |
| 32 | 2.38 | 1.92 | 1.87 | 0.99 |
| 64 | 3.45 | 2.74 | 2.64 | 1.00 |
| 128 | 4.35 | 3.57 | 3.47 | 1.00 |

*Overpayment under verifiable random placement.*

CLO holds at the true share through 128 identities, more than twice the honest population. Every other mechanism overpays in proportion to the count. Coherence-only is the worst of them, as Theorem 1 predicts.

When the attacker chooses its placement and stacks every identity on one region, the agreement mechanisms collapse. At 128 identities, coherence-only overpays 61.6 times and multi-task 60.0 times. Naive leave-one-out reaches 4.87. CLO holds at 0.99 through 32 identities, fails in one of three seeds at 64, and fails in all three at 128. The failure occurs where the attacker's share of a single item's observers exceeds about nine-tenths. There the signal anchor is captured: too few pairs remain that join an honest agent to anyone. Verifiable random placement holds each item's adversarial share near the global share, and this is why placement is a structural requirement of the mechanism and not a convenience.

### The first estimator

The first version of CLO assumed that every report loads on the global section with weight one. A coalition of constant reporters, holding a fifth of the identities, appeared to that estimator as a set of noiseless witnesses and received 87% of the emission. The task-seeded coalition of Section II received 25%. Two further defects were found in the same version. Unequal variance estimates within a near-singular cluster leaked the all-ones vector into the cluster's null directions and inflated its value by up to 1.6 times; the one-factor model of Section III removes this. And the signal anchor could not be made robust to clones and to non-loading reporters at once, since clones inflate the upper quantiles of item covariance while non-loading reporters deflate the lower ones. The loading gate removes this by separating the two tasks. The order of the final pipeline is not arbitrary: gate, anchor, cluster, re-anchor, factor.

### Collusion

| coalition of one-fifth of agents | coherence-only | multi-task | CLO |
|---|---|---|---|
| constant reports | 13.8% | 0.0% | 0.0% |
| task-seeded reports | 10.4% | 5.4% | 0.0% |

*Share of emission received by coalitions holding no information.*

### Concealment

An attacker facing CLO may add private noise of standard deviation η to each identity, lowering the correlation among its copies below the threshold at which they are joined into one class. The threshold is set by the precision with which noise correlation can be estimated. The standard deviation of the pairwise estimate was measured at 1.9/√T, and a threshold of seven standard deviations, c_th ≈ 13.3/√T, produced no false joining among honest agents. Concealment pays exactly when

> **μ · c_th(T) > 1**

where μ is the number of copies observing each item. Below the threshold the copies are recognised, and CLO pays their true marginal value, which concealment reduces. Above it, they are counted separately, but the noise required to cross it degrades every report they make.

| tasks per epoch T | best simulated attack | analytic upper bound |
|---|---|---|
| 400 | 3.99 | 5.83 |
| 1,600 | 3.16 | 3.77 |
| 6,400 | 1.55 | 2.27 |
| 25,600 | — | 1.28 |
| 102,400 | — | 0.69 |

*Maximum gain from concealment, sixteen copies per item, attacker-chosen placement.*

The bound crosses break-even at T ≈ (13.3μ)², about 45,000 tasks for μ = 16. Payment is Sybil-proof in the limit of observation, at a stated cost: the tasks per epoch must grow with the square of the number of copies per item. Random placement keeps μ = mk/D small, and a detector that estimates correlation from coboundary residuals, where the global section cancels, would lower the constant.

## V. The Two Worlds

The last question is not who is paid but what is believed. A coalition of forgers reports a fabricated story b, and adds independent noise to each identity so that the coalition does not appear as a single class. The forgery succeeds on an item when the mechanism's estimate of the global section agrees more closely with b than with θ.

**Theorem 4 (The unseen subspace).** A coalition K can introduce an undetectable forgery that varies by task if and only if there exists a nonzero cochain b supported on K with δb = 0, that is, a section that vanishes on the coalition's boundary.

Every other forgery leaves residual covariance with honest neighbours. The forgers then fall into a noise block with no signal covariance toward the honest agents and receive no information value. Two consequences follow. A reporter's private dimensions, the directions of its stalk that lie in the kernel of every restriction map at v, can be forged by that reporter alone; the payable stalk is the quotient F(v) / ⋂ker F_{v⊴e}, and a mechanism pays only for what neighbours can see. And the smallest forging coalition is governed by how large the space of global sections is relative to the cochains.

The coordinate sheaf is the worst case. Each item is its own direction of H⁰, so the smallest coalition able to forge an item is that item's set of observers. In a second family, the global section is constrained to a low-dimensional subspace: θ = Gz with z of rank ten across 300 items, so that items are bound to one another by consistency. The forgers either lie item by item, or tell a lie that is itself a global section, b = Gz′.

| forger share of identities | coordinate sheaf | low-rank, lie by item | low-rank, consistent lie |
|---|---|---|---|
| 5% | 0.010 | 0 | 0 |
| 10% | 0.023 | 0 | 0 |
| 20% | 0.083 | 0 | 0 |
| 30% | 0.147 | 0 | 0 |
| 40% | 0.337 | 0 | 0 |
| 45% | 0.437 | 0 | 0.010 |
| 50% | 0.570 | 0 | 1 |
| 55% | 0.690 | 0 | 1 |
| 60% | 0.823 | 0 | 1 |

*Fraction of items on which the forged story prevails.*

On the coordinate sheaf, corruption begins at the smallest coalition and grows smoothly. Where H⁰ is small, a lie that is not itself a global section never prevails, even at three-fifths of the identities; it fails to fit the structure and is discarded as error. A lie that is a global section prevails nowhere up to forty-five percent and everywhere at fifty. The smallest forging coalition is half the network, which is linear in its size, as the design requires. The transition is complete and it is silent.

The reason is the Sleeper's, enlarged. Past half the identities there are two consistent worlds. Under the hypothesis that b is the truth, the forgers are independent honest witnesses, each with its own idiosyncratic error, and the honest agents are a single correlated class sharing one common error, θ − b. Every statistic available to the mechanism is symmetric under exchanging the two. The census counts independent errors, and an adversary with more identities than the honest population can present more independent errors than the honest population has. No peer mechanism distinguishes the two worlds. Beyond the threshold there is no degradation to manage, only the substitution of one world for another.

What remains beyond it is the price of an identity: the resource floor of *The Multiplicity Freedom*, which that paper proves bounds the fleet at the adversary's budget over the cost of one gated identity, and which *Gauge-Fixing the Section Space* builds as a dissipation floor that prices the minting of identities and does nothing else. Cluster-leave-out makes copies unprofitable. Only the cost of identity prevents copies from becoming the majority. The two defences are not alternatives. The first holds in the limit of observation and the second holds at the boundary where observation ends.

## Coda

The Sleeper's question was what counts as one subject. The network's answer is an independence class of errors: two reporters who err together are one, and two who err apart are two. The answer is operational, and it is sufficient for payment. It is not sufficient for truth. Where enough witnesses err together in the same direction, their shared error is indistinguishable from the world, and the census, however exact, counts the wrong world correctly.

---

### Design rules

1. Pay independence classes, not nodes.
2. Assign placement by verifiable randomness; never let reporters choose their overlaps.
3. Hide task identifiers from reporters, and present each reporter its own transform of each task.
4. Choose task families whose answers are bound together, so that the space of global sections is small relative to the cochains.
5. Pay only for the quotient of each stalk that neighbours can see.
6. Budget tasks per epoch at T ≳ (cμ)².
7. Price identity. It is the only defence at half.

### What Is Declined

**That the measurements are reproducible from the repository.** They are not. The simulator and the five experiment scripts were built in the sandbox of the session that drafted this paper and were not recovered with it. Section IV's tables stand as reported on 2026-10-03, and nothing in `code/` recomputes them. The corpus's rule that a cited measurement is reproducible from `code/` is not met here, and the paper is admitted with the gap named rather than held back until it is closed; Open Problem 1 is the closing.

**That the model is general.** The results hold in a linear-Gaussian model with a single attacker, honest agents of equal precision, and loadings constant across items. The low-rank experiment assumes the structure G is known; in practice it is estimated, and an estimated G is a second place for a coalition to stand.

**That the extension to language-model outputs is made.** It requires replacing the Gaussian information measure with estimators of f-mutual information on embedding stalks, and that extension is unproven.

**That Theorem 3 proves the mechanism Sybil-proof.** It proves the payment rule Sybil-proof under two assumptions, that the independence classes are conditionally independent given θ and that the decomposition is identified. Identification is the whole of the difficulty — Section IV's first estimator was a failure of identification, and the concealment attack is an attack on it — and the theorem assumes it.

**That the concealment table bounds the attacker.** The "best simulated attack" column is a maximum over strategies that were written down, and a strategy nobody thought of gains more. The analytic bound is the statement; the simulated column is a floor under the attacker, not a ceiling over it. The corpus's rule for the trace gap, that a measured minimum over written-down forgeries errs toward safety, runs the other way here, and the table is read accordingly.

**That the alarm exists.** A rising second factor in the consensus structure is expected to precede the transition of Section V and to serve as an alarm. It is untested.

**That the cap is this paper's.** It is not. Cluster-leave-out makes copies unprofitable; it does not bound their number. The bound is *The Multiplicity Freedom*'s, and it is conditional on a resource floor whose height the weakest honest participant sets. This paper's contribution at the cap is to say where the cap takes over: at half.

**That half is a security result.** It is an impossibility. Past half the identities no statistic available to any peer mechanism distinguishes the two worlds, and the claim is not that the mechanism degrades gracefully there but that it does not degrade at all — it substitutes one world for another, silently.

### Open Problems

1. **Rebuild the instrument.** Section III's pipeline — gate, anchor, cluster, re-anchor, factor — and Section IV's parameters are specified closely enough to rebuild in `code/`. Where the rebuilt instrument disagrees with a table here, the new number stands and the old one is printed beside it, as the corpus does.
2. **The f-information extension.** Replace Gaussian mutual information with an f-mutual-information estimator on embedding stalks, and determine whether Theorem 3's data-processing step survives the replacement.
3. **A coboundary detector.** The global section cancels in the coboundary, so noise correlation estimated from δr rather than from r would lower the constant in the concealment threshold. By how much, and whether the estimate is identified when the coalition sits on both ends of an edge, is open.
4. **The second factor as alarm.** Whether the consensus structure acquires a second factor before the transition of Section V, how far before, and whether a coalition can suppress it.
5. **The census and the boundary.** *One's Own Anchor* prices a coalition by the work-weighted fraction of its boundary edges, under commitment; this paper pays a coalition as one independence class. Both place the coalition's price where its noise is not shared with honest neighbours. Whether the independence class of errors and the boundary of the coalition are the same object, and whether the two accountings agree on the program's own complex, is the natural joint instrument.
6. **One bound at half.** *The Multiplicity Freedom*'s cap bounds the fleet by budget over the cost of one identity; Section V says the fleet becomes the world at half the identities. Joining the two gives the budget at which a resource floor stops protecting a given honest population, and no paper has written it down.

### Neighbours

*The Multiplicity Freedom* proves the cap: under duplication-boundedness and a resource floor, an adversary fields at most its budget over the cost of one gated identity, conditional on two conditions it names, participation and a tolerance below the spectral gap. The two subtitles share a phrase and divide the work: that paper proves the cap, and this one builds the payment rule beneath it, under which the fleet, whatever its size, is paid as one witness.

*Gauge-Fixing the Section Space* fixes the identity gauge with a unique encoding, on the observation that a section may be duplicated and that informational content does not individuate its bearer. Section III is the same observation turned into a count: content does not individuate, error does. Design rule 2 is that paper's beacon given a second job, and *Every Basis at Once* names the job — the beacon draws who is compared with whom, so that a coalition's placement is a random cut rather than its choice. Section IV's stacking attack, where the attacker chooses its region and the agreement mechanisms overpay sixty times, is what the redrawn cover is for.

*One's Own Anchor* commits before comparing, which is the commit-reveal of CLO's first step, and finds that an overlap published before commitment is a copy channel. Its whole-network fiction, scoring a residual of zero at zero cost, is Theorem 1 at the scale of the network; its coalition that fabricates the interior and derives only the boundary is Theorem 4's unseen subspace, a section supported on the coalition and vanishing where it meets honest data. *The Budget Across Levels* states the same criterion for a Sybil refinement — the adversary controls both sides of an interface — and finds it is not readable from residuals, which Theorem 4 says in the language of cochains.

*A Consistent Fiction* names the fiction space, the kernel of the sheaf Laplacian, as the set of distinct outcomes all scoring as perfectly coherent. Theorem 1's continuum of empty equilibria is that space, and the theorem adds that the mechanism pays most everywhere on it.

*Sign and Work* defines the trace gap τ and reads every measured forgery as a minimum over written-down strategies. The symbol is avoided here for that reason — the concealment noise is η — and the direction of error it establishes is applied in reverse to Section IV's concealment table.

*Proof of Coherence* is the agreement machine of Section II with its reward by marginal removal, and Section III's leave-one-out failure is that paper's copy-symmetry problem with the copies made to differ.

### Companion

This piece is the counterpart of *Combination Proofs*, which asks what a mechanism measures; this paper asks who. The simulator and the experiments that produced Section IV — `clo_sim.py` and `e1.py` through `e5.py` — were built in the sandbox of the session that drafted the paper on 2026-10-03 and are **not in `code/`**. Nothing in the repository reproduces Section IV; its tables are as reported on that date. Open Problem 1 is the rebuild.

### References

- Chandrasekaran, V., Sanghavi, S., Parrilo, P. A., and Willsky, A. S. (2011). Rank-sparsity incoherence for matrix decomposition. *SIAM Journal on Optimization* 21(2).
- Dasgupta, A., and Ghosh, A. (2013). Crowdsourced judgement elicitation with endogenous proficiency. *Proceedings of WWW*.
- Douceur, J. R. (2002). The Sybil attack. *Proceedings of IPTPS*.
- Elga, A. (2000). Self-locating belief and the Sleeping Beauty problem. *Analysis* 60(2).
- Hansen, J., and Ghrist, R. (2019). Toward a spectral theory of cellular sheaves. *Journal of Applied and Computational Topology* 3.
- Jurca, R., and Faltings, B. (2009). Mechanisms for making crowds truthful. *Journal of Artificial Intelligence Research* 34.
- Kong, Y., and Schoenebeck, G. (2019). An information theoretic framework for designing information elicitation mechanisms that reward truth-telling. *ACM Transactions on Economics and Computation* 7(1).
- Krause, A., and Guestrin, C. (2005). Near-optimal nonmyopic value of information in graphical models. *Proceedings of UAI*.
- Lewis, D. (2001). Sleeping Beauty: reply to Elga. *Analysis* 61(3).
- Piccione, M., and Rubinstein, A. (1997). On the interpretation of decision problems with imperfect recall. *Games and Economic Behavior* 20(1).
- Shnayder, V., Agarwal, A., Frongillo, R., and Parkes, D. C. (2016). Informed truthfulness in multi-task peer prediction. *Proceedings of ACM EC*.
- Yokoo, M., Sakurai, Y., and Matsubara, S. (2004). The effect of false-name bids in combinatorial auctions. *Games and Economic Behavior* 46(1).
