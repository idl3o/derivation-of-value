# lean

Machine-checked proofs for the *Derivation of Value* program, in Lean 4 with Mathlib.

The directory holds proofs only where a paper's claim is an argument rather than a
restatement of a cost model. The set-arithmetic theorems of the exclusion line are not
here: the risk in them was never the arithmetic. What is here is the one theorem the
corpus states for an arbitrary ring and offers to a hostile reader.

## Contents

| file | what it proves |
|---|---|
| `DerivationOfValue/Cyclic/Basic.lean` | The section graph of a cyclic cover as a `LayeredGraph`: finite nodes and edges, edges labelled by layer (context), `tail`/`head` the restrictions to the predecessor and successor overlaps. The Čech compatibility system of *The Obstruction, Computed* Proposition 3.2, read on a cyclic cover as conservation of an `R`-valued flow (`IsConserved`); the obstruction `Vanishes R s`; the section graph with a layer removed (`without`). |
| `DerivationOfValue/Cyclic/Reachability.lean` | **Theorem 6.3** (`vanishes_iff_reachable`): `γ_R(s) = 0` iff `head s` and `tail s` are joined by an undirected path in the section graph with `s`'s layer removed. **Corollary 6.4** (`vanishes_iff_vanishes`): the obstruction vanishes over one nontrivial ring iff over any other; `ℤ`, `ℚ` and `ℤ₂` instantiated. |
| `DerivationOfValue/Cyclic/Cover.lean` | The cyclic structure (`CyclicLayeredGraph`: every node on an overlap, layer `j` running from overlap `j − 1` to overlap `j`) and what the empty overlaps impose. Conservation forces adjacent layers to carry equal totals (`total_succ`), hence all layers (`total_eq`), so the Čech system with the empty-overlap equations included is equivalent to conservation alone (`isCechCompatible_iff`). |

## What the formalisation changed

Stated before the first build, per the program's method, and left as written.

- **Commutativity is not used.** The paper assumes a commutative ring with `1 ≠ 0`; the
  proof assumes `Ring R` and `Nontrivial R`. Negation sends a path's edges traversed
  against their orientation to `−1`; `1 ≠ 0` is used once, at the end of the converse.
- **The empty overlaps.** The paper's proof says non-consecutive contexts "share nothing
  and impose nothing". Their Čech cochain group is `R`, and the equation there says two
  layers carry the same total coefficient. `Cover.lean` derives it from conservation,
  which is why `code/contextuality.py` may skip disjoint pairs in `cech_system` without
  changing the answer on a cyclic cover.
- **Parallel edges.** Two sections of one context with the same tail and head are
  parallel edges of the section graph. `without` collapses them into a `SimpleGraph`,
  which reachability does not see.
- **The cycle is upstream.** Nothing in `Reachability.lean` uses the cyclic hypothesis;
  the theorem holds for any finite layered multigraph. Where the hypothesis is
  load-bearing is in reading the Čech system *as* a flow system at all — a section of a
  context with three or more overlaps is a hyperedge — which is why *The Ring and the
  Chord* §3 finds the equivalence failing on chorded covers.

## What is declined

`Vanishes` is Proposition 3.2's linear system with `R` in place of `ℤ`. Its identification
with the relative Čech class of Abramsky, Barbosa, Kishida, Lal and Mansfield
(*Contextuality, Cohomology and Paradox*, Proposition 4.3) is cited in the paper and not
formalised. Proposition 6.5 (extension is directed reachability) and Corollaries 6.6–6.7
are not formalised. No measurement scenario is instantiated: the structures take the
section graph as given, and the instrument's `section_graph` builds it.

## Build

```
cd lean
lake exe cache get   # Mathlib's prebuilt oleans; .lake/ comes to ~7 GB
lake build
```

Toolchain `leanprover/lean4:v4.35.0` (`lean-toolchain`); Mathlib pinned to its `v4.35.0`
tag in `lakefile.toml`, exact commit in `lake-manifest.json`. Bumping either is a decision,
made for both together. `.github/workflows/lean.yml` builds the development on every push
touching this directory and fails on any `sorry`.
