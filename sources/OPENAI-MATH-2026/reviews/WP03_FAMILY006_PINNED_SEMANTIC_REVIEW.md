# WP03 Family 006 — Density is not mean rank

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH`. This is a bounded source-and-index review, not a claim that no Lean formalization exists anywhere, not a theorem refutation, and not MATHCERT.

## Independently pinned manuscript editions

1. **Goldfeld's analytic density conjecture and the 2-converse for elliptic curves** — `preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-October-7-2026/paper.pdf`; 130 pages, 1087540 bytes; Git blob `58b8904f39b2a12534732010191fd35435559a61`; SHA-256 `c417858c9fe566daacb7738741dc66e211eea148b3da587eb5ee68eaad208d64`; exact paper-path crosswalk matches: **0**.
2. **The mean analytic rank of quadratic twists of elliptic curves** — `preprints/The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-October-6-2026/paper.pdf`; 41 pages, 549633 bytes; Git blob `fef228e3a2a26c0b1302fbd6f85de0da1c87a3ba`; SHA-256 `718fcfce4014a878685365edfb8a285a611512dea362dc5a9e1dc93d023cd7b1`; exact paper-path crosswalk matches: **0**.

All document digests were calculated from actual pinned PDF bytes. The checked corpus crosswalk contains 173 `source_papers` and 200 `main_results` entries. Exact PDF paths above do not match its `source_papers`; no candidate source-to-Lean theorem equivalence is established by this index. Path absence is not proof of unformalization.

## Source-derived mathematical analysis

The Goldfeld density paper asserts asymptotic densities 1/2 for quadratic twists of analytic rank 0 and 1 and a separate 2-Selmer converse. The mean-rank paper asserts average analytic rank tends to 1/2 for signed squarefree parameters ordered by absolute value. Density statements alone cannot establish the mean because exceptional twists of density zero may have large analytic rank.

**Mathematical verification still required:** Verify the high-rank tail/uniform integrability estimate and definition of signed squarefree twist ordering, not just density; no indexed Lean mapping is established. Formal proof dependencies, exact Lean source and compiler replay, axioms and independently adjudicated mathematical correctness were not established in this source review. Distinguish the manuscripts' claims from verified theorems.

## Critical scope test

**Positive witness:** the named pinned edition(s) make the distinct mathematical claims and conditions just recorded in their opening definitions, abstracts and theorem sections. **Countervailing witness:** no exact indexed source paper correspondence exists, so asserting that a particular crosswalk comparator verifies any of these manuscript statements would be unsupported. The review is a deliberately source-edition-bound `UNRESOLVED` verdict, which WP03 explicitly permits.

**Reproduction:** obtain each PDF at the upstream pinned commit, recompute its Git blob SHA-1 and SHA-256, compare its initial theorem/assumption statements, and match exact PDF paths against the crosswalk. Obtain a named Lean declaration and full semantic definition bridge before any `PROPOSITION_LEVEL_ALIGNMENT` promotion. WP01 separately owns Lean and axiom replay; WP04 independently criticizes mathematical validity.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F006
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: 58b8904f39b2a12534732010191fd35435559a61; fef228e3a2a26c0b1302fbd6f85de0da1c87a3ba
REPLAY: PINNED_PDF_STATIC_REVIEW_ONLY; LEAN_NOT_RUN
UNRESOLVED: Verify the high-rank tail/uniform integrability estimate and definition of signed squarefree twist ordering, not just density; no indexed Lean mapping is established.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
