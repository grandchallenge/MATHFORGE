# OM26-H7 — Erdős Problem 3: semantic source map

**Campaign binding:** OM26-H7  
**Exact organizer hill:** `ottogin/erdos-3`  
**Version:** `0.1.0`  
**Spec version:** 3

## Protected source chain

- Forge source lock: `reports/discovery/openmath_2026/unassigned_sources/erdos-3/SOURCE_LOCK.json`
- Slot binding: `reports/discovery/openmath_2026/SLOT_BINDING.json`
- Protected source capture: `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90`
- Exact formal statement: `work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/erdos-3/PUBLIC_SOURCE/statement.lean`
- Operative README, hill manifest, evaluator, tests, and pinned Lean environment are in the same protected source capture.

## Source-derived task semantics

The hill asks for a machine-checked Lean 4 proof completing the fixed theorem `hill`. The submission supplies only the proof following the theorem's `:=`; it does not restate the theorem or add imports.

The fixed source comment states the mathematical question:

> If (Asubsetmathbb N) has divergent reciprocal sum, must (A) contain arbitrarily long arithmetic progressions?

The exact Lean statement is the protected `statement.lean`; that file, not this prose paraphrase, governs formal correctness.

The README identifies this as an open Erdős problem and a research-level conjecture.

## Formal environment

- Lean toolchain: v4.33.1.
- Pinned hill image: `ghcr.io/ottogin/lean-mathlib@sha256:964547ad81e109c78545512867bae70b710c55d833078674878faad7de0ebb85`.
- Fixed context imports `FormalConjecturesUtil`.
- Formalization source is attributed by the organizer to `google-deepmind/formal-conjectures`, Erdős Problems/3.

## Metric

`proved` — maximize; 1 only when the submitted proof passes the evaluator.

## Semantic boundary

This map does not assert the conjecture is solved, does not alter the fixed theorem, and does not treat partial related mathematics as a passing hill proof. Competition acceptance and MATHCERT certification are separate.
