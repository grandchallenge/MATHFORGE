from __future__ import annotations
import json,sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'sources/OZ-PHI-SOURCES-001'
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import laws
M=HERE/'manifest.json'; S=HERE/'manifest.schema.json'; E=HERE/'coefficient_laws.json'
def load(p):return json.loads(p.read_text())
def errors(m=None,e=None):
 m=load(M) if m is None else m;e=load(E) if e is None else e;out=[]
 out += [x.message for x in Draft202012Validator(load(S)).iter_errors(m)]
 a=m.get('authority',{});exp={'forge_base':'49071febcacd9c84fe4ff268d4e11d7e0c4ff0e5','programme_merge':'d5f6b8babd385c13eca09accef5f14087e29d5aa','upstream_commit':'6cc0bf07137815ceeef0d9f340559f85352391e5','upstream_tree':'be780558454b704bdd016a3070d698c2e106e2b8'}
 for k,v in exp.items():
  if a.get(k)!=v:out.append('authority drift '+k)
 blobs={'ledger':'fcb12d96bd0583c4f2074aee663dd4ce36fb970c','producer':'506b059d64f481618013bc8858b3d411c860f8a9','holdout_producer':'fb47fb257cd085745c2540a6cfd557218993eb74','results':'3f81a2a218e981928a938cb116cf5323d9fe6e75','holdout_results':'27bb3be2b71f25ed39c8e88b7aa5f65d61f45e5c'}
 for k,v in blobs.items():
  if a.get('source_blobs',{}).get(k,{}).get('blob')!=v:out.append('blob drift '+k)
 if m.get('family_partition',{}).get('eisenstein_source_claims')!=laws.FAMILIES:out.append('family drift')
 if m.get('family_partition',{}).get('no_fit_in_stated_basis')!=['s7','s10','s18']:out.append('Cooper classification drift')
 if e!=laws.table(60):out.append('closed-form coefficient-law artifact drift')
 if any(v[0]!=1 for v in e.values()):out.append('normalization q coefficient drift')
 r=m.get('replay',{})
 if r.get('recurrence_to_phi_regenerated') or r.get('modularity_hypotheses_certified') or r.get('sturm_promotion_certified'):out.append('unearned proof promotion')
 if m.get('disposition')!='SOURCE_IDENTIFICATION_PARTIALLY_ADMITTED_WITH_BLOCKERS':out.append('disposition drift')
 if m.get('proof_effect')!='NONE' or m.get('promotion_effect')!='NONE' or any(m.get('nonclaims',{}).values()):out.append('authority inflation')
 return out
def main():
 e=errors()
 if e:print('\n'.join(e),file=sys.stderr);return 1
 print('MF-OZ-PHI-SOURCES-001 partial replay valid');return 0
if __name__=='__main__':raise SystemExit(main())
