import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Defs
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Data.Fintype.BigOperators

/-!
# Layered graphs, flows and the cyclic obstruction

*The Obstruction, Computed* §6 (Definitions 6.1–6.2). On a cyclic cover the
section graph has a node for every (overlap, assignment) pair and, for every
local section `t` of a context `C`, an edge from `t`'s restriction to the
overlap with `C`'s predecessor (its *tail*) to its restriction to the overlap
with `C`'s successor (its *head*). Edges are grouped in *layers* by context.

Proposition 3.2 of the same paper writes the Čech obstruction `γ_R(s)` of a
section `s` as an `R`-linear system: one unknown per local section of every
context other than `s`'s own, with `s`'s layer fixed to the indicator of `s`,
and one equation per (overlap, assignment) saying that the coefficients
restricting to that assignment agree on both sides. On a cyclic cover every
overlap lies between exactly two consecutive contexts, so the equation at a
node is conservation of an `R`-valued flow: the coefficients of the edges
ending at the node sum to the coefficients of the edges starting there.

This file sets up that combinatorial skeleton, `LayeredGraph`, on arbitrary
finite types of nodes and edges with an arbitrary type of layer labels. The
cyclic cover enters only through the labelling; nothing below uses the cycle,
and the reachability theorem in `Reachability.lean` holds for any layered
graph. Where the cyclic hypothesis is genuinely load-bearing is upstream, in
reading the Čech system *as* a flow system — a section of a context with three
or more overlaps is a hyperedge, not an edge, which is why *The Ring and the
Chord* §3 finds the equivalence failing on chorded covers.

The equations for disjoint pairs of contexts — whose overlap is the empty set,
with its single (empty) assignment, so that the Čech cochain group there is `R`
itself — are omitted from `IsConserved`. On a cyclic cover they are implied:
`CyclicLayeredGraph.total_succ` in `Cover.lean` shows that conservation at
every node of one overlap forces the two adjacent layers to carry the same
total coefficient, so all layers do. The paper's proof says "non-consecutive
contexts share nothing and impose nothing"; this is the reason, stated.
-/

namespace DerivationOfValue

open Finset

/-- A finite directed multigraph whose edges carry a layer label. For the
section graph of a cyclic cover: nodes are (overlap, assignment) pairs, edges
are (context, local section) pairs, `layer` is the context, `tail`/`head` are
the restrictions to the predecessor and successor overlaps. -/
structure LayeredGraph (ι V E : Type*) where
  /-- The layer (context) an edge belongs to. -/
  layer : E → ι
  /-- Restriction to the overlap with the predecessor context. -/
  tail : E → V
  /-- Restriction to the overlap with the successor context. -/
  head : E → V

namespace LayeredGraph

variable {ι V E : Type*} (G : LayeredGraph ι V E)
variable {R : Type*} [Ring R]
variable [Fintype E] [DecidableEq V] [DecidableEq E]

/-- Sum of the coefficients of the edges ending at `v`. -/
def inflow (r : E → R) (v : V) : R :=
  ∑ e, (if G.head e = v then r e else 0)

/-- Sum of the coefficients of the edges starting at `v`. -/
def outflow (r : E → R) (v : V) : R :=
  ∑ e, (if G.tail e = v then r e else 0)

/-- Net excess at `v`: what arrives minus what leaves. -/
def ex (r : E → R) (v : V) : R :=
  G.inflow r v - G.outflow r v

/-- The Čech compatibility condition of Proposition 3.2 on a cyclic cover:
conservation of the coefficient flow at every (overlap, assignment) node. -/
def IsConserved (r : E → R) : Prop :=
  ∀ v, G.inflow r v = G.outflow r v

/-- The obstruction `γ_R(s)` vanishes: some conserved family of coefficients
fixes `s`'s own layer to the indicator of `s`. This is Proposition 3.2's
system with `R` in place of `ℤ`; its identification with the relative Čech
class of Abramsky–Barbosa–Kishida–Lal–Mansfield, Proposition 4.3, is cited in
the paper and not reproduced here. -/
def Vanishes (R : Type*) [Ring R] (s : E) : Prop :=
  ∃ r : E → R, G.IsConserved r ∧
    ∀ e, G.layer e = G.layer s → r e = if e = s then 1 else 0

/-- One undirected step through an edge not in layer `i`. -/
def Step (i : ι) (u v : V) : Prop :=
  ∃ e, G.layer e ≠ i ∧ ((G.tail e = u ∧ G.head e = v) ∨ (G.tail e = v ∧ G.head e = u))

/-- The section graph with layer `i` removed, as a simple graph on the nodes:
`u` and `v` are adjacent when some edge outside layer `i` joins them in either
direction. Parallel edges collapse, which reachability does not see. -/
def without (i : ι) : SimpleGraph V :=
  SimpleGraph.fromRel fun u v => ∃ e, G.layer e ≠ i ∧ G.tail e = u ∧ G.head e = v

/-- Unit demand from `a` to `b`: the excess a flow carrying one unit from `a`
to `b` must show at every node. -/
def demand (a b v : V) : R :=
  (if b = v then 1 else 0) - (if a = v then 1 else 0)

/-- `r` is a unit flow from `a` to `b` supported off layer `i`. -/
def IsFlowFrom (i : ι) (r : E → R) (a b : V) : Prop :=
  (∀ e, G.layer e = i → r e = 0) ∧ ∀ v, G.ex r v = demand a b v

/-- The indicator of a single edge. -/
def single (e : E) : E → R :=
  fun e' => if e' = e then 1 else 0

end LayeredGraph

end DerivationOfValue
