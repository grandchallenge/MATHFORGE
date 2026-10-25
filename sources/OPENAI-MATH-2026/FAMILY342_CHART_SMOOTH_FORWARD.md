# Family 342: upstream smoothness implies smooth coefficients in every chart

**Proof lane:** `MF-OAI-MATH-2026-F342-SEM-009`  
**Protected predecessor:** `grandchallenge/MATHFORGE@b9ffa9f6f396627d9ffd8fac327934948be04b54`  
**Upstream source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Lean:** `leanprover/lean4:v4.34.1`; pinned Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.

The exact upstream definition of `IsSmooth α` quantifies over globally defined smooth maps `f : Space → X`, and requires `ContDiffOn ℝ ∞ (pullback α f) U` for each open smooth test domain `U`.

The formal theorem candidate `gcl_isSmooth_implies_chartwise` establishes, for any raw tangent two-form `α : TwoForm X` and every actual manifold chart `chartAt Space x`, that

```lean
IsSmooth α →
  ContDiffOn ℝ ∞ (pullback α (chartAt Space x).symm)
    (chartAt Space x).target
```

The proof uses the protected global chart-extension existence theorem from #324 and the derivative/pullback locality theorems from #325. At each point of the chart target, it obtains a globally smooth extension `F` of the local chart inverse on a positive-radius inner ball. Applying upstream `IsSmooth` to `F`, restricting to the local intersection, and using pullback equality proves local chart smoothness. `contDiffOn_of_locally_contDiffOn` assembles the result over the entire chart target.

**Acceptance boundary:** No kernel-accepted theorem is claimed until the exact-source `semantic-342` replay succeeds on the candidate PR head and prints an axiom list without `sorryAx`. The proof pipeline separately source-hashes all three GCL inputs (native chart extension, pullback locality, and smoothness implication), and retains the exact generated composite.

**Still open:** The converse implication (smooth chartwise coefficients imply upstream universal-test `IsSmooth`), the bidirectional manifold exterior closedness theorem under smoothness, full manifold category/hypothesis correspondence, corrected cone theorem semantics, and manuscript-level certification. Source assurance remains `SOURCE_LOCKED`; `MATHCERT` remains `NOT_GRANTED`.
