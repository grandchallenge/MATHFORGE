#!/usr/bin/env python3
"""Actual pinned Lean theorem/axiom replay, deliberately separate from Comparator certification."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PIN = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
TREE = "45074722c918576d65b4c8be9686c76f508ba696"
NAME = re.compile(r"^[A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*$")
AXIOM_LIST = re.compile(r"depends on axioms:\s*\[([^\]]*)\]")
NO_AXIOMS = re.compile(r"does not depend on (?:any )?axioms")

def parsed_axioms(text):
    if "sorryAx" in text:
        return None, "UNAPPROVED_SORRY_AXIOM"
    values = AXIOM_LIST.findall(text)
    if len(values) == 1:
        return sorted({item.strip() for item in values[0].split(",") if item.strip()}), None
    if len(values) == 0 and NO_AXIOMS.search(text):
        return [], None
    return None, "AXIOM_OUTPUT_NOT_PARSEABLE"

def execute(argv, cwd, logfile, timeout=1800):
    try:
        p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout, encoding="utf-8", errors="replace")
        body = p.stdout + "\n=== STDERR ===\n" + p.stderr
        code = p.returncode
    except subprocess.TimeoutExpired as e:
        body = f"TIMEOUT {argv} after {timeout}s\n"
        code = 124
    logfile.write_text(body, encoding="utf-8")
    return code, hashlib.sha256(body.encode("utf-8")).hexdigest()

def verify_environment(upstream):
    head = subprocess.check_output(["git", "-C", str(upstream), "rev-parse", "HEAD"], text=True).strip()
    tree = subprocess.check_output(["git", "-C", str(upstream), "rev-parse", "HEAD^{tree}"], text=True).strip()
    toolchain = (upstream/"lean"/"lean-toolchain").read_text().strip()
    if (head,tree,toolchain) != (PIN,TREE,"leanprover/lean4:v4.34.1"):
        raise ValueError("source revision/tree/toolchain mismatch")
    return {"source_sha":head,"source_tree":tree,"toolchain":toolchain}

def prepare_tasks(crosswalk, report, start, count):
    from replay_first25_sources import first_shard, check_report
    check_report(crosswalk, report)
    if start < 0 or count < 1 or start + count > 25:
        raise ValueError("invalid bounded first-25 subrange")
    tasks = report["rows"][start:start+count]
    for item in tasks:
        if not NAME.fullmatch(item["declaration"]):
            raise ValueError("bad pinned declaration identifier")
        if not NAME.fullmatch(item["solution_module"] or ""):
            raise ValueError("bad pinned module identifier")
    return tasks

def replay(upstream, destination, tasks, env):
    lean_root = upstream/"lean"
    destination.mkdir(parents=True, exist_ok=True)
    records=[]
    for offset, task in enumerate(tasks):
        declaration = task["declaration"]
        module = task["solution_module"]
        config_rel = task["comparator_config"]
        solution_rel = task["lean_source"]
        for rel, expected in ((config_rel,task["comparator_blob"]),
                              (solution_rel,task["source_blob"])):
            pathname = upstream/rel
            if not pathname.is_file():
                raise ValueError("missing checked-out pinned source: "+rel)
            oid = subprocess.check_output(["git","-C",str(upstream),"hash-object",str(pathname)],
                                          text=True).strip()
            if oid != expected:
                raise ValueError(f"source Git object changed: {rel}")
        cfg = json.loads((upstream/config_rel).read_text())
        if cfg["solution_module"] != module or declaration not in cfg["theorem_names"]:
            raise ValueError("Comparator configuration identity drift")
        allowed = set(cfg["permitted_axioms"])
        stem = f"{offset:02d}-{re.sub('[^A-Za-z0-9]+','_',declaration)[-70:]}"
        build_exit, build_log = execute(["lake","build",module],lean_root,
                                        destination/(stem+".build.log"),timeout=1500)
        evidence = {"declaration":declaration,"solution_module":module,
                    "solution_git_blob":task["source_blob"],
                    "comparator_config":config_rel,"comparator_git_blob":task["comparator_blob"],
                    "allowed_axioms":sorted(allowed),"build_exit":build_exit,
                    "build_log_sha256":build_log,"axioms_exit":None,
                    "axioms_log_sha256":None,"observed_axioms":None,
                    "verdict":"BUILD_FAILED_OR_INFRASTRUCTURE_BLOCKED",
                    "actual_comparator_executed":False}
        if build_exit == 0:
            checker = destination/(stem+".lean")
            checker.write_text(f"import {module}\n#check {declaration}\n#print axioms {declaration}\n")
            code, logfile = execute(["lake","env","lean",str(checker)],lean_root,
                                     destination/(stem+".axioms.log"),timeout=180)
            body = (destination/(stem+".axioms.log")).read_text()
            observed, why = parsed_axioms(body) if code == 0 else (None,"AXIOM_QUERY_FAILED")
            evidence.update(axioms_exit=code,axioms_log_sha256=logfile,
                            observed_axioms=observed)
            if code == 0 and observed is not None:
                extra = sorted(set(observed) - allowed)
                evidence["verdict"] = "LEAN_REPLAY_AND_AXS_PASS" if not extra else "UNAPPROVED_AXIOMS"
                evidence["extra_axioms"] = extra
            else:
                evidence["verdict"] = why
        records.append(evidence)
        print("LEAN_REPLAY",declaration,evidence["verdict"],flush=True)
        receipt = {"record_type":"GCL_OAI26_WP01_TARGET_LEAN_REPLAY/1",
                   "provenance":env,"count_completed":len(records),
                   "claim_boundary":"Lean source replay/axiom closure only; Comparator isolation and manuscript-semantic equivalence not verified",
                   "results":records}
        (destination/"receipt.json").write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
    return records

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--upstream",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--start",type=int,default=0)
    parser.add_argument("--count",type=int,default=5)
    args=parser.parse_args()
    report=json.loads((ROOT/"FIRST25_CONFIG_PREFLIGHT.json").read_text())
    crosswalk=json.loads((ROOT/"FORMALIZATION_CROSSWALK.json").read_text())
    tasks=prepare_tasks(crosswalk,report,args.start,args.count)
    env=verify_environment(args.upstream)
    env.update(first25_range=[args.start,args.start+args.count],
               declared_upstream_manifest_sha256=hashlib.sha256(
                   (args.upstream/"lean"/"lake-manifest.json").read_bytes()).hexdigest())
    result=replay(args.upstream,args.output,tasks,env)
    successes=sum(x["verdict"]=="LEAN_REPLAY_AND_AXS_PASS" for x in result)
    print(f"LEARNED: {successes}/{len(result)} pinned declarations passed Lean compilation and axiom whitelist")
    if successes != len(result):
        raise SystemExit("EXACT_PROOF_REPLAY_INCOMPLETE: preserve receipt and logs")
if __name__=="__main__":
    main()
