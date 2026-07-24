# NS-CI-WP01 — Adversarial semantic review

**Review date:** 2026-07-23  
**Campaign:** `NS-CI-001`  
**Provider PR:** `grandchallenge/MATHFORGE#17`

## Verdict

**APPROVE FOR REFEREE PROMOTION AS A ROUTE-REJECTION ATLAS.**

The atlas is mathematically and semantically fit for its declared purpose: it rejects fourteen specified proof patterns without treating the failure of those patterns as evidence against the open critical-integrability statement.

Promotion is limited to an eliminative governance artifact. It is not a negative theorem about Navier–Stokes regularity.

## Review method

The review attempted to falsify each fixture along four axes:

1. **Exactness:** Does the displayed witness or exponent calculation actually contradict the false claim?
2. **Scope:** Does the fixture reject only the stated route, or does it overreach into a claim about the target theorem?
3. **Quantifiers and classes:** Are the domain, initial-data class, solution class, and universal/existential quantifiers preserved?
4. **Trust boundary:** Are computational and formal artifacts assigned only the evidentiary force they possess?

## Exact-fixture replay

### FP-001 — scalar time witness

For `f(t)=t^{-1/3}` on `(0,1)`,

```math
\int_0^1 |f|^2dt=\int_0^1t^{-2/3}dt=3,
\qquad
\int_0^1 |f|^4dt=\int_0^1t^{-4/3}dt=\infty.
```

The fixture correctly rejects `L^2(0,T)\subset L^4(0,T)`.

### FP-002 — energy interpolation

Interpolating `(q,p)=(\infty,2)` with `(2,6)` gives

```math
\frac1q=\frac\theta2,
\qquad
\frac1p=\frac12-\frac\theta3.
```

`q=4` forces `theta=1/2` and `p=3`; `p=6` forces `theta=1` and `q=2`. The desired pair `(4,6)` is not on the energy segment.

### FP-007 — cutoff loss

In three dimensions,

```math
\|P_{\le N}v\|_6\le C N^{3(1/2-1/6)}\|v\|_2=CN\|v\|_2.
```

Taking the fourth power produces the displayed `N^4` loss. Fixed-dimensional smoothness is therefore nonuniform in the critical norm.

### FP-008 — mollification loss

The `L^2\to L^6` norm of spatial smoothing at scale `epsilon` has the same dimensional exponent `epsilon^{-1}`. Its fourth power gives `epsilon^{-4}`. The fixture correctly rejects bare mollify-and-limit reasoning.

### FP-012 — exponent order

```math
\frac24+\frac36=1,
\qquad
\frac26+\frac34=\frac{13}{12}.
```

Time and space exponents cannot be exchanged.

All exact tests are replayed by `tests/test_ns_ci_false_proof_fixtures.py`. Forge CI run `30058521633` passed.

## Semantic findings by fixture family

### Function-space fixtures: FP-001 through FP-004

No overreach found. Each fixture distinguishes an unavailable estimate from impossibility of that estimate. FP-004 correctly observes that

```math
X\le K e^{cX}
```

does not impose an upper bound on `X`, because the right-hand side eventually dominates the left-hand side.

### Weak-formulation fixtures: FP-005 and FP-006

No contradiction with WP02. These fixtures reject unconditional use of the strong-level `-Delta u` calculation. They expressly permit smooth approximation or the audited conditional regularity theorem.

### Approximation fixtures: FP-007 and FP-008

The constants are correctly displayed and the conclusion is properly limited to the absence of a uniform estimate from the stated argument.

### Data and theorem-scope fixtures: FP-009, FP-012, FP-013, FP-014

The full Fefferman rapid-decay class, the compact-support restricted lane, the time-first exponent convention, the distinction between interior and global theorem interfaces, and the universal Leray–Hopf quantifier agree with WP00 and WP02.

### Numerical fixture: FP-010

The fixture is accepted with the following interpretation: the relevant object is a **fixed finite-dimensional approximation over its verified interval**, not an assertion that every numerical scheme has a global or faithful ODE realization. The rejected inference is from finitely many finite approximations to a uniform continuum theorem.

### Formal fixture: FP-011

The fixture correctly distinguishes kernel-checking an implication from proving its imported analytic premise. This matches the MATHCERT interface policy.

## Counter-route attempts

The Adversary attempted the following evasions:

- replacing finite-time inclusion by interpolation;
- obtaining the missing supremum from Sobolev alone;
- using pressure cancellation to justify weak testing;
- appealing to smoothness of every approximation without uniformity;
- replacing the universal weak-solution claim by a selected solution;
- treating a formal imported interface as a certificate of its fields.

Each evasion either triggers another atlas fixture or introduces a genuinely new hypothesis. No fixture was found to reject a valid route without changing the route's assumptions.

## Cross-document consistency

Checked against:

- `NS-CI-WP00` problem and source audit;
- the corrected Fefferman full data class;
- the WP00 theorem spine `NS-CI-C004`, `O005`, `L008`, `L010`, `B011`, and `T013`;
- WP02 entries `CR-003` through `CR-011`;
- the MATHCERT imported-interface boundary.

No blocking conflict was found.

## Referee conditions

The atlas is promoted subject to these standing rules:

1. It is extensible rather than exhaustive; new false routes receive new fixture IDs.
2. Triggering a fixture terminates or narrows a route, but passing the atlas does not validate a mechanism.
3. Numerical diagnostics remain permissible for falsification and mechanism discovery, not continuum proof.
4. Every future route record must state which fixtures were checked and what new estimate bypasses any nearby obstruction.

## Promotion decision

- Verifier: **reviewed**.
- Adversary: **reviewed**.
- Amanuensis consistency: **reviewed**.
- Referee: **approved**.
- Blocking obligations: **none**.
- Programme status: `REFEREE_PROMOTED_ROUTE_REJECTION_ATLAS`.
