# OM26-H4 — evaluator contract

**Protected evaluator:** `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90:work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/collatz-modular-descent/PUBLIC_SOURCE/eval.py`

## Rule bounds

- `solution.json` maximum 262,144 bytes.
- 1–512 rules.
- `modulus_power` (k): integer 2–32.
- `residue`: odd integer in ((0,2^k)).
- 1–24 valuation exponents per rule.
- each exponent 1–32.
- duplicate rules rejected.

## Exact rule verification

For each rule the evaluator:
1. requires (kge 1+sum e_i), which stabilizes the valuation sequence over the residue class;
2. recomputes every required (v_2(3x+1));
3. checks (3^s<2^{sum e_i});
4. checks strict descent at the least representative, yielding the class-wide affine descent certificate used by the hill.

## Scoring

Validation and final modes use different private weighted odd residue targets, with modulus powers 8–12.

A target is covered when it is a subclass of a verified submitted rule.

Metrics:
- `coverage_ppm`: covered target weight / total weight, scaled to one million;
- `min_descent_ppm`: weakest exact contraction margin among rules covering a target;
- `rule_count`: number of verified submitted rules.

## Trust boundary

The evaluator proves the submitted finite residue-class certificates and scores them against private target collections. It does not prove global coverage, the Collatz conjecture, novelty, competition acceptance, or MATHCERT certification.
