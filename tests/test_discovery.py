from __future__ import annotations

import io
import json
import sys
import unittest
from email.message import Message
from pathlib import Path
from urllib.error import HTTPError, URLError

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from discovery.adapters import (  # noqa: E402
    DiscoveryError,
    deduplicate_records,
    fetch_bytes,
    make_batch,
    parse_arxiv,
    parse_openalex,
    parse_zbmath,
    require_openalex_key,
    require_zbmath_terms,
)

FIXTURES = ROOT / "tests" / "fixtures"
NOW = "2026-06-14T10:00:00Z"
URL = "https://example.test/query"


class Response:
    def __init__(self, payload: bytes):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.payload


class DiscoveryTests(unittest.TestCase):
    def test_zbmath_fixture(self):
        records = parse_zbmath((FIXTURES / "zbmath.json").read_bytes(), URL, NOW)
        self.assertEqual(records[0]["record_id"], "doi:10.1016/0097-3165(92)90068-6")
        self.assertEqual(records[0]["classifications"][0]["identifier"], "05D05")

    def test_openalex_deduplicates_by_doi(self):
        records = parse_openalex((FIXTURES / "openalex.json").read_bytes(), URL, NOW)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["record_id"], "doi:10.1016/0097-3165(92)90068-6")
        self.assertEqual(len(records[0]["classifications"]), 2)

    def test_arxiv_fixture(self):
        records = parse_arxiv((FIXTURES / "arxiv.xml").read_bytes(), URL, NOW)
        self.assertEqual(records[0]["provider_id"], "2306.12351")
        self.assertEqual(records[0]["identifiers"]["arxiv"], "2306.12351")

    def test_malformed_responses_are_rejected(self):
        with self.assertRaises(DiscoveryError):
            parse_openalex(b"{", URL, NOW)
        with self.assertRaises(DiscoveryError):
            parse_arxiv(b"<feed>", URL, NOW)

    def test_rate_limit_retries(self):
        calls = []
        sleeps = []
        headers = Message()
        headers["Retry-After"] = "0"

        def opener(_request, timeout):
            calls.append(timeout)
            if len(calls) == 1:
                raise HTTPError(URL, 429, "rate limited", headers, io.BytesIO())
            return Response(b"ok")

        self.assertEqual(fetch_bytes(URL, opener=opener, sleeper=sleeps.append), b"ok")
        self.assertEqual(len(calls), 2)
        self.assertEqual(sleeps, [0.0])

    def test_provider_outage_fails_after_retries(self):
        calls = []

        def opener(_request, timeout):
            calls.append(timeout)
            raise URLError("offline")

        with self.assertRaises(DiscoveryError):
            fetch_bytes(URL, opener=opener, sleeper=lambda _delay: None, retries=2)
        self.assertEqual(len(calls), 3)

    def test_arxiv_id_deduplication(self):
        record = parse_arxiv((FIXTURES / "arxiv.xml").read_bytes(), URL, NOW)[0]
        duplicate = json.loads(json.dumps(record))
        duplicate["provider_id"] = "2306.12351v3"
        self.assertEqual(len(deduplicate_records([record, duplicate])), 1)

    def test_page_results_can_be_combined_and_deduplicated(self):
        first = parse_zbmath((FIXTURES / "zbmath.json").read_bytes(), URL + "?page=0", NOW)
        second = parse_openalex((FIXTURES / "openalex.json").read_bytes(), URL + "?page=1", NOW)
        self.assertEqual(len(deduplicate_records(first + second)), 1)

    def test_missing_credentials_and_terms_are_rejected(self):
        with self.assertRaises(DiscoveryError):
            require_openalex_key(True, None)
        with self.assertRaises(DiscoveryError):
            require_zbmath_terms(False, None)
        require_openalex_key(False, None)
        require_zbmath_terms(True, None)

    def test_normalized_batch_matches_schema(self):
        records = parse_zbmath((FIXTURES / "zbmath.json").read_bytes(), URL, NOW)
        batch = make_batch("zbmath", {"mode": "keyword", "text": "union-closed"}, NOW, records)
        schema = json.loads(
            (ROOT / "schemas" / "discovery_record.schema.json").read_text(encoding="utf-8")
        )
        errors = list(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(batch)
        )
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
