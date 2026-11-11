import OAI.NumberTheory.TotientFibers.FiniteFiber

open Filter
open scoped Topology

namespace GCL.OAI26.Family011

/-- The shifted primes counted at a fixed real smoothness exponent. -/
noncomputable def smoothPrimeSet (x : ℕ) (δ : ℝ) : Finset ℕ := by
  classical
  exact (Finset.Ioc (2 * x) (5 * x)).filter fun p =>
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
  have haR : (6 : ℝ) ≤ (a : ℝ) := by exact_mod_cast ha
  have hprod : 1 ≤ a * a := by nlinarith
  have hc : ((a * a - 1 : ℕ) : ℝ) = (a : ℝ) ^ 2 - 1 := by
    rw [Nat.cast_sub hprod]
    push_cast
    ring
  have hcpos : (0 : ℝ) < ((a * a - 1 : ℕ) : ℝ) := by
    rw [hc]
    nlinarith
  have haux : (0 : ℝ) ≤ ((a : ℝ) - 6) * ((a : ℝ) + 2) :=
    mul_nonneg (by linarith) (by linarith)
  refine ⟨div_pos (by positivity) hcpos, ?_, div_pos (by norm_num) hcpos⟩
  apply (div_lt_iff₀ hcpos).2
  rw [hc]
  nlinarith [haux]

private lemma rpow_nat_power (N c b : ℕ) (hc : 0 < c) :
    (((N ^ c : ℕ) : ℝ) ^ ((b : ℝ) / (c : ℝ))) = (N ^ b : ℕ) := by
  have hcnz : (c : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hc)
  have hN : (0 : ℝ) ≤ (N : ℝ) := by positivity
  calc
    (((N ^ c : ℕ) : ℝ) ^ ((b : ℝ) / (c : ℝ)))
        = ((N : ℝ) ^ c) ^ ((b : ℝ) / (c : ℝ)) := by norm_cast
    _ = (N : ℝ) ^ ((c : ℝ) * ((b : ℝ) / (c : ℝ))) :=
      (Real.rpow_natCast_mul hN c _).symm
    _ = (N : ℝ) ^ (b : ℝ) := by
      have heq : (c : ℝ) * ((b : ℝ) / (c : ℝ)) = (b : ℝ) := by field_simp
      rw [heq]
    _ = (N ^ b : ℕ) := by rw [Real.rpow_natCast]; norm_cast

private lemma rpow_nat_power_minus_one (N c : ℕ) (hc : 0 < c) :
    (((N ^ c : ℕ) : ℝ) ^ (1 - 1 / (c : ℝ))) = (N ^ (c - 1) : ℕ) := by
  have hcnz : (c : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hc)
  have hcast : ((c - 1 : ℕ) : ℝ) = (c : ℝ) - 1 := by
    rw [Nat.cast_sub (by omega : 1 ≤ c)]
    norm_num
  have hexp : (1 : ℝ) - 1 / (c : ℝ) = ((c - 1 : ℕ) : ℝ) / (c : ℝ) := by
    rw [hcast]
    field_simp
  rw [hexp]
  exact rpow_nat_power N c (c - 1) hc

private lemma choose_a (ε : ℝ) (hε : 0 < ε) :
    ∃ a : ℕ, 6 ≤ a ∧ 4 ≤ (a : ℝ) * ε := by
  obtain ⟨a, ha⟩ := exists_nat_gt (max (6 : ℝ) (4 / ε))
  refine ⟨a, ?_, ?_⟩
  · have h6 : (6 : ℝ) < (a : ℝ) := lt_of_le_of_lt (le_max_left _ _) ha
    exact_mod_cast h6.le
  · have h4 : (4 : ℝ) / ε < (a : ℝ) :=
      lt_of_le_of_lt (le_max_right _ _) ha
    have h4' := mul_lt_mul_of_pos_right h4 hε
    have hdiv : (4 / ε) * ε = (4 : ℝ) := by
      field_simp [ne_of_gt hε]
    rw [hdiv] at h4'
    exact h4'.le

theorem prime_supply_of_smooth_count
    (hcount : SmoothPrimeCount) (ε : ℝ) (hε : 0 < ε) :
    PrimeSupplyForExponent ε := by
  classical
  intro T
  obtain ⟨a, ha6, haε⟩ := choose_a ε hε
  let c : ℕ := a * a - 1
  let δ : ℝ := (a : ℝ) / (c : ℝ)
  let η : ℝ := 1 / (c : ℝ)
  have hc : 1 ≤ c := by
    dsimp [c]
    have h : 36 ≤ a * a := by nlinarith
    omega
  have hcEq : c + 1 = a * a := by
    dsimp [c]
    have h : 36 ≤ a * a := by nlinarith
    omega
  have hδpos : 0 < δ := by simpa [δ, c] using (param_pos a ha6).1
  have hδlt : δ < 1 / 4 := by simpa [δ, c] using (param_pos a ha6).2.1
  have hηpos : 0 < η := by simpa [η, c] using (param_pos a ha6).2.2
  obtain ⟨K, hK⟩ := Filter.eventually_atTop.1 (hcount δ hδpos hδlt η hηpos)
  let N : ℕ := K + T + a + 6
  let x : ℕ := N ^ c
  let t : ℕ := N ^ a
  let P : Finset ℕ := smoothPrimeSet x δ
  have hN5 : 5 ≤ N := by dsimp [N]; omega
  have hNK : K ≤ N := by dsimp [N]; omega
  have hNT : T ≤ N := by dsimp [N]; omega
  have hNa : a ≤ N := by dsimp [N]; omega
  have hNx : N ≤ x := by
    dsimp [x]
    exact le_self_pow (by omega : 1 ≤ N) (by omega : c ≠ 0)
  have hNt : N ≤ t := by
    dsimp [t]
    exact le_self_pow (by omega : 1 ≤ N) (by omega : a ≠ 0)
  have hcountP : (x : ℝ) ^ (1 - η) ≤ (P.card : ℝ) := by
    exact hK x (hNK.trans hNx)
  have hxδ : (x : ℝ) ^ δ = (t : ℝ) := by
    simpa [x, t, δ] using rpow_nat_power N c a (by omega : 0 < c)
  have hxη : (x : ℝ) ^ (1 - η) = (N ^ (c - 1) : ℕ) := by
    simpa [x, η] using rpow_nat_power_minus_one N c (by omega : 0 < c)
  have hSize : 5 * x ≤ t ^ a := by
    have h5 : 5 * x ≤ x * N := by
      simpa [mul_comm] using (Nat.mul_le_mul_left x hN5)
    calc
      5 * x ≤ x * N := h5
      _ = N ^ (c + 1) := by simp [x, pow_succ]
      _ = N ^ (a * a) := by rw [hcEq]
      _ = t ^ a := by simp [t, pow_mul]
  have hExp : a * (a - 1) < c - 1 := by
    have hprod : a * (a - 1) = a * a - a := by
      rw [Nat.mul_sub_left_distrib]
      simp
    have h : 36 ≤ a * a := by nlinarith
    dsimp [c]
    omega
  have hCard : t ^ (a - 1) < P.card := by
    have hpow : N ^ (a * (a - 1)) < N ^ (c - 1) :=
      Nat.pow_lt_pow_right (by omega : 1 < N) hExp
    have hlt : ((t ^ (a - 1) : ℕ) : ℝ) < (x : ℝ) ^ (1 - η) := by
      rw [hxη]
      have heq : t ^ (a - 1) = N ^ (a * (a - 1)) := by
        simp [t, pow_mul]
      rw [heq]
      exact_mod_cast hpow
    exact_mod_cast lt_of_lt_of_le hlt hcountP
  refine ⟨t, a, P, hNT.trans hNt, (by omega : 5 ≤ a), hNa.trans hNt, haε, ?_, ?_, ?_, hCard⟩
  · intro p hp
    exact (Finset.mem_filter.mp hp).2.1
  · intro p hp
    have hp5 : p ≤ 5 * x :=
      (Finset.mem_Ioc.mp (Finset.mem_filter.mp hp).1).2
    exact hp5.trans hSize
  · intro p hp q hq hd
    have hqR : (q : ℝ) ≤ (x : ℝ) ^ δ :=
      (Finset.mem_filter.mp hp).2.2 q hq hd
    rw [hxδ] at hqR
    exact_mod_cast hqR

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
open Filter
open scoped Topology

namespace GCL.OAI26.Family011

open scoped Classical

/-- A literal statement mirror of cadamcat/totient-fibers-lean4
    Erdos821/Supply.lean, audited at f75d4f2c2d6685a0547f17fa07240377aa2c2ed4.
    No external proof is imported by this definition. -/
noncomputable def externalSmoothShiftedPrimes (δ x : ℝ) : Finset ℕ :=
  (Finset.Ioc ⌊2 * x⌋₊ ⌊5 * x⌋₊).filter fun p =>
    p.Prime ∧ ∀ q : ℕ, q.Prime → q ∣ p - 1 → (q : ℝ) ≤ x ^ δ

def ExternalSmoothPrimeCount : Prop :=
  ∀ δ : ℝ, 0 < δ → δ < 1 / 4 → ∀ σ : ℝ, 0 < σ →
    ∀ᶠ x : ℝ in atTop, x ^ (1 - σ) ≤ ((externalSmoothShiftedPrimes δ x).card : ℝ)

/-- Real-x counting agrees exactly with GCL's natural-x count at integer x. -/
private theorem external_set_nat (δ : ℝ) (n : ℕ) :
    externalSmoothShiftedPrimes δ (n : ℝ) = smoothPrimeSet n δ := by
  have h2 : ⌊(2 : ℝ) * (n : ℝ)⌋₊ = 2 * n := by
    simpa using (Nat.floor_natCast (2 * n) : ⌊((2 * n : ℕ) : ℝ)⌋₊ = 2 * n)
  have h5 : ⌊(5 : ℝ) * (n : ℝ)⌋₊ = 5 * n := by
    simpa using (Nat.floor_natCast (5 * n) : ⌊((5 * n : ℕ) : ℝ)⌋₊ = 5 * n)
  simp [externalSmoothShiftedPrimes, smoothPrimeSet, h2, h5]

/-- Exact statement bridge; existence of external count proof is not assumed proved here. -/
theorem smooth_count_of_external (h : ExternalSmoothPrimeCount) : SmoothPrimeCount := by
  intro δ hδ hδ4 η hη
  obtain ⟨K, hK⟩ := Filter.eventually_atTop.1 (h δ hδ hδ4 η hη)
  obtain ⟨N, hN⟩ := exists_nat_gt K
  apply Filter.eventually_atTop.2
  refine ⟨N, ?_⟩
  intro n hn
  have hKReal : K ≤ (n : ℝ) := by
    calc
      K ≤ (N : ℝ) := le_of_lt hN
      _ ≤ (n : ℝ) := by exact_mod_cast hn
  have hcount := hK (n : ℝ) hKReal
  simpa only [external_set_nat] using hcount

theorem infinite_fibers_of_external
    (h : ExternalSmoothPrimeCount) (ε : ℝ) (hε : 0 < ε) :
    Set.Infinite {n : ℕ | 0 < n ∧ (n : ℝ) ^ (1 - ε) < (OAI.TotientFibers.g n : ℝ)} :=
  infinite_fibers_of_smooth_count (smooth_count_of_external h) ε hε

end GCL.OAI26.Family011

#print axioms GCL.OAI26.Family011.smooth_count_of_external
#print axioms GCL.OAI26.Family011.infinite_fibers_of_external
