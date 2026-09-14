# BSD-001 source screen — literal-p=2 Heegner-index / twist-L-ratio residual after WP58A

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP59-RESIDUAL-SOURCE-BARRIER`.
- Protected MATHFORGE predecessor: `d588543151ddb458d627ac9b9fb37ec57cd90780`.
- Protected MATHSOLVE anchor: `55434c50ae05c3bdb66f329ee15d4ece4534d4fd`.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Disposition: `QUALIFIED_NO_CURRENT_ADMITTED_LITERAL_P2_RESIDUAL_CLOSURE`.
- Claim class: bounded source/applicability screen only; not a mathematical impossibility theorem and not a literature-exhaustiveness claim.

## Exact downstream residual

Protected MATHSOLVE WP58A fixes an explicit source-compatible optimal-composite parametrization and proves

`delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`,

where

`lambda_D := L(E^D,1)/Omega(E^D) in Q^x`.

The modular-differential scalar has already been removed from the `2`-adic valuation by the protected theorem `ord_2(C_f)=0`. The substantive D2d source question is therefore whether currently available admissible theorems determine either

1. `ord_2(m_K(f))`, or
2. `ord_2(lambda_D)`,

uniformly for the protected selected class and the WP09 auxiliary-field constraints:

- `D_K<0` fundamental;
- `(D_K,2N)=1`;
- `2` splits in `K`;
- every `ell|N` splits in `K`;
- `L(E^D,1) != 0`.

A combined theorem determining the required sum of the two residual valuations would also suffice. A theorem only after inverting `2`, only up to a `2`-adic unit, or conditional on an additional hypothesis not proved for the selected class does not close the residual.

## Screen A — Kato cyclotomic main-conjecture route

Protected MATHFORGE audit `KATO_P2_HEIGHT_ONE_WP17B_SOURCE_AUDIT.md` already establishes the exact boundary from Kato's 2004 primary source.

At `p=2`, Kato controls ordinary characteristic/Fitting information away from the height-one prime containing `2`. The integral clauses that extend the divisibility to every height-one prime explicitly require `p != 2`.

Therefore Kato's original theorem does not determine the missing literal height-one-`(2)` exponent and cannot be used as a one-sided integral inequality that forces the WP59 residual valuations.

**Disposition:** `DOES_NOT_CLOSE_LITERAL_P2_HEIGHT_ONE_2`.

## Screen B — standard Heegner-point main-conjecture / primitivity route

Protected MATHSOLVE WP10 and its admitted source interface already establish that the screened standard odd-prime chain cannot be specialized mechanically to `p=2`.

Burungale–Castella–Kim's Heegner-point main-conjecture/primitivity setup uses `p>3`. Modern good-ordinary extensions such as Yan–Zhu, *Main conjectures for non-CM elliptic curves at good ordinary primes*, Journal of Algebra 693 (2026), likewise formulate the elliptic-curve theory for an odd prime `p` (the arXiv version states `p>2`).

Recent p-converse extensions screened in this continuation also retain odd-prime hypotheses; for example Castella's exceptional-zero p-converse theorem assumes `p>3`, and the potentially-good-ordinary Eisenstein-prime formulations screened assume `p>2`.

**Disposition:** `ODD_PRIME_ONLY_FOR_CURRENT_UNIFORM_MAIN_CONJECTURE_LANE`.

## Screen C — Kriz–Li literal-p=2 Heegner congruences

Daniel Kriz and Chao Li, *Goldfeld's conjecture and congruences between Heegner points*, Forum of Mathematics, Sigma 7 (2019), provide a genuine literal-`p=2` mechanism.

For an elliptic curve with `E(Q)[2]=0`, their relevant rank-one/twist results require an imaginary quadratic field satisfying the Heegner hypothesis together with their additional Assumption `(star)`, a nonvanishing condition modulo `2` on the normalized `2`-adic logarithm of the Heegner point. Under this assumption and the stated local hypotheses, their Lemma 5.4/Section 5 mechanism gives `2`-indivisibility of the Heegner point and supports the `2`-part BSD propagation statements in Theorem 1.12.

This is highly relevant but does not close the selected class uniformly:

- Assumption `(star)` is an additional arithmetic hypothesis;
- it is not one of the protected BSD-R2-A1 hypotheses;
- no admitted theorem currently proves that a WP09 auxiliary field satisfying all prescribed splitting and nonvanishing conditions can always be chosen so that `(star)` also holds;
- the theorem propagating BSD(2) over `Q` assumes BSD(2) for seed curves and therefore cannot be used as a uniform proof of the selected target without circularity.

Protected WP36 computes a finite local norm-membership invariant for the saturated rational generator, but it does not identify that invariant with the Kriz–Li mod-`2` Heegner logarithm condition and therefore does not discharge `(star)`.

**Disposition:** `LITERAL_P2_BUT_EXTRA_HEEGNER_LOG_HYPOTHESIS_NOT_UNIFORMLY_DISCHARGED`.

## Screen D — exact 2-adic central-value results for quadratic twists

### Zhai

Shuai Zhai, *The Birch--Swinnerton-Dyer exact formula for quadratic twists of elliptic curves* (published online 2025; arXiv:2102.11798), proves a general lower bound for the `2`-adic valuation of algebraic central values and exact BSD(2) results for explicit twist families under additional seed hypotheses.

The general theorem is a lower bound, not an exact valuation. The exact-family mechanisms screened require an appropriate rank-zero/nonzero central-value seed and do not yield, from the selected rank-one base hypotheses alone, the exact value of

`ord_2(L(E^D,1)/Omega(E^D))`

for a WP09 field with all primes in `2N` prescribed to split.

**Disposition:** `LOWER_BOUND_OR_SEEDED_FAMILY_ONLY`.

### Adachi–Nomoto–Shii

Taiga Adachi, Keiichiro Nomoto, Ryota Shii, *The 2-adic valuations of the algebraic central L-values for quadratic twists of weight 2 newforms*, Acta Arithmetica 222 (2026), 197–218, prove sharp lower bounds and exact valuations for infinitely many twists under their explicit hypotheses.

The candidate was screened specifically in the odd negative discriminant case relevant to `2` splitting. In the zero-new-prime seed case, the exact-equality condition is controlled by the `2`-adic valuation of the untwisted algebraic central value. For the selected curve `L(E,1)=0` because the analytic rank is one, so this is not a finite rank-zero seed and does not furnish the required exact WP09 twist value. The paper therefore gives strong family information but not the required uniform residual closure from the selected hypotheses.

**Disposition:** `EXACT_FAMILIES_REQUIRE_INAPPLICABLE_CENTRAL_VALUE_SEED_FOR_THIS_LANE`.

### Earlier modular-symbol twist propagation

Ono–Papanikolas and related modular-symbol nonvanishing theorems provide large sets of nonvanishing quadratic twists when the mod-`2` representation has suitable nontrivial traces. These theorems are valuable for constructing rank-zero twists but do not, in the screened form, determine the exact `2`-adic valuation of the WP00 whole-real-period quotient while simultaneously imposing the protected all-`2N`-split local conditions.

**Disposition:** `NONVANISHING_NOT_EXACT_WP00_VALUATION`.

## Screen E — small-prime / special-family theorems

There are literal-`2` exact BSD or Heegner-divisibility theorems for special CM curves, congruent-number curves, curves with rational `2`-torsion, and other tightly specified families. These hypotheses are not consequences of the protected selected class, whose mod-`2` representation is irreducible and whose only global hypotheses are semistability, odd conductor, good ordinary reduction at `2`, irreducible `E[2]`, and analytic rank one.

Such family theorems therefore cannot be promoted to the selected uniform target.

**Disposition:** `SPECIAL_FAMILY_ONLY`.

## Screen F — unreviewed claims that conflict with protected primary-source boundaries

A 2026 independent manuscript surfaced in search claiming a good-ordinary `p=2` main conjecture and advertising a proof whose first integral divisibility step attributes an all-height-one `p=2` conclusion to Kato's 2004 theorems.

Protected WP17B checked the Kato primary source theorem-by-theorem and records that the decisive integral clauses covering the height-one prime containing `2` explicitly require `p != 2`. The surfaced manuscript was not admitted as authority; its claimed first step would require an independent proof repairing precisely the protected Kato boundary, not a restatement of Kato's theorem.

**Disposition:** `NOT_ADMITTED; PRIMARY_SOURCE_CONFLICT_REQUIRES_INDEPENDENT_PROOF`.

## Combined-route assessment

A combined theorem could close D2d without evaluating `m_K(f)` and `lambda_D` separately. The most promising literal-`2` mechanism located is the Kriz–Li mod-`2` Heegner-log route. However, its additional logarithmic nonvanishing hypothesis is not currently a theorem of the protected selected class or of the WP09 auxiliary-field construction.

Conversely, the modern exact twist-L-value papers located either provide lower bounds or propagate exact valuations from a rank-zero/nonzero central-value seed. The selected base curve has analytic rank one, so `L(E,1)=0`; that seed cannot be supplied by the base curve.

Thus the current admitted source interfaces do not produce the required uniform exact equality.

## Exact source boundary after this screen

The bounded source boundary is

`MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.

Equivalent closure forms include any one of:

1. a literal-`p=2` theorem proving the required Heegner-index valuation for every selected curve and a WP09-compatible auxiliary field;
2. an exact theorem for `ord_2(lambda_D)` that permits the WP09 simultaneous splitting constraints and does not require an unavailable rank-zero seed;
3. a theorem proving that one may always choose the WP09 field so that the Kriz–Li mod-`2` Heegner-log condition holds, together with the exact normalization comparison needed downstream;
4. a direct combined theorem determining
   `2 ord_2(m_K(f)) - ord_2(lambda_D)`
   in the protected normalization;
5. a new literal-`p=2` integral main-conjecture/reciprocity theorem that genuinely controls the height-one prime `(2)` and specializes to the protected finite primitive determinant line.

## Non-exhaustiveness and reopening rule

This screen does not claim that no such theorem exists or can be proved. It records the failure of the specific reasonably available source routes screened through September 2026.

Reopen the source lane immediately if a candidate supplies one of the five closure forms above at literal `p=2`. Do not reopen merely because a theorem says `p` is ordinary while its standing assumptions later impose `p>2`, because it proves only nonvanishing, or because it gives equality only after inverting `2`.

## Provider disposition

`QUALIFIED_NO_CURRENT_ADMITTED_LITERAL_P2_RESIDUAL_CLOSURE`

No BSD claim, MATHCERT certification, novelty, or priority is promoted by this screen.
