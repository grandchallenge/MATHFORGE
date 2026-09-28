# OM26-H6 — evaluator contract

**Protected evaluator:** `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90:work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/matrix-multiplication-tensor-3x3/PUBLIC_SOURCE/eval.py`

## Input contract

`solution.json` contains only `u`, `v`, and `w`.

- all three factors have the same row count;
- row count is 1–40;
- every row has exactly 9 coefficients;
- each coefficient is an integer or exact `[numerator, denominator]` rational;
- denominator is positive; numerator magnitude and denominator are at most (10^6);
- maximum JSON size is 262,144 bytes.

## Exact tensor verification

The evaluator checks, for each of 9 A coordinates, 9 B coordinates, and 9 C coordinates, that the submitted rank-one sum equals the target multiplication tensor coefficient. That is all (9^3=729) Brent identities over exact `Fraction` arithmetic.

It then replays a nonempty private validation/test set of concrete integer matrix products as an additional regression check.

## Metrics

- `rank`: number of rows / bilinear products, minimize;
- `support`: total nonzero coefficients across U, V, W, minimize.

## Trust boundary

Passing certifies the exact submitted bilinear decomposition under the fixed coordinate conventions. It does not prove minimal rank, novelty, competition acceptance, or MATHCERT certification.
