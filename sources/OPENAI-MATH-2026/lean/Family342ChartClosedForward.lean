/-
Family-342 SEM-342-02: source-locked one-direction exterior derivative
bridge on actual upstream tangent two-forms. This theorem candidate
depends on the already accepted GCL chart extension and pullback
locality declarations. Its converse is not claimed.
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open scoped Manifold ContDiff Topology
open Set

variable {X : Type*} [TopologicalSpace X] [ChartedSpace Space X]
  [IsManifold Model ∞ X]

theorem gcl_isClosed_implies_chartwise
    (α : TwoForm X) (hα : IsClosed α) (x : X) :
    ∀ y ∈ (chartAt Space x).target,
      extDerivWithin (pullback α (chartAt Space x).symm)
        (chartAt Space x).target y = 0 := by
  intro y hy
  obtain ⟨f, hF, _hEq, hyBall⟩ :=
    gcl_exists_globalSmooth_chartInverse_extension x y hy
  let B : Set Space := Metric.ball y f.rIn
  have hB : B ∈ 𝓝 y := Metric.isOpen_ball.mem_nhds hyBall
  have hT : (chartAt Space x).target ∈ 𝓝 y :=
    (chartAt Space x).open_target.mem_nhds hy
  have hZero : extDerivWithin
      (pullback α (gcl_chartBumpExtension x y f)) B y = 0 :=
    hα (gcl_chartBumpExtension x y f) B Metric.isOpen_ball
      hF.contMDiffOn y hyBall
  have hEq : extDerivWithin
      (pullback α (gcl_chartBumpExtension x y f)) B y =
      extDerivWithin (pullback α (chartAt Space x).symm) B y :=
    extDerivWithin_congr'
      (gcl_chartBumpExtension_pullback_eqOn α x y f) hyBall
  have hDomain : extDerivWithin
      (pullback α (chartAt Space x).symm) B y =
      extDerivWithin (pullback α (chartAt Space x).symm)
        (chartAt Space x).target y := by
    simp [extDerivWithin, fderivWithin_of_mem_nhds hB,
      fderivWithin_of_mem_nhds hT]
  rw [hEq, hDomain] at hZero
  exact hZero

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_isClosed_implies_chartwise
