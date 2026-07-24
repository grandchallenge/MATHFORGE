# NS-CI-WP01 — Exact false-proof atlas

## Status

- Campaign: `NS-CI-001`
- Work Package: `WP01`
- Parent: `grandchallenge/MATH-PROGRAMME#55`
- Tracker: `grandchallenge/MATHFORGE#16`
- Result class: negative route audit
- Claim boundary: this atlas proves that specified arguments fail; it does not prove the critical-integrability target false.

## Governing target

For every smooth, divergence-free, rapidly decreasing datum in the whole-space Fefferman class, and every associated Leray–Hopf weak solution, determine whether

```math
I_T(u):=\int_0^T\|u(t)\|_{L^6(\mathbb R^3)}^4\,dt<\infty
```

for every finite `T>0`.

Each fixture below isolates a tempting shortcut, gives the smallest exact obstruction, records what is genuinely ruled out, and preserves the nearest viable route.

---

## FP-001 — Reversed finite-measure inclusion

### False claim

Because `(0,T)` has finite measure, `L^2(0,T)` control implies `L^4(0,T)` control.

### Exact witness

On `(0,1)`, let

```math
f(t)=t^{-1/3}.
```

Then

```math
\int_0^1|f(t)|^2dt=\int_0^1t^{-2/3}dt=3<\infty,
```

while

```math
\int_0^1|f(t)|^4dt=\int_0^1t^{-4/3}dt=\infty.
```

### Smallest failed step

On a finite-measure space, `L^4\subset L^2`; the inclusion does not reverse.

### Rules out

Any proof whose only time-variable input is `\|u(\cdot)\|_6\in L^2(0,T)`.

### Does not rule out

An equation-specific estimate that prevents the temporal concentration represented by `f`.

### Nearest viable route

Identify a new bound controlling either the height, duration, or frequency structure of `L^6` spikes.

---

## FP-002 — Incorrect energy interpolation endpoint

### False claim

Interpolating the energy bounds

```math
u\in L_t^\infty L_x^2\cap L_t^2L_x^6
```

yields `u\in L_t^4L_x^6`.

### Exact interpolation calculation

Complex or real interpolation with parameter `\theta\in[0,1]` gives

```math
\frac1q=\frac\theta2,
\qquad
\frac1p=\frac{1-\theta}{2}+\frac\theta6
=\frac12-\frac\theta3.
```

Setting `q=4` forces `\theta=1/2`, and then

```math
\frac1p=\frac13,
\qquad p=3.
```

Thus the energy line gives

```math
u\in L_t^4L_x^3,
```

not `L_t^4L_x^6`. Conversely, `p=6` forces `\theta=1`, hence `q=2`.

### Smallest failed step

The desired pair `(q,p)=(4,6)` is not on the interpolation segment joining `(\infty,2)` and `(2,6)`.

### Rules out

Generic interpolation between the two standard energy endpoints.

### Does not rule out

Interpolation involving a genuinely stronger third endpoint obtained from additional Navier–Stokes structure.

### Nearest viable route

Produce a scale-compatible improvement beyond the energy segment, then verify that it is not already equivalent to regularity.

---

## FP-003 — Hidden `L_t^\infty H_x^1` assumption

### False claim

The target follows from

```math
\int_0^T\|u(t)\|_6^4dt
\le
\sup_{0<t<T}\|u(t)\|_6^2
\int_0^T\|u(t)\|_6^2dt.
```

### Exact diagnostic

The inequality is correct, but it requires

```math
u\in L_t^\infty L_x^6.
```

By Sobolev, a sufficient condition is

```math
u\in L_t^\infty H_x^1,
```

which is precisely the strong-norm control not supplied by the Leray–Hopf energy inequality.

### Smallest failed step

A missing supremum is inserted as though it were part of the energy class.

### Rules out

Any argument that upgrades the target by multiplying the known `L_t^2L_x^6` norm by an unproved `L_t^\infty L_x^6` norm.

### Does not rule out

A proof of a uniform `H^1` bound from a new monotone quantity or structural depletion estimate.

### Nearest viable route

State the exact new hypothesis or estimate that supplies the supremum and test it for circularity.

---

## FP-004 — Circular Grönwall closure

### False claim

Use the `H^1` estimate to obtain `L_t^\infty H_x^1`, then use that bound to prove the critical integral finite.

### Exact loop

The classical estimate gives

```math
\sup_{s\le t}\|\nabla u(s)\|_2^2
\le
\|\nabla u_0\|_2^2
\exp\!\left(C\nu^{-3}I_t(u)\right).
```

Sobolev would then give

```math
I_t(u)
\le Ct\left(\sup_{s\le t}\|\nabla u(s)\|_2^2\right)^2
\le Kt\exp\!\left(2C\nu^{-3}I_t(u)\right).
```

An inequality of the form

```math
X\le K e^{cX}
```

does not upper-bound `X`; it is satisfied by all sufficiently large `X`.

### Smallest failed step

The target integral is the coefficient required to obtain the strong bound later used to estimate the target integral.

### Rules out

Self-referential use of the standard Grönwall estimate without an independent smallness or continuity mechanism.

### Does not rule out

A bootstrap on a short interval if a genuinely small, independently controlled quantity appears on the right-hand side.

### Nearest viable route

Find a scale-compatible inequality whose nonlinear dependence is absorbable rather than exponentially self-amplifying.

---

## FP-005 — Testing a Leray–Hopf solution by `-\Delta u`

### False claim

Pair the weak equation directly with `-\Delta u` to derive the `H^1` inequality for every Leray–Hopf solution.

### Exact regularity gap

The Leray–Hopf class gives

```math
u\in L_t^\infty L_x^2\cap L_t^2\dot H_x^1.
```

It does not provide `\Delta u\in L_t^2L_x^2` or enough time regularity to justify

```math
\left\langle \partial_tu,-\Delta u\right\rangle
=\frac12\frac d{dt}\|\nabla u\|_2^2.
```

The calculation is valid for smooth approximants or an already strong solution, followed by a justified limiting argument. That limit is itself part of the regularity theorem.

### Smallest failed step

An inadmissible test function is used before the regularity needed to define it has been established.

### Rules out

Treating the strong-solution energy estimate as an unconditional weak-solution estimate.

### Does not rule out

A rigorous approximation argument under the critical integrability hypothesis, as used in the conditional regularity theorem.

### Nearest viable route

Make the approximation class, convergence mode, and lower-semicontinuity steps explicit.

---

## FP-006 — Pressure cancellation mistaken for test admissibility

### False claim

The pressure term cancels against `-\Delta u`, so the `H^1` test is automatically valid for weak solutions.

### Exact distinction

For a sufficiently smooth divergence-free field on `\mathbb R^3`,

```math
\int_{\mathbb R^3}\nabla p\cdot\Delta u\,dx=0
```

under appropriate decay. This algebraic cancellation does not imply that `\Delta u` is an admissible test function in the weak formulation, nor that the pressure pairing is defined at Leray–Hopf regularity.

### Smallest failed step

A formal cancellation is substituted for a function-space justification.

### Rules out

Pressure-based rhetoric that bypasses the weak-to-strong upgrade.

### Does not rule out

Pressure-free formulations using the Leray projector or rigorous smooth approximation.

### Nearest viable route

Perform the calculation at the Galerkin or strong level and track every uniform estimate needed for passage to the limit.

---

## FP-007 — Fixed Galerkin cutoff

### False claim

Every finite-dimensional Galerkin solution has finite critical integral; therefore the continuum solution does as well.

### Exact divergent constant

Let `P_{\le N}` be a frequency cutoff. Bernstein in three dimensions gives

```math
\|P_{\le N}v\|_6\le C N\|v\|_2.
```

Hence the energy bound yields only

```math
\int_0^T\|P_{\le N}u(t)\|_6^4dt
\le C T N^4\sup_{0<t<T}\|u(t)\|_2^4.
```

The bound is finite for fixed `N` but diverges as `N^4`.

### Smallest failed step

No cutoff-uniform `L_t^4L_x^6` estimate is available.

### Rules out

Passing from finite-dimensional smoothness to the critical continuum norm without a uniform estimate.

### Does not rule out

A frequency-localized estimate whose shell contributions are summable uniformly in `N`.

### Nearest viable route

Measure and prove a cutoff-uniform flux, envelope, or concentration bound before taking `N\to\infty`.

---

## FP-008 — Mollification removes the singularity

### False claim

Mollify a Leray–Hopf solution and pass the finite critical norm of the mollified field to the limit.

### Exact divergent constant

For spatial mollification at scale `\varepsilon`, Young/Bernstein scaling gives

```math
\|\rho_\varepsilon*u\|_6
\le C\varepsilon^{-1}\|u\|_2.
```

Therefore

```math
\int_0^T\|\rho_\varepsilon*u(t)\|_6^4dt
\le C T\varepsilon^{-4}\sup_t\|u(t)\|_2^4.
```

The estimate diverges as `\varepsilon\downarrow0`.

### Smallest failed step

Smoothness of each approximation is confused with uniform critical control.

### Rules out

A bare mollify-and-limit argument.

### Does not rule out

A commutator or flux estimate that compensates for the `\varepsilon^{-4}` loss.

### Nearest viable route

Identify a cancellation that produces a positive power of `\varepsilon` or a scale-summable defect.

---

## FP-009 — Compact-support promotion

### False claim

A theorem for every `u_0\in C_c^\infty(\mathbb R^3)` proves the full whole-space positive Clay branch.

### Exact logical gap

```math
C_c^\infty(\mathbb R^3)
\subsetneq
\mathcal S(\mathbb R^3),
```

where the official whole-space class is smooth, divergence-free, and rapidly decreasing with all derivatives. Approximation of a Schwartz datum by compactly supported data does not transfer the theorem unless the critical estimates are uniform and the solution map is stable in a topology strong enough to pass `L_t^4L_x^6` control.

### Smallest failed step

A strict subclass is silently identified with the full quantified data class.

### Rules out

Promotion of `NS-CI-R-COMPACT` without a data-class extension theorem.

### Does not rule out

A compact-support theorem combined with a proved, uniform approximation/stability result.

### Nearest viable route

State and prove the missing extension theorem as an independent bridge.

---

## FP-010 — Numerical boundedness implies regularity

### False claim

The measured critical integral remains finite on increasingly fine simulations, therefore the continuum integral is finite.

### Exact obstruction

A fixed finite-dimensional Galerkin truncation or fully discrete approximation produces a finite reported value over its verified simulation interval. Such a value does not provide:

- a resolution-uniform upper bound;
- a verified truncation error in the critical norm;
- convergence to every Leray–Hopf solution;
- exclusion of concentration below the grid scale;
- a proof that numerical dissipation preserves the relevant flux.

### Smallest failed step

Finite values at finitely many resolutions are extrapolated to a uniform continuum theorem.

### Rules out

Numerical regularity claims without certified continuum error bounds.

### Does not rule out

Verified a posteriori numerical analysis under its stated hypotheses, or simulations used to falsify proposed mechanisms, identify concentration regimes, or test scaling diagnostics.

### Nearest viable route

Define a resolution-uniform observable and a verified convergence theorem before assigning continuum evidentiary weight to the numerical trend.

---

## FP-011 — Formalized assumptions presented as a formalized theorem

### False claim

Introduce the universal critical estimate as an axiom or interface field, derive global regularity in Lean, and describe the result as formal verification of Navier–Stokes regularity.

### Exact distinction

A theorem of the form

```text
(universal critical-integrability assumption)
  -> (global-regularity conclusion)
```

certifies only the logical composition. The analytic content remains entirely in the imported assumption.

### Smallest failed step

The trust boundary is hidden by naming or presentation.

### Rules out

Formalization theatre and opaque imported theorems.

### Does not rule out

Kernel-checking scaling identities, implication architecture, and explicitly provenance-bearing imported interfaces.

### Nearest viable route

Expose every imported theorem and open assumption in the generated theorem statement and claim ledger.

---

## FP-012 — Exponent-order confusion

### False claim

The pair `(4,6)` may be read interchangeably as `L_t^4L_x^6` or `L_t^6L_x^4`.

### Exact check

The critical relation is

```math
\frac2q+\frac3p=1
```

with `q` the time exponent and `p` the space exponent. For `(q,p)=(4,6)`, the left side is `1`. Reversing the pair gives

```math
\frac26+\frac34=\frac{13}{12}>1,
```

which is a different, supercritical mixed norm.

### Smallest failed step

Notation from two sources is merged without recording which exponent is temporal.

### Rules out

Source normalization by ordered pair alone.

### Does not rule out

Equivalent statements after an explicit notation translation.

### Nearest viable route

Every theorem record must name `time_exponent` and `space_exponent` separately.

---

## FP-013 — Interior regularity silently promoted to global whole-space regularity

### False claim

An interior Serrin theorem immediately supplies the full global `\mathbb R^3` continuation and initial-time statement required by the campaign.

### Exact gap

Interior regularity controls compact subsets away from the parabolic boundary. The campaign also requires:

- behavior at the initial time;
- whole-space integrability and decay;
- compatibility with the global Leray–Hopf energy class;
- a global uniqueness/continuation statement.

These require an operational global theorem or additional patching arguments.

### Smallest failed step

Local smoothness is identified with the global theorem interface.

### Rules out

Using Serrin's title or historical attribution as a substitute for a normalized theorem statement.

### Does not rule out

A rigorous localization-and-patching proof with global energy and decay controls.

### Nearest viable route

Keep historical attribution separate from the modern operational theorem used by the ledger.

---

## FP-014 — Existence of one selected weak solution settles the universal formulation

### False claim

Construct or numerically approximate one regular weak solution for each datum; therefore every Leray–Hopf solution satisfies the critical bound.

### Exact quantifier gap

The campaign target quantifies over every Leray–Hopf solution. Existence of one selected solution does not settle the universal statement unless weak–strong uniqueness applies on the whole interval and identifies all weak solutions with that selected strong solution.

### Smallest failed step

An existential witness is substituted for a universal quantifier.

### Rules out

Selection-based arguments without an accompanying uniqueness bridge.

### Does not rule out

Constructing one strong solution and then invoking a fully matched weak–strong uniqueness theorem.

### Nearest viable route

Record the solution-selection mechanism and the precise uniqueness theorem that upgrades existence to universality.

---

## Atlas summary

| Fixture | Failure class | Protected spine node |
|---|---|---|
| FP-001 | time-integrability inclusion | `NS-CI-O005` |
| FP-002 | interpolation geometry | `NS-CI-C004` / `NS-CI-T013` |
| FP-003 | hidden strong norm | `NS-CI-L010` |
| FP-004 | circular closure | `NS-CI-L010` / `NS-CI-T013` |
| FP-005 | inadmissible test | `NS-CI-L008` |
| FP-006 | formal cancellation | `NS-CI-L008` |
| FP-007 | nonuniform truncation | `NS-CI-T013` |
| FP-008 | nonuniform mollification | `NS-CI-T013` |
| FP-009 | data-class drift | `NS-CI-B011` / `NS-CI-R-COMPACT` |
| FP-010 | numerical overclaim | claim boundary |
| FP-011 | formalization overclaim | certification boundary |
| FP-012 | notation drift | `NS-CI-D001` / `NS-CI-L008` |
| FP-013 | local/global theorem drift | `NS-CI-L008` / `NS-CI-L010` |
| FP-014 | quantifier drift | `NS-CI-B011` |

## Promotion rule

A proposed route that triggers a fixture is terminated or narrowed before mechanism work begins. Passing the atlas does not validate a route; it only establishes that these known failure modes have been avoided.
