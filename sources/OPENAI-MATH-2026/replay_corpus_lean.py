#!/usr/bin/env python3
"""Pinned WP01 whole-corpus shard replay; Lean evidence only, not Comparator certification."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from replay_first25_lean import verify_environment, replay, NAME, PIN, ROOT

def prepare_corpus(crosswalk, upstream, start, count):
    rows = crosswalk["main_results"]
    if len(rows) != 200 or len({r["declaration"] for r in rows}) != 200:
        raise ValueError("exactly 200 distinct declaration records required")
    if not 25 <= start < 200 or not 1 <= count <= 5 or start + count > 200:
        raise ValueError("out-of-range bounded replay")
    if start // 25 != (start + count - 1) // 25:
        raise ValueError("replay cannot cross a 25-declaration shard boundary")
    ordered = sorted(rows, key=lambda r: r["declaration"].encode("utf-8"))
    tasks = []
    for item in ordered[start:start+count]:
        decl = item["declaration"]
        if not NAME.fullmatch(decl):
            raise ValueError("invalid theorem identifier")
        config_path = upstream / item["comparator_config"]
        source_path = upstream / item["lean_source"]
        if not config_path.is_file() or not source_path.is_file():
            raise ValueError("pinned source/config file absent")
        config = json.loads(config_path.read_text())
        module = config.get("solution_module")
        if not isinstance(module, str) or not NAME.fullmatch(module):
            raise ValueError("invalid pinned solution module")
        if decl not in config.get("theorem_names", []):
            raise ValueError("pinned comparator lacks indexed declaration")
        if not re.search(r"(?<![A-Za-z0-9_])" + re.escape(decl.rsplit(".",1)[-1])
                         + r"(?![A-Za-z0-9_])", source_path.read_text()):
            raise ValueError("solution source lacks indexed declaration token")
        blobs = []
        for path in (source_path, config_path):
            blobs.append(subprocess.check_output(
                ["git", "-C", str(upstream), "hash-object", str(path)], text=True).strip())
        if not all(re.fullmatch("[a-f0-9]{40}", b) for b in blobs):
            raise ValueError("invalid pinned Git object hash")
        tasks.append({"declaration": decl, "lean_source": item["lean_source"],
                      "comparator_config": item["comparator_config"],
                      "solution_module": module, "source_blob": blobs[0],
                      "comparator_blob": blobs[1]})
    return tasks

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--upstream", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--start", type=int, required=True)
    p.add_argument("--count", type=int, required=True)
    p.add_argument("--build-timeout", type=int, choices=(1500, 4200), default=1500)
    a = p.parse_args()
    upstream = a.upstream.resolve()
    env = verify_environment(upstream)
    crosswalk = json.loads((ROOT / "FORMALIZATION_CROSSWALK.json").read_text())
    tasks = prepare_corpus(crosswalk, upstream, a.start, a.count)
    env.update(corpus_range=[a.start, a.start + a.count],
               manifest_sha256=hashlib.sha256(
                   (upstream / "lean" / "lake-manifest.json").read_bytes()).hexdigest(),
               claim_boundary="LEAN_AND_AXIOM_ONLY_NOT_COMPARATOR")
    results = replay(upstream, a.output, tasks, env, build_timeout=a.build_timeout)
    passed = sum(r["verdict"] == "LEAN_REPLAY_AND_AXS_PASS" for r in results)
    print(f"EXACT_CORPUS_REPLAY: {passed}/{len(results)} verified Lean and axiom checks")
    if passed != len(results):
        raise SystemExit("REPLAY_INCOMPLETE: check retained row receipts")

if __name__ == "__main__":
    main()
