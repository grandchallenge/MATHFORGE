# OpenAI Math 2026: bounded semantic concordance

**Exact upstream revision:** `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. This is a **source-to-statement review**, not a Lean proof replay or MATHCERT certification.

## Family 342: Donaldson's tamed-to-compatible conjecture

Sources inspected at exact revision:

- `preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/build/sections/01-introduction.tex`
- `preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/01-introduction.tex`
- `preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/08-cones.tex`
- `lean/docs/342.md`
- `lean/OAI/Geometry/TamingCompatibility/Main.lean`
- `lean/ComparatorChallenges/TamingCompatibility.lean` and `.json`

The **principal existence theorem** is textually unchanged in the two paper editions: a smooth almost complex structure on a closed connected smooth real four-manifold that is tamed by a symplectic form admits a symplectic form compatible with the same structure. The corresponding Lean declaration `OAI.TamingCompatibility.taming_implies_compatibility` has an explicit existential taming-form hypothesis and concludes existence of a compatible symplectic form on a connected compact smooth four-manifold. The comparator pins that declaration; its `sorry` is a comparator placeholder, *not* proof-execution evidence.

The **cone theorem** changed materially. The September 23 edition asserted an unconditional cone-sum identity. The October 6 edition instead characterizes the compatible cone via strict intersection positivity on the closure of the invariant taming cone and deduces the sum identity under the extra condition `h_J^- = b_2^+(X)-1`; it documents a strict-inclusion four-torus case. No identified comparator captures the corrected cone theorem. The upstream formalization catalogue and `lean/docs/342.md` reference the older PDF, whereas the current `CONTENTS.md` links the October 6 edition.

**Disposition:** main existence theorem `PRELIMINARY_STATEMENT_ALIGNMENT`; corrected cone theorem `NOT_COVERED_BY_IDENTIFIED_COMPARATOR`; overall family `REVISION_LINK_REVIEW_PENDING`. Structural similarity does not establish equality of imported definitions, hidden assumptions, proof dependency soundness, or complete theorem correspondence.

## Family 003: quasi-Riemann hypothesis

Inspected:

- `lean/docs/003.md`
- `lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean`
- `lean/ComparatorChallenges/QuasiRiemannHypothesis.lean` and `.json`

The declaration `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` assumes `(7 / 8 : ℝ) < s.re` and concludes `riemannZeta s ≠ 0`, aligning at the displayed proposition level with the README's zeta `7/8` bound. The separate Dirichlet statement requires `¬ (χ = 1 ∧ s = 1)`; this correctly retains the principal-character pole exception. The accompanying family documentation also references Hecke and Landau–Siegel results; those are not globally reviewed by this check.

**Disposition:** bounded displayed-statement alignment only, `PRELIMINARY_STATEMENT_ALIGNMENT`; no exact Lean build or dependency-axiom verification completed.

## Audit gates still required

1. Run `leanprover/lean4:v4.34.1` under the pinned Lake dependency manifest and produce exact log, exit code and axioms for each solution declaration.
2. Run corresponding Comparator challenges in the *solution* environment; distinguish intentional `sorry` in the challenge file from executable proof witnesses.
3. Review full paper hypotheses and definitions (including imported modules), manuscript corrections, and original literature independently per family.
4. Promote no family to `SEMANTICALLY_REVIEWED` or mathematical certification using these preliminary observations alone.

These notes do **not** constitute independent specialist review, a formally admitted source provider, proof certification or an external priority decision.
