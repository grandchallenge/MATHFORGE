# Algebraic Witness Export

## Purpose

This lane lets MATHFORGE produce structured algebraic witnesses for polynomial reasoning tasks. It is not a certification layer. It is a disciplined way to record what an external symbolic search found so that MATHSOLVE can use it tactically and MATHCERT can later replay or formally check it.

The governing doctrine is:

> MATHFORGE may discover. MATHCERT must certify.

## Programme links

Read this lane through the programme front door and the shared doctrine pages:

- [MATH-PROGRAMME Pages home](https://grandchallenge.github.io/MATH-PROGRAMME/)
- [Programme Atlas](https://grandchallenge.github.io/MATH-PROGRAMME/PROGRAMME_ATLAS/)
- [MATHFORGE pillar doctrine](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/MATHFORGE_SPEC.md)
- [Cross-pillar lanes](https://grandchallenge.github.io/MATH-PROGRAMME/CROSS_PILLAR_LANES/)
- [Computational Algebraic Geometry Lane](https://grandchallenge.github.io/MATH-PROGRAMME/COMPUTATIONAL_ALGEBRAIC_GEOMETRY_LANE/)
- [Groebner and EXPSPACE doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/GROEBNER_EXPSPACE_DOCTRINE/)
- [Claim-boundary doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/CLAIM_BOUNDARY_DOCTRINE/)
- [Resource Budget Policy](https://grandchallenge.github.io/MATH-PROGRAMME/RESOURCE_BUDGET_POLICY/)

## Covered witness classes

MATHFORGE may emit witnesses for:

- polynomial identities;
- normal-form and remainder computations;
- ideal membership and non-membership;
- ideal equality;
- Groebner-basis candidates;
- radical-membership candidates;
- elimination outputs;
- finite truncations of growing algebraic systems;
- sampled tropical initial-ideal records.

## Admission contract

Every governed witness must use `schemas/algebraic_witness.schema.json`, version `0.2.0`, and must be registered in `governance/algebraic_witness_registry.json` by exact Git blob identity.

The record must state:

- the local claim and local-scope justification;
- coefficient domain, variable universe, variable count, and monomial order;
- exact backend identity, command, and output digest;
- input polynomial count and maximum input degree;
- maximum variables, degree, runtime, basis size, and intermediate-term count;
- expected witness and fallback route;
- observed execution status and resource use;
- a failure ledger, including the fallback taken for unsuccessful runs;
- intended MATHCERT certificate kind and current trust status.

A record with `global_open_problem_encoding: true` is inadmissible. MATHFORGE must not encode an entire open problem as one unbounded symbolic search.

## Fail-closed rules

The validator rejects:

- unregistered or missing witness files;
- duplicate witness IDs or paths;
- changed files at an unchanged registry digest;
- variable-count or degree drift;
- runtime, basis-size, or intermediate-term budget overruns;
- unsuccessful runs without a failure-ledger entry;
- non-completed runs marked `ready_for_mathcert`;
- schemas or records that omit the fallback route or expected witness.

A failed or exhausted search remains useful evidence only when the failure and fallback are recorded.

## Trust status

MATHFORGE outputs use one of these statuses:

| Status | Meaning |
| --- | --- |
| `external_output_only` | A backend produced a result, but no stable witness is admitted. |
| `external_witness_recorded` | A content-addressed witness exists. |
| `script_replayed` | MATHFORGE replayed bounded shape and provenance checks. |
| `ready_for_mathcert` | A completed, budget-conforming witness is ready for Cert intake. |
| `blocked` | The route failed, exceeded a budget, or lacks a valid handoff. |

No MATHFORGE status means `certified`.

## Relationship to MATHSOLVE and MATHCERT

MATHFORGE witness exports should be transformable into a MATHSOLVE tactic record and then into a MATHCERT certificate packet with minimal loss.

```text
external symbolic backend
  -> content-addressed MATHFORGE witness
  -> bounded MATHSOLVE tactic record
  -> MATHCERT certificate packet
  -> exact replay or kernel-checked result
```

External CAS output is evidence. Exported witnesses are durable evidence. MATHCERT owns the adjudication and proof boundary.
