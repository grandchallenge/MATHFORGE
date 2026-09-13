# BSD-001 source audit — Cai–Shu–Tian split Steinberg toric factor for Disegni `Q^ord`

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP53A-DISEGNI-SPLIT-BAD-PRIME-QORD`.
- Protected MATHFORGE predecessor: `79302cdc05f3f11c56e048f68e9095d3280872a7`.
- Protected MATHSOLVE predecessor: `3aae8375de252a782eaf82e0bb393814e033f857`.
- Primary source 1: Daniel Disegni, *The universal p-adic Gross–Zagier formula*, Invent. Math. 230 (2022), 509–649; exact loci: (1.2.7)–(1.2.9), Remark 1.2.2, (4.2.1)–(4.2.4), Lemma 4.3.3 / (4.3.4).
- Primary source 2: Li Cai, Jie Shu, Ye Tian, *Explicit Gross-Zagier and Waldspurger formulae*, Algebra Number Theory 8 (2014), no. 10, 2523–2572, arXiv:1408.1733; exact loci: §2 measure normalization, Proposition 3.11, Proposition 3.12.
- Corroborating local-newform source: Ralf Schmidt, *Some remarks on local newforms for GL(2)*, J. Ramanujan Math. Soc. 17 (2002), 115–147, special-representation Kirillov newform formula.
- Disposition: `QUALIFIED_EXACT_SPLIT_STEINBERG_TORIC_FACTOR_WITH_MEASURE_LEDGER`.
- Claim class: source/local-normalization admission only; no global `Q^ord`, BSD, or certification promotion.

## Source-lock note

The CST arXiv PDF was inspected by searchable text and rendered page images. In particular the page containing Proposition 3.12 and the page containing the global/self-dual measure system were rendered successfully. Disegni's public author PDF was inspected at the exact formula loci; one later page-image call returned a cache miss, but the introductory local-normalization page rendered successfully and the searchable text layer remained available. No independently recomputed PDF digest is claimed.

## Downstream question

Protected WP41B reduces the source-normalized p-adic Gross–Zagier factor to `Q^ord`. Protected WP42B computes the selected good-ordinary split-`2` factor in its canonical local normalization. The remaining bad-prime question is:

> For an odd semistable bad prime `ell|N`, with the protected auxiliary quadratic field split at `ell`, trivial toric character, and the local automorphic representation an unramified twist of Steinberg, what is the exact normalized local toric factor on the newvector/test-vector line?

## 1. Disegni's local normalization equals the CST beta normalization

For a finite place `v`, Disegni (1.2.7) defines

`Lcal(V_(pi,chi),v,0)
 := zeta_F,v(2) L(V_v,0)
    / (L(1,eta_v) L(ad(V_pi,v),1))`.

Equations (1.2.7)–(1.2.8), equivalently (4.2.1)–(4.2.2), give

`Q_{v,dt}((f1 tensor f2)/(f3 tensor f4))
 = Lcal(V_v,0)^(-1)
   * [integral_{E_v^x/F_v^x} (pi_v(t)f1,f2) dt]
     /(f3,f4)`.

Cai–Shu–Tian define their normalized local toric functional

`beta(f1,f2)
 = L(1,eta) L(1,pi,ad)
   / (L(1/2,pi,chi) L(2,1_F))
   * integral_{F^x\K^x}
       ((pi(t)f1,f2)/(f1,f2)) chi(t) dt`.

For the motive normalization used by Disegni,

`L(V_v,0)=L(1/2,pi_v,chi_v)`

and `zeta_F,v(2)=L(2,1_F)`. Therefore, for the same local Haar measure and for `f1=f3=f`, `f2=f4=f^vee`, Disegni's local ratio is exactly CST's `beta(f)`. This is equality of source-normalized formulas, not an equality only up to a unit.

Disegni Remark 1.2.2 explicitly points to CST for evaluating `Q` on suitable local test vectors.

## 2. Selected bad-prime local representation

For the BSD-001 selected semistable branch, every odd `ell|N` is multiplicative. The local GL2 representation has conductor exponent

`n=1`

and is a special representation, equivalently an unramified twist of Steinberg. The central character is trivial.

CST Proposition 3.11 defines a correction exponent `delta_pi` and states it is zero whenever the GL2 representation is a subrepresentation of an induced representation with at least one unramified inducing character. A special representation with unramified twist lies on this `delta_pi=0` branch.

Protected WP09 chooses the auxiliary imaginary quadratic field so every `ell|N` splits. Thus locally

`K_ell ~= Q_ell direct_sum Q_ell`.

Protected WP09 also fixes `chi=1`, so the local toric-character conductor is

`c=0`.

## 3. CST Proposition 3.12

CST Proposition 3.12 states, for a nonarchimedean local field and any nonzero vector in the one-dimensional test-vector line, that in the case

`n>0`, `c=0`, and `K` split,

`beta(f) |D delta|^(-1/2)
 = [L(1,1_F)/L(2,1_F)] * L(1,pi,ad)^(delta_pi)`.

For the selected local field `F=Q_ell`:

- the base-field different is trivial, so `|delta|=1`;
- the split quadratic algebra has trivial relative discriminant factor, so `|D|=1`;
- `delta_pi=0` as above.

Therefore

`beta_ell(f)
 = L(1,1_Qell)/L(2,1_Qell)`.

Since

`L(1,1_Qell)=(1-ell^(-1))^(-1)`

and

`L(2,1_Qell)=(1-ell^(-2))^(-1)`,

one obtains the exact identity

`beta_ell(f)=1+ell^(-1)`.

The same value is visible directly in CST's conductor-one computation of the normalized matrix coefficient.

Combining with the Disegni/CST normalization identity gives, for the CST local Haar measure and the source-compatible newvector/test-vector line,

`Q_{ell,dt_ell^CST}=1+ell^(-1)`.

Consequently

`ord_2(Q_{ell,dt_ell^CST})=ord_2(ell+1)`,

because `ell` is a `2`-adic unit.

The formula does not depend on whether the multiplicative reduction is split or nonsplit over `Q_ell`; that distinction is carried by the unramified Steinberg twist, while the CST normalized value on this split-torus, conductor-one, trivial-character branch is unchanged.

## 4. Measure normalization and the global ledger

CST do not use an arbitrary local measure. In §2 they choose local additive measures self-dual for a fixed global additive character, derive multiplicative measures from them, and endow the torus quotient with the corresponding quotient measure. Their product gives the global toric measure whose quotient volume is

`2 L(1,eta)`.

Disegni instead fixes an adelic torus measure of total quotient volume `1` in (1.2.9). A decomposition of that global measure into local components is not unique.

Accordingly, if the local component used in Disegni's decomposition is

`dt_ell = s_ell * dt_ell^CST`,

then linearity of the local integral gives exactly

`Q_{ell,dt_ell}
 = s_ell * (1+ell^(-1))`.

No claim that `s_ell` is a `2`-adic unit is admitted.

One may choose CST's canonical local measure at every finite bad place and compensate the product normalization at the remaining places, but the compensating global scalar must remain explicit in the global measure ledger. This audit therefore closes the newvector/test-vector integral, not the entire global-measure normalization.

## 5. Exact downstream interface

After protection, MATHSOLVE may use the following bounded statements.

1. At every selected odd semistable bad prime `ell|N`, with `K/Q` split at `ell`, `chi_ell=1`, and the source-compatible conductor-one test-vector line,

   `Q_{ell,dt_ell^CST}=1+ell^(-1)`.

2. Hence

   `ord_2 Q_{ell,dt_ell^CST}=ord_2(ell+1)`.

3. For an arbitrary local component in Disegni's globally volume-one decomposition,

   `dt_ell=s_ell dt_ell^CST`

   implies

   `Q_{ell,dt_ell}=s_ell(1+ell^(-1))`.

4. Therefore the intrinsic split semistable bad-prime newvector factor is exact. The remaining global ordinary-factor debt is the explicit measure-reconciliation scalar together with any nonbad auxiliary-vector factors and remaining global/archimedean normalization.

## 6. Refined D2c boundary

The former boundary

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`

is resolved at the local test-vector level.

The surviving source/normalization debt is narrower:

`MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`.

## Claim firewall

This audit does not prove:

- `Q^ord=1`;
- `ord_2(Q^ord)=sum_{ell|N} ord_2(ell+1)` without the remaining global measure/vector ledger;
- that the measure scalars `s_ell` are `2`-adic units;
- cancellation of the bad-prime factor against Tamagawa or determinant terms unless proved downstream in an exact common normalization;
- fixed-`2` height nondegeneracy;
- D1c;
- the classical Gross–Zagier/WP00 normalization;
- final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

**Disposition:** `QUALIFIED_EXACT_SPLIT_STEINBERG_TORIC_FACTOR_WITH_MEASURE_LEDGER`.
