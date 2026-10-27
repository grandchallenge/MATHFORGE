# Family 342 native global chart inverse extension

**Lane:** `MF-OAI-MATH-2026-F342-SEM-006`  
**Exact source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Kernel:** Lean 4.34.1, Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.

## Completed proof target, conditional on exact Lean replay

The upstream semantic predicates test all globally defined `ContMDiffOn Model Model ∞` functions `F:Space→X`, but the intrinsic geometric chart inverse `ψ=(chartAt Space x).symm` is only smooth on its chart target.

A compactly supported smooth Euclidean bump `f:ContDiffBump y₀` has support on the outer ball `ball y₀ f.rOut`, lies in `[0,1]`, and equals one on the inner ball `ball y₀ f.rIn`. Set

\[
H(z)=y₀+f(z)(z-y₀), \qquad F(z)=\psi(H(z)).
\]

When `ball y₀ f.rOut ⊆ (chartAt Space x).target`, the previous bounded Euclidean cutoff argument proves `H(Space)` remains in this ball. Because the chart inverse is smooth on its target, `F` is globally smooth on all of `Space`. On the inner ball `f(z)=1`, so `F(z)=ψ(z)` and the derivatives agree locally.

The executable proof `sources/OPENAI-MATH-2026/lean/Family342ChartInverseExtension.lean` establishes, with native upstream types:

1. `gcl_chartBumpExtension_smooth`, `ContMDiff Model Model ∞ F`.
2. `gcl_chartBumpExtension_eqOn`, `EqOn F ψ (ball y₀ f.rIn)`.

**This claim is conditional on the job `semantic-342` compiling the source without `sorryAx` or nonpermitted axioms.** The declarations are not accepted based on this document alone.

## Constructive existence in any open chart image

The extended native Lean module additionally proves `gcl_exists_chartFittingBump`: every point in an open subset of `Space` has a `ContDiffBump` with outer support ball contained in that subset. It uses `Metric.isOpen_iff` to choose the outer radius and sets the inner radius to half of it.

The resulting `gcl_exists_globalSmooth_chartInverse_extension` asserts that for every point in the target of a chart, there exists a globally smooth map `F:Space→X` which agrees with the chart inverse on a **nonempty** Euclidean inner ball containing the chosen point. This is the exact global-chart-inverse extension that the original atlas-equivalence mathematical proof needs. The theorem is accepted only on a clean exact-source Lean replay.

## Remaining steps to full smoothness / closedness equivalence

1. **Global inverse chart extension:** completed by the new existential theorem, conditional on exact Lean replay.
2. **Pullback identity.** Use `EqOn F ψ` on the inner ball plus locality of `mfderiv` to prove equality of `pullback α F` and chartwise inverse-coordinate coefficients there.
3. **SEM-342-01.** Recover intrinsic smoothness from the globally quantified `IsSmooth α` via `F`; prove its converse by local smooth pullback in arbitrary charts.
4. **SEM-342-02.** Repeat using locality of `extDerivWithin` and the pinned `extDerivWithin_pullback`; explicitly require smoothness for the exterior derivative and verify overlap invariance.
5. **SEM-342-04.** Independently audit the manifold typeclass equivalence and absence of hidden extra hypotheses.

Unchanged assurance boundary: `SOURCE_LOCKED`, `MATHCERT_NOT_GRANTED`; the October 6 corrected cone theorem is not certified by the family-342 Comparator. The article-level geometric result and these semantic-admission obligations must not be conflated.
