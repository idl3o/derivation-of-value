# The service line — opened 2026-08-06

Working document. Not published to the site.

A third line beside the anthology and the harvest line. Where the harvest line takes an
outside *formalism* and imports it, this varies something the corpus has never varied:
**what the mechanism emits.**

---

## 1. The reframe

> Instead of exchanging value, the system provides the most tuned-coherent messaging
> service.

Nineteen documents assume the mechanism *pays* for coherence. The output is a reward;
coherence must therefore be attested to a third party; attestation must be priced;
pricing is the attestation problem. That chain is the program.

Break the first link. If the mechanism **delivers** coherence as a service — routing,
admission, delivery priority, tuned per recipient — then coherence is not attested, it
is consumed. The recipient verifies by use.

**This is not a departure from the operator; it is the operator applied one level up.**
The spine is *derive the staked quantity instead of borrowing it*. A token is borrowed:
its value presupposes the mechanism working, which is the circularity *Gauge-Fixing* §6
declines proof-of-stake for and *A Consistent Fiction* diagnoses as closure. Delivery
priority is scarce natively. Deriving it from measured coherence stakes something the
substrate already produces.

Volume III is called *Admitted or Refused*. It has been an admission-control title for
nineteen documents.

### The scale claim

The largest instance is a **world sim** — a shared model, coherence scoped across the
whole network. The smallest is a **bitchat** — two parties, coherence scoped to the
pair. Same mechanism, recurring scale. This is the K–B axis of *Kar-Coin* made
operational: Kardashev is the infrared limit, Barrow the ultraviolet, and scope is the
dial between them. It is also the first object P7 (*The Same Move at Every Scale*,
renormalization) could be tested on — Volume IV's coda claims the operator recurs at
every layer and has never had an instance where the recurrence could be *measured*.

---

## 2. What the corpus already has that fits

Three of the program's negative results become affordances rather than obstacles.

**No global section.** *No Global Section* establishes contextuality as the general form
of composition failure. It bites because the mechanism demands a global coherent state
to score. **A per-recipient service does not.** A message need only cohere in its
context. That paper's §6 — contextuality as a *resource* rather than a pathology, marked
speculative — is where this reframe makes it concrete, and "tuned" is the word doing the
work.

**Interfaces are grown, not specified.** *Sign and Work* §6 proposes cultivating an
interface — fix the medium and the reading rule, let density find itself — and supplies
*Gluing the Gates* Conjecture 5.2 the mechanism it lacked. Routing topology is that
object. The proposal has had no instance until now.

**Coutility.** *Coutility* Claim 3.1 says a super-mechanism should gate on its
constituents' coutility — utility returned to the environment — rather than their
utility. A delivered service **is** coutility by type. That paper's §7.1 asks for a
Combination Proof exhibited as an open game, which is materially easier when the output
already has the right type.

---

## 3. What has been measured, 2026-08-06

`code/usage_coupling.py`.

### The coupling claim is refuted

The reframe's most attractive property looked like free structural coupling: recipients
who stop consuming are external signal, so usage supplies the contact *A Consistent
Fiction* prices at d scalars and *Gauge-Fixing*'s anchors are forbidden to give.

**It does not.** Satisfaction is maximised at *exactly* zero contact — a network with
nothing anchored serves every recipient what they already believe, scoring 1.0000 while
tracking nothing — and declines monotonically as contact is added.

| anchored | 0.00 | 0.01 | 0.03 | 0.08 | 0.15 | 1.00 |
|---|---|---|---|---|---|---|
| satisfaction | **1.0000** | 0.9924 | 0.9856 | 0.9881 | 0.9832 | 0.9278 |
| truth | −0.15 | +0.09 | +0.55 | +0.91 | +0.95 | +0.93 |

**And there is no barrier**, which is worse than a barrier. A valley would leave coupled
states locally stable once reached. A slope means the gradient points at closure from
*every* configuration, so every coupled state is under continuous pressure back.

**Truth is cheap and satisfaction pays for it anyway.** Truth saturates near 8% anchored
— +0.91 of the +0.95 available. That is the design point, and a satisfaction-scored
mechanism will never stop there because satisfaction keeps falling past it.

**What this refutes is the coupling claim, not the reframe.** A service mechanism need
not score usage. If it scores coherence and merely *delivers*, the coupling problem is
exactly what it was under the payment framing, and the reframe's case rests on §2's
three affordances instead.

### The recurrence is real, and has a direction

Cost of full contact, in satisfaction, against scope:

| scope | 2 (bitchat) | 4 | 16 | 64 | 240 (world sim) |
|---|---|---|---|---|---|
| cost | +0.1069 | +0.0896 | +0.0769 | +0.0735 | +0.0722 |

Same sign and order of magnitude across two orders of magnitude of scope. **First
evidence for Volume IV's coda**, and it carries something the coda does not: the cost of
contact with the world is *higher at small scale*. A bitchat pays more of its
satisfaction for truth than a world sim does. In P7's vocabulary that is a coupling
constant that **flows** with scale, which is exactly the shape renormalization wants and
the corpus has only ever asserted.

---

## 4. Papers this implies

### S1 · The service reframe — *planned*

**Thesis.** A mechanism that delivers coherence rather than paying for it stakes a
natively scarce quantity and escapes the token's circularity, and three of the program's
obstruction results become design affordances under it.

**Must contain**, or it is the harvest line's named failure mode with the import
stripped off: the refuted coupling claim, stated as prominently as the affordances. A
paper presenting §2 without §3 would be flattery.

**Declines.** That usage couples. That the attestation problem is dissolved — Conjecture
R predicts relocation, and the likely relocation is that "what counts as good delivery"
becomes the new proxy. Whether it relocates *usefully* is the paper's real question.

### S2 · The capture adversary — *planned, and probably prerequisite*

**Thesis.** Every bound the program owns is denominated in **extraction**. The Sybil
cap prices identities that collect reward; τ prices forging a trace *for payment*; ι
prices faking a projection *to be paid*. A service adversary wants none of that. It
wants **capture**: routing influence, amplification, suppression, priority. Sybil
identities buy reach rather than income, and none of the arithmetic transfers.

**Why it may be prerequisite.** S1's security section cannot be written without it. A
reframe whose adversary model is absent is a reframe whose security claims are vacuous,
and the corpus has spent nineteen documents earning the right not to do that.

**PRIOR-ART CHECK RUN 2026-08-06, AND IT KILLED TWO OF THE FOUR CLAIMS.** This is the
second time the rule has caught the program claiming an established result, after
*Gluing the Gates* and contextuality. Recorded rather than quietly absorbed.

Singh, Castro, Druschel & Rowstron, *Eclipse Attacks on Overlay Networks: Threats and
Defenses*, INFOCOM 2006 (~380 citations), states the intended claims 1 and 2 outright:

> "In an *Eclipse* attack, a set of malicious, colluding overlay nodes arranges for a
> correct node to peer only with members of the coalition. If successful, the attacker
> can mediate most or all communication to and from the victim."
>
> "Defenses against Sybil attacks **do not prevent** Eclipse attacks, because attackers
> may manipulate the overlay maintenance algorithm to mount an Eclipse attack."

That is *exactly* "Sybil bounds are extraction-shaped and do not bound capture." It has
been known for twenty years. The Kademlia literature adds the quantitative form —
eclipse succeeds with as few as **eight** strategically-placed nodes — which is the
"capture needs position, not budget" claim with a number the program does not have.

**Revised claims, after the check.**
1. ~~Extraction and capture are different adversary classes.~~ **Established** (Singh et
   al. 2006). Imported, cited, not claimed.
2. ~~The Sybil cap does not bound capture.~~ **Established.** The program's contribution
   is narrower and still worth making: *The Multiplicity Freedom*'s theorems are stated
   as if they bounded an adversary generally, and they bound one adversary class. That
   is a correction to this corpus, not a result about the world.
3. **τ has a capture analogue, and it is a different ratio.** Forging a trace to be
   *paid* is priced against earning; occupying a position to be *routed through* is
   priced against whatever the recipient would otherwise have received. Open, and the
   paper's likely real contribution.
4. **Do the trace-gap ceilings transfer?** They are results about a *reading*, and the
   reading changes under capture. Open.
5. **New, and the most promising.** Singh et al.'s defence is that nodes *anonymously
   audit each other's connectivity* — a structural check on the graph, which is what
   this program's machinery already is. **Is the eclipse condition a cohomological
   one?** If a coalition mediating all of a node's communication is detectable as an
   obstruction rather than by a degree audit, the sheaf earns its place in the service
   setting, and *Gluing the Gates*' claim that failures live at interfaces acquires a
   worked instance in a field that has been attacking the problem by other means.

**Further prior art still unchecked:** S/Kademlia's certified-ID approach, reputation
systems, adversarial IR. Check before drafting.

### P7 gains an object

*The Same Move at Every Scale* has been planned since the harvest line opened and has
never had a measurable instance. It has one now, with a coupling constant that flows.
This should move up the queue.

---

## 5. Open problems, ranked

1. **Does the reframe relocate the attestation problem usefully, or merely rename it?**
   The whole line turns on this. Conjecture R says relocation; the question is whether
   "what counts as good delivery" is a *better* place for the difficulty to sit than
   "what counts as attested coherence." Not obviously yes.
2. **The capture adversary.** S2. Prerequisite to any security claim in this line.
3. **Is there a delivery score that is not satisfaction?** §3 kills usage-as-coupling
   because satisfaction is maximised by closure. A score that rewards *coherent change*
   rather than agreement would evade it, and no formulation is on offer — the same gap
   *Proof of Coherence* v0.5 §4.5 names for temporal projections. **These are the same
   open problem in two settings**, which is worth noticing.
4. **Does scope compose?** If a bitchat and a world sim are the same mechanism at
   different scale, does a hierarchy of scopes glue? This is *Gluing the Gates*'
   question asked of the scale axis rather than the holarchy axis, and the answer is
   probably no by the same argument.
5. **Where does the 8% come from?** Truth saturates at roughly a twelfth of the
   population anchored. Whether that number is a property of the model's parameters or
   of something structural is unknown, and if structural it is the service line's
   analogue of "d scalars, at one vertex, once."

---

## 6. Standing risks

**The metaphor tax, in a new form.** "Messaging service" is a familiar object with a
large industry and a large literature. Entering it without contact — restating
distributed-systems folklore in sheaf vocabulary — is the failure mode. Every claim in
this line must be one an existing messaging system could falsify.

**The corpus's centre of mass.** Nineteen documents assume payment. If this line
succeeds, a large fraction of them need re-reading, and the program should decide
deliberately whether that is a v0.x pass or an acknowledged fork. It should not happen
by drift.

**Satisfaction is a seductive metric** and §3 shows exactly why. Any design in this line
that finds itself optimising a user-contentment number has rediscovered the attractor,
not escaped it.
