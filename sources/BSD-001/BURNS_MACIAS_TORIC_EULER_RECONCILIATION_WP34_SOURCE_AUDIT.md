# BSD-001 source audit — Burns–Macias S-truncation, finite local comparison, and the p=2 boundary

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP34-TORIC-EULER-DETERMINANT-RECONCILIATION`.
- Protected MATHFORGE baseline: `3966bccfe4c8e788f0ca978b5d62cd2e20119043`.
- Protected MATHSOLVE baseline: `e6c98a0494514d3b74924139edefc9aecd817c4d`.
- Primary source: David Burns and Daniel Macias Castillo, *On Refined Conjectures of Birch and Swinnerton-Dyer Type for Hasse-Weil-Artin L-Series*, arXiv:1909.03959v3; Memoirs AMS 297 (2024), no. 1482.
- Exact interfaces inspected: Proposition 2.8 and equations (19)–(20); §3.2.2–§3.2.3, especially the definition of `mu_v`, `mu_S`, and Conjecture 3.3; §6 opening hypotheses, §6.2 Theorem 6.5 and Remark 6.6.
- Disposition: `QUALIFIED_P2_S_TRUNCATION_AND_FINITE_COMPARISON_ORIENTATION_WITH_ODD_P_CLASSICAL_RECONCILIATION_BARRIER`.
- Claim class: source/applicability admission only; no conjecture is promoted to theorem and no p=2 specialization of an odd-prime theorem is authorized.

## Exact downstream question

Protected WP33 computes the odd bad-prime finite term that occurs in the Burns–Macias perfect-Selmer comparison:

`len_Z2 E(Q_ell)^wedge_2 = v2(ell-a_ell)+v2(c_ell)`.

The new question is not whether the valuations happen to resemble Euler factors. It is:

> What analytic truncation is paired by the source with the perfect Selmer complex, what is the exact orientation of the finite local comparison terms, and does the source itself supply a theorem reconciling these data at `p=2`?

The source gives precise answers to the first two questions and a precise negative applicability answer to the third.

## 1. Exact orientation of the finite local comparison

Proposition 2.8 compares the Nekovar-style perfect Selmer complex

`CS := SCS(A_F/k; X, X')`

with the classical `p`-adic Selmer complex `C'_Sigma`.

Equation (19) realizes `CS` as the mapping fibre of a morphism from

`C'_Sigma direct_sum X[-1] direct_sum X'[0]`

to the local point/cohomology complexes.

The resulting long exact sequence (20) is, in the relevant order,

`0 -> cok H^0(kappa_2)
   -> H^1(CS)
   -> H^1(C'_Sigma)
   -> (A^t(F_p)^wedge_p/X)
      direct_sum_{v in (S cap S_f) minus S_p} A^t(F_v)^wedge_p
      direct_sum_{v real} H^1(k_v,T_p(A^t))
   -> H^2(CS)
   -> H^2(C'_Sigma)
   -> direct_sum_{v real} H^2(k_v,T_p(A^t))`.

Thus the nonarchimedean point-completion module occurs between classical degree one and perfect-complex degree two. Its determinant/Euler contribution has a fixed orientation; it is not an unspecified finite error.

For `F=k=Q`, `p=2`, and the full local module at `2`, the quotient

`E(Q_2)^wedge_2/X`

vanishes. Protected MATHSOLVE WP32 separately proves that the specifically real-place degree-one/degree-two terms have equal length and zero net determinant valuation. Consequently the remaining finite comparison contribution at the valuation level is exactly the direct sum of the odd bad-prime modules computed in protected WP33.

## 2. The analytic side is S-truncated

In §3.2.3 the source defines

`L_S(A,psi,z)`

as the Hasse-Weil-Artin L-series truncated by removing the Euler factors at the places in `S`.

Hence, for the trivial extension and character,

`L_S(E,s) = L(E,s) * product_{v in S_f} L_v(E,s)^(-1)`

as an identity of Euler products wherever both sides are defined, and therefore by continuation at the leading term whenever the removed local factors are nonzero at `s=1`.

For a bad multiplicative prime `ell`, the standard local factor used by the protected BSD campaign is

`L_ell(E,s) = (1-a_ell ell^(-s))^(-1)`

with `a_ell=+1` for split and `a_ell=-1` for nonsplit multiplicative reduction. Therefore deleting this factor multiplies the leading term by

`1-a_ell/ell`.

Since `ell` is a `2`-adic unit,

`v2(1-a_ell/ell)=v2(ell-a_ell)`.

This last local-factor calculation is elementary and already recorded without cancellation claim in protected WP33. The source premise supplied here is the exact `S`-truncation convention.

## 3. Fontaine–Messing term does not reinsert the bad places in S

In §3.2.2 the source defines a local correction `mu_v(A_F/k)` only for places `v` outside `S`, and then sets

`mu_S(A_F/k) := sum_{v notin S} mu_v(A_F/k)`.

Conjecture 3.3(iv) places this correction beside the perfect Selmer Euler characteristic:

`boundary(L_S^*/Omega) = chi(SCS,h) + mu_S`.

Accordingly, an odd bad prime that is included in `S` contributes through the deleted Euler factor on the analytic side and through the finite local comparison structure of the perfect complex; it is not separately reintroduced by `mu_S`.

This is a statement about the source's normalization architecture. Conjecture 3.3 itself remains conjectural.

## 4. The source's classical reconciliation theorem is odd-prime only

Section 6 begins by explicitly fixing an **odd** prime `p` before listing hypotheses `(H1)`–`(H6)`.

Theorem 6.5 is proved only under that section-wide setup. It compares the `p`-component of the refined BSD equality with a determinant formula for the classical Selmer complex and a leading-term element whose L-series is truncated only at a ramification set.

Remark 6.6 gives especially clean forms when the relevant wild/unramified correction sets vanish.

None of this authorizes specializing Theorem 6.5 to `p=2`.

This point is material. The selected BSD-001 operation is explicitly a literal-`p=2` campaign. Theorem 6.5 may be used as structural motivation or as an odd-prime comparator, but not as the theorem that closes the selected p=2 reconciliation.

## 5. What is source-qualified for downstream WP34

After protected admission, downstream may use the following exact source interfaces:

1. Equation (20) fixes the orientation and position of the nonarchimedean local point-completion modules in the comparison between the perfect and classical Selmer complexes.
2. At literal `p=2`, Proposition 2.8 still gives the perfect complex and equation (20); the finite real-place terms must be retained rather than discarded.
3. `L_S` is exactly the Hasse-Weil-Artin L-series with Euler factors at `S` removed.
4. `mu_S` is supported outside `S`; it does not separately reinsert a bad prime already placed in `S`.
5. The source's later classical-complex reconciliation theorem, Theorem 6.5, is unavailable as a literal-p=2 theorem because §6 fixes `p` odd.

These clauses are sufficient for a downstream **valuation/Fitting comparison** that combines protected WP32 and WP33 with elementary determinant-line additivity. They are not sufficient to assert the full p=2 refined BSD conjecture, a canonical determinant generator, or a Bockstein/regulator identity.

## 6. Candidate downstream valuation reconciliation

The source architecture nominates the following bounded internal calculation.

At each odd bad prime, protected WP33 gives algebraic comparison length

`v2(ell-a_ell)+v2(c_ell)`.

Passing from the complete local Euler product to `L_S` shifts the analytic valuation by

`v2(ell-a_ell)`.

Thus the **difference of normalization shifts** leaves precisely

`v2(c_ell)`.

This is exactly the protected WP22 Tamagawa/control length.

The present source audit authorizes carrying out that valuation calculation downstream. It does not pre-assert the determinant-line theorem, and it does not authorize replacing equality of valuations by equality of determinant generators.

## 7. What this source does not establish

This source does not establish for the selected literal-p=2 branch:

- Theorem 6.5 at `p=2`;
- validity of Conjecture 3.3 or BSD;
- a canonical determinant-line equality between the perfect and classical p=2 Selmer complexes;
- equality of determinant generators rather than their `2`-adic valuations/Fitting exponents;
- exact identification of the Burns–Macias degree-two module with protected `X_E`;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- protected WP31 `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.

## Provider conclusion

The Burns–Macias source fixes enough normalization data to reconcile the odd-bad **valuation surplus** directly at literal `p=2`: the perfect-complex comparison contains the local point completions in a fixed orientation, while the paired analytic object deletes the corresponding Euler factors at `S`, and `mu_S` is supported away from `S`.

The paper does **not** supply the desired p=2 classical determinant theorem: §6 explicitly assumes `p` odd. Downstream must therefore prove only the bounded valuation/Fitting reconciliation from the literal-p=2 interfaces and retain all stronger determinant/Bockstein boundaries.

**Disposition:** `QUALIFIED_P2_S_TRUNCATION_AND_FINITE_COMPARISON_ORIENTATION_WITH_ODD_P_CLASSICAL_RECONCILIATION_BARRIER`.

## Claim firewall

This source admission changes no BSD or certification claim state. It authorizes a bounded p=2 valuation/Fitting normalization calculation only.