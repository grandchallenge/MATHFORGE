# Family 342 semantic bridge: chart-local equivalence and native metric audit

**Lane:** MF-OAI-MATH-2026-F342-SEM-003
**Source lock:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`; Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`; Lean `leanprover/lean4:v4.34.1`.
**Protected predecessor:** MATHFORGE `d317412e60ce065a41cd83ec1affac692b7c5f1c`.

## Distinguish the semantic representations

The paper uses an intrinsic smooth differential two-form \(\alpha\) on the four-manifold \(X\), with \(d\alpha=0\). The Lean model instead defines a *raw* section

```lean
abbrev TwoForm (X : Type*) [TopologicalSpace X] [ChartedSpace Space X] :=
  (x : X) → (TangentSpace Model x) [⋀^Fin 2]→L[ℝ] ℝ
```

and tests `IsSmooth` and `IsClosed` on pullbacks by all globally defined maps `f : Space → X` that are smooth on some open set `U : Set Space`. The word **globally** matters: a chart inverse is ordinarily only defined on a proper open subset of `Space`, so it cannot simply be substituted as `f` without first extending it. Prior source-only review was correct not to assume this extension.

### SEM-342-01, exact chart-extension obligation

For each manifold chart \(\phi : V\subseteq X \to W\subseteq\mathbb R^4\) and each \(y_0\in W\), construct an open Euclidean ball \(B\ni y_0\) with closure inside a convex ball \(D\subseteq W\), together with a smooth globally defined \(F:\mathbb R^4\to X\) satisfying \(F(z)=\phi^{-1}(z)\) for \(z\in B\).

One explicit construction uses a smooth bump \(\chi:\mathbb R^4\to[0,1]\), supported in \(D\), with \(\chi=1\) on \(B\), and defines the interpolating coordinate \(H(z)=y_0+\chi(z)(z-y_0)\) on \(D\). Outside \(D\), set \(F(z)=\phi^{-1}(y_0)\); inside \(D\), set \(F(z)=\phi^{-1}(H(z))\). Because \(\chi=0\) near the boundary, the branches glue smoothly. On \(B\), \(H(z)=z\).

**Formal work required:** a Mathlib proof of this smooth global extension using the pinned manifold `ChartedSpace` / `IsManifold` API and Euclidean smooth bump API, including the equalities of `mfderiv` of \(F\) and the local chart inverse where the functions agree. Then `IsSmooth α` entails smoothness of \(\phi_* \alpha\) on \(B\), by restricting the universal test to \(F\); cover \(W\) by these balls. Conversely, local smooth chart coefficients must imply smooth pullbacks along arbitrary `f` smooth on `U`.

The final equivalence is **OPEN** until both implications compile on the exact upstream model, and the coordinate regularity definition is independently admitted as representing the usual intrinsic smooth two-forms.

### SEM-342-02, exact closedness obligation

The pinned Mathlib `Mathlib/Analysis/Calculus/DifferentialForm/Basic.lean` defines `extDeriv` using alternation of Fréchet derivatives, and proves `extDeriv_pullback` and `extDerivWithin_pullback`. The prior GCL proof `gcl_extDeriv_zero_pullback_in_coordinates` already verifies the **forward** zero-derivative naturality on Euclidean coordinate maps.

For the manifold bridge, establish:

1. Equality of the `pullback α F` section to the local chart-coefficient form on the ball \(B\), using the chart-extension \(F\).
2. Equality of `extDerivWithin` for the locally agreeing smooth forms on \(B\), and equivalence to the usual coordinate exterior derivative.
3. Coordinate change invariance by `extDerivWithin_pullback`, with its exact `ContDiffWithinAt`, `UniqueDiffOn` and mapping-to-open-set hypotheses discharged by local diffeomorphisms.
4. Bidirectional correspondence between `IsClosed α` and chartwise \(d\alpha=0\) under `IsSmooth α`. For the converse, local chart vanishing and pullback naturality imply every global-test `f` satisfies `IsClosed`.

These steps are not implied merely by the existence of the `extDeriv_pullback` library theorem. Formal check is still **OPEN**.

### SEM-342-03, native metric instantiation

`sources/OPENAI-MATH-2026/lean/Family342NativeMetric.lean` proves signed alternation for the actual `TwoForm X` sections, uses `J.square` from the exact `AlmostComplexStructure`, and derives

\[
\operatorname{IsInvariant}(\alpha,J)
\iff
\forall x,u,v,\quad
\alpha_x(u,J_xv)=\alpha_x(v,J_xu).
\]

It also derives the exact equivalence

\[
\operatorname{Compatible}(\alpha,J)
\iff
\bigl[\text{pairing }\alpha(u,Jv)\text{ is symmetric and strictly positive on }v\ne0\bigr].
\]

**Acceptance rule:** assert this only if the new Lean module passes with no `sorryAx` or other additional axioms. This establishes the pointwise positive symmetric bilinear datum of a Hermitian metric on each tangent space. Smoothness of the metric and global equivalence to a Riemannian metric are still contingent on SEM-342-01, plus smoothness of the almost-complex structure already supplied by `AlmostComplexStructure.smooth`.

### SEM-342-04, manifold hypotheses

Review `[T2Space X]`, `[SecondCountableTopology X]`, `[CompactSpace X]`, `[ConnectedSpace X]`, `[ChartedSpace Space X]`, `[IsManifold Model ∞ X]` against the article's closed, connected, smooth four-manifold statement. Establish both constructions across the intended mathematical category with no hidden orientation or integrability assumptions. This remains **OPEN**.

## Nonpromotion rule

This tranche is a proof/refinement of sublemmas, not yet the bidirectional manifold form semantics theorem. The family-342 Comparator acceptance and prior protected Lean checks remain distinct. The source catalog stays `SOURCE_LOCKED`; no paper-level approval, novelty adjudication, cone theorem verification, or MATHCERT certification is authorized.

**Next decisive unit after native metric replay:** formalize the compact-support Euclidean bump extension to a globally defined smooth manifold-valued test map and prove chartwise pullback agreement; use that lemma for both SEM-342-01 and SEM-342-02, rather than duplicating infrastructure.
