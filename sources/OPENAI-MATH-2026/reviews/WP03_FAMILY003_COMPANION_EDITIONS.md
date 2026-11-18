# WP03 Family 003 — exact companion-edition concordance

**Upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`. **Family index:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`. **Crosswalk:** `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.

This is a supplementary source-edition review to [MATHFORGE PR #554](https://github.com/grandchallenge/MATHFORGE/pull/554), whose pinned September 30 manuscript review examined the strict seven-eighths Hecke/Dirichlet theorem and the exact zeta comparator. It completes examination of the **other two** indexed Family 003 PDF editions. It neither independently replays Lean nor proves the source arguments.

## Other two editions: exact custody

1. **October 5 alternate quasi-Riemann hypothesis:** `preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf`, 49 PDF pages, 784,503 bytes; Git blob `3ea94d87ffdee8db02c6ef1e563e6d166021ad2f`; SHA-256 `f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18`.
2. **October 1 Landau–Siegel exclusion:** `preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf`, 9 PDF pages, 404,812 bytes; Git blob `e31b1a244f251439b01d930c906f4e0c91dfc3a8`; SHA-256 `fab9f6e84ece2a37d834b2c031d8eb14e81413d9f6270791e7b5468b295214ef`.

Both original PDF blobs were downloaded from the exact pinned upstream revision and their standard Git blob SHA-1 and SHA-256 recomputed from byte content.

## Distinct theorem statements and mathematical comparison

**October 5, Theorem 1.1:** all finite-order Hecke `L` functions over `K=Q(sqrt(-3))` and hence all Dirichlet `L` functions, including zeta, are claimed zero-free for `Re(s)>11/12`. This is a weaker half-plane conclusion than the September 30 `Re(s)>7/8` theorem. The October 5 manuscript explicitly describes its theorem as an intermediate step toward the stronger seven-eighths paper. The zeta comparator in `lean/ComparatorChallenges/QuasiRiemannHypothesis.json` names `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`, which has a seven-eighths conclusion: a successful check would not prove that the **October 5 paper's own analytic argument** is valid, although the stronger claimed conclusion would logically imply the weaker zero-free assertion. Scope and proof provenance must remain edition-specific.

**October 1, Theorem 1:** there exists an *absolute* `c>0` such that for every primitive nonprincipal real Dirichlet character of conductor `q>=3`, every real zero `beta∈(0,1)` satisfies `(1-beta) log(q)>=c`. This is an effective conductor-scaled real-zero exclusion, **not** the same quantifier form as a uniform complex half-plane for all Dirichlet L-functions. The crosswalk's distinct SiegelZeros candidate is `OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap` in `lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean`, pinned Git blob `9ed5a07a40ab668baa9b537d46fae0421dc47435`. That declaration explicitly quantifies a positive constant, conductors, primitive nonprincipal real-valued characters and real zero, with the inequality `c <= (1-beta)*log(q)`. It therefore has **proposition-level alignment** with the October 1 theorem, subject to the precise Lean character/real-valuedness conventions and a separately replayed proof.

**Elementary implication between manuscript claims (conditional only):** if the September 30 seven-eighths assertion holds for all Dirichlet `L` functions, then every real zero `beta∈(0,1)` of a primitive real character satisfies `beta<=7/8`; for `q>=3` it follows that `(1-beta) log(q)>=(log 3)/8>0`. This derives a possible constant in the October 1 assertion from the stronger half-plane statement. It is **not independent evidence** that the seven-eighths theorem is correct and not verification of the October 1 paper's determinant argument.

## Correct bounded disposition

- September 30 seven-eighths edition: `PROPOSITION_LEVEL_ALIGNMENT` for the displayed zeta/Dirichlet consequences, full Hecke-family semantic bridge unresolved; see PR #554.
- October 5 eleven-twelfths edition: `UNRESOLVED` as a source-specific analytic proof / exact Lean candidate; logical implication from stronger claim does not establish the paper's own proof.
- October 1 Siegel-zero edition: `PROPOSITION_LEVEL_ALIGNMENT` for the displayed real-zero-gap theorem and indexed Lean declaration; full definition bridge and fresh replay unresolved.
- **Family-wide WP03:** `UNRESOLVED`, with three exact edition-level dispositions; not `FULL_SEMANTIC_MATCH_PROVED` or MATHCERT.

**Proof-verification next steps:** expand character conventions and external definitions; establish exact source manuscript-to-declaration edition mapping; independently compile both Lean declarations under pinned dependencies, inspect axiom reports, and criticise the analytic proof bodies. No route around the governed Lean/CI/protected admission rules is implied.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F003-EDITION-SUPPLEMENT
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: THREE_EDITIONS_SOURCE_REVIEWED; FAMILY_WIDE_UNRESOLVED
EVIDENCE: PDF blobs 3ea94d87ffdee8db02c6ef1e563e6d166021ad2f; e31b1a244f251439b01d930c906f4e0c91dfc3a8; Lean Siegel theorem blob 9ed5a07a40ab668baa9b537d46fae0421dc47435
REPLAY: SOURCE_ONLY; LEAN_NOT_NEWLY_REPLAYED
UNRESOLVED: definitions, proof provenance, Lean/axiom replay, paper correctness
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
