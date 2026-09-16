# UC-001 WP07 — avg-rare source provenance

Date: 2026-09-16

## Scope

This record binds the external formal source used for the UC-001 WP07
functional-preorder theorem-interface audit. It establishes source identity and
source drift only. It does not import the repository as a trusted dependency,
certify its theorem, or change the UC campaign claim boundary.

## Historical and current identities

Historical WP07 observation:

```text
repository: kashiwabarakenji/avg-rare
commit: 49c3f1d96ca8518d16e203fd0429ac1216838a4f
```

Selected current source revision:

```text
repository: kashiwabarakenji/avg-rare
commit: 21451877e9996a295bbc1ec25856d07fa302d48c
observed default branch: main
```

The selected revision is exactly two commits after the historical pin.

## Source drift

Commit `0a97001888d6b8c0b29c1dda2e49dbc725698446` changes comments only:

- `AvgRare/Basics/SetFamily.lean`: punctuation in a doc comment;
- `AvgRare/Old/Forest.lean`: removal of a Japanese comment.

Commit `21451877e9996a295bbc1ec25856d07fa302d48c` changes one comment only:

- `AvgRare/Secondary/MainStatement.lean`: `Paer Theorem 2.8` to
  `Paper Theorem 2.8`.

No theorem statement or proof term is changed by this two-commit delta.

## Environment identity

At the selected revision:

```text
lean-toolchain: leanprover/lean4:v4.23.0
lean-toolchain blob: 14a44240f0b7a83ef66c40a0a0db083992c0673d
lakefile.lean blob: 333187d1d756741fbffb0657cb64a28640f4b63f
lake-manifest.json blob: 12c14a66a9b4641a51e0f1695d2bfb0130ca6615
mathlib input revision: v4.23.0
mathlib resolved commit: 37df177aaa770670452312393d4e84aaad56e7b6
```

The three environment blobs above are unchanged from the historical WP07 pin.

## Audited theorem contract

The selected source defines:

```lean
structure FuncSetup (α : Type u) [DecidableEq α] where
  ground : Finset α
  nonempty : Nonempty ground
  f : {x // x ∈ ground} → {y // y ∈ ground}
```

Its functional preorder is the reflexive-transitive closure of the cover
relation `f(x) = y`. Its order-ideal predicate is:

```lean
def isOrderIdealOn (le : α → α → Prop) (V I : Finset α) : Prop :=
  I ⊆ V ∧ ∀ ⦃x⦄, x ∈ I → ∀ ⦃y⦄, y ∈ V → le y x → y ∈ I
```

The source-shaped ideal family is the family of all such order ideals on
`S.ground`. The paper-facing theorem declaration is:

```lean
theorem main_nds_nonpos {α : Type u} [DecidableEq α]
  (S : FuncSetup α) :
  (S.idealFamily).NDS ≤ 0
```

The repository's paper-sync record identifies this as the main
functional-preorder NDS-nonpositivity theorem.

## Placeholder and trust boundary

GitHub source search at the selected revision finds no active `sorry`
declaration and no explicit `axiom` declaration. The string `admit` occurs in a
comment in `AvgRare/Old/Forest.lean`; that file is not a default library root and
the occurrence is not an active proof placeholder.

MATHSOLVE performs the independent exact-revision `lake update`, `lake build`,
active-placeholder scan, and `#print axioms AvgRare.main_nds_nonpos` replay for
WP07. Those build results are theorem-interface evidence, not MATHFORGE source
identity.

## Claim boundary

This record establishes the exact current external source identity selected for
UC-001 WP07 and records that the drift from the historical pin is comment-only.
It does not certify `main_nds_nonpos`, does not establish a governed local UC
proof, does not add a claim to `MC-ROUTE-UC-001`, and does not alter the status
of `UC-P04` or `UC-FRANKL`.
