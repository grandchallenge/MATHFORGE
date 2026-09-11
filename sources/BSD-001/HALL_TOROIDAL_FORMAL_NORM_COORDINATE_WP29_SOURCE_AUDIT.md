# BSD-001 source audit — Hall/Lubin–Rosen toroidal construction of the formal norm coordinate

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP29-P2-TOROIDAL-FORMAL-NORM-COORDINATE`.
- Protected Forge baseline: `e5c49ee60ba300cff8026ddf65059c3049ab1226`.
- Protected downstream MATHSOLVE baseline: `3bae7e80d148adb297fc3746e4f1eb0466148354`.
- Primary modern reconstruction: Christopher Stephen Hall, *Class Field Theory and Arithmetic of Abelian Varieties over Local Fields*, arXiv:`2203.11855v1` (2022).
- Detailed authorial version inspected: Christopher Stephen Hall, *Investigations into Local Class Field Theory with General Residue Fields*, PhD thesis, University of Nottingham, 2023, especially §§2.5 and 4.1–4.2.
- Historical theorem reconstructed there: Jonathan Lubin and Michael Rosen, *The norm map for ordinary abelian varieties*, J. Algebra 52 (1978), 236–240, Theorem 1 and their reproof of Mazur Proposition 4.39.
- Disposition: `QUALIFIED_P2_TOROIDAL_FORMAL_NORM_COORDINATE_CONSTRUCTION`.
- Claim class: source/applicability admission only; no evaluation of the selected generator, no BSD, determinant, regulator, or MATHCERT promotion.

## Exact downstream question

Protected WP28 gives the exact local sequence

`0 -> F_2^norm -> U_2 -> E_tilde(F_2) -> 0`

and reduces the remaining local D1b uncertainty to the order of one explicit element

`z_form(P) in F_2^norm`.

Tan's protected theorem gives the ambient group description, in dimension one,

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`,

but the WP28 source audit deliberately did not claim an element-level formula under that isomorphism.

The bounded source question is now:

> Is the isomorphism from a height-one ordinary formal-group norm quotient to the Galois quotient constructed through explicit maps on individual formal points, so that the class of `z_form(P)` has a source-defined toroidal/local-class-field coordinate rather than only an abstract ambient group isomorphism?

Hall's reconstruction supplies this construction, but it still does not turn that coordinate into a closed formula involving a formal logarithm, the protected unit root, or the WP20 Bockstein.

## Prime range

Hall's setup fixes an arbitrary prime `p`, a complete discretely valued field of characteristic zero with residue characteristic `p`, a totally ramified `p`-extension, and a good-ordinary abelian variety. The finite-residue-field specialization reviewed in §2.5 is exactly the Lubin–Rosen setting:

- `F/Q_p` finite;
- `A/F` good ordinary;
- `L/F` a totally ramified `Z_p`-extension.

No condition `p>2` occurs in this construction. Therefore the source interface specializes literally to

`p=2`, `F=Q_2`, `L=Q_{infty,2}`.

## Toroidal formal-group model

Let `H` be the formal group of a good-ordinary abelian variety. Hall recalls the Lubin–Rosen/Mazur toroidal description: after base change to the completion of the maximal unramified extension, choose an isomorphism

`k:H -> Ghat_m^d`.

Applying Frobenius to the coefficients gives `k^phi`, and

`k^phi o k^(-1)`

is represented by a twist matrix

`u in GL_d(Z_p)`.

Hall defines the twisted principal-unit module

`V_u(L)
 = { alpha in U^1_{L Fhat}^d : alpha^phi = alpha^u }`.

He then proves that `k` induces a Galois-module isomorphism

`H(O_L) ~= V_u(L)`.

Thus an individual formal point is transported by an explicit formal power-series isomorphism into the twisted principal-unit module. This is stronger than knowing only the isomorphism class of the quotient group.

## Finite-layer norm quotient

In the finite-residue-field Lubin–Rosen setting, Hall records the exact finite-layer theorem

`V_u(F)/N_{L_n/F}V_u(L_n)
 ~= (G_n^ab)^d/(I-u)(G_n^ab)^d`,

where

`G_n=Gal(L_n/F)`.

For the selected elliptic case `d=1`, this is

`V_u(F)/N V_u(L_n)
 ~= G_n/(1-u)G_n`.

The infinite `Z_p`-extension then yields the corresponding limit quotient

`Z_p^d/(I-u)Z_p^d`

mapping naturally into the full abelian-variety universal-norm quotient.

## Explicit maps used in the reconstruction

The detailed Hall proof does not treat the quotient isomorphism as a black box. It constructs the relevant maps through a commutative diagram.

For the generalized setting Hall defines, for a Frobenius generator `phi`,

`i_alpha(phi) = phi(alpha)/u_phi(alpha)`

on principal units and a Galois-side map

`omega(g)(phi)=g^(1-u_phi)`.

He also writes the finite local-class-field/Tate-cohomology map explicitly: after choosing a uniformizer `pi`, an element of `G^ab` maps to the class represented by

`pi^(g-1)`

in the appropriate principal-unit quotient, and the corresponding homomorphism-side map is written similarly. The proof verifies commutativity and then obtains the norm quotient through the Snake Lemma.

In dimension one with finite residue field, the single Frobenius generator reduces `omega` to

`g |-> g^(1-u)`,

so its cokernel is the Lubin–Rosen quotient

`G/(1-u)G`.

Consequently the finite-layer class of an individual formal point is obtained by the source-defined composite:

1. apply the toroidal power-series isomorphism `k` to the formal point;
2. take its class in the twisted principal-unit norm quotient;
3. transport that class through the explicit commutative-diagram isomorphism to the Galois quotient `G_n/(1-u)G_n`.

Passing compatibly through the finite layers gives an element coordinate in the inverse-limit quotient

`Gamma/(1-u)Gamma`.

## What is canonical for the downstream order

The auxiliary toroidal isomorphism `k` is not a canonical coordinate choice. The downstream quantity, however, is the **order** of the resulting class.

Any change of source-compatible toroidal coordinate induces a group automorphism on the finite cyclic quotient in dimension one. Such an automorphism preserves element order. Therefore downstream may use the order of the source-defined toroidal/Galois coordinate as an invariant representation of

`s_form(P)`

without claiming that a chosen coordinate value itself is canonical.

This audit does not assert a stronger coordinate-independence statement than order invariance.

## Qualified downstream composition

After source admission, MATHSOLVE may define, for the WP28 formal element `z_form(P)`, a toroidal norm coordinate

`theta_form(P) in Gamma_2/(1-u)Gamma_2`

as its image under the protected Hall/Lubin–Rosen construction.

It may then prove

`ord(theta_form(P)) = ord(z_form(P))`

and hence

`s_form(P)=ord_2(ord(theta_form(P)))`.

This is an exact element-level representation theorem. It makes the remaining D1b datum algorithmically local-class-field-theoretic, but it does not by itself evaluate the order.

## What the source does not establish

The source does not establish:

- a closed formula for `theta_form(P)` in terms of a formal logarithm;
- a value of `ord(theta_form(P))` for the selected saturated generator;
- an identification of the twist scalar `u` with the protected WP07 unit root `alpha` or `alpha^(-1)`;
- a canonical generator of `Gamma_2` or a canonical scalar representative of the quotient class;
- equality with a p-adic height, regulator, or WP20 Bockstein factor;
- D1a, D1c, or D2;
- the selected BSD equality or `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.

## Negative route retained

Hazewinkel's explicit cyclotomic norm theorem for one-dimensional formal groups was separately checked as a potential shortcut. Its main explicit theorem is stated for formal-group height at least two (and infinite height). The selected good-ordinary elliptic formal group is height one. That route is therefore not admissible for the present element-level step and is not used here.

## Provider conclusion

Hall's reconstruction of the Lubin–Rosen/Mazur norm argument supplies a literal-`p=2`, map-level toroidal construction of the formal universal-norm quotient. It permits downstream representation of the specific WP28 formal class by an explicit local-class-field/Galois quotient coordinate, while leaving its order, unit-root normalization, and any Bockstein/regulator comparison open.

**Disposition:** `QUALIFIED_P2_TOROIDAL_FORMAL_NORM_COORDINATE_CONSTRUCTION`.

## Claim firewall

This audit changes no protected claim state. It is a bounded source/applicability record only.
