# WP03 — Family 008: Deligne–Drinfeld principal theorem concordance

**Pinned source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Decision:** `PROPOSITION_LEVEL_ALIGNMENT`, not full semantic equivalence or mathematical certification.

## What the manuscript says

The September 23, 2026 *The Deligne–Drinfeld conjecture* manuscript (pinned `paper.pdf` Git blob `0aa3328661d35567ec7e2dfb802b0351003e7a31`, 41 pages, SHA-256 `5ae63f326803a634e7c6dc5684ce7062ea0ac6940a88a75c7052875382dbc762`) defines the rational free Lie algebra on two letters and a solution space `W` via **antisymmetry, the three-term relation and the four-strand pentagon**. It uses the Ihara bracket `D_ψ(φ) − D_φ(ψ) + [ψ,φ]`, with `D_ψ(x)=0` and `D_ψ(y)=[y,ψ]`.

**Theorem 1.1 on PDF page 2** asserts homogeneous generators of weights 3, 5, 7, … forming a graded rational free Lie algebra isomorphic to `W` under the Ihara bracket. It includes closure under that bracket and a continuous graded isomorphism of weight completions. The final proof on PDF page 40 uses independent Hall-word images plus a dimension squeeze to obtain freeness and surjectivity, then extends the resulting isomorphism degreewise to the completions.

The manuscript also discusses the graph-complex consequence `H⁰(GC₂)`, relying on an external comparison, and regularized transport. Those applications are not part of the selected Comparator target, and are **not admitted** here.

## What the Lean theorem states

`lean/OAI/Algebra/Drinfeld/Completion.lean` at Git blob `98a996a90f4f57a205a3e3e8673a8528e8e3dbbf` ends with the actual proof

```lean
theorem main : MainStatement :=
  CategoricalValues.main_of_oddSolutions odd_solution
```

`MainStatement`, defined in `lean/OAI/Algebra/Drinfeld/Foundations.lean` (Git blob `04320b5982c12c9d638b6f7119f6e83c69ca6c13`), requests a graded `ℚ`-linear equivalence between `OddFree` and `W`, preservation of the Ihara bracket, mutually inverse completion maps, continuity in both directions, and a componentwise bracket compatibility identity. `oddWeight k = 2*k+3` corresponds precisely to odd weights starting at 3.

The source `IsSolution` predicate contains the two-term relation, three-term relation and four-strand pentagon in the braid quotient `T4`. The source and Comparator challenge definitions were compared after whitespace normalization for `IsSolution`, `MainStatement`, `oddWeight` and `Graded`: **all four exact text matches**. This supports the selected theorem-level correspondence but does not prove the manuscript's external definitions, topology or imported objects are semantically identical to the formal model.

The challenge `lean/ComparatorChallenges/DeligneDrinfeld.lean` has a `sorry` placeholder. It is *not* the actual solution proof. The config `DeligneDrinfeld.json` selects exactly `OAI.DeligneDrinfeld.main` with solution module `OAI.Algebra.Drinfeld.Completion`.

## Evidence provenance and limitations

This theorem is entry **38 (zero-based)** in the separate 200-main-result declaration register. Previously protected WP01 corpus ledger `CORPUS_25_89_LEAN_RECEIPT_LEDGER.json` (Git blob `530e9a65b37345957f29049b5b24353f0fe8887d`) records source-pinned Lean build and axiom audit passing at workflow run `40490625900`, observed `Classical.choice`, `Quot.sound`, `propext` and no extra axioms. The current transaction **did not perform** another build or actual Comparator execution, and those earlier receipts do not certify the paper.

The declaration register's `family_binding` remains `UNRECONCILED`. The manuscript index for family `008`, `lean/docs/008.md`, selected Comparator and proof file independently support this **case-level manual mapping**; the raw 200-entry register was not silently altered.

A separate nonauthoring **logical critic** examined likely overclaims: source/challenge equivalence is not paper/model equivalence; the main proof is not a graph-complex formalization; closure under Ihara follows from the graded equivalence and bracket preservation but a full mathematical bridge remains unproven; generic module names do not confer certification; a successful Lean compile does not imply a Comparator pass. No independent authenticated external reviewer or reserved certification role is claimed.

## Bounded disposition

**Family 008 principal theorem:** `PROPOSITION_LEVEL_ALIGNMENT`. Main formula, equation constraints, generator weights, bracket convention, and completion *statement* exhibit direct correspondence to the pinned manuscript.

**Unresolved:** exact model/definition bridge and dependency proof correspondence, external graph-complex consequence, actual Comparator acceptance, full mathematical certification. WP03's twelve-family first pilot is **not** completed by this one case.

Machine-readable details, exact source Git blobs, ten-source hash pins, provenance and hostile controls are in `WP03_FAMILY008_DELIGNE_DRINFELD_SEMANTIC_REVIEW.json` and `tests/test_openai_math_wp03_family008.py`.
