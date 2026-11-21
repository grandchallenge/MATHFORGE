# OAI-26 F003 — reconcile completed Lean endpoint, conditional Gaussian bands and exact replay evidence

**Disposition:** `F003_FORMAL_ENDPOINT_TECHNICAL_REPLAY_ALREADY_PASS__INDEPENDENT_MATHEMATICAL_AND_HECkE_SEMANTICS_OPEN`  
**Bounded audit:** existing source-pinned formal theorem and dependency closure, not a new proof.  
**Source lock:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`; tree `45074722c918576d65b4c8be9686c76f508ba696`; Lean `v4.34.1`; manifest SHA-256 `cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794`.  
**Protected predecessor:** MATHFORGE main `a407e0752a362d87e3ad0ca1f2c051e320f43424`, merged PR #586.

## 1. Correction of the scientific work classification

**The source already contains formal unconditional endpoint declarations.** Pinned `OAI/NumberTheory/DirichletL/Nonvanishing.lean`, Git blob `46c67f4000906b1391a471d6e6396ac0da3c16a5`, states:

```lean
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0 :=
  SevenEighths.ProbeFinalAssemblyUnconditional.dirichlet_nonzero
    q (NeZero.ne q) χ s hs hpole

theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0 :=
  SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero s hs
```

The separately indexed Hecke theorem in `Hecke/Nonvanishing.lean` (Git blob `4fb158e2dc0d50f71a313ca1c6bdc56923c9d201`) universally quantifies the formal `HeckeFamily.Character` and excludes exactly the principal-pole pair `χ.residue=1,s=1`. This is not an unproved statement declaration `axiom`; it applies `LFunction_ne_zero_of_certified_bands` to the **constructed** `ProbeFinalAssemblyUnconditional.detector_certified_bands` theorem.

**Why the earlier “four sharp Gaussian powers open” language was misleading:** The actual `Energy/CanonicalMainGaussian.actual_main_gaussian_from_bands` (blob `149d54db73c4a8ca82646702cba3346c2b57c054`) and `CanonicalErrorGaussian.actual_error_gaussian_from_bands` (blob `1239786517727b801e0553c53a672003a92c8274`) take prior-stage `ZeroAt` and `PositiveAt` hypotheses. These are not undischarged hypotheses of the final nonvanishing declaration. The existing **formal induction actually constructs** those estimates. A separate *human-readable independent analytic derivation* of every step may still be absent, but that is a **proof-adjudication/semantics** obligation rather than a missing formal lemma. All prior mathematical reconstructions and finite arithmetic checks remain useful for independent audit, but are **not a new prerequisite for Lean endpoint compilation**. Do not claim GCL itself proved the theorem by those reconstruction notes.

## 2. Read directly from the pinned induction source: no extra terminal bands supplied by the caller

The **source proof path**, with specific proof-carrying transitions, is:

1. `Energy/WidthFloor.lean:actual_joint_floor`, blob `873260358de18594ed1b26a0996550cd16185a01`, constructs both base `ZeroAt` and `PositiveAt` from its declared data, \(51/100\le\beta\) and \(\kappa\ge2\beta-1\).
2. `Energy/CappedWidthInduction.lean:certified_floor` and `CertifiedBand`, blob `0f1fc34a0033ee423642d372c16dcd6690d59363`, wrap that genuine base in a width-capped band.
3. `Energy/CappedAnalyticSuccessor.lean:actual_successor`, blob `e48d2c10a65012a44b1525fa5231921ad1120566`, takes the prior certified band and invokes `CappedLowStage.actual_capped_low`, `NaturalHighStage.actual_high_stage`, and `NaturalZeroStage.actual_zero_stage`; `CappedSuccessorPacking.certified_from_stages` assembles the successor. Their declared premises are supplied from the previous stage and the explicit numerical admission inequalities.
4. `Energy/CertifiedExistence.lean:certified_bands`, blob `bb8024070c2f9c406801529e962eb94711178179`, proves `∀k≤count Mcap ε, CertifiedBand ... k` by induction, using `certified_floor` for the base and `actual_successor` for the step. `terminal_certificate` combines this with `CappedRadialTransport.certified_from_max_two`.
5. `Detector/FinalAssemblyUnconditional.lean:detector_certified_bands`, blob `e7c20910424837fb954796e1216f5aa453bbd5da`, introduces `hβ:(7/8)<HeckeZeroSupremum.beta`, chooses the actual `HighData` fixed parameters, and invokes `terminal_certificate` with the required profile/mesh/parameter proof arguments. In particular \(7/8<\beta\) implies \(51/100\le\beta\) for the induction's floor. It produces `DetectorCertifiedBands` without assuming `ZeroAt` or `PositiveAt` as global inputs.
6. `Detector/FinalAssemblyCertifiedBands.lean:chosen_moments_of_certified`, blob `8c7337e8f0755ba24fddab46a6630d58a32a9c86`, obtains moments; `dirichlet_of_certified`, `zeta_of_certified` and the Hecke conditional nonvanishing route discharge the final detector hypothesis. `Hecke/ZeroSupremum.lean:zeroRealParts`, blob `1139da5652ec349aebb9f395fe7ca0ba6e1fa654`, explicitly defines \(\beta\) as the supremum of real parts of zeros of the formal Hecke L-functions plus the \(1/2\) sentinel. `Hecke/CommonProbe.lean:beta_le_seven_eighths` (blob `92ae82094f323d97b92ae54801e88f2c97f20187`) is the contradiction step.

**Scope limit:** this is a read-only theorem-spine/declaration audit, *not* a fresh Lean replay of the entire induction, line-by-line independent verification of the upstream mathematical argument, or a certification of the September 30 PDF. The full endpoint's previously pinned Lean and hardened Comparator acceptance is separately evidenced below.

## 3. Existing exact technical proof receipts — avoid redundant 6,000–7,000-step replays

| Formal target | Sorted corpus index | Pinned Lean build and `#print axioms` | Hardened Comparator |
|---|---:|---|---|
| `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re` | 43 | [40610405028](https://github.com/grandchallenge/MATHFORGE/actions/runs/40610405028), success; recovered in protected `NEXT25_LEAN_RECEIPT_LEDGER.json` | [41076140621](https://github.com/grandchallenge/MATHFORGE/actions/runs/41076140621), success; protected `CORPUS_043_COMPARATOR_RECEIPT_LEDGER.json` |
| `OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re` | 145 | [40697520692](https://github.com/grandchallenge/MATHFORGE/actions/runs/40697520692), success; protected `CORPUS_145_6500S_LEAN_RECEIPT_LEDGER.json` | [41688402483](https://github.com/grandchallenge/MATHFORGE/actions/runs/41688402483), success; protected `CORPUS_144_145_147_149_COMPARATOR_RECEIPT_LEDGER.json` |
| `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` | 199 | [40743532665](https://github.com/grandchallenge/MATHFORGE/actions/runs/40743532665), success; protected `WP01_F003_ZETA199_RECOVERED_DUAL_REPLAY.md` | [42292101995](https://github.com/grandchallenge/MATHFORGE/actions/runs/42292101995), success; protected recovered same |

All **six** GitHub provider workflow-run objects were read back afresh and show `completed / success`, bound to historical GCL run heads (not to current `main`), with the exact immutable upstream pin recorded in protected receipts. Each positive Lean receipt reports `build_exit=0`, `axioms_exit=0`, observed axioms exactly `[Classical.choice, Quot.sound, propext]`, extra axioms `[]`. Each hardened Comparator separately accepts its corresponding named theorem; `sorry` placeholders in challenge stubs are **not** accepted as solution evidence. The initial index43 `1500s` and `4200s` timeouts were **recovered** by the later successful exact run; they are historical infrastructure, not mathematical failures.

**Subtle older-ledger inconsistency:** the generic `FORMALIZATION_CROSSWALK.json` source-inventory rows still contain `"replay":"NOT_RUN","semantic_review":"NOT_REVIEWED"`. These are stale relative to the subsequently admitted immutable run/receipt records. The GCL proof claim must be determined from newer protected exact receipts, not by treating either the stale row or the existence of one finished workflow as the final scientific verdict. Do not mutate the inventory's baseline history to erase the timeline.

**Current CI trap:** `.github/workflows/openai-math-pinned-lean.yml` has the name `OpenAI Math pinned Lean 4.34.1 replay` but its target is **Family 342**: `OAI.Geometry.TamingCompatibility.Main` and its source-specific semantic bridge, not Family 003's `DirichletL`. Its broad PR path trigger `sources/OPENAI-MATH-2026/**` causes the expensive Family 342 build and Comparator jobs even for pure F003 `.md`/`.py` changes. For instance F003 PR #586 actually triggered Family 342 replay pending; that job is **not** supplementary evidence for F003. The companion workflow fix narrows the PR source trigger to the seven `sources/OPENAI-MATH-2026/lean/Family342*.lean` files it explicitly reads, while retaining workflow-self-change and manual dispatch triggers. This avoids spurious resource-intensive replays; it does not remove dedicated indexed F003 replay workflows or invalidate historical run receipts.

## 4. What remains epistemically open (no reproof of the existing theorem)

**Supported positive semantic bridge for the three declared targets:**

- The final Dirichlet Lean theorem explicitly states nonvanishing of **`_root_.DirichletCharacter.LFunction`**, for all natural `q\ne0` and all `DirichletCharacter ℂ q`; this is the underlying Mathlib object rather than an invented `OAI` copy of Dirichlet L. Its source uses the nontrivial bridge `Hecke/Dirichlet.lean:LFunction_eq_dirichlet_product` (blob `a95e8042b3714a064486c6de6cc0bf8c63116b49`) to transfer from the Hecke model through a product of genuine Dirichlet L-functions. The zeta result is stated in terms of Lean's `riemannZeta`; this audit found no alternate local OAI definition in the pinpointed source. **Full imported Mathlib definition audit** is not newly executed.
- `Hecke/Family.lean`, blob `3d87da47cd57f0a4f11859c654e3e3202a519100`, defines `K=CyclotomicField 3 ℚ`, `O=RingOfIntegers K`, and `Character` as a residue-character with unit triviality, proper ideal modulus and integer period. The field is mathematically isomorphic to \(\mathbb Q(\sqrt{-3})\). `Hecke/IdealBridge.lean`, blob `bcb15758326db111dd0b007b79a58103a4fa659e`, defines `LFunction χ s=continuedLattice χ s/6` and proves `LFunction_eq_ideal_tsum` for \(\Re s>1\); `Hecke/Euler.lean`, blob `e5a4790fbd39d41b27c04efe8cfd45d238c189aa`, proves `LFunction_eq_series` in that region; `Hecke/FamilySeries.lean`, blob `445b25ae3b9c13d59ee0ac03c5c8d8b6777970d2`, controls equality of the continued function when two representations have the same element coefficients. This is **not** an arbitrary isolated function; its absolutely convergent Hecke ideal-series regime is explicitly proved in the source.
- **Still unproved in this GCL audit:** exhaustive equivalence of `HeckeFamily.Character` to **every** conventionally defined finite-order Hecke character over \(\mathbb Q(\sqrt{-3})\), including conductor variations, archimedean type/triviality, and all analytic normalizations. Previous `WP03_FAMILY003_HECKE_145_FORMAL_SCOPE_CORRECTION.md` correctly retains this missing correspondence proof. Nor does a Lean theorem certify every argument or variant edition in the 199-page manuscript or later October 1/5 papers.

**Retire/reclassify work:** Further brute-force sextic/CRT tests or standalone analytic reconstruction of `CanonicalMainGaussian` and `CanonicalErrorGaussian` should **not** be presented as necessary to *finish the Lean proof*. Retain prior F003 source audits, PRs #584–#586, and checked calculations as independent cross-examination evidence, not as a proof dependency on the final declared theorem. The highest-value next mathematical task is the *standard finite-order Hecke character equivalence and L-function semantics* or a specific falsifying counterexample to a pivotal analytic lemma. 

**Governance:** Existing protected technical acceptance does **not** confer MATHCERT or public scientific certification. Do not infer external peer-review agreement, paper-correctness, or proof novelty from compiler/Comparator receipt alone. No automatic governance promotion or issue closure is authorized by this report.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-WP03-F003-FORMAL-ENDPOINT-RECONCILIATION
UPSTREAM_PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
LEAN_TECHNICAL: PREVIOUSLY COMPLETED, 43 / 145 / 199, EXACT ALLOWED AXIOMS
HARDENED_COMPARATOR: PREVIOUSLY COMPLETED, 43 / 145 / 199
FORMAL_FINAL_GAUSSIAN_BANDS: CONSTRUCTED BY EXISTING CERTIFIED INDUCTION
INDEPENDENT_ANALYTIC_REDERIVATION: NOT CLAIMED
SEMANTIC_HECkE_EQUIVALENCE: OPEN
ADDITIONAL_GCL_LEAN_REPLAY: NOT PERFORMED — redundant
FAMILY003_FULL_MANUSCRIPT: UNRESOLVED
MATHCERT: NONE
```
