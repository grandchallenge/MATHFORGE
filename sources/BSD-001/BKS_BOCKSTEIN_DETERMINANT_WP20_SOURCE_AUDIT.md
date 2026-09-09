# BSD-001 source audit — BKS Bockstein/determinant architecture versus selected `p=2`

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#151`.
- Protected Forge baseline: `0fe76d81147f34a814754bf09813b699e7bbf2e2`.
- Downstream protected MATHSOLVE baseline: `6bfb41402f216069b3b5ed001320170cc411b6cf`.
- Primary source: David Burns, Masato Kurihara, Takamichi Sano, *On derivatives of Kato's Euler system for elliptic curves*, Journal of the Mathematical Society of Japan 76 (2024), 855–919, DOI `10.2969/jmsj/90699069`.
- Disposition: `QUALIFIED_BKS_BOCKSTEIN_ARCHITECTURE_ODD_P_ONLY`.
- Claim class: bounded source/applicability evidence only; no BSD, theorem-nonexistence, or certification promotion.

## Exact downstream query

Protected WP20 proves the universal algebraic identity

`(coeff_T det A(T)) = Fitt^1_R(M) * B_A`

for a rank-one specialization `M`, with `B_A` the intrinsic rank-one Bockstein ideal.

The protected arithmetic obligations are now:

- D1: `MISSING_P2_PRIMITIVE_RANK1_DETERMINANT_REALIZATION`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

This audit asks whether Burns–Kurihara–Sano (BKS) supplies either obligation literally at `p=2`, or a separately composable theorem clause that may be admitted without extending an odd-prime theorem by analogy.

## Global prime range

BKS fixes an **odd prime `p`** at the outset of the paper. The same odd-prime standing assumption is repeated when the paper enters its main-conjecture/descent section.

Accordingly every theorem, construction, and comparison in the paper is stated inside a global odd-prime environment unless the authors explicitly provide a separate prime-independent statement. No such separate literal-`p=2` arithmetic theorem is identified in the clauses audited below.

This point is controlling: the fact that a local theorem statement does not repeat `p` odd does not authorize deleting the paper-wide standing hypothesis.

**Disposition:** `PAPER_WIDE_ODD_P_SCOPE`.

## Hypothesis 2.2 — structurally close, but still inside odd-`p` scope

Hypothesis 2.2 assumes, in substance:

1. the relevant global `H^1` is `Z_p`-free;
2. the algebraic rank `r` is positive;
3. `Sha[p^infinity]` is finite.

The accompanying remark notes that irreducibility of `E[p]` gives standard simplifications for the Tate module and rational `p`-torsion.

This hypothesis profile is structurally close to the protected selected rank-one setting. It does not override the paper-wide assumption that `p` is odd.

**Disposition:** `STRUCTURALLY_RELEVANT_HYPOTHESES_ODD_P_CONTEXT`.

## Bockstein regulator — exact architecture relevant to D2

BKS constructs canonical Bockstein maps and Bockstein regulators. In rank one, the source explicitly notes that the relevant Bockstein construction simplifies to the one-dimensional case.

This is materially relevant to protected WP20: it confirms that a regulator-like first-order factor is not an artificial feature introduced by the GCL matrix lemma. Positive-rank Euler-system/determinant formulas naturally contain a Bockstein/regulator contribution.

BKS Theorem 5.6 gives an exact comparison of the shape

`<x, R_Boc_omega>_p = log_omega(x) * R_p`,

where the source's Bockstein regulator is compared with its `p`-adic regulator through the formal logarithm.

This is exactly the kind of factorization needed for a D2 proof architecture. But Theorem 5.6 remains a theorem in a paper whose standing prime is odd. It is therefore not admitted here as a literal `p=2` comparison theorem.

**Disposition:** `BOCKSTEIN_TO_PADIC_REGULATOR_ARCHITECTURE_ODD_P_ONLY`.

## Generalized Perrin–Riou statement — conjectural at the BKS level

BKS formulates a Generalized Perrin–Riou Conjecture for the derivative of Kato's Euler system. In rank one the paper identifies this with the classical Perrin–Riou conjectural framework.

Thus the strongest general derivative-to-regulator statement in this part of BKS is not, merely by appearing in BKS, an unconditional theorem that can close D2.

**Disposition:** `GENERAL_DERIVATIVE_FORMULA_CONJECTURAL`.

## Theorem 6.2 — Rubin-type derivative/height formula

BKS Theorem 6.2 gives, in the good or nonsplit multiplicative setting, a formula of the source-normalized shape

`<x, kappa_infinity>_p
 = (1-1/alpha)^(-1) (1-1/beta) log_omega(x) * L_{S,p}^{(r)}`.

For rank one BKS explains that this recovers the classical Rubin/Perrin–Riou type formula.

The formula has the right D2 architecture:

`p-adic derivative` + `interpolation factors` + `height/logarithm`.

It nevertheless remains inside the global odd-prime scope of the paper. It is not a literal selected-`p=2` theorem interface.

**Disposition:** `RUBIN_DERIVATIVE_ARCHITECTURE_ODD_P_ONLY`.

## Corollary 6.7 — exact shape of the desired normalization, but conditional/general and odd-`p`

BKS Corollary 6.7 derives a `p`-adic Beilinson formula from the Generalized Perrin–Riou Conjecture. In the good/nonsplit case its source-normalized shape is

`(1-1/alpha)^(-1) (1-1/beta) L_{S,p}^{(r)}
 = [L_S^*(E,1)/(Omega_xi R_infinity)] * R_p`.

This is extremely close to the protected WP20 D2 target conceptually: after dividing by the Bockstein/`p`-adic-regulator factor, an analytic derivative is compared with the complex leading term divided by the real regulator, with interpolation corrections explicit.

However:

1. the ambient source still fixes `p` odd;
2. the corollary is derived from the Generalized Perrin–Riou Conjecture in the general positive-rank framework;
3. its period, imprimitive `S`-factor, interpolation, local-condition, and regulator normalizations are not yet the protected WP00 normalization;
4. it does not by itself identify the protected primitive Kummer module `X_E` or its WP20 Bockstein ideal.

BKS Remark 6.8 is therefore the important successor pointer: it states that in rank one, in the ordinary good-reduction case, the relevant formula was already proved by Perrin–Riou, citing B. Perrin–Riou, *Points de Heegner et dérivées de fonctions L p-adiques*, Inventiones Mathematicae 89 (1987), 455–510, in particular Corollary 1.8.

**Disposition:** `D2_ARCHITECTURE_CONFIRMED_SUCCESSOR_PERRIN_RIOU_REQUIRED`.

## Section 7 — determinant/main-conjecture lane does not supply D1 at `p=2`

BKS Section 7 again explicitly assumes `p` odd.

Its main-conjecture descent results are therefore not literal selected-`p=2` determinant-realization theorems. In particular, the audited results either:

- assume an Iwasawa main conjecture;
- produce a conclusion only up to a `Z_p` unit at an intermediate stage; or
- combine the main conjecture with the Generalized Perrin–Riou input and nonvanishing of a Bockstein regulator to deduce a `p`-part BSD-style statement.

None of these clauses supplies the protected D1 requirement at `p=2`:

`exact primitive Kummer rank-one determinant realization with both WP13 Tamagawa regimes and no hidden 2-power`.

**Disposition:** `MAIN_CONJECTURE_DETERMINANT_LANE_ODD_P_NOT_D1`.

## Primitive Kummer comparison remains unsupplied

BKS uses Selmer-complex and Euler-system constructions adapted to its own local and compact-support conventions. This audit does not identify an exact theorem in BKS proving that its specialized rank-one module is the protected WP16B object

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`

with classical primitive Kummer conditions at `2` and every bad prime.

Therefore, even apart from the odd-prime restriction, protected D1 would still require exact local-condition and specialization comparison.

No Greenberg/ordinary or compact-support object is silently identified with `X_E`.

**Disposition:** `PRIMITIVE_KUMMER_SPECIALIZATION_COMPARISON_UNSUPPLIED`.

## Exact WP00 normalization remains unsupplied

The BKS formulas display the right kinds of factors, but a selected D2 theorem must still determine every `2`-adic contribution from:

- the ordinary/unit-root interpolation factors at `2`;
- the source's imprimitive `S`-Euler factors;
- Kummer versus ordinary local conditions at `2`;
- primitive versus imprimitive local conditions at bad primes;
- WP13 even-Tamagawa/residual-conductor-drop factors;
- period/Manin normalization;
- the Bockstein/`p`-adic regulator and its relation to the WP00 Néron–Tate regulator;
- augmentation/derivative-parameter normalization;
- any finite lattice or specialization index.

BKS does not license declaring these factors `2`-adic units in the selected setting.

## Provider conclusion

BKS strongly validates the **architecture** protected by WP20:

`positive-rank determinant derivative
 = finite algebraic/Fitting contribution
   x Bockstein-regulator contribution`,

followed by a normalization step relating a `p`-adic derivative divided by the regulator factor to a complex leading term.

But BKS itself is globally an **odd-prime** paper. It therefore supplies neither D1 nor D2 as a literal selected-`p=2` theorem.

This audit does not prove that the required `p=2` theorem does not exist.

## Successor query

The next bounded source query is only:

> Audit Perrin–Riou, *Points de Heegner et dérivées de fonctions L p-adiques*, Invent. Math. 89 (1987), especially Corollary 1.8, for the exact prime range and hypotheses of the ordinary rank-one formula cited by BKS Remark 6.8. Determine whether it literally includes `p=2`, and if so, compare its interpolation, height/regulator, period, and local-condition normalization against protected D2.

Do not broaden to another generic Iwasawa survey before this prime-range question is resolved.

## Claim firewall

This audit does not prove:

- D1 or D2;
- a `p=2` extension of any BKS theorem;
- equality between BKS Selmer complexes and the protected primitive Kummer module;
- equality of Bockstein and WP00 Néron–Tate regulators;
- the selected first-Fitting reciprocity theorem;
- `BSD-R2-A1`;
- theorem nonexistence;
- MATHCERT certification, novelty, or priority.
