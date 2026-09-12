# BSD-001 source audit — literal-`p=2` Nekovář extended/Greenberg to classical Kummer comparison

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP39-P2-KUMMER-GREENBERG-COMPARISON`.
- Protected MATHFORGE predecessor: `5a5bf90af046e91ed13949ad8087c35e6a74d059`.
- Protected MATHSOLVE predecessor: `efac1b7eaa9b7d1da42c9d33fbb73516fec93a42`.
- Primary source: Jan Nekovář, *Selmer complexes*, Astérisque 310 (2006), especially §§9.6.1–9.6.7.
- Existing companion source already protected in MATHFORGE: Ralph Greenberg, *Iwasawa Theory for Elliptic Curves*, admitted in `GREENBERG_P2_PRIMITIVE_LOCAL_CONTROL_SOURCE_AUDIT.md`.
- Disposition: `QUALIFIED_LITERAL_P2_EXTENDED_STRICT_KUMMER_COMPARISON`.
- Claim class: bounded source/comparison admission only; no D1c, D2, BSD, or MATHCERT promotion.

## Source-access note

The official NUMDAM edition and its searchable primary-source text were inspected. The web PDF renderer rejected the full Astérisque volume because of its size; a required screenshot call was attempted and failed because the source could not be materialized as a PDF by the renderer. The exact theorem text was cross-checked against the searchable transcription of the same volume and against Nekovář's own later citations of Lemma 9.6.3. This audit therefore binds exact section/lemma locators and bibliographic identity, but does not claim an independently recomputed PDF digest or successful page-image lock.

## Downstream question

Protected WP38 proves that quadratic base change itself introduces no index in the rank-one Mordell–Weil free lattice:

`E(Q)/tors ~= E(K)/tors`,

hence

`E(Q) tensor Z_2 ~= E(K) tensor Z_2`.

The surviving D2b question is therefore local/Selmer-complex:

> For `T=T_2(E)` over the protected WP09 imaginary quadratic field `K`, what is the exact relation between Nekovář's source-compatible extended/strict ordinary Selmer lattice and the classical compact Kummer Selmer lattice, and what finite local target measures their discrepancy?

## Prime range

Nekovář §9.6 is stated for a general prime `p`; §§9.6.1, 9.6.3 and 9.6.7 do not insert an odd-prime hypothesis. The abelian-variety specialization §9.6.7 takes `O=Z_p`, `F=Q_p`, and treats good ordinary reduction at every `v|p` without excluding `p=2`.

The broader BSD-001 height construction remains on the protected totally imaginary field `K`, which is already source-qualified in WP37 for the literal-`p=2` duality/Bockstein setting. Thus no odd-prime theorem is specialized here.

## Lemma 9.6.3 — extended to strict Greenberg

With Greenberg local data `T_v^+ subset T` and `T_v^-:=T/T_v^+`, Nekovář Lemma 9.6.3 gives, for `X=T,V,A`, the exact sequence

`0 -> H~^0_f(X) -> X^{G_K}`

`   -> direct_sum_{v|p} (X_v^-)^{G_v}`

`   -> H~^1_f(X) -> S_X^str(K) -> 0`.

Here `S_X^str(K)` is the strict Greenberg Selmer group defined in §9.6.1.

For an elliptic curve with good ordinary reduction at `v|p`, Lemma 9.6.7.6(i) proves

`H^0(G_v,V_v^-)=0`.

Since `T_v^-` embeds in `V_v^-`, it follows that

`H^0(G_v,T_v^-)=0`.

On the protected BSD-001 branch, WP06 gives `E(K)[2^infinity]=0`, hence

`T_2(E)^{G_K}=0`.

Therefore the exact sequence specializes to the literal integral isomorphism

`H~^1_f(K,T_2(E)) ~= S_T^str(K)`.

This closes the possible degree-zero/exceptional extended-Selmer correction for the compact rank-one lattice in the selected good-ordinary `p=2` lane.

It does **not** identify the strict Greenberg group with the classical Kummer group.

## Lemma 9.6.7.3 — strict Greenberg to classical compact Kummer

For an abelian variety `B/K`, Nekovář §9.6.7 defines the compact classical Kummer Selmer group

`S_p(B/K) = lim_n Sel(B/K,p^n)`

using the actual local Kummer images.

In the elementary ordinary/toric setup, Lemma 9.6.7.3(i) gives an exact injection

`0 -> S_T^str(K) -> S_p(B/K)`

whose quotient maps into the explicit finite local module

`R_K(T) :=`

`  direct_sum_{v|p} H^1(G_v,T_v^-)_tors`

`  direct_sum direct_sum_{v not| p} H^1(G_v,T)/H^1_ur(G_v,T)`.

The displayed source sequence is exact through this local target; it does not assert that the map onto the entire ambient target is surjective. Downstream must therefore retain the image subgroup rather than silently replace it by `R_K(T)`.

Lemma 9.6.7.3(ii) proves that each non-`p` local term is finite with `Z_p`-length equal to the local `p`-adic Tamagawa exponent.

Lemma 9.6.7.3(iii) identifies each `p`-local compact term with

`H^1(G_v,T_v^-)_tors ~= H^0(G_v,A_v^-)/div`.

The companion Greenberg source already protected by MATHFORGE computes, literally at `p=2` for a good-ordinary elliptic curve, the finite classical-Kummer/ordinary local discrepancy to have order

`#E_tilde(k_v)[2^infinity]`.

Thus the two source interfaces agree on the finite local length; no local discrepancy is discarded as a unit.

## Specialization to the protected all-`2N`-split field `K`

Protected WP09 chooses `K/Q` so that `2` and every prime `ell|N` split. Therefore:

- there are exactly two places `w,wbar|2`, each with `K_w ~= Q_2` and residue field `F_2`;
- for every `ell|N`, there are exactly two places above `ell`, each with local field canonically isomorphic to `Q_ell` as an extension of `Q_ell` under the chosen split embedding.

Protected WP07 gives

`#E_tilde(F_2)=3-a_2 in {2,4}`.

Put

`m_2 := ord_2(3-a_2)`.

Then each of the two `2`-adic local comparison terms has length `m_2`, so their ambient total length is

`2 m_2`.

At each split bad prime above `ell|N`, Lemma 9.6.7.3(ii) contributes length `ord_2(c_ell)`. There are two such places, so the ambient bad-prime total is

`2 sum_{ell|N} ord_2(c_ell)`.

Good primes away from `2N` have zero Tamagawa exponent and contribute no `2`-primary length.

Consequently the complete ambient comparison module for the protected field has exact length

`len_Z2 R_K(T)^vee`

` = 2 ord_2(3-a_2)`

`   + 2 sum_{ell|N} ord_2(c_ell)`.

This is an ambient target length. It is **not** the length of the actual global quotient unless the global comparison map is proved surjective.

## Exact bounded interface admitted downstream

After protected admission, MATHSOLVE may use the following exact statements.

1. For the selected good-ordinary elliptic curve over the protected totally imaginary `K`, at `p=2`,
   `H~^1_f(K,T_2(E)) ~= S_T^str(K)`.
2. There is a canonical injection
   `H~^1_f(K,T_2(E)) -> S_2(E/K)`
   into the compact classical `2`-primary Kummer Selmer group.
3. Define the actual comparison defect
   `J_K := im(S_2(E/K) -> R_K(T))`.
   Then there is an exact sequence
   `0 -> H~^1_f(K,T_2(E)) -> S_2(E/K) -> J_K -> 0`.
4. `J_K` is finite and is a subgroup of an explicit finite ambient module of exact length
   `2 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`.
5. No additional global Mordell–Weil base-change index occurs, by protected WP38.

The remaining mathematical task is to determine the globally hit subgroup `J_K` exactly, not to recompute the ambient local factors.

## Refined D2b boundary

The source comparison narrows

`MISSING_P2_NEKOVAR_EXTENDED_TO_PRIMITIVE_KUMMER_LOCAL_INDEX`

to

`MISSING_P2_KUMMER_GREENBERG_GLOBAL_HIT_SUBGROUP_OVER_K`.

This is an exact global-local incidence problem for the protected field `K`.

## Claim firewall

This source audit does not prove:

- `J_K = R_K(T)`;
- global localization surjectivity;
- fixed-`2` height nondegeneracy;
- Heegner-point primitivity;
- a height-one `(2)` analytic determinant generator;
- exact Disegni interpolation-factor valuations;
- the classical/WP00 normalization;
- the final WP06 descent;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.
