/-
OpenAI Math family 342, SEM-342-01 forward implication.

The upstream universal smooth-test predicate entails C∞ local chart
coefficients for any raw TwoForm X. This is a source-locked theorem
on actual upstream types, relying on the previously proved globally
smooth inverse-chart extension and exact tensor pullback locality.

The converse smoothness implication and closedness bridge remain open.
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open scoped Manifold ContDiff Topology
open Set

variable {X : Type*} [TopologicalSpace X] [ChartedSpace Space X]
  [IsManifold Model ∞ X]

/-- The upstream globally quantified IsSmooth predicate implies
ordinary C∞ chart coefficients on each inverse chart target. -/
theorem gcl_isSmooth_implies_chartwise
    (α : TwoForm X) (hα : IsSmooth α) (x : X) :
    ContDiffOn ℝ ∞ (pullback α (chartAt Space x).symm)
      (chartAt Space x).target := by
  apply contDiffOn_of_locally_contDiffOn
  intro y hy
  obtain ⟨f, hF, _hEq, hyBall⟩ :=
    gcl_exists_globalSmooth_chartInverse_extension x y hy
  refine ⟨Metric.ball y f.rIn, Metric.isOpen_ball, hyBall, ?_⟩
  have hGlobal : ContDiffOn ℝ ∞
      (pullback α (gcl_chartBumpExtension x y f))
      (Metric.ball y f.rIn) :=
    hα (gcl_chartBumpExtension x y f) (Metric.ball y f.rIn)
      Metric.isOpen_ball hF.contMDiffOn
  apply (hGlobal.mono Set.inter_subset_right).congr
  intro z hz
  exact (gcl_chartBumpExtension_pullback_eqOn α x y f hz.2).symm

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_isSmooth_implies_chartwise
