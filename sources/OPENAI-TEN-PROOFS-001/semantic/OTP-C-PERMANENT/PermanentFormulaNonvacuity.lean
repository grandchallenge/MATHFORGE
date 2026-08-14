import ComparatorChallenges.C_PermanentFormulaLowerBound

namespace PermanentFormulaLowerBound

universe u v

namespace Nonvacuity

/-- Every multivariate polynomial has a division-free `Formula` representative.
This is proved only from the constructors admitted by the protected formula model. -/
theorem formula_eval_surjective {ι : Type u} {R : Type v} [CommRing R]
    (p : MvPolynomial ι R) :
    ∃ f : Formula ι R, Formula.eval f = p := by
  induction p using MvPolynomial.induction_on with
  | C a =>
      exact ⟨Formula.const a, rfl⟩
  | add p q hp hq =>
      rcases hp with ⟨f, hf⟩
      rcases hq with ⟨g, hg⟩
      exact ⟨Formula.add f g, by simp [Formula.eval, hf, hg]⟩
  | mul_X p i hp =>
      rcases hp with ⟨f, hf⟩
      exact ⟨Formula.mul f (Formula.var i), by simp [Formula.eval, hf]⟩

/-- Embed a division-free formula into the rational-formula syntax without
introducing any division nodes. -/
def formulaToRational {ι : Type u} {R : Type v} :
    Formula ι R → RationalFormula ι R
  | .var i => .var i
  | .const c => .const c
  | .add f g => .add (formulaToRational f) (formulaToRational g)
  | .sub f g => .sub (formulaToRational f) (formulaToRational g)
  | .mul f g => .mul (formulaToRational f) (formulaToRational g)

/-- A division-free formula remains valid when embedded into rational syntax. -/
theorem formulaToRational_valid {ι : Type u} {R : Type v} [Field R]
    (f : Formula ι R) :
    RationalFormula.Valid (formulaToRational f) := by
  induction f with
  | var i => exact RationalFormula.Valid.var i
  | const c => exact RationalFormula.Valid.const c
  | add f g hf hg => exact RationalFormula.Valid.add hf hg
  | sub f g hf hg => exact RationalFormula.Valid.sub hf hg
  | mul f g hf hg => exact RationalFormula.Valid.mul hf hg

/-- The division-free embedding preserves evaluation under the canonical map
from polynomials to their fraction ring. -/
theorem formulaToRational_eval {ι : Type u} {R : Type v} [Field R]
    (f : Formula ι R) :
    RationalFormula.eval (formulaToRational f) =
      algebraMap (MvPolynomial ι R) (FractionRing (MvPolynomial ι R))
        (Formula.eval f) := by
  induction f with
  | var i => rfl
  | const c => rfl
  | add f g hf hg =>
      simp [formulaToRational, RationalFormula.eval, Formula.eval, hf, hg]
  | sub f g hf hg =>
      simp [formulaToRational, RationalFormula.eval, Formula.eval, hf, hg]
  | mul f g hf hg =>
      simp [formulaToRational, RationalFormula.eval, Formula.eval, hf, hg]

/-- The embedding preserves the variable-leaf statistic used by the two
encoded lower-bound targets. -/
theorem formulaToRational_variableLeaves {ι : Type u} {R : Type v}
    (f : Formula ι R) :
    RationalFormula.variableLeaves (formulaToRational f) =
      Formula.variableLeaves f := by
  induction f <;>
    simp [formulaToRational, RationalFormula.variableLeaves,
      Formula.variableLeaves, *]

/-- The division-free representation premise of the encoded Permanent target
is inhabited for every dimension, hence in particular throughout `n ≥ 32`. -/
theorem permanent_divisionFree_formula_nonvacuous (n : ℕ) :
    ∃ f : Formula (Fin n × Fin n) ℂ,
      Formula.eval f = permanentPolynomial n := by
  exact formula_eval_surjective (permanentPolynomial n)

/-- The validity-plus-representation premises of the encoded rational
Permanent target are jointly inhabited for every dimension. -/
theorem permanent_rational_formula_nonvacuous (n : ℕ) :
    ∃ f : RationalFormula (Fin n × Fin n) ℂ,
      RationalFormula.Valid f ∧
      RationalFormula.eval f =
        algebraMap (MvPolynomial (Fin n × Fin n) ℂ)
          (FractionRing (MvPolynomial (Fin n × Fin n) ℂ))
          (permanentPolynomial n) := by
  rcases permanent_divisionFree_formula_nonvacuous n with ⟨f, hf⟩
  refine ⟨formulaToRational f, formulaToRational_valid f, ?_⟩
  rw [formulaToRational_eval, hf]

end Nonvacuity

end PermanentFormulaLowerBound
