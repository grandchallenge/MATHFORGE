# OAI26 Family 011 — explicit analytic-to-Lean supply reduction

**Disposition:** `PARAMETER_BRIDGE_MATHEMATICAL_DERIVATION_NONCERTIFYING`. The finite pigeonhole-to-infinitude implication is already Lean-checked in PR #544. This note identifies precisely what must be obtained from the *separate, unverified* smooth-shifted-prime asymptotic in the pinned manuscript. This is a conditional mathematical reduction, **not** a Lean formalization of the prime-count asymptotic and not a proof that the asymptotic is true.

## Immutable source and theorem

- `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
- Manuscript: `preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/00-introduction.tex`, blob `3d9d4c55c1f30d7736e7c7427b97cb0461f06040`. The manuscript **asserts**, for each fixed `0<δ<1/4`, a count of primes `2x<p≤5x` with `P⁺(p-1)≤x^δ` of at least `x^(1-o(1))` as `x→∞`. Its `o(1)` is allowed to depend on fixed `δ`, but no uniformity as `δ→0` is claimed.
- Lean baseline: `lean/OAI/NumberTheory/TotientFibers/FiniteFiber.lean`, blob `217cfe4d7f9c39981eabe9bbeeb8458febb0fc76`. `finite_large_fiber_rpow` explicitly assumes `5≤a≤t`, `ε≤1`, `4≤a ε`, prime/smoothness/size bounds and `t^(a-1)<|P|`. `infinite_of_unbounded_g` supplies the infinitude step.
- New conditional theorem in protected MATHFORGE PR #544, merge `8496b8c5f13df8f31954f13f99b4267c64e8395e`: `GCL.OAI26.Family011.infinite_fibers_of_supply` from the explicit hypothesis `PrimeSupplyForExponent ε`. No unconditional prime-supply theorem was proved there.

## Exact parameter choice

Fix `0<ε≤1`. Choose an **integer** `a≥6` such that `a ε≥4`; choosing `a=max(6,⌈4/ε⌉)` works. Define the **fixed** real exponent

```
δ = (2a-1) / (2a(a-1)).
η = 1/(4a).
```

Then, exactly,

```
0 < δ < 1/4,
aδ = 1 + 1/(2(a-1)) > 1,
(a-1)δ = 1 - 1/(2a) = 1 - 2η < 1-η.
```

Since `a` and `δ` are held fixed as `x→∞`, the manuscript's asserted lower bound can be read in the precise form: for any fixed `η>0`, eventually the number of counted primes is **at least** `x^(1-η)`. This inference uses the asserted `x^(1-o(1))` theorem, not independent verification.

For sufficiently large real `x`, define `t=⌈x^δ⌉` (an integer), and let `P` consist of all primes satisfying the source theorem's bounds. The following hold eventually:

1. `t≥T` for any previously specified threshold `T`, and `5≤a≤t`.
2. `p≤5x≤t^a`: because `t≥x^δ` and `aδ>1`.
3. Every prime divisor `q | (p-1)` has `q≤P⁺(p-1)≤x^δ≤t`.
4. `t^(a-1)≤(x^δ+1)^(a-1)<x^(1-η)≤|P|` for all sufficiently large `x`. The strict middle inequality uses `(a-1)δ=1-2η` and the positive exponent gap `η`.

Thus, **conditional on the manuscript's asserted prime-count estimate**, `PrimeSupplyForExponent ε` follows for each fixed `0<ε≤1`. This supplies exactly the hypothesis of the Lean-checked `infinite_fibers_of_supply`, yielding infinitely many `n>0` with `g(n)>n^(1-ε)`. For `ε≥1`, the pre-existing pinned Lean theorem `totient_large_fibers_of_one_le` already covers the exponent range.

## Adversarial gates

- Do **not** choose `δ=1/a`; then `t^a` need not dominate `5x`.
- Do **not** choose `δ≥1/(a-1)`; then `t^(a-1)` need not stay below an `x^(1-o(1))` count.
- Do **not** let `δ=δ(x)→0` without uniformity; the manuscript only claims a fixed-`δ` asymptotic.
- Do **not** replace `p-1` smoothness by smoothness of `p`, or conflate `p≤5x` with `p≤x`.
- Do **not** infer an unconditional theorem from a manuscript assertion before independently validating its analytic proof.
- Do **not** treat this explanatory derivation or its deterministic arithmetic tests as kernel-checked formalization of the asymptotic.

## Remaining formal and critical obligations

1. State the fixed-`δ` prime-count assertion as an explicit Lean hypothesis/predicate, with quantified eventual bound `∀η>0,∀ᶠ x, x^(1-η)≤card P(x,δ)` and exact prime/predecessor definitions.
2. Formalize the parameter selection and count-to-`PrimeSupplyForExponent` implication in Lean 4.34.1, preserving source and manifest pins.
3. Independently assess the primary manuscript's **analytic proof** of the prime-count assertion and mathematical literature. That analytic assertion is a substantive external input, not something proved by this note.
4. Execute critical/negative checks, compare source semantics, and admit any formal bridge through normal protected review; reserve MATHCERT certification for its own process.

**Claim boundary:** conditional deduction from a source assertion, not independent proof of that assertion, not full semantic correspondence certification.
