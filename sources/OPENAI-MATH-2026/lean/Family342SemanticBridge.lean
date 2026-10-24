/-
Family-342 semantic bridge, stage 1; exact pinned OpenAI Math 2026 source.

This module imports upstream OAI.Geometry.TamingCompatibility.Model; it proves
that for a taming two-form, the explicit Lean IsNondegenerate assumption is
mathematically redundant, and establishes the linear-algebra equivalence
between J-invariance and symmetry of g(u,v)=ω(u,Jv) under explicit
alternating-form identities. It does NOT establish the manifold/chart or
exterior-derivative naturality bridges.

Replayed by .github/workflows/openai-math-pinned-lean.yml against upstream
openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
using leanprover/lean4:v4.34.1.
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open scoped Manifold ContDiff

variable {X : Type*} [TopologicalSpace X] [ChartedSpace Space X]
  [IsManifold Model ∞ X]

/-- Strict taming excludes every nonzero vector from the radical of the form.
This is a nontrivial exact implication in the upstream manifold model. -/
theorem gcl_tames_implies_isNondegenerate
    (α : TwoForm X) (J : AlmostComplexStructure X)
    (ht : Tames α J) : IsNondegenerate α := by
  intro x v hv
  by_contra hne
  have hp : 0 < eval α x v (J.endomorphism x v) := ht x v hne
  have hz : eval α x v (J.endomorphism x v) = 0 :=
    hv (J.endomorphism x v)
  rw [hz] at hp
  exact (lt_irrefl (0 : ℝ)) hp

/-- Taming makes the IsNondegenerate conjunct of IsSymplectic redundant.
Thus the formal taming hypothesis cannot be artificially strengthened by
the presence of the additional algebraic conjunct. -/
theorem gcl_symplectic_and_tames_iff_smooth_closed_tames
    (α : TwoForm X) (J : AlmostComplexStructure X) :
    (IsSymplectic α ∧ Tames α J) ↔
      (IsSmooth α ∧ IsClosed α ∧ Tames α J) := by
  constructor
  · rintro ⟨⟨hs, hc, _⟩, ht⟩
    exact ⟨hs, hc, ht⟩
  · rintro ⟨hs, hc, ht⟩
    exact ⟨⟨hs, hc, gcl_tames_implies_isNondegenerate α J ht⟩, ht⟩

/-- A self-contained metric symmetry identity, requiring precisely the
skewness and sign properties that an alternating two-form provides.

The next semantic step is to instantiate these algebraic hypotheses with
the actual ContinuousAlternatingMap upstream eval and J.square. -/
theorem gcl_invariant_iff_metric_symmetric_abstract
    {V : Type*} [AddGroup V] (ω : V → V → ℝ) (J : V → V)
    (skew : ∀ u v, ω u v = -ω v u)
    (neg_left : ∀ u v, ω (-u) v = -ω u v)
    (neg_right : ∀ u v, ω u (-v) = -ω u v)
    (square : ∀ u, J (J u) = -u) :
    (∀ u v, ω (J u) (J v) = ω u v) ↔
      (∀ u v, ω u (J v) = ω v (J u)) := by
  constructor
  · intro h u v
    have hi := h (J u) v
    rw [square u, neg_left u (J v), skew (J u) v] at hi
    exact neg_injective hi
  · intro h u v
    calc
      ω (J u) (J v) = ω v (J (J u)) := h (J u) v
      _ = ω v (-u) := by rw [square u]
      _ = -ω v u := neg_right v u
      _ = ω u v := by rw [skew v u]; simp


/-- On the Euclidean model space, exterior closedness survives any smooth
change of coordinates. This is the forward naturality direction of the
closedness bridge; it does NOT yet establish the manifold-level converse. -/
theorem gcl_extDeriv_zero_pullback_in_coordinates
    (ω : Space → Space [⋀^Fin 2]→L[ℝ] ℝ)
    (f : Space → Space) (y : Space)
    (hω : DifferentiableAt ℝ ω (f y))
    (hf : ContDiffAt ℝ ∞ f y)
    (hcl : extDeriv ω (f y) = 0) :
    extDeriv (fun z : Space =>
      (ω (f z)).compContinuousLinearMap (fderiv ℝ f z)) y = 0 := by
  rw [extDeriv_pullback hω hf le_top, hcl]
  simp

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_tames_implies_isNondegenerate
#print axioms OAI.TamingCompatibility.gcl_symplectic_and_tames_iff_smooth_closed_tames
#print axioms OAI.TamingCompatibility.gcl_invariant_iff_metric_symmetric_abstract
#print axioms OAI.TamingCompatibility.gcl_extDeriv_zero_pullback_in_coordinates
