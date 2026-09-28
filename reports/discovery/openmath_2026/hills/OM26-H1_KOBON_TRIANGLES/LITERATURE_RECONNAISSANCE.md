# OM26-H1 literature reconnaissance — Kobon triangles

**Reconnaissance date:** `2026-09-27`

Current public literature gives a materially stronger target than the current GCL campaign leader.

## Current external benchmark

Bartholdi, Blanc, and Loisel, arXiv:0706.0723v1, give for even n the affine simple-pseudoline upper bound `floor(n(n - 7/3)/3)`. At n=18 this is 94. Their Theorem 1.4 table records affine n=18 as `93–94`, and its legend states that bold entries are known to be stretchable; the 93 entry is bold.

OEIS A006066, accessed 2026-09-27 and internally timestamped 2026-09-14, records `n=18: >=93, upper bound 94 [Bader]`.

The LineOrder Kobon gallery presents an explicit order table titled `18-Line Solution (93 Triangles) by Johannes Bader`. This is a useful order-type target, not an AutoLab submission: the hill requires actual straight-line coefficients.

Pavlo Savchuk, arXiv:2507.07951 (2025), describes table encoding, SAT search, and heuristic straightening of pseudoline arrangements into straight-line arrangements. This is directly relevant to reconstructing the 93 target.

## Admitted consequences

- Current external sources report a straight-line-realizable 93-triangle arrangement at n=18.
- The cited simple-arrangement literature gives 94 as the n=18 upper bound under its hypotheses.
- The protected GCL campaign leader at 86 is below the external 93 construction benchmark.
- The Bader 93 order table is a high-value realization/straightening target.

## Qualifications

- This record does not prove that 93 is the current global best under every variant of the hill.
- It does not yet import 94 as a hill-global upper bound because the hill permits parallel lines and multiple concurrence whereas the cited theorem is stated for simple affine arrangements.
- It does not establish that the line-order table alone is a valid hill submission.
- It does not provide rational coefficients for the 93 arrangement.
- It makes no novelty, priority, optimality, competition-acceptance, or MATHCERT claim.

## Research consequence

Primary next route: reconstruct the published 93 order table as actual rational straight lines and exact-replay it under the hill evaluator. Retain exact local search from 86 as an independent secondary route. Separately audit whether the simple-arrangement 94 bound transfers to the hill's degeneracy semantics.

## Sources

- https://arxiv.org/abs/0706.0723
- https://arxiv.org/html/0706.0723v1
- https://oeis.org/A006066
- https://oeis.org/A006066/internal
- https://zegalur.github.io/line-order/gallery/kobon.html
- https://arxiv.org/abs/2507.07951


## General-versus-simple bound audit

A follow-up source audit distinguishes two upper bounds that must not be conflated.

- Clément–Bader (2007) treats the general Kobon quantity (K(n)), explicitly discusses multiple-line intersections/common-side triangles, and gives (K(18)le 95).
- Bartholdi–Blanc–Loisel (2007) gives the stronger value 94 only under its simple affine arrangement hypotheses.
- OEIS currently reports 94 for (n=18), but the status row is not itself a hill-semantic proof.

Accordingly, Forge currently admits the source-grounded interval (93le K_{hill}(18)le95). The value 94 remains a target and reported status, not a Forge-admitted hill-global theorem.

See `GENERAL_BOUND_AUDIT.md`.
