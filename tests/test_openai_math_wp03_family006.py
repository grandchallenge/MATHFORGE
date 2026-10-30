import json
from pathlib import Path

def test_family006_indexed_scope():
    p = Path(__file__).resolve().parents[1] / 'sources/OPENAI-MATH-2026/WP03_FAMILY006_GOLDFELD_INDEXED_COVERAGE.json'
    d = json.loads(p.read_text())
    assert d['family_id'] == '006'
    assert d['source_lock']['commit'] == '1581d4cbdd69a0faf34b2089614fe2a814316a6a'
    assert len(d['source_lock']['manuscripts']) == 2
    assert not d['coverage']['semantic_alignment_established']
    assert not d['coverage']['pilot_12_family_complete']
