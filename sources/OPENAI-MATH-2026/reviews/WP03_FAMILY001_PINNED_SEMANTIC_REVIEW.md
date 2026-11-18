# WP03 Family 001 — Milne rationality and specialization

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH`. This is a bounded source-and-index review, not a claim that no Lean formalization exists anywhere, not a theorem refutation, and not MATHCERT.

## Independently pinned manuscript editions

1. **Milne's rationality conjecture for abelian varieties** — `preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf`; 36 pages, 595267 bytes; Git blob `72cfde4183262eabe6383f245fd2c470ac65d304`; SHA-256 `640701a0ea8d8026d2f019e571e052f2d106cad3f5216cf6f7fca0d643873234`; exact paper-path crosswalk matches: **0**.

All document digests were calculated from actual pinned PDF bytes. The checked corpus crosswalk contains 173 `source_papers` and 200 `main_results` entries. Exact PDF paths above do not match its `source_papers`; no candidate source-to-Lean theorem equivalence is established by this index. Path absence is not proof of unformalization.

## Source-derived mathematical analysis

The source claims rational equality of pairings of rational Hodge classes against divisors on good reductions, including residue characteristic 2, across prime-to-p and crystalline realizations. It also discusses a separate algebraicity consequence using CM abelian varieties. Equality of realization-dependent numerical pairings must not be inflated to unconditional algebraicity of all Hodge classes.

**Mathematical verification still required:** Check good-reduction, Hodge-class and realization assumptions; compatibility of cycle-class maps and CM restriction. No candidate Lean declaration is established in the indexed crosswalk. Formal proof dependencies, exact Lean source and compiler replay, axioms and independently adjudicated mathematical correctness were not established in this source review. Distinguish the manuscripts' claims from verified theorems.

## Critical scope test

**Positive witness:** the named pinned edition(s) make the distinct mathematical claims and conditions just recorded in their opening definitions, abstracts and theorem sections. **Countervailing witness:** no exact indexed source paper correspondence exists, so asserting that a particular crosswalk comparator verifies any of these manuscript statements would be unsupported. The review is a deliberately source-edition-bound `UNRESOLVED` verdict, which WP03 explicitly permits.

**Reproduction:** obtain each PDF at the upstream pinned commit, recompute its Git blob SHA-1 and SHA-256, compare its initial theorem/assumption statements, and match exact PDF paths against the crosswalk. Obtain a named Lean declaration and full semantic definition bridge before any `PROPOSITION_LEVEL_ALIGNMENT` promotion. WP01 separately owns Lean and axiom replay; WP04 independently criticizes mathematical validity.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F001
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: 72cfde4183262eabe6383f245fd2c470ac65d304
REPLAY: PINNED_PDF_STATIC_REVIEW_ONLY; LEAN_NOT_RUN
UNRESOLVED: Check good-reduction, Hodge-class and realization assumptions; compatibility of cycle-class maps and CM restriction. No candidate Lean declaration is established in the indexed crosswalk.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
