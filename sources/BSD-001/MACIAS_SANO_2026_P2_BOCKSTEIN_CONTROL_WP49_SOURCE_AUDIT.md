# BSD-001 source audit — Macias Castillo–Sano 2026 Selmer/Poitou–Tate and derived-height applicability at `p=2`

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP49A-BOCKSTEIN-CONTROL-QUOTIENT`.
- Protected MATHFORGE predecessor: `4306aaeef25ac0923e4442ca1c8c1068ed55b514`.
- Protected MATHSOLVE predecessor: `05a45bd103d33ee828df9f3ff6050a895635a6d7`.
- Source: Daniel Macias Castillo and Takamichi Sano, *On Selmer complexes, Stark systems and derived p-adic heights*, arXiv:2603.23978 (2026).
- Primary source inspected: arXiv experimental HTML/full text and abstract page.
- Disposition: `QUALIFIED_ODD_PRIME_COMPARATOR_NOT_LITERAL_P2`.
- Claim class: bounded source/applicability result only; no theorem-nonexistence, BSD, or certification promotion.

## Downstream question

Protected WP48A has already constructed, at literal `p=2`, the exact global strict/Kummer derived comparison cone and recovered protected `J_K` and `D_K` on that surface.

The remaining D2b question asks whether a source theorem identifies the resulting finite global control quotient with a canonical Bockstein/height subquotient, preferably through a Selmer-complex/Poitou–Tate comparison.

The Macias Castillo–Sano paper is the closest contemporary source located in the bounded WP49 screen because it:

- proves a canonical comparison between Nekovar Selmer complexes and Poitou–Tate complexes;
- relates determinants of Selmer complexes to Stark systems;
- compares derived p-adic heights with Nekovar's higher-height formalism.

## Prime-range barrier

The source explicitly states at the start of §1.2:

> `Let p be a prime number. For simplicity, we assume that p is odd throughout this article.`

This is a global standing hypothesis for the article, not a hypothesis inserted only in a later application.

Accordingly, its Selmer/Poitou–Tate comparison theorem (Theorem 1.1 / Theorem 2.20 in the paper's numbering) and its derived-height comparison results are proved inside an odd-prime framework.

Therefore they cannot be specialized mechanically to the selected literal-`p=2` BSD-001 branch.

## Exact positive content retained as comparator

The source is relevant as an odd-prime structural comparator. It shows that, under its hypotheses, one can canonically compare Nekovar Selmer complexes with Poitou–Tate complexes and use this comparison in derived-height calculations.

This confirms that the mathematical shape sought by WP49A is natural. It does **not** supply the required `p=2` theorem.

## What this source does not establish for BSD-001

This source does not establish, on the protected selected branch:

- a literal-`p=2` Selmer-complex/Poitou–Tate quasi-isomorphism under the WP48A local conditions;
- a literal-`p=2` identification of the WP40 annihilator `D_K` with a Bockstein image, cokernel, radical, or derived-height subquotient;
- fixed-`2` height nondegeneracy;
- the height-one `(2)` analytic determinant generator;
- any remaining Disegni/WP00/descent normalization;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

## Provider conclusion

Macias Castillo–Sano 2026 is a strong structural comparator but is unavailable as direct authority for the remaining WP49 literal-`p=2` bridge because the paper assumes `p` odd throughout.

**Disposition:** `QUALIFIED_ODD_PRIME_COMPARATOR_NOT_LITERAL_P2`.

This is an applicability result for this source, not a theorem that no literal-`p=2` bridge exists elsewhere.
