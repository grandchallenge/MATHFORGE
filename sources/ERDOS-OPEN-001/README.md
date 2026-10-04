# ERDOS-OPEN-001 — strict-open Erdős intake

This package makes the current strict-open Erdős problem pool durable in MATHFORGE without turning source status into GCL proof, promotion, or certification authority.

## Protected inputs

Registry/status evidence is locked to `teorth/erdosproblems@b916d95cdfd41a6d2f21aa304515834e84f247c9`. The upstream repository describes `data/problems.yaml` as its ground-truth table for the community database corresponding to `erdosproblems.com`. Exact upstream bytes for the data file and its schema are vendored under `upstream/`; their Git blob identities match the upstream blobs recorded in `source_lock.json`.

Formal-statement availability is cross-walked only against the already admitted `FC-GDM-85F86371` provider snapshot at `google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020`. A newer upstream Formal Conjectures file is not treated as protected merely because the registry reports it as formalized.

## Selection rule

The strict-open pool is exactly the set with:

`informal_status.state == "open"`

At the locked registry revision this yields **593** records out of **1,221**.

The special unresolved states `decidable`, `falsifiable`, `verifiable`, `not provable`, `not disprovable`, and `independent` are intentionally excluded from the strict-open manifest. They total **52** records and remain visible in the manifest summary.

Four strict-open records currently also have `formal_status.state == "Lean"`, meaning the registry reports a formalized solution while the human/informal status remains open. Those rows are retained for fidelity but set to `HOLD_PENDING_REGISTRY_STATUS_RECONCILIATION`; they are not ordinary campaign candidates until that status mismatch is resolved.

## Formalization cross-walk

Of the 593 strict-open rows:

- **298** have a matching statement file in the protected FC-GDM snapshot.
- **59** are reported by the registry as statement-formalized but are absent from the protected FC-GDM snapshot.
- **236** are not reported as statement-formalized.

This distinction is deliberate. "Formalized upstream" is evidence; "present in the admitted GCL provider snapshot" is protected identity.

## Authority boundary

Forge intake does not authorize Solve work, certify any theorem, or adjudicate that a problem is mathematically open. Every row has `solve_eligibility = REQUIRES_PROGRAMME_SELECTION`. MATH-PROGRAMME retains current-status and promotion authority.

## Refresh rule

A refresh must be explicit and reviewable:

1. Resolve a new immutable `teorth/erdosproblems` commit and exact `data/problems.yaml`/schema blob identities.
2. Vendor those exact bytes.
3. Recompute the strict-open projection.
4. Cross-walk against the currently admitted FC-GDM snapshot, not an unadmitted upstream head.
5. Preserve the formal-solution/open-status hold rule.
6. Run `python ci/validate_erdos_open_intake.py` and the unit suite.
7. Treat all upstream movement as evidence requiring review; never auto-admit it.

The committed manifest is therefore a dated, reproducible intake snapshot, not a live claim that can silently change underneath a campaign.
