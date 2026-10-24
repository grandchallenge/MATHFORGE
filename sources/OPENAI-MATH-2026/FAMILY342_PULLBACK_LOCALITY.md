# Family 342: chart extension derivative and pullback locality

**Lane:** MF-OAI-MATH-2026-F342-SEM-008  
**Exact upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Toolchain:** Lean `leanprover/lean4:v4.34.1`, Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.  
**Protected predecessor:** `MATHFORGE@75272aa269610ae4cffca5f3d9334d67aa82bb5a`.

## Scope

PR #324 admitted an existential *global smooth chart inverse extension* around each chart target point. The remaining issue was whether its derivatives, and therefore tensor pullbacks, agree with the local inverse chart on an inner ball.

`sources/OPENAI-MATH-2026/lean/Family342PullbackLocality.lean` contains two native Lean proof targets:

1. `gcl_chartBumpExtension_mfderiv_eq`: inside the inner ball, the manifold Fréchet derivative of the globally defined extension equals that of the chart inverse, using `Filter.EventuallyEq.mfderiv_eq`.
2. `gcl_chartBumpExtension_pullback_eqOn`: for **any raw `TwoForm X`**, even without smoothness, the pullback along the global extension is equal on the inner ball to the coordinate-form pullback along the chart inverse.

The imported source uses the exact upstream `mfderiv Model Model`, `TwoForm X`, and `pullback` definitions. The new job is wired into `semantic-342`; these are **proof candidates only until exact Lean replay passes**. A failed elaboration or `sorryAx` dependency is not an admissible result.

## Why this is consequential

It makes precise the critical step in the mathematical atlas-equivalence argument: a predicate quantified over globally defined maps can test a *local* chart coefficient form without changing its first-order geometry.

The mathematical consequences, once the two Lean theorems pass, are:

- For any point `y₀` in the chart target, PR #324 supplies a smooth global extension `F` agreeing with the inverse chart locally.
- Derivative locality implies `F^*α = (chartAt Space x).symm^*α` near `y₀`.
- The upstream `IsSmooth α` can therefore be applied to `F` to force smooth chart coefficients; similarly the upstream `IsClosed α` forces vanishing chartwise exterior derivative once `extDerivWithin` locality is discharged.

The *full* equivalence still requires actual Lean proofs for:

1. local-to-global `IsSmooth` and global-to-local `IsSmooth` via chart transitions;
2. `IsClosed` iff chartwise exterior derivative vanishes, under smoothness, using `extDerivWithin` locality and `extDerivWithin_pullback`;
3. complete equivalence between the paper's smooth manifold hypotheses and Lean's instance model.

No change to `SOURCE_LOCKED`, no MATHCERT certification and no certification of the revised cone theorem.
