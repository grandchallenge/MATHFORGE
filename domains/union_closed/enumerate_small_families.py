#!/usr/bin/env python3
"""Exact small-universe enumerator for Union-Closed Sets.

This is a MATHFORGE reconnaissance tool, not a proof of Frankl's conjecture.
It enumerates all families of subsets of {0,...,n-1} for n <= 4 by brute force,
checks union-closure exactly using bitmasks, and checks the Frankl condition exactly.
"""
from __future__ import annotations
import json
import hashlib
from pathlib import Path

GENERATOR_VERSION = "uc-small-audit-v1"
COUNTING_CONVENTION = (
    "raw union-closed counts include the empty family; Frankl-facing counts include "
    "only nontrivial families with nonempty support"
)

def subsets(n: int) -> list[int]:
    return list(range(1 << n))


def is_union_closed(fam: tuple[int, ...]) -> bool:
    s = set(fam)
    for a in fam:
        for b in fam:
            if (a | b) not in s:
                return False
    return True


def is_nontrivial(fam: tuple[int, ...]) -> bool:
    # Nonempty family with nonempty support.
    return len(fam) > 0 and any(x != 0 for x in fam)


def freq(fam: tuple[int, ...], i: int) -> int:
    bit = 1 << i
    return sum(1 for a in fam if a & bit)


def frankl_holds(fam: tuple[int, ...], n: int) -> bool:
    if not is_nontrivial(fam):
        return True
    return any(2 * freq(fam, i) >= len(fam) for i in range(n))


def enumerate_n(n: int) -> dict:
    subs = subsets(n)
    total_families = 1 << len(subs)
    uc = 0
    nontrivial = 0
    violations = []
    for mask in range(total_families):
        fam = tuple(subs[j] for j in range(len(subs)) if mask & (1 << j))
        if is_union_closed(fam):
            uc += 1
            if is_nontrivial(fam):
                nontrivial += 1
                if not frankl_holds(fam, n):
                    violations.append(list(fam))
    return {
        "n": n,
        "universe_size": n,
        "all_subsets": len(subs),
        "all_families": total_families,
        "union_closed_families": uc,
        "nontrivial_union_closed_families": nontrivial,
        "violations": len(violations),
        "violation_examples_bitmasks": violations[:5],
    }


def main() -> None:
    results = [enumerate_n(n) for n in range(0, 5)]
    out = Path(__file__).with_name("union_closed_small_audit.json")
    payload = {
        "generator_version": GENERATOR_VERSION,
        "counting_convention": COUNTING_CONVENTION,
        "results": results,
    }
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    certificate = {
        "certificate_type": "union_closed_small_universe_audit",
        "generator_version": GENERATOR_VERSION,
        "counting_convention": COUNTING_CONVENTION,
        "source_audit": "MATHFORGE/domains/union_closed/union_closed_small_audit.json",
        "source_audit_sha256": digest,
        "results": [
            {
                "universe_size": r["universe_size"],
                "raw_union_closed_families": r["union_closed_families"],
                "nontrivial_union_closed_families": r["nontrivial_union_closed_families"],
                "frankl_violations": r["violations"],
            }
            for r in results
        ],
    }
    cert_out = Path(__file__).parents[2] / ".." / "MATHCERT" / "certificates" / "exact"
    cert_out.mkdir(parents=True, exist_ok=True)
    (cert_out / "union_closed_n_le_4.json").write_text(
        json.dumps(certificate, indent=2) + "\n", encoding="utf-8"
    )
    for r in results:
        print(
            f"n={r['n']}: union_closed={r['union_closed_families']}, "
            f"nontrivial={r['nontrivial_union_closed_families']}, violations={r['violations']}"
        )


if __name__ == "__main__":
    main()
