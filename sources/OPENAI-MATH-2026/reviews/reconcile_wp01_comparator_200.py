#!/usr/bin/env python3
"""Read-only, no-network reconstruction of protected WP01 comparator receipts."""
import json, hashlib, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[3]
BASE=ROOT/'sources/OPENAI-MATH-2026'
SRC='1581d4cbdd69a0faf34b2089614fe2a814316a6a'
cross=json.loads((BASE/'FORMALIZATION_CROSSWALK.json').read_text())
expected=sorted(cross['main_results'],key=lambda x:x['declaration'].encode())
files=sorted(BASE.glob('CORPUS_*_COMPARATOR_RECEIPT_LEDGER.json'))+sorted((ROOT/'evidence/oai26/wp01').glob('*.json'))
assert len(expected)==200 and len(files)>=87
records={};errors=[]
def pick(item, outer, *keys):
 for obj in (item,item.get('artifact'),item.get('runner'),outer.get('replay'),outer.get('execution'),outer.get('artifact'),outer.get('runner')):
  if isinstance(obj,dict):
   for key in keys:
    if obj.get(key) is not None:return obj[key]
 return None
for f in files:
 data=json.loads(f.read_text())
 groups=next((data[k] for k in ('results','entries','indices','runs') if isinstance(data.get(k),list)),None)
 if groups is None:groups=[data]
 digest=hashlib.sha1(b'blob '+str(f.stat().st_size).encode()+bytes([0])+f.read_bytes()).hexdigest()
 for item in groups:
  target=item.get('target') or data.get('target') or data.get('challenge') or {}
  idx=item.get('index',item.get('index_zero_based'))
  if idx is None and isinstance(target,dict):idx=target.get('index',target.get('index_zero_based'))
  if idx is None:errors.append((f.name,'missing_index'));continue
  idx=int(idx)
  declaration=item.get('declaration') or (target.get('declaration') if isinstance(target,dict) else target)
  if declaration is None and idx==199: declaration=data.get('challenge',{}).get('declaration')
  if declaration is None or (idx<200 and declaration!=expected[idx]['declaration']):
   # index 176-178 files have no declaration, can bind through crosswalk by index but explicitly flag this
   if declaration is None and 0<=idx<200:declaration=expected[idx]['declaration']; binding='INDEX_ONLY'
   else:errors.append((f.name,'declaration_mismatch',idx,declaration,expected[idx]['declaration']));continue
  else:binding='EXPLICIT'
  exitv=pick(item,data,'hardened_exit')
  accepted=pick(item,data,'comparator_hardened_accepted','hardened_accepted','comparator_accepted','accepted')
  run=pick(item,data,'run_id')
  artifact=pick(item,data,'artifact_id','id')
  if run is None and 'runner' in data:run=data['runner'].get('run_id')
  if exitv is None or run is None or artifact is None: errors.append((f.name,'missing_gates',idx,exitv,run,artifact));continue
  if int(exitv)!=0:errors.append((f.name,'hardened_exit_nonzero',idx,exitv));continue
  if accepted is False:errors.append((f.name,'explicit_rejection',idx));continue
  if accepted is None:
   # Some historical ledgers record exact exit and verified receipt without an explicit accepted boolean.
   decision=(data.get('decision') or data.get('disposition') or '')
   if not ('ACCEPTED' in decision or 'PASS' in decision or 'PROTECTED' in data.get('record_type','') or 'ADMISSION' in data.get('record_type','')):
    errors.append((f.name,'no_positive_assurance',idx,decision));continue
  diagnostic=pick(item,data,'diagnostic_fallback')
  if diagnostic is True:errors.append((f.name,'diagnostic_fallback',idx));continue
  rec={'index':idx,'declaration':declaration,'binding':binding,'run_id':int(run),'artifact_id':int(artifact),'hardened_exit':0,'explicit_accepted':accepted is True,'evidence_path':f.relative_to(ROOT).as_posix(),'evidence_blob':digest}
  records.setdefault(idx,[]).append(rec)
print('SOURCE_FILES',len(files),'VALIDATED_SLOTS',len(records),'ERRORS',len(errors))
for e in errors[:50]:print('ERROR',e)
print('MISSING',sorted(set(range(200))-set(records)))
print('DUPLICATE',[i for i,x in records.items() if len(x)>1])
for i in [0,1,38,49,50,125,176,177,178,199]:print('CASE',i,records.get(i))
if errors:sys.exit(2)
assert len(records)==200 and set(records)==set(range(200))
selected=[]
for idx in range(200):
    # Duplicated index 199 is corroboration, never a second declaration.
    rows=records[idx]
    selected.append({**rows[0], 'additional_corrob_receipts':rows[1:]})
report={
 'record_type':'GCL_OAI26_WP01_PROTECTED_COMPARATOR_200_RECONCILIATION/1',
 'source_commit':SRC,
 'pinned_crosswalk_git_blob':'5fc50adc9430a91f22f1c3913bdfec62fe75acda',
 'scope':'HARDENED_TECHNICAL_EXECUTION_ONLY_NOT_MANUSCRIPT_SEMANTICS_OR_MATHCERT',
 'distinct_declarations':200,
 'protected_receipt_files':len(files),
 'unique_indices_covered':len(records),
 'duplicate_corrob_indices':[i for i in sorted(records) if len(records[i])>1],
 'index_only_bindings':[i for i in sorted(records) if selected[i]['binding']=='INDEX_ONLY'],
 'explicit_acceptance_count':sum(r['explicit_accepted'] for r in selected),
 'status':'RECONCILED_PROTECTED_TECHNICAL_COMPARATOR_COVERAGE_200_OF_200',
 'rows':selected,
 'claim_boundary':'NO_MATHCERT_CERTIFICATION; NO_AUTOMATIC_FAMILY_MAPPING',
}
out=BASE/'WP01_COMPARATOR_200_PROTECTED_RECEIPT_INDEX.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('INDEX_JSON_BYTES',out.stat().st_size,'INDEX_ONLY',report['index_only_bindings'],'EXPLICIT_ACCEPTED',report['explicit_acceptance_count'])

