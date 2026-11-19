# OAI-26 WP05 — complete catalogue portfolio, two-wave synthesis

**Governing assignment:** [MATHFORGE #334](https://github.com/grandchallenge/MATHFORGE/issues/334); [MATH-PROGRAMME #2850](https://github.com/grandchallenge/MATH-PROGRAMME/issues/2850).  
**Exact source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.  
**Canonical deterministic ledger:** [WP05_CANONICAL_372_FAMILY_VERDICTS.json](WP05_CANONICAL_372_FAMILY_VERDICTS.json).  
**Generator:** [build_wp05_portfolio.py](build_wp05_portfolio.py).  
**Fail-closed check:** [validate_wp05_portfolio.py](validate_wp05_portfolio.py).  
**Protected input evidence revision:** `grandchallenge/MATHFORGE@fef6acbcc757a153509d6728e878c63404e8ad36` (the WP04 wave's protected merge). Exact Git blob IDs for *seven* imported source registers and family-008 receipts are locked inside the generated ledger and verified against raw bytes using the standard Git blob SHA-1 construction.

## Executive classification: distinct denominators

| Object | Count | What it means |
| --- | ---: | --- |
| Families in source catalogue | **372** | Exactly one portfolio verdict row per family ID |
| Manuscript PDF paths | **719** | Original indexed paths retained without adding, dropping or duplicating |
| Source-paper paths in Lean crosswalk | **173** | Presence of a source-paper row, not certification or a theorem-level proof mapping |
| Distinct Lean declaration/comparator rows | **200** | Formally indexed targets, not the publisher's 300 claims |
| Publisher's top-line claims | **300** | Different claim convention, not reconciled 1:1 to the other denominators |
| MATHCERT authorizations/certifications newly granted | **0** | No certification authority inferred from execution or review |

**Whole catalogue verdict distribution:**

| Verdict | Families | Interpretation |
| --- | ---: | --- |
| `VERIFIED_WITHIN_EXPLICIT_SCOPE` | **1** | Family 008's precise Lean theorem and its bounded mathematical model are backed by source-locked theorem/axiom compilation, a hardened Comparator and independent low-degree falsification |
| `UNRESOLVED` | **24** | A source/semantic or edition-risk review identifies concrete residual proof or correspondence obligations |
| `INSUFFICIENT_EVIDENCE` | **347** | Catalogue metadata exists, but no governed family-level mathematical verdict has been imported; **not refuted, not globally unformalized** |
| `SEMANTIC_MISMATCH` claim-level exception | **1** | Family 342's historical *unconditional cone equality* is superseded; its current main existence theorem is not classified as false |

The single explicit formal-success family is **not** a certification of all its associated manuscript statements, historical novelty or the conjecture in every independently standardized mathematical language. The 24 unresolved cases comprise 18 WP04 cases other than 008 and 6 distinct additional WP02 risk cases (IDs 019, 032, 036, 232, 233, 341). The recorded WP04 cases overlap the preceding WP03 first pilot: do not double-count them.

## Two-wave research comparison

### Wave 1: WP03 source/semantic pilot

Twelve family IDs 001–012, 24 exact pinned manuscript editions; zero newly proven all-manuscript theorems within that wave. This completed controlled source/semantic comparison and exposed missing formal targets and exact-scope gaps. Protected [PR #557](https://github.com/grandchallenge/MATHFORGE/pull/557) is the admitted basis.

### Wave 2: WP04 bounded adversarial wave

Nineteen distinct cases, 16 targeted and 3 reproducibly SHA-256-selected held-out baseline families; 12 cases overlap Wave 1, meaning **seven additional distinct family IDs**. It found one historical source-claim-level mismatch requiring rollback (Family 342's old unconditional cone equality), preserved Family 008's bounded formal success, and retained source-dependent mathematical gaps. The wave's four hostile verdict mutations were correctly rejected. Protected [PR #561](https://github.com/grandchallenge/MATHFORGE/pull/561) is the admitted basis.

### Between waves: genuine formal execution

The strongest *new* scientific evidence relative to the original source-only pilot is **one** precisely identified formal result, Family 008's `OAI.DeligneDrinfeld.main`. Its exact [Lean run #44298907335](https://github.com/grandchallenge/MATHFORGE/actions/runs/44298907335) passed 8,944 build jobs and permitted-axiom check; [hardened Comparator #44304148849](https://github.com/grandchallenge/MATHFORGE/actions/runs/44304148849) separately accepted the solution. Both artifact ZIP SHA-256s, exact source/run identities and bounded mathematical model checks were protected-admitted in [PR #559](https://github.com/grandchallenge/MATHFORGE/pull/559), with subsequent mathematical criticism in [PR #560](https://github.com/grandchallenge/MATHFORGE/pull/560). **WP05 generated zero fresh Lean proofs; it imported this one prior exact result.** Four review PRs do not equal four verified theorems.

## Six proof-obligation classes that could change a verdict

1. **Source version vs formal scope — 342:** The October 6 repaired source now requires `h_J^- = b2+(X)-1` for the cone equality. The selected Lean comparator targets only the **unchanged** taming-to-compatibility existence theorem. A fresh source-to-formal proof for the conditional cone claim would be new evidence, not retroactive validation of the obsolete unconditional claim.
2. **Analytic estimates — 005, 006, 191:** Catalan irrationality requires checking nonvanishing and determinant estimates; Goldfeld mean rank requires a high-rank uniform tail estimate beyond density; Heilbronn power improvement requires a fixed positive exponent and uniform determinant/sampling control.
3. **Different mathematical invariants — 009, 010, 095:** Mod-ell Milnor K vs characteristic-p reconstruction, completed-Hecke occurrence vs classical regular-de-Rham Fontaine–Mazur, and nonspectrahedral cones vs non-liftable shadows must each be separated at the theorem-hypothesis level.
4. **Limit regime and exceptional endpoints — 223, 012:** The FK `q=4` endpoint, `q<1`, quenched, thermal and natural occupation laws are six different targets. Joint Dickman independence and tie-sensitive comparison cannot be concluded from marginal distributions alone.
5. **Corrected proof dependencies — 002, 034, 056, 376:** Recheck the exact repaired hypotheses, auxiliary lemmas, and field/coordinate correspondence rather than relying on unchanged theorem headings or compiler green.
6. **Broader formal target coverage — 003, 011:** Exact Lean existence of a zeta declaration or first-manuscript totient bridge does not verify all Hecke families or unrelated prime-factor companion claims. Expanded proof replay must use the exact identified source statement, theorem and import/axiom closure.

## Withdrawal protections

The publisher's source-locked history withdraws three specific assertions involving split eightfold Weil classes, Kuga–Satake algebraicity and rational Hodge for products of K3 surfaces. These are retained in a **separate title-level quarantine**, not silently assigned to unrelated active family IDs. A prior Lean build or citation cannot reinstate them. An explicit corrected source edition, independently reviewed claim/dependency mapping and governed authorization would be needed. The remaining downstream dependency search is open.

## Reproducibility and hostile tests

Run from the exact candidate checkout:

```bash
python3 sources/OPENAI-MATH-2026/reviews/build_wp05_portfolio.py
python3 sources/OPENAI-MATH-2026/reviews/validate_wp05_portfolio.py
git diff --check
```

The generator reads only the pinned catalogue, crosswalk, WP02 risk register and protected WP03/WP04 ledgers; it neither downloads nor proves a mathematical result. Its locked inputs include F008's protected execution receipts. The validator independently enforces source-file Git blob identities, exact protected evidence revision, 372 unique family IDs, identical 719-path multisets, separate declaration/publisher counts, and one scoped formal success with exact GitHub run/job/artifact IDs.

Six hostile mutations plus an exact source blob-lock mutation must fail: promotion of a source-only family; deletion of a PDF path; F008 artifact substitution; revival of a withdrawn title; revival of the old 342 cone equality; stale evidence head; alteration of a source Git blob lock. The final exact-head replay observed all seven hostile rollback tests PASS and all original metrics match. This demonstrates noninflation of the **ledger**, not global mathematical correctness.

## Programme handoff and limitations

**Completion:** the 372-row inventory and source-bound portfolio triage, not 372 proofs. All 719 indexed paths are preserved, all 200 formal declaration slots remain distinct, and the source-supported statuses are explicit. One family has a verified theorem within an explicit scope. **New family-level final classes attributable to WP05 generation itself: zero** (it imports existing evidence); cumulative newly evidenced theorem targets since the WP03 source-only pilot: one; new certifications: zero.

**Highest-leverage next work:** independently replay other exact pinned Lean candidates with high-impact missing or mismatched paper bridges, start source-proof criticism with the F095 no-lift obstruction or F006 mean-rank tail bound, and complete withdrawal dependency mapping. Do not optimize the count of reviews at the expense of proof obligation discharge.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP05-PORTFOLIO372
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: PORTFOLIO_TRIAGE_372_ROWS_PREPARED__PROTECTED_ADMISSION_READBACK_REQUIRED
EVIDENCE: WP05_CANONICAL_372_FAMILY_VERDICTS.json; build_wp05_portfolio.py; validate_wp05_portfolio.py
REPLAY: 372_ID_UNIQUE_PASS; 719_PATH_MULTISET_PASS; 200_DECLARATION_DENOMINATOR_PASS; SEVEN_HOSTILE_ROLLBACKS_PASS; SEVEN_EXACT_INPUT_GIT_BLOB_LOCKS
UNRESOLVED: 24 case-specific proof/semantic gaps; 347 metadata-only families; three withdrawn-title dependency maps; full 200-row independent proof coverage; MATHCERT authorization
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```

## Corrective evidence reconciliation — protected WP01 Comparator 200/200

**This section supersedes any interpretation above that the 199 indexed declarations besides F008 have no technical checks.** A read-only, source-blind (no manuscript-semantic inference) recomputation scanned **87 previously protected WP01 receipt files** under `sources/OPENAI-MATH-2026/CORPUS_*_COMPARATOR_RECEIPT_LEDGER.json` and `evidence/oai26/wp01/comparator-indexed-*.json`. The exact protected evidence collection covers **all 200 distinct sorted indexed Comparator declarations** with hardened exit zero, recorded authenticated GitHub run/artifact identities, and the pinned source revision. Index 199 has two corroborating accepted comparator records and is counted **once**. Several historical receipt formats require crosswalk-by-index binding; the 17 such slots are flagged, not presented as verbatim declaration-name matches.

The reproducible, checked, per-declaration technical evidence index is `sources/OPENAI-MATH-2026/WP01_COMPARATOR_200_PROTECTED_RECEIPT_INDEX.json`; its generator is `reviews/reconcile_wp01_comparator_200.py`, with separate `reviews/validate_wp01_comparator_200.py` verifying exact 200-row permutation, all 87 raw Git receipt blobs and **five** hostile modifications. The WP05 portfolio itself now records the complete corpus-wide **200/200 technical Comparator coverage**, retains source-locked run references, and has **two** additional hostile safety tests against erasing that evidence or promoting a zeta-only check to the full Hecke manuscript claim.

The already protected `CORPUS_199_6500S_LEAN_RECEIPT_LEDGER.json` and `CORPUS_199_COMPARATOR_RECEIPT_LEDGER.json` document actual passed exact-revision checks of `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` (Lean Actions **40743532665**, hardened Comparator **40777019339**). This newly imported **technical subclaim evidence** is attributed to Family 003 but the family's final class remains **UNRESOLVED**: the comparator tests zeta nonvanishing, not every finite-order Hecke L-function or the manuscript's complete analytic proof. No new computation was necessary.

**Critical distinction in the resulting counts:** `200/200` means all formalized indexed *Comparator targets have protected technical acceptance records*. `1` means one *family* (F008) has the additional explicitly scoped verified formal theorem, definition correspondence and bounded mathematical model-adversary package required by this particular WP05 family-classification policy. `347` means the new portfolio lacks family-level mathematical adjudication for those families; it **does not** mean the underlying repository lacks successful Lean/Comparator runs. Global Lean build/axiom coverage is separately recorded in historical WP01 technical ledgers and is **not yet recounted as a deduplicated 200/200 claim by this correction**. Manuscript-wide certification and MATHCERT remain zero.
