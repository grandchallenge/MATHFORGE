# OAI-26 WP03 — Family 003: pinned seven-eighths semantic audit

**Record:** `GCL-OAI26-WP03-F003-SEVEN-EIGHTHS/1`  
**Result:** `PROPOSITION_LEVEL_ALIGNMENT` for the **zeta and Dirichlet subclaims** of the September 30 manuscript; **NOT** a full-family verdict, Lean replay, paper-proof verification, or MATHCERT certification.  
**Crosswalk:** MATHFORGE `sources/OPENAI-MATH-2026/FORMALIZATION_CROSSWALK.json` (Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`), Family index `MANUSCRIPT_INDEX.json` (blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`).  
**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.  
**Review scope:** source/static, September 30 7/8 paper edition and named formal declarations only. No new compiler execution.

## Exact source and provenance

- Manuscript: `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf`. Original upstream Git blob SHA-1 `8132b77eeb270a70b25df8d6609f008e83e65d91`. Read as an actual **199-page PDF**, 1,588,969 bytes; locally rederived Git blob SHA-1 **matches**; PDF SHA-256 `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`. The PDF was fetched read-only from the pinned GitHub raw object; static extraction used `pypdf`. Original bytes were not changed.
- Lean source: `lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean`, upstream Git blob `46c67f4000906b1391a471d6e6396ac0da3c16a5`, fetched at the exact commit.
- Comparator: `lean/ComparatorChallenges/QuasiRiemannHypothesis.json`, upstream Git blob `acf552468fc23c1a27d685d33983c58c50040542`. Its only `theorem_names` entry is `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`.
- Second Family 003 crosswalk entry: `lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean`, Git blob `9ed5a07a40ab668baa9b537d46fae0421dc47435`, declaration `OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap`. This is a different theorem about a uniform real-zero gap for primitive real Dirichlet characters and does not itself prove the seven-eighths half-plane claim.
- Other manuscript editions in Family 003 (not reviewed here): `preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf` and `preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf`. The scope of a *family-wide* judgement remains open.

## Direct mathematical statement comparison

**Manuscript evidence:** PDF page 4, Theorem 1.1, states that **every finite-order Hecke L-function over** `F = Q(sqrt(-3))` **and every Dirichlet L-function (including zeta)** is zero-free in the **strict** half-plane `Re(s) > 7/8`, permitting the principal character's pole at `s=1`. Pages 84–85 (Proposition 11.3) provide a named transfer from primitive Hecke to Dirichlet functions. Page 197 concludes the stated bound using this transfer. The abstract on PDF page 1 agrees on scope.

**Pinned Lean source:** the following two top-level declarations occur textually in `Nonvanishing.lean`:

```lean
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0 :=
  SevenEighths.ProbeFinalAssemblyUnconditional.dirichlet_nonzero
    q (NeZero.ne q) χ s hs hpole

theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0 :=
  SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero s hs
```

**Alignment established by static inspection:**

1. **Half-plane / quantifier:** `∀ s : ℂ, 7/8 < Re(s)` is explicit in the Lean `riemannZeta` declaration and agrees with the zeta consequence of Theorem 1.1. The boundary `Re(s)=7/8` is excluded in both.
2. **Dirichlet scope:** Lean quantifies all natural moduli with `NeZero q`, all characters `χ`, and complex `s` in the strict half-plane, excluding exactly `χ=1 ∧ s=1` at the declaration level. This corresponds at the surface statement level to the manuscript's principal pole allowance. Formal identification of all character and L-function conventions is **not yet proved**.
3. **Hecke scope gap:** Theorem 1.1 has a Hecke-`F` universal quantifier. Neither top-level declaration in the inspected `Nonvanishing.lean` file states this Hecke claim. The **configured comparator checks only the zeta declaration**. Hence a passing comparator cannot, merely by its theorem list, validate the full scope of Theorem 1.1. Imported modules may establish additional Hecke facts, but that must be checked separately; absence from this one module is not evidence of mathematical falsity.
4. **Proof dependencies:** `Nonvanishing.lean` imports `OAI.NumberTheory.DirichletL.Foundation` and `OAI.NumberTheory.DirichletL.Detector.FinalAssemblyUnconditional`; the declarations invoke `SevenEighths.ProbeFinalAssemblyUnconditional.dirichlet_nonzero` and `.zeta_nonzero`. The imported proof bodies, source-to-paper analytic arguments, complete dependency closure, and axiom report have **not** been independently checked in this review. The comparator allows `propext`, `Quot.sound`, `Classical.choice`, but this is **configuration**, not a measured axiom report.
5. **Edition scope:** the paper's September 30 claim and the specifically indexed Lean declaration align in conclusion and major explicit hypotheses. No conclusion follows about the October 5 alternate 11/12 paper or the October 1 Siegel-zero paper from this inspection.

## Positive and falsifying witnesses

- **Positive witness:** exact PDF page 4 Theorem 1.1 explicitly includes the zeta consequence for all `Re(s)>7/8`; exact Lean declaration `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` has precisely that strict numeric inequality and nonvanishing conclusion.
- **Falsifying scope witness:** PDF page 4 asserts nonvanishing for every finite-order Hecke `L_F(s,eta)` over `Q(sqrt(-3))`, while the *sole comparator-listed declaration* is zeta-specific. Therefore `COMPARATOR_PASS => FULL_MANUSCRIPT_THEOREM_VERIFIED` is unjustified even if Lean replay later succeeds.
- **Scope countercheck:** `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re` is broader than the configured comparator's single zeta theorem but is still a Dirichlet, not the manuscript's full Hecke-family statement.

## Disposition and further concrete mathematical checks

`PROPOSITION_LEVEL_ALIGNMENT` — **source-derived, September 30 zeta/Dirichlet component only**. `FULL_SEMANTIC_MATCH_PROVED` is withheld. The *family-wide* twelve-pilot slot is `UNRESOLVED` until other editions and dependency/definition bridges are checked.

Next checks, without reopening CONTROL #79: (a) inspect and source-pin the exact Hecke-family Lean declaration if one exists, including the transfer to Dirichlet L-functions; (b) prove or document definitions/model bridges for the manuscript's finite-order Hecke characters and Lean's characters; (c) replay exact Lean declarations and axioms under the pinned toolchain and manifest in WP01; (d) review both other Family 003 manuscript editions; (e) obtain a distinct non-authoring critical pass before any full-semantic claim. These are **genuine proof-verification obligations**, not infrastructure prerequisites for the present static finding.

**Evidence boundary:** No mathematical correctness of the 199-page analytic argument, no successful Lean compile, no full paper-to-Lean correspondence, no MATHCERT promotion.

## Reproduction

Read GitHub blob `8132b77eeb270a70b25df8d6609f008e83e65d91` from the pinned upstream commit, verify `sha1(b"blob " + len(data).encode() + b"\\0" + data)` equals that Git blob, then extract PDF pages 1, 4, 84–85 and 197. Fetch the exact two Lean files and comparator JSON from the same pinned commit. Compare the explicit quantifier domains, strict inequality, pole exception, theorem target and comparator-listed declaration. This requires no CONTROL supervisor or mathematical certificate and is independently auditable.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F003-SEP30
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: PROPOSITION_LEVEL_ALIGNMENT; FAMILY_WIDE_UNRESOLVED
EVIDENCE: PDF Git blob 8132b77eeb270a70b25df8d6609f008e83e65d91; Lean blob 46c67f4000906b1391a471d6e6396ac0da3c16a5; comparator blob acf552468fc23c1a27d685d33983c58c50040542
REPLAY: STATIC_SOURCE_INSPECTION_ONLY; NO_LEAN_REPLAY
UNRESOLVED: full Hecke declaration bridge; definitions/axioms; alternate Family 003 editions; formal independent critique
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
