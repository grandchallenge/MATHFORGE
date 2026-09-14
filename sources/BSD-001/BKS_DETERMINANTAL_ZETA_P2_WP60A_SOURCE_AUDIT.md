# BSD-001 source audit — determinantal-zeta architecture at literal `p=2`

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#186`.
- Downstream execution tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `c8af223d0e05f999b4977a0dae5b1b5281eff93e`.
- Protected MATHSOLVE baseline: `24fb349e28e4cbb5e034f4684edcc413975aed04`.
- Constitutional issuance anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary source A: David Burns, Masato Kurihara, Takamichi Sano, *On derivatives of Kato's Euler system and the Mazur–Tate Conjecture*, arXiv:2103.11535; published in IMRN (2025), rnaf012.
- Primary source B: David Burns, Ryotaro Sakamoto, Takamichi Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448; accepted in Algebra & Number Theory.
- Previously protected related audit: `sources/BSD-001/BKS_BOCKSTEIN_DETERMINANT_WP20_SOURCE_AUDIT.md`.
- Previously protected Kato audit: `sources/BSD-001/KATO_P2_HEIGHT_ONE_WP17B_SOURCE_AUDIT.md`.
- Disposition: `QUALIFIED_DETERMINANTAL_ZETA_ARCHITECTURE_WITH_LITERAL_P2_LIFT_AND_PRIMITIVITY_GAP`.
- Claim class: bounded source/applicability evidence only; no theorem promotion, impossibility claim, literature-exhaustiveness claim, or certification.

## Exact downstream query

Protected MATHSOLVE WP60A asks whether one can bypass the missing all-height-one ordinary main-conjecture theorem by constructing an integral analytic determinant generator directly at residue characteristic `2`.

The protected algebraic target is already exact:

`Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`

and protected WP35 supplies a square cyclotomic presentation with

`(coeff_T det A(T)) Z_2
 = Fitt^0(C_E^vee) Fitt^1(X_E) B_A`.

Protected WP52A separately evaluates the full finite strict/Kummer determinant correction. Thus the source question is now narrowly:

> Does the determinantal-zeta/Mazur–Tate machinery supply at literal `p=2` an integral lift of Kato's zeta class into the relevant determinant lattice, together with enough primitivity or reverse divisibility at the height-one prime `(2)` to determine the missing exponent?

## Source A: the determinant-line architecture is exactly relevant

Burns–Kurihara–Sano construct, for cyclotomic Iwasawa cohomology, a determinant-line object whose image in first cohomology is Kato's Iwasawa zeta class. This is the closest located published architecture to the WP60A target.

In §4.2, with `T_K=T\otimes\Lambda_K`, the source constructs a determinantal zeta element in

`det^{-1}_{Lambda_K} RGamma(O_{K,S},T_K)`.

Lemma 4.2 asserts, under Hypothesis 2.2, that Kato's Iwasawa zeta class `z_{F_infinity}` belongs to the image of the canonical map from the determinant line to `H^1`. Definition 4.3 then defines the determinantal zeta element by lifting this class and projecting to finite layers.

The proof of Lemma 4.2 is not merely formal determinant algebra. It passes through the authors' Stark-system and Kolyvagin-system machinery: the determinant module is mapped to Stark systems, then via the regulator to Kolyvagin systems, and the first Kolyvagin component is identified with Kato's zeta class.

This is materially stronger than the already-protected abstract matrix identity. It identifies the precise arithmetic construction that would be needed for WP60A.

**Disposition:** `EXACTLY_RELEVANT_DETERMINANT_LIFT_ARCHITECTURE`.

## Source A: Hypothesis 2.2 excludes literal `p=2`

The applicability obstruction is explicit.

Hypothesis 2.2 requires, among other conditions,

`p \nmid 6 m N #E(Q)_tors Tam(E) product_{ell|pmN} #E^ns(F_ell)`.

In particular the condition itself excludes `p=2` and `p=3`.

Remark 2.8 makes the intended scope explicit: the methods in this paper neglect the `2`-primary and `3`-primary components.

Therefore Lemma 4.2 and the resulting determinant lift are not literal selected-`p=2` theorem interfaces.

This is not a cosmetic prime-range restriction that can be removed by deleting an odd-prime phrase. The proof of the lift invokes the higher Kolyvagin/Stark regulator machinery audited below.

**Disposition:** `BKS_DETERMINANT_LIFT_NOT_LITERAL_P2`.

## Source B: the regulator isomorphism used by the lift is not a `p=2` theorem

Burns–Sakamoto–Sano develop the general higher-rank Euler/Kolyvagin/Stark-system machinery used by the determinant-lift argument.

The paper works in an odd-prime setting. More importantly, the decisive regulator theorem is Theorem 5.25, whose hypothesis explicitly begins

`Suppose p>3`.

Under its hypotheses the regulator map

`Reg_r : SS_r -> KS_r`

is an isomorphism and the Kolyvagin-system module controls Fitting ideals of the corresponding Selmer modules.

Thus the exact regulator isomorphism and Fitting-control mechanism that turns a Stark/determinant object into a Kolyvagin-system statement is not available from this source at residue characteristic `2`.

The source therefore does not authorize reusing the proof of BKS Lemma 4.2 unchanged at `p=2`.

**Disposition:** `STARK_KOLYVAGIN_REGULATOR_ISOMORPHISM_P_GT_3`.

## Determinant lift and primitivity are distinct obligations

The source architecture separates two facts that must not be conflated downstream.

### Obligation A — determinant lift

One must first produce an integral determinant element whose image in `H^1` is Kato's zeta class, or construct a finite-level replacement with the same specialization property.

For the selected literal-`p=2` branch the currently audited sources do not supply this step.

Record the WP60A sub-boundary

`MISSING_P2_KATO_ZETA_DETERMINANT_LIFT_AT_RESIDUE_CHARACTERISTIC_2`.

### Obligation B — height-one `(2)` primitivity

Existence of a determinant lift does not by itself prove that the element is a basis of the integral determinant lattice, nor that its coordinate has no extra factor of `2`.

Burns–Kurihara–Sano formulate the relevant equality of their determinantal zeta element with the algebraic special element as a separate statement. Proposition 4.4 obtains the equality from their earlier conjectural input, and Theorem 4.6 derives the Mazur–Tate conclusion assuming that equality.

In rank one this is precisely the kind of reverse-divisibility/primitivity information that cannot be replaced by the mere existence of a lift.

Record the second WP60A sub-boundary

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

These two sub-boundaries sit under the already-protected campaign boundary

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

## Relation to the protected Kato audit

The protected Kato WP17B audit and the present audit are consistent and complementary.

Kato supplies genuine ordinary characteristic control at `p=2` away from the height-one prime containing `2`, but his all-height-one integral upgrade assumes `p != 2`.

The BKS determinant architecture shows how one can conceptually bypass an abstract characteristic-ideal comparison by lifting Kato's zeta class into a determinant line. But the located proof of that lift itself passes through arithmetic machinery whose hypotheses exclude `p=2`.

Accordingly the height-one `(2)` defect has not disappeared; it has been localized to a more concrete construction/primitivity problem.

## Finite-level bypass remains logically open

The source failure above does not prove that a literal-`p=2` determinant lift is impossible.

In particular, WP60A may attempt a direct finite-level construction that avoids the higher Kolyvagin/Stark regulator isomorphism. Such a construction would have to specify exactly:

1. the finite-level perfect complex or presentation;
2. the integral determinant lattice over `Z_2` or the relevant group ring;
3. the analytic/modular-symbol or zeta element;
4. the map sending the determinant element to the analytic class;
5. the primitive Kummer local-condition comparison at `2` and at every bad prime;
6. specialization to the protected rank-one first-Fitting target;
7. a proof of primitivity or exact reverse divisibility at `(2)`.

A result only after inverting `2`, or only up to an unspecified power of `2`, does not satisfy WP59 reopening condition `R5`.

## Nearby literal-`2` modular-element results do not supply a uniform interface

Recent literal-`2` work on Mazur–Tate elements and rank-one curves provides useful evidence that residue characteristic `2` is not intrinsically inaccessible. However, the screened examples are special-family results with hypotheses not implied by the selected `BSD-R2-A1` class. In particular, located CM/twist families may have reduction behavior at `2` incompatible with the selected good-ordinary branch.

Such papers may inform a proof construction or WP60C computation, but they are not admitted here as a uniform theorem for the selected class.

## Exact provider conclusion

The determinantal-zeta route is the right architecture for WP60A, but the located source chain does not close literal `p=2`.

The missing mathematics is now more precise than a generic `p=2` main-conjecture debt:

1. construct a literal-`p=2` determinant lift of the analytic/Kato zeta class, or an exact finite-level replacement; and
2. prove that this determinant element is primitive at the height-one prime `(2)`, equivalently supply the exact reverse divisibility/basis statement required to remove any residual factor of `2`.

Combined source boundary:

`MISSING_LITERAL_P2_KATO_ZETA_DETERMINANT_LIFT_AND_PRIMITIVITY_AT_HEIGHT_ONE_2`.

This refines, but does not close, protected D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

**Disposition:** `QUALIFIED_DETERMINANTAL_ZETA_ARCHITECTURE_WITH_LITERAL_P2_LIFT_AND_PRIMITIVITY_GAP`.

## Reopening contract for WP60A

Reopen the determinant lane immediately on a protected result that supplies either:

- an integral literal-`p=2` determinant lift plus a proof of primitivity/reverse divisibility at `(2)`; or
- a finite-level primitive Kummer/Fitting reciprocity theorem that directly determines the same height-one `(2)` exponent without using the odd-prime regulator chain.

A determinant lift without primitivity is partial progress only. A rational determinant identity after inverting `2` is insufficient.

## Claim firewall

This audit does not establish:

- a `p=2` extension of Burns–Kurihara–Sano or Burns–Sakamoto–Sano;
- a determinant lift at `p=2`;
- determinant primitivity at `(2)`;
- equality of ordinary and primitive Kummer local conditions at `2`;
- the selected first-Fitting reciprocity theorem;
- WP59 reopening condition `R5`;
- `BSD-R2-A1`;
- nonexistence of another source or proof;
- literature exhaustiveness;
- novelty, priority, or MATHCERT certification.
