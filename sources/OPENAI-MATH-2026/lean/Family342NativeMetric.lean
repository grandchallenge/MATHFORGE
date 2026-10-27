/-
Native family-342 compatibility/metric bridge.

Imports exactly the upstream OpenAI model. All results are about its actual
continuous alternating tangent forms, not a separate abstract surrogate.
A positive symmetric pairing is the pointwise Riemannian metric datum.
Metric smoothness is NOT asserted: it requires the open manifold-chart bridge.
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open scoped Manifold ContDiff

variable {X : Type*} [TopologicalSpace X] [ChartedSpace Space X]
  [IsManifold Model ∞ X]


/-- Under the elementary skew/negation identities and J²=-I,
invariance of a form is equivalent to symmetry of its induced pairing. -/
private theorem gcl_metric_abstract_iff
    {V : Type*} [AddGroup V] (A : V → V → ℝ) (J : V → V)
    (skew : ∀ u v, A u v = -A v u)
    (neg_left : ∀ u v, A (-u) v = -A u v)
    (neg_right : ∀ u v, A u (-v) = -A u v)
    (square : ∀ u, J (J u) = -u) :
    (∀ u v, A (J u) (J v) = A u v) ↔
      (∀ u v, A u (J v) = A v (J u)) := by
  constructor
  · intro h u v
    have hi := h (J u) v
    rw [square u, neg_left u (J v), skew (J u) v] at hi
    exact neg_injective hi
  · intro h u v
    calc
      A (J u) (J v) = A v (J (J u)) := h (J u) v
      _ = A v (-u) := by rw [square u]
      _ = -A v u := neg_right v u
      _ = A u v := by rw [skew v u]; simp

theorem gcl_eval_skew (α : TwoForm X) (x : X)
    (u v : TangentSpace Model x) :
    eval α x u v = -eval α x v u := by
  have h := (α x).toAlternatingMap.map_swap
    (v := ![v, u]) (i := (0 : Fin 2)) (j := (1 : Fin 2)) (by decide)
  have hs : (![v,u] ∘ Equiv.swap (0 : Fin 2) 1) = ![u,v] := by
    funext i
    fin_cases i <;> rfl
  rw [hs] at h
  exact h

theorem gcl_eval_neg_left (α : TwoForm X) (x : X)
    (u v : TangentSpace Model x) :
    eval α x (-u) v = -eval α x u v := by
  have h := (α x).toAlternatingMap.map_update_neg
    (v' := ![u, v]) (0 : Fin 2) u
  have hl : Function.update ![u,v] (0 : Fin 2) (-u) = ![-u,v] := by
    funext i
    fin_cases i <;> simp
  have hr : Function.update ![u,v] (0 : Fin 2) u = ![u,v] := by
    funext i
    fin_cases i <;> simp
  rw [hl,hr] at h
  exact h

theorem gcl_eval_neg_right (α : TwoForm X) (x : X)
    (u v : TangentSpace Model x) :
    eval α x u (-v) = -eval α x u v := by
  have h := (α x).toAlternatingMap.map_update_neg
    (v' := ![u, v]) (1 : Fin 2) v
  have hl : Function.update ![u,v] (1 : Fin 2) (-v) = ![u,-v] := by
    funext i
    fin_cases i <;> simp
  have hr : Function.update ![u,v] (1 : Fin 2) v = ![u,v] := by
    funext i
    fin_cases i <;> simp
  rw [hl,hr] at h
  exact h

/-- The induced metric pairing α(u,Jv) is symmetric iff α is J-invariant,
proved on the *actual upstream* manifold's continuous alternating two-form. -/
theorem gcl_native_invariant_iff_metric_symmetric
    (α : TwoForm X) (J : AlmostComplexStructure X) :
    IsInvariant α J ↔
    ∀ x (u v : TangentSpace Model x),
      eval α x u (J.endomorphism x v) =
        eval α x v (J.endomorphism x u) := by
  unfold IsInvariant
  constructor
  · intro h x
    exact (gcl_metric_abstract_iff
      (A := fun u v : TangentSpace Model x => eval α x u v)
      (J := J.endomorphism x)
      (gcl_eval_skew α x)
      (gcl_eval_neg_left α x)
      (gcl_eval_neg_right α x)
      (J.square x)).mp (h x)
  · intro h x
    exact (gcl_metric_abstract_iff
      (A := fun u v : TangentSpace Model x => eval α x u v)
      (J := J.endomorphism x)
      (gcl_eval_skew α x)
      (gcl_eval_neg_left α x)
      (gcl_eval_neg_right α x)
      (J.square x)).mpr (h x)

/-- Compatible is equivalent to a pointwise symmetric and positive pairing.
The smoothness of the resulting metric remains an independent obligation. -/
theorem gcl_native_compatible_iff_symmetric_positive
    (α : TwoForm X) (J : AlmostComplexStructure X) :
    Compatible α J ↔
    (∀ x (u v : TangentSpace Model x),
       eval α x u (J.endomorphism x v) =
         eval α x v (J.endomorphism x u)) ∧
    (∀ x (v : TangentSpace Model x), v ≠ 0 →
      0 < eval α x v (J.endomorphism x v)) := by
  unfold Compatible
  constructor
  · rintro ⟨ht, hi⟩
    exact ⟨(gcl_native_invariant_iff_metric_symmetric α J).mp hi, ht⟩
  · rintro ⟨hs, ht⟩
    exact ⟨ht, (gcl_native_invariant_iff_metric_symmetric α J).mpr hs⟩

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_eval_skew
#print axioms OAI.TamingCompatibility.gcl_eval_neg_left
#print axioms OAI.TamingCompatibility.gcl_eval_neg_right
#print axioms OAI.TamingCompatibility.gcl_native_invariant_iff_metric_symmetric
#print axioms OAI.TamingCompatibility.gcl_native_compatible_iff_symmetric_positive
