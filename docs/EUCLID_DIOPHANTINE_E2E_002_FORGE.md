# EUCLID-DIOPHANTINE-E2E-002 — Forge intake

## Two approachable tasks

First solve

\[
252x + 105y = 84.
\]

Stage 1 protected the identity

\[
-2\cdot252 + 5\cdot105 = 21.
\]

Because `84 = 4*21`, multiplying the coefficients by `4` gives the candidate witness

\[
-8\cdot252 + 20\cdot105 = 84.
\]

Now consider

\[
252x + 105y = 20.
\]

Every integer combination of `252` and `105` is divisible by their protected gcd `21`. However,

\[
20 = 0\cdot21 + 20, \qquad 0 < 20 < 21.
\]

The nonzero remainder is the candidate obstruction. A failed search would not be an obstruction.

## The modern theorem

For integers `a`, `b`, and `c`, with `(a,b) != (0,0)`, there exist integers `x,y` with

\[
a x + b y = c
\]

if and only if `gcd(|a|,|b|)` divides `|c|`.

The absolute values fix sign normalization. The target `c = 0` is included: `x = y = 0` is a solution, and every positive gcd divides zero.

## Object, witness, obstruction, certificate

| Surface | Meaning |
|---|---|
| Object | whether the equation has an integer solution |
| Constructive witness | integers `x,y` satisfying the equation |
| Unsatisfiable obstruction | a checked nonzero remainder modulo the normalized gcd |
| Candidate output | deterministic JSON from MATHSOLVE |
| Certificate | an independent MATHCERT disposition |

MATHFORGE fixes these distinctions. It does not accept either candidate.

## Protected Stage 1 reuse

Stage 2 consumes the protected GCD and Bézout trust spine:

- MATHFORGE `3622bac82a39cdb9e82ec463919d9e6927c1ec0e`;
- MATHSOLVE `3a8493aa322f0e640c921b8824c4d7f88a8c057d`;
- MATHCERT `78b69e6a3461a83f4893d61c421b1570c08a9ba6`;
- MATH-PROGRAMME `183ff2a0adfbe5bd0ffd5f2e638089b94b868c54`.

No competing gcd definition or duplicate Euclidean trace contract is admitted.

## Downstream route

MATHSOLVE #103 will emit either a scaled constructive witness or an exact divisibility obstruction. MATHCERT #89 will use an implementation independent of that producer, verify the protected identities and arithmetic, and prove the admitted Lean equivalence with positive and negative concrete replays.

## Historical and scope boundary

This is a modern classical theorem statement. It is not attributed verbatim to Euclid. It does not claim a complete procedure for arbitrary multivariable or nonlinear Diophantine equations. It carries no novelty or priority claim.

## Chaidez documentary sequence

Any later historical edition remains ordered as follows:

1. exact source lock;
2. historical-to-modern concordance;
3. semantic web reader;
4. edition record and native accessible plates;
5. atomic documentary-manifest admission.

Illuminated plates are pedagogical only. The source record, normalized theorem, equations, protected dependency map, claim ledger, and technical appendix govern.
