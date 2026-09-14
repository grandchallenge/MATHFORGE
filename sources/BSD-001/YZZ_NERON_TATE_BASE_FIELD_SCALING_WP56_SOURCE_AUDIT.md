# BSD-001 source audit — YZZ Néron–Tate base-field scaling for WP56

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP56A-CLASSICAL-HEIGHT-REGULATOR-DESCENT`.
- Protected MATHFORGE predecessor: `2207d9a366e84dc7a1f5726e78e3cfe5e4ab1468`.
- Protected MATHSOLVE predecessor: `956024627383d76b7b30212c0eaadf52e2fff7a2`.
- Primary source: Xinyi Yuan, Shou-Wu Zhang, Wei Zhang, *The Gross-Zagier Formula on Shimura Curves*, Annals of Mathematics Studies 184, Princeton University Press, 2013.
- Primary source locus: §7.1.1, “Néron–Tate height on abelian varieties”.
- Companion source: Li Cai, Jie Shu, Ye Tian, *Explicit Gross–Zagier and Waldspurger formulae*, Algebra & Number Theory 8 (2014), §2.3 / Proposition 2.5 comparison note and Theorem 1.1.
- Disposition: `QUALIFIED_EXACT_HEIGHT_BASE_FIELD_SCALING`.
- Claim class: source/normalization admission only; no BSD or MATHCERT promotion.

## Exact YZZ normalization

Yuan–Zhang–Zhang fix a number field `F` and explicitly state that their normalization of heights depends on `F`.

For a projective point whose coordinates are contained in a finite extension `L/F`, their standard logarithmic projective height has the form

`h_F(x) = (1/[L:F]) * sum_{w in M_L} log max_i |x_i|_w`,

with normalized local absolute values. The associated Weil heights and the Néron–Tate height are then defined from this base-field-normalized height; the canonical limit preserves multiplication by a constant scalar.

Consequently, if `K/F` is a finite extension and `P` is a point defined over `K`, evaluating the same geometric height datum with base field `K` instead of base field `F` gives exactly

`h_K(P) = [K:F] * h_F(P)`

and therefore

`hhat_K(P) = [K:F] * hhat_F(P)`.

This is a direct algebraic consequence of the displayed YZZ definition, not an “up to a unit” comparison.

For the protected BSD auxiliary lane, `F=Q` and `K/Q` is imaginary quadratic. Hence

`[K:Q]=2`

and for every point in the common domain,

`hhat_K(P) = 2 hhat_Q(P)`.

## Match to Cai–Shu–Tian

Cai–Shu–Tian define the Néron–Tate pairing used in their explicit Gross–Zagier formula as the height **over K**. In their comparison with Yuan–Zhang–Zhang they explicitly warn that their height is over `K` while the height in YZZ is over the totally real base field `F`.

Thus the factor above is exactly the convention conversion required by the already-protected WP55 CST source admission. For the selected `F=Q`, quadratic `K` lane, the CST height in Theorem 1.1 is twice the corresponding Q-normalized canonical height.

## Exact downstream interface admitted after protection

MATHSOLVE may use the following bounded normalization statement in WP56A:

For the selected quadratic auxiliary field `K/Q` and the CST/YZZ height conventions just identified,

`hhat_K(P) = 2 hhat_Q(P)`

for every point `P` to which the common Néron–Tate height datum applies.

In particular, once a protected internal argument writes the CST Heegner point as

`P_K(f) = m P + T`

with `P` a primitive generator of `E(Q)/E(Q)_tors`, `m in Z`, and `T` torsion, the source interface permits

`hhat_K(P_K(f)) = 2 m^2 hhat_Q(P)`

using the standard quadraticity and torsion-insensitivity of the canonical height.

This source admission does **not** determine `m`.

## Boundaries retained

This audit does not prove or assume:

- that the Heegner trace `P_K(f)` is primitive;
- that its index `m` is odd or a 2-adic unit;
- a p=2 Kolyvagin/Heegner primitivity theorem;
- fixed-2 p-adic height nondegeneracy;
- a height-one `(2)` analytic determinant generator;
- any cancellation of the WP54A `u_K/h_K` or bad-prime factors;
- any rank-zero BSD formula for the twist `E^D`;
- the remaining area/period/twist-central-value scalar in WP55A;
- the final WP06 normalization descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

## Source-access note

The YZZ source identity was checked against publisher bibliographic records and the text of §7.1.1. The relevant section states both that the normalization depends on the chosen base field and gives the `1/[L:F]` projective-height normalization from which the exact extension-degree scaling follows. The CST primary PDF was independently inspected at its height definition and its explicit comparison note that CST uses height over `K` while YZZ uses height over `F`.

## Provider disposition

`QUALIFIED_EXACT_HEIGHT_BASE_FIELD_SCALING`

The interface is restricted to this exact normalization conversion. It does not enlarge any arithmetic theorem or certify any BSD claim.
