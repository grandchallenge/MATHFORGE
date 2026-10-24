/-
OpenAI Math 2026 family 342, the next SEM-342-01/02 bridge:
construct a genuinely manifold-valued global test map agreeing with a
smooth inverse chart on a smaller coordinate ball.

This imports the cutoff interpolation lemma compiled at the previous
bounded stage (same pinned source tree and Lean 4.34.1).
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open scoped Manifold ContDiff
open Set

variable {X : Type*} [TopologicalSpace X] [ChartedSpace Space X]
  [IsManifold Model ∞ X]

noncomputable def gcl_chartBumpExtension
    (x : X) (y₀ : Space) (f : ContDiffBump y₀) : Space → X :=
  (chartAt Space x).symm ∘
    (fun z => y₀ + f z • (z - y₀))

/-- The smooth inverse of a manifold chart, composed with a global
Euclidean cutoff interpolation mapping into the chart's target,
is a globally defined smooth manifold-valued map. -/
theorem gcl_chartBumpExtension_smooth
    (x : X) (y₀ : Space) (f : ContDiffBump y₀)
    (hfit : Metric.ball y₀ f.rOut ⊆ (chartAt Space x).target) :
    ContMDiff Model Model ∞ (gcl_chartBumpExtension x y₀ f) := by
  have hψ : ContMDiffOn Model Model ∞
      (chartAt Space x).symm (chartAt Space x).target :=
    contMDiffOn_chart_symm
  have hH : ContDiff ℝ ∞ (fun z : Space => y₀ + f z • (z - y₀)) :=
    contDiff_const.add (f.contDiff.smul (contDiff_id.sub contDiff_const))
  have hRange : ∀ z : Space,
      (y₀ + f z • (z - y₀)) ∈ (chartAt Space x).target := by
    intro z
    apply hfit
    have hd : Convex ℝ (Metric.ball y₀ f.rOut) := convex_ball y₀ f.rOut
    by_cases hz : z ∈ Metric.ball y₀ f.rOut
    · exact hd.add_smul_sub_mem (Metric.mem_ball_self f.rOut_pos)
        hz ⟨f.nonneg, f.le_one⟩
    · have hzero : f z = 0 := by
        by_contra hn
        have hs : z ∈ Function.support f := hn
        rw [f.support_eq] at hs
        exact hz hs
      have hcenter : y₀ ∈ Metric.ball y₀ f.rOut :=
        Metric.mem_ball_self f.rOut_pos
      simpa [hzero] using hcenter
  exact hψ.comp_contMDiff hH.contMDiff hRange

/-- The global map agrees with the true inverse chart on the bump's
inner ball, so it is a valid replacement in local tensor pullback tests. -/
theorem gcl_chartBumpExtension_eqOn
    (x : X) (y₀ : Space) (f : ContDiffBump y₀) :
    EqOn (gcl_chartBumpExtension x y₀ f)
      (chartAt Space x).symm (Metric.ball y₀ f.rIn) := by
  intro z hz
  have hχ : f z = 1 := f.one_of_mem_closedBall
    (Metric.mem_closedBall.mpr (le_of_lt (Metric.mem_ball.mp hz)))
  simp [gcl_chartBumpExtension, hχ]

/-- Every point of an open Euclidean chart image admits a packaged
smooth cutoff whose outer support ball is contained in the image. -/
theorem gcl_exists_chartFittingBump
    (W : Set Space) (hW : IsOpen W)
    (y₀ : Space) (hy₀ : y₀ ∈ W) :
    ∃ f : ContDiffBump y₀, Metric.ball y₀ f.rOut ⊆ W := by
  obtain ⟨r, hr, hball⟩ := Metric.isOpen_iff.mp hW y₀ hy₀
  let f : ContDiffBump y₀ :=
    { rIn := r / 2
      rOut := r
      rIn_pos := half_pos hr
      rIn_lt_rOut := half_lt_self hr }
  exact ⟨f, hball⟩

/-- A smooth global manifold-valued extension of each local chart inverse
exists at every point of the open target; it agrees with the inverse on a
nonempty inner neighborhood. No global chart inverse is assumed. -/
theorem gcl_exists_globalSmooth_chartInverse_extension
    (x : X) (y₀ : Space)
    (hy₀ : y₀ ∈ (chartAt Space x).target) :
    ∃ (f : ContDiffBump y₀),
      ContMDiff Model Model ∞ (gcl_chartBumpExtension x y₀ f) ∧
      EqOn (gcl_chartBumpExtension x y₀ f)
        (chartAt Space x).symm (Metric.ball y₀ f.rIn) ∧
      y₀ ∈ Metric.ball y₀ f.rIn := by
  obtain ⟨f, hfit⟩ := gcl_exists_chartFittingBump
    (chartAt Space x).target (chartAt Space x).open_target y₀ hy₀
  refine ⟨f, gcl_chartBumpExtension_smooth x y₀ f hfit,
    gcl_chartBumpExtension_eqOn x y₀ f, ?_⟩
  exact Metric.mem_ball_self f.rIn_pos

#print axioms OAI.TamingCompatibility.gcl_exists_chartFittingBump
#print axioms OAI.TamingCompatibility.gcl_exists_globalSmooth_chartInverse_extension

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_chartBumpExtension_smooth
#print axioms OAI.TamingCompatibility.gcl_chartBumpExtension_eqOn
