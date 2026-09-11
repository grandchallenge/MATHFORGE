# BSD-001 source audit — Silverman deep formal logarithm at p=2

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP36-FINITE-FORMAL-NORM-MEMBERSHIP`.
- Protected MATHFORGE baseline: `4cf5f8838541fb15296619ead3aaaf298198fe65`.
- Protected MATHSOLVE baseline: `757da986335a11a847bf31b396396729e1e7e983`.
- Primary source: Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, second edition, Graduate Texts in Mathematics 106, Springer, 2009, Chapter IV, Theorem 6.4.
- Source identifier: Springer DOI `10.1007/978-0-387-09494-6`.
- Disposition: `QUALIFIED_P2_DEEP_FORMAL_LOG_NORM_LINEARIZATION`.
- Claim class: bounded source/applicability evidence only; no BSD, main-conjecture, Bockstein/regulator, or certification promotion.

## Exact downstream query

Protected WP31 reduces the remaining local place-2 defect to a finite twisted-reciprocity exponent in a degree-2 or degree-4 local cyclotomic layer. To turn that finite class into an exact computable norm-membership criterion, downstream needs a range on which the elliptic formal-group law is canonically linearized by the formal logarithm at `p=2`.

The source question is therefore narrow:

> On what integral depth does Silverman's formal logarithm give an actual group isomorphism at `p=2`, and may it be used Galois-equivariantly to convert formal-group norms on that deep subgroup into field traces?

## Silverman IV.6.4

Let `K` be a characteristic-zero field complete for a normalized discrete valuation `v`, with valuation ring `R`, maximal ideal `M`, and residue characteristic `p`. Let `F/R` be a one-dimensional formal group.

Silverman IV.6.4 states:

1. `log_F` defines a homomorphism from `F(M)` to the additive group of `K`;
2. for every integer `r` satisfying

   `r > v(p)/(p-1)`, 

   the formal logarithm gives an isomorphism

   `log_F : F(M^r) -> M^r`

   onto the additive formal group.

The strict inequality is material at `p=2`.

## Literal p=2 specialization over Q_2

For `K=Q_2` with normalized valuation `v_2(2)=1`, the condition becomes

`r>1`.

Thus downstream may use the exact isomorphism

`log_E : Ehat(4 Z_2) -> 4 Z_2`.

This audit does **not** admit an isomorphism on the full shallow subgroup `Ehat(2 Z_2)`. The source threshold does not justify that claim; the shallow subgroup can contain 2-torsion for a general formal group.

## Finite totally ramified layers

Let `L/Q_2` be a finite totally ramified extension of ramification index `e`, with normalized valuation `v_L` and maximal ideal `m_L`. Then

`v_L(2)=e`.

The ideal `4 O_L` is

`m_L^{2e}`.

Applying IV.6.4 with `p=2` and `r=2e` is valid because

`2e > e = v_L(2)`.

Therefore downstream may use

`log_E : Ehat(4 O_L) -> 4 O_L`

as an exact group isomorphism in every finite local cyclotomic layer considered by WP31.

## Galois equivariance and norm-to-trace linearization

The formal logarithm is defined from the normalized invariant differential of the formal group over the base ring. For a formal group obtained from the fixed elliptic curve over `Q_2`, its coefficients are fixed by `Gal(L/Q_2)`. Hence on its domain of convergence,

`log_E(sigma R)=sigma(log_E(R))`

for `sigma in Gal(L/Q_2)`.

For `R in Ehat(4 O_L)`, the formal-group norm is the formal sum

`N_E(R) := sum_F_{sigma in Gal(L/Q_2)} sigma R`.

Because `log_E` is a homomorphism and Galois-equivariant on this deep subgroup,

`log_E(N_E(R)) = Tr_{L/Q_2}(log_E(R))`.

Consequently the deep formal norm image is exactly the inverse logarithmic image of the additive trace ideal:

`N_E(Ehat(4 O_L))
 = log_E^{-1}(Tr_{L/Q_2}(4 O_L))`.

This is the only norm-linearization interface admitted by this audit.

## Permitted downstream use

Downstream MATHSOLVE may combine this source-qualified deep logarithm interface with internally proved explicit trace-ideal calculations for the degree-2 and degree-4 local cyclotomic layers. In particular, if those calculations establish

`Tr_{L_1/Q_2}(O_{L_1})=2 Z_2`

and

`Tr_{L_2/Q_2}(O_{L_2})=4 Z_2`, 

then the admitted source interface permits the exact deductions

`N_E(Ehat(4 O_{L_1}))=Ehat(8 Z_2)`

and

`N_E(Ehat(4 O_{L_2}))=Ehat(16 Z_2)`.

The trace-ideal identities themselves are downstream algebraic calculations; they are not attributed to Silverman.

## Exact source boundary

This audit admits only:

- Silverman IV.6.4's formal-logarithm homomorphism and deep isomorphism;
- the literal `p=2` threshold `r>v(2)`, hence depth `4` over `Q_2` and depth `4O_L=m_L^{2e}` over a totally ramified finite layer;
- Galois-equivariant norm-to-trace linearization on that deep subgroup.

It does not admit or prove:

- a logarithm isomorphism on `Ehat(2 Z_2)` or `Ehat(m_L)`;
- a direct closed formula for the WP31 twisted-reciprocity exponent;
- the degree-2 or degree-4 trace ideals without downstream proof;
- equality of the formal logarithm with a p-adic height, WP20 Bockstein, or WP00 regulator;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `BSD-R2-A1`;
- novelty, priority, patentability, commercial significance, or MATHCERT certification.

## Provider conclusion

Silverman supplies exactly the deep integral linearization needed for a finite norm-membership calculation at `p=2`, but only below the shallow formal layer. Using depth `4O_L` respects the theorem's strict convergence threshold and preserves all 2-primary information. The remaining passage from the shallow subgroup to the deep subgroup is finite and must be performed explicitly downstream.

**Disposition:** `QUALIFIED_P2_DEEP_FORMAL_LOG_NORM_LINEARIZATION`.
