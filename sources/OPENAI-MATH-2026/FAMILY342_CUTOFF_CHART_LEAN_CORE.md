# Family 342: first Lean-checked chart-extension component

**Lane:** `MF-OAI-MATH-2026-F342-SEM-005`  
**Upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Toolchain:** `leanprover/lean4:v4.34.1`  
**Baseline protected head:** `b19f3d3ff54da47134b39f2e20963269862011e3`.

## Problem and bounded proof

The remaining SEM-342-01/02 issue is that the source `IsSmooth` and `IsClosed` predicates quantify over maps `f : Space → X` defined globally; standard manifold inverse charts are defined only on an open Euclidean chart image `D`.

The ordinary mathematical argument in `FAMILY342_ATLAS_EQUIVALENCE_MATH_PROOF.md` extends an inverse chart near a point `y₀` using a smooth cutoff `χ`:

\[
H(z)=y₀+χ(z)(z-y₀).
\]

The new Lean file `sources/OPENAI-MATH-2026/lean/Family342CutoffChart.lean` implements exactly this Euclidean interpolating map and five theorems:

- `gcl_cutoffInterpolation_mapsTo`: for convex `D` containing `y₀`, a cutoff `χ∈[0,1]` vanishing outside `D` gives `H(\mathbb R^4)⊆D`.
- `gcl_cutoffInterpolation_smooth`: if `χ` is `C∞`, so is `H`.
- `gcl_cutoffInterpolation_eq_self`: if `χ(z)=1`, then `H(z)=z`.
- `gcl_cutoffInterpolation_chart_core`: combines these into global smoothness, image-in-chart and agreement with identity on a specified set `B`.
- `gcl_bump_cutoff_chart_core`: instantiates these hypotheses using the pinned Mathlib `ContDiffBump` on concentric Euclidean inner/outer balls.

The pinned Mathlib API `Convex.add_smul_sub_mem` supplies the critical range proof. These facts require **neither** compactness nor connectedness of the target manifold. The code is part of the `semantic-342` exact-source CI replay; **acceptance requires an actual completed pass and permitted kernel axiom list**.

## What this does not establish

The generic lemmas take a cutoff as input; the packaged-bump lemma constructs its required properties from an existing Mathlib `ContDiffBump` with chosen radii. A future proof must choose a sufficiently small outer radius to lie inside an arbitrary chart image, then define a globally smooth manifold-valued map `F = ψ ∘ H` for the chart inverse `ψ`. That final map must be proved admissible to the upstream `ContMDiffOn Model Model ∞` quantification and its `mfderiv` must be shown equal to the local inverse-chart derivative wherever `χ=1`.

Only then can we finish the two directions of intrinsic `IsSmooth` and, under smoothness, intrinsic `IsClosed` equivalence. The current math-level argument is not a kernel proof of those equivalences.

The following stay unchanged: `SEM342_01_INTRINSIC_SMOOTHNESS_OPEN`, `SEM342_02_INTRINSIC_CLOSEDNESS_OPEN`, `SEM342_04_MANIFOLD_MODEL_OPEN`, `SOURCE_LOCKED`, `MATHCERT_NOT_GRANTED`, and the October cone theorem is not covered by the family-342 Comparator.

## Exact follow-on steps

1. Given an arbitrary open chart image and point, choose a sufficiently small outer ball inside it and instantiate the existing `ContDiffBump` type with appropriate inner/outer radii; the packaged-bump lemma supplies the remaining properties.
2. Compose it with the chart's total inverse function, proving `ContMDiff Model Model ∞` globally by `ContMDiffOn` composition and `H(E)⊆D`.
3. Prove equality of chart inverse `mfderiv` on the neighborhood and, consequently, equality of the resulting pulled-back differential forms there.
4. Prove full local-to-global and global-to-local `IsSmooth`/chart coefficient equivalence.
5. Use pinned `extDerivWithin_pullback` and derivative locality to prove closedness equivalence. Then consider theorem-level manuscript semantic admission, not before.
