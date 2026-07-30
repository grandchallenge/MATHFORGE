# MF-GOV-WP01 — External Formal-Source Provenance Contract

## Status

Implemented for the `FC-GDM-001` pilot.

## Rule

An external formal repository is an upstream source. It is not the MATHFORGE provider repository imported by MATH-PROGRAMME. MATHFORGE must retain an immutable source lock, a deterministic extraction route, a governed snapshot, and campaign-level concordance records before Programme use.

The intake fails closed on:

1. source commit drift;
2. toolchain, dependency-lock, extractor, or statement-source blob drift;
3. an extracted module outside the locked selection;
4. duplicate theorem identities;
5. partial proof-link metadata;
6. snapshot digest drift;
7. unregistered source locks, snapshots, or concordance records.

## Authority boundary

Upstream categories such as `research open` and `research solved` are advisory metadata. They do not replace MATH-PROGRAMME status review. A Lean declaration containing `sorry` is a formulation artifact. A sorry-free declaration is not MATHCERT-certified unless the MATHCERT route independently admits and replays it.

## Schemas

- `schemas/external_formal_source.schema.json`
- `schemas/external_formal_source_registry.schema.json`
- `schemas/formal_statement_snapshot.schema.json`
- `schemas/statement_concordance.schema.json`

## Registry

`governance/external_formal_sources.json` is canonical. CI rejects missing and orphaned governed artifacts.

## Promotion condition

MATH-PROGRAMME may cite an external formal-source result only through the merged MATHFORGE commit and the exact registered artifact path and identity. This contract establishes provenance and formulation evidence only.
