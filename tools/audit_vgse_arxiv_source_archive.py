#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import re
import tarfile
from pathlib import Path, PurePosixPath

TEXT_EXTS = {".tex", ".bib", ".sty", ".cls", ".txt", ".md", ".asy", ".tikz", ".pgf"}
CODE_EXTS = {".py", ".sage", ".sagews", ".m", ".wl", ".nb", ".ipynb", ".jl", ".r", ".R", ".cpp", ".cc", ".c", ".h", ".hpp", ".sh", ".bash", ".zsh", ".lua"}
DATA_EXTS = {".json", ".csv", ".tsv", ".dat", ".data", ".yaml", ".yml", ".npz", ".npy", ".mat"}
FIGURE_EXTS = {".pdf", ".eps", ".ps", ".svg", ".png", ".jpg", ".jpeg"}
GRAPH_WEIGHT_TERMS = re.compile(r"(?i)\b(weight|weights|weighted|pl[uü]cker|matching|boundary measurement|meas\s*\(|kasteleyn|bipartite graph|t-embedding)\b")
EXAMPLE_MARKERS = [re.compile(r"Example\s+B\.3", re.I), re.compile(r"Example\s+9\.3", re.I)]
INCLUDE_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
CAPTION_RE = re.compile(r"\\caption(?:\[[^\]]*\])?\{")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_members(path: Path) -> tuple[str, list[tuple[str, bytes]]]:
    raw = path.read_bytes()
    archive_sha = sha256_bytes(raw)
    members: list[tuple[str, bytes]] = []
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as archive:
            for member in archive.getmembers():
                if not member.isfile():
                    continue
                handle = archive.extractfile(member)
                if handle is not None:
                    members.append((member.name, handle.read()))
            if members:
                return archive_sha, members
    except tarfile.ReadError:
        pass
    try:
        return archive_sha, [(path.stem or "source.tex", gzip.decompress(raw))]
    except Exception:
        return archive_sha, [("source.bin", raw)]


def decode_text(data: bytes) -> str | None:
    for encoding in ("utf-8", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            pass
    return None


def resolve_asset(source_name: str, target: str, names: set[str]) -> str | None:
    source_dir = str(PurePosixPath(source_name).parent)
    target_path = PurePosixPath(source_dir) / target if source_dir not in ("", ".", "/") else PurePosixPath(target)
    candidates = [str(target_path)]
    if PurePosixPath(target).suffix == "":
        candidates.extend(str(target_path) + ext for ext in sorted(FIGURE_EXTS | TEXT_EXTS))
    for candidate in candidates:
        normalized = str(PurePosixPath(candidate))
        if normalized.startswith("./"):
            normalized = normalized[2:]
        if normalized in names:
            return normalized
    basename = PurePosixPath(target).name
    matches = [name for name in names if PurePosixPath(name).name == basename or (not PurePosixPath(target).suffix and PurePosixPath(name).stem == basename)]
    return matches[0] if len(matches) == 1 else None


def structural_window(lines: list[str], marker_index: int, radius: int = 100) -> dict:
    start = max(0, marker_index - radius)
    end = min(len(lines), marker_index + radius + 1)
    window = "\n".join(lines[start:end])
    return {
        "line_start": start + 1,
        "line_end": end,
        "includegraphics_targets": sorted(set(INCLUDE_RE.findall(window))),
        "input_targets": sorted(set(INPUT_RE.findall(window))),
        "labels": sorted(set(LABEL_RE.findall(window))),
        "caption_command_present": bool(CAPTION_RE.search(window)),
        "graph_weight_terms_present": sorted(set(match.group(1).lower() for match in GRAPH_WEIGHT_TERMS.finditer(window))),
        "window_sha256": sha256_bytes(window.encode("utf-8", errors="replace")),
    }


def build_record(path: Path) -> dict:
    archive_sha, members = load_members(path)
    names = {name for name, _ in members}
    inventory = []
    text_cache: dict[str, str] = {}
    for name, data in members:
        ext = PurePosixPath(name).suffix.lower()
        kind = "code" if ext in CODE_EXTS else "data" if ext in DATA_EXTS else "figure" if ext in FIGURE_EXTS else "text" if ext in TEXT_EXTS else "other"
        inventory.append({"path": name, "size_bytes": len(data), "sha256": sha256_bytes(data), "extension": ext, "class": kind})
        if ext in TEXT_EXTS or ext in CODE_EXTS or ext in DATA_EXTS:
            text = decode_text(data)
            if text is not None:
                text_cache[name] = text

    example_hits = []
    figure_refs = []
    for name, text in text_cache.items():
        lines = text.splitlines()
        for marker in EXAMPLE_MARKERS:
            for match in marker.finditer(text):
                line_index = text[: match.start()].count("\n")
                window = structural_window(lines, line_index)
                hit = {"source_file": name, "marker": match.group(0), "line": line_index + 1, **window}
                hit["resolved_figure_assets"] = [
                    {"target": target, "resolved_member": resolve_asset(name, target, names)}
                    for target in window["includegraphics_targets"]
                ]
                example_hits.append(hit)
        for target in INCLUDE_RE.findall(text):
            figure_refs.append({"source_file": name, "target": target, "resolved_member": resolve_asset(name, target, names)})

    code_members = [item for item in inventory if item["class"] == "code"]
    data_members = [item for item in inventory if item["class"] == "data"]
    figure_members = [item for item in inventory if item["class"] == "figure"]
    generation_term_hits = []
    for name, text in text_cache.items():
        if PurePosixPath(name).suffix.lower() not in CODE_EXTS | DATA_EXTS:
            continue
        terms = sorted(set(match.group(1).lower() for match in GRAPH_WEIGHT_TERMS.finditer(text)))
        if terms:
            generation_term_hits.append({"path": name, "terms": terms, "sha256": sha256_bytes(text.encode("utf-8", errors="replace"))})

    return {
        "schema_version": "1.0.0",
        "audit_id": "VGSE-ARXIV-SOURCE-ARCHIVE-AUDIT-001",
        "campaign_id": "VGSE-001",
        "source": {
            "arxiv_id": "2410.09574v2",
            "acquisition_url": "https://arxiv.org/e-print/2410.09574v2",
            "archive_sha256": archive_sha,
            "archive_size_bytes": path.stat().st_size,
        },
        "member_count": len(inventory),
        "member_inventory": sorted(inventory, key=lambda item: item["path"]),
        "example_markers": example_hits,
        "figure_references": figure_refs,
        "code_members": code_members,
        "data_members": data_members,
        "figure_members": figure_members,
        "generation_term_hits_in_code_or_data": generation_term_hits,
        "interpretation": {
            "source_bytes_committed": False,
            "mathematical_certification_performed": False,
            "c06_reopening_effect": "none_until_reviewed_against_protected_reopening_condition",
            "scope": "source-package inventory and Figure 16 lineage only",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-archive", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = build_record(args.source_archive)
    text = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
