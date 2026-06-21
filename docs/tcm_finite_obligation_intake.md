# TCM Finite-Obligation Intake

## Role

This lane teaches MATHFORGE when to emit a problem card for the MATHSOLVE `SEMIRING-CONTRACTION/TCM` route.

MATHFORGE does not certify the result. It recognizes finite proof debt, preserves semantic provenance, and emits a route-ready problem card.

Doctrine:

> Encoding is a mathematical act.

A TCM route is appropriate only when the finite encoding faithfully represents the subclaim under audit.

## Programme links

This intake lane remains downstream of MATH-PROGRAMME doctrine:

- [MATH-PROGRAMME Pages home](https://grandchallenge.github.io/MATH-PROGRAMME/)
- [Programme Atlas](https://grandchallenge.github.io/MATH-PROGRAMME/PROGRAMME_ATLAS/)
- [MATHFORGE pillar doctrine](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/MATHFORGE_SPEC.md)
- [Cross-pillar lanes](https://grandchallenge.github.io/MATH-PROGRAMME/CROSS_PILLAR_LANES/)
- [Claim-boundary doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/CLAIM_BOUNDARY_DOCTRINE/)
- [Resource Budget Policy](https://grandchallenge.github.io/MATH-PROGRAMME/RESOURCE_BUDGET_POLICY/)
- [TCM semiring-contraction route doctrine](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/docs/routes/TCM_SEMIRING_CONTRACTION_ROUTE.md)

## Route trigger

Mark a problem card as TCM-eligible when the obligation has all of these properties:

1. finite or explicitly bounded search domain;
2. local constraints or factorable objective;
3. checkable witness or counterexample format;
4. plausible OPB/SAT/CSP/QUBO/tensor-network encoding;
5. clear certification handoff to MATHCERT.

## Eligible forms

- pseudo-Boolean optimization;
- SAT / MaxSAT;
- QUBO;
- finite-domain CSP;
- graph coloring / independent set / cut / matching;
- bounded model search;
- exact finite counterexample search;
- exact finite witness search.

## Required problem-card fields

```yaml
route_family: SEMIRING-CONTRACTION/TCM
finite_domain:
  variables: []
  domain_sizes: []
encoding:
  target_format: OPB|SAT|CSP|QUBO|TENSOR_NETWORK
  semantic_correspondence: REQUIRED
certificate_plan:
  witness_shape: REQUIRED
  checker_target: MATHCERT
  expected_certificate: primal_witness|dual_bound|unsat_refutation|contraction_trace
claim_boundary:
  status: candidate
  forbidden_claim: TCM proves the theorem
```

## Rejection rules

Do not route to TCM when:

- the problem is not finite or no finite reduction has been justified;
- the encoding loses the mathematical semantics;
- only a soft/heuristic objective is available;
- no independent checker is planned;
- the proposed output would be only a visualization or score.

## Fixture 006 intake pattern

Fixture 006 begins from a finite pseudo-Boolean assignment obligation. MATHFORGE's role is to emit the OPB-ready problem card and preserve the claim boundary:

```text
finite assignment subclaim
  -> OPB-compatible problem card
  -> MATHSOLVE TCM artifact emitter
  -> MATHCERT PB checker
```
