# RH-A26 D05 — Theta-lift and automorphic bridge, source-level reconstruction

**Date:** 2026-11-21  
**Claim scope:** original-source statement/hypothesis reconstruction, not full Lean replay or mathematical certification.  
**Upstream original:** Alpöge–Claude 14-part assembled archive, SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`. Local CHAD immutable-intent source custody `~/.local/share/gcl/source-intake/RH-A26-2026-11-20/unpacked/lean/src/`.

## A. Theta-lift source identity and quantifiers

- `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/TLiftK.lean`, SHA-256 `cb810adcf09297fdd356174b67d6abdc43c079dbe65797b1f47383871c1bf6ca`: `UpperTheory.TP.K.tLiftK : UpperTheory.TP.TLiftK := UpperTheory.TP.tLift_holds_k`.
- `.../ThetaParseval/HalfIndexLattices/TLiftK.lean`, SHA-256 `8a58c624cd91dbfb4d3e8b7735e232e1463dd51d0daa7a6174b99349b31d6fc5`: defines `TLiftK : Prop`.
- `.../ThetaParseval/ThetaKernels/GalTPDefs.lean`, SHA-256 `47f54c0dac340626f9b602eb4ad10e27543f496e61f995b71f55ce205642a20c`: defines `TLift_k : Prop` and the 14-field `Tools_k` structure.
- A bounded source-text check normalized whitespace and the fully qualified `GoodK` predicate name. The two proposition bodies `TLiftK` / `TLift_k` were **exactly equal** (1,132 characters each); CHAD receipt `8e410f6b4ab04ccc97d997735bd97631`. This is source-text agreement, **not** fresh proof-kernel definitional equality.
- The proposition quantifies over CM fields and base data satisfying `GoodK`, ranks `n≥1`, sufficiently large `d`, prescribed hermitian and skew-hermitian spaces, compatible Hecke characters and archimedean weights, and automorphic representation submodules. It concludes existence of `U'` satisfying `IsLift`, itself a structure carrying automorphicity, weight lifting, and local matching. **Nonvacuity** of the parameter domain and authentic analytic meaning of every predicate remain independent semantic obligations.

## B. Concrete theorem construction behind theta lift

- `.../ThetaKernels/TPGHolds.lean`, SHA-256 `571074fd012521a7ed0c9f26c3a74e0e3ed3fa50b110979affa4566f6ba0f5ba`: `tools_holds_k` builds `Tools_k` with Siegel–Weil, box section, doubling, stabilizer, compactness, basic theta and Schwartz theory, unfolding, pairing, vacuum fixing, representation action, and Lie differential inputs; `tLift_holds_k := tLift_of_tools_k tools_holds_k (hgtEx_of_k ...)`.
- `.../ThetaKernels/TPGTop.lean`, SHA-256 `8bbd5719adda270dc2c425180e45de3f6ac6c3c4fef21a95306e1633151a1e3f`: `tLift_of_tools_k` combines bridging, height, real-pair, Rallis, decomposition, bump, datum, tail, Schur-step, lift-aut, projective existence, and read-lift components.
- `.../ThetaParseval/SchurStep.lean`, SHA-256 `901ac70f413697a2cf0aea4a35f8d3bc419699c48e01e62a8e06d49503a2e07c`: its inspected `IsLift` includes `aut`, `wt`, and `loc` fields.

## C. From theta lifts to Galois row

- `.../IntegralStructures/GaloisRepresentationsOfThetaLift.lean`, SHA-256 `3f72f1644a6214bb5b90a5e9bac5e33b0474d52eb22f2f1841d443ed342531c2`: `galoisRepresentations_of_thetaLift (up : TP.TLiftK) : GalStar.Row0b recT := galoisLocalGlobalStrong_of_geometry_lift Geo.geoOne_holds up`.
- `.../IntegralStructures/Development.lean`, SHA-256 `b78ea71866812c4d1f3f3e702fa65ec2bb1ea61ca1a250b6fdd536bd`: `recT` is `fun h rc => UpperTheory.Zero.LLC.IsRecT h rc`. `coreAll_of` assembles crystalline descent, geometric/congruence seed, and finite odd trace-limit inputs. `rest` assembles Galois local-global compatibility; `galoisLocalGlobalStrong_of_geometry_lift` upgrades `Row0` to `Row0b`.
- `.../GeometricFlagBases/WeightOneGeometricRealization.lean`, SHA-256 `e642fff070242ac3a7d1857786deb0ead525003c2327254cc3f7d3836cc79b0f`: `geoOne_holds` is derived from a holomorphic Lefschetz fixed-point theorem.
- `.../TypeConditions/WeightsConjBis.lean`, SHA-256 `e3020031e884beef2eff18275019b7213a16f3c721242e9a79891b5396955719`: `Row0b` asserts existence of continuous and semisimple l-adic representations, weight compatibility, conjugate weights, and local p-adic comparison data for the specified regular algebraic polarized automorphic inputs. This is *not merely* an RH proposition renamed; audit the semantic content of its large imported predicates.

## D. Automorphic window and nonvanishing bridge

- `.../ThresholdArguments/DenseThresholdCases/TopMainZj.lean`, SHA-256 `f824d3f7873a493432bdfcbdc279fa82d70a6a9dbaac44c2a30316cada2eae3e`: `automorphic_window_of_inputs` builds `Top.VWin` from literature/open image, isobaric base change, and Galois row; `vwin_of_row` applies it to `Row0b`.
- `.../CharacterBoxes/ExistsPageN.lean`, SHA-256 `732c3347fb02e410cf9af8831afdbba1d230fc522c3dbbccdb4b708e5dde73db`: **exact `VWin` definition** is `∀ ψ : PChar, VWinAt ψ 401`. It is a strong, parameter-uniform analytic/arithmetic estimate: `VWinAt` demands uniform windows for all `0<eps<1/52`, level choices satisfying `PageN`, sufficiently large `X`, prime pairs satisfying `WinPair`, and a `VVle` cohomological length/cost upper bound over all stated field and coefficient data. Merely identifying a `Top.VWin` proof is not independent validation of the claimed number-theoretic bound.
- `.../ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean`, SHA-256 `e761e876e3236895eec1b67b5a2118846ddfcc6883eed367ac6cc78523da15f2`: `every_character_of_theta_integrals_local_matching` consumes `UnitaryGroupThirdPlaceHypotheses`, `ThetaLocalInputs`, `ThetaIntegralsAgree`, `LocalMatching`, `CovolumeBoundOfX`, `RecTExists`, and `VWin`. It invokes `every_character_of_green_v_win` plus a constructed `Nonempty HypsAlt` witness. **All these inputs must be shown true of genuine classical objects** rather than merely packaged under abstract structures.
- `.../CharacterBoxes/EveryCharacter.lean`, SHA-256 `31f6e49936226cfc3d71b15685347bd2874db0aef384e5cf4fea7d09ba68dc71`: `EveryCharacter` is the exact right-half-plane Dirichlet L nonvanishing claim. `plugAll` consumes `Green`, `VWin`, and nonempty closed-bounded family hypotheses to derive it. `ZeroFreeAllOfTopG.lean` explicitly constructs the zero-free route from `TopG` and host-family hypotheses.

## E. Next falsifiable technical obligations

1. **Independent theorem-level nonvacuity fixture:** construct one genuine CM field/base/automorphic representation and show admissibility of all leading `TLiftK` hypotheses, including a nonzero source `U`; do not treat vacuous implications as evidence of a theta lift.
2. **Window-bound reconstruction:** select an explicit character `ψ` and an admissible `WinPair` with a nonempty `IsChiField` family. Prove the actual `VVle` bound, retaining the parameter dependence in `eps`, `X`, `J`, `Y`, and the conductor/loss budget. A bare proof of a conditional `VWinAt` statement does not establish the arithmetic bound.
3. **Noncircular analytic transition:** independently reconstruct `every_character_of_green_v_win` and the `Nonempty HypsAlt` deduction, checking no premise already states a zero-free result equivalent to RH/GRH.
4. **Pinned formal replay:** reconstruct original exact Lean v4.33.1/Mathlib commit and retain `#print axioms`, kernel replay, import graph, generated-declaration and metaprogram trust review. A successful textual comparison is not that replay.

**Classification:** `RH-A26-D05_THETA_LIFT_SOURCE_CROSSWALK_RECONSTRUCTED__VWIN_COST_AND_GENUINE_MODEL_VALIDATION_OPEN`.

This is not an RH/GRH proof claim, independent 175,187-module replay, or MATHCERT certification.
