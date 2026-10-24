/-
OpenAI Math family 342, SEM-342-01/02: the exact local derivative
and differential-two-form pullback consequences of the global chart
extension. No manifold smoothness/closedness equivalence is claimed here.

Upstream: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
Lean: leanprover/lean4:v4.34.1
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open scoped Manifold ContDiff Topology
open Set

variable {X : Type*} [TopologicalSpace X] [ChartedSpace Space X]
  [IsManifold Model ∞ X]

/-- On the inner bump ball, the globally smooth extension and the chart
inverse have identical manifold derivatives. The derivative equality
uses locality, not a synthetic computation of the Jacobian. -/
theorem gcl_chartBumpExtension_mfderiv_eq
    (x : X) (y₀ : Space) (f : ContDiffBump y₀)
    (z : Space) (hz : z ∈ Metric.ball y₀ f.rIn) :
    @Eq (Space →L[ℝ] Space)
      (mfderiv Model Model (gcl_chartBumpExtension x y₀ f) z)
      (mfderiv Model Model (chartAt Space x).symm z) := by
  have hlocal : gcl_chartBumpExtension x y₀ f =ᶠ[𝓝 z]
      (chartAt Space x).symm := by
    filter_upwards [Metric.isOpen_ball.mem_nhds hz] with w hw
    have hχ : f w = 1 := f.one_of_mem_closedBall
      (Metric.mem_closedBall.mpr (le_of_lt (Metric.mem_ball.mp hw)))
    simp [gcl_chartBumpExtension, hχ]
  have h := Filter.EventuallyEq.mfderiv_eq hlocal
  have hp : gcl_chartBumpExtension x y₀ f z =
      (chartAt Space x).symm z :=
    gcl_chartBumpExtension_eqOn x y₀ f hz
  rw [hp] at h
  simpa using h

/-- The raw two-form pullback along the global chart extension agrees
on the inner ball with the local inverse-chart coefficients, for every
pointwise alternating tangent 2-form, *without* assuming its smoothness. -/
theorem gcl_chartBumpExtension_pullback_eqOn
    (α : TwoForm X) (x : X) (y₀ : Space)
    (f : ContDiffBump y₀) :
    EqOn (pullback α (gcl_chartBumpExtension x y₀ f))
      (pullback α (chartAt Space x).symm)
      (Metric.ball y₀ f.rIn) := by
  intro z hz
  have hp : gcl_chartBumpExtension x y₀ f z =
      (chartAt Space x).symm z :=
    gcl_chartBumpExtension_eqOn x y₀ f hz
  have hd := gcl_chartBumpExtension_mfderiv_eq x y₀ f z hz
  simp only [pullback]
  rw [hp]
  rw [hd]

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_chartBumpExtension_mfderiv_eq
#print axioms OAI.TamingCompatibility.gcl_chartBumpExtension_pullback_eqOn
