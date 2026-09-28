# OM26-H5 — evaluator contract

**Protected evaluator:** `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90:work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/grothendieck-constant-witnesses/PUBLIC_SOURCE/eval.py`

## Input contract

`solution.json` contains exactly:
- `matrix`;
- `left_vectors`;
- `right_vectors`.

The matrix is rectangular, 2–8 rows by 2–8 columns, with entries exactly (-1) or (1). Left/right vector counts match the matrix dimensions. All vectors share a dimension 2–16.

Each coordinate is a canonical reduced rational pair `[numerator, denominator]`, denominator positive, numerator and denominator bounded in magnitude by (10^6). Every vector must have exact squared Euclidean norm one.

Maximum JSON size: 262,144 bytes.

## Exact verification

The evaluator:
1. computes the signed bilinear optimum exactly by exhaustive enumeration of one sign side and the closed-form best response of the other;
2. computes every vector dot product and objective using `Fraction`;
3. requires positive submitted vector objective;
4. forms the exact ratio `objective / sign_optimum`.

Validation/final private files contain disjoint rational arithmetic fixtures that guard evaluator correctness; they are not hidden target matrices.

## Metrics

- `gap_ppm = floor(1_000_000 * ratio)`, maximize;
- `matrix_area`, minimize;
- `certificate_bits`, minimize.

## Trust boundary

Passing certifies the submitted finite rational witness and reported ratio under this evaluator. It does not establish optimality, the exact constant, novelty, competition acceptance, or MATHCERT certification.
