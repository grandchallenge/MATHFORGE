# BSD-001 source audit — Nekovář literal-`p=2` strict-H2 Matlis duality

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP51A-STRICT-H2-SELMER-DUALITY`.
- Protected MATHFORGE predecessor: `79f7c88cf4e59886902c2f12d29d7c73afced379`.
- Protected MATHSOLVE predecessor: `e078beae05252c4152787fc812e0823b14c23fac`.
- Primary source: Jan Nekovář, *Selmer complexes*, Astérisque 310 (2006), DOI `10.24033/ast.717`.
- Exact source loci: §5.2.3–5.2.4, Theorem 6.3.4, §6.3.5, and §6.7.1–6.7.2; prior protected WP37 audit supplies the literal-`p=2` totally-imaginary applicability condition.
- Disposition: `QUALIFIED_LITERAL_P2_STRICT_H2_MATLIS_DUALITY`.
- Claim class: bounded source/duality admission only; no height-radical, nondegeneracy, BSD, or certification promotion.

## Source-access note

The official NUMDAM Astérisque volume was queried at the exact theorem loci. Its PDF is approximately 42 MB and the current PDF renderer rejected the document as too large; a page screenshot was attempted and could not be resolved because the oversized PDF never materialized as a screenshot-capable PDF source. No independent page-image lock or PDF digest is claimed. The interface below is bound to the official NUMDAM/DOI edition and exact theorem numbering.

## Downstream question

Protected MATHSOLVE WP50A defines the finite strict degree-two silent kernel

`K_K^sil
 := ker(
      H~^2_f(K,T;Delta_str)
      -> H^2(C_Kum,0) direct_sum Zloc
    )`

and proves

`D_K^vee ~= K_K^sil`.

The next question is whether the source supplies an exact integral dual description of strict degree-two Selmer cohomology, at literal `p=2` over the protected imaginary quadratic field `K`, so that the finite subgroup `K_K^sil` can be converted into a canonical quotient on the discrete dual Selmer side.

## Theorem 6.3.4 — derived Selmer duality

Nekovář Theorem 6.3.4 states that, for a perfect duality

`pi:X_1 tensor_R X_2 -> J(1)`

and mutually orthogonal Selmer local conditions, the induced Selmer-complex duality map fits into an exact triangle whose third term is the local-condition error complex. When the local conditions are orthogonal complements, the error complex vanishes and the duality map is an isomorphism in the derived category.

Section 6.7 gives the Greenberg example. In §6.7.2 the local plus conditions are orthogonal precisely when the composite

`X_v^+ tensor_R Y_v^+ -> X tensor_R Y -> J(1)`

is zero. For the elliptic self-dual ordinary lane used downstream, the dual local conditions are the source-compatible orthogonal Greenberg conditions already fixed in the protected WP37/WP43A setup.

## Section 6.3.5 — cohomological Matlis duality

Section 6.3.5 gives the cohomological consequence of Theorem 6.3.4. In the Matlis-duality case `J=I[n]`, when the error complex vanishes,

`H~^q_f(X_1)
 ~= D(H~^{3-n-q}_f(X_2))`.

For the ordinary coefficient normalization used in the protected BSD-001 Selmer-complex lane, this gives the familiar degree-(2,1) duality between the compact lattice complex and the discrete dual representation. In adapted notation:

`H~^2_f(K,T;Delta_str)
 ~= (H~^1_f(K,A^*(1);Delta_str^perp))^vee`,

where

`A^*(1):=Hom(T,Q_2/Z_2(1))`

and `(-)^vee` denotes Pontryagin duality.

Equivalently, there is a canonical perfect Pontryagin pairing

`H~^2_f(K,T;Delta_str)
 x H~^1_f(K,A^*(1);Delta_str^perp)
 -> Q_2/Z_2`.

No rationalization and no equality only up to a `2`-adic unit is involved.

## Literal `p=2` applicability

Chapter 6 operates under the standing duality hypothesis `(P)` from Chapter 5. Protected MATHFORGE WP37 already source-binds Nekovář's explicit `p=2` branch: `(P)` is available when the base field is totally imaginary. Protected WP09 supplies exactly such an imaginary quadratic `K`.

Therefore this duality interface applies literally at `p=2` in the protected auxiliary-field lane. No odd-prime theorem is being specialized.

## Exact downstream interface admitted

After protection, MATHSOLVE may use the following bounded statements.

1. The protected strict Greenberg Selmer complex over `K` has an exact degree-(2,1) Matlis/Pontryagin duality with the source-compatible discrete dual Selmer complex.
2. Writing

   `S_str^dual := H~^1_f(K,A^*(1);Delta_str^perp)`,

   there is a canonical perfect pairing

   `H~^2_f(K,T;Delta_str) x S_str^dual -> Q_2/Z_2`.
3. For every finite subgroup `F` of strict `H~^2_f`, if

   `F^perp := {y in S_str^dual : <f,y>=0 for all f in F}`,

   then Pontryagin duality gives canonically

   `F^vee ~= S_str^dual/F^perp`.
4. In particular MATHSOLVE may apply item 3 to the protected finite subgroup `K_K^sil` from WP50A.

Item 3 is elementary exact duality once item 2 is source-bound; it does not require a new arithmetic theorem.

## Separation from the p-adic height pairing

This audit does **not** identify the quotient

`S_str^dual/(K_K^sil)^perp`

with a radical or cokernel of Nekovář's p-adic height.

The protected WP37 height is constructed by composing the cyclotomic Bockstein on lattice-level strict `H~^1_f(K,T)` with Selmer-complex duality. Its rank-one height pairing and the Matlis pairing with the discrete dual Selmer group are related by the same derived formalism, but the equality of a finite subgroup of strict `H^2` with a Bockstein image, torsion image, or height radical is a separate mathematical statement.

Thus source duality localizes the remaining problem; it does not solve fixed-`2` height nondegeneracy.

## What this source does not establish

This source admission does not prove:

- `K_K^sil=0`;
- `D_K=0` or `J_K=R_K`;
- `K_K^sil=im(beta_str)` or any containment between these objects;
- identification of `D_K` with a p-adic-height radical;
- fixed-`2` height nondegeneracy;
- the height-one `(2)` analytic determinant generator;
- remaining Disegni/WP00/descent normalization;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

## Provider conclusion

Nekovář's original Selmer-complex duality supplies the exact literal-`p=2` degree-(2,1) Matlis/Pontryagin duality needed after WP50A. The protected finite silent kernel therefore has a canonical quotient description on the discrete dual strict Selmer side.

**Disposition:** `QUALIFIED_LITERAL_P2_STRICT_H2_MATLIS_DUALITY`.

The surviving mathematical obligation is to determine how that finite quotient relates, if at all, to the lattice-level cyclotomic Bockstein/height radical; no such relation is promoted by this audit alone.
