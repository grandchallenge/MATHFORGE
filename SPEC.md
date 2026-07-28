# SPEC.md

## Purpose

MATHFORGE is the discovery and exploration pillar of the Grand Challenge mathematical platform. It finds candidate problems, reconstructs source context, performs status and prior-art audits, generates examples and bounded witnesses, compares representations, records failed routes, and emits provenance-bearing handoff packets for MATHSOLVE.

MATHFORGE is not a certification layer. It may propose, search, speculate, and fail. It must not promote conjectural or externally generated evidence into a theorem.

## Authority and ownership

`grandchallenge/MATH-PROGRAMME/MATHFORGE_SPEC.md` is the canonical programme doctrine. This repository implements that doctrine.

MATHFORGE owns provider work:

1. problem intake;
2. source reconstruction and source-lock support;
3. current-status and claim triage;
4. domain clustering;
5. reconnaissance computation;
6. representation and encoding search;
7. reduction-system reconnaissance;
8. conjecture and candidate-route mining;
9. false-proof, failed-route, and danger labelling;
10. discovery normalization;
11. prior-art and novelty-prohibition audits;
12. provider manifests and handoff packets.

MATH-PROGRAMME owns campaign authority, theorem-spine state, promotion decisions, and canonical claim status. MATHSOLVE owns controlled theorem obligations and tactics. MATHCERT owns replay and formal certification.

Provider results remain evidence until admitted by MATH-PROGRAMME and, where applicable, checked by MATHCERT.

## Non-responsibilities

MATHFORGE does not:

- certify mathematical truth;
- declare a proof complete;
- assert that an open problem remains open without a dated audit;
- hide failed searches or resource exhaustion;
- conflate finite or numerical evidence with a universal theorem;
- treat a CAS transcript as a certificate;
- infer semantic equivalence from an encoding without a correspondence audit;
- alter MATH-PROGRAMME claim ledgers or MATHCERT certification records.

## Provider campaign manifest

Every active MATH-PROGRAMME campaign must have exactly one MATHFORGE provider campaign manifest or an approved Programme waiver.

Provider manifests live under `provider_manifests/` and validate against `schemas/provider_campaign_manifest.schema.json`.

A manifest records:

- the canonical campaign identifier;
- native or retrospective provider coverage;
- immutable Programme source references;
- MATHFORGE-owned artifacts and their content identities;
- the required handoff packet;
- source, status, fixture, failed-route, provenance, and downstream-reference records;
- an explicit non-certification statement.

A retrospective manifest does not copy authoritative Programme text. It indexes the immutable Programme commit and paths that predated the provider contract, records the missing native Forge work, and establishes the provider boundary for future stages.

## Required handoff packet

Each manifest contains the following logical packet, whether represented by one artifact or several:

```text
PROBLEM_CARD
SOURCE_MAP
STATUS_TRIAGE
RECONNAISSANCE_LEDGER
FAILURE_RISKS
SUGGESTED_WP01
CERTIFICATION_ROUTE_SKETCH
```

Each packet component has one of these states:

- `present`: implemented as a MATHFORGE artifact;
- `referenced`: indexed at an immutable external Programme source;
- `not_applicable`: inapplicable with an explicit reason;
- `deferred`: provider debt remains visible and blocks the dependent promotion;
- `waived`: allowed only by an approved Programme waiver.

## Artifact identity

A local MATHFORGE artifact record must include:

- repository-relative path;
- artifact kind;
- ownership;
- claim boundary;
- content identity using Git blob SHA-1 or SHA-256.

CI recomputes the identity and fails closed on a mismatch, missing artifact, unregistered manifest, duplicate campaign, unresolved local reference, malformed external commit, or incomplete packet.

## Provider coverage registry

`governance/provider_coverage.json` is the current active-campaign inventory. Every entry names either:

- a provider manifest, or
- an approved waiver with approver, reason, scope, and review date.

The registry and manifest set must agree exactly. Unregistered manifests and uncovered campaigns fail CI.

## Inputs

MATHFORGE may ingest:

- official problem statements;
- primary literature and authoritative reconstructions;
- surveys and bibliographies;
- existing code and formal libraries;
- exact finite examples and counterexamples;
- symbolic, SAT/SMT, interval, and numerical outputs;
- polynomial, toric, and reduction-system encodings;
- user-curated research programmes.

## Discovery outputs

MATHFORGE may emit:

```text
PROBLEM_CARD
SOURCE_LEDGER
HYPOTHESIS_MATRIX
STATUS_AUDIT
FALSE_PROOF_ATLAS
FAILED_ROUTE_LEDGER
PRIOR_ART_LEDGER
CANDIDATE_SHORTLIST
RECONNAISSANCE_LEDGER
ALGEBRAIC_ENCODING_CARD
TERM_ORDER_SWEEP
ELIMINATION_MAP
RESULTANT_FEASIBILITY_PROBE
QUOTIENT_ALGEBRA_MODEL
REAL_ROOT_ISOLATION_LEDGER
LOCAL_SINGULARITY_CARD
SYZYGY_DEPENDENCY_MAP
CRITICAL_PAIR_LEDGER
SPARSE_SUPPORT_FORECAST
PARAMETRIC_BRANCH_LEDGER
RESOURCE_LEDGER
CANDIDATE_WITNESS
CERTIFICATION_ROUTE_SKETCH
```

Each output must preserve source provenance, side conditions, backend and resource details where relevant, failed routes, and a non-certification status.

## Quality gates

A MATHFORGE handoff may pass to MATHSOLVE only when:

1. the problem statement and scope are explicit;
2. primary or reputable source provenance is recorded;
3. current status is dated and qualified;
4. formulation, quantifier, and data-class boundaries are explicit;
5. failed routes and false-proof risks are visible;
6. the next Work Package recommendation is bounded;
7. the certification route is sketched without claiming certification;
8. local artifacts are content-addressed;
9. the provider manifest is registered;
10. the relevant Programme campaign imports the manifest at a stable Forge commit and verifies its hash.

## Promotion gate

Before MATH-PROGRAMME promotes WP00, WP01, a prior-art package, or a restricted-target selection, it must possess either:

- a stable MATHFORGE commit, provider-manifest path, and verified manifest hash; or
- an approved, scoped waiver.

Missing provider coverage is a blocking governance defect. It may not be repaired by copying provider work into MATH-PROGRAMME without a Forge record.

## Grand Challenge posture

MATHFORGE should be generous with possibility and severe with status.

The correct statement is not “the search solved the problem.” It is:

> Under this source, encoding, scope, and resource contract, MATHFORGE produced this candidate artifact for controlled downstream evaluation.
