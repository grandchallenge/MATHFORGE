"""WP01 90-124 original receipts and effective retry references; no Comparator claim."""
import copy,csv,hashlib,json
from pathlib import Path
import unittest
R=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026"
def load(n):return json.loads((R/n).read_text())
def valid(d):
    with (R/"SOURCE_CROSSWALK_DECLARATIONS.csv").open() as f: cross=list(csv.DictReader(f))
    rows=d.get("rows",[]); runs=d.get("runs",[]); corr=d.get("effective_replay_corrections",[])
    if len(cross)!=200 or len(rows)!=35 or len(runs)!=7 or len(corr)!=5:return False
    if d.get("record_type")!="GCL_OAI26_WP01_CORPUS_RECONCILIATION_90_124/2":return False
    if d["source_identity"]["upstream_sha"]!="1581d4cbdd69a0faf34b2089614fe2a814316a6a":return False
    if [x["index_range"] for x in runs]!=[[i,i+5] for i in range(90,125,5)]:return False
    if sum(x["verified_internal_file_hashes"] for x in runs)!=130:return False
    if len({x["run_id"] for x in runs})!=7:return False
    if [x["index_zero_based"] for x in rows]!=list(range(90,125)):return False
    historical=[91,102,107,108,124]
    for i,row in enumerate(rows,90):
        if row["declaration"]!=cross[i]["declaration"] or row["comparator_config"]!=cross[i]["comparator_config"] or row["comparator_executed"] is not False:return False
        if i in historical:
            if row["build_exit"]!=124 or row["axioms_exit"] is not None:return False
        elif row["verdict"]!="LEAN_REPLAY_AND_AXS_PASS" or row["build_exit"]!=0 or row["axioms_exit"]!=0 or row["extra_axioms"]!=[]:return False
    if [c["index_zero_based"] for c in corr]!=historical:return False
    for c in corr:
        i=c["index_zero_based"];rel=c["protected_evidence_path"]
        if not rel.startswith("sources/OPENAI-MATH-2026/"):return False
        blob=(R/rel.rsplit("/",1)[-1]).read_bytes()
        sha=hashlib.sha1(b"blob "+str(len(blob)).encode()+b"\0"+blob).hexdigest()
        if c["protected_evidence_blob_sha"]!=sha or c["comparator_executed"] is not False:return False
        ev=json.loads(blob)
        x=next((v for v in ev["results"] if v["zero_based_index"]==i),None) if "results" in ev else ev["result"]
        if not x or x["declaration"]!=rows[i-90]["declaration"] or x["build_exit"]!=0 or x["axioms_exit"]!=0 or x["extra_axioms"]!=[] or x["comparator_executed"] is not False:return False
        if x["solution_git_blob"]!=rows[i-90]["solution_git_blob"] or x["comparator_git_blob"]!=rows[i-90]["comparator_git_blob"]:return False
        if c["historical_timeout_run_id"]!=rows[i-90]["run_id"]:return False
        if c["verified_success_run_id"]!=x.get("run_id",ev.get("evidence",{}).get("run_id")):return False
    return d["effective_counts"]["unique_effective_lean_axiom_pass"]==35 and d["effective_counts"]["comparator_executed"]==0
class TestCorpus90124(unittest.TestCase):
    def test_positive(self):self.assertTrue(valid(load("CORPUS_90_124_LEAN_RECEIPT_LEDGER.json")))
    def test_hostile(self):
        d=load("CORPUS_90_124_LEAN_RECEIPT_LEDGER.json")
        changes=[("rows",0,"index_zero_based",89),("rows",1,"declaration","OAI.Forged"),
                 ("rows",1,"comparator_executed",True),("effective_replay_corrections",0,"protected_evidence_blob_sha","0"*40),
                 ("effective_replay_corrections",1,"index_zero_based",91),("effective_counts",None,"unique_effective_lean_axiom_pass",36)]
        for section,i,key,value in changes:
            with self.subTest(section=section,key=key):
                v=copy.deepcopy(d);target=v[section] if i is None else v[section][i];target[key]=value
                self.assertFalse(valid(v))
