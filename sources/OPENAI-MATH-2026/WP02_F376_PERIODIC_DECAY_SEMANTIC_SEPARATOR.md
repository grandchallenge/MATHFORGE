# Family 376 — exact periodicity versus quantitative decay

**Record:** GCL-OAI26-WP02-F376-SEM-PERIODIC-DECAY/1  
**Upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Scope:** A mathematical entailment check across pinned Lean theorem predicates and the October 6 manuscript revision. This is **not** a complete import-closure audit or a certification of manuscript/formalization equivalence.

## Direct source evidence

1. `lean/OAI/MathematicalPhysics/NavierStokes/BalancedTransport/MainResult.lean`, theorem `OAI.BalancedTransport.balanced_three_stack_realization`, explicitly supplies `BoundedMixed (U M w)`, `PeriodicAfterOne (U M w)`, and `∀ t, 1 ≤ t → ∀ x, U M w t x = repeated M t x`. It also supplies `Function.Periodic (repeated M) 1` and bounded mixed derivatives of forces.
2. `lean/OAI/MathematicalPhysics/NavierStokes/BalancedTransport/FieldBounds.lean` defines `RepeatsAfter T v` as `∀ t, T ≤ t → v (t + 1) = v t` and proves `boundedMixed_of_compact_repeating` from smoothness, compact spatial support, and eventual repetition. In this proof the bounding constant is obtained on a **compact time interval** and propagated by periodicity. It is not an asymptotic decay rate.
3. `lean/OAI/MathematicalPhysics/NavierStokes/BalancedTransport/Periodic.lean` proves `loadedRepeat_repeats` and `repeatTemplate_zero_period`. These supply the periodicity used by the main theorem.
4. The already protected source-delta ledger `sources/OPENAI-MATH-2026/WP02_F376_TEX_REVISION_DELTA.json` records an additional October `clocks.tex` inequality for a **slow profile** `U_{α1}` and `f_{α1}`: derivatives bounded by `C_(h,r) (1+t)^(-1-h)`. The paper's quantities `U_{α1}` and `f_{α1}` must **not** silently be identified with the Lean theorem's `U M w` and `f`.

## Mathematical separator lemma

**Proposition.** Let `u : [T,∞) → V` take values in a normed vector space, with `u(t+1)=u(t)` for all `t≥T`. Suppose `∥u(t)∥≤C(1+t)^(-a)` for all `t≥max(T,0)`, with `C≥0` and `a>0`. Then `u(t)=0` for all `t≥max(T,0)`.

**Proof.** Fix `t≥max(T,0)`. By induction on `n∈ℕ`, periodicity gives `u(t+n)=u(t)`. Consequently, `0≤∥u(t)∥≤C(1+t+n)^(-a)` for every `n`. The right-hand side tends to zero as `n→∞`; thus `∥u(t)∥=0` and `u(t)=0`. ∎

The same proposition applies pointwise in space and to any time derivative that is eventually periodic and obeys such decay. It shows that **a nontrivial eventually periodic field cannot itself satisfy global positive-power time decay**. Conversely, eventual periodicity plus boundedness does not imply the October clock-decay estimate: the constant nonzero scalar function is a counterexample to that implication.

## Semantic disposition

- **Established:** The pinned main Lean theorem proves eventual repetition and uniform boundedness of mixed derivatives, not a specified `(1+t)^(-1-h)` rate in its displayed conclusion.
- **Established:** If the paper's slow profile were proven to be the same nonzero field as the eventual periodic Lean velocity, an unrestricted decay estimate for that same field would be incompatible with eventual repetition. This is a **conditional separator**, not a discovered contradiction.
- **Unresolved:** Whether `U_{α1}` is a distinct slow/profile component of the construction, how it maps to Lean definitions, and whether imported lemmas formalize the October clock inequality or projected-force/pressure bounds under other names.
- **Not claimed:** No proof that the October paper is wrong; no conclusion that the entire Lean import closure lacks the new estimates; no formal Lean proof of the separator lemma; no certification.

## Next concrete proof obligation

Construct an explicit source-to-source mapping of the October `U_{α1}, f_{α1}` and projected `Pg,Qg,p−φ` to the pinned Lean definitions. Trace the imports used by `balanced_three_stack_realization` and inspect the actual hypotheses/conclusions of any mapped lemmas. Either locate the rate with exact statement and source line or record the smallest verified missing bridge. The mapping must be completed before asserting formal coverage or a manuscript-level mismatch.
