# MF-FC-WP00 — Formal Conjectures Governed Intake

## Source

- Repository: `google-deepmind/formal-conjectures`
- Source lock: `source_lock.json`
- Pinned commit: `85f863718beeec7b58a3a1926ee92e3472bc2020`
- Lean toolchain: `leanprover/lean4:v4.27.0`
- mathlib revision: `v4.27.0`

## Pilot scope

- `FormalConjectures/Millenium/RiemannHypothesis.lean`
- `FormalConjectures/Millenium/NavierStokes.lean`

## Replay

From a checkout at the pinned commit:

```bash
python formal_sources/formal_conjectures/intake.py intake \
  --source-lock formal_sources/formal_conjectures/source_lock.json \
  --checkout /path/to/formal-conjectures \
  --output formal_sources/formal_conjectures/snapshots/FC-GDM-001-RH-NS-PILOT.json \
  --generated-at 2026-07-30T11:08:00Z
```

For an already captured extractor result:

```bash
python formal_sources/formal_conjectures/intake.py normalize \
  --source-lock formal_sources/formal_conjectures/source_lock.json \
  --extract-json extract_names.json \
  --output snapshot.json \
  --generated-at 2026-07-30T11:08:00Z
```

Verify a committed snapshot:

```bash
python formal_sources/formal_conjectures/intake.py verify \
  --source-lock formal_sources/formal_conjectures/source_lock.json \
  --snapshot formal_sources/formal_conjectures/snapshots/FC-GDM-001-RH-NS-PILOT.json
```

## Digest contract

`sha256-canonical-json-v1` hashes canonical JSON containing only:

- `source_lock_id`;
- `source_commit`;
- `scope`;
- sorted normalized `statements`.

The timestamp and stored digest are excluded from the digest payload.

## Claim boundary

The snapshot records what the pinned upstream Lean environment declared. It does not establish semantic equivalence, current mathematical status, proof, novelty, or certification.
