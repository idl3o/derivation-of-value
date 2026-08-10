# The rebuild — charter and ledger

Working document. Not published to the site. Opened 2026-08-10.

This opens a fourth line, distinct from the harvest line (`research-program.md`,
which varies the imported formalism) and the service line (`service-reframe.md`,
which varies what the mechanism emits). **The rebuild varies nothing. It re-derives
what is already claimed, from the ground, and records what survives.**

The occasion is stated in `state-of-the-program.md` §7: the central mechanism has
been shown to contribute nothing to forgery resistance, the central parameter may
not be a scalar, and the program "should expect its next result to be a
subtraction too." A corpus in that state does not need another paper on top. It
needs its foundations walked again, slowly, by someone willing to find them
wrong. That is what this line is for — and it is also, explicitly, a pedagogical
line: the operator wants to *understand* each topic at the depth of being able to
re-derive it, not merely to have written it once.

---

## 1. What "rebuilt" means

Rebuilding is not revision. A revision pass improves the prose of a claim it
still trusts. A rebuild withdraws trust first and makes the claim earn it back.
A topic counts as **rebuilt** when all four of the following hold:

1. **Re-derived cold.** The core claim can be stated and derived in a fresh
   document without consulting the original — the original is opened only
   *afterwards*, for comparison. Where the re-derivation and the original
   disagree, the disagreement is the finding, whichever way it resolves.
2. **Reproduced.** Every measurement the topic cites runs from `code/` and
   returns the published figure. A figure that no longer reproduces is
   downgraded on the spot.
3. **Attacked.** At least one deliberate attempt to break the claim — a
   counterexample sought, a hypothesis relaxed, a calibration object built whose
   answer is known in advance. The instrument lesson from the state document
   applies: *build the specimen whose answer you already know, and point the
   instrument at it first.*
4. **Regraded.** The claim's entry in the proved / measured / refuted /
   conjectured ledger is confirmed or moved, with the reason recorded here.

Divergence is data. If the rebuild converges to the same corpus, the corpus has
passed a replication test it has never had. If it diverges, the program learns
which of its results were robust and which were artifacts of the path that first
produced them. Either outcome pays.

Two failure modes to refuse from the start. **The reverence pass** — walking the
corpus admiringly and changing nothing, the import-without-contact failure turned
inward. And **the demolition pass** — treating "ground up" as license to discard
what is actually established; the Sybil bounds are theorems and stay theorems
unless an error is exhibited.

---

## 2. The strata

The corpus is nineteen documents, but its logical structure is seven strata,
each resting on the ones below. The rebuild proceeds bottom-up where dependency
demands it and by interest where it does not — this is also a curriculum, and a
curriculum that ignores appetite gets abandoned.

### S0 · The operator

*Sources:* Vol I, home page. *Grade:* definitional — the one stratum that is not
a claim but a lens.

The move from staking contingent quantities to staking what they derive from;
borrowed versus derived. Everything else presumes it.

**Rebuild questions.** Can borrowed/derived be stated as a *definition* that
classifies an arbitrary mechanism without a judgment call — or is it a
sensibility rather than a predicate? What exactly does Vol I's "recursive"
critique of proof of stake establish, and does it prove too much (does any
staked quantity whatever, including negentropy, admit the same circle)?
`borrowed-again.md` found the migration "moves between structures, not from
structure to bulk" — does the operator survive being applied to itself, or is
derived-versus-borrowed itself a matter of degree?

### S1 · The mathematical substrate

*Sources:* Proof of Coherence, Onboarding, `complexes.py`. *Grade:* imported
mathematics — the risk is not falsity but misuse.

Simplicial complexes, sheaves on them, H⁰ and H¹, the sheaf Hodge Laplacian, the
spectral reading. The stratum where understanding is most likely to be
*apparent* rather than real, because the formalism can be operated without being
understood.

**Rebuild questions.** Derive by hand, on a complex small enough to see: what is
a sheaf on a simplicial complex, what does a global section *mean* in the
inference reading, why is H¹ = 0 the right statement of "coherent," and what is
the smallest complex on which H¹ ≠ 0 with every pairwise overlap agreeing?
(That last is the whole mechanism in miniature; if it cannot be produced from
scratch, S1 is not understood.) Then: what does the Hodge Laplacian's kernel
recover, and where precisely does C2 — tolerance below the spectral gap — enter
and why does the score break without it?

### S2 · The security quantities

*Sources:* Combination Proofs, The Multiplicity Freedom, Sign and Work,
`sybil_bound.py`, `trace_gap.py`, `temporal_iota.py`, `independence.py`.
*Grade:* mixed — the program's only theorems live here, next to its least
formalised quantity.

Four symbols carry the program: **ρ** (richness, measured as fractional spectral
dimension), **ι** (independence, unformalised, possibly not a scalar), **τ**
(trace gap, with two ceiling results), **Γ** (amplified fake-cost,
Γ = γ(1 + (K−1)ι)). Plus the Sybil theorems T1–T3 and the conditions C1–C3.

**Rebuild questions.** Re-prove T1–T3 from stated hypotheses alone; the proofs
are short and the exercise is finding which hypotheses are actually used —
compare against the three conditions the state document says they silently
carry. Re-derive both τ ceilings (Prop 5.1, Prop 5.2) and attack Prop 5.2's cost
model, which is open problem 7 and cheap. For ι: reproduce the temporal result
(ι(ker | persist) = 1.000, asymmetry 0.277) and confront the type question —
open problem 2, prior to formalisation — with more attack intensities on
machinery that already exists. The reordering finding (independent *and*
expensive to forge, and the two pull against each other) should be re-derived
from first principles: is the ι–τ tension a theorem-shaped fact or a
three-data-point coincidence?

### S3 · Anchors, closure, and the fiction space

*Sources:* Gauge-Fixing the Section Space, A Consistent Fiction,
`fiction_space.py`, C3. *Grade:* measured, with one uncomfortable result on top.

The four anchors; the fiction space of dimension d; structural coupling priced
at d scalars once; and the sharpest recent finding — the trace gap is bought
*entirely* by the anchors, the sheaf machinery contributing nothing to forgery
resistance.

**Rebuild questions.** Re-derive the fiction-space dimension by hand on a small
complex (it should equal the kernel dimension — check understanding by
predicting it before running the code). Re-read Gauge-Fixing knowing the
anchors-buy-everything result: does the paper's own architecture already imply
it, and was it visible in v0.1? State precisely the two purchases the state
document distinguishes — closing the fiction space versus opening a trace gap —
and verify they are independent (one anchor closes content-freedom and buys no
τ; which anchors buy τ and what do they *not* close?). If the coherence layer
buys no forgery resistance, state plainly what it does buy, and whether that
purchase justifies its complexity — this is open problem 5 approached from below.

### S4 · The substrates

*Sources:* Proof of Preservation, Omnium, Kar-Coin, What Cannot Be Helped, Sign
and Work §§1–3. *Grade:* essayistic derivations; the volumes.

Negentropy, the value-vector, civilizational capacity, residue. Each names
something to stake; each met the same wall (the attestation, not the substrate).

**Rebuild questions.** For each substrate, reconstruct the derivation *and* the
wall: state in one paragraph why the substrate is attractive and in one
paragraph exactly where its attestation fails. Landauer's asymmetry (energy
spent is certifiable; order made-here is not) should be re-derived carefully —
it is the physical foundation of the whole negentropy line and deserves a slow
pass through the actual thermodynamics. Omnium's five dimension kinds are a
measurement-theoretic claim made without the literature (P10's observation) —
the rebuild of Omnium should test the five kinds against Stevens/Krantz
admissible-transformation classes directly. Vol V's claim that the one
distinction has been derived six times: enumerate the six, and check they are
the same distinction rather than a family resemblance.

### S5 · Composition

*Sources:* Gluing the Gates, No Global Section, Coutility. *Grade:* one
conjecture load-bearing and untested (Conjecture 3.1 — open problem 1), one
claim (GtG 4.3), one proposition (Coutility 4.1).

Why mechanisms fail to nest; contextuality as the general form; open games and
the coutility reading.

**Rebuild questions.** Work one contextuality example end-to-end by hand (the
Abramsky–Brandenburger triangle) and then exhibit the gate-sheaf translation on
it — the translation is P1's load-bearing move and should be verified on the
smallest instance, not trusted from the paper. Open problem 1 lives here: the
distributional-presheaf transfer is the highest-leverage untested conjecture in
the corpus, and the rebuild of this stratum is the natural occasion to finally
test it. Re-derive Coutility Prop 4.1's counterexample and state crisply why
admissibility and equilibrium are different logical shapes.

### S6 · Durability

*Sources:* Borrowed Hardness, Borrowed Again. *Grade:* audit; one open question
with a possibly-negative answer worth having (unstructured delay functions).

**Rebuild questions.** Re-derive the Shor/Grover sorting (structured hardness
dissolves, unstructured hardness is taxed) at the level of actually
understanding *why* — period-finding needs the group structure; Grover is
provably optimal for black-box search — rather than at the level of citation.
Re-check the VDF fragility finding: is the temporal anchor still the program's
most quantum-exposed load-bearing piece, and has the literature moved on
unstructured delay since the audit? (BA §7.2.)

### S7 · The instruments

*Sources:* `code/` entire, the eleven self-corrections, the calibration-object
lesson. *Grade:* method.

Not a topic in the corpus but the stratum the rebuild itself depends on: the
discipline of instruments that can return impossible numbers, calibration
objects built before measurement, prior-art checks before novelty claims.

**Rebuild questions.** Reproduce every figure in `code/` from a clean
environment before anything else — this is the rebuild's own calibration and
should be session 1's first act. Read the eleven self-corrections as a set: they
are the program's actual epistemology and the rebuild inherits it wholesale.

---

## 3. Rules of the line

1. **Cold first.** Derive before rereading. The original is the answer key, not
   the textbook.
2. **The code is the referee.** Claims cite measurements; measurements run from
   `code/`; a rebuilt topic re-runs them.
3. **Prior-art rule inherited** (it has caught the program twice): before any
   rebuilt claim is called new or newly-sharpened, check whether it is
   established elsewhere.
4. **Questions are first-class output.** A session that produces a sharp
   question and no answer is a successful session; the question goes in the
   ledger. The operator's stated purpose for this line is understanding, and
   understanding is measured in the quality of the questions one becomes able
   to ask.
5. **Grades move in public.** Any regrade — up or down — is recorded in §5 with
   its reason, and `state-of-the-program.md` is the eventual beneficiary.
6. **The corpus stays live.** The rebuild happens beside the published papers,
   not instead of them; nothing is deleted or rewritten until a rebuilt topic
   demands it, and then per the archive convention (`_archive/<slug>/`).

---

## 4. Session protocol

Each rebuild session, in order:

1. Pick the topic — from §2, respecting dependencies, following appetite.
2. State the target claims from memory, in the ledger, before opening sources.
3. Derive / reproduce / attack, per §1's four conditions.
4. Compare against the original; record convergences and divergences.
5. Update the ledger (§5) and regrade anything that moved.
6. Queue the next session's topic and its opening questions.

A session need not complete a stratum; strata are weeks, not sittings.

---

## 5. Ledger

### Session 0 — 2026-08-10 — orientation, charter

Read the state of the program (2026-08-06), the harvest plan, Vol I's opening,
the code README. Wrote this charter. No claims regraded — nothing has been
rebuilt yet, and the ledger starts honest.

**Queued for session 1: S7 then S0.** First act: clean-environment reproduction
of every `code/` figure — the rebuild calibrating its own instrument before
pointing it at anything. Then the operator itself, cold: write the
borrowed/derived distinction as a definition and test it against the mechanisms
the corpus names, before rereading Vol I.

**Opening questions for session 1, recorded before any rereading:**

- Is "derived" a two-place or three-place predicate — derived *from what*, and
  does the answer bottom out anywhere, or is every substrate borrowed from one
  stratum further down? (Vol IV's coda suggests the program already suspects
  the regress is the point.)
- The proof-of-stake circle (the stake's value presumes the protocol it
  secures): does the negentropy substrate escape it, or does "order is valuable"
  also presume an institution with a half-life?
- What would it take for the operator to be *refuted* rather than merely
  unfruitful? A lens that cannot fail is a sensibility, and the program's own
  ethic demands the stronger reading if it is available.

---

## 6. Questions for the operator

Standing questions about the line itself, to be answered in conversation and
folded back into this charter:

1. **Convergence or divergence?** Is the rebuild a replication test of the
   existing corpus (success = same results, independently reached), or is it
   licensed to become a second edition that supersedes — and if divergences
   accumulate, which document wins?
2. **Is the site in scope?** "Ground up" could include the Jekyll build,
   typography, information architecture. This charter assumes the *content* is
   the rebuild's object and the site follows later; say so if the assumption is
   wrong.
3. **Publication posture.** Do rebuilt derivations become published documents
   (a parallel track on the site), stay in `_plan/`, or replace originals as
   they mature?
