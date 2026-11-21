# RH-A26 D05 — independent error-dominance reconstruction and VWin cost decomposition

**Date:** 2026-11-21  
**Original archive:** SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc` (same archive examined in the RH-A26 #577 docket).  
**Claim level:** independent elementary analytic derivation plus original-source dependency audit. NOT independent full-Lean proof replay and NOT proof of any genuine `VVle` estimate.

## Exact VWin target

`Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean` defines `VWin := ∀ ψ : PChar, VWinAt ψ 401`. For every `eps>0` with `eps<1/52`, admissible page function, and all sufficiently large `X`, the conclusion must handle **all** prime pairs satisfying `WinPair`, find `Y` in the specified growth window, and establish `VVle E ⌊x^401⌋₊ (sqrt(exp(x^eps)))` for **every** number field `E` with `IsChiField`, every algebraic closure `Ω`, and **every** choice of compatible `LData` over all primes.

The `VVle` definition uses actual `Module.length ℤ_[l] (Sha D e)`, finite for every relevant `l,e`, and a universal finite-subset prime-weighted sum
```text
sum_{l in S} log(l) * sum_{1≤e<t} length(Sha(ld[l],e)) ≤ B.
```
`LData` consists of a specific prime-place set, valuation data and a character restricting to the cyclotomic character; it is not an arbitrary table of nonnegative integers. The cost cannot be tested on fictitious LData by inventing group lengths.

## Identified exact proof chain

The original `WindowBoundOfLiteratureLevel.lean` proves `VWin` via:
```text
LiteratureRankNHypothesis
 -> HypothesesH'
 -> LemmaK, CountI, CountII, CountIII, CountV, CountZ
 -> PointHV -> ThmHV
 + PoitouTateDuality, LocalFinitenessK, LocalTateDualityK
 + ThmBab(401) via TowerBound and FerreroWashington
 + ThmBcFree
 -> JointWin(401) + ThmBc(401)
 -> vwin_of_joint -> VWin
```
Located original files include:
- `.../DenseThresholdCases/WindowBoundOfLiteratureLevel.lean`, SHA-256 `576e18ba083451bcffe9e94075dc8d22ccfa6995fa8d30d68ea108b1cc910cf0`.
- `.../DenseThresholdCases/HVCore.lean`, SHA-256 `695927bf54a16053ae211e0d1f7ad26217806520d60f884459f9c0d7aac1460d`.
- `.../HeightAndVanishing/JointWinOfCounts.lean`, SHA-256 `3c71cf0dabc617e3d1ab9fc04939c311e4242912407cdfbc71c8e0764563d558`.
- `.../HeightAndVanishing/Counts.lean`, SHA-256 `cc00a1a2e38f8dc5a87a0cc5d79ab8100db8c59255d62be12c95931262fc53c2`.
- `.../HeightAndVanishing/LayerLe.lean`, SHA-256 `248298d006f0013fa87fbee49075d6b750bba77eb403d7b34aeca70feb141e07`.
- `.../PrimeSetBoundDataOfPrimitiveChar.lean`: `ThmBcFree` uniformly bounds minus-eigenspace cohomological lengths; `ThmHV` bounds plus-eigenspace lengths using an explicit conductor factor and `exp(x^(4 eps/5))`; `JointWin` joins the window and plus-length estimate.
- `.../LengthEqAddEigen.lean`: `shaLen_eq_add` decomposes the odd-prime `Sha` length into plus/minus components; `vvle_of_parts` combines the 2-primary, plus, and minus costs, giving `B₂ log 2 + Bm + Bp`.
- `.../CMFieldExponentialBounds/ConductorBoundsOfIsChiField.lean`: conditional source theorem asserts `1 ≤ condF E ≤ 2^(e+2) ψ.N q d` and `[E:Q] ≤ condF E`.
- `.../CMFieldExponentialBounds/minusle.lean`: source bounds the explicit `minusBound` by `K exp(8W)` assuming `log(Nt) ≤ 2W`.
- `.../CMFieldExponentialBounds/AdmissibleOfPageN.lean`: uses conductor growth and error-dominance lemmas to turn these conditional bounds into `VWin`.

## An independently proved conditional error-dominance inequality

The standalone elementary analytic claim in original `ErrorTermsLeSqrtExpRpow.lean` (SHA-256 `1725fcaea1649db68c3876803ae79e3140ac464dbbe9b04be77cf47b51ecdc59`) states the following for any real `K,C` and `eps>0`:

For `x≥x0`, `u≥1`, and `log u ≤ 2 x^(eps/4)`,
```math
e^{x^{4\varepsilon/5}}\log 2
+K e^{8x^{\varepsilon/4}}
+(u^C+C e^{x^{4\varepsilon/5}})
\le \sqrt{e^{x^\varepsilon}}.
```

**Independent proof (not relying on the original Lean proof).** Put
```math
a=x^{\varepsilon/4},\qquad
b=x^{4\varepsilon/5},\qquad
s=x^{\varepsilon/5},\qquad
N=\log2+|C|+|K|+1,\qquad
D=9+2|C|.
```
For `x≥1`, `1≤a≤b`, `b≥1`, and `x^eps=bs`. The logarithm hypothesis and `u≥1` imply
```math
u^C=\exp(C\log u)\le \exp(2|C|a)\le e^{Db}.
```
The other three terms are respectively bounded above by `(log 2)e^(Db)`, `|K|e^(Db)`, and `|C|e^(Db)`, because `D≥9` and `a≤b`. Therefore the entire left side is at most `Ne^(Db)`.

Now choose
```math
x_0=\max\{1,\,[2(D+\log N+1)]^{5/\varepsilon}\}.
```
Then `s≥2(D+log N+1)`, and (since `b≥1` and `log N≥0`)
```math
Db+\log N\le b(D+\log N+1)\le bs/2=x^\varepsilon/2.
```
Exponentiate to obtain `Ne^(Db)≤e^(x^eps/2)`, which is exactly the target ceiling. This argument is valid for *all real* `K,C`, including negative values. No genuine cohomological bound was used.

### Bounded independent numerical regression

A separate Python standard-library, log-domain smoke test at `eps=0.01, K=2, C=5` uses `r=x^(eps/5)`; the sufficient `r` gate is `44.325070069763854`. With the worst permitted `log u=2x^(eps/4)`, the calculated log margin `log(RHS)-log(LHS)` is negative at `r=2` (-7.803509) and positive at `r=45` (+88,163,435.760737) and `r=48` (+122,093,566.260737). CHAD execution capture: `235f075a697d41f1b0d47ce53ec33f26`. Regression source is committed as `tests/rh_a26_error_dominance_smoke.py`. These spot checks corroborate—but cannot replace—the analytic proof above.

## Substantive boundary of this result

**Discharged by independent mathematical argument here:** the last pure real-analysis growth/error-dominance inequality, conditional on the explicit conductor/logarithmic premises. The matching original Lean proof has NOT been recompiled locally.

**Not discharged:** actual `ThmBcFree` and `ThmHV` estimates for nonempty genuine `LData` and `IsChiField` families, the 2-primary `B₂` estimate, universal prime-sum budget, construction of an admissible `WinPair`/family (to exclude vacuous use), and noncircularity of `LiteratureRankNHypothesis` and the five counting claims.

Therefore this tranche shows the exponent bookkeeping *can* close once the mathematical arithmetic estimates are true; it does not show those estimates are true. It is not evidence that RH or Dirichlet GRH is proved.

**Disposition:** `RH-A26-D05_ERROR_DOMINANCE_INDEPENDENTLY_PROVED__GENUINE_SHA_LENGTH_BOUNDS_AND_NONVACUITY_OPEN`.
