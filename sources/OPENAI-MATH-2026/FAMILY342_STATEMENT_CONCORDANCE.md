# Family 342: exact-edition statement concordance and comparator replay disposition

Date: 2026-10-23. Scope: OpenAI Math 2026 family 342 only.
GCL protected evidence source: MATHFORGE `5602487b42fc1328784cae3a1b4c378cede19f23`.
Pinned upstream: `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

## 1. Source statement identity, two manuscript editions

The September 23, 2026 and October 6, 2026 editions have textually identical **main existence theorem** in `build/sections/01-introduction.tex`, lines 23–27:

> Suppose that a smooth almost complex structure J on a closed connected smooth real four-manifold X is tamed by a symplectic form. Then there is a smooth symplectic form compatible with J.

The next paragraph, lines 29–32, explicitly fixes J and disclaims preservation of the taming form's de Rham cohomology class.

The formal target is `OAI.TamingCompatibility.taming_implies_compatibility` from `lean/OAI/Geometry/TamingCompatibility/Main.lean`. It takes a compact, connected, second-countable, Hausdorff manifold `X` modelled on `EuclideanSpace ℝ (Fin 4)`, a smooth `AlmostComplexStructure X` and `∃ α : TwoForm X, IsSymplectic α ∧ Tames α J`, and yields `∃ η : TwoForm X, IsSymplectic η ∧ Compatible η J`. It imposes neither integrability nor equality of the two forms' classes.

The comparator's challenge module `ComparatorChallenges.TamingCompatibility` states the same target with `by sorry` as an intentional test hole. Its definition block from `abbrev Space` to `Compatible` is **textually identical** (1,841 characters) to the corresponding `lean/OAI/Geometry/TamingCompatibility/Model.lean` block at the pinned upstream commit. The target theorem's displayed binder and proposition also match on source reading. This structural comparison is not itself Comparator execution.

Definitions warranting continued semantic audit:

- `Space`: four-dimensional Euclidean space over ℝ; `Model`: the standard smooth model.
- `AlmostComplexStructure`: continuous linear tangent endomorphisms squaring to `-I`, plus a manifold-smoothness witness.
- `TwoForm`: smoothness is **not intrinsic to the raw type**; `IsSymplectic` separately requires `IsSmooth α ∧ IsClosed α ∧ IsNondegenerate α`.
- `IsSmooth`: a chart/pullback regularity predicate; `IsClosed`: `extDerivWithin (pullback α f) U y = 0` for specified local test maps. That this fully captures the paper's intrinsic exterior derivative condition requires independent differential-geometric definition audit.
- `Tames`: strict evaluation positivity on `(v,Jv)` for all nonzero `v`.
- `Compatible`: `Tames α J ∧ IsInvariant α J` under `J`.

**Result:** `MAIN_EXISTENCE_STATEMENT_PRELIMINARILY_ALIGNED`; definitions still require mathematical-equivalence verification. No manuscript-level certification.

## 2. Material edition change, not covered by target

The September 23 introduction, lines 37–59, asserts the unconditional cone-sum identity
`K_J^t = K_J^c + H_J^-` and (for `b_2^+=1`) equality of the two cones.

The October 6 edition, lines 37–78, replaces that unconditional statement with a compatible-cone characterization by strict intersection positivity inside `V=(H_J^-)^⊥` and `C=K_J^t∩V`. It only recovers `K_J^t = K_J^c + H_J^-` under `h_J^-=b_2^+(X)-1`. Its `build/sections/08-cones.tex` includes an explicit four-torus strict-inclusion example.

The current `CONTENTS.md` indexes the October 6 revised PDF, while `lean/docs/342.md` and `lean/formalization.yaml` retain the September 23 PDF. The main theorem is unchanged but the versions must not be promoted as equivalent theorem suites. No identified challenge covers the corrected cone result.

**Result:** `MAIN_THEOREM_UNCHANGED_BETWEEN_EDITIONS`; `CONE_CLAIM_CORRECTED_AND_NOT_FORMALIZED_HERE`; `UPSTREAM_FORMALIZATION_PDF_REVISION_MISMATCH`.

## 3. Executed evidence and next gate

The exact protected-head workflow `OpenAI Math pinned Lean 4.34.1 replay`, run [40031587392](https://github.com/grandchallenge/MATHFORGE/actions/runs/40031587392), job `family-342`, succeeded. It built target module `OAI.Geometry.TamingCompatibility.Main` and printed:

```
'OAI.TamingCompatibility.taming_implies_compatibility' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The comparator configuration permits precisely those three axioms. The workflow's generated receipt explicitly recorded `actual_comparator_executed: false`. Therefore kernel compilation and axiom closure were verified, but Comparator acceptance was not.

A separate bounded comparator execution is commissioned using pinned sources:

- `leanprover/comparator@d03acab154d269c06e60e4de7e4cc85deebff94b`
- `leanprover/lean4export@076e8e57707e813375e8f9da8bf989799ace9680`, rebuilt with Lean 4.34.1
- `zouuup/landrun@5ed4a3db3a4ad930d577215c6b9abaa19df7f99f`

The comparator job distinguishes a `systemd-run` hardened invocation from a lower-assurance `landrun` diagnostic if the runner lacks user-systemd support; it does not promote the diagnostic into acceptance. This provides reproducible failure evidence for legitimate environment remediation.

## 4. Required final disposition

The family cannot be marked `SEMANTICALLY_REVIEWED` or promoted to any MATHCERT proof merely because Lean accepts the declaration or Comparator accepts a challenge. Completing the semantic gate also requires independent checking of the model-to-manifold definitions (especially intrinsic closedness), all changed-paper claims relevant to the target, the complete theorem's scope and cited mathematical prerequisites, and absence of hidden imported hypothesis strengthening. The corrected cone statement remains **uncovered** by the identified Lean challenge.
