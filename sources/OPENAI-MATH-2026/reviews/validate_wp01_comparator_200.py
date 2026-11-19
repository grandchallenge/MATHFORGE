#!/usr/bin/env python3
"""Validate existing protected 200-target technical Comparator evidence, not semantics."""
import copy,hashlib,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[3]
BASE=ROOT/'sources/OPENAI-MATH-2026'
DATA=BASE/'WP01_COMPARATOR_200_PROTECTED_RECEIPT_INDEX.json'
SRC='1581d4cbdd69a0faf34b2089614fe2a814316a6a'
def test(d):
 cross=json.loads((BASE/'FORMALIZATION_CROSSWALK.json').read_text())
 targets=sorted(cross['main_results'],key=lambda v:v['declaration'].encode('utf-8'))
 assert len(targets)==len(d['rows'])==d['unique_indices_covered']==200
 assert d['source_commit']==SRC
 assert d['claim_boundary'].startswith('NO_MATHCERT_CERTIFICATION')
 assert d['scope']=='HARDENED_TECHNICAL_EXECUTION_ONLY_NOT_MANUSCRIPT_SEMANTICS_OR_MATHCERT'
 assert len({x['index'] for x in d['rows']})==200
 assert [x['index'] for x in d['rows']]==list(range(200))
 assert d['duplicate_corrob_indices']==[199]
 files={}
 for x in d['rows']:
  i=x['index'];assert x['declaration']==targets[i]['declaration'],i
  assert x['hardened_exit']==0 and x['run_id']>0 and x['artifact_id']>0,i
  assert x['binding'] in ('EXPLICIT','INDEX_ONLY')
  assert x['evidence_path'].startswith(('sources/OPENAI-MATH-2026/','evidence/oai26/wp01/'))
  files[x['evidence_path']]=x['evidence_blob']
  for alt in x['additional_corrob_receipts']:
   assert i==199 and alt['index']==199 and alt['declaration']==x['declaration']
   assert alt['hardened_exit']==0
   files[alt['evidence_path']]=alt['evidence_blob']
 assert len(files)==d['protected_receipt_files']==87
 assert d['index_only_bindings']==[x['index'] for x in d['rows'] if x['binding']=='INDEX_ONLY']
 assert d['explicit_acceptance_count']==sum(x['explicit_accepted'] for x in d['rows'])
 for path,wanted in files.items():
  raw=(ROOT/path).read_bytes();h=hashlib.sha1(b'blob '+str(len(raw)).encode()+bytes([0])+raw).hexdigest()
  assert h==wanted,('stale evidence file',path)
 return True

def reject(d,label,mutation):
 x=copy.deepcopy(d);mutation(x)
 try:test(x)
 except (AssertionError,KeyError,TypeError,ValueError):print('WP01_HISTORICAL_HOSTILE_ROLLBACK_PASS',label)
 else:raise AssertionError('mutation accepted: '+label)

def main():
 d=json.loads(DATA.read_text());test(d)
 reject(d,'WRONG_THEOREM_NAME',lambda x:x['rows'][199].update(declaration='OAI.false'))
 reject(d,'MISSING_RECEIPT_INDEX',lambda x:x['rows'].pop(50))
 reject(d,'UNSUCCESSFUL_HARDENED_EXIT',lambda x:x['rows'][176].update(hardened_exit=1))
 reject(d,'STALE_HISTORICAL_BLOB',lambda x:x['rows'][38].update(evidence_blob='0'*40))
 reject(d,'DUPLICATE_INFLATED',lambda x:x.update(unique_indices_covered=201))
 print('WP01_PROTECTED_COMPARATOR_INDEX_PASS 200/200 distinct technical targets, 87 protected files, 5 hostile rollbacks; no semantic certification')
if __name__=='__main__':
 try:main()
 except (AssertionError,KeyError,ValueError,OSError) as e:
  print('WP01_HISTORICAL_AUDIT_FAIL',e,file=sys.stderr);sys.exit(1)
