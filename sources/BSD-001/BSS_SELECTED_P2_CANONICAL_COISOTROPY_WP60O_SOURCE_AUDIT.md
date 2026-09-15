# BSD-001 source audit — selected literal-2 canonical residual coisotropy

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#203`.
- Downstream tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `39cda156c4ce16ec97cc80f415efa3b8a8716cea`.
- Protected MATHSOLVE anchor: `e6ec267cf5de910d2cb827008c66d10f31fe92c6`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary source A: Barry Mazur and Karl Rubin, *Kolyvagin Systems*, Memoirs AMS 168 (2004), no. 799, especially Definitions 1.1.6, 3.2.1 and local-duality interfaces in §1.3.
- Primary source B: Bjorn Poonen and Eric Rains, *Random maximal isotropic subspaces and Selmer groups*, JAMS 25 (2012), 245–269, especially Proposition 4.10.
- Comparison source: Ryotaro Sakamoto, *The theory of Kolyvagin systems for p=3*, JTNB 36 (2024), 919–946, Definition 9.2 and Lemma 9.3.
- Protected downstream source interface: `sources/BSD-001/BSS_COISOTROPIC_P2_CONNECTIVITY_WP60N_SOURCE_AUDIT.md`.
- Disposition: `SELECTED_P2_MR_BSS_CANONICAL_RESIDUAL_STRUCTURE_IS_COISOTROPIC`.
- Claim class: bounded source/applicability evidence only.

## Exact downstream query

Protected MATHSOLVE WP60N proves characteristic-two residual core-graph connectivity under a cartesian self-dual core-rank-one Selmer structure that is residually coisotropic.

The remaining selected-lane question is therefore whether, after identifying `E[2]` with `E[2]^*(1)` by the Weil pairing, the exact Mazur–Rubin/Burns–Sakamoto–Sano canonical residual structure satisfies

`H^1_{Fcan*}(Q_v,E[2]) subset H^1_{Fcan}(Q_v,E[2])`

for every place `v`.

The answer is yes. The key point is that the exact canonical structure used by Mazur–Rubin/BSS is not Sakamoto's unramified-away-from-`p` elliptic structure. The finite-level Mazur–Rubin canonical local condition always contains the ordinary local Kummer image, and that Kummer image is self-annihilating under the local Tate pairing.

## 1. Exact Mazur–Rubin canonical structure

Mazur–Rubin Definition 3.2.1 defines `Fcan` on the integral lattice `T` by:

1. `Sigma(Fcan)={ell:T ramified at ell} union {p,infinity}`;
2. for finite `ell != p` in `Sigma(Fcan)`,
   `H^1_Fcan(Q_ell,T)` is the kernel of
   `H^1(Q_ell,T) -> H^1(Q_ell^unr,T tensor Q_p)`;
3. at `p`,
   `H^1_Fcan(Q_p,T)=H^1(Q_p,T)`;
4. at the real place,
   `H^1_Fcan(R,T)=H^1(R,T)`;
5. on a finite quotient `T/IT`, the canonical structure is propagated from the integral one.

The source explicitly warns that the propagated quotient condition at `p` need not be the whole residual cohomology group. Thus residual coisotropy must be proved for the propagated subgroup, not by silently replacing it with full `H^1`.

For the selected lane put

`T=T_2(E)`, `A=T/2T=E[2]`.

For every place `v`, let

`L_v:=H^1_Fcan(Q_v,A)`

(with `Q_infinity=R`) and let

`K_v:=im(E(Q_v)/2E(Q_v) -> H^1(Q_v,E[2]))`

be the ordinary local Kummer image.

## 2. Kummer image is self-annihilating at every place

The principal polarization and Weil pairing identify

`E[2] ~= E[2]^*(1)`.

Poonen–Rains Proposition 4.10 proves, for every local field including archimedean fields, that the image of the local descent/Kummer map for a self-dual isogeny is a maximal isotropic subgroup of the corresponding local cohomology group with respect to the local quadratic form whose polar form is the Tate pairing.

For multiplication by `2` on an elliptic curve this gives, under the fixed Weil self-duality,

`K_v^perp = K_v`

inside `H^1(Q_v,E[2])` for every place `v`.

This includes `v=2` and `v=infinity`; no odd-prime convention is used in this finite local statement.

## 3. The canonical residual condition contains the Kummer image

### 3.1 The places `v=2` and `v=infinity`

At these places Mazur–Rubin put the unrestricted condition on the integral lattice:

`H^1_Fcan(Q_v,T)=H^1(Q_v,T)`.

The inverse-limit Kummer sequence gives the usual `2`-adic Kummer map from the `2`-adic completion of `E(Q_v)` to `H^1(Q_v,T)`. Reduction modulo `2` is the ordinary Kummer map

`E(Q_v)/2E(Q_v) -> H^1(Q_v,E[2])`.

Therefore propagation from the unrestricted integral condition contains every ordinary mod-2 Kummer class:

`K_v subset L_v`

for `v=2` and `v=infinity`.

This argument does not require the propagated canonical condition to equal all of `H^1(Q_v,E[2])`. In particular, possible rational local `2`-torsion at the good-ordinary place `2` does not obstruct coisotropy.

At the real place this also avoids an odd-prime shortcut. The residual local condition can be nonzero at `p=2`; nevertheless its Kummer subgroup is still self-annihilating and is contained in the propagated canonical condition.

### 3.2 Finite ramified places `ell != 2`

At a finite `ell !=2` in `Sigma(Fcan)`, the integral canonical condition is the Bloch–Kato finite kernel

`ker(H^1(Q_ell,T) -> H^1(Q_ell^unr,V))`,

where `V=T tensor Q_2`.

An ordinary local Kummer class mod `2` is represented by a compatible `2`-power Kummer class in `H^1(Q_ell,T)`. Its image in `H^1(Q_ell,V)` is the rational Kummer class associated to the image of the local point in `E(Q_ell) tensor Q_2`. For `ell !=2`, the latter tensor product is zero; equivalently the compatible Kummer class is integral torsion and maps to zero after tensoring with `Q_2`. Hence it lies in the displayed finite kernel.

After propagation to `A=E[2]` this gives

`K_ell subset L_ell`.

No condition on the parity of the Tamagawa number is used.

This is consistent with protected MATHSOLVE WP60L. WP60L used an **odd** Tamagawa factor at one multiplicative prime to prove the stronger statement that the entire integral local cohomology there is unramified, in order to exclude a specific ramified auxiliary cohomology defect. That stronger unramifiedness statement is not needed for residual coisotropy.

### 3.3 Good finite places outside `Sigma(Fcan)`

At a good finite place `ell !=2` outside the Selmer support, `T_2(E)` is unramified and the canonical local condition is the unramified one. The ordinary mod-2 Kummer image is the same unramified finite condition at such a good place. In particular

`K_ell=L_ell`

and this local condition is self-dual.

## 4. Coisotropy is a formal consequence of Kummer containment

For every place `v` we have proved

`K_v subset L_v`

and Source B gives

`K_v^perp=K_v`.

Orthogonal complements reverse inclusions, so

`L_v^perp subset K_v^perp=K_v subset L_v`.

By definition of the dual Selmer structure, after the fixed Weil self-duality,

`L_v^perp = H^1_Fcan*(Q_v,E[2])`.

Therefore for every place `v`,

`H^1_Fcan*(Q_v,E[2]) subset H^1_Fcan(Q_v,E[2])`.

Hence the exact Mazur–Rubin/BSS residual canonical structure is residually coisotropic.

Record

`SELECTED_P2_MR_BSS_CANONICAL_RESIDUAL_STRUCTURE_IS_COISOTROPIC`.

The proof actually uses only the elliptic self-duality/Kummer interfaces and the exact canonical local-condition definitions; the selected good-ordinary and semistable hypotheses are not needed for the local inclusion itself.

## 5. Why Sakamoto's Tamagawa hypothesis does not contradict this result

Sakamoto Definition 9.2 uses, for his elliptic `p=3` application, a different local structure: it takes the unramified condition at every finite place away from `3` and the unrestricted condition at `3`.

For a bad prime, the unramified residual subgroup need not equal the ordinary Kummer subgroup when the Tamagawa number has nontrivial `p`-part. This is why Sakamoto Lemma 9.3 assumes the bad Tamagawa factors are prime to `3` in order to verify his chosen structure is cartesian and residually coisotropic.

Mazur–Rubin Definition 3.2.1 instead uses the integral finite/Bloch–Kato condition at a ramified prime and then propagates it to finite quotients. The Kummer-containment argument above applies to this exact structure even when the bad Tamagawa factor is even.

Thus the protected WP60N provider warning was correct — Sakamoto Lemma 9.3 does not itself verify selected `p=2` coisotropy — but the warning does not constitute an obstruction to the distinct Mazur–Rubin/BSS canonical structure.

Record the distinction

`SAKAMOTO_TAMAGAWA_RESTRICTION_DOES_NOT_OBSTRUCT_MR_BSS_CANONICAL_P2_COISOTROPY`.

## 6. Downstream consequence

Protected MATHSOLVE WP60N at

`e6ec267cf5de910d2cb827008c66d10f31fe92c6`

proves full residual BSS core-graph connectivity at characteristic two assuming the relevant residual self-dual core-rank-one canonical structure is cartesian and residually coisotropic.

The present audit discharges the **coisotropy** component for the exact selected Mazur–Rubin/BSS canonical residual structure.

It does not independently re-prove cartesianness, core rank one, residual BSS restriction injectivity, or the WP60N exchange theorem. Those remain downstream/protected inputs and must be checked as a coherent application package before promoting full selected-lane BSS Fitting control.

Accordingly the previous boundary

`MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`

is reduced to any still-unverified non-coisotropy-independent application hypotheses; the coisotropy alternative itself is discharged.

## Claim firewall

This audit does not establish:

- BSS Theorem 5.20, Theorem 5.2, Theorem 5.25, or Corollary 6.15 at literal `p=2`;
- that every other hypothesis of those theorems has been repaired;
- formal global BSS Hypothesis 3.2(iii), which protected MATHSOLVE proves false at finite level;
- the protected infinite BSS H3 condition, which remains false;
- Kato/Fitting divisibility at the height-one prime `(2)`;
- determinant primitivity at `(2)`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
