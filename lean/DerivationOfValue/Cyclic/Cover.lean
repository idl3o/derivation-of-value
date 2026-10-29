import DerivationOfValue.Cyclic.Reachability
import Mathlib.Algebra.Group.Fin.Basic
import Mathlib.Data.ZMod.Defs

/-!
# The cyclic structure, and what the empty overlaps impose

A `LayeredGraph` over `Fin n` becomes the section graph of a cyclic cover once
every node is placed on an overlap: nodes on overlap `j` lie between contexts
`j` and `j + 1`, so an edge of layer `j` runs from overlap `j - 1` to overlap `j`.

The Čech system of *The Obstruction, Computed* Proposition 3.2 has one equation
per pair of contexts and assignment on their overlap. Non-consecutive contexts
of a cyclic cover are disjoint; their overlap is the empty set, which carries
exactly one assignment, so the cochain group there is `R` itself and the
equation says the two contexts carry the same total coefficient.
`LayeredGraph.IsConserved` omits these equations, and `code/contextuality.py`
`cech_system` skips disjoint pairs outright. This file shows the omission is
harmless on a cyclic cover: conservation at the nodes of overlap `j` forces
layers `j` and `j + 1` to carry equal totals (`total_succ`), hence every layer
carries the same total (`total_eq`), and the system with the empty overlaps
included is equivalent to the one without (`isCechCompatible_iff`). The paper's
proof says "non-consecutive contexts share nothing and impose nothing"; this is
the reason, stated.
-/

namespace DerivationOfValue

/-- A layered graph over `Fin n` whose nodes sit on overlaps: an edge of layer
`j` runs from overlap `j - 1` to overlap `j`. -/
structure CyclicLayeredGraph (n : ℕ) [NeZero n] (V E : Type*) extends
    LayeredGraph (Fin n) V E where
  /-- The overlap a node's assignment lives on. -/
  ov : V → Fin n
  ov_head : ∀ e, ov (head e) = layer e
  ov_tail : ∀ e, ov (tail e) = layer e - 1

namespace CyclicLayeredGraph

open Finset

variable {n : ℕ} [NeZero n] {V E : Type*} (G : CyclicLayeredGraph n V E)
variable {R : Type*} [Ring R] [Fintype V] [Fintype E] [DecidableEq V]

/-- Total coefficient carried by layer `j`: the image of the layer's cochain in
the cochain group `R` of the empty overlap. -/
def total (r : E → R) (j : Fin n) : R :=
  ∑ e, (if G.layer e = j then r e else 0)

lemma total_eq_sum_inflow (r : E → R) (j : Fin n) :
    G.total r j = ∑ v ∈ univ.filter (fun v => G.ov v = j), G.toLayeredGraph.inflow r v := by
  rw [LayeredGraph.sum_inflow]
  refine Finset.sum_congr rfl fun e _ => ?_
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, G.ov_head]

lemma total_succ_eq_sum_outflow (r : E → R) (j : Fin n) :
    G.total r (j + 1) =
      ∑ v ∈ univ.filter (fun v => G.ov v = j), G.toLayeredGraph.outflow r v := by
  rw [LayeredGraph.sum_outflow]
  refine Finset.sum_congr rfl fun e _ => ?_
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, G.ov_tail, sub_eq_iff_eq_add]

/-- Conservation at every node of overlap `j` forces layers `j` and `j + 1` to
carry the same total: the equation of the empty overlap between them, derived. -/
theorem total_succ (r : E → R) (hr : G.toLayeredGraph.IsConserved r) (j : Fin n) :
    G.total r (j + 1) = G.total r j := by
  rw [total_succ_eq_sum_outflow, total_eq_sum_inflow]
  exact Finset.sum_congr rfl fun v _ => (hr v).symm

open scoped Fin.NatCast in
/-- Every layer of a conserved family carries the same total. The cast `ℕ → Fin n`
is opt-in in this Mathlib (`Fin.NatCast`), since it wraps. -/
theorem total_eq (r : E → R) (hr : G.toLayeredGraph.IsConserved r) (j k : Fin n) :
    G.total r j = G.total r k := by
  suffices h : ∀ m : ℕ, G.total r (j + (m : Fin n)) = G.total r j by
    have hk := h (k - j).val
    rw [Fin.cast_val_eq_self, add_sub_cancel] at hk
    exact hk.symm
  intro m
  induction m with
  | zero => simp
  | succ m ih => rw [Nat.cast_succ, ← add_assoc, total_succ G r hr, ih]

/-- Proposition 3.2's system with the equations of the empty overlaps included:
conservation at every node, and equal totals on every pair of layers. -/
def IsCechCompatible (r : E → R) : Prop :=
  G.toLayeredGraph.IsConserved r ∧ ∀ j k, G.total r j = G.total r k

/-- On a cyclic cover the empty overlaps impose nothing: the full Čech system is
equivalent to conservation at the nodes alone. -/
theorem isCechCompatible_iff (r : E → R) :
    G.IsCechCompatible r ↔ G.toLayeredGraph.IsConserved r :=
  ⟨And.left, fun h => ⟨h, G.total_eq r h⟩⟩

end CyclicLayeredGraph

end DerivationOfValue
