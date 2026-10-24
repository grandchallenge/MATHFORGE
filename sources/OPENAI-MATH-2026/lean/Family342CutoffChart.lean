/-
Family 342: exact Euclidean cutoff interpolation for chart inverse extension.

Proves a reusable and constructive first stage of SEM-342-01/02.
It makes no assumption that a globally defined smooth chart inverse exists.
This is not yet a proof of manifold-valued smooth chart extension.
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open Set
open scoped Manifold ContDiff

/-- The Euclidean interpolation used to extend a local chart inverse.

For a smooth cutoff χ supported in convex chart ball D about y₀,
this map remains within D and equals the identity wherever χ=1.
-/
noncomputable def gcl_cutoffInterpolation
    (y₀ : Space) (χ : Space → ℝ) : Space → Space :=
  fun z => y₀ + χ z • (z - y₀)

/-- A cutoff interpolation never leaves its convex chart ball when its
cutoff is supported there, takes values in [0,1], and the center lies
in that ball. The bound is global, not merely near the chart center. -/
theorem gcl_cutoffInterpolation_mapsTo
    (y₀ : Space) (χ : Space → ℝ)
    (D : Set Space) (hD : Convex ℝ D) (hy₀ : y₀ ∈ D)
    (hχrange : ∀ z, χ z ∈ Icc (0 : ℝ) 1)
    (hχoutside : ∀ z, z ∉ D → χ z = 0) :
    MapsTo (gcl_cutoffInterpolation y₀ χ) univ D := by
  intro z _
  by_cases hz : z ∈ D
  · exact hD.add_smul_sub_mem hy₀ hz (hχrange z)
  · simp [gcl_cutoffInterpolation, hχoutside z hz, hy₀]

/-- Infinitely differentiable cutoff gives infinitely differentiable
interpolation on all of Euclidean space. -/
theorem gcl_cutoffInterpolation_smooth
    (y₀ : Space) (χ : Space → ℝ)
    (hχ : ContDiff ℝ ∞ χ) :
    ContDiff ℝ ∞ (gcl_cutoffInterpolation y₀ χ) := by
  unfold gcl_cutoffInterpolation
  exact contDiff_const.add (hχ.smul (contDiff_id.sub contDiff_const))

/-- Whenever the cutoff is 1, the interpolation is the identity. -/
theorem gcl_cutoffInterpolation_eq_self
    (y₀ : Space) (χ : Space → ℝ) (z : Space)
    (hz : χ z = 1) :
    gcl_cutoffInterpolation y₀ χ z = z := by
  simp [gcl_cutoffInterpolation, hz]

/-- All ingredients necessary for using the interpolated map as a
globally smooth input to a local chart inverse, stated without any
implicit extension theorem for manifold-valued functions. -/
theorem gcl_cutoffInterpolation_chart_core
    (y₀ : Space) (χ : Space → ℝ)
    (D B : Set Space) (hD : Convex ℝ D) (hy₀ : y₀ ∈ D)
    (hχrange : ∀ z, χ z ∈ Icc (0 : ℝ) 1)
    (hχoutside : ∀ z, z ∉ D → χ z = 0)
    (hχone : ∀ z ∈ B, χ z = 1)
    (hχ : ContDiff ℝ ∞ χ) :
    ContDiff ℝ ∞ (gcl_cutoffInterpolation y₀ χ) ∧
      MapsTo (gcl_cutoffInterpolation y₀ χ) univ D ∧
      EqOn (gcl_cutoffInterpolation y₀ χ) id B := by
  refine ⟨gcl_cutoffInterpolation_smooth y₀ χ hχ,
    gcl_cutoffInterpolation_mapsTo y₀ χ D hD hy₀ hχrange hχoutside, ?_⟩
  intro z hz
  exact gcl_cutoffInterpolation_eq_self y₀ χ z (hχone z hz)

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_cutoffInterpolation_mapsTo
#print axioms OAI.TamingCompatibility.gcl_cutoffInterpolation_smooth
#print axioms OAI.TamingCompatibility.gcl_cutoffInterpolation_eq_self
#print axioms OAI.TamingCompatibility.gcl_cutoffInterpolation_chart_core
