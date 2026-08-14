import Mathlib

namespace PermanentFormulaLowerBound

universe u v

inductive Formula (ι : Type u) (R : Type v) where
  | var : ι → Formula ι R
  | const : R → Formula ι R
  | add : Formula ι R → Formula ι R → Formula ι R
  | sub : Formula ι R → Formula ι R → Formula ι R
  | mul : Formula ι R → Formula ι R → Formula ι R

namespace Formula

variable {ι : Type u} {R : Type v}

noncomputable def eval [CommRing R] : Formula ι R → MvPolynomial ι R
  | .var i => MvPolynomial.X i
  | .const c => MvPolynomial.C c
  | .add f g => eval f + eval g
  | .sub f g => eval f - eval g
  | .mul f g => eval f * eval g

def variableLeaves : Formula ι R → ℕ
  | .var _ => 1
  | .const _ => 0
  | .add f g => variableLeaves f + variableLeaves g
  | .sub f g => variableLeaves f + variableLeaves g
  | .mul f g => variableLeaves f + variableLeaves g

def leafCount : Formula ι R → ℕ
  | .var _ => 1
  | .const _ => 1
  | .add f g => leafCount f + leafCount g
  | .sub f g => leafCount f + leafCount g
  | .mul f g => leafCount f + leafCount g

def internalGateCount : Formula ι R → ℕ
  | .var _ => 0
  | .const _ => 0
  | .add f g => internalGateCount f + internalGateCount g + 1
  | .sub f g => internalGateCount f + internalGateCount g + 1
  | .mul f g => internalGateCount f + internalGateCount g + 1

def vertexCount : Formula ι R → ℕ
  | .var _ => 1
  | .const _ => 1
  | .add f g => vertexCount f + vertexCount g + 1
  | .sub f g => vertexCount f + vertexCount g + 1
  | .mul f g => vertexCount f + vertexCount g + 1

end Formula

inductive RationalFormula (ι : Type u) (R : Type v) where
  | var : ι → RationalFormula ι R
  | const : R → RationalFormula ι R
  | add : RationalFormula ι R → RationalFormula ι R → RationalFormula ι R
  | sub : RationalFormula ι R → RationalFormula ι R → RationalFormula ι R
  | mul : RationalFormula ι R → RationalFormula ι R → RationalFormula ι R
  | div : RationalFormula ι R → RationalFormula ι R → RationalFormula ι R

namespace RationalFormula

variable {ι : Type u} {R : Type v}

noncomputable def eval [Field R] :
    RationalFormula ι R → FractionRing (MvPolynomial ι R)
  | .var i =>
      algebraMap (MvPolynomial ι R) (FractionRing (MvPolynomial ι R))
        (MvPolynomial.X i)
  | .const c =>
      algebraMap (MvPolynomial ι R) (FractionRing (MvPolynomial ι R))
        (MvPolynomial.C c)
  | .add f g => eval f + eval g
  | .sub f g => eval f - eval g
  | .mul f g => eval f * eval g
  | .div f g => eval f / eval g

inductive Valid [Field R] : RationalFormula ι R → Prop where
  | var (i : ι) : Valid (.var i)
  | const (c : R) : Valid (.const c)
  | add {f g : RationalFormula ι R} : Valid f → Valid g → Valid (.add f g)
  | sub {f g : RationalFormula ι R} : Valid f → Valid g → Valid (.sub f g)
  | mul {f g : RationalFormula ι R} : Valid f → Valid g → Valid (.mul f g)
  | div {f g : RationalFormula ι R} :
      Valid f → Valid g → eval g ≠ 0 → Valid (.div f g)

def variableLeaves : RationalFormula ι R → ℕ
  | .var _ => 1
  | .const _ => 0
  | .add f g => variableLeaves f + variableLeaves g
  | .sub f g => variableLeaves f + variableLeaves g
  | .mul f g => variableLeaves f + variableLeaves g
  | .div f g => variableLeaves f + variableLeaves g

def leafCount : RationalFormula ι R → ℕ
  | .var _ => 1
  | .const _ => 1
  | .add f g => leafCount f + leafCount g
  | .sub f g => leafCount f + leafCount g
  | .mul f g => leafCount f + leafCount g
  | .div f g => leafCount f + leafCount g

def internalGateCount : RationalFormula ι R → ℕ
  | .var _ => 0
  | .const _ => 0
  | .add f g => internalGateCount f + internalGateCount g + 1
  | .sub f g => internalGateCount f + internalGateCount g + 1
  | .mul f g => internalGateCount f + internalGateCount g + 1
  | .div f g => internalGateCount f + internalGateCount g + 1

def vertexCount : RationalFormula ι R → ℕ
  | .var _ => 1
  | .const _ => 1
  | .add f g => vertexCount f + vertexCount g + 1
  | .sub f g => vertexCount f + vertexCount g + 1
  | .mul f g => vertexCount f + vertexCount g + 1
  | .div f g => vertexCount f + vertexCount g + 1

end RationalFormula

noncomputable def permanentPolynomial (n : ℕ) :
    MvPolynomial (Fin n × Fin n) ℂ :=
  (Matrix.mvPolynomialX (Fin n) (Fin n) ℂ).permanent

theorem permanent_divisionFree_formula_lower_bound
    {n : ℕ} (hn : 32 ≤ n)
    (f : Formula (Fin n × Fin n) ℂ)
    (hf : Formula.eval f = permanentPolynomial n) :
    (n : ℝ) ^ 4 / (128 * Real.logb 2 (n : ℝ)) ≤
        (Formula.variableLeaves f : ℝ) ∧
    (n : ℝ) ^ 4 / (128 * Real.logb 2 (n : ℝ)) ≤
        (Formula.leafCount f : ℝ) ∧
    (n : ℝ) ^ 4 / (128 * Real.logb 2 (n : ℝ)) ≤
        (Formula.vertexCount f : ℝ) ∧
    (n : ℝ) ^ 4 / (256 * Real.logb 2 (n : ℝ)) ≤
        (Formula.internalGateCount f : ℝ) := by
  sorry

theorem permanent_rational_formula_lower_bound
    {n : ℕ} (hn : 32 ≤ n)
    (f : RationalFormula (Fin n × Fin n) ℂ)
    (hvalid : RationalFormula.Valid f)
    (hf : RationalFormula.eval f =
      algebraMap (MvPolynomial (Fin n × Fin n) ℂ)
        (FractionRing (MvPolynomial (Fin n × Fin n) ℂ))
        (permanentPolynomial n)) :
    (n : ℝ) ^ 4 / (192 * Real.logb 2 (n : ℝ)) ≤
        (RationalFormula.variableLeaves f : ℝ) ∧
    (n : ℝ) ^ 4 / (192 * Real.logb 2 (n : ℝ)) ≤
        (RationalFormula.leafCount f : ℝ) ∧
    (n : ℝ) ^ 4 / (192 * Real.logb 2 (n : ℝ)) ≤
        (RationalFormula.vertexCount f : ℝ) ∧
    (n : ℝ) ^ 4 / (384 * Real.logb 2 (n : ℝ)) ≤
        (RationalFormula.internalGateCount f : ℝ) := by
  sorry

end PermanentFormulaLowerBound
