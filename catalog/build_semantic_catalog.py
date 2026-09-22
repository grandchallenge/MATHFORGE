#!/usr/bin/env python3
"""Build and verify the provider-neutral GCL semantic catalog.

The adapter is deliberately conservative: normalization is textual and deterministic;
provider status and proof metadata remain attributed assertions; and no catalog tier is
treated as mathematical certification.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Iterator

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
ENTRY_DIR = ROOT / "catalog" / "entries"
PROVIDER_DIR = ROOT / "catalog" / "providers"
SCHEMA_DIR = ROOT / "schemas"
SHARD_SIZE = 2_000
SCHEMA_VERSION = "2.0.0"
RM_PROVIDER = "RM-AMPHORA-001"
RM_SNAPSHOT = "RM-AMPHORA-001-F22D0F28"
RM_REVISION = "f22d0f28b55e6e777acf82e722d97ae982dff02e"
RM_SOURCE_SHA256 = "3f6c96d18925a47ac223555717226c5408cc9c75e07a1e96bddcffde8a06f029"
FC_PROVIDER = "FC-GDM"
FC_SNAPSHOT = "FC-GDM-85F86371"
FC_REVISION = "85f863718beeec7b58a3a1926ee92e3472bc2020"
EXCLUDED_INFERENCES = [
    "programme_status", "semantic_equivalence", "proof", "novelty",
    "campaign_authority", "certification",
]
CLAIM_BOUNDARY = (
    "This catalog entry records provider provenance, deterministic normalization, and explicitly "
    "attributed annotations only. It does not establish Programme status, semantic equivalence, "
    "mathematical proof, novelty, campaign authority, Claim Ledger authority, or certification."
)
RM_MSC = {
    "Analysis, PDEs, and Dynamics": "35-XX",
    "Mathematical Physics": "81-XX",
    "Discrete Mathematics and Combinatorics": "05-XX",
    "Geometry and Topology": "00-XX",
    "Algebra and Representation Theory": "16-XX",
    "Applied and Computational Mathematics": "65-XX",
    "Number Theory": "11-XX",
    "Theoretical Computer Science": "68-XX",
    "Probability, Statistics, and ML": "60-XX",
    "Logic and Foundations": "03-XX",
}
REVIEWED_RELATIONS = {
    "NavierStokes.navier_stokes_existence_and_smoothness_R3": ("GCL-REL-NS-CI-001", "CAMPAIGN_CONCORDANT"),
    "RiemannHypothesis.riemannHypothesis": ("GCL-REL-RH-001", "CAMPAIGN_CONCORDANT"),
    "UnionClosed.union_closed": ("GCL-REL-UC-001", "CAMPAIGN_CONCORDANT"),
    "RiemannZetaValues.infinite_irrational_at_odd": ("GCL-REL-OZ-ODD-INFINITUDE", "SEMANTICALLY_REVIEWED"),
    "RiemannZetaValues.irrational_odd": ("GCL-REL-OZ-ODD-UNIVERSAL", "SEMANTICALLY_REVIEWED"),
    "RiemannZetaValues.irrational_eleven": ("GCL-REL-OZ-ZETA11", "SEMANTICALLY_REVIEWED"),
    "RiemannZetaValues.irrational_three": ("GCL-REL-OZ-ZETA3", "SEMANTICALLY_REVIEWED"),
    "RiemannZetaValues.irrational_five": ("GCL-REL-OZ-ZETA5", "SEMANTICALLY_REVIEWED"),
    "RiemannZetaValues.irrational_seven": ("GCL-REL-OZ-ZETA7", "SEMANTICALLY_REVIEWED"),
    "RiemannZetaValues.irrational_nine": ("GCL-REL-OZ-ZETA9", "SEMANTICALLY_REVIEWED"),
    "RiemannZetaValues.exists_irrational_of_five_seven_nine_eleven": ("GCL-REL-OZ-ZUDILIN-5-11", "CAMPAIGN_CONCORDANT"),
    "ComplexityTheory.P_ne_NP": ("GCL-REL-PNP-001", "SEMANTICALLY_REVIEWED"),
}


class CatalogError(RuntimeError):
    pass


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_line(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("utf-8")


def canonical_json_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return sha256_bytes(payload)


def canonical_inventory_sha256(inventory: dict[str, Any]) -> str:
    problems = inventory.get("problems")
    if not isinstance(problems, list):
        raise CatalogError("DeepMind extractor inventory has no problems array")
    canonical_problems = []
    for problem in problems:
        if not isinstance(problem, dict):
            raise CatalogError("DeepMind extractor inventory contains a non-object problem")
        item = dict(problem)
        for field in ("answerKinds", "subjects"):
            if isinstance(item.get(field), list):
                item[field] = sorted(item[field], key=str)
        canonical_problems.append(item)
    canonical_problems.sort(key=lambda item: (str(item.get("module", "")), str(item.get("theorem", ""))))
    return canonical_json_sha256({"problems": canonical_problems})


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def normalized_text(value: str) -> str:
    lines = value.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    return "\n".join(line.rstrip() for line in lines).strip()


def token_shingles(value: str) -> frozenset[str]:
    tokens = re.findall(r"[a-z0-9]+", value.lower())
    if len(tokens) < 3:
        return frozenset(tokens)
    return frozenset(" ".join(tokens[index:index + 3]) for index in range(len(tokens) - 2))


def git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True, text=True
    )
    return completed.stdout.strip()


def assertion(issuer: str, value: Any, locator: str, authority: str = "source_attributed") -> dict[str, str]:
    return {
        "issuer": issuer,
        "value": json.dumps(value, sort_keys=True, ensure_ascii=True) if not isinstance(value, str) else value,
        "source_locator": locator,
        "authority": authority,
    }


def write_shards(prefix: str, entries: Iterable[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    ENTRY_DIR.mkdir(parents=True, exist_ok=True)
    for existing in ENTRY_DIR.glob(f"{prefix}-*.jsonl"):
        existing.unlink()
    shards: list[dict[str, Any]] = []
    bucket: list[dict[str, Any]] = []
    total = 0

    def flush() -> None:
        nonlocal bucket
        if not bucket:
            return
        index = len(shards)
        path = ENTRY_DIR / f"{prefix}-{index:05d}.jsonl"
        payload = b"".join(canonical_line(item) for item in bucket)
        path.write_bytes(payload)
        relative = path.relative_to(ROOT).as_posix()
        shards.append({
            "path": relative,
            "entry_count": len(bucket),
            "byte_length": len(payload),
            "sha256": sha256_bytes(payload),
            "first_catalog_id": bucket[0]["catalog_id"],
            "last_catalog_id": bucket[-1]["catalog_id"],
        })
        bucket = []

    for entry in entries:
        bucket.append(entry)
        total += 1
        if len(bucket) == SHARD_SIZE:
            flush()
    flush()
    return shards, total


def researchmath_entries(path: Path) -> Iterator[dict[str, Any]]:
    first_by_normalized_digest: dict[str, int] = {}
    relation_ids_by_index: dict[int, list[str]] = {}
    duplicate_relations: list[dict[str, Any]] = []
    shingle_sets: list[frozenset[str]] = []
    fingerprint_buckets: dict[str, list[int]] = {}
    with path.open("rb") as preflight:
        for index, raw_with_newline in enumerate(preflight):
            row = json.loads(raw_with_newline.rstrip(b"\r\n").decode("utf-8"))
            original = str(row.get("self_contained_problem") or row.get("original_question") or "").strip()
            normalized = normalized_text(original)
            digest = sha256_bytes(normalized.encode("utf-8"))
            shingles = token_shingles(normalized)
            fingerprints = sorted(sha256_bytes(value.encode("utf-8"))[:16] for value in shingles)[:8]
            candidates = {candidate for fingerprint in fingerprints for candidate in fingerprint_buckets.get(fingerprint, [])}
            best: tuple[float, int] | None = None
            for candidate in candidates:
                prior = shingle_sets[candidate]
                union = len(shingles | prior)
                similarity = len(shingles & prior) / union if union else 1.0
                if similarity >= 0.82 and (best is None or similarity > best[0]):
                    best = (similarity, candidate)
            first = first_by_normalized_digest.get(digest)
            if first is None and best is not None:
                first = best[1]
            first_by_normalized_digest.setdefault(digest, index)
            shingle_sets.append(shingles)
            for fingerprint in fingerprints:
                bucket = fingerprint_buckets.setdefault(fingerprint, [])
                if len(bucket) < 100:
                    bucket.append(index)
            if first is None:
                continue
            relation_id = f"GCL-REL-RM-DUP-{first:05d}-{index:05d}"
            relation_ids_by_index.setdefault(first, []).append(relation_id)
            relation_ids_by_index.setdefault(index, []).append(relation_id)
            duplicate_relations.append({
                "schema_version": SCHEMA_VERSION, "relation_id": relation_id,
                "subject_id": f"GCL-CAT-RM-{index:05d}", "predicate": "duplicate_candidate",
                "object_id": f"GCL-CAT-RM-{first:05d}", "review_state": "AUTOMATED_PROPOSAL",
                "proposer": "deterministic token-shingle candidate cluster v1",
                "evidence": [f"normalized_sha256:{digest}", f"trigram_jaccard:{1.0 if best is None else best[0]:.6f}"],
            })
    write_json(ROOT / "catalog" / "relations" / "researchmath-duplicate-candidates.json", {
        "schema_version": SCHEMA_VERSION,
        "relations": duplicate_relations,
        "authority_boundary": "Exact normalized-text matches are duplicate candidates only. They are not semantic equivalence, implication, campaign authority, mathematical proof, or certification."
    })
    with path.open("rb") as handle:
        for index, raw_with_newline in enumerate(handle):
            raw = raw_with_newline.rstrip(b"\r\n")
            row = json.loads(raw.decode("utf-8"))
            catalog_id = f"GCL-CAT-RM-{index:05d}"
            locator = f"data/train.jsonl#row={index}"
            source_url = (
                "https://huggingface.co/datasets/amphora/ResearchMath-14k/blob/"
                f"{RM_REVISION}/data/train.jsonl"
            )
            original = str(row.get("self_contained_problem") or row.get("original_question") or "").strip()
            if not original:
                raise CatalogError(f"ResearchMath row {index} has no problem representation")
            taxonomy = [
                str(row[key]).strip() for key in ("taxonomy_level_1", "taxonomy_level_2", "taxonomy_level_3")
                if row.get(key)
            ]
            status: list[dict[str, str]] = []
            if row.get("open_status") not in (None, ""):
                status.append(assertion("amphora/ResearchMath-14k", f"open_status:{row['open_status']}", locator))
            if row.get("status_search_result") not in (None, ""):
                status.append(assertion("amphora/ResearchMath-14k", str(row["status_search_result"]), locator))
            if row.get("status_evidence") not in (None, ""):
                status.append(assertion("amphora/ResearchMath-14k", row["status_evidence"], locator))
            ambiguities: list[str] = []
            if str(row.get("open_status", "")).lower() in {"", "unknown", "unclear"}:
                ambiguities.append("Provider status is missing or expressly unresolved.")
            if not row.get("status_evidence_urls"):
                ambiguities.append("No provider status-evidence URL was supplied.")
            status_prose = str(row.get("status_search_result", ""))
            evidence_years = [int(value) for value in re.findall(r"\b(?:19|20)[0-9]{2}\b", status_prose)]
            if evidence_years and max(evidence_years) < 2024:
                ambiguities.append("Provider status evidence may be stale; its newest explicit year predates 2024.")
            asserted = str(row.get("open_status", "")).lower()
            uncertain_prose = any(marker in status_prose.lower() for marker in ("unclear", "unknown", "did not locate", "not definitively"))
            if asserted not in {"", "unknown", "unclear"} and uncertain_prose:
                ambiguities.append("Provider status field and status-search prose may be contradictory.")
            if relation_ids_by_index.get(index):
                ambiguities.append("Automated exact-text duplicate candidate requires human semantic review.")
            yield {
                "schema_version": SCHEMA_VERSION,
                "catalog_id": catalog_id,
                "provider_id": RM_PROVIDER,
                "snapshot_id": RM_SNAPSHOT,
                "source": {"locator": locator, "url": source_url, "raw_sha256": sha256_bytes(raw)},
                "statement_kind": "problem",
                "representations": {
                    "original": original,
                    "normalized": normalized_text(original),
                    "normalization_method": "unicode-preserving newline and trailing-whitespace normalization v1",
                },
                "classification": {
                    "msc2020_primary": RM_MSC.get(str(row.get("taxonomy_level_1", ""))),
                    "mapping_method": "deterministic broad MSC2020 projection from provider level-1 taxonomy; not human semantic review",
                    "facets": sorted(set(taxonomy + [f"paper_id:{row.get('paper_id', 'unknown')}"])),
                },
                "status_assertions": status,
                "proof_annotations": [],
                "licensing": {"license": "MIT with per-entry source terms retained", "redistribution_class": "full_text"},
                "assurance": {"tier": "NORMALIZED_REPLAYED", "evidence": [f"sha256:{sha256_bytes(raw)}", "catalog/build_semantic_catalog.py@2.0.0"]},
                "relation_ids": relation_ids_by_index.get(index, []),
                "unresolved_ambiguities": ambiguities,
                "excluded_inferences": EXCLUDED_INFERENCES,
                "claim_boundary": CLAIM_BOUNDARY,
            }


def build_researchmath(args: argparse.Namespace) -> None:
    path = args.input.resolve()
    if sha256_file(path) != RM_SOURCE_SHA256:
        raise CatalogError("ResearchMath source object does not match the admitted LFS sha256")
    shards, count = write_shards("researchmath", researchmath_entries(path))
    if count != 14_056:
        raise CatalogError(f"ResearchMath inventory mismatch: expected 14056, found {count}")
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "snapshot_id": RM_SNAPSHOT,
        "provider_id": RM_PROVIDER,
        "revision": RM_REVISION,
        "admitted_at": args.admitted_at,
        "admission_basis": {"revision_kind": "exact_commit", "benchmark_tag": None, "tag_exception_reason": "The dataset provider does not publish bench-v benchmark releases; the exact repository commit and LFS object are locked."},
        "source_objects": [{"locator": "data/train.jsonl", "sha256": RM_SOURCE_SHA256}],
        "inventory_count": count,
        "catalog_shards": shards,
        "replay": {
            "adapter": "catalog/build_semantic_catalog.py", "adapter_version": "2.0.0",
            "command": "python catalog/build_semantic_catalog.py build-researchmath --input <pinned-train.jsonl> --admitted-at <timestamp>",
            "environment": ["Python >=3.11", "jsonschema >=4"], "deterministic": True,
        },
        "claim_boundary": CLAIM_BOUNDARY,
    }
    write_json(PROVIDER_DIR / f"{RM_SNAPSHOT}.json", manifest)
    taxonomy = Counter()
    statuses = Counter()
    with path.open("r", encoding="utf-8") as source:
        for line in source:
            row = json.loads(line)
            taxonomy[str(row.get("taxonomy_level_1", "UNCLASSIFIED"))] += 1
            statuses[str(row.get("open_status", "UNATTRIBUTED"))] += 1
    write_json(PROVIDER_DIR / f"{RM_SNAPSHOT}-composition.json", {
        "schema_version": SCHEMA_VERSION, "provider_id": RM_PROVIDER, "snapshot_id": RM_SNAPSHOT,
        "inventory_count": count, "taxonomy_level_1": dict(sorted(taxonomy.items())),
        "provider_status_assertions": dict(sorted(statuses.items())),
        "claim_boundary": "These counts summarize provider metadata and catalog accounting only. Status counts are attributed to the provider and are not Programme determinations."
    })


def derive_source_path(module: str) -> str:
    if not module.startswith("FormalConjectures."):
        raise CatalogError(f"DeepMind declaration outside FormalConjectures: {module}")
    components: list[str] = []
    current: list[str] = []
    quoted = False
    for character in module:
        if character == "«":
            if quoted:
                raise CatalogError(f"nested quoted module component: {module}")
            quoted = True
            continue
        if character == "»":
            if not quoted:
                raise CatalogError(f"unmatched module quote: {module}")
            quoted = False
            continue
        if character == "." and not quoted:
            components.append("".join(current))
            current = []
            continue
        current.append(character)
    if quoted:
        raise CatalogError(f"unterminated quoted module component: {module}")
    components.append("".join(current))
    if any(not component or component in {".", ".."} for component in components):
        raise CatalogError(f"invalid module component: {module}")
    return "/".join(components) + ".lean"


def msc_from_subjects(subjects: list[str]) -> str | None:
    for subject in subjects:
        value = subject.strip().upper()
        if re.fullmatch(r"[0-9]", value):
            value = value.zfill(2)
        if re.fullmatch(r"[0-9]{2}[A-Z-][0-9X]{2}", value):
            return value
        if re.fullmatch(r"[0-9]{2}", value):
            return value + "-XX"
    return None


def formal_conjecture_entries(checkout: Path, inventory: dict[str, Any]) -> Iterator[dict[str, Any]]:
    problems = inventory.get("problems")
    if not isinstance(problems, list) or not problems:
        raise CatalogError("DeepMind extractor inventory has no non-empty problems array")
    toolchain = (checkout / "lean-toolchain").read_text(encoding="utf-8").strip()
    ordered = sorted(problems, key=lambda item: (str(item.get("module", "")), str(item.get("theorem", ""))))
    seen: set[str] = set()
    for problem in ordered:
        theorem = str(problem.get("theorem", "")).strip()
        module = str(problem.get("module", "")).strip()
        statement = str(problem.get("statement", "")).strip()
        if not theorem or not module or not statement:
            raise CatalogError("DeepMind declaration is missing theorem, module, or statement")
        stable = hashlib.sha256(theorem.encode("utf-8")).hexdigest()[:16].upper()
        catalog_id = f"GCL-CAT-FC-{stable}"
        if catalog_id in seen:
            raise CatalogError(f"duplicate DeepMind theorem identity: {theorem}")
        seen.add(catalog_id)
        source_path = derive_source_path(module)
        if not (checkout / source_path).is_file():
            raise CatalogError(f"missing source file for {theorem}: {source_path}")
        locator = f"{source_path}#{theorem}"
        source_url = f"https://github.com/google-deepmind/formal-conjectures/blob/{FC_REVISION}/{source_path}"
        subjects = sorted(str(value) for value in problem.get("subjects", []))
        status = []
        if problem.get("category") is not None:
            status.append(assertion("google-deepmind/formal-conjectures", f"category:{problem['category']}", locator))
        for answer_kind in problem.get("answerKinds", []):
            status.append(assertion("google-deepmind/formal-conjectures extractor", f"answer_kind:{answer_kind}", locator))
        proof = [assertion(
            "google-deepmind/formal-conjectures extractor",
            f"has_sorry_free_proof:{str(bool(problem.get('hasSorryFreeProof', False))).lower()}",
            locator,
        )]
        if problem.get("formalProofKind") is not None or problem.get("formalProofLink") is not None:
            proof.append(assertion("google-deepmind/formal-conjectures", {
                "formal_proof_kind": problem.get("formalProofKind"), "formal_proof_link": problem.get("formalProofLink")
            }, locator))
        ambiguities = []
        if not problem.get("hasSorryFreeProof", False):
            ambiguities.append("The extracted declaration contains or depends on a proof placeholder.")
        if str(problem.get("category", "")).lower() == "research solved" and problem.get("formalProofKind") is None:
            ambiguities.append("Provider category says research solved but no formal-proof annotation is present.")
        reviewed = REVIEWED_RELATIONS.get(theorem)
        relation_ids = [reviewed[0]] if reviewed else []
        assurance_tier = reviewed[1] if reviewed else "NORMALIZED_REPLAYED"
        assurance: dict[str, Any] = {
            "tier": assurance_tier,
            "evidence": [f"sha256:{sha256_bytes(statement.encode('utf-8'))}", "catalog/build_semantic_catalog.py@2.0.0"],
        }
        if reviewed:
            assurance["reviewer"] = "MATHFORGE historical concordance review"
        yield {
            "schema_version": SCHEMA_VERSION,
            "catalog_id": catalog_id,
            "provider_id": FC_PROVIDER,
            "snapshot_id": FC_SNAPSHOT,
            "source": {"locator": locator, "url": source_url, "raw_sha256": sha256_bytes(statement.encode("utf-8"))},
            "statement_kind": "formal_declaration",
            "representations": {"original": statement, "normalized": normalized_text(statement), "normalization_method": "Lean extractor statement with newline and trailing-whitespace normalization v1"},
            "formal_language": {"language": "Lean 4", "toolchain": toolchain, "declaration_name": theorem, "source_path": source_path},
            "classification": {"msc2020_primary": msc_from_subjects(subjects), "mapping_method": "source AMS/MSC tag projection without semantic promotion", "facets": sorted(set(subjects + [f"category:{problem.get('category', 'unattributed')}" ]))},
            "status_assertions": status,
            "proof_annotations": proof,
            "licensing": {"license": "CC-BY-4.0 with per-source third-party terms retained", "redistribution_class": "metadata_only"},
            "assurance": assurance,
            "relation_ids": relation_ids,
            "unresolved_ambiguities": ambiguities,
            "excluded_inferences": EXCLUDED_INFERENCES,
            "claim_boundary": CLAIM_BOUNDARY,
        }


def build_formal_conjectures(args: argparse.Namespace) -> None:
    checkout = args.checkout.resolve()
    inventory_path = args.inventory.resolve()
    actual = git(checkout, "rev-parse", "HEAD")
    if actual != FC_REVISION:
        raise CatalogError(f"DeepMind checkout mismatch: expected {FC_REVISION}, found {actual}")
    inventory = load_json(inventory_path)
    shards, count = write_shards("formal-conjectures", formal_conjecture_entries(checkout, inventory))
    if count != 3_232:
        raise CatalogError(f"DeepMind inventory mismatch: expected 3232, found {count}")
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "snapshot_id": FC_SNAPSHOT,
        "provider_id": FC_PROVIDER,
        "revision": FC_REVISION,
        "admitted_at": args.admitted_at,
        "admission_basis": {"revision_kind": "exact_commit", "benchmark_tag": None, "tag_exception_reason": "No immutable bench-v release contains the admitted revision; see the retained FC-GDM-002 tag-resolution evidence."},
        "source_objects": [
            {"locator": "canonical extract_names inventory", "sha256": canonical_inventory_sha256(inventory)},
            {"locator": "lean-toolchain", "sha256": sha256_file(checkout / "lean-toolchain")},
        ],
        "inventory_count": count,
        "catalog_shards": shards,
        "replay": {
            "adapter": "catalog/build_semantic_catalog.py", "adapter_version": "2.0.0",
            "command": "lake exe extract_names FormalConjectures --exclude=docstring,moduleDocstrings; python catalog/build_semantic_catalog.py build-formal-conjectures --checkout <pinned-checkout> --inventory <extract-names.json> --admitted-at <timestamp>",
            "environment": ["leanprover/lean4:v4.27.0", "Python >=3.11", "jsonschema >=4"], "deterministic": True,
        },
        "claim_boundary": CLAIM_BOUNDARY,
    }
    write_json(PROVIDER_DIR / f"{FC_SNAPSHOT}.json", manifest)
    problems = inventory["problems"]
    categories = Counter(str(item.get("category", "UNATTRIBUTED")) for item in problems)
    subjects = Counter(subject for item in problems for subject in item.get("subjects", []))
    proof_kinds = Counter(str(item.get("formalProofKind")) for item in problems if item.get("formalProofKind") is not None)
    answer_kinds = Counter(str(answer) for item in problems for answer in item.get("answerKinds", []))
    write_json(PROVIDER_DIR / f"{FC_SNAPSHOT}-composition.json", {
        "schema_version": SCHEMA_VERSION, "provider_id": FC_PROVIDER, "snapshot_id": FC_SNAPSHOT,
        "inventory_count": count, "categories": dict(sorted(categories.items())),
        "ams_or_subject_tags": dict(sorted(subjects.items())), "formal_proof_kinds": dict(sorted(proof_kinds.items())),
        "answer_kinds": dict(sorted(answer_kinds.items())),
        "sorry_free_declarations": sum(bool(item.get("hasSorryFreeProof", False)) for item in problems),
        "placeholder_or_unproved_declarations": sum(not bool(item.get("hasSorryFreeProof", False)) for item in problems),
        "claim_boundary": "These counts summarize source annotations and replay metadata only. Research-solved categories remain distinct from formal-proof availability and from MATHCERT certification."
    })


def finalize(args: argparse.Namespace) -> None:
    manifests = [load_json(PROVIDER_DIR / f"{snapshot}.json") for snapshot in (RM_SNAPSHOT, FC_SNAPSHOT)]
    total = sum(int(item["inventory_count"]) for item in manifests)
    public = sum(int(item["inventory_count"]) for item in manifests)
    write_json(ROOT / "catalog" / "manifest.json", {
        "schema_version": SCHEMA_VERSION,
        "catalog_release_id": "GCL-CATALOG-TWO-PROVIDER-001",
        "generated_at": args.generated_at,
        "provider_snapshots": [RM_SNAPSHOT, FC_SNAPSHOT],
        "total_entries": total,
        "public_entries": public,
        "assurance_vocabulary": ["SOURCE_LOCKED", "NORMALIZED_REPLAYED", "SEMANTICALLY_REVIEWED", "CAMPAIGN_CONCORDANT"],
        "relation_vocabulary": ["same_statement", "formalizes", "specializes", "generalizes", "implies", "related", "duplicate_candidate", "conflicts", "rejected_match"],
        "authority_boundary": "The catalog exposes provenance and assurance metadata. It is not a canonical claim ledger, does not itself create a MATHSOLVE result or campaign target, and cannot issue or imply a MATHCERT certificate."
    })


def schema_validator(name: str) -> Draft202012Validator:
    return Draft202012Validator(load_json(SCHEMA_DIR / name), format_checker=FormatChecker())


def relation_policy_errors(relation: dict[str, Any]) -> list[str]:
    errors = []
    if relation.get("review_state") == "AUTOMATED_PROPOSAL" and relation.get("predicate") not in {"related", "duplicate_candidate"}:
        errors.append(f"{relation.get('relation_id')}: automated proposal exceeds permitted relation types")
    if relation.get("review_state") == "HUMAN_REVIEWED" and not relation.get("reviewer"):
        errors.append(f"{relation.get('relation_id')}: human-reviewed relation requires a reviewer")
    return errors


def catalog_validation_errors() -> list[str]:
    errors: list[str] = []
    manifest = load_json(ROOT / "catalog" / "manifest.json")
    for error in schema_validator("semantic_catalog_manifest.schema.json").iter_errors(manifest):
        errors.append(f"catalog/manifest.json: {error.message}")
    total = 0
    seen: set[str] = set()
    entry_relations: dict[str, set[str]] = {}
    entry_tiers: dict[str, str] = {}
    entry_validator = schema_validator("semantic_catalog_entry.schema.json")
    for snapshot in manifest.get("provider_snapshots", []):
        provider_path = PROVIDER_DIR / f"{snapshot}.json"
        provider = load_json(provider_path)
        for error in schema_validator("external_source_snapshot.schema.json").iter_errors(provider):
            errors.append(f"{provider_path.relative_to(ROOT)}: {error.message}")
        provider_total = 0
        for shard in provider.get("catalog_shards", []):
            path = ROOT / shard["path"]
            if not path.is_file():
                errors.append(f"missing catalog shard: {shard['path']}")
                continue
            payload = path.read_bytes()
            if len(payload) != shard["byte_length"] or sha256_bytes(payload) != shard["sha256"]:
                errors.append(f"catalog shard identity mismatch: {shard['path']}")
            lines = payload.splitlines()
            if len(lines) != shard["entry_count"]:
                errors.append(f"catalog shard count mismatch: {shard['path']}")
            for number, line in enumerate(lines, 1):
                entry = json.loads(line)
                for error in entry_validator.iter_errors(entry):
                    errors.append(f"{shard['path']}:{number}: {error.message}")
                catalog_id = entry.get("catalog_id")
                if catalog_id in seen:
                    errors.append(f"duplicate catalog_id: {catalog_id}")
                seen.add(catalog_id)
                entry_relations[str(catalog_id)] = set(entry.get("relation_ids", []))
                entry_tiers[str(catalog_id)] = str(entry.get("assurance", {}).get("tier", ""))
                if entry_tiers[str(catalog_id)] in {"SEMANTICALLY_REVIEWED", "CAMPAIGN_CONCORDANT"} and not entry.get("assurance", {}).get("reviewer"):
                    errors.append(f"{catalog_id}: reviewed assurance tier requires a reviewer")
                if entry_tiers[str(catalog_id)] == "CAMPAIGN_CONCORDANT" and not entry_relations[str(catalog_id)]:
                    errors.append(f"{catalog_id}: campaign-concordant tier requires a typed relation")
                for field in ("status_assertions", "proof_annotations"):
                    if any(not item.get("issuer") for item in entry.get(field, [])):
                        errors.append(f"{catalog_id}: unattributed {field}")
            provider_total += len(lines)
        if provider_total != provider.get("inventory_count"):
            errors.append(f"{snapshot}: provider inventory accounting mismatch")
        total += provider_total
    if total != manifest.get("total_entries"):
        errors.append("catalog manifest total_entries mismatch")
    relation_validator = schema_validator("semantic_relation.schema.json")
    relation_ids: set[str] = set()
    reviewed_campaign_relations: set[str] = set()
    for relation_path in sorted((ROOT / "catalog" / "relations").glob("*.json")):
        for relation in load_json(relation_path).get("relations", []):
            for error in relation_validator.iter_errors(relation):
                errors.append(f"{relation.get('relation_id')}: {error.message}")
            relation_id = relation.get("relation_id")
            if relation_id in relation_ids:
                errors.append(f"duplicate relation_id: {relation_id}")
            relation_ids.add(relation_id)
            errors.extend(relation_policy_errors(relation))
            if relation.get("review_state") == "HUMAN_REVIEWED" and (
                str(relation.get("subject_id", "")).startswith("GCL-CAMPAIGN:")
                or str(relation.get("object_id", "")).startswith("GCL-CAMPAIGN:")
            ):
                reviewed_campaign_relations.add(str(relation_id))
    for catalog_id, references in entry_relations.items():
        missing = references - relation_ids
        if missing:
            errors.append(f"{catalog_id}: unknown relation references {sorted(missing)}")
        if entry_tiers[catalog_id] == "CAMPAIGN_CONCORDANT" and not (references & reviewed_campaign_relations):
            errors.append(f"{catalog_id}: campaign-concordant tier lacks a human-reviewed campaign relation")
    return errors


def verify_catalog(_: argparse.Namespace) -> None:
    errors = catalog_validation_errors()
    if errors:
        raise CatalogError("\n".join(errors))
    manifest = load_json(ROOT / "catalog" / "manifest.json")
    print(f"semantic catalog valid: {manifest['total_entries']} entries")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    rm = sub.add_parser("build-researchmath")
    rm.add_argument("--input", type=Path, required=True)
    rm.add_argument("--admitted-at", default="2026-09-22T06:34:00Z")
    fc = sub.add_parser("build-formal-conjectures")
    fc.add_argument("--checkout", type=Path, required=True)
    fc.add_argument("--inventory", type=Path, required=True)
    fc.add_argument("--admitted-at", default="2026-09-22T06:34:00Z")
    final = sub.add_parser("finalize")
    final.add_argument("--generated-at", default="2026-09-22T06:34:00Z")
    sub.add_parser("verify")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    commands = {
        "build-researchmath": build_researchmath,
        "build-formal-conjectures": build_formal_conjectures,
        "finalize": finalize,
        "verify": verify_catalog,
    }
    try:
        commands[args.command](args)
    except (CatalogError, OSError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"catalog error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
