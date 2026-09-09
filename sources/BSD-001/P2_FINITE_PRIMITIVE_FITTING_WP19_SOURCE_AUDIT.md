# BSD-001 source audit — literal `p=2` finite-level primitive/Fitting screen for WP19

## Record

- Campaign: `BSD-001`.
- Provider baseline: `grandchallenge/MATHFORGE@6b0bc6444bcf675c1b7774caa1f719efabdd49f6`.
- Downstream protected MATHSOLVE baseline: `grandchallenge/MATHSOLVE@f7f88319550881a615edbea6d3425158d20136e7`.
- Downstream exact invariant:

  `T_E := Tor_{Z_2}(Sel_{2^infinity}^{Kum}(E/Q)^vee)`

  with

  `Fitt^0_{Z_2}(T_E) = 2^{lim_n s_n(E)} Z_2`.

- Selected residual/local branch: good ordinary at `2`, globally irreducible/surjective `E[2]` with image `GL_2(F_2) ~= S_3`, semistable, both WP13 Tamagawa regimes retained.
- Disposition: `QUALIFIED_P2_FINITE_PRIMITIVE_FITTING_SOURCE_GAP`.
- Claim class: bounded source/applicability evidence only. This audit does not assert theorem nonexistence, BSD, novelty, or certification.

## Exact source question

WP18 has now closed the two-control normalization atlas exactly. The remaining issue is no longer whether the primitive Kummer/Fitting normalization is viable. The remaining issue is uniform integral control.

This audit therefore asks a narrow question:

> Does a literal `p=2` theorem already determine the finite-level or specialized primitive Kummer/Fitting invariant needed by WP16B for good-ordinary curves with irreducible/surjective `E[2]`, while retaining even-Tamagawa/residual-conductor-drop cases?

The screen is intentionally limited to the closest theorem shapes surfaced after WP18:

1. Chan-Ho Kim's finite-layer anticyclotomic strong Fitting theorem;
2. Kurihara's strong Mazur-Tate/Fitting formulation that underlies this theorem family;
3. Matsuno's literal `p=2` ordinary Iwasawa theorem.

## Source A — Chan-Ho Kim finite-layer anticyclotomic Fitting theorem

### Primary source

Chan-Ho Kim, *On the Fitting ideals of anticyclotomic Selmer groups of elliptic curves with good ordinary reduction*, Canadian Mathematical Bulletin 69 (2026), 21–31; published online 14 July 2025; DOI `10.4153/S000843952510088X`; arXiv `2505.09125`.

### Theorem shape

Kim proves a finite-layer anticyclotomic analogue of Kurihara's strong main conjecture. The theorem completely determines an initial Fitting ideal of dual Selmer groups over finite subextensions of an imaginary quadratic anticyclotomic `Z_p`-extension in terms of Bertolini-Darmon theta elements.

This is structurally very close to the kind of finite-level theorem WP19 would prefer.

### Literal hypotheses that exclude the selected branch

The paper begins with:

- `p >= 5`;
- `p` good ordinary for `E`;
- mod-`p` representation surjective;
- residual representation ramified at every prime dividing the conductor, with the stated consequence that `p` does not divide the Tamagawa factors;
- an imaginary quadratic field with the stated splitting and definiteness hypotheses.

Therefore:

1. the theorem does not include `p=2` literally;
2. it does not cover WP13 regime B, where an even Tamagawa factor is part of the selected class and the residual conductor drops at exactly that support;
3. deleting `p>=5` or the ramification/Tamagawa hypothesis would change the theorem and is not an allowed specialization.

**Disposition:** `STRONG_FINITE_FITTING_SHAPE_P_GE_5_AND_TAMAGAWA_PRIME_TO_P`.

## Source B — Kurihara strong Mazur-Tate/Fitting formulation

### Primary source

Masato Kurihara, *On the Tate Shafarevich groups over cyclotomic fields of an elliptic curve with supersingular reduction I*, Inventiones Mathematicae 149 (2002), 195–224. The paper's Conjecture 0.3 is the strong Mazur-Tate/Fitting formulation cited by the later finite-layer literature.

### Prime and local restrictions

Conjecture 0.3 is stated for an **odd prime** `p`, assumes good reduction at `p`, no rational point of order `p`, and `p` not dividing the Tamagawa factor. It predicts the relevant finite-layer Fitting ideal in terms of Mazur-Tate modular elements.

Thus the canonical strong finite-layer theorem shape itself is not a literal selected `p=2` theorem, and its stated Tamagawa restriction would exclude WP13 regime B at the selected prime.

This source is useful as a theorem-design template only. A `p=2` theorem cannot be obtained by typographical substitution.

**Disposition:** `STRONG_MAZUR_TATE_FITTING_TEMPLATE_ODD_P`.

## Source C — Matsuno literal `p=2` ordinary Iwasawa theorem

### Primary source

Kazuo Matsuno, *On the 2-adic Iwasawa invariants of ordinary elliptic curves*, International Journal of Number Theory 4 (2008), 403–422; DOI `10.1142/S1793042108001468`.

### Positive `p=2` content

Matsuno works explicitly at `p=2` for good-ordinary elliptic curves and extends variation formulas for Iwasawa invariants to the cyclotomic `Z_2` setting.

For semistable curves, Theorem 5.1 assumes

`mu_{E,2}(Q)=0`

and then proves that suitable quadratic twists also have `mu=0`, together with an explicit formula for the variation of the `lambda`-invariant.

This is genuine ordinary `p=2` Iwasawa theory and is directly relevant to the protected cyclotomic height-one `(2)` diagnosis.

### Why it does not close the selected debt

The missing selected input is precisely a theorem that determines or eliminates the height-one `(2)` / relative-`mu` exponent for the base curve in the irreducible/surjective branch. Matsuno's theorem assumes base `mu=0`; it does not prove that hypothesis for the selected base curve.

Accordingly it can propagate an independently known `mu=0` statement through a twist comparison, but it cannot supply the missing base `mu=0` theorem itself.

Moreover, the theorem controls cyclotomic Iwasawa invariants. It does not by itself identify:

- the Greenberg/ordinary Selmer structure with WP16B's primitive finite Kummer tower at `2`;
- primitive and imprimitive bad-prime local conditions with exact even-Tamagawa corrections;
- the specialized rank-one free quotient and the finite torsion module `T_E`;
- the exact WP00 complex leading-term normalization.

**Disposition:** `LITERAL_P2_ORDINARY_VARIATION_REQUIRES_BASE_MU_ZERO`.

## Joint diagnosis

The three closest theorem shapes separate the remaining problem sharply.

### What exists

- A modern finite-layer strong Fitting theorem for good-ordinary, surjective residual representations exists in the anticyclotomic setting, but only for `p>=5` and under a Tamagawa-prime-to-`p` residual ramification hypothesis.
- The strong Mazur-Tate finite-layer Fitting template is itself formulated for odd `p` and Tamagawa prime to `p`.
- Literal ordinary `p=2` Iwasawa variation theory exists, but its semistable twist theorem assumes the base `mu_2=0` statement that WP17B/WP17C identify as missing.

### What is still not supplied by this screen

No screened source supplies a theorem with all of the following simultaneously:

1. literal `p=2`;
2. good ordinary reduction at `2`;
3. irreducible/surjective `E[2] ~= S_3`;
4. exact integral control rather than a statement after inverting `2`;
5. primitive classical Kummer local conditions or an exact comparison to them;
6. the rank-one saturated free-direction quotient required to isolate `T_E`;
7. both WP13 regimes, including even Tamagawa and residual-conductor drop;
8. an exact Fitting/length output sufficient to determine `v_2(Fitt^0_{Z_2}(T_E))`.

This is a bounded source result, not a theorem-nonexistence result.

## Consequence for theorem construction

The evidence now favors a direct finite-level route over stacking further cyclotomic comparisons.

A useful new theorem would be a **rank-one derived strong Mazur-Tate/primitive-Fitting theorem at `p=2`**. It should not apply `Fitt^0` to the whole rank-one specialization. It must first quotient the canonical saturated free line and then determine the initial Fitting ideal of the resulting finite torsion object, with exact local correction factors.

Schematically, the desired theorem must reach

`v_2(Fitt^0_{Z_2}(T_E))`

from a finite-level analytic/determinant element while retaining:

- the primitive Kummer condition at `2`;
- every bad-prime Kummer/Tamagawa correction;
- the rank-one augmentation/derivative normalization;
- every power of `2`.

A theorem over the protected WP09 field `K` remains admissible only if the WP06 integral plus/minus and twist defects are retained exactly when descending to `Q`.

## Updated bounded source boundary

The source-level boundary can now be stated more precisely as

`P2_RANK1_DERIVED_PRIMITIVE_MAZUR_TATE_FITTING_OR_BASE_MU_ZERO_CONTROL`.

Two proof branches remain:

1. **finite-level branch:** construct the literal `p=2` rank-one derived primitive-Fitting theorem described above;
2. **cyclotomic branch:** prove base `mu_2=0` on the selected good-ordinary surjective `S_3` branch, then discharge every WP16B specialization/local-condition comparison.

The finite-level branch has fewer independent comparison obligations and is the preferred theorem-construction target after WP18.

## Claim firewall

This audit does not prove:

- that the desired theorem does not exist elsewhere;
- `mu_2(E)=0` for the selected class;
- any `p=2` extension of Kim's or Kurihara's odd-prime theorem;
- equality between Greenberg and primitive Kummer local conditions;
- a rank-one derived Mazur-Tate/Fitting identity;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.
