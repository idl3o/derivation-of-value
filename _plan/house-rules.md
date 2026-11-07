# House rules — 2026-10-03, rewritten 2026-11-07

Working document. Not published to the site.

Decided 2026-10-03 and drafted the same day with a revised `index.md`; neither
file reached the repository (the connector was read-only) and both were lost.
This is the rewrite from the record of the decision. It supersedes
`research-program.md` §4 "Drafting conventions", which remains in place as the
history of what the rules replaced.

---

## 1. One world, each piece whole

**Every published piece stands alone and belongs to one universe.** A reader who
opens any document first is owed a complete argument, and a reader who has read
the rest is owed the same objects under the same names. The two obligations are
met together or not at all:

- A paper is **complete in itself**. Its claims are stated, its definitions are
  given or restated, and its result is reachable from its own pages.
- A paper **shares the anthology's vocabulary and its objects**. τ is the trace
  gap, ι is graded independence, Γ is the conjunction's fake-cost, the anchors
  are *Gauge-Fixing*'s four, residue is Volume V's word. A paper that needs one
  of these uses the name the corpus uses; a paper that needs a different quantity
  gives it a different symbol.

## 2. Naming other papers

**Body text names other papers by title, never by section number.** "*One's Own
Anchor* proves that every declared-frame reading evidences nothing" is a sentence
a reader can act on; "*OOA* Thm 3.4" is a pointer that moves when the paper is
revised. Section references belong in `_plan/` and in the changelog, where they
are maintenance, not argument. A theorem may be named by its number when it is
quoted in full and the number is part of its name in the corpus (Theorem 3.4 of
*One's Own Anchor*; Theorem 6.3 of *The Obstruction, Computed*).

**A borrowed result is restated where it is used.** One or two sentences, in the
borrowing paper's own words, saying what the result is and what it is being used
for. The reader is not sent elsewhere to find out what the sentence means.

## 3. Mandatory and optional sections

- **What Is Declined** is mandatory. Every paper carries one. It names the
  flattering readings the paper refuses, and it is where a prior-art check
  records what is cited rather than claimed.
- **Open Problems** are numbered.
- **Neighbours** is optional. It names the papers whose objects this one shares
  and says, in a line each, where they touch. It is the place for the connective
  tissue that §2 keeps out of the body.
- Where a paper carries a measurement, it names the `code/` module that
  reproduces it. Where the instrument is lost or was never in the repository,
  the paper says so where the measurement is reported.

## 4. The governing figure

**Each paper carries a governing figure that opens and closes it.** The figure
is the paper's object seen whole — the sleeper, the wound clock, the ledger
nobody built, the path across the grass. It is introduced before the machinery
and returned to after it, so that the machinery is seen to have been about
something.

## 5. Register

Unchanged from the corpus's practice, stated here so that it is stated:
absent narrator, declaratives, no rhetorical questions, no staged uncertainty,
no reader-directed imperatives. Negative results stand without recuperative
framing. Corrections are made in place, with strikethrough and a pointer to the
paper that made them; a refuted claim stays visible. Mathematics is Unicode, not
LaTeX; the site has no MathJax. British English. A prior-art check precedes any
claim of novelty.

## 6. Grandfathering

**Orders 1–28 are grandfathered**, and so are the three papers of 2026-08-10
admitted on 2026-11-07 as orders 29–31, which were written before these rules
and whose arguments were not revised on admission. A grandfathered paper is
**conformed only when it is next revised**, and then only in the parts the
revision touches. Nothing is rewritten for style alone. From order 32 onward the
rules apply at drafting.

## 7. What this replaces

`research-program.md` §4 fixed the front-matter shape, the `## Abstract` and
`## N. Title` structure for technical papers, the Borges register for the
volumes, the mandatory What Is Declined, and a six-item checklist. All of that
stands except where §§1–4 above say more. In particular the checklist's item 1 —
read the sibling papers on the shared substrate before drafting — is now the
two obligations of §1, and its item 6 — a cited measurement must be reproducible
from `code/` — now carries the exception in §3 for an instrument that is not in
the repository.
