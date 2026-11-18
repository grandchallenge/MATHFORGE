# WP03 Family 010 — Completed Hecke is not classical modularity

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH`. Source-edition-bound audit, no MATHCERT. A missing index mapping is neither a global proof of nonformalization nor evidence that a claim is false.

## Independently pinned manuscript editions

1. **Unrestricted pro-modularity at the prime two** — `preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/two-adic-promodularity.pdf`; 29 pages, 454918 bytes; Git blob `60af9a2ac3e85261ded26474e61783dde8eb2f13`; SHA-256 `ef74b48557930663cab287cabd5280854f059de298e3016cc2172106eba1a1db`; exact paper-path crosswalk matches: **0**.
2. **The Dimension of the Two-Adic Hecke Algebra at Odd Level** — `preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/two-adic-hecke.pdf`; 12 pages, 347687 bytes; Git blob `2d7765cad8290f158660dc8aec58f1540dc0015b`; SHA-256 `b15081ee4a06c6c609eee447ee2dffd69578ce3550cbcd923e7206c7443333c5`; exact paper-path crosswalk matches: **0**.
3. **Fontaine–Mazur modularity at the prime 2** — `preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/paper.pdf`; 72 pages, 767547 bytes; Git blob `dea72dd57adfbe896cafccc6097b012bcd6dbb07`; SHA-256 `3c8797c7d468cdcccbfedf719c9a758a083954ba3c3005975736eb911d26a636`; exact paper-path crosswalk matches: **0**.

The PDF bytes were retrieved at the pinned upstream commit and their content digests calculated. The GCL crosswalk has 173 source-paper rows and 200 main-result declaration/comparator rows. Literal paper-path correspondence is distinct from name-based Lean candidate discovery. Full manuscript proof verification and Lean compilation were **not** performed here.

## Source-derived theorem scope and critical comparison

The main pro-modularity paper asserts occurrence of odd absolutely irreducible 2-adic Galois representations in a completed Hecke algebra at some odd tame level **without** de Rham hypotheses; it expressly does not assert classical modularity. The second paper claims Krull dimension exactly four for every irreducible component of the full two-adic Hecke algebra at odd level. The third assumes regular de Rham at 2 and claims classical Fontaine–Mazur modularity up to Tate twist. These are different theorem targets, with different hypotheses and ambient objects.



**Critical outstanding mathematical obligations:** Check exact completion topology, tame-level quantification, absolute irreducibility and oddness; distinguish all residual cases and Krull dimension from de Rham regularity and classical eigenforms.

**Positive witness:** the specific manuscripts' introductory theorem statements establish the distinct claimed quantifiers, hypotheses and conclusions recorded above. The corresponding PDF editions have been source-locked and individually distinguished.

**Countervailing witness:** The index cannot identify an exact Lean theorem corresponding to these PDF paths, so a compiler success elsewhere cannot be attributed to this family without a theorem-level correspondence record.

## Reproduction and bounded result

Fetch each PDF path from the exact source revision; verify the Git blob SHA-1 and SHA-256 shown; compare its specified theorem/quantifier scope with the crosswalk and, when present, the pinned Lean candidate. WP00 owns source mapping, WP01 owns Lean/axiom replay and WP04 owns independent mathematical criticism. This package is an **auditable WP03 source-level disposition**, not verification that the manuscript claims hold.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F010
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: 60af9a2ac3e85261ded26474e61783dde8eb2f13; 2d7765cad8290f158660dc8aec58f1540dc0015b; dea72dd57adfbe896cafccc6097b012bcd6dbb07
REPLAY: PINNED_MANUSCRIPT_STATIC_REVIEW; LEAN_NOT_NEWLY_REPLAYED
UNRESOLVED: Check exact completion topology, tame-level quantification, absolute irreducibility and oddness; distinguish all residual cases and Krull dimension from de Rham regularity and classical eigenforms.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
