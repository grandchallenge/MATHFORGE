#!/usr/bin/env python3
"""Provider adapters for normalized mathematical literature discovery."""
from __future__ import annotations

import hashlib
import json
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

USER_AGENT = "MATHFORGE-Discovery/1.0 (+https://github.com/fyremael/MATHFORGE)"
ARXIV_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


class DiscoveryError(RuntimeError):
    pass


def require_openalex_key(semantic: bool, api_key: str | None) -> None:
    if semantic and not api_key:
        raise DiscoveryError("OpenAlex semantic search requires OPENALEX_API_KEY")


def require_zbmath_terms(acknowledged: bool, environment_value: str | None) -> None:
    accepted = (environment_value or "").lower() in {"1", "true", "yes"}
    if not acknowledged and not accepted:
        raise DiscoveryError(
            "zbMATH access requires --ack-zbmath-terms or ZBMATH_TERMS_ACCEPTED=yes"
        )


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def content_hash(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def normalize_doi(value: str | None) -> str | None:
    if not value:
        return None
    doi = value.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.startswith(prefix):
            doi = doi[len(prefix) :]
    return doi or None


def normalize_arxiv_id(value: str | None) -> str | None:
    if not value:
        return None
    identifier = value.strip()
    for prefix in ("https://arxiv.org/abs/", "http://arxiv.org/abs/", "arxiv:"):
        if identifier.lower().startswith(prefix):
            identifier = identifier[len(prefix) :]
            break
    if "v" in identifier and identifier.rsplit("v", 1)[-1].isdigit():
        identifier = identifier.rsplit("v", 1)[0]
    return identifier or None


def stable_record_id(provider: str, provider_id: str, identifiers: dict[str, str]) -> str:
    doi = normalize_doi(identifiers.get("doi"))
    if doi:
        return f"doi:{doi}"
    arxiv_id = normalize_arxiv_id(identifiers.get("arxiv"))
    if arxiv_id:
        return f"arxiv:{arxiv_id}"
    return f"{provider}:{provider_id}"


def deduplicate_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    deduplicated: dict[str, dict[str, Any]] = {}
    for record in records:
        key = stable_record_id(record["provenance"]["source_id"], record["provider_id"], record["identifiers"])
        record["record_id"] = key
        if key not in deduplicated:
            deduplicated[key] = record
            continue
        existing = deduplicated[key]
        existing["identifiers"].update(record["identifiers"])
        seen_classes = {
            (item["scheme"], item["identifier"], item.get("role"))
            for item in existing["classifications"]
        }
        for item in record["classifications"]:
            marker = (item["scheme"], item["identifier"], item.get("role"))
            if marker not in seen_classes:
                existing["classifications"].append(item)
                seen_classes.add(marker)
    return list(deduplicated.values())


def fetch_bytes(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    timeout: int = 30,
    retries: int = 2,
    opener: Callable[..., Any] = urlopen,
    sleeper: Callable[[float], None] = time.sleep,
) -> bytes:
    request_headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    request_headers.update(headers or {})
    request = Request(url, headers=request_headers)
    for attempt in range(retries + 1):
        try:
            with opener(request, timeout=timeout) as response:
                return response.read()
        except HTTPError as exc:
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or attempt >= retries:
                raise DiscoveryError(f"provider request failed with HTTP {exc.code}: {url}") from exc
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            if retry_after:
                try:
                    delay = float(retry_after)
                except ValueError:
                    delay = max(0.0, (parsedate_to_datetime(retry_after) - datetime.now(timezone.utc)).total_seconds())
            else:
                delay = 2**attempt
            sleeper(delay)
        except URLError as exc:
            if attempt >= retries:
                raise DiscoveryError(f"provider request failed: {url}: {exc.reason}") from exc
            sleeper(2**attempt)
    raise AssertionError("unreachable")


def cache_raw(cache_root: Path, provider: str, page: int, raw: bytes, extension: str) -> Path:
    directory = cache_root / provider
    directory.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(raw).hexdigest()[:16]
    path = directory / f"page-{page:04d}-{digest}.{extension}"
    path.write_bytes(raw)
    return path


def parse_json(raw: bytes, provider: str) -> dict[str, Any]:
    try:
        data = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise DiscoveryError(f"{provider} returned malformed JSON") from exc
    if not isinstance(data, dict):
        raise DiscoveryError(f"{provider} returned a non-object JSON response")
    return data


def parse_zbmath(raw: bytes, query_url: str, retrieved_at: str) -> list[dict[str, Any]]:
    data = parse_json(raw, "zbMATH")
    results = data.get("result")
    if not isinstance(results, list):
        raise DiscoveryError("zbMATH response is missing result list")
    digest = content_hash(raw)
    records = []
    for item in results:
        title = item.get("title", {})
        title_text = title.get("title") if isinstance(title, dict) else str(title)
        provider_id = str(item.get("identifier") or item.get("id") or "")
        if not provider_id or not title_text:
            continue
        authors = [
            author.get("name", "")
            for author in item.get("contributors", {}).get("authors", [])
            if author.get("name")
        ]
        identifiers = {"zbmath": provider_id}
        for link in item.get("links", []):
            link_type = str(link.get("type", "")).lower()
            value = link.get("identifier") or link.get("url")
            if link_type == "doi" and normalize_doi(value):
                identifiers["doi"] = normalize_doi(value) or ""
            if link_type == "arxiv" and normalize_arxiv_id(value):
                identifiers["arxiv"] = normalize_arxiv_id(value) or ""
        classifications = [
            {
                "scheme": str(msc.get("scheme") or "msc2020").upper(),
                "identifier": str(msc.get("code")),
                "role": "provider-assigned",
            }
            for msc in item.get("msc", [])
            if msc.get("code")
        ]
        year = item.get("year")
        records.append(
            {
                "record_id": "",
                "provider_id": provider_id,
                "title": title_text,
                "authors": authors,
                "publication_year": int(year) if str(year).isdigit() else None,
                "identifiers": identifiers,
                "classifications": classifications,
                "metrics": {},
                "provenance": {
                    "source_id": "zbmath_open",
                    "query_url": query_url,
                    "retrieved_at": retrieved_at,
                },
                "content_hash": digest,
                "review_status": "UNREVIEWED",
            }
        )
    return deduplicate_records(records)


def parse_openalex(raw: bytes, query_url: str, retrieved_at: str) -> list[dict[str, Any]]:
    data = parse_json(raw, "OpenAlex")
    results = data.get("results")
    if not isinstance(results, list):
        raise DiscoveryError("OpenAlex response is missing results list")
    digest = content_hash(raw)
    records = []
    for item in results:
        provider_id = str(item.get("id", "")).rsplit("/", 1)[-1]
        title = item.get("title")
        if not provider_id or not title:
            continue
        authors = [
            authorship.get("author", {}).get("display_name", "")
            for authorship in item.get("authorships", [])
            if authorship.get("author", {}).get("display_name")
        ]
        identifiers = {"openalex": provider_id}
        doi = normalize_doi(item.get("doi") or item.get("ids", {}).get("doi"))
        if doi:
            identifiers["doi"] = doi
        arxiv_id = normalize_arxiv_id(item.get("ids", {}).get("arxiv"))
        if arxiv_id:
            identifiers["arxiv"] = arxiv_id
        classifications = []
        primary_topic = item.get("primary_topic")
        if isinstance(primary_topic, dict) and primary_topic.get("id"):
            classifications.append(
                {
                    "scheme": "OPENALEX",
                    "identifier": str(primary_topic["id"]).rsplit("/", 1)[-1],
                    "role": "primary-topic",
                }
            )
        for topic in item.get("topics", []):
            if topic.get("id"):
                classifications.append(
                    {
                        "scheme": "OPENALEX",
                        "identifier": str(topic["id"]).rsplit("/", 1)[-1],
                        "role": "topic",
                    }
                )
        records.append(
            {
                "record_id": "",
                "provider_id": provider_id,
                "title": title,
                "authors": authors,
                "publication_year": item.get("publication_year"),
                "identifiers": identifiers,
                "classifications": classifications,
                "metrics": {
                    "cited_by_count": item.get("cited_by_count"),
                    "relevance_score": item.get("relevance_score"),
                },
                "provenance": {
                    "source_id": "openalex",
                    "query_url": query_url,
                    "retrieved_at": retrieved_at,
                },
                "content_hash": digest,
                "review_status": "UNREVIEWED",
            }
        )
    return deduplicate_records(records)


def parse_arxiv(raw: bytes, query_url: str, retrieved_at: str) -> list[dict[str, Any]]:
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        raise DiscoveryError("arXiv returned malformed Atom XML") from exc
    digest = content_hash(raw)
    records = []
    for entry in root.findall("atom:entry", ARXIV_NS):
        id_text = entry.findtext("atom:id", default="", namespaces=ARXIV_NS)
        arxiv_id = normalize_arxiv_id(id_text)
        title = " ".join(entry.findtext("atom:title", default="", namespaces=ARXIV_NS).split())
        if not arxiv_id or not title:
            continue
        authors = [
            name
            for name in (
                author.findtext("atom:name", default="", namespaces=ARXIV_NS)
                for author in entry.findall("atom:author", ARXIV_NS)
            )
            if name
        ]
        identifiers = {"arxiv": arxiv_id}
        doi = normalize_doi(entry.findtext("arxiv:doi", default="", namespaces=ARXIV_NS))
        if doi:
            identifiers["doi"] = doi
        classifications = [
            {
                "scheme": "ARXIV",
                "identifier": category.attrib["term"],
                "role": "category",
            }
            for category in entry.findall("atom:category", ARXIV_NS)
            if category.attrib.get("term")
        ]
        published = entry.findtext("atom:published", default="", namespaces=ARXIV_NS)
        year = int(published[:4]) if len(published) >= 4 and published[:4].isdigit() else None
        records.append(
            {
                "record_id": "",
                "provider_id": arxiv_id,
                "title": title,
                "authors": authors,
                "publication_year": year,
                "identifiers": identifiers,
                "classifications": classifications,
                "metrics": {},
                "provenance": {
                    "source_id": "arxiv",
                    "query_url": query_url,
                    "retrieved_at": retrieved_at,
                },
                "content_hash": digest,
                "review_status": "UNREVIEWED",
            }
        )
    return deduplicate_records(records)


def make_batch(
    provider: str,
    query: dict[str, Any],
    retrieved_at: str,
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    query_key = json.dumps(query, sort_keys=True).encode("utf-8")
    stamp = retrieved_at.replace("-", "").replace(":", "").replace("T", "-").replace("Z", "")
    return {
        "batch_id": f"{provider}-{stamp}-{hashlib.sha256(query_key).hexdigest()[:12]}",
        "provider": provider,
        "query": query,
        "retrieved_at": retrieved_at,
        "records": deduplicate_records(records),
    }
