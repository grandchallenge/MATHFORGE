# OpenAI Mathematics collection: source-locked intake candidate

This is a distinct external source observation, **not** the older OpenAI Selected Proofs / `OPENAI-TEN-PROOFS-001` programme. It is not an admitted `catalog/providers` provider snapshot or a mathematical result.

Pinned upstream: [openai/math@`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a).

## Verified index scope

- `CONTENTS.md` at Git blob `2c68c086fff36a5806c936ad1659cf1a8d0b6dd9` was structurally parsed into **372 numbered families / 719 manuscript PDF links**.
- Family headings and PDF paths are indexed in `MANUSCRIPT_INDEX.json`; they are not proof statements or independent title/conclusion verification.
- `SOURCE_LOCK.json` binds the Git commit/tree, selected upstream blobs, stated Lean environment, licensing, and correction/withdrawal history.
- The publisher reports **300/719 top-line results formalized** (approximately 42%); this figure is attributed, **not** a GCL replay or semantic audit.

## Source warnings

The [2026-10-07 history](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/history.md) reports three withdrawals, fourteen repaired manuscripts, and thirteen dependency-citation updates. Treat historical versions and dependencies separately. Compilation, a Comparator output, and a manuscript claim must not be conflated. Per-result `lean/docs/` scope notes and source/Lean correspondence need their own reviews.

The root `LICENSE` is Apache-2.0; any reuse or redistribution must observe its terms. Manuscript content is linked, not mirrored in this packet.

## Deterministic replay

On an independent checkout of the **exact** pinned commit, run:

```sh
python3 sources/OPENAI-MATH-2026/replay_index.py \
  --contents /path/to/openai-math/CONTENTS.md \
  --index sources/OPENAI-MATH-2026/MANUSCRIPT_INDEX.json
```

The replay script compares every family headline and every indexed PDF link; a changed upstream file or index fails. Source-tree completeness, Lean replay, theorem-semantic concordance, and external literature comparison remain separate obligations.

## Follow-on admission

MATHFORGE should propose a new catalog provider and replay adapter only after source/version/correction fixtures, legal review as applicable, and deterministic replay are in place. Any downstream campaign requires explicit Programme authorization; MATHSOLVE and MATHCERT retain their established boundaries.

Assurance: **external-source observation + link-index extraction only**, with no certification or theorem promotion.
