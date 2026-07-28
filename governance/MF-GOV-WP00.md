# MF-GOV-WP00: MATHFORGE Provider Coverage and Handoff Audit

## Result status

- Status: implemented provider-governance remediation.
- Scope: MATHFORGE specification, active-campaign coverage, handoff schema, recursive validation, retrospective provider registration, and Programme import prerequisites.
- Strongest supported claim: the eight active research campaigns listed in `governance/provider_coverage.json` have a registered MATHFORGE manifest; native and retrospective coverage are distinguished.
- Claims not made: no retrospective manifest asserts that native Forge work occurred, no provider artifact proves a campaign theorem, and no novelty claim is introduced.
- First downstream obligation: MATH-PROGRAMME must import these manifests at the exact merged Forge commit and verify their content identities.

## Audit determination

MATHFORGE was conceptually correct but operationally optional. Union-Closed, Navier-Stokes, and Hodge had native provider work. BSD, P versus NP, Riemann, Yang-Mills, and Odd Zeta had substantial or newly instantiated Programme-owned source and governance packages without a stable Forge provider record.

This package repairs the provider boundary without copying authoritative Programme text.

## Coverage inventory

| Campaign | Coverage | Determination |
| --- | --- | --- |
| UC-001 | native | Exact finite reconnaissance registered. |
| NS-CI-001 | native | Source, false-proof, prior-art, and target-reconnaissance artifacts registered. |
| HC-001 | native | Source and formulation audit registered. |
| BSD-001 | retrospective | Immutable Programme WP00 paths indexed; native Forge debt remains explicit. |
| PNP-001 | retrospective | Immutable Programme WP00 paths indexed; future discovery work must originate in Forge. |
| RH-001 | retrospective | Immutable Programme WP00 paths indexed; future discovery work must originate in Forge. |
| YM-001 | retrospective | Immutable Programme WP00 path indexed; future discovery work must originate in Forge. |
| OZ-001 | retrospective | Incomplete Programme intake and source-lock package indexed; source acquisition remains gated. |

## Handoff contract

Every provider manifest records the logical packet:

1. problem card;
2. source map;
3. status triage;
4. reconnaissance ledger;
5. failure risks;
6. suggested WP01;
7. certification-route sketch.

A packet component may be present, referenced, deferred, not applicable, or waived. Deferred components remain visible provider debt.

## Fail-closed conditions

CI rejects:

- an uncovered active campaign;
- an unregistered provider manifest;
- duplicate campaign or manifest identifiers;
- a missing local artifact;
- a mismatched Git blob or SHA-256 identity;
- an incomplete handoff packet;
- an external Programme reference without a full commit identity;
- a retrospective record that presents Programme-owned text as Forge-owned;
- a waiver without approver, scope, reason, and review date.

## Promotion boundary

After Programme integration, WP00, WP01, prior-art, and restricted-target promotion require either:

- an imported provider manifest pinned to a full MATHFORGE commit and verified hash; or
- an approved scoped waiver.

The manifest is provenance and provider evidence. Programme and MATHCERT retain claim and certification authority.
