# BSD-001 source audit — Perrin–Riou 1987 ordinary rank-one formula and literal `p=2`

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#153`.
- Protected Forge baseline: `c8251ba36184d72de431b2c9c3f4f17e601b6f53`.
- Downstream protected MATHSOLVE baseline: `6bfb41402f216069b3b5ed001320170cc411b6cf`.
- Trigger: protected BKS audit, Remark 6.8 successor pointer to Bernadette Perrin–Riou, *Points de Heegner et dérivées de fonctions L p-adiques*, Invent. Math. 89 (1987), 455–510, especially Corollary 1.8.
- Disposition: `NO_LITERAL_P2_ADMISSION_FROM_PERRIN_RIOU_1987_SOURCE_FAMILY`.
- Claim class: bounded source/applicability evidence only. No theorem-nonexistence, BSD, novelty, or certification claim.

## Exact downstream query

Protected WP20 split the selected theorem debt into:

- D1: `MISSING_P2_PRIMITIVE_RANK1_DETERMINANT_REALIZATION`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

BKS Remark 6.8 states that the ordinary rank-one formula underlying its D2 architecture was proved by Perrin–Riou, citing Invent. Math. 89 (1987), Corollary 1.8. This audit asks only whether that source pointer licenses literal `p=2` use.

## Source-access discipline

The current source path resolved bibliographic metadata for the Inventiones article, but did not provide the full text of Corollary 1.8 itself. This audit therefore does **not** claim direct inspection of the corollary's printed hypothesis line.

Instead, two accessible primary Perrin–Riou papers from the same 1987 Heegner/Iwasawa programme were inspected for the ambient prime convention.

### Primary companion A — Astérisque 147–148 (1987)

Bernadette Perrin–Riou, *Fonctions L p-adiques et points de Heegner*, Astérisque 147–148 (1987), 151–171.

At the opening of the paper Perrin–Riou fixes

> `p` a prime number that is odd, with `E` ordinary at `p`.

The paper then develops the ordinary two-variable `p`-adic `L`-function/Heegner-point setup, its derivative conjecture, and the connection with `p`-adic BSD inside that standing prime range.

### Primary companion B — Bulletin SMF 115 (1987)

Bernadette Perrin–Riou, *Fonctions L p-adiques, théorie d'Iwasawa et points de Heegner*, Bull. Soc. Math. France 115 (1987), 399–456.

Section 1 likewise begins by fixing an imaginary quadratic field `k` and an **odd prime `p`**. The paper later explicitly invokes the oddness of `p` in a descent/functoriality step.

This is not incidental notation: the odd-prime condition is part of the ambient 1987 Heegner/Iwasawa formalism used by these accessible primary sources.

## Provider consequence for BKS Remark 6.8

The accessible primary evidence does not support deleting the odd-prime hypothesis when following BKS's historical pointer back to Perrin–Riou.

Accordingly, the provider may use Perrin–Riou 1987 as historical and architectural evidence that an ordinary rank-one `p`-adic Gross–Zagier/height formula exists in the classical odd-prime setting. It may **not** admit the cited Corollary 1.8 as a literal `p=2` theorem premise on the basis of the current source record.

This conclusion is deliberately narrower than saying that the Inventiones corollary itself has been directly verified to print `p` odd. The direct corollary text was not acquired in this operation. The correct governed statement is:

`NO_SOURCE_BASIS_TO_ADMIT_PERRIN_RIOU_COR_1_8_AT_P2`.

## Why this does not close D2

Even if a future source supplied a literal `p=2` ordinary Gross–Zagier formula, protected D2 would still require an exact composition with the WP20 Bockstein ideal and the WP00 normalization. In particular it would have to retain every `2`-adic contribution from:

- the ordinary/unit-root interpolation factors at `2`;
- the choice and normalization of the `p`-adic height;
- the comparison of that height/Bockstein scalar with the protected rank-one free direction;
- the complex Néron–Tate regulator;
- the whole-real-locus minimal-model period;
- primitive versus imprimitive Euler factors;
- the WP13 even-Tamagawa/residual-conductor-drop terms;
- derivative-parameter normalization and any finite lattice index.

No such literal-`p=2` exact composition is admitted here.

## Consequence for theorem construction

The historical Perrin–Riou shortcut is closed as a **source substitution** under the present evidence. It does not close the mathematical route.

The next constructive work should therefore proceed independently on the two WP20 obligations rather than continue widening historical Gross–Zagier searches:

1. construct a literal `p=2` primitive Selmer-complex/determinant realization whose specialization is exactly the protected `X_E`, or isolate the smallest missing theorem needed for such a construction;
2. separately construct the rank-one Bockstein/height comparison at `p=2`, retaining all local and normalization defects explicitly.

## Claim firewall

This audit does not prove:

- that Perrin–Riou's Inventiones Corollary 1.8 has been directly read in this operation;
- that no `p=2` Gross–Zagier formula exists elsewhere;
- D1 or D2;
- equality between an ordinary/Greenberg Selmer object and the protected primitive Kummer module;
- equality of a `p`-adic Bockstein regulator with the WP00 Néron–Tate regulator;
- the selected first-Fitting reciprocity theorem;
- `BSD-R2-A1`;
- any MATHCERT disposition.
