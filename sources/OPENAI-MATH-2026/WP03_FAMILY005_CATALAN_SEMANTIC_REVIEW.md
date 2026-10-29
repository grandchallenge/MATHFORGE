# WP03 — Family 005: Catalan's constant, narrow theorem-semantic review

**Disposition:** `PROPOSITION_LEVEL_ALIGNMENT` (bounded).  
**Source lock:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.  
**Machine-readable evidence:** `WP03_FAMILY005_CATALAN_SEMANTIC_REVIEW.json`.

## Statement comparison

The pinned September 24, 2026 *Catalan's constant is irrational* manuscript (PDF Git blob `ecbe60eb89d2d25c1d07da6232f8d9869e6c0c1d`, SHA-256 `4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e`, 44 pages) defines the constant as the alternating sum over nonnegative integers of `(-1)^j/(2j+1)^2`. Its Theorem 1.1 on PDF page 1 states that this constant is irrational.

The actual formalized theorem, in `lean/OAI/NumberTheory/Catalan/Results/Conclusions.lean` (Git blob `a21cbc0e56a4e71ec21ce765b16e6ef0adb864f0`), is

```lean
theorem catalan_irrational :
    Irrational (∑' j : ℕ, (-1 : ℝ) ^ j / ((2 * j + 1 : ℕ) : ℝ) ^ 2) := by
```

This expression has the same signs, denominator, exponent, index range, and conclusion as the displayed manuscript result. Neither displayed principal statement requires additional assumptions. The actual proof body applies a rationality contradiction, nonvanishing prime-scale determinants, and competing finite- and real-place bounds. The manuscript's conclusion on PDF page 42 similarly derives a contradiction from finite-place and real-place estimates. This is a **statement- and broad-proof-strategy alignment**, not a proof that each dependency or mathematical object is definitionally equivalent.

The pinned `lean/ComparatorChallenges/Catalan.json` (Git blob `78b89138b45ecbe09c061b25c2e2f6177ffd4b9b`) selects `OAI.InternalCatalan.catalan_irrational` in solution module `OAI.NumberTheory.Catalan.Main`. The challenge file (Git blob `f7941ef960ec9d0ec745f15f2ee7b2ff46bd6058`) contains the same proposition and a `sorry` placeholder. The separate solution proof file contains no `sorry` token. No actual Comparator replay or complete imported-axiom audit is asserted here.

## Exact scope restrictions and adversarial reading

The PDF conclusion goes on to infer irrationality of particular hyperbolic three-manifold and arithmetic-orbifold volumes. These geometric consequences are **not covered by the selected Comparator theorem**. The central proposition cannot stand in for their source-semantic acceptance.

The upstream source tree contains modules with names such as `ManuscriptCaseOneX4SubstitutionError`. An error-*bound* lemma name alone neither refutes the manuscript nor proves that its numeric certificate has been wholly reviewed. A complete imported-definition/model bridge, proof-body audit, numerical certificate comparison and independent literature check remain outstanding.

Family 005 appears in the 372-family `MANUSCRIPT_INDEX.json` with one pinned PDF. Neither this theorem nor manuscript is listed in the separate 200-main-result / 173-source-paper formalization crosswalk. That distinction does **not** mean no formalization exists: the pinned `lean/docs/005.md`, actual Lean proof and Comparator config explicitly exist. It means the WP01 200-declaration replay receipts cannot be applied automatically to this theorem.

An independent *logical* nonauthoring critic check was performed within the same authenticated system; no separate human/agent login or reserved MATHCERT authority is claimed. Deliberate hostile fixtures test changed series, forged theorem/source, unearned Comparator success, hidden imported-axiom claims and false closure of the 12-family pilot.

## Terminal boundary for this work unit

**Family 005 principal-statement inspection: complete.** WP03's twelve-family pilot and later stratified semantic cohorts: **open**. The next source-semantic obligation is to verify the other required pilot families, not to repeat this same source inspection. No full semantic-equivalence proof, mathematical truth finding, certification or novelty determination is asserted.
