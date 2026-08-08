from __future__ import annotations
import json,sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'sources/OZ-CUSPIDAL-FRICKE-001'
if str(P) not in sys.path:sys.path.insert(0,str(P))
import replay
M=P/'manifest.json';S=P/'manifest.schema.json';E=P/'evidence.json'
def load(p):return json.loads(p.read_text())
def errors(m=None,e=None):
 m=load(M) if m is None else m;e=load(E) if e is None else e;out=[x.message for x in Draft202012Validator(load(S)).iter_errors(m)]
 a=m.get('authority',{});exp={'forge_base':'49071febcacd9c84fe4ff268d4e11d7e0c4ff0e5','programme_merge':'d5f6b8babd385c13eca09accef5f14087e29d5aa','upstream_commit':'6cc0bf07137815ceeef0d9f340559f85352391e5','upstream_tree':'be780558454b704bdd016a3070d698c2e106e2b8'}
 for k,v in exp.items():
  if a.get(k)!=v:out.append('authority drift '+k)
 blobs={'level6_ledger':'15bf786f67723aab80a322a91f1abcfb2bea4282','d1_ledger':'bf28c96c45a5b514a13e8f2f1acf3bd87328f412','level6_producer':'fed208e189dcc46ec1bebc7107d6749e8ef44890','limit_script':'7f33f4f275162d2ffed6edaa31a488ee8f3ceb2b','paper':'92a07da5125acf229a2f4eb3ccab8aafc928f6d2'}
 for k,v in blobs.items():
  if a.get('source_blobs',{}).get(k,{}).get('blob')!=v:out.append('source blob drift '+k)
 want=replay.evidence()
 if e!=want:out.append('exact replay evidence drift')
 if e['level6']['w_prefix'][:4]!=['1','17','433','12257']:out.append('level6 forcing drift')
 if e['level6']['B_prefix'][:4]!=['0','1','67/4','12515/36']:out.append('level6 B drift')
 if e['d1']['B_prefix'][:5]!=['0','1','37/4','818/9','141587/144']:out.append('D1 B drift')
 if not e['level6']['all_scaled_integer']:out.append('level6 finite denominator failure')
 if not e['d1']['all_scaled_integer']:out.append('D1 finite denominator failure')
 if e['newform']['f6_q1_q8'][:5]!=[1,-2,-3,4,6]:out.append('f6 eta prefix drift')
 if e['newform']['fstar_q1_q8'][:5]!=[1,-6,-3,12,6]:out.append('fstar eta prefix drift')
 c=m.get('claim_decomposition',{})
 if c.get('d1_all_n_denominator')!='OPEN' or c.get('d1_exact_half_constant')!='OPEN':out.append('open proof obligation promoted')
 if m.get('proof_effect')!='NONE' or m.get('promotion_effect')!='NONE' or any(m.get('nonclaims',{}).values()):out.append('authority inflation')
 return out
def main():
 e=errors()
 if e:print('\n'.join(e),file=sys.stderr);return 1
 print('MF-OZ-CUSPIDAL-FRICKE-001 exact finite replay valid');return 0
if __name__=='__main__':raise SystemExit(main())
