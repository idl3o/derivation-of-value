# _archive — superseded versions

Working note on the convention. Not published to the site.

## Why this exists

Every document in `_papers/` carries one version, and `_papers/` holds only the
current one. When a document is revised, the version it replaces stops existing
anywhere except in git history — which records that a change happened but makes
it awkward to *read* the earlier document as a document. This directory keeps
each superseded version as a readable file.

That matters more here than in most repositories, because the program's own
discipline is that a claim which could have been refuted and was not is worth
more than a claim never permitted to fail. Keeping the superseded drafts means
the record of what was claimed, and later withdrawn or sharpened, stays legible
rather than being flattened into the latest revision.

## Convention

```
_archive/<paper-slug>/v<version>.md
```

`<paper-slug>` matches the filename in `_papers/`. The archived file is the
document verbatim, front matter included, exactly as it stood at that version.
Nothing is edited on the way in — an archived version that contained an error
keeps the error, which is the point.

**Archive on supersession, not on publication.** A version is copied here at the
moment it stops being current, so `_papers/` holds vN and `_archive/` holds
v0.1 … v(N−1). A version that never went live still gets archived when it is
superseded; the changelog is where the question of what was ever published is
settled.

## Snapshotting

From the last committed state, before making the edit that supersedes it:

```sh
git show HEAD:_papers/<slug>.md > _archive/<slug>/v<old>.md
```

Or from the working tree, when the version being superseded is uncommitted:

```sh
cp _papers/<slug>.md _archive/<slug>/v<old>.md
```

## Not published

`_archive/` begins with an underscore, so Jekyll ignores it unless it is declared
as a collection, and it is additionally named in `_config.yml`'s `exclude` list.
It ships with the source and never becomes a site page. The same holds for
`code/`, which is excluded explicitly since it has no underscore.

## Contents

| paper | archived | note |
|---|---|---|
| `admitted-or-refused` | v0.1 | published state, 2026-07-23 |
| `borrowed-hardness` | v0.1 | published state, 2026-07-23 |
| `combination-proofs` | v0.1, v0.2 | v0.2 never published — see below |
| `kar-coin` | v0.1 | published state, 2026-07-23 |
| `proof-of-coherence` | v0.2, v0.3 | v0.3 never published |
| `sign-and-work` | v0.1 | never published |
| `the-multiplicity-freedom` | v0.1, v0.2 | neither published |

The 2026-07-23 v0.1 files are the state the site carried before this session,
recovered from git.

**Four of these versions never went live**, and they are kept for exactly the
reason the convention exists. `combination-proofs` v0.2 was the Kardashev–Barrow
and spectral-measurement revision, superseded by v0.3 within the hour.
`proof-of-coherence` v0.3 settled the copy-symmetry fork on the rank toy and was
superseded by v0.4 the same day, when the rank result turned out not to transfer
to H⁰. `the-multiplicity-freedom` v0.1 and v0.2 track the same discovery from the
other side: v0.1 stated hypothesis H1 about individual earnings when its own
theorem needed group totals, v0.2 corrected that and reported H1 discharged, and
v0.3 had to withdraw the discharge. `sign-and-work` v0.1 predates the first
measured trace gap.

Reading v0.2 and v0.3 of the Sybil paper side by side is the clearest record the
program has of a claim being made, corrected, strengthened, and then partly
withdrawn inside a single day. That sequence is invisible in the current version
and is the thing this directory exists to keep.
