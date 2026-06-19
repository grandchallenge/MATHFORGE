#!/usr/bin/env python3
"""Search approved discovery providers and emit normalized records."""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import urlencode

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from discovery.adapters import (  # noqa: E402
    DiscoveryError,
    cache_raw,
    fetch_bytes,
    iso_now,
    make_batch,
    parse_arxiv,
    parse_openalex,
    parse_zbmath,
    require_openalex_key,
    require_zbmath_terms,
)

ROOT = Path(__file__).resolve().parents[1]


def read_query(path: str | None) -> str:
    if not path:
        return ""
    query = Path(path).read_text(encoding="utf-8").strip()
    if not query:
        raise DiscoveryError("query file is empty")
    return query


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", required=True, choices=("zbmath", "openalex", "arxiv"))
    parser.add_argument("--query-file")
    parser.add_argument("--semantic", action="store_true")
    parser.add_argument("--category")
    parser.add_argument("--since")
    parser.add_argument("--max-results", type=int, default=25)
    parser.add_argument("--max-pages", type=int, default=1)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--ack-zbmath-terms", action="store_true")
    args = parser.parse_args()

    if args.max_results < 1 or args.max_results > 100:
        raise DiscoveryError("--max-results must be between 1 and 100")
    if args.max_pages < 1:
        raise DiscoveryError("--max-pages must be positive")

    query_text = read_query(args.query_file)
    retrieved_at = iso_now()
    cache_root = ROOT / ".cache" / "discovery"
    all_records = []

    if args.provider == "zbmath":
        if not query_text:
            raise DiscoveryError("zbMATH requires --query-file")
        require_zbmath_terms(
            args.ack_zbmath_terms, os.environ.get("ZBMATH_TERMS_ACCEPTED")
        )
        query = {"mode": "keyword", "text": query_text}
        for page in range(args.max_pages):
            params = urlencode(
                {"search_string": query_text, "page": page, "results_per_page": args.max_results}
            )
            url = f"https://api.zbmath.org/v1/document/_search?{params}"
            raw = fetch_bytes(url, headers={"Accept": "application/json"})
            cache_raw(cache_root, "zbmath", page, raw, "json")
            records = parse_zbmath(raw, url, retrieved_at)
            all_records.extend(records)
            if len(records) < args.max_results:
                break
    elif args.provider == "openalex":
        if not query_text:
            raise DiscoveryError("OpenAlex requires --query-file")
        api_key = os.environ.get("OPENALEX_API_KEY")
        require_openalex_key(args.semantic, api_key)
        query = {"mode": "semantic" if args.semantic else "keyword", "text": query_text}
        for page in range(1, args.max_pages + 1):
            public_params = {
                "search.semantic" if args.semantic else "search": query_text,
                "per_page": args.max_results,
                "page": page,
            }
            public_url = f"https://api.openalex.org/works?{urlencode(public_params)}"
            params = dict(public_params)
            if api_key:
                params["api_key"] = api_key
            url = f"https://api.openalex.org/works?{urlencode(params)}"
            raw = fetch_bytes(url, headers={"Accept": "application/json"})
            cache_raw(cache_root, "openalex", page, raw, "json")
            records = parse_openalex(raw, public_url, retrieved_at)
            all_records.extend(records)
            if len(records) < args.max_results:
                break
    else:
        if not args.category:
            raise DiscoveryError("arXiv requires --category")
        search_query = f"cat:{args.category}"
        if args.since:
            compact_date = args.since.replace("-", "")
            if len(compact_date) != 8 or not compact_date.isdigit():
                raise DiscoveryError("--since must use YYYY-MM-DD")
            search_query += f" AND submittedDate:[{compact_date}0000 TO 999912312359]"
        query = {"mode": "category", "category": args.category}
        if args.since:
            query["since"] = args.since
        for page in range(args.max_pages):
            if page:
                time.sleep(3.0)
            params = urlencode(
                {
                    "search_query": search_query,
                    "start": page * args.max_results,
                    "max_results": args.max_results,
                    "sortBy": "submittedDate",
                    "sortOrder": "descending",
                }
            )
            url = f"https://export.arxiv.org/api/query?{params}"
            raw = fetch_bytes(url, headers={"Accept": "application/atom+xml"})
            cache_raw(cache_root, "arxiv", page, raw, "xml")
            records = parse_arxiv(raw, url, retrieved_at)
            all_records.extend(records)
            if len(records) < args.max_results:
                break

    batch = make_batch(args.provider, query, retrieved_at, all_records)
    rendered = json.dumps(batch, indent=2, ensure_ascii=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DiscoveryError as exc:
        print(f"discovery error: {exc}", file=sys.stderr)
        raise SystemExit(2)
