# Family 342: atlas-level equivalence theorem for the upstream differential-form tests

**Work package:** `MF-OAI-MATH-2026-F342-SEM-004`  
**Provenance:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a` with Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.  
**Status:** Detailed ordinary mathematical argument. **NOT** a Lean-accepted theorem; the native chart-extension construction and the two formal equivalences remain open until compiled and replayed.  
**Scope:** The smoothness and closedness predicates in `lean/OAI/Geometry/TamingCompatibility/Model.lean`, not the main existence theorem or the October cone theorem.

## 1. Exact objects being compared

Let \(X\) be a smooth four-manifold modelled on \(E=\mathbb R^4\). Let \(\alpha\) be a pointwise alternating continuous bilinear form on each tangent space \(T_xX\). Do **not** assume smoothness of the map \(x\mapsto\alpha_x\) at this stage.

The upstream Lean model names the section `TwoForm X`; it defines `pullback α f` using `mfderiv Model Model f y` on both arguments. The domain of each test is a globally defined function `f : Space → X`, whose restriction to an open `U ⊆ Space` is `ContMDiffOn Model Model ∞`. The two predicates are:

- `IsSmooth α`: for every such `f,U`, `ContDiffOn ℝ ∞ (pullback α f) U`.
- `IsClosed α`: for every such `f,U` and `y∈U`, `extDerivWithin (pullback α f) U y = 0`.

By **atlas-smooth**, we mean: for every smooth chart \(\phi:V\to W\subset E\), the local two-form \(A_\phi=(\phi^{-1})^*\alpha:W\to\operatorname{Alt}^2(E;\mathbb R)\) is \(C^\infty\). By **atlas-closed**, we mean: an atlas-smooth \(\alpha\) has \(d A_\phi=0\) on every chart image \(W\), using the usual Euclidean exterior derivative.

The latter are intrinsic notions because smooth transition maps obey exterior-derivative naturality. This text proves their equivalence **mathematically**, including the nontrivial global-test-versus-local-chart mismatch; it does not claim an available bundled Mathlib manifold differential-form API.

## 2. Local-to-global chart inverse extension lemma

**Lemma E (smooth global test extension).** Let \(\phi:V\to W\) be a smooth chart from \(X\) to an open subset of \(E\), with smooth local inverse \(\psi:W\to V\subset X\). For any \(y_0\in W\), there exist open neighborhoods \(B\ni y_0\) and \(D\ni y_0\), with \(\overline B\subset D\), \(D\) an open convex ball contained in \(W\), and a globally defined smooth map \(F:E\to X\) such that \(F|_B=\psi|_B\).

**Proof.** Choose concentric Euclidean balls \(B\Subset D\Subset W\) about \(y_0\). Take a smooth bump \(\chi:E\to[0,1]\), identically 1 on \(B\), with compact support inside \(D\). Define a global coordinate map

\[
H(z)=y_0+\chi(z)(z-y_0),\qquad z\in E.
\]

If \(z\notin\operatorname{supp}\chi\), then \(H(z)=y_0\in D\). If \(z\in\operatorname{supp}\chi\subset D\), both \(y_0\) and \(z\) are in the convex ball \(D\), hence their convex combination \(H(z)\) belongs to \(D\). Thus \(H(E)\subset D\subset W\), and \(F=\psi\circ H:E\to X\) is globally defined and smooth. On \(B\), \(\chi=1\), so \(H(z)=z\) and \(F(z)=\psi(z)\). \(\square\)

This lemma uses a smooth cutoff **only on Euclidean coordinate space**, not a global partition of unity on \(X\), nor compactness or connectedness of \(X\). The pinned Mathlib revision includes Euclidean smooth-bump existence (`Mathlib/Analysis/Calculus/BumpFunction/FiniteDimension.lean`) and smooth chart inverses (`Mathlib/Geometry/Manifold/ContMDiff/Atlas.lean`). The formal construction must show \(H(E)\subset W\), and derive smoothness by composition with the locally smooth chart inverse.

## 3. Atlas smoothness if and only if the upstream test predicate

**Theorem S.** For a pointwise alternating tangent two-form \(\alpha\), the following are equivalent:

1. `IsSmooth α` according to the pinned upstream definition.
2. \(\alpha\) is atlas-smooth in the sense of Section 1.

**(1 ⇒ 2).** Fix a smooth chart \(\phi:V\to W\) and \(y_0\in W\). Lemma E supplies a globally defined smooth \(F:E\to X\) coinciding with \(\psi=\phi^{-1}\) on a neighborhood \(B\ni y_0\). In particular, \(F\) is an admissible upstream test map on \(B\). The test predicate implies \(F^*\alpha\) is smooth on \(B\).

On \(B\), \(F=\psi\). Their ordinary derivatives and manifold derivatives agree there by locality, so \(F^*\alpha=\psi^*\alpha=A_\phi\) on \(B\). Consequently \(A_\phi\) is smooth near \(y_0\). Since \(y_0\) was arbitrary, \(A_\phi\) is smooth on \(W\). Repeat over every chart.

**(2 ⇒ 1).** Let \(f:E\to X\) be any globally defined map smooth on an open \(U\subseteq E\); outside \(U\), impose no hypothesis. Let \(y_0\in U\). Choose a smooth chart \(\phi:V\to W\) around \(f(y_0)\). By continuity of \(f|_U\), there is an open \(B\ni y_0\), \(B\subset U\), with \(f(B)\subset V\). Set \(h=\phi\circ f:B\to W\). This is smooth on \(B\). On \(B\),

\[
f^*\alpha=h^*((\phi^{-1})^*\alpha)=h^* A_\phi.
\]

The chart coefficients \(A_\phi\) are smooth by hypothesis. Smoothness of a pullback of a smooth alternating tensor by a smooth map is a standard finite-dimensional chain-rule calculation, hence \(f^*\alpha\) is smooth on \(B\). Such \(B\) cover \(U\), implying `ContDiffOn ℝ ∞ (pullback α f) U`. This is precisely `IsSmooth α`. \(\square\)

**Formal proof obligations:** (i) construct Lemma E in Lean using `chartAt`, `contMDiffOn_chart_symm` and a smooth cutoff; (ii) transfer `mfderiv` under equality of maps on neighborhoods; (iii) prove smoothness of the alternating-map pullback under the `ContMDiffOn` composition rules; (iv) combine local regularity over an open cover. Neither implication is claimed kernel-checked today.

## 4. Atlas closedness if and only if the upstream test predicate

**Theorem C.** Assuming the equivalent smoothness hypotheses of Theorem S, these are equivalent:

1. `IsClosed α` according to the pinned upstream definition.
2. \(dA_\phi=0\) on the image of every smooth chart \(\phi\).

**(1 ⇒ 2).** Fix a chart, point \(y_0\in W\), and globally smooth extension \(F\) agreeing with \(\psi\) on \(B\), as in Lemma E. The upstream test gives \(\operatorname{extDerivWithin}(F^*\alpha,B,y)=0\) for all \(y\in B\). Since \(B\) is open and \(F^*\alpha\) is smooth there (Theorem S), this is the usual Euclidean exterior derivative \(d(F^*\alpha)=0\) on \(B\). Local equality \(F=\psi\) implies equality of their pullbacks on \(B\), hence \(dA_\phi=0\) on \(B\). Cover \(W\) by such neighborhoods.

**(2 ⇒ 1).** Fix an upstream test \((f,U)\). Near each \(y_0\in U\), choose a chart \(\phi\) around \(f(y_0)\), and restrict to \(B\subseteq U\) with \(f(B)\subseteq V\). On \(B\), \(f^*\alpha=h^*A_\phi\) for \(h=\phi\circ f\). Because \(A_\phi\) is smooth and closed, the naturality of the exterior derivative yields

\[
d(f^*\alpha)=d(h^*A_\phi)=h^*(dA_\phi)=0
\]

on \(B\). This implies \(\operatorname{extDerivWithin}(f^*\alpha,U,y_0)=0\) because the derivative depends only on a neighborhood of \(y_0\). Every \(y_0\in U\) was arbitrary. Therefore `IsClosed α`. \(\square\)

**Exact supporting kernel material:** the pinned Mathlib `Mathlib/Analysis/Calculus/DifferentialForm/Basic.lean` provides `extDeriv_pullback`, `extDerivWithin_pullback`, and locality lemmas for `extDerivWithin`. The protected GCL native declaration `gcl_extDeriv_zero_pullback_in_coordinates` replays the forward Euclidean naturality statement. The remaining chart-extension, chart transition and tangent `mfderiv` identifications must still be established in Lean before Theorem C can be admitted as a formal semantic bridge.

## 5. Consequences for the main theorem and retained boundary

Theorems S and C make explicit why the upstream universal test-map formulation is **mathematically aligned** with ordinary smooth and closed differential two-forms, conditional on the stated standard manifold calculus facts. They do not establish correctness of the source manuscript's long geometric argument.

The term `IsSymplectic α` also requires `IsNondegenerate α`; the previously protected `gcl_tames_implies_isNondegenerate` proves that this conjunct adds nothing in the presence of `Tames α J`.

**Dispositions:**

- `ATLAS_BRIDGE_MATHEMATICAL_ARGUMENT_COMPLETE_WITH_LISTED_LEMMAS`: the mathematical reductions, hypotheses, and equations are recorded above.
- `SEM342_01_INTRINSIC_SMOOTHNESS_KERNEL_OPEN`: bidirectional Lean proof not run.
- `SEM342_02_INTRINSIC_CLOSEDNESS_KERNEL_OPEN`: bidirectional Lean proof not run.
- `SEM342_03_NATIVE_METRIC`: read only the exact-head Lean receipt from the separate, protected native metric work, not from this document.
- `SEM342_04_MANIFOLD_MODEL_EQUIVALENCE_OPEN`: still requires separate theorem/hypothesis audit.
- `MATHCERT_NOT_GRANTED`, `PROVIDER_SOURCE_LOCKED`, `CONE_THEOREM_NOT_COVERED`: unchanged.

**Next executable theorem:** formalize Lemma E as a reusable `smooth_global_chart_extension` with a strict source-pinned test; follow it with the two exact `mfderiv`/pullback locality bridges and then a two-direction theorem for S and C. This is an evidentiary and engineering proof obligation, not a request for Human Steward intervention.
