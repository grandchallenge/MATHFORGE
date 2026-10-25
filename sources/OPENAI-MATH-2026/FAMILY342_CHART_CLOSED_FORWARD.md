# Family 342: upstream closedness implies chartwise exterior closedness

**Work package:** `MF-OAI-MATH-2026-F342-SEM-010`  
**Protected predecessor:** `grandchallenge/MATHFORGE@ff3b9bebff2007f3ac18883d99c94195562046f2`  
**Upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Kernel and mathlib:** Lean 4.34.1 and `d13f23b723b8a846827a245b89c10fc7d3f11612`.

The exact upstream `IsClosed α` tests every globally defined smooth `F:Space→X` on each open domain `U`, requiring `extDerivWithin (pullback α F) U y=0` at every `y∈U`.

The new formal theorem candidate `gcl_isClosed_implies_chartwise` proves, for each chart `chartAt Space x`, that every target point `y` satisfies

```lean
extDerivWithin (pullback α (chartAt Space x).symm)
  (chartAt Space x).target y = 0
```

assuming only upstream `IsClosed α`, not a new regularity axiom. The proof selects the source-locked smooth global inverse-chart extension of #324, uses derivative and raw two-form pullback locality from #325 to identify coefficients on the inner ball, and transfers `extDerivWithin` between the inner open ball and full chart target using `fderivWithin_of_mem_nhds`.

This result is **not admitted until** the exact-head `semantic-342` replay succeeds with a permitted-axiom record and no `sorryAx`. The workflow retains and hashes the GCL source proofs and the generated composite module.

Successful admission closes the **forward implication** of SEM-342-02 as a theorem about upstream raw forms. The full intrinsic equivalence additionally requires chartwise-to-universal `IsClosed`, the converse `IsSmooth`, and correspondence of the source's coordinate `extDerivWithin` to intrinsic exterior derivative on smooth forms. SEM-342-04 manifold hypotheses equivalence remains open. No `SOURCE_LOCKED` assurance promotion, manuscript certification or MATHCERT claim is authorized.
