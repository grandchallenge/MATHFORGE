# OM26-H6 — 3×3 matrix multiplication tensor: semantic source map

**Campaign binding:** OM26-H6  
**Exact organizer hill:** `alejandrozu/matrix-multiplication-tensor-3x3`  
**Version:** `0.1.0`

## Protected source chain

- Forge source lock: `reports/discovery/openmath_2026/unassigned_sources/matrix-multiplication-tensor-3x3/SOURCE_LOCK.json`
- Slot binding: `reports/discovery/openmath_2026/SLOT_BINDING.json`
- Protected source capture: `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90`
- Operative sources: protected README, hill manifest, exact evaluator, tests, and baseline decomposition.

## Source-derived mathematical target

Construct an exact rational bilinear algorithm for multiplying two arbitrary (3	imes3) matrices.

A submission gives factor matrices `u`, `v`, and `w`. Each row defines one bilinear product. The evaluator expands the submitted decomposition over (mathbb{Q}) and checks the complete tensor identity through all 729 Brent identities.

The protected README states:
- rank 23 is known;
- the supplied baseline is Laderman's rank-23 decomposition;
- the longstanding open problem is whether the tensor has rank at most 22.

The source treats a rank-22 certificate as a major result and a new exact rank-23 decomposition with lower support as meaningful hill progress.

## Metrics

1. `rank` — minimize.
2. `support` — minimize as a compactness tie-breaker.

## Coordinate conventions

- A and B input coordinates are row-major.
- W uses the source-stated column-major output coordinate (3cdot	ext{column}+	ext{row}).
- coefficients are exact rationals.

## Semantic boundary

A passing decomposition proves the exact submitted tensor identity. It does not establish a lower bound on tensor rank, novelty, competition acceptance, or MATHCERT certification.
