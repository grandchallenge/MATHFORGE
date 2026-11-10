import OAI.NumberTheory.TotientFibers.FiniteFiber

open OAI

namespace GCL.OAI26.Family011

/-- Explicit smooth-prime supply input. This hypothesis is NOT established by this file. -/
def PrimeSupplyForExponent (ε : ℝ) : Prop :=
  ∀ T : ℕ, ∃ (t a : ℕ) (P : Finset ℕ),
    T ≤ t ∧ 5 ≤ a ∧ a ≤ t ∧ 4 ≤ (a : ℝ) * ε ∧
    (∀ p ∈ P, p.Prime) ∧
    (∀ p ∈ P, p ≤ t ^ a) ∧
    (∀ p ∈ P, ∀ q : ℕ, q.Prime → q ∣ p - 1 → q ≤ t) ∧
    t ^ (a - 1) < P.card

/-- Conditional bridge only; does not establish its prime-supply hypothesis. -/
theorem infinite_fibers_of_supply
    (ε : ℝ) (hε : 0 < ε) (hεle : ε ≤ 1)
    (hsupply : PrimeSupplyForExponent ε) :
    Set.Infinite {n : ℕ | 0 < n ∧ (n : ℝ) ^ (1 - ε) < (OAI.TotientFibers.g n : ℝ)} := by
  apply OAI.TotientFibers.infinite_of_unbounded_g
  intro B
  obtain ⟨t, a, P, htB, ha, hat, haε, hprime, hsize, hsmooth, hcard⟩ :=
    hsupply (B + 1)
  obtain ⟨n, hn, htg, hnε⟩ :=
    OAI.TotientFibers.finite_large_fiber_rpow ha hat hεle haε hprime hsize hsmooth hcard
  exact ⟨n, hn, hnε, by omega⟩

end GCL.OAI26.Family011
