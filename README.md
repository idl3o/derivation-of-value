# Derivation of Value

A working program in mechanism design and the philosophy of value, presented as an open anthology.

**Site:** [idl3o.github.io/derivation-of-value](https://idl3o.github.io/derivation-of-value/)

## What this is

This repository carries four working drafts:

- **Anthology, Volume I — *Derivation of Value*.** The opening essay, naming the operator the series turns around: the move from staking contingent quantities (energy, capital) to staking what such quantities are derived from (structural agreement, negentropy, dimensional integrity). Borges-register essayistic.
- **Framework — *Combination Proofs*.** A framework paper formalising the property that distinguishes Goodhart-asymptotic mechanisms: reward gated on the conjunction of verifiably independent projections of a structural substrate. Establishes the multiplication claim and the publicity-positive security claim. PoC + PbR is the worked instance.
- **Whitepaper — *Proof of Coherence* (v0.2).** A Goodhart-asymptotic incentive mechanism for decentralised inference. Sheaf-theoretic, with a spectral extension via *Proof by Resonance*. The technical core of the program.
- **Companion — *Onboarding*.** A reader's path into the whitepaper. Intuitions and motivations before the formalism.

All four are working drafts — stable enough for circulation, not yet for citation. Versioning is tracked in `CHANGELOG.md`.

## Repo layout

```
.
├── _config.yml                 Jekyll config (baseurl set for project-page hosting)
├── _layouts/                   Page templates
│   ├── default.html
│   ├── home.html
│   └── document.html
├── assets/css/style.css        Editorial stylesheet (EB Garamond, cream/ink/oxblood)
├── index.md                    Landing
├── anthology/
│   └── derivation-of-value-i.md    Volume I
├── combination-proofs/
│   └── index.md                Framework paper
├── whitepaper/
│   └── index.md                Proof of Coherence v0.2
├── onboarding/
│   └── index.md                Companion to the whitepaper
├── CHANGELOG.md
├── LICENSE                     CC BY 4.0
├── Gemfile
└── README.md
```

## Editing

Markdown is canonical. GitHub Pages builds the site on every push to `main`.

Local preview (requires Ruby + bundler):

```bash
bundle install
bundle exec jekyll serve
```

To revise a document, edit its `index.md` in place — leave the front matter (between the `---` markers at the top) intact. Section breaks render as ornamental glyphs from three hyphens on their own line; italic centered section titles use the kramdown class syntax:

```markdown
*The First Derivation*
{:.section-title}
```

## Hosting configuration

`_config.yml` is set for project-page hosting at `idl3o.github.io/derivation-of-value`. If switching to a custom domain or a user/org root, change `baseurl: "/derivation-of-value"` to `baseurl: ""`.

## License

The writing in this repository is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Share and adapt freely, with attribution.

See `LICENSE` for the full text. Source code added later may carry its own permissive licence (MIT or Apache 2.0) noted in the relevant directory.

## Versioning

Tracked in `CHANGELOG.md`. The scheme:

- **Patch** — typos, prose polish, single-paragraph clarifications. No new claims, no structural change.
- **Minor** — new sections, sharpened theorems, added worked examples, reframed claims that don't contradict the previous version.
- **Major** — the document graduates from working draft. Claims would be defended to a hostile reader.

Each document carries its own version, noted in its front matter and inside the document.
