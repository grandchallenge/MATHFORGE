# OPENMATH-2026 provider intake

**Forge tracker:** `grandchallenge/MATHFORGE#282`  
**Programme tracker:** `grandchallenge/MATH-PROGRAMME#1072`  
**Initial state:** `EXTERNAL_HILL_LOCK_PENDING`

This directory is the native MATHFORGE intake for the OpenMath 2026 sprint.

MATHFORGE owns statement/source reconstruction, dated status triage, reconnaissance, failure-risk recording, and the provider packet. It does not own theorem certification or Programme promotion.

## Source-lock rule

Do not infer a hill title, statement, identifier, difficulty, evaluator, or formal target from event prose or neighbouring archive entries.

A hill becomes Forge-ready only when an organizer-authoritative AutoLab record or equivalent authoritative export has been acquired and bound to:

- exact external identity;
- exact statement;
- exact version or observation time;
- Ulam/UnsolvedMath identity where applicable;
- primary/authoritative mathematical source;
- dated status triage;
- statement-fidelity hazards;
- checker/evaluator identity when available.

Until then its slot remains `PENDING_AUTHORITATIVE_ACQUISITION`.

## Seven slots

The provider reserves `OM26-H1` through `OM26-H7`. They are placeholders for identity only, not claims about content.

## Required packet after lock

Each acquired hill should produce:

```text
PROBLEM_CARD
SOURCE_MAP
STATUS_TRIAGE
RECONNAISSANCE_LEDGER
FAILURE_RISKS
SUGGESTED_WP01
CERTIFICATION_ROUTE_SKETCH
```

Shared reconnaissance may inventory formal environments, common libraries, submission/checker semantics, and source-acquisition methods before all six hills are locked. It must not make substantive claims about an unresolved slot.

## Downstream boundary

A Forge source lock permits MATHSOLVE to organize work. It does not establish mathematical correctness, novelty, semantic fidelity of a future formal artifact, certification, or competition acceptance.

## Human Steward cardinality correction

The sprint cardinality is seven. `OM26-H7` is reserved following the Human Steward correction identifying an additional Erdős problem. That high-level identification is not a source lock: exact H7 organizer identity, statement, evaluator, version, and source metadata remain `PENDING_AUTHORITATIVE_ACQUISITION`.
