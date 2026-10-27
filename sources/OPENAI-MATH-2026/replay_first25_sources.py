#!/usr/bin/env python3
"""Reproduce pinned first-shard source/Comparator metadata, never Lean proof claims."""
import argparse
import base64
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parent
PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
def first_shard(crosswalk):
    rs=crosswalk["main_results"]
    if len(rs)!=200 or len({x["declaration"] for x in rs})!=200:
        raise ValueError("not exactly 200 unique pinned declarations")
    return sorted(rs,key=lambda x:x["declaration"].encode("utf-8"))[:25]

def check_report(crosswalk, report):
    if report["record_type"]!="OAI26_WP01_SOURCE_CONFIG_PREFLIGHT/1" or report["upstream"]!=PIN:
        raise ValueError("unrecognized source report provenance")
    if report["scope"]!="SOURCE_FILES_AND_CONFIG_ONLY_NOT_LEAN_REPLAY":
        raise ValueError("source result falsely promoted")
    wanted=first_shard(crosswalk)
    seen=report["rows"]
    if len(seen)!=25 or [x["declaration"] for x in seen]!=[x["declaration"] for x in wanted]:
        raise ValueError("incorrect UTF-8 shard membership or order")
    for actual,expected in zip(seen,wanted):
        if actual["lean_source"]!=expected["lean_source"] or actual["comparator_config"]!=expected["comparator_config"]:
            raise ValueError("unbound solution or Comparator path")
        if not actual["config_includes_decl"] or not actual["source_contains_unqualified_name"]:
            raise ValueError("config theorem or source lexical name not witnessed")
        if actual["declaration"] not in actual["config_theorems"]:
            raise ValueError("Comparator config does not list declaration")
        for field in ("source_blob","comparator_blob"):
            if not re.fullmatch("[0-9a-f]{40}",actual[field]):
                raise ValueError("invalid pinned Git blob SHA-1")
    return True

def fetch(path):
    cmd=["gh","api",f"repos/openai/math/contents/{path}?ref={PIN}"]
    p=subprocess.run(cmd,check=False,capture_output=True,text=True,timeout=45)
    if p.returncode:raise RuntimeError(f"cannot retrieve source object {path}: {p.stderr[:100]}")
    obj=json.loads(p.stdout)
    content=base64.b64decode(obj["content"])
    git_blob=hashlib.sha1(b"blob "+str(len(content)).encode()+bytes([0])+content).hexdigest()
    if git_blob!=obj["sha"]:raise ValueError(f"Git blob mismatch: {path}")
    return path,(git_blob,content)

def live_report(crosswalk):
    rs=first_shard(crosswalk)
    paths=sorted({x[k] for x in rs for k in ("lean_source","comparator_config")})
    with ThreadPoolExecutor(max_workers=8) as pool:
        found=dict(pool.map(fetch,paths))
    checked=[]
    for r in rs:
        decl=r["declaration"];a,b=found[r["lean_source"]];c,d=found[r["comparator_config"]]
        conf=json.loads(d.decode("utf-8"));source=b.decode("utf-8")
        suffix=decl.rsplit(".",1)[-1]
        checked.append({"declaration":decl,"lean_source":r["lean_source"],
           "source_blob":a,"comparator_config":r["comparator_config"],
           "comparator_blob":c,"challenge_module":conf.get("challenge_module"),
           "solution_module":conf.get("solution_module"),
           "config_theorems":conf.get("theorem_names",[]),
           "config_includes_decl":decl in conf.get("theorem_names",[]),
           "source_contains_unqualified_name":bool(re.search(
               r"(?<![A-Za-z0-9_])"+re.escape(suffix)+r"(?![A-Za-z0-9_])",source)),
           "permitted_axioms":conf.get("permitted_axioms",[])})
    result={"record_type":"OAI26_WP01_SOURCE_CONFIG_PREFLIGHT/1","upstream":PIN,
        "scope":"SOURCE_FILES_AND_CONFIG_ONLY_NOT_LEAN_REPLAY","rows":checked}
    check_report(crosswalk,result)
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--live",action="store_true",help="fetch pinned source bytes through authenticated gh")
    p.add_argument("--check",action="store_true",help="compare live output with committed report")
    p.add_argument("--report",type=Path,default=ROOT/"FIRST25_CONFIG_PREFLIGHT.json")
    args=p.parse_args()
    crosswalk=json.loads((ROOT/"FORMALIZATION_CROSSWALK.json").read_text())
    output=live_report(crosswalk) if args.live else json.loads(args.report.read_text())
    check_report(crosswalk,output)
    rendered=json.dumps(output,sort_keys=True,indent=2)+"\n"
    if args.check:
        if args.report.read_text()!=rendered:raise SystemExit("DRIFT: pinned report differs from replay")
    elif args.live:
        args.report.write_text(rendered)
    print("PASS: 25/25 pinned config/theorem-name and source-token witnesses; NOT Lean proof replay")

if __name__=="__main__":main()
