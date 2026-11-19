# OAI-26 Family 003 — independent audit of analytic energy budgets, parameter scales, and uniformity

**Review assignment:** `GCL-OAI26-F003-ENERGY-SCHEDULE-AND-HEIGHT-UNIFORMITY/1`  
**Upstream source lock:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.  
**Proposed new evidence:** [exact-rational audit](f003_energy_scale_rational_audit.py).  
**Scientific disposition:** `ENERGY_SCHEDULE_ARITHMETIC_PASS__EXTREME_NONCOMPUTATIONAL_QUANTIFIERS_CONFIRMED__ANALYTIC_BOUND_VALIDITY_OPEN`.

## 1. Why this matters: verify the instrument, not just its final reading

The source's route to a zero-free strip is a *reductio*. Let `β` be the supremum of real parts of zeros over its Hecke-character family. Suppose `β > 7/8`. Its `PrimitiveContract` constructs an analytic factor `H(s)`, uniformly within distance `1/2` of `1`, and a detector `J(x)` satisfying

```
J(x) = O(x^(3/16 + ω)),
J(x) − signal(χ,H,−11/16)(x) = O(x^(β − 11/16 − σ)),
                                  ω>0, σ>0.
```

The analytic continuation and nonvanishing lemma in `Hecke/SignalIdentity.lean` explains how these two bounds force any zero near `β` to be impossible. This **conditional analytic inference** is structurally clear. The extraordinary task is proving the input estimates for actual characters, with the right uniformity. The source goes through `FinalAssemblyUnconditional → Energy.CertifiedExistence → Energy.CappedAnalyticSuccessor → moment bounds → UniformCommonProbe`.

Lay intuition: the final step says a detector cannot produce the signal expected from a certain zero if its error is strictly smaller than that signal. But we have to inspect **why the detector is accurate**. A logically impeccable contradiction built atop a falsely calibrated detector would say nothing about the zeros.

## 2. Two exact lower bounds hidden in the source parameters

The pinned `ParametersHighData.lean` defines `HighData` with:

```lean
t_small     : t ≤ 1/100000000
slots_sum   : (∑ j, ell j) = 1/6
slots_bounds: ∀ j, ell j ≤ (1/200)*t
```

Therefore, for any mathematically admissible `HighData` witness,

`1/6 = Σ_j ell(j) ≤ N·t/200 ≤ N/(200·10^8)`.

In particular,

```text
N ≥ ceil(100/(3t)) ≥ 3,333,333,334.
```

This is a **universal lower bound**, not a claimed numerical construction of a full `HighData` witness. The theorem `exists_high_data` establishes nonemptiness symbolically; it does not list billions of slot lengths.

The energy schedule then has an even larger necessary induction depth. From `DetectorPlainMomentParameters.lean`, `stageError(D)=t/4`. From `Moments/FirstSecondLossParameters.lean`, `depth(M,a)=⌈2M/a⌉₊+1`. From `Energy/WidthSchedule.lean`,

```lean
amplification ε = min 1 (ε/16000)
count M ε       = depth M (amplification ε)
```

The actual final detector passes `Mcap=2` and `ε=t/4`. Since `t≤10⁻⁸`,

```text
amplification(t/4) = t/64000,
count(2,t/4) = ceil(256000/t)+1 ≥ 25,600,000,000,001.
```

The source does **not** mechanically iterate over this many concrete states during compilation. It applies `Nat` induction to a symbolic `k` and thus checks one general successor lemma. This makes the theorem possible to formalize without operationally enumerating a 25.6-trillion-step construction.

There is another very large finite quantifier: `Energy/Bands.lean`, `exists_positive_bottom`, uses `Finset.univ : Finset (Finset α)`. In final assembly `α=Fin D.N`, so the index set includes `2^N` subsets. Even at the *smallest possible* `N`, this integer contains **at least 1,000,000,001 decimal digits**; the exact proof is `2^10>10^3` plus the ten possible remainders in the exponent. The compiled use of `Finset.univ` is a finite **mathematical** construction, not an actually enumerated implementation.

**Disposition:** these scales do not refute the theorem, but are a firm evidentiary boundary against claiming direct numerical reconstruction of every slot, every subset, or every induction stage. A bounded independent experiment must test transferable lemmas or specialized small instances, not pretend to evaluate the full explicit construction.

## 3. Is the error budget algebraically sound?

At the optimistic parameter ceiling `t=10⁻⁸`, the independent [Python rational audit](f003_energy_scale_rational_audit.py) reproduces exactly the formulae for amplification, width, reserve, terminal loss, and stage count from the pinned source. It verifies:

```text
width(2, 0, t/4, count) > 2
loss(2, 0, t/4, count) ≤ (t/4)/1000
20·reserve ≤ amplification/2
```

These are exact rational comparisons of the stated **budget formulas**. They do not validate the analytic estimates being budgeted: a ledger that balances does not prove that the listed expenses were genuine.

A useful knife-edge is the parameter `κ`. The source sets `Δ=β−7/8` and `kappaPlain(D)=3/4+2Δ`. Hence

```
κ = 3/4 + 2(β−7/8) = 2β − 1.
```

Thus `κ` **saturates**, rather than strictly exceeds, the hypothesis `2β−1≤κ` in the actual energy successor. The source's inequality is non-strict, so this is permitted. The adversarial numerical check verifies that reducing `κ` by any positive amount would violate that exact hypothesis. This flags where **a hidden demand for strict slack** in a lower analytic lemma could be consequential; none is asserted here without inspecting such a lemma.

## 4. The height-loss trap: ruled out by the stated quantifier order

The intermediate `SourceMomentBound` permits a polynomial height factor `C(1+Z^(2τ))^J`. With a fixed positive `τ`, large `J` could absorb the entire hoped-for `Z^t` saving. This is a real mathematical hazard, not cosmetic bookkeeping.

The source addresses it explicitly:

- `ChosenMomentInput` has `∃J≥0, ∀η, ∃C>0, ∀τ>0 ...`, with the same `J` for all `η`.
- `HighData.height_choice` chooses a **single** `τ≤t/[4(J+7)]` *after* choosing `J`, but *before* the universal character `η`.
- `FinalAssemblyMomentInput.polynomial_height_absorption` proves the sufficient condition `2τ(1+J)≤t`, yielding

  `C(1+Z^(2τ))^J ≤ C·2^J·Z^t` for `Z≥1`.

Indeed, `2τ(1+J)≤t(1+J)/[2(J+7)]<t`, uniformly for every `J≥0`. The independent exact-rational audit tests `J=0,1,5,100,10^6,10^20` and rejects the hostile unsuppressed choice `τ=t`.

This is a **genuine positive finding**: the apparent loss of the crucial exponent through unbounded polynomial height is **not** an overlooked algebraic or quantifier-order gap at this precise interface. It does **not** independently certify the existence of the source's `SourceMomentBound` itself.

## 5. Where the independent referee must bear down

The current critical obligation is no longer whether `∑ell=1/6`, the schedule's terminal width, `2β−1≤κ`, or the polynomial height absorption can coexist; these exact checks pass.

It is whether the real mathematical estimates that enter `Energy/CappedAnalyticSuccessor.actual_successor` and especially `Energy/CappedWidthInduction.certified_floor` are valid for the **natural** characters, source-supported test profiles, and masked prime rows required downstream, without silently substituting a weaker toy ensemble. The source's `CertifiedBand` quantifies over

```text
∃ degree, finite S, ∀ η₀, ∀ Q with Q≤M and
internalQ(Q,η₀) nonzero, proper, and bounded by (72),
∃ positive constants, ∀ sufficiently large Z,
both ZeroAt(...) and PositiveAt(...).
```

The downstream `plain_inputs` instantiates `Q=sourceFixedIdeal F` and separately supplies the required ideal gates, so the visible transition is **not trivially vacuous**. It still requires reconstructing the specific `actual_joint_floor` and `actual_high_stage` analytic inequalities, their quantifier dependence, and how the natural principal / nonprincipal characters are handled.

**Recommendation:** independent mathematical reconstruction should target `actual_joint_floor` (initial joint zero/positive bound) and the `actual_high_stage` call in `actual_successor`, then the prime-row/source-moment translation. Stop producing raw all-module recompilations unless an exact semantic or proof-obligation change needs a new pinned run.

## 6. Claim and source ledger

| Component | Exact upstream Git blob |
| --- | --- |
| `ParametersHighData.lean` | `c565dc0a72c7da9a2706cdd835e69a39e8c0dc14` |
| `Moments/FirstSecondLossParameters.lean` | source-locked by upstream commit (definition `depth` inspected) |
| `Energy/WidthSchedule.lean` | `6258a7a987c90df8bae1d24f7fd80e0e36baa24b` |
| `Moments/DetectorPlainMomentParameters.lean` | `4b74374fdf210f7c80377c624c435fb14e70e3a8` |
| `Detector/FinalAssemblyMomentInput.lean` | `436856065bd974c5ca52ac43b751a716f454ed20` |
| `Detector/FinalAssemblyChosenData.lean` | `94b7543e8076fc514b61e89efa7141831e102c03` |
| `Energy/Bands.lean` | `a565218399cadcd62d92fbb47313631847c1ff4f` |
| `Energy/CappedWidthInduction.lean` | `0f1fc34a0033ee423642d372c16dcd6690d59363` |
| `Energy/CappedAnalyticSuccessor.lean` | `e48d2c10a65012a44b1525fa5231921ad1120566` |
| `Detector/FinalAssemblyUnconditional.lean` | `e7c20910424837fb954796e1216f5aa453bbd5da` |
| `Hecke/CommonProbe.lean` | `92ae82094f323d97b92ae54801e88f2c97f20187` |

The accompanying exact-rational executable provides source-independent arithmetic tests. It is **not** a proof checker for the PDE/analytic-energy portion, nor a formal Lean replay of source-inductive estimates.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI26-F003-ENERGY-SCHEDULE-AND-HEIGHT-UNIFORMITY/1
SOURCE_SHA: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: ENERGY_BUDGET_RATIONAL_PASS__SYMBOLIC_SCALE_LIMITS_QUANTIFIED__SUBSTANTIVE_ANALYTIC_FLOOR_AND_HIGH_STAGE_OPEN
EVIDENCE: source-locked exact-rational audit + pinned source proofs above
TESTS: SLOT_LOWER_BOUND; DEPTH_LOWER_BOUND; WIDTH_AND_LOSS; KAPPA_SATURATION; HEIGHT_POLYNOMIAL_ABSORPTION; HOSTILE_TAU_AND_KAPPA
UNRESOLVED: independent actual_joint_floor; natural actual_high_stage; entire zero-free analytic proof and external Hecke L semantics
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
