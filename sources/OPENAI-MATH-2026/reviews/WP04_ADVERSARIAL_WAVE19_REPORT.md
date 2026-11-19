# OAI-26 WP04 — sixteen targeted plus three seeded baseline cases

**Programme:** [MATH-PROGRAMME #2850](https://github.com/grandchallenge/MATH-PROGRAMME/issues/2850)  
**Governing assignment:** [MATHFORGE #333](https://github.com/grandchallenge/MATHFORGE/issues/333)  
**Exact source revision:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Machine-readable ledger:** [WP04_ADVERSARIAL_WAVE16_LEDGER.json](WP04_ADVERSARIAL_WAVE16_LEDGER.json) (version `GCL-OAI26-WP04-ADVERSARIAL-WAVE19/1`); 19 distinct family IDs  
**Fail-closed test:** `python3 sources/OPENAI-MATH-2026/reviews/validate_wp04_wave19.py`  
**Scope:** independent *logical criticism* of claim scope using protected source records, direct pinned primary manuscripts for selected cases and held-out hostile semantic fixtures. Roles are non-authoring logical passes of the same authenticated worker, **not separately authenticated external referees**. The exercise is **not** nineteen independent full-paper proof reconstructions.

## Case selection and anti-inflation

- **Revision/source-integrity cases:** Families 002, 034, 056, 342, 376 (five).
- **Named formal matches or targeted bridges:** Families 003, 008, 011, 342 (four; 342 is a risky match, not a successful cone proof).
- **Unfamiliar mathematical domains:** Families 001, 004, 005, 009, 010 (five).
- **Predeclared controls:** Families 004, 006, 007, 012 (four; **not** described as random).
- **Actual deterministic baseline:** Families **223**, **095**, **191** (three, not selected for favorable outcomes), selected by the smallest SHA-256 of `GCL-OAI26-WP04-ADVERSARY-v1|<pinned source SHA>|<three-digit family ID>` over the full family IDs 001–372 with the sixteen targeted families removed. The immutable selection rule and hashes are in the JSON ledger.

Each of the 19 case rows contains a concrete objection, source observation, typed disposition, exact source-path evidence and a next mathematical proof obligation. Their case records do not claim external mathematical refereeing. The three seeded baseline families were additionally examined directly in the exact upstream PDFs, not inferred from titles.

## Material adversarial results

### Case 342 — **true source-semantic rollback, not main theorem refutation**

The September 23 claim `K_J^t = K_J^c + H_J^-` was unconditional. The October 6 manuscript now imposes `h_J^- = b_2^+(X)-1` on that equality and gives a torus strict-inclusion example otherwise. The pinned formal `OAI.TamingCompatibility.taming_implies_compatibility` instead targets existence of a compatible symplectic form from some taming form; that headline existence theorem is unchanged across editions. Thus a Lean replay of the selected existence theorem cannot reinstate the superseded **unconditional cone equality**. The proper verdict is `SEMANTIC_MISMATCH__SUPERSEDED_CONE_CLAIM` for the obsolete corollary, with the distinct existence theorem preserved. This is source-backed and does not claim an independent refutation of the entire revised paper. Primary source: the exact `preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/01-introduction.tex` blob `d9b79cce7dd94790552a15e9d5685b24f144f917`, the protected `WP02_F342_LITERAL_CONE_STATEMENT_DELTA.json` blob `073c5fcfa549c1f86daee8c331f55657857deb58`, and pinned `lean/docs/342.md` blob `890c10b573d2d383741d727fba384d4e52c0942e`.

### Case 008 — **bounded successful formal theorem**

Pinned Lean `OAI.DeligneDrinfeld.main` (sorted index 38) **does** compile against exact pinned Lean 4.34.1 with only `propext`, `Classical.choice`, `Quot.sound`. An independent hardened isolated Comparator accepts that solution. The pinned PDF's theorem and the expanded formal definition agree as shown in protected PRs #558 and #559, with an exact-rational independent low-weight check and hostile sign/relations fixtures protected in PR #560. `VERIFIED_WITHIN_EXPLICIT_SCOPE__UNCERTIFIED` is warranted for the exact Lean statement. Neither graph-complex corollaries nor complete source-proof independent adjudication inherit it.

### Case 095 — **spectrahedral ≠ spectrahedral shadow**

Three pinned PDFs must not be conflated. The September 24 paper supplies a cone with no direct LMI representation; its October 5 companion supplies an exact size-100, 307-auxiliary-variable lift of **that cone**. This is consistent: absence of a direct representation does not imply absence of a lifted representation. A *different* October 5 paper claims existence of a hyperbolicity cone with **no finite auxiliary semidefinite lift** at all. A purported contradiction between the latter existential theorem and the companion lifted cone would be invalid without identifying the two examples. Family-wide no-shadow theorem remains `UNRESOLVED__DIFFERENT_CONES_AND_LIFT_CLASSES` pending actual non-liftability proof review. The three PDFs were fetched and their pinned Git blobs independently computed: `820b7cecbcff0fea25eb323da94f07593d8f5d12`, `7515f77649b53cb14bbc2847d9abff6e092a8b6f`, `5f5d99899e05ab637c4c1f40b3b9fa1487d81e2f`.

### Case 223 — **six distinct random-cluster scaling targets**

Critical SLE/CLE for `1≤q<4` and a later claimed `1≤q≤4` result require **endpoint** scrutiny, and neither implies the distinct `0<q<1` paper. Quenched weak bond disorder (conditional-law convergence in probability), thermal massive SLE (finite mass and drift), and natural occupation (Minkowski-content measure rather than only curve shape) are separate limit modes. All **six pinned PDF introductions** were inspected and their exact Git hashes checked, but none of these six all-scale proofs has been independently replayed by this adversarial wave. Disposition `UNRESOLVED__SIX_DISTINCT_LIMIT_REGIMES`.

### Case 191 — **fixed power gain versus asymptotically vanishing exponent**

The September 25 manuscript asserts `Δ(n) ≥ c n^(-2+η)` for all sufficiently large `n` and some **fixed absolute** `η>0`. This is not interchangeable with a bound allowing an exponent tending to zero with `n`. The substantive review obligation is a uniform determinant-obstruction, divisor-count and deletion/rescaling estimate, not arithmetic on the final displayed exponent. Its 24-page pinned PDF was inspected (Git blob `41ed93344ef3bfbcf430d0889dce8211f434f7e8`). Disposition `UNRESOLVED__GLOBAL_DETERMINANT_COUNT`.

### Other significant failures of inference

- **Family 006:** A zero-density exceptional population can contribute non-negligibly to the mean if ranks grow; density-half alone does not imply Goldfeld's mean-rank statement. Requires uniform rank-tail control.
- **Family 010:** Representation in a completed Hecke algebra without regular-de-Rham hypotheses cannot be promoted into classical Fontaine–Mazur modularity.
- **Family 002:** Exact full BSD leading coefficient, Selmer converse and two-primary formula are not one proposition. Updated citation/proof dependencies demand separate testing.
- **Family 034:** Analytic nefness is not literal generation of a rational line bundle. The revised proof adds a base-presentations section and must preserve the logarithmic Iitaka assumption.
- **Family 056:** The main theorem text is unchanged, but the perturbation proof expands from 2,155 to 2,615 lines and adds new transfer lemmas; a title or theorem-text match cannot certify the revised argument.
- **Family 376:** An affine-conjugate terminal detector cannot be silently identified with an original observation field or encoding. The exact source-to-Lean event bridge is unresolved.
- **Family 003:** Named zeta and Siegel-zero statements do not validate the entire Hecke family nor their published analytic proofs.
- **Family 011:** Existing protected real-to-natural / positive-target totient statement bridges do not automatically verify the full external proof or two separate prime-factor-limit manuscripts.

## Hostile semantic fixtures and replay

The actual source-locked validator ran from exact candidate head `18e7bfdc74dd16067dc109a36a082d1111cc9f05` and checked 19 unique family IDs, 372 total catalogue IDs and 719 catalogue PDF paths, four selection-category minima, evidence path existence, seeded baseline ranking, no claimed independent reviewer identity, and no certification. It deliberately mutated a known-good evidence record to assert four false/unsupported verdicts and required the validator to reject each:

| Hostile proposition | Expected safe result |
| --- | --- |
| 342 unconditional old cone equation is formally verified | **ROLLBACK** |
| 006 mean analytic rank follows from rank density alone | **ROLLBACK** |
| 095 distinct lifted and non-liftable cones are identified, making all claims contradictory | **ROLLBACK** |
| 008 successful Lean replay automatically equals MATHCERT certification | **ROLLBACK** |

Exact output:

```text
HOSTILE_SEMANTIC_ROLLBACK_PASS 342
HOSTILE_SEMANTIC_ROLLBACK_PASS 006
HOSTILE_SEMANTIC_ROLLBACK_PASS 095
HOSTILE_SEMANTIC_ROLLBACK_PASS 008
WP04_WAVE19_SEMANTIC_VALIDATOR_PASS 19 distinct families; 3 seeded baseline; 4 hostile rollbacks; zero certification
```

The checker does **not** itself decide mathematical truth; its role is to reject known overclaims or misclassified evidence. The initial validator caught an ambiguity between `UNCERTIFIED` and the literal forbidden `CERTIFIED`; this was corrected to exact status-token matching. It also caught one incorrectly transcribed sample-hash suffix, repaired before this successful exact-head replay. Both recoveries are retained in branch history.

## Source and reviewer boundaries

The protected `WP02_CANONICAL_3_14_13_RISK_REGISTER.json` (blob `2d43ab80ca9d6a4395566d38f0afd5a464e4395e`) records three **withdrawn** title-level claims: split eightfold Weil-class algebraicity, Kuga–Satake algebraicity for K3, and rational Hodge for K3 products. They are **not** re-admitted by this wave and have **no newly established family-ID mappings**. The risk remains active for downstream dependencies. A withdrawal is not generalized to unrelated legitimate mathematical results.

**Reviewer status:** The non-authoring critical pass examines source claims and attempts logical falsification, using the same authenticated GCL agent identity as permitted by policy. It is not a separately authenticated researcher or an independent peer-review publication. The three seeded cases provide a genuinely held-out cross-domain check; most other rows reuse pinned WP02/WP03 evidence and challenge its inference boundaries instead of re-reading every full article. No claim of 19 complete manuscript proof reviews is made.

**Counts:** 19 source-semantic case assessments (16 targeted, three seeded), one reused full Lean+Comparator formal target F008, one explicit obsolete source-claim mismatch F342, zero new MATHCERT certificates. The scoped model review of F008 was previously protected admitted; the portfolio count must not triple-count its WP03, WP01 and WP04 receipts.

**Next consequential proof targets:** (1) Families 342/034/056: prove or reject edition-critical source dependencies; (2) F095 non-shadow obstruction, contrasted with its lifted companion; (3) F006 tail estimate; (4) F223 q=4 endpoint and natural-time mass tightness; (5) F003 broader Hecke vs zeta formal scope. For full programme completion, WP05 must still build its distinct **372-family/719-manuscript** verdict ledger, retaining WP01's 200 formal declarations and the publisher's 300 claim count as different denominators.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP04-ADVERSARIAL-WAVE19
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: ADVERSARIAL_WAVE19_SOURCE_AND_SEMANTIC_CRITIC_PASS__NO_CERTIFICATION
EVIDENCE: WP04_ADVERSARIAL_WAVE16_LEDGER.json + validate_wp04_wave19.py; 19 exact cases, three seeded baselines, four hostile rollbacks
REPLAY: EXACT_HEAD_SOURCE_RECORD_AND_HOSTILE_VALIDATOR_PASS; NO_NEW_LEAN_OR_FULL_PAPER_PROOF_REPLAY_IN_THIS_WAVE
UNRESOLVED: full independent all-paper proof criticism; withdrawals dependency propagation; per-family WP05 certification-independent triage
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
