# RH-A26 D05 — independently reconstructed headline dependency spine

**Original source identity:** assembled SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`; original 175,187-module Lean archive. **Scope:** literal source dependency trace and mathematical proof obligations, not a fully independent theorem verification. **Date:** 2026-11-21.

## Literal proof-source spine

| Source file (`lean/src/` prefix) | Original declaration | Immediate source-level dependency |
|---|---|---|
| `Main.lean` | five headline declarations | `rhOfAll`, `rhOfAll`, `allChi`, `claimAll.2.1`, `critAll` |
| `Supplements/Kernels/MainTheorems.lean` | `allChi : UpperTheory.EveryCharacter` | `UpperTheory.FinalTheorems.everyCharacter` |
| same | `rhOfAll : RiemannHypothesis` | `Formalism.VW.rh_of_every allChi` |
| same | `critAll` | `Formalism.VW.critLine allChi` |
| same | `claimAll : Claim.HalfPlane ∧ Claim.Strip ∧ Claim.Zeta` | `allChi`, `Claim.strip allChi`, `Claim.zeta allChi` |
| `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean` | `UpperTheory.FinalTheorems.everyCharacter` | `everyCharacter_of_row UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` |
| same | `everyCharacter_of_row` | `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` applied to the row, `recTExists`, and `UpperTheory.One.vwin_of_row` |
| `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean` | `galoisLocalGlobalStrong_recParameter` | `galoisRepresentations_of_thetaLift UpperTheory.TP.K.tLiftK` |
| `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VwinOfRow.lean` | `vwin_of_row` | `automorphic_window_of_inputs` with `OpenImageCondition.mk` and `baseChangeN` |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean` | `every_character_of_literature_of_vWin` | `UpperTheory.Lit.every_character_of_theta_integrals_local_matching`; numerous explicit literature input projections, self-intersection/volume bound, local Langlands input, and `VWin` |

## Exact final analytic reductions (inspected original source)

- `Formalism/GammaFactorNonvanishing/CritLine.lean`, `Formalism.VW.critLine`: for primitive χ and zeros at `0 < Re(s) < 1/2`, nonvanishing of the gamma factor plus the completed L functional equation reflects a zero of inverse χ to `1-s`, contradicting `EveryCharacter`. For zeros at `Re(s)>1/2`, it invokes `EveryCharacter` directly. Its `rh_of_every` specializes to modulus one and uses `LFunction_modOne_eq`.
- `Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean`, `Claim.prim_zero`: imprimitive χ zeros in the open critical strip transfer to the primitive associate using `LFunction_changeLevel`; nonzero Euler factors for `Re(s)>0` exclude a spurious zero in the level-change product.
- Same file `Claim.prim_reflect`: primitive completed L functional equation reflects zeros under `s→1-s` and `χ→χ⁻¹`. `Claim.strip` combines `prim_zero`, `prim_reflect`, and `HalfPlane` to derive all-character critical-line zeros.
- Same file `Claim.zeta`: isolates negative-even trivial zeros, modulus-one specialization, gamma factors, and nonvanishing in `Re(s)≥1`; `Claim.zeta_iff : Zeta ↔ RiemannHypothesis := Iff.rfl`.

## Mathematical proof debt — prioritize the actual load-bearing claim

The final reflection and level-change arguments are explicit in source and can be audited lemma by lemma. They do **not** independently substantiate the new half-plane nonvanishing result because they consume `UpperTheory.EveryCharacter` as input.

The hardest and potentially novel mathematical dependency visible in this trace is:

```text
UpperTheory.TP.K.tLiftK
    ↓ galoisRepresentations_of_thetaLift
UpperTheory.GalStar.Row0b recT
    ↓ automorphic_window_of_inputs / baseChangeN
UpperTheory.Top.VWin
    ↓ every_character_of_theta_integrals_local_matching
UpperTheory.EveryCharacter
    ↓ analytic functional equations and imprimitive factor handling
RH + Dirichlet GRH headline propositions
```

**Next independent reconstruction obligations:** (1) unfold `tLiftK` and `galoisRepresentations_of_thetaLift`, record their exact mathematical hypotheses and whether their constructions are nonempty; (2) independently audit `automorphic_window_of_inputs` and its required threshold/conductor accounting; (3) reconstruct the large `every_character_of_theta_integrals_local_matching` proof at statement level, including each literature bridge and noncircularity; (4) test the final analytic lemmas with exact-original source and independent Lean kernel/axiom reports at suitable compute. Mere spelling presence/absence of `axiom` or `sorry` is not this audit.

## GitHub checks versus mathematical replay

MATHFORGE PR #587, exact old head `43530d8790fbc7065797707ffa0a7e1a6f7c3a46`, passed GitHub repository checks including conformance and CodeQL; these checks concern this documentary PR, not the 175,187-module original Lean archive. Nothing here upgrades RH/GRH proof or MATHCERT authority.

**Disposition:** `RH-A26-D05_HEADLINE_PROOF_SPINE_SOURCE_TRACED__LOAD_BEARING_AUTOMORPHIC_BRIDGE_OPEN`.
