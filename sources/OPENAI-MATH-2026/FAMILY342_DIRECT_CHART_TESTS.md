# Family 342: direct open-domain chart tests

**Scope:** Narrow proof simplification of SEM-342-01 and SEM-342-02 forward directions, retaining theorem names and pinned upstream definitions.

**Upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`; Lean 4.34.1 and repository-locked Mathlib.

## Exact semantic observation

The source predicates `IsSmooth α` and `IsClosed α` universally quantify over functions `f : Space → X` and open sets `U`, but require `ContMDiffOn ... f U`, not `ContMDiff ... f` globally. An inverse chart `(chartAt Space x).symm` is already a total term of type `Space → X`, and Mathlib's `contMDiffOn_chart_symm` proves it is smooth on `(chartAt Space x).target`.

Both forward theorems are therefore direct instances of the upstream predicates. Replacing their bodies removes the otherwise unnecessary cutoff existence, local derivative/pullback equality, and exterior derivative domain comparison *from the forward theorem dependency chains*. Those earlier constructions remain valid independently proved results and are **not** erased or downgraded.

The source-locked replay now compiles each direct proof standalone in addition to the retained composite checks. The explicit `#print axioms` declarations must show no `sorryAx`. CI and protected merge/readback are required before the revised proof is admitted.

## Claim boundary

This simplification proves **only**:
- upstream `IsSmooth α` implies smooth coordinate pullback coefficients in each inverse chart;
- upstream `IsClosed α` implies zero coordinate exterior derivative on each chart target.

It does not prove either converse. SEM-342-04 still requires exact correspondence of source's typed smooth manifolds and intrinsic differential geometry. No conclusion is drawn about Donaldson's conjecture, corrected cone theorems, the October manuscript, source assurance or MATHCERT.

**Next mathematical work:** establish a chartwise-to-universal pullback smoothness theorem, with the correct `mfderiv` chain rule and smooth dependence of the `ContinuousAlternatingMap` composition; then chartwise-to-universal exterior closedness on smooth forms using `extDerivWithin` pullback naturality. Distinguish these substantive theorems from the now trivial forward tests.
