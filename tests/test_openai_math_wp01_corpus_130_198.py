"""Exact-source WP01 130–198 replay, excluding indices 145 and 199."""
import csv, hashlib, json, copy, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026"
DOC=ROOT/"CORPUS_130_198_EXCLUDING_145_199_LEAN_RECEIPT_LEDGER.json"
SRC=ROOT/"SOURCE_CROSSWALK_DECLARATIONS.csv"
FIX=[139,143,168,190,192]
def admissible(d, cross):
    r=d.get("rows",[]);c=d.get("effective_replay_corrections",[]);runs=d.get("runs",[])
    if d.get("record_type")!="GCL_OAI26_WP01_130_198_PINNED_REPLAY/2":return False
    if d.get("excluded_by_user")!=[145,199] or len(r)!=68 or len(c)!=5 or len(runs)!=14:return False
    if len(cross)!=200 or [x.get("index_zero_based") for x in r]!=[i for i in range(130,200) if i not in (145,199)]:return False
    if [x["index_range"] for x in runs]!=[[i,i+5] for i in range(130,200,5)]:return False
    if len({x["run_id"] for x in runs})!=14 or sum(x["internal_file_hashes_verified"] for x in runs)!=266:return False
    if any(x["runner_head"]!="dd1a0c2001a4ce6ff0c7f9a0979d590edeafa777" for x in runs):return False
    if d["historical_counts"]["timeout_indices"]!=FIX or d["historical_counts"]["lean_axiom_pass"]!=63:return False
    if d["effective_counts"]["effective_lean_axiom_pass"]!=68 or d["effective_counts"]["comparator_executed"]!=0:return False
    for x in r:
        i=x["index_zero_based"]
        if x["declaration"]!=cross[i]["declaration"] or x["comparator_config"]!=cross[i]["comparator_config"]:return False
        if x.get("comparator_executed") is not False or x["run_id"]!=runs[(i-130)//5]["run_id"]:return False
        if i in FIX:
            if x["build_exit"]!=124 or x["axioms_exit"] is not None:return False
        elif x["build_exit"]!=0 or x["axioms_exit"]!=0 or x["extra_axioms"]!=[]:return False
    if [x["index_zero_based"] for x in c]!=FIX:return False
    for x in c:
        i=x["index_zero_based"];old=next(y for y in r if y["index_zero_based"]==i)
        if x["original_run_id"]!=old["run_id"] or x["declaration"]!=old["declaration"]:return False
        if x.get("comparator_executed") is not False or (x["corrective_build_exit"],x["corrective_axioms_exit"])!=(0,0):return False
        path=x["corrective_ledger_path"]
        if not path.startswith("sources/OPENAI-MATH-2026/"):return False
        buf=(ROOT/path.split("/")[-1]).read_bytes()
        oid=hashlib.sha1(b"blob "+str(len(buf)).encode()+bytes([0])+buf).hexdigest()
        if oid!=x["corrective_ledger_git_blob"]:return False
        z=json.loads(buf)
        y=next(v for v in z["results"] if v["zero_based_index"]==i) if "results" in z else z["result"]
        if (y["declaration"],y["solution_git_blob"],y["comparator_git_blob"])!=(old["declaration"],old["solution_git_blob"],old["comparator_git_blob"]):return False
        if (y["build_exit"],y["axioms_exit"])!=(0,0) or y["extra_axioms"]!=[]:return False
        if y.get("comparator_executed",y.get("actual_comparator_executed")) is not False:return False
        if y.get("run_id",z.get("evidence",{}).get("run_id"))!=x["corrective_run_id"]:return False
    return True
class TestWP01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc=json.loads(DOC.read_text())
        with SRC.open(newline="") as f:cls.cross=list(csv.DictReader(f))
    def test_positive(self):self.assertTrue(admissible(self.doc,self.cross))
    def test_hostile(self):
        changes=[
            lambda d:d["rows"][0].__setitem__("index_zero_based",145),
            lambda d:d["rows"][0].__setitem__("comparator_executed",True),
            lambda d:d["rows"][1].__setitem__("declaration","OAI.Forged"),
            lambda d:d["effective_replay_corrections"][0].__setitem__("corrective_run_id",1),
            lambda d:d["effective_replay_corrections"][0].__setitem__("corrective_ledger_git_blob","0"*40),
            lambda d:d["effective_counts"].__setitem__("effective_lean_axiom_pass",69),
            lambda d:d["excluded_by_user"].remove(145)
        ]
        for m in changes:
            x=copy.deepcopy(self.doc);m(x);self.assertFalse(admissible(x,self.cross))
