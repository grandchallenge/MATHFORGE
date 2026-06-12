# Algebraic Witness Export

## Purpose

This lane lets MATHFORGE produce structured algebraic witnesses for polynomial reasoning tasks. It is not a certification layer. It is a disciplined way to record what an external symbolic search found so that MATHSOLVE can use it tactically and MATHCERT can later replay or formally check it.

The governing doctrine is:

> MATHFORGE may discover. MATHCERT must certify.

## Covered witness classes

MATHFORGE may emit witnesses for:

- polynomial identities;
- normal-form and remainder computations;
- ideal membership;
- ideal equality;
- Gröbner-basis candidates;
- radical-membership candidates;
- elimination outputs;
- finite truncations of infinite-variable or growing-family algebraic systems.

## Required payload

Every exported algebraic witness should record:

- `witness_id`;
- `claim_id` or provisional claim target;
- witness kind;
- coefficient domain;
- variable universe;
- monomial order;
- external backend;
- source polynomials;
- target expression or ideal statement;
- witness data;
- side conditions;
- hash/provenance metadata;
- intended MATHCERT certificate kind.

The schema lives at `schemas/algebraic_witness.schema.json`.

## Trust status

MATHFORGE outputs should normally use one of these statuses:

| Status | Meaning |
| --- | --- |
| `external_output_only` | A backend produced a result, but no artifact is stable yet. |
| `external_witness_recorded` | A witness artifact has been serialized and hashed. |
| `script_replayed` | A MATHFORGE script replayed lightweight shape/provenance checks. |
| `ready_for_mathcert` | The witness is ready to be translated into a MATHCERT algebraic certificate. |

No MATHFORGE status means `certified`.

## Relationship to MATHCERT

MATHFORGE witness exports should be transformable into MATHCERT algebraic certificates with minimal loss. The MATHCERT side owns the trusted boundary:

- external CAS output is evidence;
- exported witnesses are durable evidence;
- replay scripts are audit evidence;
- Lean-checked lemmas are certification.

## Future work

The next useful implementation step is a small adapter package:

```text
SageMath/SymPy/Singular output
  -> MATHFORGE witness JSON
  -> MATHSOLVE tactic record
  -> MATHCERT certificate JSON
  -> Lean theorem/check result
```
