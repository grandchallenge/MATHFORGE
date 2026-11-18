# OAI-26 WP01 — Family 008 exact dual replay receipt

**Assignment:** `GCL-OAI-26-WP01-F008-LEAN38-COMPARATOR38`  
**Target:** `OAI.DeligneDrinfeld.main : OAI.DeligneDrinfeld.MainStatement` in `OAI.Algebra.Drinfeld.Completion`.  
**Corpus declaration:** UTF-8 sorted index **38** of 200, one element only.  
**Source identity:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, source tree `45074722c918576d65b4c8be9686c76f508ba696`; Lean `leanprover/lean4:v4.34.1`; pinned `lean/lake-manifest.json` SHA-256 `cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794`.  
**Protected GCL run head:** `grandchallenge/MATHFORGE@4dcf6e4ac49bed6c61b05980ca17036a78d5e894`.  
**Conclusion:** `PINNED_LEAN_AXIOMS_PASS__HARDENED_COMPARATOR_PASS` on this exact target. This is **formal artifact verification only**, not full manuscript mathematical certification.

## 1. Independent pinned Lean build and axiom report

[GitHub Actions #44298907335](https://github.com/grandchallenge/MATHFORGE/actions/runs/44298907335); job `134783123190`, completed successfully at 2026-11-18 12:06:49 UTC. Exact downloaded artifact `oai26-corpus-lean-38-1`, artifact ID `14425447501`, ZIP SHA-256 `c33410fb5331c7c3178cf4714e64ddfd91972e7dc6bfb52c02ac1a782c14cbac`. All **8** archived file hashes from the run's `files.sha256` were independently recalculated and matched. The source-identity files record the GCL and upstream revisions above.

- `lake build OAI.Algebra.Drinfeld.Completion` succeeded: **8,944 jobs**, module `OAI.Algebra.Drinfeld.Completion` built.
- Exact `#check OAI.DeligneDrinfeld.main` output: `OAI.DeligneDrinfeld.main : OAI.DeligneDrinfeld.MainStatement`.
- Exact `#print axioms OAI.DeligneDrinfeld.main` output: `[propext, Classical.choice, Quot.sound]`.
- Build and axiom subprocess exit codes **0/0**, extra axioms **none**, no `sorryAx` in the theorem's axiom closure. Machine receipt verdict `LEAN_REPLAY_AND_AXS_PASS`. Its `actual_comparator_executed=false` is correct for this **first** run, and must not be conflated with the separate second run.

## 2. Independent hardened and isolated Comparator

[GitHub Actions #44304148849](https://github.com/grandchallenge/MATHFORGE/actions/runs/44304148849); job `134801236450`, completed successfully at 2026-11-18 12:40:48 UTC. Exact downloaded artifact `openai-math-comparator-indexed`, artifact ID `14428700812`, ZIP SHA-256 `ee010b0d1f8de9eb079a6c3a4af00b1926a41aafc3ddb6587bc63c99752997ad`. The artifact ZIP digest matched the GitHub provider digest. **All 11** file hashes and lengths in the machine receipt `REPLAY_RECEIPT.json` were independently recalculated and matched, as were the exact selected declaration and index.

- Machine receipt: `record_type=GCL_OPENAI_MATH_COMPARATOR_REPLAY/1`, `corpus_index=38`, `target=OAI.DeligneDrinfeld.main`, `hardened_exit=0`, `comparator_hardened_accepted=true`, `diagnostic_exit=null` (no additional lower-assurance diagnostic used).
- Declared isolation tool pins: Comparator `d03acab154d269c06e60e4de7e4cc85deebff94b`, exporter `076e8e57707e813375e8f9da8bf989799ace9680`, landrun `5ed4a3db3a4ad930d577215c6b9abaa19df7f99f`.
- The hardened log's result is `Lean default kernel accepts the solution`, `Your solution is okay!`, `Finished with result: success`.
- The `ComparatorChallenges.DeligneDrinfeld` **challenge fixture** logged `declaration uses sorry`. This is not a claim that the **accepted solution** uses `sorry`: the accepted solution is built from `OAI.Algebra.Drinfeld.Completion` and the separate `#print axioms` shows no `sorryAx`. The Comparator challenge fixture should remain labelled as an unproved placeholder; it is not the proof.
- The input `lake-manifest` SHA-256 is unchanged across the Comparator run; `selected-identity.json` explicitly binds the exact solution module, declaration and allowed axioms. The challenge and proof are not treated interchangeably.

## 3. Mathematical meaning and remaining critical review

The separately protected [Family 008 expanded definition bridge](https://github.com/grandchallenge/MATHFORGE/pull/558) (merge `4dcf6e4ac49bed6c61b05980ca17036a78d5e894`) established `PROPOSITION_LEVEL_ALIGNMENT__DEFINITIONS_EXPLICIT` for the manuscript's rational graded free Lie solution space, its Ihara bracket, odd generators 3,5,7,..., and mutually inverse continuous weight-completion maps. The present **two exact Lean executions** add evidence that the formal target checks under the pinned toolchain and permitted axioms.

This evidence is **not** an independent review that every source manuscript proof is sound, that the formal presentation is equivalent to every standard definition of the Grothendieck–Teichmüller Lie algebra, or that the result is novel or universally accepted. Inspect the braid algebra quotient, the topological completion convention, and the imported proof dependencies with a mathematical Adversary/Referee before any higher claim. The pinned Lake environment prints compatibility-patched external dependency warnings; the manifest stayed pinned and both independent runs succeeded, but those warnings should be retained in the proof provenance.

**Operational lesson:** The 12-family WP03 pilot yielded zero newly executed proof checks; this immediate WP01 follow-up has now yielded **one** exactly pinned theorem with **two** successful formal replay mechanisms. Review throughput and proof-verification throughput are distinct counters. The rest of the 200-entry WP01 register is not claimed complete.

## Reproduction

1. Inspect run `44298907335` artifact `14425447501`, verify ZIP digest and the eight file hashes, solution build exit, `#check` and `#print axioms`.
2. Inspect run `44304148849` artifact `14428700812`, verify ZIP digest, eleven receipt file hashes, `hardened.exit`, `hardened.stdout_stderr.log`, selected index/target and `REPLAY_RECEIPT.json`.
3. Verify both source, manifest, toolchain and GCL head identities match, without treating the Comparator fixture `sorry` as a theorem proof.
4. Only promote to a stronger mathematical claim after separate definition equivalence and independent mathematical critique. No MATHCERT action is authorized by these receipts.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP01-F008-LEAN38-COMPARATOR38
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
EXACT_HEAD: 4dcf6e4ac49bed6c61b05980ca17036a78d5e894
DISPOSITION: PINNED_LEAN_AXIOMS_PASS__HARDENED_COMPARATOR_PASS
EVIDENCE: GH runs 44298907335 (ZIP c33410fb5331c7c3178cf4714e64ddfd91972e7dc6bfb52c02ac1a782c14cbac), 44304148849 (ZIP ee010b0d1f8de9eb079a6c3a4af00b1926a41aafc3ddb6587bc63c99752997ad)
REPLAY: LEAN4_34_1_BUILD_8944_JOBS_PASS; AXIOMS_EXACT_3_PERMITTED; HARDENED_COMPARATOR_ACCEPTED
UNRESOLVED: broader manuscript proof, imported axioms/definitions beyond exposed closure, semantic equivalence to all standard mathematical conventions, MATHCERT
CLAIM_BOUNDARY: SOURCE_AND_FORMAL_EVIDENCE_ONLY__NO_MATHCERT_CERTIFICATION
```
