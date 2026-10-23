#!/usr/bin/env python3
"""Replay source-locked OpenAI math family/PDF link index (not a proof check)."""
import argparse
import json
import re
from pathlib import Path


def extract(text):
    blocks = re.findall(r"<tbody><tr>\s*<td>([\s\S]*?)</td>\s*</tr></tbody>", text)
    families = []
    for block in blocks:
        match = re.search(r"\*\*(\d{3})\.\s*([\s\S]*?)\*\*", block)
        if match:
            headline = re.sub(r"<[^>]*>", "", match.group(2))
            headline = re.sub(r"\s+", " ", headline).strip()
            families.append({"family_id": match.group(1), "headline": headline, "manuscripts": []})
            continue
        paper = re.search(r"&emsp;\[([\s\S]*?)\]\((preprints/[^)]+)\)", block)
        if not paper or not families:
            raise ValueError("Unmatched manuscript block")
        families[-1]["manuscripts"].append({
            "title": re.sub(r"\s+", " ", paper.group(1)).strip(),
            "pdf_path": paper.group(2)
        })
    return families


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--contents", type=Path, required=True)
    parser.add_argument("--index", type=Path, required=True)
    args = parser.parse_args()
    index = json.loads(args.index.read_text(encoding="utf-8"))
    actual = extract(args.contents.read_text(encoding="utf-8"))
    count = sum(len(f["manuscripts"]) for f in actual)
    paths = [p["pdf_path"] for f in actual for p in f["manuscripts"]]
    if (len(actual), count, len(set(paths))) != (372, 719, 719):
        raise SystemExit("FAIL: upstream catalogue count / uniqueness drift")
    if index["families"] != actual:
        raise SystemExit("FAIL: index changed relative to exact upstream contents")
    print("PASS: 372 families, 719 unique manuscript links; exact catalogue correspondence")


if __name__ == "__main__":
    main()
