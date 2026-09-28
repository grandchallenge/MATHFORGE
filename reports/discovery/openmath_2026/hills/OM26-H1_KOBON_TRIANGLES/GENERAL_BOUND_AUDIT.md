# OM26-H1 bound-source audit — general versus simple arrangements

**Audit date:** `2026-09-27`

## Why this audit exists

The AutoLab hill explicitly permits parallel lines and intersections of three or more lines. Therefore an upper bound proved only for simple affine arrangements cannot be imported as a hill-global theorem without an additional reduction.

## Source 1 — Clément–Bader general Kobon bound

Gilles Clément and Johannes Bader, *Tighter Upper Bound for the Number of Kobon Triangles* (draft, 2007), cached by OEIS at:

`https://oeis.org/A006066/a006066.pdf`

The paper defines (K(n)) as the maximal number of nonoverlapping triangles made by (n) straight lines. Its proof explicitly analyzes degenerate configurations:

- Proposition 1 counts the maximal number of points/segments in general position.
- Lemma 1 then discusses common-side triangles and points incident with more than two lines, including the loss of points/segments at multiple intersections.
- Theorem 1 concludes
  [
  K(n)le leftlfloorrac{n(n-2)}{3}ightfloor-1
  ]
  when (nequiv0,2pmod 6).

For (n=18), this gives the source-matched general upper bound

[
K(18)le 95.
]

This source is materially closer to the hill semantics than the simple-arrangement theorem because it explicitly treats multiple-line intersections and common triangle sides.

## Source 2 — Bartholdi–Blanc–Loisel simple bound

Nicolas Bartholdi, Jérémy Blanc, and Sébastien Loisel, arXiv:0706.0723v1:

`https://arxiv.org/html/0706.0723v1`

Their affine arrangement definition requires every pair of pseudo-lines to intersect exactly once, and their work is explicitly restricted to **simple** arrangements, meaning no multiple intersections. Theorem 1.1 proves, for even (n),

[
overline a_3^s(n)le leftlfloorrac{n(n-7/3)}{3}ightfloor.
]

At (n=18), this is 94.

That is a stronger bound, but its stated hypotheses do not match the hill's allowance of parallel lines and higher-order concurrence.

## Source 3 — current status index

OEIS A006066, current entry accessed 2026-09-27:

`https://oeis.org/A006066`

records (n=18) as (ge 93) with upper bound 94. This is useful status evidence, but the status row alone is not a proof object and does not resolve the hypothesis mismatch identified above.

## Forge disposition

The source-grounded state is therefore:

[
93le K_{	ext{hill}}(18)le 95
]

using the protected 93 construction benchmark and the Clément–Bader general bound.

The value 94 remains:

- the upper bound for the cited simple-arrangement theorem;
- the current OEIS-reported upper bound;
- a high-value construction target;
- **not yet admitted by Forge as a hill-global proved upper bound**.

A downstream Solve route may close the 94 question only by either:

1. sourcing a proof whose hypotheses already cover the hill semantics; or
2. proving a reduction from hill-admissible arrangements to the simple setting without decreasing the counted triangular-face total.

## Claim boundary

This audit is source/status triage. It does not certify the Clément–Bader proof, prove that 95 is tight, prove or disprove 94 as a hill-global bound, or establish optimality of the 93 construction.
