# OM26-H7 — evaluator contract

**Protected evaluator:** `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90:work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/erdos-3/PUBLIC_SOURCE/eval.py`

## Submission contract

The submission directory contains `solution.lean`, consisting only of the proof term or `by` tactic block that follows the fixed theorem's `:=`.

The evaluator concatenates:
1. protected `statement.lean`;
2. submitted proof text;
3. `#print axioms hill`.

## Pinned formal environment

- Lean 4 toolchain v4.33.1.
- Hill image `ghcr.io/ottogin/lean-mathlib@sha256:964547ad81e109c78545512867bae70b710c55d833078674878faad7de0ebb85`.
- Lean compile timeout inside evaluator: 1500 seconds.
- Hill watchdog: 1800 seconds.

## Acceptance

The proof must:
- compile successfully;
- not use `sorry`;
- depend on no axioms beyond the allowed set `propext`, `Classical.choice`, and `Quot.sound`.

The evaluator parses Lean's reported axiom list and rejects extra axioms.

## Metric

A passing proof returns `proved=1`.

## Trust boundary

Passing establishes machine acceptance of the submitted proof for the exact protected formal statement in the pinned environment. It does not by itself establish novelty, organizer/jury acceptance, or MATHCERT certification.
