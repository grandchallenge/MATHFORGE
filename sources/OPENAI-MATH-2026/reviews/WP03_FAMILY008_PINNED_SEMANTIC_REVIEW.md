# WP03 Family 008 — Deligne–Drinfeld free Lie algebra

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `UNRESOLVED__NAMED_LEAN_CANDIDATE_NEEDS_DEFINITION_BRIDGE`. Source-edition-bound audit, no MATHCERT. A missing index mapping is neither a global proof of nonformalization nor evidence that a claim is false.

## Independently pinned manuscript editions

1. **The Deligne-Drinfeld conjecture** — `preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/paper.pdf`; 41 pages, 539601 bytes; Git blob `0aa3328661d35567ec7e2dfb802b0351003e7a31`; SHA-256 `5ae63f326803a634e7c6dc5684ce7062ea0ac6940a88a75c7052875382dbc762`; exact paper-path crosswalk matches: **1**.

The PDF bytes were retrieved at the pinned upstream commit and their content digests calculated. The GCL crosswalk has 173 source-paper rows and 200 main-result declaration/comparator rows. Literal paper-path correspondence is distinct from name-based Lean candidate discovery. Full manuscript proof verification and Lean compilation were **not** performed here.

## Source-derived theorem scope and critical comparison

The manuscript's claimed theorem identifies the rational Grothendieck–Teichmüller Lie algebra as a free graded Lie algebra with one generator in every odd weight at least three, and asserts the corresponding weight-completed isomorphism. The pinned comparator `DeligneDrinfeld.json` names the Lean declaration `OAI.DeligneDrinfeld.main : MainStatement` in `OAI/Algebra/Drinfeld/Completion.lean`. Its visible proof term is `CategoricalValues.main_of_oddSolutions odd_solution`. This is a genuine direct named candidate, but `MainStatement` is defined in imported sources; the surface name and opaque target alone do not yet prove mathematical equivalence.

**Pinned Lean candidate:** `lean/OAI/Algebra/Drinfeld/Completion.lean` Git blob `98a996a90f4f57a205a3e3e8673a8528e8e3dbbf`; comparator `lean/ComparatorChallenges/DeligneDrinfeld.json` blob `479c2ef4d2352da81193e5ff8248f2cf86f484d7` (lists exactly the `main` declaration; allowed axioms are configuration, not a measured report). Source paper appears in the crosswalk, but its `main_results` entry supplies a declaration not a direct manuscript-path reference.

**Critical outstanding mathematical obligations:** Expand `MainStatement` and all relevant definitions; check free/Ihara Lie bracket, weight grading, odd generators, completion/topology and imported proof dependencies; verify pinned Lean and axioms independently.

**Positive witness:** the specific manuscripts' introductory theorem statements establish the distinct claimed quantifiers, hypotheses and conclusions recorded above. The named Lean declaration and comparator exist at exact source blobs.

**Countervailing witness:** The top-level Lean theorem returns an imported `MainStatement` and does not expose its expanded propositions in this limited inspection. Therefore neither the paper's full Lie-theoretic identity nor the weight-completed equivalence is established by the comparator name alone.

## Reproduction and bounded result

Fetch each PDF path from the exact source revision; verify the Git blob SHA-1 and SHA-256 shown; compare its specified theorem/quantifier scope with the crosswalk and, when present, the pinned Lean candidate. WP00 owns source mapping, WP01 owns Lean/axiom replay and WP04 owns independent mathematical criticism. This package is an **auditable WP03 source-level disposition**, not verification that the manuscript claims hold.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F008
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NAMED_LEAN_CANDIDATE_NEEDS_DEFINITION_BRIDGE
EVIDENCE: 0aa3328661d35567ec7e2dfb802b0351003e7a31
REPLAY: PINNED_MANUSCRIPT_STATIC_REVIEW; LEAN_NOT_NEWLY_REPLAYED
UNRESOLVED: Expand `MainStatement` and all relevant definitions; check free/Ihara Lie bracket, weight grading, odd generators, completion/topology and imported proof dependencies; verify pinned Lean and axioms independently.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
