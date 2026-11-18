# OAI-26 WP03 — Family 004: Hilbert's tenth problem over Q, pinned semantic/coverage review

**Record:** `GCL-OAI26-WP03-F004/1`  
**Family:** `004`, "Hilbert's tenth problem over Q"  
**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Scoped verdict:** `UNRESOLVED` (exact theorem-to-Lean mapping absent from the indexed 200-entry crosswalk); **not** `UNFORMALIZED` as a global assertion; no proof replay or mathematical certification.  
**Review type:** two-source manuscript theorem extraction, metadata-coverage audit, and near-name comparator countercheck.

## Exact source custody

The canonical MATHFORGE Family index `sources/OPENAI-MATH-2026/MANUSCRIPT_INDEX.json` (Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`) lists two manuscripts for Family 004:

| Edition | Source path | PDF bytes / pages | Git blob SHA-1 | PDF SHA-256 |
| --- | --- | --- | --- | --- |
| Oct 6 — H10(Q) | `preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/main.pdf` | 701,017 / 62 | `b75dddd5e05503cc04a156e94bb15d6fadf8158e` | `f79236c22b981fe66aaf3ba494a466bf26db212117db47d95a31bf0315af2b30` |
| Oct 7 — rational 2-torsion converse | `preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/paper.pdf` | 893,027 / 91 | `1d35e83ccc541890903bfa978c1f0f73972843ca` | `df42f33f68fbef7766e5679b298e68e910157f78f2266889fb757824b9e44939` |

Both PDFs were retrieved from the exact pinned upstream tree. Local Git blob digests were recomputed from the unmodified bytes and matched GitHub's exact pinned contents metadata. The PDFs were read with `pypdf`, without OCR. Source-derived manuscript observations below are **claims made by the documents**, not facts independently established as mathematical theorems.

## Actual theorem statements and scope

**H10(Q), PDF physical page 3, Theorem 1.1:** The manuscript asserts no algorithm decides whether an input polynomial `f ∈ Z[X₁,…,Xₙ]`, with the number of variables `n` itself part of the input, has a zero in `Qⁿ`. This is an **unconditional undecidability claim** in the document's statement; it is not just the already-known negative solution for integer unknowns. The manuscript's stated route uses effectively generated finite rational-solvability tests for integer solvability and a parallel search.

**H10(Q), physical pages 56–57, Corollary 7.1:** The document further asserts that `H10(Q)` has Turing degree `0′` and that two bounded-degree variants have that same degree: degree-at-most-four polynomial rational solvability and a finite list of degree-at-most-two equations encoded as a sum of rational squares. The text explicitly distinguishes its `H10(Z) ≤_T H10(Q)` **Turing reduction** from a claimed many-one reduction; it does *not* claim many-one completeness of `H10(Q)`, nor a fixed-dimensional input, nor an existential definition of `Z` inside `Q`. These distinctions matter for comparator validity.

**Pointwise converse, PDF physical page 2, Theorem 1.1:** Let `E/Q` be an elliptic curve with `E(Q)[2] ≠ 0`, and let `s₂(E) = corank_{Z₂} Sel_{2∞}(E/Q)`. Under the explicit condition `s₂(E) ∈ {0,1}`, the document asserts
`ord_{s=1} L(E,s) = rank_Z E(Q) = s₂(E)`, together with finiteness of `Sha(E/Q)`. The manuscript says the assertion includes arbitrary reduction at 2; it expressly **does not** claim the full BSD leading-coefficient formula, and `rank E(Q) ≤ 1` alone is *not* the stated Selmer hypothesis. This companion is **not equivalent** to the undecidability statement in the other Family 004 paper.

The review does not establish the validity of any analytic, geometric, computational, or model-theoretic arguments in either manuscript.

## Pinned formalization crosswalk test

Crosswalk exact blob: MATHFORGE `sources/OPENAI-MATH-2026/FORMALIZATION_CROSSWALK.json`, Git SHA-1 `5fc50adc9430a91f22f1c3913bdfec62fe75acda`, with 173 `source_papers` records and 200 `main_results` records at the pinned collection revision.

For **each of the two exact Family 004 PDF paths**, there are **zero** equal `source_papers[].pdf_path` entries and **zero** `main_results` entries containing that literal PDF path. This is a precise coverage result about the *indexed crosswalk*, not a proof that the corpus contains no relevant Lean file.

A name-based search within the crosswalk suggested a possible false positive: `OAI.RationalHitting.main`, source `lean/OAI/Computability/RationalHitting/Main.lean`, exact upstream Git blob `e175e44e4ed74294984eb07dab58c5232cc7eed3`, comparator `lean/ComparatorChallenges/RationalHitting.json` blob `c13cb85bb4833ab52f05c20b4576fded30c0f610`. Source inspection shows this declaration is written as `theorem main : MainStatement := ExecutableGenerator.main_of_implementation ExecutableGenerator.implementation`, and the declaration's local docstring describes **polynomial-time finite-state generation of a canonical rational hitting list**, with invertible values and preservation of inverse domains. Nothing in that displayed declaration or its comparator identifies a decision procedure for general polynomial rational zeros or an undecidability/Turing-degree theorem. The definition of `MainStatement` and its full dependencies were not expanded in this review: **do not call this a formal mathematical inequivalence proof**. The correct conclusion is that `RationalHitting` **cannot be admitted as an H10(Q) theorem match merely from its name or observed declaration**.

## Positive, countervailing and missing witnesses

- **Positive source witness:** H10(Q) physical page 3 states the exact ambient ring, quantification over varying `n`, and the rational-existence decision predicate. Physical pages 56–57 separate Turing and many-one reductions and limit the quartic result's scope.
- **Positive source witness:** The pointwise-converse PDF physical page 2 states explicit rational two-torsion and 2-primary Selmer-corank premises; the analytic-rank, Mordell–Weil-rank and finite-Sha conclusions are not the same as the H10(Q) conclusion.
- **Countervailing evidence to an inflated formalization claim:** neither Family 004 manuscript path appears in the crosswalk's 173 source-paper entries or 200 declaration-entry records. `RationalHitting` is a different observed declaration with a separate comparator, not a demonstrated Hilbert's-tenth comparator.
- **Missing evidence:** an explicit GCL family-to-declaration concordance, any relevant exact Lean theorem and definition bridges, exact Lean replay and axiom report, a source-critical check of the 62-page H10(Q) or 91-page elliptic proof, and independent non-authoring mathematical review. Do not infer that the paper is unformalized across all repositories from a missing index mapping.

## WP03 disposition, replay and next action

**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH` for both Family 004 editions. Neither `FULL_SEMANTIC_MATCH_PROVED` nor `PROPOSITION_LEVEL_ALIGNMENT` is assigned to a Lean comparison because **no comparable Lean theorem has been established**. Do not promote either manuscript as proved, disproved, or formally checked.

**Next concrete obligation:** WP00 should provide an exact family/manuscript/declaration mapping or a source-backed `NO_CROSSWALK_ENTRY` record for both paths. If a candidate Lean source emerges, perform theorem-statement and definition-level comparison; run pinned Lean replay only in WP01 after exact source+manifest binding. Separately check whether the pointwise converse is actually used as an input to the H10(Q) proof rather than inferring a dependency from Family 004 grouping.

**Reproduction:** Fetch `MANUSCRIPT_INDEX.json` and `FORMALIZATION_CROSSWALK.json` on MATHFORGE protected main and match the two Family 004 `pdf_path` values literally against `source_papers[].pdf_path` and against each `main_results` entry. Fetch the listed PDF bytes from pinned `openai/math`, recompute Git blob SHA-1 and document SHA-256, inspect physical PDF pages 2–3 and 56–57 as specified. Fetch exact `RationalHitting/Main.lean` and comparator to reject a declaration-name-only assignment. No Colab or CONTROL service changes are needed for this source-level audit.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F004
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: H10Q PDF git-blob b75dddd5e05503cc04a156e94bb15d6fadf8158e; pointwise PDF git-blob 1d35e83ccc541890903bfa978c1f0f73972843ca; CROSSWALK blob 5fc50adc9430a91f22f1c3913bdfec62fe75acda
REPLAY: EXACT_SOURCE_PDFS_AND_DECLARATION_STATIC_REVIEW_ONLY; LEAN_NOT_RUN
UNRESOLVED: full crosswalk family mapping; theorem/definition bridge; Lean replay; manuscript proof; nonauthoring criticism
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
