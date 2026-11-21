import Mathlib.NumberTheory.NumberField.HeckeLFunction

/-!
# F003 native idèle Hecke character: deleted-conductor local Euler factor

Independent sidecar against mathlib4@6e96f3e25b9b23468a6f155342b5a1e5e33ac8f9,
Lean v4.36.0-rc2. This is NOT compiled inside old openai/math v4.34.1.

The native local Euler polynomial is 1-aX at an unramified place and
1 at a ramified place. The zero-extended ray-character presentation
deletes *every* Euler factor at primes dividing its chosen modulus,
including primes where the intrinsic native character is unramified.

This file proves the precise local polynomial correction, a zero-free
analytic-disk lemma under a bounded local value, and its consequence for
the actual native Hecke-character local polynomial. It does NOT construct
the global idele-to-ray map or prove global Euler/meromorphic equality.
-/

namespace GCL.OAI26.F003.NativeConductor

open NumberField
open IsDedekindDomain
open Polynomial

noncomputable section

variable {R K : Type*} [CommRing R] [IsDedekindDomain R]
  [Field K] [Algebra R K] [IsFractionRing R K]

variable (χ : NumberField.HeckeCharacter R K)

/-- The local polynomial of a ray presentation extended by zero at the
entire defining modulus. At a prime in the modulus, its polynomial is
1 even if the underlying native Hecke character is unramified there. -/
def presentationPolynomial (bad : Set (HeightOneSpectrum R))
    (v : HeightOneSpectrum R) : ℂ[X] :=
  if v ∈ bad then 1 else 1 - C (χ.localValue v) * X

/-- The missing polynomial precisely at an unramified prime which the
chosen presentation's modulus deletes. At ramified primes it is 1. -/
def deletionCorrection (bad : Set (HeightOneSpectrum R))
    (v : HeightOneSpectrum R) : ℂ[X] :=
  if v ∈ bad then χ.localPolynomial v else 1

theorem presentationPolynomial_of_mem
    (bad : Set (HeightOneSpectrum R)) (v : HeightOneSpectrum R)
    (hv : v ∈ bad) :
    presentationPolynomial χ bad v = 1 := by
  simp [presentationPolynomial, hv]

theorem deletionCorrection_of_not_mem
    (bad : Set (HeightOneSpectrum R)) (v : HeightOneSpectrum R)
    (hv : v ∉ bad) :
    deletionCorrection χ bad v = 1 := by
  simp [deletionCorrection, hv]

theorem deletionCorrection_of_ramified
    (bad : Set (HeightOneSpectrum R)) (v : HeightOneSpectrum R)
    (hram : ¬ χ.IsUnramifiedAt v) :
    deletionCorrection χ bad v = 1 := by
  by_cases hv : v ∈ bad
  · simp [deletionCorrection, hv,
      NumberField.HeckeCharacter.localPolynomial, hram]
  · simp [deletionCorrection, hv]

/-- An exact, character-typed correction at each finite place.
The only required hypothesis is that the native character be
unramified *outside* the chosen zero-extension modulus. -/
theorem localPolynomial_presentation_times_correction
    (bad : Set (HeightOneSpectrum R)) (v : HeightOneSpectrum R)
    (houtside : v ∉ bad → χ.IsUnramifiedAt v) :
    χ.localPolynomial v =
      presentationPolynomial χ bad v * deletionCorrection χ bad v := by
  by_cases hv : v ∈ bad
  · simp [presentationPolynomial, deletionCorrection, hv]
  · have hu : χ.IsUnramifiedAt v := houtside hv
    simp [presentationPolynomial, deletionCorrection, hv,
      NumberField.HeckeCharacter.localPolynomial, hu]

/-- The elementary disk estimate at the exact local factor;
it does not assume analyticity or summation of an infinite Euler product. -/
theorem one_sub_mul_ne_zero_of_norm_lt_one
    (a z : ℂ) (ha : ‖a‖ ≤ 1) (hz : ‖z‖ < 1) :
    (1 : ℂ) - a * z ≠ 0 := by
  intro hzero
  have heq : a * z = 1 := (sub_eq_zero.mp hzero).symm
  have hlt : ‖a * z‖ < (1 : ℝ) := calc
    ‖a * z‖ = ‖a‖ * ‖z‖ := norm_mul a z
    _ ≤ 1 * ‖z‖ := mul_le_mul_of_nonneg_right ha (norm_nonneg z)
    _ < 1 := by simpa using hz
  rw [heq, norm_one] at hlt
  exact (lt_irrefl (1 : ℝ)) hlt

/-- The actual native idèle-class character's deletion polynomial
cannot vanish in the open unit disk when its local value has norm ≤ 1. -/
theorem deletionCorrection_eval_ne_zero
    (bad : Set (HeightOneSpectrum R)) (v : HeightOneSpectrum R)
    (z : ℂ) (hvalue : ‖χ.localValue v‖ ≤ 1) (hz : ‖z‖ < 1) :
    (deletionCorrection χ bad v).eval z ≠ 0 := by
  by_cases hv : v ∈ bad
  · by_cases hu : χ.IsUnramifiedAt v
    · simpa [deletionCorrection, hv,
        NumberField.HeckeCharacter.localPolynomial, hu]
        using one_sub_mul_ne_zero_of_norm_lt_one (χ.localValue v) z hvalue hz
    · simp [deletionCorrection, hv,
        NumberField.HeckeCharacter.localPolynomial, hu]
  · simp [deletionCorrection, hv]

end

end GCL.OAI26.F003.NativeConductor
