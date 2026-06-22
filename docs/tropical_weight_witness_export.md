# Tropical Weight Witness Export

## Purpose

This lane lets MATHFORGE export the discovery artifacts needed by TROPIC-GROEBNER.

The doctrine is:

> MATHFORGE may propose weights and record initial forms. MATHSOLVE decides whether the route helps. MATHCERT checks the certificate.

A tropical witness is not a proof of a tropical variety. It is a durable record of a sampled weight, the support data that produced it, and the exact initial-form claim that downstream pillars can replay.

## Covered witness classes

MATHFORGE may emit:

- support lists and Newton-polytope forecasts;
- coefficient valuation records;
- candidate weight vectors;
- weighted term-score tables;
- initial-form records;
- retained/rejected sampled-weight hints;
- monomial witnesses for obviously rejected weights;
- handoff payloads for `tropical_initial_ideal` certificates.

## Required payload

Every exported tropical weight witness should record:

```yaml
witness_id: ""
schema_version: "0.1.0"
witness_kind: tropical_weight_probe
coefficient_domain: QQ
valuation: trivial
variables: []
monomial_order: weight_refined_lex
problem:
  statement: ""
  generators: []
witness:
  weight: []
  term_scores: {}
  minimal_terms: []
  initial_form: ""
  contains_monomial: true|false
  monomial_witness: null
handoff:
  mathsolve_route: TROPIC_GROEBNER_CAMPAIGN
  mathcert_certificate_kind: tropical_initial_ideal
  trust_status: external_witness_recorded
```

## Trust status

| Status | Meaning |
| --- | --- |
| `candidate_weight` | MATHFORGE generated a weight but has not stabilized the witness. |
| `initial_form_recorded` | Term scores and initial terms are recorded. |
| `external_witness_recorded` | Payload is durable and hashable. |
| `ready_for_mathsolve` | Route decision can be made by MATHSOLVE. |
| `ready_for_mathcert` | Payload is shaped as a MATHCERT certificate request. |

No MATHFORGE status means `certified`.

## First fixture

For `TROPIC-GROEBNER-001`, MATHFORGE should export one witness per sampled weight for

```text
f = x + y + 1
```

under trivial valuation. The smallest complete witness is the retained sample

```text
w = (1, 0), initial form = y + 1.
```

The adversarial witnesses are equally important: `w=(-1,0)` emits monomial witness `x`, and `w=(1,2)` emits monomial witness `1`.

## Boundary

The witness may support a sampled-weight route decision. It may not support complete fan traversal, theorem-level tropical membership claims, real/integer conclusions, or efficiency claims beyond the declared budget.
