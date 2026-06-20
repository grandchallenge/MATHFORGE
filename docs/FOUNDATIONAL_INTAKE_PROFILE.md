# Foundational Intake Profile Standard

Status: proposed MATHFORGE intake standard  
Purpose: make every problem card foundation-aware before it enters MATHSOLVE or MATHCERT.

## Intake rule

MATHFORGE must not pass a mathematical object downstream as a bare set when the statement depends on geometry, measure, topology, algebra, computation, or a certificate discipline.

Every intake card should answer:

```text
What is the carrier?
What is the ambient structure?
What operations are legal?
What regularity is assumed?
What foundation is being used?
What kind of witness or certificate is expected?
```

## Required card block

Add the following block to new problem cards and work-package seeds. Unknown values are permitted during intake, but they must be marked as unknown rather than silently assumed.

```yaml
foundational_profile:
  carrier_type: finite | countable | continuum | higher_type | categorical | unknown
  carrier_description: ""
  ambient_structure:
    - vector_space
    - affine_space
    - metric_space
    - topological_space
    - measurable_space
    - probability_space
    - algebraic_structure
    - order_structure
    - computable_presentation
  admissible_operations:
    - equality_test
    - membership_test
    - addition
    - scalar_multiplication
    - multiplication
    - order_comparison
    - limit
    - integration
    - optimization
    - finite_search
    - oracle_query
  regularity:
    - finite
    - decidable
    - computable
    - Borel
    - Lebesgue_measurable
    - compact
    - convex
    - smooth
    - Noetherian
    - separable
  axiom_profile:
    base: finite | constructive | ZF | ZF+DC | ZFC | stronger | unknown
    choice_usage: none | finite_choice | countable_choice | dependent_choice | full_choice | unknown
    excluded_middle: avoided | local | used | unknown
  witness_policy:
    existence_claim: explicit_witness | extractable | nonconstructive | contradiction_only | unknown
    expected_artifact: none | example | counterexample | proof_term | certificate | computation_trace | unknown
  pathology_risk:
    level: low | medium | high | unknown
    triggers: []
    notes: ""
```

## Intake classification

MATHFORGE should assign one of these tags before handoff:

### finite-computable

The object is finite, explicitly represented, or reducible to bounded search. Preferred downstream routes: enumeration, SAT/SMT/PB, Lean finite proof, proof-producing CAS, small verifier.

### constructive-witnessed

The claim is meaningful only if witnesses or algorithms can be extracted. Preferred downstream routes: constructive proof, type-theoretic statement, executable construction, proof term.

### regular-analytic

The claim lives in analysis, probability, dynamics, geometry, PDE, or optimization and uses regular ambient spaces. Preferred refinements: Polish, standard Borel, separable, compact metric, Borel, Lebesgue measurable, convex, smooth.

### classical-choice-marked

The claim may require full choice or a classical maximality argument. Examples: arbitrary vector-space bases, ultrafilters, maximal ideals, full Hahn-Banach, arbitrary products. This is acceptable only if marked.

### foundations-sensitive

The claim is about determinacy, large cardinals, consistency strength, forcing, non-measurable sets, or independence. It must be routed as a foundations problem rather than ordinary analysis.

### under-specified

The statement uses phrases like `subset`, `function`, `space`, `measure`, `basis`, `generic`, `almost all`, or `random` without enough structure to determine the admissible operations. The card may be created, but it must carry a clarification task.

## Red flags

MATHFORGE should mark `pathology_risk.level: high` when it sees:

- arbitrary subsets of the continuum without Borel/measurable/definable qualification;
- choice of one representative from each class of an uncountable quotient;
- arbitrary vector-space bases over infinite-dimensional spaces;
- ultrafilters or non-principal filters;
- products over arbitrary index classes;
- existential claims with no witness, no extraction route, and no certificate target;
- probability claims without a declared sigma-algebra;
- convexity claims without an affine or vector-space ambient;
- measurability claims without a measurable-space profile.

## Example refinement

Raw statement:

```text
Let A be a subset of R. Prove that ...
```

Foundation-aware intake:

```yaml
object: A
raw_description: subset of R
clarification_required: true
possible_refinements:
  - A finite subset of R
  - A Borel subset of R
  - A Lebesgue-measurable subset of R
  - A computably presented closed subset of R
  - A completely arbitrary subset of R, with choice/pathology risk marked
foundational_profile:
  carrier_type: continuum
  ambient_structure: [topological_space, measurable_space]
  regularity: []
  axiom_profile:
    base: unknown
    choice_usage: unknown
    excluded_middle: unknown
  pathology_risk:
    level: high
    triggers:
      - arbitrary_subset_of_continuum
    notes: "Statement is not ready for downstream proof routing until regularity is declared or arbitrariness is intentional."
```

## Handoff contract

A MATHFORGE handoff to MATHSOLVE should include:

```yaml
handoff_contract:
  statement: ""
  provenance: []
  foundational_profile: {}
  route_recommendation: finite-computable | constructive-witnessed | regular-analytic | classical-choice-marked | foundations-sensitive | under-specified
  missing_structure_questions: []
  expected_certificate_boundary: ""
```

MATHFORGE succeeds when the solver receives not just a problem, but a structured object with an honest account of what kind of mathematics is being requested.
