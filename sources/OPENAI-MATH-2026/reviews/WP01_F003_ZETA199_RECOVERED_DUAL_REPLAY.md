# OAI-26 F003 — recovered historical exact Lean and hardened Comparator evidence

**Date of recovery:** 2026-11-19. **Claim-boundary:** SOURCE-PINNED FORMAL REPLAY ONLY; NO MATHCERT.

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`; source tree `45074722c918576d65b4c8be9686c76f508ba696`. **Lean:** `leanprover/lean4:v4.34.1`; `lean/lake-manifest.json` SHA-256 `cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794`.

## Formal target

The exact, UTF-8-sorted corpus index is **199**, named `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` in `lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean` (upstream Git blob `46c67f4000906b1391a471d6e6396ac0da3c16a5`). It states

```lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0
```

Its proof invokes `SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero s hs`; the imported analytic proof chain is very large. The companion Dirichlet-character theorem is present in the same module, but is **not** included in this recovered *index 199* Comparator result. An assertion covering all finite-order Hecke L-functions or the October 5 alternate manuscript is **not** obtained from this one zeta target.

**Exact selected Comparator config:** `lean/ComparatorChallenges/QuasiRiemannHypothesis.json`, upstream blob `acf552468fc23c1a27d685d33983c58c50040542`. It selects only the above theorem, permits `propext`, `Classical.choice`, `Quot.sound`, and `enable_nanoda=false`. `lean/docs/003.md` (blob `cf794e93da2e1a494434153f5b91f2990fe9fd60`) describes broader claimed formal coverage, but other declarations and their own receipts are separate obligations.

## Recovered pinned Lean proof and axiom execution — **PASS**

[Actions run #40743532665](https://github.com/grandchallenge/MATHFORGE/actions/runs/40743532665), job `123011164040`, October 28, 2026, successful; original GCL run head `4ef88e6ea8c17ff02a41339268ca39d0a2410077`. Downloaded exact `oai26-corpus-lean-199-1` artifact ID `12845633244`, archive SHA-256 `dedc2cfbac637619162f8b61ca2652cba3adb83550eeef035c43b86767c69ef3`; all **eight** file hashes in archived `files.sha256` independently recalculated and matched.

The captured build log says `Build completed successfully (7061 jobs)`. The `#check` output reports the precise proposition `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re {s : ℂ} (hs : 7 / 8 < s.re) : riemannZeta s ≠ 0`. The `#print axioms` log reports exactly `[propext, Classical.choice, Quot.sound]`, no extra axioms and no `sorryAx`. Machine receipt: `build_exit=0`, `axioms_exit=0`, `verdict=LEAN_REPLAY_AND_AXS_PASS`, and (correctly) `actual_comparator_executed=false` in **this** first workflow.

## Recovered independent hardened Comparator — **PASS**

[Actions run #42292101995](https://github.com/grandchallenge/MATHFORGE/actions/runs/42292101995), job `128147874814`, November 6, 2026, successful; original GCL run head `510f45a6918a3737bebd0756ee2e55e64e9ebe30`. Downloaded `openai-math-comparator-indexed` artifact ID `13547059649`, archive SHA-256 `e4d0be2054c00c5a4f7a10e208766a1b7760b92c59b02edf484ef3c5d722053d`; all **11** archived files matched their independently recalculated SHA-256 and byte counts in `REPLAY_RECEIPT.json`.

The receipt binds index `199`, exact selected theorem, same upstream source and Lean toolchain, `hardened_exit=0`, `comparator_hardened_accepted=true`, `diagnostic_exit=null`, and tool commits Comparator `d03acab154d269c06e60e4de7e4cc85deebff94b`, exporter `076e8e57707e813375e8f9da8bf989799ace9680`, landrun `5ed4a3db3a4ad930d577215c6b9abaa19df7f99f`. The complete log states `Lean default kernel accepts the solution`, `Your solution is okay!`, `Finished with result: success`. This workflow builds the solution under its declared hardening/isolation policy.

**The two executions are independent workflow runs**, but neither is an independently authenticated external mathematician's full analytic-proof assessment. Both use the same pinned source and dependencies. Some dependency repositories report local compatibility changes; the locked manifest identity and proof/axiom reports were inspected, and these warnings remain provenance qualifiers.

## Scientific and programme verdict

**Correct positive result:** `F003_ZETA_EXACT_PINNED_LEAN_AND_HARDENED_COMPARATOR_PASS`. This upgrades the *specific indexed declaration* from unknown imported replay to **proof replay evidence present**. The mathematical statement is exceptionally strong; successful execution is an observation about a formal theorem in a particular Lean environment and does **not** independently certify that all imported definitions or analytic lemmas agree with external standard mathematics, or that all manuscript arguments are sound.

**Correct family-wide result:** `PROOF_REPLAY_ONLY__FAMILY_WIDE_SEMANTIC_AND_ANALYTIC_REVIEW_OPEN`. The September 30 manuscript asserts a seven-eighths zero-free region for **all finite-order Hecke L-functions** over `ℚ(√-3)`, implying Dirichlet and zeta cases; the recovered check targets the narrower zeta statement only. The October 5 eleven-twelfths manuscript has its own mathematical provenance; the October 1 Landau–Siegel statement has a separate formal comparator target. Neither is individually verified by this zeta receipt. The *full general-Hecke bridge* and the independent review of critical analytic energy/detector bounds remain open.

**Avoid false throughput accounting:** This is **a previously completed formal result recovered into a portfolio** (October 28 and November 6), not a new theorem proven in November. It must not be counted as a fresh WP05 execution. No new expensive build was performed in this recovery.

## Exact reproduction

Inspect both public Actions runs and their artifact IDs above; verify archive digests against provider digests; recompute internal eight and eleven SHA-256 values, respectively; inspect `receipt.json`, `REPLAY_RECEIPT.json`, `axioms.log`, `hardened.stdout_stderr.log`, `selected-identity.json`, `gcl-head.txt`, `upstream-head.txt`, and manifest pin. Do not accept a green workflow status without these individual checks.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP01-F003-ZETA199-HISTORICAL-RECOVERY
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: ZETA_INDEX199_PINNED_LEAN_AXIOMS_AND_HARDENED_COMPARATOR_PASS__FAMILY_WIDE_UNRESOLVED
EVIDENCE: run 40743532665 artifact 12845633244 sha256 dedc2cfbac637619162f8b61ca2652cba3adb83550eeef035c43b86767c69ef3; run 42292101995 artifact 13547059649 sha256 e4d0be2054c00c5a4f7a10e208766a1b7760b92c59b02edf484ef3c5d722053d
REPLAY: HISTORICAL_TWO_RUN_RECEIPT_RECOMPUTATION_PASS__NOT_NEW_EXECUTION
UNRESOLVED: full Hecke and analytic paper proof; October 5/October 1 separate targets; imported model/source correctness and MATHCERT
CLAIM_BOUNDARY: SOURCE_SCOPED_FORMAL_ARTIFACT_PASS__NO_MATHCERT_CERTIFICATION
```
