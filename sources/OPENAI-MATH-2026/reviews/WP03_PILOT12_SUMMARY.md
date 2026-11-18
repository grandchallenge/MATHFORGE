# OAI-26 WP03 — twelve-family source-edition-bound pilot

**Programme:** [MATH-PROGRAMME #2850](https://github.com/grandchallenge/MATH-PROGRAMME/issues/2850); **assignment:** [MATHFORGE #332](https://github.com/grandchallenge/MATHFORGE/issues/332).  
**Locked corpus:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.  
**Machine-readable ledger:** [WP03_PILOT12_EVIDENCE_LEDGER.json](WP03_PILOT12_EVIDENCE_LEDGER.json).  
**Local verification:** `python3 sources/OPENAI-MATH-2026/reviews/validate_wp03_pilot12.py`.  
**Terminal candidate:** `SEMANTIC_PILOT_COMPLETE__SOURCE_SCOPED__NO_CERTIFICATION`, contingent on protected admission and readback. The terminal pertains to **triage coverage**, not independently verified theorem proofs.

## Scope and findings

All **12** specified family IDs 001–012 are represented with **24 exact pinned PDF editions** and one explicit source-edition-bound WP03 disposition for each family. These 24 documents are a subset of the larger 372-family / 719-manuscript catalogue; the existing 173 source-paper entries, 200 Lean comparator/declaration rows and publisher's 300 claims count **different things** and are not treated as interchangeable.

| Family | Claim family | Source-edition-bound WP03 disposition | Precise evidence limitation |
| --- | --- | --- | --- |
| 001 | Milne rationality | UNRESOLVED | No indexed Lean match; rational pairings are not unconditional algebraicity |
| 002 | BSD formula / Selmer converse | UNRESOLVED | Three different claims; formula and rank converse are not interchangeable |
| 003 | Quasi-Riemann / Siegel zeros | UNRESOLVED, partial proposition alignment | All three editions now reviewed; zeta and real-zero claims have named Lean declarations, full Hecke and proof concordance open |
| 004 | Rational H10 and pointwise converse | UNRESOLVED | No exact indexed paper match; unrelated RationalHitting declaration rejected as default mapping |
| 005 | Catalan constant | UNRESOLVED | No indexed Lean match; numerical contradiction is conditional on unreplayed determinant estimates |
| 006 | Goldfeld density and mean rank | UNRESOLVED | No indexed Lean match; density 1/2 alone does not imply mean rank 1/2 |
| 007 | Ordinary Chowla/Elliott | UNRESOLVED | No indexed Lean match; ordinary and logarithmic averages differ |
| 008 | Deligne–Drinfeld | UNRESOLVED, named Lean candidate | `OAI.DeligneDrinfeld.main : MainStatement` identified; definition/model bridge and exact replay outstanding |
| 009 | Milnor K / Bogomolov–Pop | UNRESOLVED | Three distinct reconstruction regimes; characteristic-p versus mod-ell requires separate proof |
| 010 | 2-adic pro-modularity | UNRESOLVED | Completed-Hecke occurrence ≠ classical Fontaine–Mazur modularity |
| 011 | Prime predecessors / totient fibers | PROPOSITION_LEVEL_ALIGNMENT, limited first paper | GCL PRs #548/#549 bridge specific totient/supply statements; external full Lean replay independently unattested; other two manuscripts separate |
| 012 | Joint Dickman law | UNRESOLVED | No indexed Lean match; independence and ordering corollary need distinct checks |

**Complete artefacts:** one family review for each of 001,002,006–012; Family 003 September 30 audit plus companion edition supplement; Family 004 and 005 prior reviews consolidated from earlier PRs [#554](https://github.com/grandchallenge/MATHFORGE/pull/554), [#555](https://github.com/grandchallenge/MATHFORGE/pull/555), and [#556](https://github.com/grandchallenge/MATHFORGE/pull/556). These historical PR numbers are provenance, not separate required promotions if this consolidated PR is admitted. Exact SHA/paths are in the ledger, with source-level witness and bounded negative evidence in each review file.

## What the pilot actually certifies

It **does not certify any mathematical theorem**. No new pinned Lean kernel run was performed for these twelve review records; previous limited Family 011 formal-statement bridge executions are distinct from independent full external-proof replay. The bounded WP03 acceptance is one auditable source-edition-bound disposition per family, including `UNRESOLVED` where the evidence does not establish a theorem-semantic match.

This pilot is **not** a replacement for WP00 mapping reconciliation, WP01 compiler/axiom replay, WP02 revision review, WP04 independently recorded criticism or WP05 portfolio verdicts. The verdicts remain claim-scoped and can only be upgraded on fresh exact-source evidence. A manuscript's asserted proof, a comparator configuration, a matched title or an upstream claimed 300-result total is not independent mathematical verification.

## Bounded non-authoring critical pass

As a separate **read-only critical review of source claims**, challenge these inflation paths before protected admission:

1. **Counting:** All twelve IDs and 24 exact paths accounted for, but no 200↔300 equality asserted.
2. **Sources:** Digest identities pinned; no substitution of newer manuscripts; Family 003's alternate 11/12 edition does not become a proof of the 7/8 result.
3. **Formality:** No exact-path match is **not** proof of global unformalization. A typed but opaque `MainStatement` is **not** a semantic proof bridge.
4. **Proof inference:** For Family 005 the strict numerical contradiction only checks the last implication if determinant premises hold. For 006, limiting density does not establish mean rank without a tail estimate.
5. **Cross-family conflation:** Completed-Hecke occurrence and Fontaine–Mazur classical modularity are not equivalent; distinct prime-predecessor statistics are not all established by the Family 011 totient bridge.
6. **Certification:** No family is promoted to MATHCERT; independent authoring-system critique and specialist proof scrutiny remain separate from this bounded administrative/source-criticism pass.

This pass is **not** an independent human mathematical review or an independent Lean proof execution. It records explicit falsification tests a later reviewer can repeat.

## Reproducibility and protected admission

Run `python3 sources/OPENAI-MATH-2026/reviews/validate_wp03_pilot12.py` from a checked-out candidate to verify family and edition coverage, exact-path crosswalk arithmetic, file existence and noncertification. The validator deliberately cannot prove that the original PDFs' analytic arguments are true or that Lean code has been successfully elaborated; digest verification of PDF bytes was performed separately in the source-acquisition run.

For subsequent waves, select cohorts of at most 24 families reproducibly from WP02's ranked revision risks followed by high-impact semantic ambiguities and an explicitly seeded baseline sample, retaining the exact sampling algorithm and source revision in the next wave manifest. Do not turn WP03 into open-ended theorem proving.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-PILOT12
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: SOURCE_EDITION_SCOPED_PILOT12_REVIEW_PREPARED__PROTECTED_READBACK_REQUIRED
EVIDENCE: WP03_PILOT12_EVIDENCE_LEDGER.json + 12 indexed family evidence packets; 24 pinned PDF identities
REPLAY: SOURCE_INSPECTION_AND_OFFLINE_LEDGER_VALIDATOR; NO_NEW_LEAN_KERNEL_EXECUTION
UNRESOLVED: Full semantic bridges; independent kernel and adversarial proof replay; WP00/WP02/WP04 reconciliations; MATHCERT
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
