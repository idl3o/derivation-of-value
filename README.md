# Derivation of Value

*A working program in mechanism design and the philosophy of value, published as an open anthology.*

[![Read online](https://img.shields.io/badge/read-idl3o.github.io-3b3b3b)](https://idl3o.github.io/derivation-of-value/)
[![Licence: CC BY 4.0](https://img.shields.io/badge/licence-CC%20BY%204.0-a63a3a)](https://creativecommons.org/licenses/by/4.0/)

A hub for working papers on Web3 cryptocurrency, sitting at the intersection of Web3, AI and the philosophy of value. The series turns around a single operator: the move from staking *contingent* quantities — energy, capital — to staking what such quantities are derived *from*: structural agreement, negentropy, dimensional integrity. Each document applies that operator once and records what survives.

The site is a static Jekyll build set in EB Garamond, published to GitHub Pages: **[idl3o.github.io/derivation-of-value](https://idl3o.github.io/derivation-of-value/)**.

## Contents

Nine working documents, in reading order. Each has its own page on the site.

1. **[Derivation of Value — Volume I](https://idl3o.github.io/derivation-of-value/anthology/derivation-of-value-i/)** *(Anthology · working draft)*
   The opening essay. Names the operator the series turns around and fixes the register for everything that follows.
2. **[Combination Proofs](https://idl3o.github.io/derivation-of-value/combination-proofs/)** *(Framework · v0.1)*
   A framework for Goodhart-asymptotic mechanism design, in which reward is gated on the conjunction of verifiably independent projections of a structural substrate. States the multiplication claim and a publicity-positive security property; reads Proof of Coherence as the worked instance.
3. **[Proof of Coherence](https://idl3o.github.io/derivation-of-value/whitepaper/)** *(Whitepaper · v0.2)*
   A sheaf-theoretic incentive mechanism for decentralised inference, with coherence recovered as the vanishing of sheaf cohomology and a spectral extension — *Proof by Resonance* — via the sheaf Hodge Laplacian.
4. **[Proof of Coherence — An Onboarding](https://idl3o.github.io/derivation-of-value/onboarding/)** *(Companion · v0.1)*
   A reader's path into the whitepaper: intuitions and motivations before the formalism.
5. **[Proof of Preservation — Volume II](https://idl3o.github.io/derivation-of-value/anthology/proof-of-preservation/)** *(Anthology · v0.1)*
   The negentropy derivation. Order is the one substrate the second law guarantees is scarce and refuses to attest: Landauer certifies that energy was *spent*, never that order was *made here*. Reframes preservation as certified by gauge-fixing the adversary's freedoms rather than by proof, and sets up the anchoring construction that follows.
6. **[Gauge-Fixing the Section Space](https://idl3o.github.io/derivation-of-value/gauge-fixing-the-section-space/)** *(Anthology paper · v0.1)*
   Anchoring architectures for negentropy-attested mechanisms. Composes four independent anchors — an astrophysical randomness beacon, a verifiable-delay-function chain, replication-style unique encoding and a dissipation floor — so that only honest global sections survive the quotient.
7. **[Omnium — Volume II](https://idl3o.github.io/derivation-of-value/anthology/omnium/)** *(Anthology · v0.1)*
   The value-as-vector derivation, paired with *Proof of Preservation*. The scalar price is a lossy projection of a vector whose coordinates — time, locality, purpose, provenance — fall into five algebraic kinds; the same entropy law that negentropy stakes against the world reappears here as the asymmetric price of erasing information inside money. Draws on the sibling [`vectorised-money`](https://github.com/idl3o/vectorised-money) and [`omnium`](https://github.com/idl3o/omnium) implementations.
8. **[Kar-Coin — Volume II](https://idl3o.github.io/derivation-of-value/anthology/kar-coin/)** *(Anthology · v0.1)*
   The civilizational-capacity derivation, completing the Volume II triptych. Value denominated against a people's position on the Kardashev scale — the order of magnitude at which it can act. The grandest substrate in the program and, minted naively against oracle-measured energy, the least intrinsically verifiable; its long-horizon nature is what forces the program's closing question of post-quantum durability. Draws on the sibling [`kar-coin`](https://github.com/idl3o/kar-coin) whitepaper.
9. **[Admitted or Refused — Volume III](https://idl3o.github.io/derivation-of-value/anthology/admitted-or-refused/)** *(Anthology · v0.1)*
   The turn from derivation to construction, and the opener of Volume III — the reserved "working examples" milestone. A running mechanism is a claim that can be false: what the vectorised-money kernel already shows (the thermodynamics — conservation, entropy-direction, substrate-independence) and what it does not yet prove (the Goodhart-asymptotic security, which needs an adversary in the loop). Records the Gauge-Fixing test suite as a challenge written before its respondent exists. Designed to stay open and accrue further examples.

## Reading it

The published site is the intended way to read the anthology: **[idl3o.github.io/derivation-of-value](https://idl3o.github.io/derivation-of-value/)**. Every document also lives as plain Markdown under [`_papers/`](_papers/) for reading directly on GitHub.

## Local preview

The site is a standard GitHub Pages / Jekyll project (see [`Gemfile`](Gemfile) and [`_config.yml`](_config.yml)). To build it locally:

```sh
bundle install
bundle exec jekyll serve
```

Then open the address Jekyll prints (by default `http://localhost:4000/derivation-of-value/`). Adding a document is a one-file operation: drop a Markdown file into `_papers/` with the collection's front matter (`label`, `blurb`, `status`, `order`) and it appears on the home page and gets its own page.

## Status

Working drafts throughout. The documents are stable enough for circulation but not yet for citation; versions are tracked per document in the [changelog](CHANGELOG.md) and noted inside each piece. Comments are welcome via issues or pull requests.

## Related

Sibling explorations of value and money by the same author:

- [vectorised-money](https://github.com/idl3o/vectorised-money) — an N-dimensional currency framework: money as a vector, not a scalar.
- [omnium](https://github.com/idl3o/omnium) — a first conception of *vectorised* money.
- [kar-coin](https://github.com/idl3o/kar-coin) — a currency that scales with and through civilisational progress.

## Licence

The writing in this repository is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — share and adapt freely, with attribution. See [`LICENSE`](LICENSE) for the full text.

---

Built by [S. Lavi](https://github.com/idl3o) · [@modsias](https://x.com/modsias) · CC BY 4.0
