# WP03 Family 011 — Totient fibers and separate prime-factor laws

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `PROPOSITION_LEVEL_ALIGNMENT__SCOPED_FIRST_MANUSCRIPT`. Source-edition-bound audit, no MATHCERT. A missing index mapping is neither a global proof of nonformalization nor evidence that a claim is false.

## Independently pinned manuscript editions

1. **Weighted dilation graphs, smooth shifted primes and totient fibers** — `preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf`; 68 pages, 802390 bytes; Git blob `063e788b4229148cbb0f5816563ea03c1418bdad`; SHA-256 `351692885d112277e969901e75fe56eeee0d263d5d5847d0b980fe2c8c7744c0`; exact paper-path crosswalk matches: **0**.
2. **The Poisson-Dirichlet law for prime predecessors** — `preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf`; 74 pages, 795971 bytes; Git blob `99e91540b99090e11bf2b5fb9e05abfe647ee189`; SHA-256 `4b54d35506a1928022ac21e6d270d30f6533423ddc5990975270a1e39a87bce7`; exact paper-path crosswalk matches: **0**.
3. **Prime Predecessors with an Even Number of Prime Factors** — `preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf`; 45 pages, 599500 bytes; Git blob `6f35ec8061dd861076882315f53cfc66913dfd25`; SHA-256 `8ee2d8f79198dd5f09c5fbf71e309a63493d1c089772499614ee58dc8575eae9`; exact paper-path crosswalk matches: **0**.

The PDF bytes were retrieved at the pinned upstream commit and their content digests calculated. The GCL crosswalk has 173 source-paper rows and 200 main-result declaration/comparator rows. Literal paper-path correspondence is distinct from name-based Lean candidate discovery. Full manuscript proof verification and Lean compilation were **not** performed here.

## Source-derived theorem scope and critical comparison

The first manuscript states that for each ε>0 infinitely many positive n have more than n^(1−ε) totient preimages; its shifted-prime supply additionally fixes δ before the eventual range. The second manuscript asserts convergence of normalized ordered prime factors of p−1 to Poisson–Dirichlet(1); the third asserts infinitely many primes p with p−1 squarefree and an even number of prime factors. These are three different problems. Separate source-level GCL formal statement bridges for the first manuscript have already been protected merged via PRs #548 and #549; the former reconciles real-x and natural-x supply, the latter the external unrestricted vs GCL positive-target totient fiber. Both are qualified statement alignment, **not** new independent attestation of the full external Lean proof or of the other manuscripts.

**Separate formal-statement bridge evidence:** [MATHFORGE #548](https://github.com/grandchallenge/MATHFORGE/pull/548) and [#549](https://github.com/grandchallenge/MATHFORGE/pull/549); external proof source `cadamcat/totient-fibers-lean4@f75d4f2c2d6685a0547f17fa07240377aa2c2ed4`. The published GCL bridge reports ordinary Lean axiom lists for the adapters; the full external source proof remains subject to an independently attested fresh replay and source-to-paper review. The 200-entry pinned crosswalk has no exact Family 011 manuscript path: **do not let this hide the separately admitted F011 evidence**.

**Critical outstanding mathematical obligations:** Replay the exact external Lean proof independently and evaluate analytic lemmas; verify no δ/ε quantifier loss; preserve n>0 exception and finite vs infinite fibers; perform separate coverage tests for Poisson–Dirichlet and parity papers.

**Positive witness:** the specific manuscripts' introductory theorem statements establish the distinct claimed quantifiers, hypotheses and conclusions recorded above. The separately merged formal statement bridges for the first manuscript are source-addressable.

**Countervailing witness:** Formal statement bridge success is not independent proof of correctness of the full external analytic argument; the other two companion manuscripts do not inherit the first one's evidence.

## Reproduction and bounded result

Fetch each PDF path from the exact source revision; verify the Git blob SHA-1 and SHA-256 shown; compare its specified theorem/quantifier scope with the crosswalk and, when present, the pinned Lean candidate. WP00 owns source mapping, WP01 owns Lean/axiom replay and WP04 owns independent mathematical criticism. This package is an **auditable WP03 source-level disposition**, not verification that the manuscript claims hold.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F011
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: PROPOSITION_LEVEL_ALIGNMENT__SCOPED_FIRST_MANUSCRIPT
EVIDENCE: 063e788b4229148cbb0f5816563ea03c1418bdad; 99e91540b99090e11bf2b5fb9e05abfe647ee189; 6f35ec8061dd861076882315f53cfc66913dfd25
REPLAY: PINNED_MANUSCRIPT_STATIC_REVIEW; PRIOR_GCL_STATEMENT_BRIDGES_ONLY
UNRESOLVED: Replay the exact external Lean proof independently and evaluate analytic lemmas; verify no δ/ε quantifier loss; preserve n>0 exception and finite vs infinite fibers; perform separate coverage tests for Poisson–Dirichlet and parity papers.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
