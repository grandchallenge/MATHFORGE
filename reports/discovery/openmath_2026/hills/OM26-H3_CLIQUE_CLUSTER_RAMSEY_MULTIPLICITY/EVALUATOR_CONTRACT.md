# OM26-H3 — evaluator contract

**Protected evaluator:** `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90:work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/clique-cluster-ramsey-multiplicity/PUBLIC_SOURCE/eval.py`

## Certificate schema

`solution.json` contains exactly:
- `schema = "weighted-two-color-blowup-v1"`;
- `weights`: 1–1024 positive integer weights, each at most 65535;
- `red_rows`: a symmetric square binary matrix encoded as strings.

The diagonal is semantically meaningful. Common weight gcd is divided out before evaluation.

## Exact objective

The evaluator computes exact red and blue weighted homomorphism counts for (K_4), including repeated template indices, and divides by (Q^4). Computation and comparison use integer/rational arithmetic.

Reference:
[
B^*=10486266368/768^4.
]

The evaluator sets `reference_beaten=1` exactly when (P<B^*). `density_ppt` is the integer ceiling of (10^{12}P).

## Audit and resources

- Candidate size limit: 4 MiB.
- Exact verification internal budget: 480 seconds; hill watchdog: 600 seconds.
- Validation/final private data are disjoint small arithmetic fixtures that audit the trusted counter. They do not alter candidate (P).
- Submission code is not executed.

## Trust boundary

A passing certificate establishes its exact blow-up density under the supplied counting/lifting semantics. Resource failure is not a mathematical impossibility result. Passing or beating the frozen reference does not by itself establish novelty, competition acceptance, full parent-problem resolution, or MATHCERT certification.
