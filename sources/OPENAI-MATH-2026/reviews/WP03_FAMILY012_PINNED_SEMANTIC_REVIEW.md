# WP03 Family 012 — Joint Dickman independence is stronger than marginals

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH`. Source-edition-bound audit, no MATHCERT. A missing index mapping is neither a global proof of nonformalization nor evidence that a claim is false.

## Independently pinned manuscript editions

1. **The joint Dickman law for consecutive integers** — `preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf`; 84 pages, 578632 bytes; Git blob `152b2fb1d9840703b874b3d46c13e8c8bb4cf867`; SHA-256 `e66b4e8a1fe197d3bb2c195548cd3bdd3fba8595db1356e571205a6baab43cb3`; exact paper-path crosswalk matches: **0**.

The PDF bytes were retrieved at the pinned upstream commit and their content digests calculated. The GCL crosswalk has 173 source-paper rows and 200 main-result declaration/comparator rows. Literal paper-path correspondence is distinct from name-based Lean candidate discovery. Full manuscript proof verification and Lean compilation were **not** performed here.

## Source-derived theorem scope and critical comparison

The manuscript's Theorem 1.1 concerns ordinary unweighted natural density of the joint events P⁺(n)≤n^a and P⁺(n+1)≤n^b for fixed a,b∈(0,1), with limit ρ(1/a)ρ(1/b). This is asymptotic **independence**, not two separate marginal smooth-number laws. It also claims the comparison P⁺(n)<P⁺(n+1) has density one half; that corollary requires a justified treatment of ties and the continuous limiting distribution, not just symmetry by fiat.



**Critical outstanding mathematical obligations:** Check moving n^a thresholds versus fixed X^a, ordinary rather than logarithmic averages, joint-to-ordering deduction and diagonal ties.

**Positive witness:** the specific manuscripts' introductory theorem statements establish the distinct claimed quantifiers, hypotheses and conclusions recorded above. The corresponding PDF editions have been source-locked and individually distinguished.

**Countervailing witness:** The index cannot identify an exact Lean theorem corresponding to these PDF paths, so a compiler success elsewhere cannot be attributed to this family without a theorem-level correspondence record.

## Reproduction and bounded result

Fetch each PDF path from the exact source revision; verify the Git blob SHA-1 and SHA-256 shown; compare its specified theorem/quantifier scope with the crosswalk and, when present, the pinned Lean candidate. WP00 owns source mapping, WP01 owns Lean/axiom replay and WP04 owns independent mathematical criticism. This package is an **auditable WP03 source-level disposition**, not verification that the manuscript claims hold.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F012
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: 152b2fb1d9840703b874b3d46c13e8c8bb4cf867
REPLAY: PINNED_MANUSCRIPT_STATIC_REVIEW; LEAN_NOT_NEWLY_REPLAYED
UNRESOLVED: Check moving n^a thresholds versus fixed X^a, ordinary rather than logarithmic averages, joint-to-ordering deduction and diagonal ties.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
