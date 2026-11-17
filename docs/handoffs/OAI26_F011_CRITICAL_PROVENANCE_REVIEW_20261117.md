# OAI26 F011 — source and provenance critical audit, 17 November 2026

**Evidence class:** bounded non-authoring source inspection and local replay reconciliation. **Disposition:** `LOCAL_REPLAY_PASS__INDEPENDENT_PROVENANCE_AND_ANALYTIC_SOURCE_REVIEW_OPEN`. This is neither mathematical certification nor a new proof of the source manuscript.

## Exact inspected inputs

- Original source collection: `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
- External proof repository: `cadamcat/totient-fibers-lean4@f75d4f2c2d6685a0547f17fa07240377aa2c2ed4`.
- External manifest SHA-256: `8df0747916e81c4d13f3ed226a6ffa5dd04760ffc13668241d603a3595c634cf`; Lean `4.34.1`.
- `Erdos821/Theorem.lean` SHA-256 `b32c493232f755e4becc588754de2e3cc187ee5a16b9efdedc26f5b676ef74a3`; `Erdos821/Final/Assembly.lean` SHA-256 `896783520bfc9c32e3daf5014f3637567b9b05b4d7e6b6848914d8e0c05e468b`.
- CHAD local receipt directory: `/home/jim/gcl-research/oai26-f011-independent-replay/chad-persistent-20261112/`. The directory is a diagnostic record, not independently authenticated execution evidence.

## Critical theorem inspection (logical critic, not theorem certificate)

1. `Erdos821.erdos_821` states that for every real epsilon strictly above zero, infinitely many natural `n` have `g(n)>n^(1-epsilon)`. Its proof is `Final.statement`, which applies `statement_of_supply` to `Final.supply`.
2. `Final.supply : SmoothShiftedPrimeSupply` is constructed from `Blueprint.supply_of_package_interfaces packageInterfaces`; the record provides named classical, sieve, transference, ideal, shift, type-II, proxy, geometric, bound, Type-I, balanced, extraction, and count ingredients. The full analytic burden is therefore hidden in this substantial imported package proof chain, **not assumed as a free hypothesis at the final theorem**. Source concordance of these intermediate analytic assertions remains an independent question.
3. `SmoothShiftedPrimeSupply` quantifies **for every fixed** `0<delta<1/4` and `sigma>0`, eventually in real `x`, at least `x^(1-sigma)` primes satisfying `2x<p<=5x` and each prime factor of `p-1` at most `x^delta`. This is a strong uniform-in-exponents formulation; direct full-text comparison to the pinned primary manuscript is still required.
4. `Erdos821/Fidelity/FormalConjectures.lean` explicitly proves `statement_iff_theorem_1_1` for the positive-fiber source statement, `statement_iff_exponentForm`, and `project_g_zero`. For positive `n`, external and positive-fiber counts coincide; the lone zero-target discrepancy cannot change an infinite set. The formal statement bridge is substantive and correctly scoped conditional on trusted imports.
5. The CHAD persistent run reports `BUILD_RC=0` (2026-11-14), `verify: PASS`, zero forbidden constructs, zero unexpected `sorry`, and exactly the standard axioms `propext`, `Classical.choice`, `Quot.sound`. The local 2026-11-15 revalidation reports matching SHA-256 for `build.log` (`e655eeadb3c29db580945b65483192f03953106866f2e8eddb6093767a8c7e33`), `verify.log` (`44a678a43d373a1f96f32eecfe0d16b60baf83fea8f2465d5a883105d95c3cec`), and `leanchecker.log` (`9f2dac808e170b716465936684104dd743bf896c5bdb424dc1d27da503865ed9`). The receipt itself says `independent_execution_attested=false`.
6. A retained lexical transitive-source audit resolved 129 modules (121 import edges), found 0 reachable modified tracked Lean files among 622 modified tracked dependency files, and listed no unresolved imports. A separate compiled-metadata intersection resolved 10,139 entries with zero modified reachable Lean files. These checks **do not rule out altered Lake build configuration, untracked shadow modules, stale compiled artifacts, or execution identity issues**. The local adverse audit specifically identifies changed dependency `lakefile.toml`, `lake-manifest.json`, and `lean-toolchain` configurations.
7. During this 17 November review a fresh exact-source `lake env leanchecker --fresh Erdos821.Theorem` was attempted via CHAD and the transport returned exit `-9` / timed out before a terminal proof result was captured; subsequently no checker process remained. Do **not** credit this attempt as either a fresh PASS or a Lean theorem FAIL.

## Specific adversarial obligations

- Verify exact loaded source and compiled artifact origins, including Lake configuration deltas, build cache, and untracked module shadowing; no inference of clean-room independence from local logs alone.
- Review the external analytic package inputs against the **pinned primary manuscript PDF**, especially fixed-delta quantifiers, real-variable asymptotic, interval boundaries and floor operations, prime factor cutoff, and the final totient inference.
- Confirm statement/definition equivalence without replacing the source's positivity restrictions by a non-equivalent target.
- If existing compiled evidence cannot meet independent provenance requirements, implement the content-addressed recovery contract admitted by MATHFORGE #550 and obtain a new governed job/lease before fresh cloud execution. No old Colab replay4/5 job is reusable as a successful terminal result.
- Record scoped Adversary/Referee review and exact-head protected readback; retain WP03 #332, WP04 #333, programme #2850 and MATHCERT obligations open until their independent closure requirements are satisfied.

**Claim boundary:** `SOURCE_INSPECTION_PLUS_LOCAL_LEAN_REPLAY_EVIDENCE_ONLY`; not `VERIFIED_WITHIN_EXPLICIT_SCOPE` until provenance and source-semantic adjudication are independently accepted.
