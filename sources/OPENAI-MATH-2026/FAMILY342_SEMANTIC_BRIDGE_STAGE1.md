# Family 342: first kernel-level geometric semantic bridge

**Lane:** MF-OAI-MATH-F342-SEM-002  
**Pinned source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Protected predecessor:** `MATHFORGE@ea8989cd173d3c9d2720165e42d7fa782b190b72`  
**Target Lean:** `leanprover/lean4:v4.34.1`

## Statement tested

The paper's main theorem assumes existence of a symplectic two-form that **tames** the prescribed smooth almost-complex structure. The upstream Lean translation uses `IsSymplectic α ∧ Tames α J`, where

```lean
def IsSymplectic (α : TwoForm X) : Prop :=
  IsSmooth α ∧ IsClosed α ∧ IsNondegenerate α
```

Since taming imposes `α(v,Jv)>0` for every nonzero `v`, any `v` in the radical of `α` must be zero. Therefore the extra `IsNondegenerate α` conjunct adds no new hypothesis to the taming case, even before proving equivalence of the *smooth* and *closed* predicates to intrinsic smooth two-forms.

The module `sources/OPENAI-MATH-2026/lean/Family342SemanticBridge.lean` contains an **actual upstream-type-level** Lean proof of the reduction:

```lean
(IsSymplectic α ∧ Tames α J) ↔
  (IsSmooth α ∧ IsClosed α ∧ Tames α J)
```

It also contains the general algebraic equivalence:

```text
∀u v, ω(Ju,Jv) = ω(u,v)
  ↔
∀u v, ω(u,Jv) = ω(v,Ju)
```

under explicit antisymmetry, negative-argument, and `J²=-I` hypotheses. This does not yet instantiate the identity for every concrete upstream continuous alternating map. That instantiation is the remaining work in SEM-342-03.

The workflow `.github/workflows/openai-math-pinned-lean.yml` has a separate `semantic-342` job compiling the exact source and printing proof axioms. Its `REPLAY_RECEIPT.json` records exit, original source identity, theorem file hash and the boundaries. If the job fails, no Lean proof is admitted; a fresh exact-head repair is necessary.

## Remaining theorem-level obligations

- **SEM-342-01, OPEN:** prove bidirectional equivalence between `IsSmooth α` and intrinsic smoothness of a differential two-form; in particular recover the local chart expression using inverses of admissible smooth charts, and prove smoothness of arbitrary pullbacks.
- **SEM-342-02, OPEN:** under smoothness, prove bidirectional `IsClosed α ↔ dα=0` for the intrinsic exterior derivative; establish that the `extDerivWithin` expression coincides with the usual exterior derivative on chart images, and its naturality under smooth pullback.
- **SEM-342-03, PARTIAL IF LEAN PASSES:** the abstract metric symmetry identity is kernel checked; the native Lean instantiation and positive-definite smooth metric correspondence remain to be proven. Positive definiteness follows algebraically from taming once symmetry is established; smoothness of the metric depends on SEM-342-01.
- **SEM-342-04, OPEN:** fully establish the manifold model/typeclass/structure equivalence and no unrecorded topological or orientability constraints.

**Not asserted:** source-metadata or proof certification, mathematical novelty or priority, theorem-level manuscript equivalence, correctness of the entire revised cone characterization. The family-342 hardened Comparator acceptance remains a distinct previously certified execution fact, with `SOURCE_LOCKED` provider assurance and no `MATHCERT` promotion.
