# WP03 Family 009 — Three inequivalent field reconstruction regimes

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH`. Source-edition-bound audit, no MATHCERT. A missing index mapping is neither a global proof of nonformalization nor evidence that a claim is false.

## Independently pinned manuscript editions

1. **Reconstruction of Function Fields from Mod-ℓ Milnor K-Theory** — `preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf`; 36 pages, 559547 bytes; Git blob `63303a74325fc94ec1aeb6cc01a67a80cfc9691e`; SHA-256 `fafdf71eafc4700ada91598eba0620dc3263dd48b5879aa42af806254124bb2f`; exact paper-path crosswalk matches: **0**.
2. **Reconstruction from Milnor K-theory modulo the characteristic** — `preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/paper.pdf`; 11 pages, 348272 bytes; Git blob `03cb80d075993b29d30f5e2609a8fc8a4b464cdc`; SHA-256 `df8a6b4a54b121c692f7221e7b606be0dde89351fcb9ab5bb3853f7c2da4da90`; exact paper-path crosswalk matches: **0**.
3. **The Bogomolov-Pop reconstruction theorem** — `preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf`; 26 pages, 449982 bytes; Git blob `0d19afa59d02fe732b3a2ec58535119393878757`; SHA-256 `4d805627401fffef78e1f0d8e21a0585f6c733e8be90643d0065cd27ffaa24f2`; exact paper-path crosswalk matches: **0**.

The PDF bytes were retrieved at the pinned upstream commit and their content digests calculated. The GCL crosswalk has 173 source-paper rows and 200 main-result declaration/comparator rows. Literal paper-path correspondence is distinct from name-based Lean candidate discovery. Full manuscript proof verification and Lean compilation were **not** performed here.

## Source-derived theorem scope and critical comparison

The first reconstruction theorem treats mod-ℓ Milnor K₁ and K₂ with their product for ℓ different from the characteristic, recovering perfect closures and constants with scalar/Frobenius ambiguities. The second specifically treats Milnor K modulo the characteristic p, with derivations and p-power subfields. The third uses pro-ℓ abelian-by-central Galois data in the Bogomolov–Pop formulation. None may be substituted for another without a proved comparison; in particular ℓ≠char does not include ℓ=char.



**Critical outstanding mathematical obligations:** Compare transcendence degree at least two, characteristic, algebraically closed constant assumptions, base-field identification, scalar and Frobenius ambiguity, Kummer duality and the two forms of invariant.

**Positive witness:** the specific manuscripts' introductory theorem statements establish the distinct claimed quantifiers, hypotheses and conclusions recorded above. The corresponding PDF editions have been source-locked and individually distinguished.

**Countervailing witness:** The index cannot identify an exact Lean theorem corresponding to these PDF paths, so a compiler success elsewhere cannot be attributed to this family without a theorem-level correspondence record.

## Reproduction and bounded result

Fetch each PDF path from the exact source revision; verify the Git blob SHA-1 and SHA-256 shown; compare its specified theorem/quantifier scope with the crosswalk and, when present, the pinned Lean candidate. WP00 owns source mapping, WP01 owns Lean/axiom replay and WP04 owns independent mathematical criticism. This package is an **auditable WP03 source-level disposition**, not verification that the manuscript claims hold.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F009
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: 63303a74325fc94ec1aeb6cc01a67a80cfc9691e; 03cb80d075993b29d30f5e2609a8fc8a4b464cdc; 0d19afa59d02fe732b3a2ec58535119393878757
REPLAY: PINNED_MANUSCRIPT_STATIC_REVIEW; LEAN_NOT_NEWLY_REPLAYED
UNRESOLVED: Compare transcendence degree at least two, characteristic, algebraically closed constant assumptions, base-field identification, scalar and Frobenius ambiguity, Kummer duality and the two forms of invariant.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
