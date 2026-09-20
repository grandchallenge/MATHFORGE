# BSD-001 source audit — BSS H2/H3 and selected maximal-image curve 53.a1

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#198`.
- Downstream tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `54f1eaea24b35d4ca37e778786345c3622b6fd98`.
- Protected MATHSOLVE anchor: `a73525fefc362aa4e1e03f006a46fd1dc3b961e8`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Sources:
  1. Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, III: applications*, arXiv:1902.07002; H2/H3 interface already audited and protected in WP60F.
  2. LMFDB, elliptic curve `53.a1` / Cremona `53a1`, `https://www.lmfdb.org/EllipticCurve/Q/53/a/1`, consulted 2026-09-14.
- Disposition: `ADMITTED_BSS_H2_H3_AND_SELECTED_53A1_MAXIMAL_IMAGE_INTERFACE`.
- Claim class: source-interface admission only.

## Purpose

Protected WP60F leaves the independent literal-`p=2` BSS standard-hypothesis boundary

`MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

This audit admits the exact BSS interface already identified in WP60F and one concrete selected curve with maximal `2`-adic image. The downstream MATHSOLVE operation will perform any finite group-cohomology calculation and decide whether H2 or H3 holds or fails.

This provider record does not make that downstream mathematical inference.

## BSS interface reused from protected WP60F

Protected MATHFORGE WP60F records the following source interface from BSS III.

### H2

The standard hypothesis H2 asks for an element

`tau in G_{F_{p-infinity}}`

such that

`T/(tau-1)T`

is free of rank one over the coefficient ring.

### H3

The standard hypothesis H3 asks for vanishing of the two first cohomology groups over the full torsion/cyclotomic extension:

`H^1(F(T)_{p-infinity}/K, bar T)=0`

and

`H^1(F(T)_{p-infinity}/K, bar T^vee(1))=0`.

WP60F also records that BSS III Lemma 6.17 proves H2/H3 from a large `p`-adic image only under the article's `p>3` hypotheses. Its H2 proof uses the restricted image and a unipotent element; its H3 proof uses vanishing of

`H^1(SL_2(Z_p),F_p^2)`.

No literal-`p=2` conclusion is imported from Lemma 6.17.

## LMFDB curve `53.a1`

LMFDB identifies the curve with label `53.a1` (Cremona label `53a1`) by the minimal equation

`y^2 + x y + y = x^3 - x^2`.

The database records the following exact arithmetic data.

### Conductor and semistability

- conductor: `53`;
- minimal discriminant: `-53`;
- the curve is semistable;
- the unique bad prime is `53`;
- reduction at `53` is nonsplit multiplicative of Kodaira type `I_1`;
- `ord_53(N)=1` and `ord_53(Delta)=1`.

Thus the conductor is odd and squarefree.

### Analytic rank

LMFDB records

`analytic rank = 1`.

It also records Mordell–Weil rank one and trivial rational torsion, though those two facts are not needed for the present F2 source interface.

### Good ordinary reduction at `2`

The modular-form expansion displayed by LMFDB begins

`q - q^2 - 3 q^3 - q^4 + ...`.

Hence

`a_2(E)=-1`,

which is odd. Since `2` does not divide conductor `53`, the curve has good ordinary reduction at `2`.

### Galois image

LMFDB states:

`The l-adic Galois representation has maximal image for all primes l.`

In particular, for `l=2`, the protected source datum is that the full `2`-adic representation has image

`GL_2(Z_2)`.

Consequently its residual mod-`2` image is `GL_2(F_2)` and is surjective.

The downstream use of this full-image datum, including any identification of restricted images or cohomology groups, is a mathematical inference and is not made by the provider audit.

## Selected-lane membership supplied by admitted facts

The protected selected `BSD-R2-A1` class requires:

1. semistable `E/Q`;
2. odd conductor;
3. good ordinary reduction at `2`;
4. surjective residual `E[2]` representation;
5. analytic rank exactly one.

The source facts above show that `53.a1` satisfies these five selected-class conditions.

This statement concerns membership in the protected research class only. It is not a BSD theorem for `53.a1` and does not use LMFDB's numerical analytic-Sha display as proof of any campaign claim.

## Exact downstream questions enabled

The protected downstream operation may now test, for `T=T_2(53.a1)` and `bar T=E[2]`:

1. the exact field `Q_{2-infinity}` in the BSS notation;
2. the restricted image of `G_{Q_{2-infinity}}` under the full `GL_2(Z_2)` representation;
3. whether a unipotent element supplies H2;
4. the exact finite quotient cohomology `H^1(GL_2(Z/4),F_2^2)` and its inflation to the full `2`-adic image;
5. the resulting truth or failure of the first H3 group;
6. by Weil self-duality, the corresponding statement for the dual H3 group.

These are mathematical obligations for MATHSOLVE and are intentionally not answered here.

## Provider conclusion

Record

`ADMITTED_BSS_H2_H3_AND_SELECTED_53A1_MAXIMAL_IMAGE_INTERFACE`.

The provider has supplied a concrete selected curve with full `2`-adic image and the exact BSS H2/H3 interface required to test the literal-`2` standard hypotheses.

## Claim firewall

This audit does not establish:

- H2 for `53.a1`;
- failure or validity of H3 for `53.a1`;
- any computation of `H^1(GL_2(Z/4),F_2^2)`;
- failure of H3 for every selected curve;
- a no-go theorem for all literal-`2` Kolyvagin-system approaches;
- F1 closure;
- BSS Fitting control at `2`;
- R5-LIFT or R5-PRIM;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
