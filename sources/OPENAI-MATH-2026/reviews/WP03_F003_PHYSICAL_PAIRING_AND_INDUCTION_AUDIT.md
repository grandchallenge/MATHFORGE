# OAI-26 Family 003 — independent high-stage left/right column pairing and induction handoff audit

**Assignment:** `GCL-OAI26-F003-PHYSICAL-COLUMN-PAIRING-AND-INDUCTION/1`  
**Upstream lock:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Independent exact-rational adversary:** [f003_high_physical_pairing_rational_adversary.py](f003_high_physical_pairing_rational_adversary.py)  
**Scientific verdict:** `F003_PHYSICAL_PAIRING_16_AND_CONDUCTOR_CANCEL_PASS__SCHEDULE_TERMINAL_PLATEAU_PROVED__ORIGINAL_MAIN_ERROR_CHILD_COLUMN_ESTIMATES_OPEN`.

## 1. Audit scope and mathematical mechanism

The previous [PR #572](https://github.com/grandchallenge/MATHFORGE/pull/572) checked Gaussian-theta FE normalization on all nonprincipal ray characters modulo 5 and derived the natural high-stage slot-capacity restriction. This pass reopens the **actual pinned source** for the two left/right physical source-column bounds and their aggregation, rather than treating their theorem names as evidence.

Core theorem dependency:

```text
Energy/CappedAnalyticSuccessor.actual_successor
  -> Energy/NaturalHighStage.actual_high_stage
    -> Energy/PositiveHighPhysical.actual_positive_high_physical
      -> Energy/CanonicalHighPhysical.actual_high_physical
        -> Energy/CanonicalHighSource.actual_original_left_high_column
        -> Energy/CanonicalRightSourceColumn.actual_original_right_high_column
        -> Moments/FirstReferenceEnergy.actual_physical_mass
          -> Moments/FirstReferenceBlock.actual_reference_block
          -> Moments/FirstReferenceSource.original_block_sum
```

The two source columns both invoke `Energy/CanonicalHighColumn.actual_admitted_subsets_high_column`, which invokes `Energy/CanonicalAnnularPower.actual_original_subsets_annular_power`, which invokes `Energy/CanonicalAmplifiedUniform.actual_original_subsets_amplified_power`. That splits into **two substantive lower estimates**, `Energy/CanonicalMainSubsets.actual_original_subsets_main_power` and `Energy/CanonicalErrorSubsets.actual_original_subsets_error_power`. Those estimates accept *previously supplied* `ZeroAt` and `PositiveAt` child obligations. Their independent analytic soundness for the natural source remains unverified. In particular this tranche must not be described as an independent proof of the high-stage theorem.

## 2. Why 16 appears: four left times four right

In `Moments/FirstReferenceEnergy.lean` the paired budget is

```text
pairedBudget(JL,JR,t,EL,ER)
 = sum_{i=0}^{3} sum_{j=0}^{3}
     windowBudget(JL,t,EL[i]) * windowBudget(JR,t,ER[j]).
```

Each `windowBudget` is a square-root energy times nonnegative polynomial height/profile factors. If `0<=EL[i],ER[j]<=H`, then

`√EL[i] * √ER[j] <= H`

for each of the **16** pairs, whence

`pairedBudget <= 16 H * heightEnvelope(t)^(JL+JR) * profileMoment(JL)*profileMoment(JR).`

This inequality is **sharp as algebra**: taking all eight input energies equal to `H>0` gives all 16 pair products equal to `H`. The standalone exact arithmetic adversary enumerates every `4^8=65,536` choice of eight perfect-square energies in `{0,1,4,9}` under `H=9`, checks the bound, and explicitly rejects the hostile replacement 16→15.

This is where Cauchy–Schwarz is paid, without inventing an unaccounted `4^4` or square of the source exponents. The analytic assertion that *actual* left and right energy terms respect `EL,ER` is **upstream of this algebra**.

## 3. Conductor cancellation: the crucial exact exponent identity

The source defines

`sourceFactor = [exp(log 4)/((prod_i lower_i)*a1*a2)] * fixedPresentationCost * K * N(modulus).`

Put `q=N(modulus)>0`, `P=(prod lower_i)*a1*a2`, assume `P>=P_lower>0` and `Z>1,K>0`. Each left/right energy is bounded by

`F Z^(Mdecl-log_Z(K)-log_Z(q)+ell)`.

Multiplying by `sourceFactor` cancels `Kq` **exactly**:

```text
 K*q * Z^(Mdecl-log_Z(K)-log_Z(q)+ell) = Z^(Mdecl+ell).
```

Thus, with the factor 16 from §2,

`sourceFactor * pairedBudget <= [64*fixedPresentationCost/P_lower] * F * Z^(Mdecl+ell) * polynomialHeightProfileFactors.`

No hidden conductor power remains at this interface. The loss estimate does **not** prove a universal result independent of conductor in later source-column inputs: the column constant `F` and threshold `Z0` can depend on the character and admissible ideal.

The exact `Fraction` adversary covers **1,296** choices of `Mdecl,ell,log_Z K,log_Z q,P,P_lower,fixedPresentationCost`, including negative powers, and verifies equality at the support-floor boundary and monotonicity otherwise.

## 4. Converting individual columns into physical mass

`Energy/CanonicalHighPhysical.actual_high_physical` first obtains left/right seminorm indices `UL,UR` and degrees `JL,JR`, then folds across every finite subset `T ⊆ α` using the positive constant `Cmass=1+Σ_T Cp(T)`. The common index set is `UL ∪ UR`, and the combined height exponent is **`2*(JL+JR)`**, because the two factors

```text
(1+height)^(JL+JR) * (1+|t|)^(JL+JR)
```

are bounded by

`(1+|t|+height)^(2*(JL+JR))`.

Let `C0,C1>=0`, `P_union>=P_L,P_R>=0`. For nonnegative column constants `CL,CR`, define

```text
 FL = CL*(C0+C1+1)*P_L^2*(1+height)^JL
 FR = CR*(C0+C1+1)*P_R^2*(1+height)^JR
 Fcap=(CL+CR)*(C0+C1+1)*P_union^2*(1+height)^(JL+JR).
```

Then `FL<=Fcap` and `FR<=Fcap`. For four exponents `powers[j]` and source base loss `base`, the source's explicit prerequisite `powers[j]+base<=ell` yields for each `j`

`(F*Z^(deficit+base))*Z^(powers[j])<=Fcap*Z^(deficit+ell)`.

Finally the physical-mass lemma absorbs the 16-pair contribution into its prefactor. In the source, one valid constant is

`Cm=Cmass*(CL+CR)*(1+profileMoment(JL))*(1+profileMoment(JR))`.

Since `Cp(T)<=Cmass` and the profile moments are nonnegative, it dominates the required product. The exact-rational adversary checked **1,296** varied choices of left/right indices, height, source time, constants and seminorm caps, plus four-power exponent cases.

**Uniformity alert:** `Cmass` aggregates over `Finset.univ : Finset (Finset α)`, potentially `2^|α|` terms. It is independent of `η0,Q` at this selection stage because `Cp(T)` is selected before them. However **`CL,CR` and the final `Cm` are selected after `η0,Q`**. The theorem has a uniform polynomial degree and finite seminorm set, not a single numerical physical-energy constant uniform over every possible character and ideal. Downstream applications must preserve that quantifier order.

## 5. Induction: no logical cycle from the terminal width plateau, but no strict width gain there

The source constructs, for positive `M=Mcap`, `a=amplification ε` and `0<r=reserve<=a/100`,

```text
depth = ceil(2*M/a)+1,
rawWidth(k)=r/16+k*a/2,
bandWidth(k)=min(M,rawWidth(k)).
```

For *all such parameters* at `k=depth-1=ceil(2*M/a)`,

```text
bandWidth(depth-1) = M = bandWidth(depth).
```

The last successor therefore **does not increase width**. This is mathematically important for explaining what induction establishes. Nevertheless, `CertifiedBand(k)` and `CertifiedBand(k+1)` are **different propositions with different stage index and error/length budgets**, so the passage is not formally circular merely because their widths coincide.

For the actual final detector ceiling `M=2, t=10^-8, ε=t/4, a=t/64000`,

```text
depth = 25,600,000,000,001,
bandWidth(25,600,000,000,000)=2,
bandWidth(25,600,000,000,001)=2.
```

At the immediately preceding stage `depth−2`, the band width is still **strictly below** 2 because `r/16<a/1600<a/2`.

The exact-rational adversary tests three reserve choices and 2,913 smaller-stage predecessor relationships, verifying

`bandWidth(k+1)-a/2 <= bandWidth(k) <= bandWidth(k+1)`

even at saturation, and rejecting the hostile assertion that the last stage strictly increases width.

The critical source handoff is visible in `Energy/CappedAnalyticSuccessor.actual_successor`: it obtains `hold : CertifiedBand k`, chooses `Mc=bandWidth(k)`, `Mp=bandWidth(k+1)`, and passes the previous **`ZeroAt` and `PositiveAt` bounds from `hold`** into `Energy/NaturalHighStage.actual_high_stage`. The latter uses `Mp-a/2<=Mc`. The dependency is explicitly earlier-stage, not an assumption that `CertifiedBand(k+1)` already holds. This source-level handoff passes the *narrow* noncircularity check. Full semantic validation still requires checking the lower-level child analytical estimates, not merely the theorem-index graph.

## 6. The actual remaining high-stage analytic obligations

The left and right column estimates are not identical copy-pastes: the left branch uses `fixedPair.left` and `seed0 | C`; the right branch uses `fixedPair.right`, `seed0 | D` and the `swapSubset(C,D,E)` conductor identity. Both constrain the character modulus to an explicit product of the source modulus, fixed-bad mask, `(72)`, and an active prime-subset conductor.

Both branches construct nonzero amplifier prime pools, ensure coprimality of new primes with active old slots, and split errors into either a **coefficient-zero case** or a **ready child error-input case**. That is a genuine structural distinction, not the same proof renamed.

The **next unverified substantive** mathematical claims are

- `Energy/CanonicalMainSubsets.actual_original_subsets_main_power`: the claimed normalized Gauss-source upper bound from ready positive/zero child inputs;
- `Energy/CanonicalErrorSubsets.actual_original_subsets_error_power`: corresponding amplified-prime error-source bound, including the special exponents **1, 6, 7** after the `errorIndex(k+1)` conversion;
- `Moments/FirstReferenceBlock.actual_reference_block`: the harmonic/divisor estimate transferring two column common energies into an absolute block norm, then the inactive radical mass and dyadic block count in `Moments/FirstReferenceSource.original_block_sum`.

These are **not independently proved by this tranche**; all we have established independently here are the exact algebraic downstream pairings, loss accounting, quantifier and induction handoff.

## 7. Pinned source ledger and evidence

| Pinned source module | Git blob |
| --- | --- |
| `Energy/CanonicalHighSource.lean` | `8d4bc5f0c5143f4778cada5c215ee8c09ca8d1bc` |
| `Energy/CanonicalRightSourceColumn.lean` | `0127493078161b4dda3bac4f0711094418f0ce86` |
| `Energy/CanonicalHighColumn.lean` | `5e29e01a499e886c5e39baa7d1fbbfad07189e24` |
| `Energy/CanonicalAnnularPower.lean` | `a6cd098e140d544b9c6518edb58d5bad506b5640` |
| `Energy/CanonicalAmplifiedUniform.lean` | `37b988def660b5eada3610597776b1b9ce4c2918` |
| `Energy/CanonicalMainSubsets.lean` | `e98464391b540da12d04de95cbbb1ac08420f61b` |
| `Energy/CanonicalErrorSubsets.lean` | `328800ca5c93d49e0075bf3a3ff8f4b865f57ce8` |
| `Energy/CanonicalHighPhysical.lean` | `a07dd29bcf9bb1b88eb1a522a0f369de4a86759f` |
| `Moments/FirstReferenceEnergy.lean` | `44dce14ed3a053bfde4314cdd7877e09faf36fdc` |
| `Moments/FirstReferenceBlock.lean` | `539dcb7d07e6be298e55aac0329b216fdd8253b3` |
| `Moments/FirstReferenceSource.lean` | `fd6a83dbfd4f746917b646cc0c84a1ada8520fa6` |
| `Energy/FirstPhysicalNormalization.lean` | `bb47eb533057aec3954bef6ee633d77a15925486` |
| `Energy/CappedAnalyticSuccessor.lean` | `e48d2c10a65012a44b1525fa5231921ad1120566` |
| `Moments/FirstSecondLossParameters.lean` | `a758177710ebf2f266fbe3aed47d1ff535b9b2e2` |

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-PHYSICAL-COLUMN-PAIRING-AND-INDUCTION/1
SOURCE: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
STATUS: PHYSICAL_PAIRING_AND_CONDUCTOR_CANCELLATION_INDEPENDENT_PASS__LAST_WIDTH_STAGE_PLATEAU_EXPLAINED__SUBSTANTIVE_MAIN_ERROR_SOURCE_ESTIMATES_OPEN
EXACT_TESTS: 65536 four-by-four pairings; 1296 conductor/exponent cases; 1296 height/constant cases; 2913 induction predecessor cases; hostile 15-factor and strict terminal gain rejected
BOUNDARY: no new general Hecke theorem or global natural high-stage theorem proven independently; no seven-eighths certification; Family003 UNRESOLVED, NO MATHCERT.
```
