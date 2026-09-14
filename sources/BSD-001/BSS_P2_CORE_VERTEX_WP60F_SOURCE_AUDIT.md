# BSD-001 source audit — BSS literal-`p=2` core-vertex and elliptic-image proof mechanism

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#192`.
- Downstream tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `8d49d253fd10708f09b8cafa262de276bed88f23`.
- Protected MATHSOLVE anchor: `c2f036fd935238a880780685a927c26ec0de2d4e`.
- Constitutional anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary sources:
  1. Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, arXiv:1805.08448.
  2. Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, III: applications*, arXiv:1902.07002.
- Disposition: `P2_FITTING_CONTROL_REQUIRES_NEW_CORE_VERTEX_LOCALIZATION_AND_ELLIPTIC_HYPOTHESIS_VERIFICATION`.
- Claim class: bounded primary-source proof-dependency audit only.

## Exact downstream query

Protected WP60E records that the concrete finite-level Kato-derivative / Fitting application theorems screened so far do not apply at literal `p=2`.

WP60F asks a deeper question: **where does the small-prime restriction enter the proof mechanism?**

The distinction matters because an odd-prime restriction in an application theorem can arise either from a replaceable verification lemma or from the core Kolyvagin/Fitting-control architecture itself.

This audit therefore separates:

1. construction of a higher Kolyvagin derivative;
2. freeness/control of the Kolyvagin-system module and the resulting Fitting containment;
3. elliptic-curve verification of the standard Galois hypotheses.

## Source A — BSS II: derivative construction versus Fitting control

### A1. The displayed higher-derivative theorem is not the same statement as Fitting control

BSS II §6.4, Theorem 6.12 constructs the higher Kolyvagin derivative under Hypotheses 6.1, 6.7 and 6.11. Its displayed statement does not itself contain the condition `p>3`.

Corollary 6.13 packages this construction as a canonical homomorphism from higher-rank Euler systems to higher-rank Kolyvagin systems.

By contrast, the Fitting-control consequence is Corollary 6.15, which explicitly begins:

`Suppose p > 3.`

and then invokes Theorem 5.2.

The article's introductory summary fixes an odd prime `p`, and the rank-one proof of Theorem 6.12 is tied to the Mazur–Rubin framework. Accordingly, the protected interface does **not** assert that Theorem 6.12 is already a literal-`p=2` theorem. The important bounded conclusion here is narrower: the source shows that the explicit `p>3` hypothesis used for Fitting control is not simply the statement “the derivative formula can be written down.”

**Disposition:** `DERIVATIVE_CONSTRUCTION_AND_FITTING_CONTROL_ARE_DISTINCT_INTERFACES`.

### A2. The simultaneous-localization lemma

BSS II Lemma 3.9 is the Chebotarev input used throughout the core-vertex argument.

For nonzero classes

`c_1,...,c_s in H^1(K,A)`

and

`c_1^*,...,c_t^* in H^1(K,A^*(1))`,

it guarantees a positive-density set of primes at which all localizations are nonzero under the numerical hypothesis

`s+t < p`.

The proof uses this inequality to show that the relevant Galois group is not covered by the union of the `s+t` proper subgroups arising from the classes.

At `p=2`, the lemma does not cover simultaneous nonvanishing of one primal and one dual class, because that case has

`s=t=1`, hence `s+t=2`,

which does not satisfy `2<2`.

This is an exact limitation of the admitted lemma. It does not prove that a stronger literal-`2` simultaneous-localization theorem is impossible.

**Disposition:** `BSS_LEMMA_3_9_DOES_NOT_SUPPLY_PRIMAL_DUAL_SIMULTANEOUS_LOCALIZATION_AT_P2`.

### A3. Core-vertex connectivity uses the small-prime inequality directly

BSS II Lemma 5.15 assumes

`2s < p`

to choose one new prime that simultaneously has the required localization properties for `s` core-vertex configurations.

Corollary 5.16 then states that two core vertices of the specified type are joined by a path only under

`p>3`.

This connectivity is used in the Kolyvagin-system control argument.

**Disposition:** `CORE_VERTEX_CONNECTIVITY_PROVED_ONLY_WITH_P_GT_3_IN_THIS_INTERFACE`.

### A4. The rank-one/freeness control theorem

BSS II Theorem 5.20 assumes Hypotheses 3.2, 3.3 and 4.2 and explicitly assumes

`p>3`.

It proves that projection of the Kolyvagin-system module to a core vertex is an isomorphism and, in particular, that the Kolyvagin-system module is free of rank one.

Its proof uses the core-vertex connectivity developed immediately beforehand. It also uses Lemma 3.9 in the injectivity argument to choose primes where primal and dual localization conditions are simultaneously nonzero.

Thus the free-rank-one control needed to convert Kolyvagin systems into sharp Fitting information is not presently proved at literal `p=2` by this source.

**Disposition:** `MISSING_LITERAL_P2_BSS_CORE_VERTEX_KOLYVAGIN_CONTROL`.

### A5. The Fitting theorem inherits the same restriction

BSS II Theorem 5.2 explicitly assumes `p>3`. It proves:

- the regulator map is an isomorphism;
- the Kolyvagin-system module is free rank one;
- images of Kolyvagin-system components lie in the relevant zeroth Fitting ideals;
- under the stated basis/principal hypotheses, the containments become equalities.

The proof is built on the core-vertex/Kolyvagin-system control developed in §5.4, including Theorem 5.20.

The integral inverse-limit theorem, Theorem 5.25, is a consequence of Theorem 5.2 and retains its small-prime restriction in the source interface used downstream.

Corollary 6.15, which is the Euler-system-to-Fitting consequence, again explicitly assumes `p>3` and cites Theorem 5.2.

**Disposition:** `P_GT_3_ENTERS_THE_ACTUAL_FITTING_CONTROL_CHAIN`.

### A6. The source itself identifies the Chebotarev condition as the small-prime issue

BSS II Remark 6.19 explains that exclusion of `p=3` in the preceding results comes from the technical condition on `p` in Lemma 3.9. It notes that `p=3` can be treated under a non-self-duality hypothesis by using the corresponding Mazur–Rubin localization result.

This confirms that the simultaneous-localization/core-vertex mechanism, rather than a mere notational convention, is part of the small-prime dependency.

The remark does not provide a `p=2` replacement.

**Disposition:** `SOURCE_IDENTIFIES_LOCALIZATION_LEMMA_AS_SMALL_PRIME_DEPENDENCY`.

## Source B — BSS III: elliptic application and standard hypotheses

### B1. Standing prime convention

BSS III §3.1 states:

`Throughout this section we assume that p is odd.`

Its general Theorem 3.6 is therefore not a literal-`p=2` theorem as stated in the article.

The proof of Theorem 3.6 imports BSS II Theorems 5.25 and 6.12 and the corresponding corollaries. In particular, its Fitting assertions use the BSS II Kolyvagin-system/Fitting-control chain described above.

**Disposition:** `BSS_III_GENERAL_APPLICATION_FRAMEWORK_ASSUMES_ODD_P`.

### B2. Elliptic Theorem 6.11 is in a `p>3` subsection

BSS III §6.4 states that throughout the subsection

`K=Q and p>3`.

Theorem 6.11 is stated inside this subsection. It obtains higher Fitting containment for the strict `p`-Selmer group by applying Theorem 3.6 after verifying its standard hypotheses.

Hence Theorem 6.11 is not a literal-`p=2` finite-level Fitting theorem.

**Disposition:** `ELLIPTIC_FITTING_APPLICATION_IS_STATED_ONLY_FOR_P_GT_3`.

### B3. Exact H2/H3 verification and its use of `p>3`

The standard hypotheses in BSS III include:

- `(H1)` residual irreducibility;
- `(H2)` existence of `tau in G_{F_{p-infinity}}` such that `T/(tau-1)T` is free rank one;
- `(H3)` vanishing of two specified first Galois cohomology groups over `F(T)_{p-infinity}`.

Lemma 6.17 proves, for the elliptic application, that if the full `p`-adic Galois image contains `SL_2(Z_p)`, then `(H1)`, `(H2)` and `(H3)` hold.

The proof of `(H2)` uses the Weil pairing and then explicitly uses

`p>3`

to assert that `SL_2(Z_p)` is perfect. Because the extension `F_{p-infinity}/K(mu_{p-infinity})` is abelian, perfectness is used to keep the restricted image equal to the full `SL_2(Z_p)`. A unipotent matrix is then chosen to supply `tau`.

The proof of `(H3)` uses the same restricted-image identification together with vanishing of the relevant first cohomology group.

Thus the source proof that full large image implies `(H2)` and `(H3)` is itself small-prime-sensitive.

**Disposition:** `MISSING_LITERAL_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

### B4. Protected residual surjectivity is not the source hypothesis

The protected selected BSD-R2-A1 class supplies surjectivity of the residual representation

`G_Q -> GL_2(F_2)`.

BSS III Lemma 6.17 assumes instead that the **full `p`-adic image** contains

`SL_2(Z_p)`

and then uses an additional perfectness argument after restriction to `G_{F_{p-infinity}}`.

The protected selected hypotheses and the source interfaces audited here do not supply a theorem upgrading residual surjectivity at `2` to the exact `(H2)` and `(H3)` conditions required by the BSS framework.

This is an implication-boundary statement only. It does not assert that `(H2)` or `(H3)` fail for every selected curve.

**Disposition:** `SELECTED_RESIDUAL_SURJECTIVITY_DOES_NOT_DISCHARGE_BSS_H2_H3_FROM_CURRENT_INTERFACES`.

## Exact proof-mechanism split

The finite-level R5 candidate therefore has **two distinct literal-`p=2` proof obligations** before it can yield the protected Fitting divisibility:

### F1 — foundational Kolyvagin/Fitting control

`MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`

A successful replacement must provide enough literal-`2` simultaneous localization/core-vertex control to recover the part of Theorem 5.20/Theorem 5.2 needed for the integral Fitting containment, or bypass those theorems with another proof.

### F2 — elliptic standard-hypothesis verification

`MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`

A successful replacement must prove the exact BSS `(H2)` and `(H3)` conditions for the protected selected elliptic lane, or provide a theorem whose Fitting conclusion does not require them.

These obligations are logically separate: repairing the elliptic-image verification alone does not remove the `p>3` core-vertex/Fitting-control proof, and repairing core-vertex control alone does not verify the elliptic hypotheses.

## Reopening forms

The BSS-based finite-level route reopens only on at least one coherent proof package that addresses both required layers, for example:

1. **F1a:** a literal-`2` strengthening of the simultaneous-localization lemma sufficient for the core-vertex connectivity and Theorem 5.20;
2. **F1b:** a direct literal-`2` Kolyvagin-system/Fitting theorem that avoids the p>3 connectivity argument;
3. **F2a:** a selected-curve theorem proving `(H2)` and `(H3)` over `F_{2-infinity}`;
4. **F2b:** a finite-level elliptic Fitting theorem whose hypotheses are directly verified by the protected selected class and which bypasses `(H2)`/`(H3)`;
5. a completely different literal-`2` primitive Kummer/Fitting argument satisfying protected WP60E reopening form E3.

A result that fixes only one of F1 and F2 is not sufficient by itself to close R5 through this architecture.

## Provider conclusion

The main obstruction in the presently screened BSS route is not merely the existence of a formula called a Kolyvagin derivative. The source chain needed for **integral Fitting control** passes through a p>3 core-vertex/simultaneous-localization theorem, and the elliptic application separately verifies its standard Galois hypotheses by a p>3 large-image/perfectness argument.

Record the bounded combined disposition

`P2_FITTING_CONTROL_REQUIRES_NEW_CORE_VERTEX_LOCALIZATION_AND_ELLIPTIC_HYPOTHESIS_VERIFICATION`.

This source audit does not prove that either replacement is impossible.

## Claim firewall

This audit does not establish:

- failure or nonexistence of a higher Kolyvagin derivative at `p=2`;
- failure of `(H2)` or `(H3)` for every selected curve;
- a literal-`p=2` Kolyvagin-system Fitting theorem;
- the missing height-one-`(2)` Kato/Fitting divisibility;
- determinant primitivity at `(2)`;
- literature exhaustiveness;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.
