/-!
# OAI-26 F003: internal ray-character series and lattice-period invariance

Source-locked off-path GCL proof obligations, not modifications to upstream.
Exact upstream: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a.
These lemmas establish internal model presentation independence and ideal
Dirichlet-series correspondence; they do NOT prove equivalence with every
external Hecke-character formalization or the 7/8 analytic estimates.
-/
import OAI.NumberTheory.DirichletL.Hecke.IdealBridge
import OAI.NumberTheory.DirichletL.Hecke.RayFamily

namespace OAI.SevenEighths.HeckeFamily

noncomputable section

/-- Equal Eisenstein coefficient functions yield equal continued L-functions
in the half-plane containing the target 7/8 region, outside s=1. -/
theorem gcl_LFunction_eq_of_elementCoeff_eq
    (χ ψ : Character)
    (hcoeff : ∀ z : O, elementCoeff χ z = elementCoeff ψ z)
    {s : ℂ} (hs : 0 < s.re) (hs₁ : s ≠ 1) :
    LFunction χ s = LFunction ψ s := by
  change continuedLattice χ s / 6 = continuedLattice ψ s / 6
  exact congrArg (fun v : ℂ => v / 6)
    (continuedLattice_eq_of_elementCoeff_eq χ ψ hcoeff hs hs₁)

/-- A change of the auxiliary positive lattice period (still contained
in the modulus ideal) cannot change the formal L-function for Re(s)>0, s≠1. -/
theorem gcl_LFunction_period_choice_immaterial
    (χ : Character) (n : ℕ) (hn : 0 < n)
    (hmem : (n : O) ∈ χ.modulus)
    {s : ℂ} (hs : 0 < s.re) (hs₁ : s ≠ 1) :
    LFunction χ s =
      LFunction ({χ with period := n, period_pos := hn,
                        period_mem := hmem} : Character) s := by
  exact gcl_LFunction_eq_of_elementCoeff_eq χ _
    (by intro z; rfl) hs hs₁

end

end OAI.SevenEighths.HeckeFamily

namespace OAI.SevenEighths.HeckeRayFamily

noncomputable section

open OAI.SevenEighths.HeckeFamily

variable (M : Ideal O) [NeZero M]
local instance : Finite (O ⧸ M) :=
  Ring.HasFiniteQuotients.finiteQuotient (NeZero.ne M)

/-- On the absolutely convergent half-plane, a finite ray-character
L-function is exactly the ideal Dirichlet series of the corresponding
unit-invariant residue character. No new analytic zero-free estimate is used. -/
theorem gcl_LFunction_eq_ray_ideal_tsum
    (ρ : OAI.SevenEighths.RayOrthogonality.rayCharacters M)
    {s : ℂ} (hs : 1 < s.re) :
    LFunction (character M ρ) s =
      ∑' I : Ideal O,
        OAI.SevenEighths.RayOrthogonality.idealCharacter M ρ I /
        (Ideal.absNorm I : ℂ) ^ s := by
  rw [LFunction_eq_ideal_tsum (character M ρ) hs]
  simp only [idealTerm, idealCoeff_character]

end

end OAI.SevenEighths.HeckeRayFamily
