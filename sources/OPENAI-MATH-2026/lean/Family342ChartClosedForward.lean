/-
OpenAI Math family 342, SEM-342-02: direct forward chart closedness.

The upstream IsClosed predicate quantifies over globally typed test maps
that are smooth on the specified open domain; the partial chart inverse
is itself such a test map on its chart target. Therefore the forward
chartwise exterior-derivative result is an instance of the definition.
No converse or manifold-model equivalence is claimed.

Source: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
-/
import OAI.Geometry.TamingCompatibility.Model

namespace OAI.TamingCompatibility
open scoped Manifold ContDiff Topology
open Set

variable {X : Type*} [TopologicalSpace X] [ChartedSpace Space X]
  [IsManifold Model ∞ X]

/-- Upstream IsClosed directly includes each inverse chart's open target. -/
theorem gcl_isClosed_implies_chartwise
    (α : TwoForm X) (hα : IsClosed α) (x : X) :
    ∀ y ∈ (chartAt Space x).target,
      extDerivWithin (pullback α (chartAt Space x).symm)
        (chartAt Space x).target y = 0 := by
  exact hα (chartAt Space x).symm (chartAt Space x).target
    (chartAt Space x).open_target contMDiffOn_chart_symm

end OAI.TamingCompatibility

#print axioms OAI.TamingCompatibility.gcl_isClosed_implies_chartwise
