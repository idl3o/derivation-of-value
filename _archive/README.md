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

| paper | archived |
|---|---|
| `admitted-or-refused` | v0.1 |
| `borrowed-hardness` | v0.1 |
| `combination-proofs` | v0.1, v0.2 |
| `kar-coin` | v0.1 |

All four v0.1 files are the state published to the site as of the 2026-07-23
commits, recovered from git. `combination-proofs` v0.2 is the Kardashev–Barrow
and spectral-measurement revision, superseded by v0.3 the same day and never
pushed.
