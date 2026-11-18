# WP03 Family 007 — Ordinary Chowla and corrected Elliott

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH`. This is a bounded source-and-index review, not a claim that no Lean formalization exists anywhere, not a theorem refutation, and not MATHCERT.

## Independently pinned manuscript editions

1. **Ordinary two-point correlations of multiplicative functions** — `preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf`; 87 pages, 819391 bytes; Git blob `60edc8ea20bc52ed80375df22f112658013894ee`; SHA-256 `ccb6f339a7505db7ab158dae4b739164ed8dda32be4012b0310198dd32f5c70a`; exact paper-path crosswalk matches: **0**.

All document digests were calculated from actual pinned PDF bytes. The checked corpus crosswalk contains 173 `source_papers` and 200 `main_results` entries. Exact PDF paths above do not match its `source_papers`; no candidate source-to-Lean theorem equivalence is established by this index. Path absence is not proof of unformalization.

## Source-derived mathematical analysis

The source makes two separate claims: fixed nonproportional affine-form Liouville two-point correlations with power-of-log savings at ordinary cutoffs, and an ordinary-average corrected Elliott statement under uniform nonpretentiousness of at least one original bounded multiplicative factor. Neither is equivalent to previously established logarithmically averaged variants.

**Mathematical verification still required:** Check the literal forms, nonproportionality, quantitative saving, nonpretentiousness condition, fixed residue-class extension and ordinary versus logarithmic averaging. Formal proof dependencies, exact Lean source and compiler replay, axioms and independently adjudicated mathematical correctness were not established in this source review. Distinguish the manuscripts' claims from verified theorems.

## Critical scope test

**Positive witness:** the named pinned edition(s) make the distinct mathematical claims and conditions just recorded in their opening definitions, abstracts and theorem sections. **Countervailing witness:** no exact indexed source paper correspondence exists, so asserting that a particular crosswalk comparator verifies any of these manuscript statements would be unsupported. The review is a deliberately source-edition-bound `UNRESOLVED` verdict, which WP03 explicitly permits.

**Reproduction:** obtain each PDF at the upstream pinned commit, recompute its Git blob SHA-1 and SHA-256, compare its initial theorem/assumption statements, and match exact PDF paths against the crosswalk. Obtain a named Lean declaration and full semantic definition bridge before any `PROPOSITION_LEVEL_ALIGNMENT` promotion. WP01 separately owns Lean and axiom replay; WP04 independently criticizes mathematical validity.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F007
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: 60edc8ea20bc52ed80375df22f112658013894ee
REPLAY: PINNED_PDF_STATIC_REVIEW_ONLY; LEAN_NOT_RUN
UNRESOLVED: Check the literal forms, nonproportionality, quantitative saving, nonpretentiousness condition, fixed residue-class extension and ordinary versus logarithmic averaging.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
