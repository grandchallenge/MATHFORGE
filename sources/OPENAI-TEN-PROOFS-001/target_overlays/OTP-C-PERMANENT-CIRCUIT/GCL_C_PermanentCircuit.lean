import Mathlib

namespace PermanentRollout

open scoped BigOperators

inductive Instruction (ι : Type) where
  | input (i : ι)
  | scalar (c : ℂ)
  | add (left right : ℕ)
  | sub (left right : ℕ)
  | mul (left right : ℕ)

def Instruction.referencesBounded {ι : Type} (position : ℕ) : Instruction ι → Bool
  | .input _ => true
  | .scalar _ => true
  | .add left right => left < position && right < position
  | .sub left right => left < position && right < position
  | .mul left right => left < position && right < position

def Instruction.isArithmetic {ι : Type} : Instruction ι → Bool
  | .input _ => false
  | .scalar _ => false
  | .add _ _ => true
  | .sub _ _ => true
  | .mul _ _ => true

noncomputable def Instruction.eval {ι : Type}
    (values : Array (MvPolynomial ι ℂ)) : Instruction ι → MvPolynomial ι ℂ
  | .input i => MvPolynomial.X i
  | .scalar c => MvPolynomial.C c
  | .add left right => values.getD left 0 + values.getD right 0
  | .sub left right => values.getD left 0 - values.getD right 0
  | .mul left right => values.getD left 0 * values.getD right 0

structure ArithmeticCircuit (ι : Type) where
  program : List (Instruction ι)
  output : ℕ
  output_lt : output < program.length
  valid : ∀ position : Fin program.length,
    (program.get position).referencesBounded position.val

noncomputable def ArithmeticCircuit.values {ι : Type}
    (circuit : ArithmeticCircuit ι) : Array (MvPolynomial ι ℂ) :=
  circuit.program.foldl
    (fun values instruction => values.push (instruction.eval values)) #[]

noncomputable def ArithmeticCircuit.polynomial {ι : Type}
    (circuit : ArithmeticCircuit ι) : MvPolynomial ι ℂ :=
  circuit.values.getD circuit.output 0

def ArithmeticCircuit.size {ι : Type} (circuit : ArithmeticCircuit ι) : ℕ :=
  (circuit.program.filter Instruction.isArithmetic).length

noncomputable def circuitComplexity {ι : Type} (f : MvPolynomial ι ℂ) : ℕ :=
  sInf {size : ℕ | ∃ circuit : ArithmeticCircuit ι,
    circuit.polynomial = f ∧ circuit.size = size}

noncomputable def permanent (n : ℕ) : MvPolynomial (Fin n × Fin n) ℂ :=
  Matrix.permanent (fun row column => MvPolynomial.X (row, column))

theorem permanent_circuit_loglog_lower_bound {n : ℕ} (hn : 2 ^ 16 ≤ n) :
    (n : ℝ) ^ 2 * (Real.logb 2 (Real.logb 2 (n : ℝ)) - 3) / 144 ≤
      (circuitComplexity (permanent n) : ℝ) := by
  sorry

theorem permanent_circuit_loglog_bigOmega :
    ∃ c : ℝ, 0 < c ∧ ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
      c * (n : ℝ) ^ 2 * Real.logb 2 (Real.logb 2 (n : ℝ)) ≤
        (circuitComplexity (permanent n) : ℝ) := by
  sorry

theorem permanent_complexity_ratio_tendsto_atTop :
    Filter.Tendsto
      (fun n : ℕ =>
        (circuitComplexity (permanent n) : ℝ) / (n : ℝ) ^ 2)
      Filter.atTop Filter.atTop := by
  sorry

end PermanentRollout
