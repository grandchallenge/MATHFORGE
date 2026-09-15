# BSD-001 source audit — literal-2 BSS inverse-limit dependencies after WP60R

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#210`.
- Downstream operation: `grandchallenge/MATHSOLVE#245` (`WP60S`).
- Protected MATHFORGE entering head: `7a7c1bcaba3c31726e34353f311a6de6d9530dbc`.
- Protected MATHSOLVE anchor: `245860ce3d7307a505e48b4165be0850327f996a`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary source: David Burns, Ryotaro Sakamoto, Takamichi Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, especially §§4.3 and 5.5, Hypothesis 4.7, Lemma 4.10, Definition 4.11, Theorem 4.12, Definition 5.24 and Theorem 5.25 in the arXiv-v1 numbering (Definitions 5.26–5.27 and Theorem 5.28 in the accepted-version numbering).
- Claim class: bounded source/dependency interface only.

## Exact downstream question

Protected MATHSOLVE WP60R proves the selected literal-`2` finite-level conclusions of BSS Theorem 5.2 for every coefficient ring `R_m=Z/2^m`, while preserving the fact that the full higher-level restriction-vanishing statement is false. The question is whether BSS §5.5 can still be replayed by replacing the uses of Hypothesis 4.7(iii) that feed the cross-level machinery, rather than asserting the false standing hypothesis.

## 1. The published standing hypothesis is genuinely stronger than the selected lane

BSS §4.3 assumes Hypothesis 4.7. Clause (iii) requires

`H^1(K(T)_{p^infty}/K,Tbar)=0`

and the analogous vanishing for the dual residual representation.

The source then uses clause (iii) to deduce finite auxiliary-field vanishing for every quotient. In particular, immediately before the construction of the Stark-system reduction maps it proves

`H^1(K(A)_{p^m}/K,A)=0`

and the dual analogue by filtering `A` by powers of `p`.

This is exactly the route that is unavailable on the protected selected literal-`2` lane: WP60K/WP60M show that the corresponding higher finite group is nonzero of order two.

Therefore record:

`FULL_BSS_HYPOTHESIS_4_7_III_NOT_AVAILABLE_ON_SELECTED_P2_LANE`.

The source cannot be imported unchanged.

## 2. Where clause 4.7(iii) enters the cross-level Stark construction

After deriving the finite cohomology vanishing from Hypothesis 4.7(iii), the source fixes the level-`m` useful-prime sets `P_m`, with `N_{m+1} subset N_m`, and assumes finite Hypothesis 4.2 at every level.

For an auxiliary ideal at level `m+1` with dual modified Selmer group zero, the source uses Corollary 3.8 and Lemma 3.10 to obtain the coefficient-reduction isomorphism

`H^1_{F_n}(K,T/p^(m+1)T) tensor R/(p^m)
  ~= H^1_{F_n}(K,T/p^mT)`.

It then applies the exterior-bidual reduction map of Corollary 2.7 to construct

`SS^r(T/p^(m+1)T,F) -> SS^r(T/p^mT,F)`.

Lemma 4.10 proves that this map is surjective and that the Stark-system ideals reduce compatibly.

The dependency is therefore precise: Hypothesis 4.7(iii) is not used as an extra ingredient after Lemma 3.10; it is used upstream to force the unrestricted finite auxiliary-field vanishing needed to invoke the source's general coefficient-reduction theorem.

## 3. Protected WP60R/WP60M replace exactly that upstream use

Protected MATHSOLVE WP60M proves, for every selected finite level, that the unique nonzero global restriction-kernel defect violates a fixed canonical local condition retained by every selected BSS modification. Consequently restriction is injective on the actual modified primal and dual Selmer classes used by the proof, and the BSS Lemma 3.10 coefficient-reduction argument is available on the selected free modified-Selmer modules.

Protected WP60R additionally proves finite Hypothesis 4.2 at every selected level, including existence of a dual-zero auxiliary modification and freeness of the corresponding primal modified Selmer group.

These protected results supply exactly the two ingredients used in the source construction of the Stark transition map:

1. a dual-zero level-`m+1` core vertex with the required free primal module;
2. the coefficient-reduction isomorphism for that selected modified Selmer module.

Hence the construction and surjectivity proof of Lemma 4.10 replay on the selected literal-`2` lane without asserting the false global cohomology vanishing.

Record:

`SELECTED_P2_STARK_CROSS_LEVEL_REDUCTION_REPLACEMENT_AVAILABLE`.

## 4. Core-vertex persistence is coefficient-reduction bookkeeping

In §5.5 the source starts with a core vertex `n in N_{m+1}` and states, by Corollary 3.8, that it remains core at level `m`.

This step is a finite coefficient-reduction statement for the modified dual Selmer module. On the selected lane the same conclusion follows from the protected cartesian/coefficient-reduction interface: the zero dual module at level `m+1` has zero lower-level reduction, while the protected core-rank bookkeeping is constant across the finite quotients.

No separate use of infinite Hypothesis 4.7(iii) occurs once the selected coefficient-reduction interface is supplied.

Record:

`SELECTED_P2_CORE_VERTEX_PERSISTS_UNDER_COEFFICIENT_REDUCTION`.

## 5. Kolyvagin transition maps can be reconstructed from the protected regulator isomorphisms

The source says that, once a level-`m+1` core vertex remains core at level `m`, one constructs

`KS^r(T/p^(m+1)T,F) -> KS^r(T/p^mT,F)`

"in the same way as in §4.3" so that the square with the Stark regulator maps commutes.

Protected WP60R gives, at every selected finite level, the regulator isomorphism of finite Theorem 5.2(i). Therefore the selected transition map can equivalently be defined by conjugating the protected Stark transition map:

`KS_{m+1}
  --Reg_{m+1}^{-1}--> SS_{m+1}
  --> SS_m
  --Reg_m--> KS_m`.

This construction is canonical once the finite regulator maps and Stark reduction map are fixed, and the regulator square commutes by definition. It uses no infinite auxiliary-field vanishing.

Record:

`SELECTED_P2_KOLYVAGIN_CROSS_LEVEL_REDUCTION_REPLACEMENT_AVAILABLE`.

## 6. Inverse-limit Stark freeness and Fitting control use only the repaired finite interfaces

Lemma 4.10(i) gives surjective transitions between the finite Stark modules. Each finite module is free of rank one by the finite Stark theorem under finite Hypothesis 4.2. Theorem 4.12(i) then obtains rank-one freeness of

`SS^r(T,F)=lim_m SS^r(T/p^mT,F)`.

Theorem 4.12(ii) identifies the inverse-limit Stark ideals with the integral Fitting ideals. The proof reduces finite Fitting ideals modulo `p^m`, uses Corollary 3.8 for coefficient compatibility, and finally uses completeness of the noetherian coefficient ring so ideals are closed.

On the selected elliptic lane the coefficient ring is `Z_2`, hence complete, noetherian, local, Gorenstein and principal. Protected WP60R supplies the finite Theorem 5.2/Fitting statements; protected WP60M/WP60R supply the required coefficient compatibility. Thus the inverse-limit Stark-system and Fitting-ideal passage is available without full Hypothesis 4.7(iii).

Record:

`SELECTED_P2_STARK_INVERSE_LIMIT_FITTING_PASSAGE_AVAILABLE`.

## 7. Theorem 5.25 has no further proof ingredient after the transition system exists

After constructing the Kolyvagin transition maps, BSS Definition 5.24 defines

`KS^r(T,F)=lim_m KS^r(T/p^mT,F)`.

The source states that the finite regulator maps induce the integral regulator map. It then uses Corollary 3.8 together with finite Theorem 5.2(ii) to obtain compatibility of the ideals `I_i(kappa^(m))` and defines their inverse limits.

Theorem 5.25 states the integral regulator isomorphism/rank-one freeness and the Fitting-ideal inclusions/equalities. Its proof is explicit: claims (i), (ii) and (iii) are direct consequences of the corresponding claims of finite Theorem 5.2.

Therefore, after replacing the cross-level construction as in §§3–6 above, there is no additional occurrence of Hypothesis 4.7(iii) inside the proof of Theorem 5.25 itself.

Record the bounded provider disposition:

`SELECTED_P2_BSS_THEOREM_5_25_INVERSE_LIMIT_DEPENDENCIES_REPLACED`.

This means only that downstream MATHSOLVE may replay Theorem 5.25 from protected WP60R plus the selected cross-level replacements above. It does not make full Hypothesis 4.7 true.

## 8. Claim firewall

This audit does not establish:

- full BSS Hypothesis 4.7, especially clause (iii);
- the protected infinite H3 condition;
- BSS Corollary 6.15 or the Euler-system-to-Kolyvagin-system map at literal `2`;
- height-one `(2)` Kato/Fitting divisibility;
- determinant primitivity at `(2)`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.
