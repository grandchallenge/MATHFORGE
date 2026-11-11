import Mathlib
import OAI.NumberTheory.TotientFibers.FiniteFiber

namespace GCL.OAI26.Family011

noncomputable def externalFiberCount (n : ℕ) : ℕ :=
  ({m : ℕ | Nat.totient m = n} : Set ℕ).ncard

theorem external_fiber_count_eq_g_of_pos (n : ℕ) (hn : 0 < n) :
    externalFiberCount n = OAI.TotientFibers.g n := by
  have hsets : ({m : ℕ | Nat.totient m = n} : Set ℕ) =
      OAI.TotientFibers.fiber n := by
    ext m
    constructor
    · intro h
      refine ⟨?_, h⟩
      by_contra hm
      have hm0 : m = 0 := Nat.eq_zero_of_not_pos hm
      subst m
      simp at h
      omega
    · intro h
      exact h.2
  simp only [externalFiberCount, OAI.TotientFibers.g, hsets]

#print axioms GCL.OAI26.Family011.external_fiber_count_eq_g_of_pos

/-- Removing the single target zero from an infinite set and rewriting the
    positive-target preimage count preserves infinitude. -/
theorem infinite_gcl_of_external (ε : ℝ)
    (h : Set.Infinite {n : ℕ | (externalFiberCount n : ℝ) >
      (n : ℝ) ^ (1 - ε)}) :
    Set.Infinite {n : ℕ | 0 < n ∧
      (OAI.TotientFibers.g n : ℝ) > (n : ℝ) ^ (1 - ε)} := by
  have hpos : Set.Infinite
      ({n : ℕ | (externalFiberCount n : ℝ) > (n : ℝ) ^ (1 - ε)} \ {0}) :=
    h.sdiff (Set.finite_singleton 0)
  convert hpos using 1
  ext n
  simp only [Set.mem_sdiff, Set.mem_ofPred_eq, Set.mem_singleton_iff]
  constructor
  · rintro ⟨hn, h⟩
    rw [← external_fiber_count_eq_g_of_pos n hn] at h
    exact ⟨h, Nat.ne_of_gt hn⟩
  · rintro ⟨h, hn0⟩
    have hn : 0 < n := Nat.pos_of_ne_zero hn0
    rw [external_fiber_count_eq_g_of_pos n hn] at h
    exact ⟨hn, h⟩

#print axioms GCL.OAI26.Family011.infinite_gcl_of_external

/-- Universal-ε transfer of the exact external Erdős 821 statement to
    GCL's positivity-restricted theorem statement. -/
theorem gcl_claim_of_external_claim
    (h : ∀ ε > (0 : ℝ),
      Set.Infinite {n : ℕ | (externalFiberCount n : ℝ) >
        (n : ℝ) ^ (1 - ε)}) :
    ∀ ε > (0 : ℝ),
      Set.Infinite {n : ℕ | 0 < n ∧
        (OAI.TotientFibers.g n : ℝ) > (n : ℝ) ^ (1 - ε)} := by
  intro ε hε
  exact infinite_gcl_of_external ε (h ε hε)

#print axioms GCL.OAI26.Family011.gcl_claim_of_external_claim


end GCL.OAI26.Family011
