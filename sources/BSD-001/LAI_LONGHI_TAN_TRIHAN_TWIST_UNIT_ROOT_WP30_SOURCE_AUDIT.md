# BSD-001 source audit — twist matrix / ordinary unit-root reconciliation at `p=2`

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP30-P2-TWIST-UNIT-ROOT-RECONCILIATION`.
- Protected MATHFORGE baseline: `2021db4f98da3d0df7cea2a37c9d9f6d4e9a4576`.
- Protected downstream MATHSOLVE baseline: `366130ecf0102ffb0fb5ea5821be4ace1b48bcc3`.
- Primary source: King Fai Lai, Ignazio Longhi, Ki-Seng Tan, Fabien Trihan, *On the Iwasawa Main Conjecture of Abelian Varieties over Function Fields*, arXiv:`1205.5945v2`, 26 April 2013; published in *Proceedings of the London Mathematical Society* 112 (2016), no. 6.
- Source locations audited: Introduction §1.1 and §1.2.2; §6.4.1, especially the definition of the twist matrix and equation (78).
- Supporting historical interface already protected: Ki-Seng Tan, *A generalized Mazur's theorem and its applications*, Trans. AMS 362 (2010), Theorem 1, as admitted in `TAN_GOOD_ORDINARY_NORM_FILTRATION_WP28_SOURCE_AUDIT.md`.
- Disposition: `QUALIFIED_P2_TWIST_MATRIX_UNIT_ROOT_RECONCILIATION`.
- Claim class: source/convention reconciliation only; no determinant, Bockstein, BSD, or certification promotion.

## Exact downstream question

Protected WP28 and WP29 use a scalar

`u in Z_2^x`

coming from Tan/Hall's one-dimensional twist matrix for the ordinary formal universal-norm quotient

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`.

Protected WP07 independently fixes

`alpha in Z_2^x`

as the unique `2`-adic unit root of

`X^2-a_2 X+2`.

WP29 deliberately proves only

`ord_2(1-u)=ord_2(1-alpha^(-1))`

through group orders. It does not identify `u` itself.

The source question is therefore precise:

> Under the Mazur/Tan twist-matrix convention used in the protected norm theorem, is the one-dimensional twist scalar exactly the ordinary unit-root Frobenius eigenvalue, and does this remain literal at `p=2`?

Lai–Longhi–Tan–Trihan answer this convention question affirmatively.

## Literal `p=2` range

The paper states at the start of §1.1:

`We fix a prime number p (p = 2 is allowed).`

No later odd-prime restriction is imposed on the local Frobenius/twist-matrix statements in §6.4.1.

Accordingly, the convention interface audited here applies literally at `p=2`.

The paper's review of elliptic curves over `Q` in §1.1.1 mentions `p>2`; that review is not the source of the present claim. The present claim uses the paper's general Frobenius/twist-matrix algebra in §6.4.1, under the paper-wide prime convention that explicitly allows `p=2`.

## Definition of the twist matrix

In §6.4.1 the source takes an ordinary abelian variety `A` over a finite field `F` of cardinality `q`.

The `p`-divisible geometric point group is identified as

`A[p^infinity] ~= (Q_p/Z_p)^g`.

The absolute Frobenius substitution

`Fr_q in Gal(Fbar/F)`

acts on this module. After choosing the above basis, its action is represented by a matrix

`u in GL_g(Z_p)`,

which the source calls the **twist matrix**.

This is the same Mazur twist-matrix convention used by Tan's ordinary universal-norm theorem. Protected WP28 already records Tan's definition of `u` as Frobenius on the reduction `p`-divisible torsion.

## Unit-root eigenvalue theorem

The source then invokes Mazur, Corollary 4.37, and states that the eigenvalues of the Frobenius endomorphism `F_q` of `A` can be ordered as

`alpha_1,...,alpha_g, beta_1=q/alpha_1,...,beta_g=q/alpha_g`,

where

`alpha_1,...,alpha_g`

are precisely the eigenvalues of the twist matrix `u`.

It further records

`alpha_i in O^x`,

`beta_i in q O`.

Thus the twist-matrix eigenvalues are exactly the `p`-adic unit-root Frobenius eigenvalues, not their inverses.

The same paper later uses the factors `alpha_i^(-1)` explicitly in its interpolation formulas, confirming that its convention distinguishes the twist eigenvalue `alpha_i` from its inverse.

## Elliptic specialization

For an elliptic curve one has `g=1`. Therefore the twist matrix is a single scalar.

Let the reduction be ordinary. The Frobenius polynomial is

`X^2-a_p X+p`.

There is a unique root of `p`-adic valuation zero. Under the source convention this root is the unique eigenvalue of `u`.

Hence, when the protected WP07 symbol `alpha` denotes the unit root of

`X^2-a_2 X+2`,

the exact convention reconciliation is

`u=alpha`.

This is an equality in `Z_2^x` under the shared Mazur/Tan Frobenius-substitution convention.

## Exact ideal consequence

Because `alpha` is a unit,

`1-alpha^(-1) = -alpha^(-1)(1-alpha)`.

Therefore

`(1-u)Z_2
 = (1-alpha)Z_2
 = (1-alpha^(-1))Z_2`.

This is an exact equality of principal ideals, not merely equality of valuations.

Consequently the protected WP29 toroidal quotient may be written equivalently as

`Gamma_2/(1-alpha)Gamma_2`

or

`Gamma_2/(1-alpha^(-1))Gamma_2`,

provided the quotient is understood only up to the evident unit automorphism when switching the generator `(1-alpha)` to `(1-alpha^(-1))`.

The protected WP29 truncated element-order invariant is therefore unchanged by replacing the modulus `(1-u)` with either unit-root normalization.

## Relation to the protected WP07 interpolation factor

Protected WP07 uses the normalization-specific local multiplier

`e_2(E)=(1-alpha^(-1))^2`.

The present source reconciliation proves that each one-dimensional Hall/Tan formal norm modulus is the same principal ideal as one factor `(1-alpha^(-1))`.

Thus the square of the formal-norm modulus ideal equals the WP07 local multiplier ideal:

`(1-u)^2 Z_2 = e_2(E) Z_2`.

This is an **ideal-level local normalization concordance**.

It does not prove that a future arithmetic determinant contains, cancels, or differentiates this factor in any specified way.

## What this source does not establish

This source does not establish:

- a value of the protected `tau_form(P)`;
- a canonical scalar representative of the protected toroidal class;
- a formula for that class in terms of a formal logarithm;
- a relation between the selected element class and a p-adic height or regulator;
- a Bockstein comparison;
- a primitive Kummer determinant realization;
- a height-one `(2)` main-conjecture theorem for the selected non-CM number-field branch;
- D1a, D1c, or D2;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

## Provider conclusion

Lai–Longhi–Tan–Trihan provide a literal-`p=2` source interface fixing the Mazur/Tan twist-matrix convention. In the one-dimensional ordinary elliptic specialization, the twist scalar is exactly the unique `2`-adic unit root:

`u=alpha`.

Therefore

`(1-u)=(1-alpha)=(1-alpha^(-1))`

as principal `Z_2` ideals, and the protected WP29 formal norm modulus is exactly concordant, at ideal level, with one factor of the protected WP07 local interpolation multiplier.

**Disposition:** `QUALIFIED_P2_TWIST_MATRIX_UNIT_ROOT_RECONCILIATION`.

## Claim firewall

This audit is a convention/source reconciliation only. It does not evaluate the selected toroidal class and does not close any BSD, determinant, Bockstein, or certification obligation.
