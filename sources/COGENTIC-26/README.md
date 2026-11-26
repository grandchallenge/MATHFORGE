# COGENTIC-26 source intake

Issue: grandchallenge/MATHFORGE#616. Scope: six new papers, four prior papers retained for collection context. Source-lock only; no mathematical certification, novelty adjudication or successor campaign admission.

The original and latest collection revisions are pinned in SOURCE_LOCK.json. All 42 files were acquired on CHAD and each Git blob SHA-1 independently recomputed from bytes; SHA-256 and sizes retained. Source bytes remain in the CHAD intake cache and at the immutable upstream URLs. Capture: 0c4c4925ed5c4ba48f1dc7a1df125112 (local execution, not independent replay). The six new papers declare CC BY 4.0 in their individual descriptions; the collection default Apache 2.0 does not override those declarations. Do not infer earlier-paper licensing from this.

## Provider-attributed claims and route triage

| Source directory | Reported result | Candidate GCL route | Verification obligation |
|---|---|---|---|
| integer_factorization | Unconditional randomized zero-error expected subexponential factoring with L exponent 1/3; constant 105 | Computational complexity atlas; arithmetic | Check uniform bit model, expected-time estimate, absence of unproved hypotheses |
| deterministic_factoring_l34 | Deterministic factoring with L exponent 3/4; subexponential quadratic nonresidue construction | Computational complexity atlas; arithmetic | Separate deterministic bounds and output specifications |
| discrete_logarithm | Fixed-characteristic finite-field discrete logarithms in sub-quasipolynomial expected time | Computational complexity atlas; arithmetic | Check field presentation, fixed-characteristic quantification and zero-error subgroup certificate |
| bimatrix_nash_equilibrium | Deterministic polynomial-time rational strategy with regret at most 1/5 | Complexity atlas; agency/game theory | Check rational bit complexity and revised prior-art baseline; not exact Nash equilibrium |
| logrank_conjecture | Deterministic communication upper bound with rank exponent 1/2 minus 0.000005 | Complexity atlas; PNP-ABOVE/SCC comparator | Check biased KL-stability obstruction and rank-to-communication transfer; not full log-rank conjecture or a P vs NP lower bound |
| edge_reconstruction | Edge-deleted deck determines finite simple graph at m >= 1000 n | Graph theory; relational identifiability | Check density hypothesis and deck equivalence; not unrestricted conjecture |

These are normalized from the provider descriptions, not independent PDF theorem/proof concordance. No Lean files were present at either pinned revision; Google reports complete Mathlib-only formalizations with release deferred. Require exact Lean files/toolchain/dependencies, declaration-level statement and axiom audit, independent replay, and mathematical source concordance before any MATHCERT promotion. Prior-art verification remains open. No active Programme domain is created here.
