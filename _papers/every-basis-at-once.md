---
layout: document
title: "Every Basis at Once"
subtitle: "The World as Hidden Variable, and the Cover the Beacon Draws"
eyebrow: "An Anthology · Paper · v0.1"
permalink: /every-basis-at-once/
anthology: "Derivation of Value"
version: "v0.1"
date: 2026-09-07
license: "CC BY 4.0"
label: "Anthology · Paper"
blurb: "Choose the measurement basis after the participants commit, so that a fiction cannot be consistent in every basis: the quantum reading of the anchor problem, taken seriously. It divides in two. A committed participant is non-contextual by construction, so contextuality can appear only where commitment is absent, and there it is the signature of a copier tailoring its answers to each partner — real, computable, and dominated by commitment, which refuses it for free. What the basis buys is the cover. If the beacon draws who compares data with whom, a coalition's boundary is a random cut that grows with the coalition: the per-identity cost that a modular substrate had let fall to one is restored to ninety-six against honest's hundred and eighty-six, with the reading run to confirm it. The price is the substrate's spectral dimension, which leaves as the cover is redrawn, so expansion and richness are one purchase with opposite signs, and the design curve One's Own Anchor asked for is a table."
status: "v0.1 · working draft"
order: 26
---

## Abstract

The quantum reading of the anchor problem — choose the measurement basis after the participants commit, so that a fiction cannot be consistent in every basis — is taken seriously here and divides in two. The first half dissolves under its own premise. A committed section is one assignment, its restrictions to every context glue by construction, and so a committed participant is non-contextual whatever the basis; a fiction committed in advance fails only by being the wrong global section, which is the stale record *One's Own Anchor* already priced. Contextuality, local sections with no global one, can appear only where commitment is absent and a participant answers each context separately, and there it is the signature of the adaptive copier, which answers each partner with that partner's revealed data and so signals in the contextuality literature's exact sense. An exact self-consistency gate refuses it at no cost to honesty, whose answers come from one derivation; measured on the program's complex the honest spread is zero, the adaptive copier's is 0.27 and it is refused, and the copier that self-consistency leaves standing is the averaging one, self-consistent and below honest's residual, which is the copier that commitment was needed for. So contextuality is a resource against exactly the adversary commitment already defeats, and *No Global Section* §6's question closes: real, computable, dominated. The second half is what the basis buys, and it is the cover. If the beacon draws which participants compare data each epoch, degree-preservingly so that no one's number of overlaps changes, a block coalition's boundary is no longer the two to four cross-edges of the hierarchical complex but a random cut, |E|·2|C|(n−|C|)/(n(n−1)) in expectation, which grows with the coalition; measured, the boundary of the block of 128 goes from 2 to 191 against a formula value of 186, its per-identity native cost from 1 to 96 against honest's 186, and the residual reading run on the redrawn cover confirms that the stale coalition fails every epoch and the deriving one pays the cut. The boundary is linear in the fraction redrawn; the spectral gap is not, rising thirteenfold by one edge in eight and then flattening; and the spectral dimension *Requisite Richness* chose the complex for leaves as the cover is redrawn, from 1.6 to 2.6 with the fit degrading, so expansion and richness are one purchase with opposite signs and the design curve *One's Own Anchor* §9.4 asked for is a table. What is claimed is the division of the reading, the measurement of the copiers, the redrawn cover's cut and cost on the program's own substrate, and the curve; random assignment against collusion, no-signalling as a witness of communication, and contextuality as a resource are cited.

---

## 1. The Hidden Variable

The question was whether a quantum-style measurement could serve as the oracular basis for a mechanism: the beacon chooses the basis after the participants commit, and a fiction cannot be consistent in every basis. The corpus has the vocabulary to take the question literally. *No Global Section* identified composition failure with contextuality — local sections with no global section — and asked, in its §6, whether contextuality could be a resource for a mechanism rather than a pathology. *The Obstruction, Computed* and *The Ring and the Chord* made the identification computable. And the world model of *One's Own Anchor* supplies the missing piece of the analogy: honest participants derive their data from one shared external world, so every honest section restricts from one global assignment. The world is the hidden variable. In Bell's setting the hidden variable is what a classical system has and a quantum one lacks; here it is what an honest participant has and a fabricating coalition lacks.

Two things follow, and the second corrects the first.

**Commitment makes every participant non-contextual.** A committed section is one assignment. Whatever contexts are chosen afterwards, its restrictions to them glue, because they are restrictions of one thing. There is no basis in which a committed fiction is inconsistent with itself; a committed fiction fails only by being the wrong global assignment, which is to say stale against the world's innovation, and that is *One's Own Anchor* §6 with nothing added. Contextuality can appear only where commitment is absent and a participant answers each context separately. The participant who does that to advantage is the adaptive copier: shown each partner's data, it answers each partner with that partner's data, and so its answers on one prompt differ across partners. In the vocabulary of *The Ring and the Chord* that is signalling — the marginal on a prompt depends on the context — and it is refused by a self-consistency gate that costs honesty nothing, since honest answers come from one derivation. But §3 measures what that gate leaves standing: the averaging copier, one estimate from every revealed source, self-consistent, and below honest's residual. That is the copier *One's Own Anchor* §5 found passing, and the one its commitment regime was built against. Contextuality is a resource against the adversary commitment already defeats.

**What the basis buys is the cover.** The one thing a beacon can choose after commitment that a committed fiction cannot anticipate is *who is compared with whom*. On the hierarchical complex a block coalition's boundary is two to four edges whatever its size, and *One's Own Anchor* found the Sybil cap gone on that account. If the beacon draws the overlap graph each epoch, the coalition's boundary is a random cut, proportional to its size, and the cap returns. §4 measures it, §5 runs the reading on it, and §6 prices it in the currency the corpus already keeps: the spectral dimension the complex was chosen for.

Everything below is measured on the program's own substrate with the instruments of the previous papers, predictions stated in `code/every_basis.py` before running, two design errors in the instrument recorded.

---

## 2. Prior Art, and the Boundary of the Claim

Three of the paper's four constructs have antecedents and are presented as applications; the fourth does not.

**Commitment as hidden variable.** Fine [11] proved that a deterministic hidden-variable model, one joint distribution over every observable, and compatible joint distributions on every pair are the same thing; Proposition 3.1 is that theorem with a commitment in place of the hidden variable. Its cryptographic form is fully worked: Brakerski, Christiano, Mahadev, Vazirani and Vidick [12] have the prover commit before the verifier chooses the basis, and Kalai, Lombardi, Vaikuntanathan and Yang [13] compile any non-local game into a single-prover game by having encryption "simulate the effect of spatial separation", their soundness argument treating a classical prover who fixed its first answer as a local hidden variable. That contextuality is a resource is the physics literature's phrase — Howard, Wallman, Veitch and Emerson [1] and Raussendorf [2] — cited here only for the phrase, since §3 finds the mechanism-design version dominated.

**No-signalling as a witness of communication.** That communication manufactures non-local statistics classically is Toner and Bacon [14], one bit sufficing for the singlet; that a party with memory of the other wing's prior settings violates Bell inequalities by classical means is the memory loophole of Barrett, Collins, Hardy, Kent and Popescu [15], and the copier of §3, shown its partners' data, is that adversary. Bell-type and marginal-selectivity tests have been run on human data by Bruza et al. [16] and by the contextuality-by-default programme of Dzhafarov and Kujala [17], whose finding cuts the other way: human respondents signal by default. The reporters here are consistently connected for a reason that programme's subjects are not — they report the world, not themselves. Zeng and Zahn [4] carry the sheaf framework to revealed preference. No source found turns the no-signalling condition into a detector of copying between classical reporters of a shared world; the crowdsourcing consistency tests nearest to it are per-worker across tasks, not across pairings.

**The beacon-drawn cover.** That a coalition is priced by its cut is the attack-edge bound of SybilLimit [5], whose random routes walk on the substrate and so inherit its mixing time; that real substrates mix slowly is Mohaisen, Yun and Kim [18], and that community structure makes the cut cheap is Viswanath et al. [6] and the survey of Alvisi et al. [19] — the diagnosis this paper's remedy answers, stated in the negative. That random assignment makes an adversary's share of every group a sample of its global share is the security argument of Elastico, OmniLedger and RapidChain [7, 20] and of Buterin's account [8]; the cuckoo rule of Awerbuch and Scheideler [21] is its ancestor in distributed hash tables, and proof-of-personhood protocols pair participants at random for the same reason. The random-cut formula of Proposition 4.1 is the expander mixing lemma of Alon and Chung [22], cited rather than derived. Jecmen et al. [9] randomise reviewer assignment against collusion rings.

**Expansion against structure.** Watts and Strogatz [10] rewire a lattice and find its path length collapse long before its clustering does; Kleinberg [23] finds navigability on a knife-edge of locality-respecting randomness; Donetti, Neri and Muñoz [24] state outright that a large spectral gap and community structure exclude each other; Lazer and Friedman [25] and Fang, Lee and Schilling [26] find the organisational form of the same trade, efficient mixing collapsing the diversity that complex problems need. None uses spectral dimension as the second axis, which is the corpus's own currency from *Requisite Richness*.

What is claimed. That the quantum reading divides as §1 says, with commitment as hidden variable stated as an application of [11–13] (§3). That the adaptive copier signals, the self-consistency gate refuses it at no cost to honesty, and the averaging copier survives it — measured, and the detector without antecedent (§3). That a beacon-drawn, degree-preserving cover restores the per-identity cost on the program's own modular substrate to half of honest, at the mixing lemma's value, with the residual reading run to confirm it (§§4–5). And that the price is the spectral dimension, measured as a curve in the fraction redrawn (§6) — the two halves known separately, the coupling and the currency not found stated.

---

## 3. Commitment and Contextuality

`code/every_basis.py`, Part 1. The setting of *One's Own Anchor* §5 with shared prompts: a world G, each honest vertex deriving G with its own noise σ/√k, and a coalition C at whose boundary members meet honest partners. Here the coalition is the block of 128 on a beacon-drawn cover (§4), so that 60 of its 109 boundary members have more than one honest partner, which is the situation in which the copiers can differ.

**Proposition 3.1 (commitment).** A participant that commits one section before the contexts are drawn has, in every gate scenario over those contexts, a global section: its own. It is possibilistically non-contextual whatever the cover. *Fine's theorem [11] with a commitment as the hidden variable; the single-prover compilers of [12, 13] are its cryptographic form.* ∎

The proposition is trivial and it is the whole of the first half of the question. What remains is the uncommitted participant, who answers per context. Three strategies for a coalition member u with honest partners v₁, …, v_b, each partner's data revealed: *honest*, one derivation answered to everyone; *averaging*, the mean of the partners' revealed derivations answered to everyone; *adaptive*, each partner answered with that partner's own derivation. The **spread** is the largest RMS difference between u's answers on the same prompt to two partners; the **residual** is the boundary residual of *One's Own Anchor* §4 after the Procrustes fit.

| strategy | spread | boundary residual | honest residual | self-consistent |
|---|---|---|---|---|
| honest | **0.0000** | 0.2073 | 0.2073 | yes |
| averaging copier | **0.0000** | 0.0815 | 0.2073 | yes |
| adaptive copier | **0.2665** | 0.0000 | 0.2073 | **refused** |

**The adaptive copier signals.** Its answers on one prompt differ across partners by the noise between two honest derivations — 0.27, above the honest noise level because the largest of many pairs is taken — and a gate that demands the same answer to every partner refuses it, at no cost to honesty, whose spread is exactly zero because its answers are one derivation. In the empirical-model vocabulary the adaptive copier's marginal on a prompt depends on the context: it signals, and *The Ring and the Chord* §4 measured that signalling is what the cohomological invariant sees. Here no invariant is needed; the spread is the witness.

**The averaging copier does not.** One estimate from every revealed source, answered to everyone, is a global section and is self-consistent by construction; its residual is 0.08 against honest's 0.21, the below-honest subsidy of *One's Own Anchor* §5 with many sources. The self-consistency gate passes it. It is the copier that commitment was introduced to defeat, and it is untouched by any test of contextuality, because it is not contextual.

So *No Global Section* §6 closes as its own §6.1 predicted: a contextuality-derived reading exists, it is computable — the spread, or the obstruction — and it is expensive to counterfeit only for the adversary who tailors, which is the adversary who did not need to. Commitment defeats both copiers and costs one hash. Contextuality is a resource in the absence of commitment, and commitment is cheaper.

---

## 4. The Cover the Beacon Draws

`code/every_basis.py`, Part 2. What a beacon can choose after commitment, and a committed fiction cannot anticipate, is who is compared with whom. Each epoch the beacon redraws a fraction f of the complex's edges *degree-preservingly* — the chosen edges' endpoints are pooled, shuffled and re-paired, loops and duplicates repaired — so every participant keeps its number of overlaps, and only the identity of its partners changes. Honest cost per vertex is therefore unchanged at k·m·deg(v); what changes is the coalition's boundary.

**Proposition 4.1 (the random cut).** For a cover of |E| edges drawn uniformly at random on n vertices, the expected boundary of a coalition of size c is |E|·2c(n−c)/(n(n−1)); for a degree-preserving redraw of every edge the same expression holds to first order in the degree variance. It is proportional to c for c ≪ n and maximal at c = n/2. *Each edge has its endpoints on different sides with probability 2c(n−c)/(n(n−1)); the concentration around the mean is the expander mixing lemma of Alon and Chung [22].* ∎

On the specimen, n = 256 and |E| = 371, the formula gives 43.6, 81.5, 139.7 and 186.2 at |C| = 16, 32, 64 and 128. Measured, over eight beacon-drawn covers:

| f | ∂ at 16 | 32 | 64 | 128 | first blocks | per identity, 128 | λ₂ (giant) | components | d_s | R² |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 3.8 | 3.5 | 3.0 | 2.0 | 3/2/3/2 | **1.0** | 0.0038 | 1.0 | 1.68 | 0.996 |
| 1/8 | 8.8 | 13.0 | 19.1 | 22.8 | 8/12/20/23 | 11.4 | **0.049** | 1.0 | 2.06 | 0.982 |
| 1/4 | 13.8 | 23.1 | 38.2 | 49.0 | 14/24/38/49 | 24.5 | 0.083 | 1.2 | 2.28 | 0.977 |
| 1/2 | 23.6 | 42.0 | 72.0 | 90.2 | 23/40/71/90 | 45.1 | 0.107 | 1.0 | 2.41 | 0.980 |
| 1 | **43.6** | **80.9** | **139.2** | **191.0** | 42/78/136/191 | **95.5** | 0.102 | 1.6 | 2.56 | 0.975 |

Honest native cost per vertex is 186. Three things are in the table.

**The cap returns.** At f = 0 the row is *One's Own Anchor*'s: boundaries 3, 2, 3, 2 for the first blocks and per-identity cost falling to 1 at 128. At f = 1 the boundaries are the random-cut formula to within sampling, and the per-identity cost of the block of 128 is 95.5 against honest's 186 — half, where the fixed complex gave a hundred-and-eighty-sixth. Per identity the cost is 174, 162, 139 and 96 across the four sizes: bounded below by half of honest at every coalition size up to half the network, because a random cut is proportional to |C|(n−|C|). *The Multiplicity Freedom*'s cap, which §6 of *One's Own Anchor* found not to be a cap on a modular substrate, is a cap on a redrawn one.

**The boundary is linear in f; the gap is not.** The block of 128 has boundary 2, 23, 49, 90, 191 across the five rows — each redrawn edge contributes its random-cut probability and each kept edge its fixed one. The spectral gap of the largest component rises thirteenfold by f = 1/8, from 0.0038 to 0.049, and then by less than a factor of two over the remaining seven eighths. That is Watts and Strogatz's small world on the program's substrate: a few random overlaps buy most of the expansion. *Gauge-Fixing* §2's design target, maximise the gap, which the specimen failed at 0.0038, is met at f = 1/8 by redrawing one edge in eight — and the coalition's price at f = 1/8 is not the gap's story but the cut's: 23 edges for the block of 128, eleven per identity, a tenth of honest. The gap says a coalition is expensive; the cut says how expensive; and the two disagree about how much of the cover to redraw.

**The dimension leaves.** The spectral-dimension fit of *Requisite Richness* — the slope of the eigenvalue counting function over its intermediate window — gives 1.68 on the fixed complex with R² 0.996, the 1.61 that paper measured at larger sizes, and 2.06, 2.28, 2.41, 2.56 across the redrawn rows with R² falling to 0.975. At n = 1024 the fixed complex gives 1.59 with R² 0.999, one edge in eight redrawn gives 2.02, and the whole cover redrawn 2.58 with R² 0.974. The richness measure the substrate was chosen for is a property of its nesting, and the nesting is what the beacon undoes.

---

## 5. The Reading on the Redrawn Cover

`code/every_basis.py`, Part 3. The residual reading of *One's Own Anchor* §4, commit-before-compare, edge-local prompts, the world's innovation at δ = 3σ/√k, the coalition the block of 128, and the cover redrawn in full each epoch by the beacon. The coalition's stale strategy uses last epoch's record; its deriving strategy derives this epoch's boundary prompts.

| epoch | \|∂C_t\| | honest r | stale r | stale | derived | cost |
|---|---|---|---|---|---|---|
| 1 | 190 | 0.2026 | 0.4753 | refused | passes | 12,160 |
| 2 | 178 | 0.2045 | 0.4733 | refused | passes | 11,392 |
| 3 | 202 | 0.2044 | 0.4685 | refused | passes | 12,928 |
| 4 | 190 | 0.2017 | 0.4713 | refused | passes | 12,160 |
| 5 | 210 | 0.2042 | 0.4670 | refused | passes | 13,440 |
| 6 | 192 | 0.2066 | 0.4760 | refused | passes | 12,288 |
| 7 | 180 | 0.2069 | 0.4744 | refused | passes | 11,520 |

Evidencing share e(C) = 0.518; native cost per identity per epoch 95.9 against 186. The stale coalition fails on every epoch, as it did on the fixed complex above the step; the deriving coalition passes at the random cut's price; and the cut is a different cut each epoch, so no boundary member can be chosen in advance. The reading is unchanged. What the beacon changed is the geometry the reading is run on, and that is where the price lived.

---

## 6. What the Basis Bought

***No Global Section* §6, closed.** Contextuality is a resource for a mechanism in exactly the sense §6.1 feared: real, computable, and expensive to counterfeit only for an adversary who did not need to counterfeit it. The uncommitted adaptive copier is contextual and a self-consistency gate refuses it for nothing; the averaging copier and the stale coalition are global sections and only commitment prices them. The section's speculation is answered and the answer is that commitment dominates.

***The Budget Across Levels* §9.1 and *One's Own Anchor* §9.4, answered.** The beacon-drawn cover restores the per-identity cost to a floor of half of honest at every coalition size, and the design curve is §4's table. The price is stated in the corpus's own currency: spectral dimension, from 1.6 to 2.6, with the fit degrading. *Sign and Work* §5.4 found richness at the coupling knob paid in trace gap; here it is paid at the cover, and in the opposite direction — a substrate rich in nesting is a substrate whose coalitions are cheap, and a substrate whose coalitions are expensive has no nesting to be rich in.

***Gauge-Fixing* §2, met at a price.** The target the specimen failed is met by redrawing one edge in eight, and met by expansion of the cover rather than by densifying it, so *Sign and Work*'s trace-gap cost of density is not paid. What is paid is the semantic cost the model cannot show: the hierarchical complex was the world-models' nesting, and a prompt shared with a beacon-drawn stranger is one the stranger's model has no reason to hold. The instrument treats every prompt as a column of the world; a deployment would have to decide whether that is true.

**The quantum reading, settled.** The basis chosen after commitment does nothing against a committed fiction and everything to a coalition's geometry. The world is the hidden variable, and the mechanism's lever is not which basis the world is measured in but who is asked to agree about it.

**Conjecture R, an eleventh time.** The measurement-basis formalism relocated the difficulty from the fiction to the cover, and what it does not supply is the cover's meaning.

---

## 7. What Is Declined

**That Proposition 3.1 is a finding.** It is the definition of commitment read against the definition of a global section. It is stated because the question presumed otherwise.

**That the self-consistency gate is new.** Answering the same question the same way to every asker is the oldest consistency check there is; its statement as the no-signalling condition of an empirical model, against reporters of a shared world rather than the self-reporting subjects on whom that condition fails by default [17], is the contribution, and it is small.

**That the random-cut formula holds exactly for the degree-preserving redraw.** It holds for a uniformly random cover; the degree-preserving redraw agrees with it to within sampling on this specimen because the degrees are nearly homogeneous, and a substrate with hubs would need the configuration-model expression.

**That the cover can be redrawn in a deployment at no cost.** The model attaches prompts to edges and a world to columns, so a redrawn edge is a new prompt block anyone can derive. On the substrate the complex was built to model — nested world-models — a beacon-drawn overlap is a prompt the participant has no reason to hold, and that cost is named in §6 and not measured.

**That expansion is the right currency.** λ₂ is *Gauge-Fixing*'s target and it saturates by f = 1/8, while the coalition's cost keeps rising linearly to f = 1. The cut is the price; the gap is a bound on it, and a loose one.

**That the spectral dimension is lost rather than changed.** The fit still returns a slope at f = 1, with R² 0.975; what it returns is not the dimension of a nested substrate. Whether a redrawn cover has a richness in *Requisite Richness*'s sense at all, or only a number, is that paper's §8.1.

**That the instrument's first two passes were findings.** A cover redrawn as uniform random pairs disconnected at f = 1/4 and read λ₂ = 0; a swap-based rewiring left a third of the edges untouched at f = 1 and read two thirds of the cut. Both were design errors and are in the docstring.

---

## 8. Open Problems

**8.1. The semantic cost.** Model the nesting as meaning: a prompt's derivation cost depends on the deriver's distance from it in the hierarchy, so that a beacon-drawn overlap with a stranger costs more than one with a sibling. The curve of §4 would then have a second axis, honest cost, and a design optimum in f.

**8.2. Partial redraw as the design.** f = 1/8 buys most of the gap and a tenth of the cut. Whether there is an f at which the coalition's per-identity cost clears a target while the spectral dimension is still the substrate's — the fit still 0.98 at f = 1/8 — is a design problem with three numbers already on the table.

**8.3. The beacon's own cost.** A redrawn cover is a per-epoch assignment every participant must learn and derive against; the beacon's randomness is consumed as assignment as well as timing, which is *Gauge-Fixing* §4's beacon doing a second job, and *A Consistent Fiction* §8.5's separability question again.

**8.4. Self-consistency as a reading.** The spread is zero for honesty and positive for the adaptive copier, and commitment makes it unnecessary; but a substrate whose state is too large to commit could use the spread in commitment's place, at the cost of answering k contexts. What that trades against a hash is a budget question in *Independent and Expensive*'s currency.

**8.5. The world-model substrate.** Whether the hierarchical complex's nesting can be kept for derivation and the cover redrawn only for comparison — participants derive their own neighbourhood's prompts and are compared, by the beacon, with strangers who happen to hold the same prompts — is the design that would keep the richness and buy the cut, and it presumes the shared-prompt model in which the coalition's cost was 1/|C| regardless.

---

## References

[1] M. Howard, J. Wallman, V. Veitch, J. Emerson. *Contextuality Supplies the "Magic" for Quantum Computation.* Nature 510, 351–355, 2014.

[2] R. Raussendorf. *Contextuality in Measurement-Based Quantum Computation.* Physical Review A 88, 022322, 2013.

[3] J.-Å. Larsson. *Loopholes in Bell Inequality Tests of Local Realism.* Journal of Physics A 47, 424003, 2014.

[4] W. Zeng, P. Zahn. *Contextuality and the Weak Axiom in the Theory of Choice.* Quantum Interaction 2015, Springer LNCS 9535, 2016. arXiv:1512.02668.

[5] H. Yu, P. B. Gibbons, M. Kaminsky, F. Xiao. *SybilLimit: A Near-Optimal Social Network Defense against Sybil Attacks.* IEEE S&P 2008, 3–17.

[6] B. Viswanath, M. Mondal, A. Clement, P. Druschel, K. P. Gummadi, A. Mislove, A. Post. *Exploring the Design Space of Social Network-Based Sybil Defenses.* COMSNETS 2012.

[7] E. Kokoris-Kogias, P. Jovanovic, L. Gasser, N. Gailly, E. Syta, B. Ford. *OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding.* IEEE S&P 2018. ePrint 2017/406.

[8] V. Buterin. *Why Sharding Is Great: Demystifying the Technical Properties.* vitalik.eth.limo, 7 April 2021. Accessed 2026-09-07.

[9] S. Jecmen, H. Zhang, R. Liu, N. B. Shah, V. Conitzer, F. Fang. *Mitigating Manipulation in Peer Review via Randomized Reviewer Assignments.* NeurIPS 2020. arXiv:2006.16437.

[10] D. J. Watts, S. H. Strogatz. *Collective Dynamics of "Small-World" Networks.* Nature 393, 440–442, 1998.

[11] A. Fine. *Hidden Variables, Joint Probability, and the Bell Inequalities.* Physical Review Letters 48, 291–295, 1982.

[12] Z. Brakerski, P. Christiano, U. Mahadev, U. Vazirani, T. Vidick. *A Cryptographic Test of Quantumness and Certifiable Randomness from a Single Quantum Device.* FOCS 2018; Journal of the ACM 68(5), 2021. arXiv:1804.00640.

[13] Y. Kalai, A. Lombardi, V. Vaikuntanathan, L. Yang. *Quantum Advantage from Any Non-Local Game.* STOC 2023. arXiv:2203.15877.

[14] B. F. Toner, D. Bacon. *Communication Cost of Simulating Bell Correlations.* Physical Review Letters 91, 187904, 2003. arXiv:quant-ph/0304076.

[15] J. Barrett, D. Collins, L. Hardy, A. Kent, S. Popescu. *Quantum Nonlocality, Bell Inequalities, and the Memory Loophole.* Physical Review A 66, 042111, 2002. arXiv:quant-ph/0205016.

[16] P. D. Bruza, K. Kitto, B. Ramm, L. Sitbon. *A Probabilistic Framework for Analysing the Compositionality of Conceptual Combinations.* Journal of Mathematical Psychology 67, 26–38, 2015.

[17] E. N. Dzhafarov, J. V. Kujala. *Contextuality-by-Default 2.0: Systems with Binary Random Variables.* In Quantum Interaction 2016, Springer LNCS 10106, 2017. arXiv:1604.04799.

[18] A. Mohaisen, A. Yun, Y. Kim. *Measuring the Mixing Time of Social Graphs.* IMC 2010, 383–389.

[19] L. Alvisi, A. Clement, A. Epasto, S. Lattanzi, A. Panconesi. *SoK: The Evolution of Sybil Defense via Social Networks.* IEEE S&P 2013.

[20] M. Zamani, M. Movahedi, M. Raykova. *RapidChain: Scaling Blockchain via Full Sharding.* ACM CCS 2018.

[21] B. Awerbuch, C. Scheideler. *Towards a Scalable and Robust DHT.* SPAA 2006, 318–327; Theory of Computing Systems 45(2), 234–260, 2009.

[22] N. Alon, F. R. K. Chung. *Explicit Construction of Linear Sized Tolerant Networks.* Discrete Mathematics 72, 15–19, 1988.

[23] J. Kleinberg. *The Small-World Phenomenon: An Algorithmic Perspective.* STOC 2000, 163–170.

[24] L. Donetti, F. Neri, M. A. Muñoz. *Optimal Network Topologies: Expanders, Cages, Ramanujan Graphs, Entangled Networks and All That.* Journal of Statistical Mechanics, P08007, 2006. arXiv:cond-mat/0605565.

[25] D. Lazer, A. Friedman. *The Network Structure of Exploration and Exploitation.* Administrative Science Quarterly 52(4), 667–694, 2007.

[26] C. Fang, J. Lee, M. A. Schilling. *Balancing Exploration and Exploitation Through Structural Design: The Isolation of Subgroups and Organizational Learning.* Organization Science 21(3), 625–642, 2010.

Propositions verified and measurements reproducible from `code/every_basis.py`, which imports the world, the honest derivations, the residual reading and the coalition of `code/evidencing.py`, the derivation of `code/holarchy.py`, and the spectral-dimension estimator of `code/spectral_richness.py`, all unchanged.
