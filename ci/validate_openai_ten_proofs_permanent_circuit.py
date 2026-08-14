#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
RECORD=ROOT/'sources/OPENAI-TEN-PROOFS-001/semantic/OTP-C-PERMANENT-CIRCUIT/audit_record.json'
SCHEMA=ROOT/'schemas/openai_ten_proofs_permanent_circuit_theorem_audit.schema.json'

def load(p): return json.loads(p.read_text(encoding='utf-8'))

def validation_errors(record=None):
    r=load(RECORD) if record is None else record
    s=load(SCHEMA)
    e=[x.message for x in Draft202012Validator(s).iter_errors(r)]
    src=r.get('source_theorem_1_1',{})
    if src.get('dimension_threshold')!=65536: e.append('threshold drift')
    if src.get('finite_bound_denominator')!=144: e.append('denominator drift')
    if src.get('division_allowed') is not False: e.append('division enabled')
    if src.get('fanout_reuse_allowed') is not True: e.append('DAG reuse removed')
    if src.get('arithmetic_gate_count_only') is not True or src.get('input_gates_counted') is not False: e.append('size semantics drift')
    replay=r.get('exact_overlay_replay',{})
    if replay.get('target_count')!=3: e.append('target count drift')
    for f in ('lean_default_kernel','nanoda_kernel','comparator'):
        if replay.get(f)!='accepted': e.append(f'replay lost: {f}')
    if replay.get('immutable_archive_modified') is not False: e.append('archive mutation')
    nv=r.get('nonvacuity',{})
    if nv.get('state')!='CLEAR': e.append('nonvacuity lost')
    cov=r.get('coverage',{})
    for f in ('source_theorem_1_1_finite_bound','source_theorem_1_1_bigomega_consequence','source_theorem_1_1_ratio_divergence_consequence','circuit_nonvacuity'):
        if cov.get(f) is not True: e.append(f'coverage lost: {f}')
    for f in ('formula_theorems_1_2_1_3_mutated','historical_pdf_byte_equivalence','solve_handoff','mathcert_intake_or_route','adjudication','cert_output','mathematical_target_proved_promoted','aggregate_ten_proofs_authority'):
        if cov.get(f) is not False: e.append(f'prohibited authority: {f}')
    return e

def main():
    e=validation_errors()
    if e:
        print('\n'.join(e),file=sys.stderr); return 1
    print('Permanent circuit Theorem 1.1 audit validates fail-closed'); return 0
if __name__=='__main__': raise SystemExit(main())
