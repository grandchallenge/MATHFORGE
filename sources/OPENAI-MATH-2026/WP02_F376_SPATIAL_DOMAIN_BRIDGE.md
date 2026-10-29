# Family 376: spatial-domain and norm bridge

**Source lock:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`. This is a bounded semantic inspection, not certification.

## Exact pinned definitions

`lean/OAI/MathematicalPhysics/NavierStokes/BalancedTransport/Model.lean` sets `Space := Fin 3 → ℝ`, `Field F := ℝ → Space → F`, `Velocity := Field Space`, and `Pressure := Field ℝ`. Its `BoundedMixed` predicate gives, for every mixed derivative index, **some time-independent bound** valid for every nonnegative time and every spatial point. It specifies no decay exponent, no projection on a torus, and no Fourier cutoff.

`BalancedTransport/MainResult.lean` proves `balanced_three_stack_realization` for a machine-indexed `Family Velocity`, with `BoundedMixed`, eventual repetition, and other physical/computational properties. `BalancedTransport/FieldBounds.lean` obtains mixed-derivative boundedness from compact spatial support and eventual repetition. These are precise facts about that Euclidean-space model; `Pressure` is a type alias, not an assertion of a projected pressure formula.

The protected source comparison `WP02_F376_TEX_REVISION_DELTA.json` attributes to the October 6 manuscript an **effective torus Hodge/Poisson decomposition** `Qg=∇φ`, `Pg=g−Qg`, pressure adjustment `p−φ`, and explicit Sobolev-to-`C^r` and time-decay estimates. `WP02_F376_PERIODIC_DECAY_SEMANTIC_SEPARATOR.md` already shows why bounded eventual-periodic motion is not interchangeable with power-law decay of a slow profile.

## New minimal bridge obligation

A faithful coverage claim for these **added quantitative estimates** requires an explicit mapping (or separate formal realization) of the paper's torus domain and projected fields to pinned Lean objects, specifying the period lattice, spatial mean-zero condition, Poisson solution or Fourier projection, Sobolev norms, regularity indices and constants, time-derivative commuting properties, and the meaning of the paper's `U_{α1}`, `f_{α1}` versus the theorem's `U M w`, `f`.

The type `Fin 3 → ℝ` alone does **not** establish that the paper's torus projection is formalized. Nor does its use preclude a torus-periodic construction elsewhere: the quotient/periodization dictionary and imported definitions have not been exhaustively reviewed.

## Logical assessment

- **Proved by source inspection:** The displayed `BoundedMixed` predicate is uniform boundedness, not quantitative decay; the stated `Space` is an ordinary real-coordinate space, not a quotient torus type.
- **Required but unverified:** An exact spatial-domain/projection/norm dictionary that transports the October estimates into relevant formal propositions.
- **Not concluded:** That such a dictionary does not exist in the full import closure, that the paper is inconsistent, or that the formal theorem fails.

Next, trace the specific manuscript `Pg,Qg,φ,U_{α1},f_{α1}` definitions into formal source names and verify each transport identity and estimate, with exact theorem references or an explicit missing-bridge ledger.
