/-
OpenAI Math family 342, SEM-342-01: direct forward chart test.

The upstream IsSmooth predicate only requires f to be smooth on the
specified open U. The chart inverse is a globally typed map Space → X,
and is smooth on its target. A bump extension is unnecessary for this
forward implication. Converse smoothness remains open.

Source: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open scoped Manifold ContDiff Topology
open Set

variable {X : Type*} [TopologicalSpace X] [ChartedSpace Space X]
  [IsManifold Model ∞ X]

/-- The upstream open-domain test directly includes every inverse chart. -/
theorem gcl_isSmooth_implies_chartwise
    (α : TwoForm X) (hα : IsSmooth α) (x : X) :
    ContDiffOn ℝ ∞ (pullback α (chartAt Space x).symm)
      (chartAt Space x).target := by
  exact hα (chartAt Space x).symm (chartAt Space x).target
    (chartAt Space x).open_target contMDiffOn_chart_symm

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_isSmooth_implies_chartwise
