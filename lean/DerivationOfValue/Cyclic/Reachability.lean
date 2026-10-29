import DerivationOfValue.Cyclic.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Mathlib.Algebra.Ring.Rat
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Abel

/-!
# The obstruction on a cyclic cover is reachability

*The Obstruction, Computed* §6, Theorem 6.3 and Corollary 6.4, for any
`LayeredGraph`: the obstruction `γ_R(s)` vanishes if and only if `head s` and
`tail s` are joined by an undirected path in the section graph with `s`'s
layer removed.

The paper states the theorem for a commutative ring with `1 ≠ 0`. The proof
never multiplies, so `Ring R` with `Nontrivial R` is what is assumed here:
negation is used to send a path's edges traversed against their orientation to
`-1`, and `1 ≠ 0` is used once, at the end of the converse.

The argument is the paper's. Forward: an undirected path from `head s` to
`tail s` gives a unit flow by induction on its length (`exists_flow_of_reflTransGen`).
Converse: let `U` be the nodes reachable from `head s` off layer `s`; summing
conservation over `U` makes every edge crossing its boundary contribute zero,
so the unit demand at `tail s` must be met inside `U` (`reflTransGen_of_flow`).
-/

namespace DerivationOfValue.LayeredGraph

open Finset

variable {ι V E : Type*} (G : LayeredGraph ι V E)

/-! ### Steps and the simple graph -/

lemma step_symm {i : ι} {u v : V} (h : G.Step i u v) : G.Step i v u := by
  obtain ⟨e, he, h⟩ := h
  exact ⟨e, he, h.symm⟩

/-- The set of nodes reachable from `a` off layer `i` is closed under every
off-layer edge, in both directions. -/
lemma reach_closed (i : ι) (a : V) {e : E} (he : G.layer e ≠ i) :
    Relation.ReflTransGen (G.Step i) a (G.head e) ↔
      Relation.ReflTransGen (G.Step i) a (G.tail e) :=
  ⟨fun h => h.tail ⟨e, he, Or.inr ⟨rfl, rfl⟩⟩, fun h => h.tail ⟨e, he, Or.inl ⟨rfl, rfl⟩⟩⟩

lemma reflTransGen_adj_of_step {i : ι} {u v : V} (h : G.Step i u v) :
    Relation.ReflTransGen (G.without i).Adj u v := by
  by_cases huv : u = v
  · subst huv
    exact Relation.ReflTransGen.refl
  · refine Relation.ReflTransGen.single ?_
    unfold without
    rw [SimpleGraph.fromRel_adj]
    obtain ⟨e, he, ⟨h1, h2⟩ | ⟨h1, h2⟩⟩ := h
    · exact ⟨huv, Or.inl ⟨e, he, h1, h2⟩⟩
    · exact ⟨huv, Or.inr ⟨e, he, h1, h2⟩⟩

lemma step_of_adj {i : ι} {u v : V} (huv : (G.without i).Adj u v) : G.Step i u v := by
  unfold without at huv
  rw [SimpleGraph.fromRel_adj] at huv
  obtain ⟨-, ⟨e, he, h1, h2⟩ | ⟨e, he, h1, h2⟩⟩ := huv
  · exact ⟨e, he, Or.inl ⟨h1, h2⟩⟩
  · exact ⟨e, he, Or.inr ⟨h1, h2⟩⟩

/-- Reachability in the section graph with layer `i` removed is the reflexive
transitive closure of one undirected step through an off-layer edge. -/
lemma reachable_without_iff (i : ι) (a b : V) :
    (G.without i).Reachable a b ↔ Relation.ReflTransGen (G.Step i) a b := by
  rw [SimpleGraph.reachable_iff_reflTransGen]
  constructor
  · intro h
    induction h with
    | refl => exact Relation.ReflTransGen.refl
    | tail _ hadj ih => exact ih.tail (G.step_of_adj hadj)
  · intro h
    induction h with
    | refl => exact Relation.ReflTransGen.refl
    | tail _ hstep ih => exact ih.trans (G.reflTransGen_adj_of_step hstep)

section Flows

variable {R : Type*} [Ring R]
variable [Fintype E] [DecidableEq V]

/-! ### Linearity of the excess -/

lemma inflow_add (r₁ r₂ : E → R) (v : V) :
    G.inflow (r₁ + r₂) v = G.inflow r₁ v + G.inflow r₂ v := by
  unfold inflow
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun e _ => ?_
  simp only [Pi.add_apply]
  split_ifs <;> simp

lemma outflow_add (r₁ r₂ : E → R) (v : V) :
    G.outflow (r₁ + r₂) v = G.outflow r₁ v + G.outflow r₂ v := by
  unfold outflow
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun e _ => ?_
  simp only [Pi.add_apply]
  split_ifs <;> simp

lemma inflow_neg (r : E → R) (v : V) : G.inflow (-r) v = -G.inflow r v := by
  unfold inflow
  rw [← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl fun e _ => ?_
  simp only [Pi.neg_apply]
  split_ifs <;> simp

lemma outflow_neg (r : E → R) (v : V) : G.outflow (-r) v = -G.outflow r v := by
  unfold outflow
  rw [← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl fun e _ => ?_
  simp only [Pi.neg_apply]
  split_ifs <;> simp

lemma ex_add (r₁ r₂ : E → R) (v : V) : G.ex (r₁ + r₂) v = G.ex r₁ v + G.ex r₂ v := by
  unfold ex
  rw [inflow_add, outflow_add]
  abel

lemma ex_neg (r : E → R) (v : V) : G.ex (-r) v = -G.ex r v := by
  unfold ex
  rw [inflow_neg, outflow_neg]
  abel

lemma ex_zero (v : V) : G.ex (0 : E → R) v = 0 := by
  simp [ex, inflow, outflow]

/-! ### Demand arithmetic -/

lemma demand_self (a v : V) : (demand a a v : R) = 0 := by
  unfold demand
  exact sub_self _

lemma demand_add (a b c v : V) : (demand a b v : R) + demand b c v = demand a c v := by
  unfold demand
  abel

lemma demand_neg (a b v : V) : -(demand a b v : R) = demand b a v := by
  unfold demand
  abel

lemma sum_demand (a b : V) (U : Finset V) :
    ∑ v ∈ U, (demand a b v : R) = (if b ∈ U then 1 else 0) - (if a ∈ U then 1 else 0) := by
  unfold demand
  rw [Finset.sum_sub_distrib, Finset.sum_ite_eq, Finset.sum_ite_eq]

/-! ### Flows compose -/

lemma isFlowFrom_zero (i : ι) (a : V) : G.IsFlowFrom i (0 : E → R) a a :=
  ⟨fun _ _ => rfl, fun v => by rw [ex_zero, demand_self]⟩

lemma isFlowFrom_neg {i : ι} {r : E → R} {a b : V} (h : G.IsFlowFrom i r a b) :
    G.IsFlowFrom i (-r) b a :=
  ⟨fun e he => by simp [h.1 e he], fun v => by rw [ex_neg, h.2 v, demand_neg]⟩

lemma isFlowFrom_add {i : ι} {r₁ r₂ : E → R} {a b c : V}
    (h₁ : G.IsFlowFrom i r₁ a b) (h₂ : G.IsFlowFrom i r₂ b c) :
    G.IsFlowFrom i (r₁ + r₂) a c :=
  ⟨fun e he => by simp [h₁.1 e he, h₂.1 e he],
   fun v => by rw [ex_add, h₁.2 v, h₂.2 v, demand_add]⟩

/-! ### A closed set has zero net excess -/

lemma sum_inflow (r : E → R) (U : Finset V) :
    ∑ v ∈ U, G.inflow r v = ∑ e, (if G.head e ∈ U then r e else 0) := by
  unfold inflow
  rw [Finset.sum_comm]
  simp_rw [Finset.sum_ite_eq]

lemma sum_outflow (r : E → R) (U : Finset V) :
    ∑ v ∈ U, G.outflow r v = ∑ e, (if G.tail e ∈ U then r e else 0) := by
  unfold outflow
  rw [Finset.sum_comm]
  simp_rw [Finset.sum_ite_eq]

lemma sum_ex (r : E → R) (U : Finset V) :
    ∑ v ∈ U, G.ex r v =
      (∑ e, (if G.head e ∈ U then r e else 0)) - ∑ e, (if G.tail e ∈ U then r e else 0) := by
  unfold ex
  rw [Finset.sum_sub_distrib, sum_inflow, sum_outflow]

/-- Summing conservation over a set closed under the off-layer edges: every edge
either lies in layer `i`, where the flow is zero, or has both ends in `U` or
neither, so the boundary carries nothing. -/
lemma sum_ex_eq_zero_of_closed {i : ι} {r : E → R} (hr : ∀ e, G.layer e = i → r e = 0)
    {U : Finset V} (hU : ∀ e, G.layer e ≠ i → (G.head e ∈ U ↔ G.tail e ∈ U)) :
    ∑ v ∈ U, G.ex r v = 0 := by
  rw [sum_ex, sub_eq_zero]
  refine Finset.sum_congr rfl fun e _ => ?_
  by_cases h : G.layer e = i
  · simp [hr e h]
  · simp only [hU e h]

/-- Converse direction of Theorem 6.3. The only use of `1 ≠ 0` in the file. -/
lemma reflTransGen_of_flow [Fintype V] [Nontrivial R] {i : ι} {r : E → R} {a b : V}
    (h : G.IsFlowFrom i r a b) : Relation.ReflTransGen (G.Step i) a b := by
  classical
  set U : Finset V := Finset.univ.filter (Relation.ReflTransGen (G.Step i) a) with hUdef
  have hmem : ∀ v, v ∈ U ↔ Relation.ReflTransGen (G.Step i) a v := fun v => by
    simp [hUdef]
  have hzero : ∑ v ∈ U, G.ex r v = 0 :=
    G.sum_ex_eq_zero_of_closed h.1 fun e he => by rw [hmem, hmem]; exact G.reach_closed i a he
  have hsum : ∑ v ∈ U, G.ex r v = (if b ∈ U then 1 else 0) - (if a ∈ U then 1 else 0) := by
    rw [Finset.sum_congr rfl fun v _ => h.2 v, sum_demand]
  rw [hzero, ite_eq_left ((hmem a).2 Relation.ReflTransGen.refl)] at hsum
  by_contra hb
  rw [ite_eq_right (fun h' => hb ((hmem b).1 h')), zero_sub] at hsum
  exact one_ne_zero (neg_eq_zero.mp hsum.symm)

section SingleEdge

variable [DecidableEq E]

/-! ### The flow of a single edge -/

lemma sum_ite_single (e : E) (p : E → Prop) [DecidablePred p] (c : R) :
    (∑ e', (if p e' then (if e' = e then c else 0) else 0)) = if p e then c else 0 := by
  have h : ∀ e', (if p e' then (if e' = e then c else 0) else 0) =
      if e' = e then (if p e' then c else 0) else 0 := by
    intro e'
    split_ifs <;> rfl
  simp_rw [h]
  rw [Finset.sum_ite_eq' Finset.univ e (fun e' => if p e' then c else 0)]
  simp

lemma inflow_single (e : E) (v : V) :
    G.inflow (single e : E → R) v = if G.head e = v then 1 else 0 := by
  unfold inflow single
  exact sum_ite_single e (fun e' => G.head e' = v) 1

lemma outflow_single (e : E) (v : V) :
    G.outflow (single e : E → R) v = if G.tail e = v then 1 else 0 := by
  unfold outflow single
  exact sum_ite_single e (fun e' => G.tail e' = v) 1

lemma ex_single (e : E) (v : V) :
    G.ex (single e : E → R) v = demand (G.tail e) (G.head e) v := by
  unfold ex demand
  rw [inflow_single, outflow_single]

lemma isFlowFrom_single {i : ι} {e : E} (he : G.layer e ≠ i) :
    G.IsFlowFrom i (single e : E → R) (G.tail e) (G.head e) := by
  refine ⟨fun e' h => ?_, fun v => G.ex_single e v⟩
  have hne : e' ≠ e := fun h' => he (h' ▸ h)
  simp [single, hne]

lemma exists_flow_of_step {i : ι} {u v : V} (h : G.Step i u v) :
    ∃ r : E → R, G.IsFlowFrom i r u v := by
  obtain ⟨e, he, ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩⟩ := h
  · exact ⟨_, G.isFlowFrom_single he⟩
  · exact ⟨_, G.isFlowFrom_neg (G.isFlowFrom_single he)⟩

/-- Forward direction of Theorem 6.3: an undirected path off layer `i` carries a
unit flow, `+1` along edges traversed with their orientation and `-1` against. -/
lemma exists_flow_of_reflTransGen {i : ι} {a b : V}
    (h : Relation.ReflTransGen (G.Step i) a b) : ∃ r : E → R, G.IsFlowFrom i r a b := by
  induction h with
  | refl => exact ⟨0, G.isFlowFrom_zero i a⟩
  | tail _ hstep ih =>
    obtain ⟨r₁, h₁⟩ := ih
    obtain ⟨r₂, h₂⟩ := G.exists_flow_of_step (R := R) hstep
    exact ⟨r₁ + r₂, G.isFlowFrom_add h₁ h₂⟩

/-! ### From the Čech system to flows -/

/-- `γ_R(s) = 0` iff the off-layer part of a compatible family is a unit flow
from `head s` to `tail s`. -/
lemma vanishes_iff_exists_flow (s : E) :
    G.Vanishes R s ↔ ∃ r : E → R, G.IsFlowFrom (G.layer s) r (G.head s) (G.tail s) := by
  constructor
  · rintro ⟨r, hr, hs⟩
    refine ⟨r - single s, fun e he => ?_, fun v => ?_⟩
    · simp only [Pi.sub_apply, single, hs e he, sub_self]
    · have hex : G.ex r v = 0 := sub_eq_zero.mpr (hr v)
      rw [sub_eq_add_neg, ex_add, ex_neg, ex_single, hex, zero_add, demand_neg]
  · rintro ⟨r, hr, hv⟩
    refine ⟨r + single s, fun v => sub_eq_zero.mp ?_, fun e he => ?_⟩
    · show G.ex (r + single s) v = 0
      rw [ex_add, hv v, ex_single, demand_add, demand_self]
    · simp only [Pi.add_apply, hr e he, single, zero_add]

/-! ### The theorem -/

/-- **Theorem 6.3** (*The Obstruction, Computed*). On a cyclic cover the
obstruction `γ_R(s)` of a section `s` vanishes if and only if `head s` and
`tail s` are joined by an undirected path in the section graph with `s`'s
layer removed. Stated for any layered graph and any nontrivial ring. -/
theorem vanishes_iff_reachable [Fintype V] [Nontrivial R] (s : E) :
    G.Vanishes R s ↔ (G.without (G.layer s)).Reachable (G.head s) (G.tail s) := by
  rw [vanishes_iff_exists_flow, reachable_without_iff]
  exact ⟨fun ⟨_, hr⟩ => G.reflTransGen_of_flow hr, fun h => G.exists_flow_of_reflTransGen h⟩

end SingleEdge

end Flows

section RingIndependence

variable [Fintype V] [Fintype E] [DecidableEq V] [DecidableEq E]

/-- **Corollary 6.4** (ring independence). On a cyclic cover the obstruction
vanishes over one nontrivial ring iff it vanishes over any other. -/
theorem vanishes_iff_vanishes (R₁ R₂ : Type*) [Ring R₁] [Nontrivial R₁]
    [Ring R₂] [Nontrivial R₂] (s : E) : G.Vanishes R₁ s ↔ G.Vanishes R₂ s := by
  rw [vanishes_iff_reachable, vanishes_iff_reachable]

/-- The three rings the instrument computes over agree on every cyclic cover. -/
theorem vanishes_int_iff_rat (s : E) : G.Vanishes ℤ s ↔ G.Vanishes ℚ s :=
  G.vanishes_iff_vanishes ℤ ℚ s

theorem vanishes_int_iff_zmod_two (s : E) : G.Vanishes ℤ s ↔ G.Vanishes (ZMod 2) s :=
  G.vanishes_iff_vanishes ℤ (ZMod 2) s

end RingIndependence

end DerivationOfValue.LayeredGraph
