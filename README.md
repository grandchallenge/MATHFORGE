# MATHFORGE

MATHFORGE is the discovery and witness-generation pillar of the Grand Challenge mathematics stack.

It is responsible for turning promising mathematical structure into durable artifacts: search traces, exact-computation outputs, counterexample candidates, witness objects, and certificate payloads that can later be consumed by MATHSOLVE and checked by MATHCERT.

MATHFORGE owns discovery, source reconstruction, candidate generation, and
reconnaissance. Programme concepts and relationships remain canonical in
`MATH-PROGRAMME`; provider results are evidence only.

## Programme links

MATH-PROGRAMME is the front door and policy source for this pillar.

- [MATH-PROGRAMME Pages home](https://grandchallenge.github.io/MATH-PROGRAMME/)
- [Programme Atlas](https://grandchallenge.github.io/MATH-PROGRAMME/PROGRAMME_ATLAS/)
- [Three-pillar architecture overview](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/ARCHITECTURE_OVERVIEW.md)
- [MATHFORGE pillar doctrine](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/MATHFORGE_SPEC.md)
- [Cross-pillar lanes](https://grandchallenge.github.io/MATH-PROGRAMME/CROSS_PILLAR_LANES/)
- [Groebner and EXPSPACE doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/GROEBNER_EXPSPACE_DOCTRINE/)
- [Claim-boundary doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/CLAIM_BOUNDARY_DOCTRINE/)

## Algebraic witness export

MATHFORGE now includes an algebraic-witness export lane for polynomial subclaims. The lane is deliberately downstream-compatible with the MATHCERT algebraic certificate lane:

```text
MATHFORGE  -> generate candidate algebraic witnesses
MATHSOLVE  -> decide when to invoke them tactically
MATHCERT   -> check, certify, and preserve the proof boundary
```

MATHFORGE may use SageMath, SymPy, Singular, Magma, or custom exact arithmetic to discover witnesses. Those outputs are not proofs. They become trustworthy only after replay or Lean-kernel checking in MATHCERT.

See `docs/algebraic_witness_export.md`.

## Discovery

```text
python discovery/search.py --provider zbmath --query-file QUERY.txt --ack-zbmath-terms
python discovery/search.py --provider openalex --semantic --query-file QUERY.txt
python discovery/search.py --provider arxiv --category math.CO --since YYYY-MM-DD
```

OpenAlex semantic search reads `OPENALEX_API_KEY`. zbMATH queries require
`--ack-zbmath-terms` or `ZBMATH_TERMS_ACCEPTED=yes`. Raw responses are written
under ignored `.cache/discovery/`; only reviewed normalized records belong in
`reports/discovery/`.

Thank you to arXiv for use of its open access interoperability.
