# BSD-001 source audit — BKS equivariant determinant lift at literal p=2

## 1. Purpose and authority boundary

This audit re-opens the Burns–Kurihara–Sano determinantal-zeta route only because downstream protected MATHSOLVE work has changed the dependency state since the earlier WP60A source audit.

Source under audit:

- David Burns, Masato Kurihara, Takamichi Sano, *On derivatives of Kato's Euler system and the Mazur–Tate conjecture*, arXiv:2103.11535; specifically Hypothesis 2.2, Lemma 4.2, Definition 4.3, and Proposition 5.2.
- David Burns, Takamichi Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems*, arXiv:1612.06187; specifically the equivariant determinant-to-Stark construction and its Stark-system freeness/isomorphism criteria.
- Burns–Sakamoto–Sano II, arXiv:1805.08448, for the Stark-to-Kolyvagin regulator and finite Kolyvagin-system control used by BKS Lemma 4.2.

This MATHFORGE record admits only the exact source dependency surface. It does not itself prove a literal-p=2 determinant lift, Fitting divisibility, primitivity, BSD, or certification.

## 2. Exact BKS Lemma 4.2 architecture

BKS Lemma 4.2 states, under BKS Hypothesis 2.2, that the Iwasawa Kato zeta class `z_{F_infinity}` belongs to the image of the canonical determinant map

`pi_{F_infinity}: det^{-1}_{Lambda_{F_infinity}} RGamma(Z_Sigma,T_{F_infinity}) -> H^1(Z_Sigma,T_{F_infinity})`.

The proof is explicitly finite-level and equivariant. For every cyclotomic layer `F_n` and coefficient exponent `m`, it uses the coefficient ring

`R_{n,m} := Z/p^m[Gal(F_n/Q)]`

and the composite

`det^{-1}_{R_{n,m}} RGamma(Z_Sigma,T_{F_n}/p^m)
  -> SS_1(T_{F_n}/p^m)
  -> KS_1(T_{F_n}/p^m)
  -> H^1(Z_Sigma,T_{F_n}/p^m)`.

The three substantive inputs are:

1. the determinant-to-Stark isomorphism `pi_{n,m}` (BKS cites Burns–Sano, Th. 3.12(ii) in the cited version);
2. the regulator isomorphism `Reg: SS_1 -> KS_1` (BKS cites Burns–Sakamoto–Sano II, Th. 5.2);
3. an Euler-system derivative for Kato's system whose first Kolyvagin component is exactly `z_{F_n} mod p^m`.

BKS then identifies `pi_{F_infinity}` with the inverse limit of these composites over `n,m`.

This is the exact dependency architecture for determinant membership. The later Bloch–Kato local-point calculations in BKS §5 are not part of the proof of Lemma 4.2 itself.

## 3. What BKS Hypothesis 2.2 does and does not authorize at p=2

BKS Hypothesis 2.2(iii) requires

`p does not divide 6 m N #E(Q)_tors Tam(E) product_{ell|pmN} #E^ns(F_ell)`.

It therefore excludes `p=2` literally. The exclusion may not be deleted from the published theorem.

In the BKS paper this hypothesis is used in several later local/Selmer-complex calculations, including vanishing of local `p`-power torsion and a free local formal-group generator. Those later uses are stronger than what Lemma 4.2's finite determinant/Stark/Kolyvagin proof sketch displays.

For Lemma 4.2 itself, the source dependency that must be replaced at literal `2` is the finite equivariant system chain above, together with integral Kato classes and the inverse-limit compatibility. A downstream proof must verify those claims independently; this audit does not infer them from Hypothesis 2.2.

## 4. Burns–Sano equivariant source restriction

Burns–Sano arXiv:1612.06187 sets `p` to be an odd prime in its global setup. The odd-prime convention is not purely typographical. In the equivariant Stark-system analysis the source uses vanishing of archimedean `p`-cohomology, for example when identifying the relevant global duality/local terms.

The source nevertheless separates two kinds of ingredients:

- characteristic-independent determinant/exterior-bidual algebra and the construction of the horizontal determinant-to-Stark map;
- arithmetic hypotheses used to show the resulting Stark-system module is free of rank one and that the determinant map is an isomorphism.

A literal-2 downstream replay must therefore account explicitly for the real-place correction rather than importing the source isomorphism unchanged.

## 5. New protected downstream facts unavailable to the old WP60A audit

The earlier negative WP60A BKS audit predated the following protected MATHSOLVE results:

1. WP60R: selected literal-2 finite-level replay of the BSS rank-one regulator/Kolyvagin theorem over `Z/2^m`, including the replacement of the small-prime localization/core-graph uses and the selected Theorem 5.2 replay.
2. WP60S: selected literal-2 inverse-limit replay of BSS Theorem 5.25 over the finite coefficient tower.
3. WP60T: selected literal-2 Euler-system derivative replay of BSS Theorem 6.12/Corollary 6.13 and the finite Corollary 6.15 application, including `kappa_m(c)_1 = c_Q mod 2^m` for admitted rank-one Euler systems such as Kato's.
4. WP32: the specifically real-place literal-2 comparison cone has equal degree-one and degree-two `Z_2` lengths and hence zero alternating determinant/Fitting valuation; WP32 does not supply a canonical unit-level trivialization.
5. WP35: the selected primitive cyclotomic Kummer module has a protected square finite-free `Lambda=Z_2[[T]]` presentation, closing the perfect determinant-realization boundary in the exact specialization-defect-accounting sense.
6. WP60A-A1: at `Lambda_(2)`, membership of the localized Kato class in the determinant lattice is exactly the one-sided height-one `(2)` Fitting divisibility; generator status is the separate primitivity equality.

These facts invalidate the earlier inference that the BKS route should remain closed merely because its displayed BSS regulator theorem had `p>3` in the published source. They do not, by themselves, prove the equivariant lift.

## 6. Remaining exact theorem gap after re-audit

BKS Lemma 4.2 requires finite stages over

`R_{n,m}=Z/2^m[Gamma_n]`, `Gamma_n=Gal(Q_n/Q)`,

not merely over the principal rings `Z/2^m` used in protected WP60R–WP60T.

For each `n,m`, `R_{n,m}` is a commutative local Artinian Gorenstein ring with maximal ideal generated by `2` and the augmentation ideal, and residue field `F_2`. The induced representation `T_{Q_n}/2^m` reduces modulo this maximal ideal to the same selected residual module `E[2]`.

Accordingly, the newly isolated downstream theorem target is:

`MISSING_P2_EQUIVARIANT_CYCLOTOMIC_DETERMINANT_STARK_KOLYVAGIN_REPLAY`.

A valid downstream closure must establish, for every `n,m` needed by the cyclotomic inverse system:

1. a literal-2, real-place-corrected determinant-to-Stark isomorphism over `R_{n,m}`;
2. a Stark-to-Kolyvagin regulator isomorphism over `R_{n,m}` using a justified equivariant extension of the protected small-prime replacement architecture;
3. a Kato-derived Kolyvagin system whose first component is exactly `z_{Q_n} mod 2^m`;
4. compatibility in both `n` and `m` sufficient to pass to the cyclotomic determinant map;
5. no use of the still-false full higher-level BSS H3.2(iii), H4.7(iii), or infinite H3.

If these conditions are proved, BKS Lemma 4.2's proof architecture can be replayed on the selected literal-2 lane and, by protected WP60A-A1, would establish the R5-LIFT one-sided height-one `(2)` Fitting divisibility. It would not establish determinant primitivity/R5-PRIM.

## 7. Source disposition

`BKS_P2_EQUIVARIANT_DETERMINANT_ROUTE_REOPENED_WITH_EXACT_GROUP_RING_REPLAY_OBLIGATION`.

This is a source/dependency disposition, not a mathematical theorem.

No screened current external theorem is admitted here as a substitute for the group-ring replay. In particular, an odd-prime Iwasawa main-conjecture theorem, a statement after inverting `2`, or a base-`Z/2^m` Kolyvagin theorem does not close this obligation.

## 8. Claim firewall

This source audit does not establish:

- `MISSING_P2_EQUIVARIANT_CYCLOTOMIC_DETERMINANT_STARK_KOLYVAGIN_REPLAY`;
- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- R5-LIFT;
- determinant primitivity or R5-PRIM;
- D2d or BSD-R2-A1;
- novelty, priority, or MATHCERT certification.
