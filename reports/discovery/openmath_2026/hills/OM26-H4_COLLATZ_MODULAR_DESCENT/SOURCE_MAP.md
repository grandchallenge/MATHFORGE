# OM26-H4 — Collatz modular descent: semantic source map

**Campaign binding:** OM26-H4  
**Exact organizer hill:** `alejandrozu/collatz-modular-descent`  
**Version:** `0.1.0`

## Protected source chain

- Forge source lock: `reports/discovery/openmath_2026/unassigned_sources/collatz-modular-descent/SOURCE_LOCK.json`
- Slot binding: `reports/discovery/openmath_2026/SLOT_BINDING.json`
- Protected source capture: `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90`
- Operative sources: protected README, hill manifest, evaluator, tests, and baseline certificate.

## Source-derived task semantics

For odd (n), the source defines the accelerated odd Collatz step
[
C(n)=(3n+1)/2^{v_2(3n+1)}.
]

A submitted rule fixes an odd residue class (nequiv rpmod{2^k}) and a finite list of exact 2-adic valuations encountered by repeated accelerated steps.

The evaluator verifies that the valuation pattern is stable throughout the residue class and that the resulting affine iterate strictly decreases every positive member of the class. The hill then measures how much private target residue mass is covered by the submitted exact rules.

## Submission object

`solution.json` contains only `rules`. Each rule has:
- `modulus_power`;
- odd `residue`;
- nonempty `exponents` list.

## Metrics

1. `coverage_ppm` — maximize.
2. `min_descent_ppm` — maximize.
3. `rule_count` — minimize.

## Semantic boundary

The README explicitly states that this is a finite modular-descent component, not a solution of the Collatz conjecture. A high score means a larger exact collection of descent lemmas under the private target distribution.
