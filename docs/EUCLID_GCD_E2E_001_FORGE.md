# EUCLID-GCD-E2E-001 — Forge intake

## The approachable task

Compute the greatest common divisor of `252` and `105`.

\[
252 = 2\cdot105 + 42,\qquad
105 = 2\cdot42 + 21,\qquad
42 = 2\cdot21 + 0.
\]

The last positive remainder is `21`. Back-substitution gives

\[
21 = -2\cdot252 + 5\cdot105.
\]

These equations are exact candidate evidence. MATHFORGE does not certify them.

## Object, construction, witness, certificate

| Surface | Meaning |
|---|---|
| Object | the greatest common divisor |
| Construction | the Euclidean division trace |
| Witness | the integer coefficients `-2` and `5` |
| Certificate | the provider-bound JSON that a separate checker can validate |

The distinction is mandatory. A solver output is not a certificate disposition, and a valid-looking trace is not self-authenticating.

## Modern statement

For natural numbers `a` and `b`, not both zero, the downstream certificate reports a positive `d`, a complete Euclidean trace ending in zero, and integers `x,y` satisfying `x*a + y*b = d`. MATHCERT must prove that its accepted-certificate predicate entails `d = Nat.gcd a b`.

The `(0,0)` input is excluded from this exemplar. The reported divisor is normalized to be positive.

## Historical boundary

Euclid’s *Elements*, Book VII, supplies historical context for common measure and algorithmic reduction. The exact proposition cluster and edition text are not asserted here. They are reserved for `EUCLID-ELEMENTS-BOOK-VII-MICRO-001`, which must source-lock exact artifacts before making proposition-level claims.

The modern extended-Euclidean algorithm, integer Bézout identity, and linear Diophantine theorem are modern normalized statements in this programme. This Forge package does not attribute them verbatim to Euclid.

## Certification route

MATHSOLVE will emit a deterministic candidate. MATHCERT will independently verify every division equation, strict remainder descent, terminal zero, positive normalization, divisibility, Bézout equality, and provider identity. Lean will then prove soundness of the accepted predicate and replay `Nat.gcd 252 105 = 21`.

## Claim boundary

This package fixes the target, evidence format, failure modes, and route. It proves no theorem, accepts no certificate, and claims no novelty, priority, or historical verbatim equivalence.

## Chaidez documentary sequence

The later documentary edition must proceed in this order:

1. exact source lock;
2. historical-to-modern concordance;
3. semantic web reader;
4. edition record and native accessible plates;
5. atomic documentary-manifest admission.

Illuminated plates will be pedagogical only. The source text, normalized statement, exact proof trace, claim ledger, and technical appendix will govern.
