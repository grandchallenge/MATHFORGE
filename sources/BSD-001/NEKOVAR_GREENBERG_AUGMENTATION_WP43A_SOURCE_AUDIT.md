# BSD-001 source audit — Nekovář Greenberg augmentation/Bockstein naturality

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP43A-GREENBERG-AUGMENTATION-NATURALITY`.
- Protected MATHFORGE predecessor: `a014559b89897bcfa2078147224e598ab6aaedca`.
- Protected MATHSOLVE predecessor: `3463858d6281bcc2030d11f7f9af76c9f9097ff9`.
- Primary source: Jan Nekovář, *Selmer complexes*, Astérisque 310 (2006), Introduction §0.16, especially (0.16.0.1); Chapters 6–8 remain the detailed formal background.
- Official bibliographic identity: DOI `10.24033/ast.717`, NUMDAM item `AST_2006__310__R1_0`.
- Disposition: `QUALIFIED_GREENBERG_AUGMENTATION_BOCKSTEIN_NATURALITY`.
- Claim class: source/formal-compatibility admission only; no classical-Kummer comparison, height nondegeneracy, BSD, or certification promotion.

## Source-access note

The official NUMDAM/SMF source surface and searchable text were inspected. The full official PDF is too large for the current web renderer; direct opening and page-image rendering of the relevant printed page failed. The official searchable source nevertheless exposes the exact §0.16 text and equation locator. A smaller official SMF sample was rendered successfully and independently confirms the book identity and that §0.16 is the generalized-height section. This audit therefore binds the official edition and exact section/equation locator, but does not claim a successful page-image lock for printed page 23 or an independently recomputed PDF digest.

## Downstream question

Protected WP41A separates two operations:

1. cyclotomic deformation/Bockstein of the strict Greenberg Selmer complex;
2. fixed-level change of local condition from strict Greenberg to classical Kummer, whose finite defect is dualized in WP40 as `D_K`.

The open compatibility boundary is

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`.

The narrow source question here is only:

> Does Nekovář's own formalism make the **Greenberg/strict side** functorial for the cyclotomic augmentation triangle, so that its Bockstein is genuinely the connecting morphism of an exact triangle of Selmer complexes rather than an ad hoc cohomology map?

This audit does not ask whether a classical-Kummer Iwasawa comparison complex exists.

## §0.16 augmentation triangle

Let `R` be the coefficient ring in Nekovář's Iwasawa setup, let `J` be the augmentation ideal, and let the cyclotomic tangent module be the rank-one augmentation quotient represented in the source by `J/J^2` / `Gamma_R` notation.

Section 0.16 begins from the canonical augmentation exact triangle for the cyclotomic deformation of the Galois representation. In the source notation, the middle term is the first-order quotient modulo `J^2`, the right term is the specialization modulo `J`, and the connecting morphism takes values in the specialized representation tensored with the cyclotomic tangent direction.

The key source statement is then formal and explicit: Greenberg local conditions induced on the three terms are compatible with that augmentation triangle, and the associated Selmer complexes themselves form an exact triangle. The source immediately identifies the resulting connecting morphism on the specialized Selmer complex as the Bockstein used in the generalized height pairing.

Thus, for Greenberg local conditions, the cyclotomic Bockstein is natural at the **Selmer-complex** level.

## Literal `p=2` applicability in the protected lane

Protected MATHFORGE WP37 already admits Nekovář's Selmer-complex duality/Bockstein-height formalism literally at `p=2` over the protected totally imaginary field `K`. The present audit adds no new odd-prime specialization: it records the formal augmentation compatibility inside the same Nekovář setup.

Consequently MATHSOLVE may use, for the protected `K`-side strict Greenberg complex, a source-qualified exact augmentation triangle

`C_str ⊗ tangent -> C_str,first-order -> C_str -> (C_str ⊗ tangent)[1]`

whose connecting morphism is the WP37 first cyclotomic Bockstein, with notation adapted from Nekovář's `(0.16.0.1)`.

## What this closes in WP41A

The strict-side uncertainty is closed:

- one does not need to separately prove that the Greenberg local conditions survive first-order cyclotomic augmentation;
- one does not need to separately prove that the resulting Selmer complexes form an exact triangle;
- one does not need to guess that the height Bockstein is natural with respect to that strict Greenberg augmentation triangle.

These are source facts in Nekovář's formalism.

## What remains missing

The source statement above does **not** supply the second local-condition structure needed by BSD-001.

In particular, this audit does not admit:

1. an integral cyclotomic Selmer complex over `K` whose finite-level local condition is the classical Kummer condition used in WP39;
2. a morphism from the strict Greenberg Iwasawa Selmer complex to such a classical-Kummer Iwasawa complex;
3. a comparison cone whose derived specialization at augmentation is exactly WP39's finite quotient `R_K=U_Kum/U_str`;
4. an identification of the specialized dual comparison image with WP40's `D_K`;
5. a resulting equality of `D_K` with a Bockstein image, kernel, cokernel, or height radical.

Nekovář's own Introduction §0.19.2 explicitly presents local conditions beyond Greenberg's as an area requiring further development; this is consistent with, but is not used as, a theorem-nonexistence statement.

## Refined downstream boundary

The former broad boundary

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`

can now be sharpened to

`MISSING_P2_KUMMER_IWASAWA_LOCAL_CONDITION_COMPLEX_AND_SPECIALIZATION_OVER_K`.

The Greenberg augmentation/Bockstein half is source-qualified. The missing object is the integral classical-Kummer cyclotomic comparison and its exact derived specialization.

## Exact downstream interface after protection

MATHSOLVE may use the following bounded statements.

1. In the protected literal-`p=2`, totally-imaginary `K` lane, the strict Greenberg Selmer complex is functorial under Nekovář's first-order cyclotomic augmentation triangle.
2. The induced Selmer complexes form an exact triangle.
3. The connecting morphism on specialization is the cyclotomic Bockstein used in the WP37 generalized height pairing.
4. No classical-Kummer Iwasawa comparison is supplied by this admission.

## Claim firewall

This audit does not prove:

- existence of the missing classical-Kummer Iwasawa Selmer complex/comparison over `K`;
- `D_K` equals any Bockstein or height defect;
- fixed-`2` height nondegeneracy;
- a height-one `(2)` analytic determinant generator;
- the remaining Disegni `Q^ord` factors;
- the WP00 real normalization or final quadratic descent;
- `BSD-R2-A1`;
- theorem nonexistence, MATHCERT certification, novelty, or priority.