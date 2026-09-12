# BSD-001 source audit — Nekovář literal-`p=2` imaginary-quadratic Bockstein-height interface

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP37-P2-IMAGINARY-QUADRATIC-BOCKSTEIN-HEIGHT`.
- Protected MATHFORGE baseline: `92fcd8596e59aa8331b2450ea66c14786581806e`.
- Protected MATHSOLVE baseline: `09c90178c71cfe295d526d7a420e3f8c43f062d4`.
- Primary source: Jan Nekovář, *Selmer complexes*, Astérisque 310 (2006), viii+559, DOI `10.24033/ast.717`.
- Primary public edition inspected through the official NUMDAM source surface: `https://www.numdam.org/item/AST_2006__310__R1_0/` and the linked volume PDF.
- Exact source loci used: §8.5 opening hypothesis; §11.1.3–11.1.6 (cyclotomic Bockstein and height); §11.6.7–11.6.8 (order of vanishing and leading term over a DVR); §11.7.1 and Proposition 11.7.6 (BSD-type descent formalism).
- Corroborating author source: Jan Nekovář, Banff lecture notes, Theorem 5.5, which states the same `p>2`-or-totally-imaginary hypothesis for the Selmer-complex height pairing.
- Disposition: `QUALIFIED_LITERAL_P2_TOTALLY_IMAGINARY_BOCKSTEIN_HEIGHT_INTERFACE`.
- Claim class: source/applicability admission only; no D1c, D2, BSD, or MATHCERT promotion.

## Source-lock note

The official NUMDAM bibliographic identity and source text were inspected through the current web source surface. Direct independent byte download of the PDF failed in the present execution environment, so this record does not claim an independently recomputed PDF digest. This is a provenance limitation only; the admitted interface below is bound to the official Astérisque/NUMDAM edition, DOI, and exact section/theorem locators.

## Question

Protected WP36 leaves two principal determinant-side obligations:

- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

Over `Q`, Burns–Macias Castillo give a literal-`p=2` perfect Selmer complex, but their arithmetic height comparison does not identify the `p=2` Bockstein exactly with the classical Selmer/regulator normalization. Protected WP09 already supplies an imaginary quadratic field `K` in which `2` and all primes dividing `N` split and `E/K` has analytic rank one.

The precise source question is therefore:

> Does Nekovář's original Selmer-complex formalism itself admit the cyclotomic Bockstein-height construction at `p=2` when the base field is the protected totally imaginary field `K`, and if so, what integral information does it give without importing an odd-prime theorem?

## Literal `p=2` range over a totally imaginary field

Nekovář's Iwasawa-duality setup in §8.5 explicitly works with `K` totally imaginary when `p=2`; the text identifies this as the condition needed to satisfy the standing duality hypothesis `(P)`.

The author's Banff summary states the corresponding height theorem transparently: in the Selmer-complex setup, assume either

`p > 2`

or

`K is totally imaginary`.

Then, for every continuous cyclotomic/Iwasawa character `ell`, there is a Selmer-complex height pairing. Therefore `p=2` is not excluded when `K` is imaginary quadratic.

This point is materially different from the already-screened later papers that impose `p` odd globally. The protected WP09 field `K` is imaginary quadratic, so it lies on the literal `p=2` branch of Nekovář's own formalism.

## The height is a Bockstein construction, not an analogy

In §11.1.3 Nekovář constructs the Bockstein morphism from the augmentation extension for the chosen `Z_p`-extension. In §11.1.4 the height morphism is defined as the composite

`RΓ_f(X) --β--> RΓ_f(X)[1] ⊗ Γ_R`

followed by Selmer-complex duality against the dual local conditions.

On cohomology, the principal pairing is

`h_{π,1,1}: H~^1_f(X) ⊗ H~^1_f(Y) -> H^0(ω_R) ⊗ Γ_R`.

Thus, on the literal-`p=2`, totally imaginary branch, the source directly identifies the Nekovář height pairing as the pairing induced by the cyclotomic Bockstein morphism. No specialization of an odd-prime theorem is needed for this formal identification.

For the BSD-001 application, take `R=Z_2`, `X=T_2(E)` and the self-dual `Y=T_2(E)` identified through the Weil pairing, with source-compatible dual Greenberg local conditions. Since the selected auxiliary field is totally imaginary, there is no real-place obstruction of the kind present over `Q`.

## Exact leading-term information supplied by §§11.6–11.7

For a DVR `A` and `Λ=A[[T]]`, §11.6.7 writes the characteristic power series of a finitely generated torsion `Λ`-module as

`char_Λ(H) = T^{r(H)} char_Λ^*(H)`

and defines the leading term

`char_Λ^*(H)(0) in Frac(A)^*/A^*`.

Lemma 11.6.8 then gives the exact valuation identity

`a_A(H) = ord_A(char_Λ^*(H)(0))`.

In §11.7 the BSD-type descent formalism applies this Bockstein spectral sequence to Selmer complexes. Proposition 11.7.6 gives, after the stated perfect-duality/local-orthogonality/low-degree-vanishing hypotheses, exact length statements and identifies nondegeneracy of the first height with the minimal leading-order behavior.

For `A=Z_2`, this is genuine `2`-adic length information. It is not merely a parity statement or an equality modulo squares.

However, the source's leading term is a characteristic-module leading term defined only modulo `A^*`. Consequently, §§11.6–11.7 determine its `2`-adic valuation exactly, but do not by themselves choose a canonical determinant-line generator in `Z_2`. This distinction matters for D1c.

## What is immediately supportable downstream

After protected admission, BSD-001 may use the following bounded interface.

1. Over the protected WP09 imaginary quadratic field `K`, Nekovář's Selmer-complex duality and height formalism applies literally at `p=2` because `K` is totally imaginary.
2. For the cyclotomic `Z_2`-extension, the Nekovář height is induced by the cyclotomic Bockstein morphism followed by Selmer-complex duality.
3. The formalism is integral over `Z_2` at the level of the Selmer complex and the resulting `Z_2`-valued height object, subject to the source's local-condition and finiteness/perfectness hypotheses.
4. The Bockstein spectral sequence and Proposition 11.7.6 give exact valuation/length control of the leading term of the relevant algebraic characteristic module once the source hypotheses and the arithmetic Selmer-complex identifications are verified.
5. The totally imaginary base removes the specifically real-place `p=2` duality obstruction. It does not remove finite local-condition comparison factors at the places above `2` or at bad primes.

## Comparison with protected WP09 Disegni

Protected WP09 already admits Disegni's corrected universal `p`-adic Gross–Zagier theorem literally at `p=2` for the same all-split auxiliary imaginary quadratic lane, subject to its automorphic/test-vector normalization.

The two admitted interfaces are therefore composable in principle:

`cyclotomic Bockstein`
`-> Nekovář p-adic height over K`
`-> Disegni p-adic L-derivative over K`.

This is a real narrowing of D2. It removes the former question whether the Bockstein-height formalism itself exists at `p=2` in the preferred imaginary-quadratic lane.

It does **not** yet prove the equality needed by BSD-001, because the following comparisons remain explicit mathematical obligations.

## Remaining integral and normalization defects

### 1. Local-condition identification

Nekovář's §§11.1 and 11.7 descent formalism is stated for source-compatible Selmer-complex local conditions, in the BSD setting naturally Greenberg-type local conditions at primes above `2`.

Protected WP16B/WP35 use the primitive classical Kummer module `X_E` over `Q`, with the exact WP21 specialization kernel `C_E^vee` retained. A downstream proof must compare the `K`-Selmer complex used for the height to the protected primitive module after quadratic descent. This comparison cannot be replaced by the phrase “same Selmer group”.

### 2. Integral lattice of the height

The existence of a `Z_2`-valued Selmer-complex height does not by itself prove that the rank-one scalar obtained on a chosen Mordell–Weil generator is primitive in `Z_2` or that its ideal is exactly the protected WP20 Bockstein ideal. Any index between the chosen integral Selmer lattice and the Mordell–Weil/Kummer lattice contributes a power of `2` and must be computed.

### 3. Disegni normalization

Disegni's identity contains explicit interpolation, local, and test-vector factors. Their `2`-adic valuations must be reconciled with the local factors already protected in WP22–WP36. They cannot be discarded as units without proof.

### 4. WP00 real regulator

A `2`-adic height is not the WP00 Néron–Tate regulator. A downstream argument must compare two formulas involving the same Heegner point so that the point index/regulator factors cancel or are otherwise evaluated exactly. The present source supplies no direct equality

`p-adic height = Néron–Tate height`.

### 5. Quadratic descent

The result required over `Q` must descend from `K` through the protected WP06 discrepancy accounting. Every factor of `2` from restriction/corestriction, plus/minus decomposition, periods, Tamagawa factors, and the twist must survive explicitly.

### 6. D1c remains independent

Nekovář's descent formalism relates an algebraic characteristic leading term to the Bockstein regulator under its hypotheses. It does not identify the selected non-CM elliptic algebraic characteristic element with the analytic `p`-adic `L`-function at the height-one prime `(2)`.

Hence it does not close

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

## Contemporary comparator screen

A bounded current screen was also made to avoid accidentally importing a later theorem with an odd-prime restriction.

- Macias Castillo–Sano, *On Selmer complexes, Stark systems and derived p-adic heights* (2026), explicitly assumes `p` odd for simplicity; it is not admitted as a literal-`p=2` replacement.
- Sano's derived-Bockstein applications likewise use odd-prime hypotheses in the relevant arithmetic applications.
- Recent non-CM ordinary main-conjecture theorems screened in WP17C retain `p>2` or stronger odd-prime hypotheses.

These comparisons reinforce the use of Nekovář's original totally-imaginary branch rather than a silent odd-prime specialization.

## Provider conclusion

Nekovář materially advances the protected D2 route.

The source proves that over the protected imaginary quadratic field `K`, the cyclotomic Selmer-complex Bockstein and its associated height pairing are available literally at `p=2`. It also supplies exact DVR leading-term/length formalism. Therefore the prior generic obstacle “Bockstein/height theory may be odd-prime only” is closed in this auxiliary lane.

The surviving D2 problem is no longer existence of the formalism. It is an exact arithmetic comparison problem:

`NEKOVAR_P2_K_HEIGHT_TO_PROTECTED_INTEGRAL_LATTICE_AND_WP00_NORMALIZATION`.

In particular, downstream must compute the integral lattice/index, Disegni interpolation factors, and quadratic descent corrections. D1c remains open independently.

**Disposition:** `QUALIFIED_LITERAL_P2_TOTALLY_IMAGINARY_BOCKSTEIN_HEIGHT_INTERFACE`.

## Claim firewall

This source audit does not:

- close D1c;
- close D2;
- prove a `p=2` main conjecture;
- identify a characteristic element with an analytic `p`-adic L-function at `(2)`;
- identify a `p`-adic height with the WP00 Néron–Tate regulator;
- prove that any interpolation or local factor is a `2`-adic unit;
- identify Greenberg and primitive Kummer local conditions without exact comparison;
- prove `BSD-R2-A1`;
- assert novelty or priority;
- authorize MATHCERT certification.
