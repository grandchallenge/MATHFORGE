# OM26-H5 — Grothendieck constant witnesses: semantic source map

**Campaign binding:** OM26-H5  
**Exact organizer hill:** `alejandrozu/grothendieck-constant-witnesses`  
**Version:** `0.1.0`

## Protected source chain

- Forge source lock: `reports/discovery/openmath_2026/unassigned_sources/grothendieck-constant-witnesses/SOURCE_LOCK.json`
- Slot binding: `reports/discovery/openmath_2026/SLOT_BINDING.json`
- Protected source capture: `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90`
- Operative sources: protected README, hill manifest, evaluator, tests, and baseline witness.

## Source-derived task semantics

The source describes the real Grothendieck constant as the supremum of a vector relaxation over the corresponding signed bilinear optimization. The hill asks for an exact finite lower-bound witness, not the exact value of the constant.

A submission gives:
- a sign matrix (A);
- rational unit vectors (u_i) and (v_j).

The evaluator computes exactly
[
operatorname{sign}(A)=max_{x_i,y_jin{-1,1}}sum_{ij}A_{ij}x_i y_j
]
and the rational vector objective
[
operatorname{vector}(A;u,v)=sum_{ij}A_{ij}langle u_i,v_jangle.
]
Their ratio is a certified finite lower bound for the real Grothendieck constant.

## Submission domain

- matrix dimensions: 2–8 by 2–8;
- vector dimension: 2–16;
- matrix entries: exactly (-1) or (1);
- vector coordinates: canonical rational pairs with positive denominators and numerator/denominator magnitude at most (10^6);
- every submitted vector must have exact squared norm one.

## Metrics

1. `gap_ppm` — maximize the certified ratio scaled by one million.
2. `matrix_area` — minimize.
3. `certificate_bits` — minimize.

## Semantic boundary

A passing witness establishes only its exact finite lower bound. It does not determine the exact Grothendieck constant, establish global optimality, prove novelty, authorize competition acceptance, or create MATHCERT certification.
