# Formal Conjectures provider lane

This directory contains the governed MATHFORGE intake for `google-deepmind/formal-conjectures`.

The lane treats the upstream repository as a versioned formal-statement source. It does not treat upstream categories, Lean elaboration, `sorry`, proof links, or sorry-free metadata as Programme status or MATHCERT certification.

- `source_lock.json` pins repository, commit, toolchain, extractor, and source blobs.
- `intake.py` verifies and normalizes extractor output.
- `snapshots/` contains content-addressed selected statement snapshots.
- `concordance/` compares upstream statements with Programme-owned targets.
- `MF-FC-WP00.md` defines replay.
- `MF-FC-WP01.md` records the RH/NS pilot disposition.
