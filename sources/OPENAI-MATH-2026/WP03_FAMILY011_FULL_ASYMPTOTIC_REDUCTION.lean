import OAI.NumberTheory.TotientFibers.FiniteFiber

open Filter
open scoped Topology

namespace GCL.OAI26.Family011

/-- The shifted primes counted at a fixed real smoothness exponent. -/
def smoothPrimeSet (x : ℕ) (δ : ℝ) : Finset ℕ :=
  (Finset.Ioc (2 * x) (5 * x)).filter fun p =>
    p.Prime ∧ ∀ q : ℕ, q.Prime → q ∣ p - 1 → (q : ℝ) ≤ (x : ℝ) ^ δ

/-- Fixed-delta prime count over integer x. This is a hypothesis, not a proven theorem. -/
def SmoothPrimeCount : Prop :=
  ∀ δ : ℝ, 0 < δ → δ < 1 / 4 → ∀ η : ℝ, 0 < η →
    ∀ᶠ x : ℕ in atTop,
      (x : ℝ) ^ (1 - η) ≤ ((smoothPrimeSet x δ).card : ℝ)

/-- Identical supply predicate to the earlier protected conditional bridge. -/
def PrimeSupplyForExponent (ε : ℝ) : Prop :=
  ∀ T : ℕ, ∃ (t a : ℕ) (P : Finset ℕ),
    T ≤ t ∧ 5 ≤ a ∧ a ≤ t ∧ 4 ≤ (a : ℝ) * ε ∧
    (∀ p ∈ P, p.Prime) ∧
    (∀ p ∈ P, p ≤ t ^ a) ∧
    (∀ p ∈ P, ∀ q : ℕ, q.Prime → q ∣ p - 1 → q ≤ t) ∧
    t ^ (a - 1) < P.card

private lemma param_pos (a : ℕ) (ha : 6 ≤ a) :
    0 < (a : ℝ) / ((a * a - 1 : ℕ) : ℝ) ∧
    (a : ℝ) / ((a * a - 1 : ℕ) : ℝ) < 1 / 4 ∧
    0 < (1 : ℝ) / ((a * a - 1 : ℕ) : ℝ) := by
  sorry

private lemma rpow_nat_power (N c b : ℕ) (hc : 0 < c) :
    (((N ^ c : ℕ) : ℝ) ^ ((b : ℝ) / (c : ℝ))) = (N ^ b : ℕ) := by
  sorry

private lemma rpow_nat_power_minus_one (N c : ℕ) (hc : 0 < c) :
    (((N ^ c : ℕ) : ℝ) ^ (1 - 1 / (c : ℝ))) = (N ^ (c - 1) : ℕ) := by
  sorry

theorem prime_supply_of_smooth_count
    (hcount : SmoothPrimeCount) (ε : ℝ) (hε : 0 < ε) :
    PrimeSupplyForExponent ε := by
  sorry

/-- Main conditional asymptotic reduction. Analytic count is an assumption. -/
theorem infinite_fibers_of_smooth_count
    (hcount : SmoothPrimeCount) (ε : ℝ) (hε : 0 < ε) :
    Set.Infinite {n : ℕ | 0 < n ∧ (n : ℝ) ^ (1 - ε) < (OAI.TotientFibers.g n : ℝ)} := by
  by_cases hεle : ε ≤ 1
  · apply OAI.TotientFibers.infinite_of_unbounded_g
    intro B
    obtain ⟨t, a, P, hT, ha, hat, haε, hprime, hsize, hsmooth, hcard⟩ :=
      prime_supply_of_smooth_count hcount ε hε (B + 1)
    obtain ⟨n, hn, htg, hnε⟩ :=
      OAI.TotientFibers.finite_large_fiber_rpow ha hat hεle haε hprime hsize hsmooth hcard
    exact ⟨n, hn, hnε, by omega⟩
  · exact OAI.TotientFibers.totient_large_fibers_of_one_le (by linarith)

end GCL.OAI26.Family011
