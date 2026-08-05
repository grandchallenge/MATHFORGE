# Book VII source lock: Heath 1908

## Begin with the historical object

Book VII does not begin with signed integers or a modern `gcd` function. It begins with a **unit**, a **number as a multitude of units**, and the relation that one number **measures** another.

This Forge package locks the smallest source cluster needed to connect that language to the protected modern gcd exemplars without rewriting the history.

## Selected edition

The source authority is:

- Euclid, *The Thirteen Books of Euclid's Elements*;
- Volume II, Books III–IX;
- translated and edited by Thomas Little Heath;
- translated from the text of J. L. Heiberg;
- Cambridge University Press, 1908;
- English.

The Wikimedia Commons scan is a 575-page mechanical scan of the public-domain original. Its stable file page, versioned page revision, original-file URL, Internet Archive identifier, file-history timestamp, and Public Domain Mark are recorded.

The operation does not invent a SHA-256 for the whole PDF. Those bytes were not independently acquired by the implementation environment. The exact governed byte surface is the repository transcription artifact:

`sources/EUCLID-ELEMENTS-BOOK-VII-MICRO-001/heath_1908_book_vii_selected_statements.txt`

It is normalized to UTF-8 with LF line endings and one final newline. Its exact byte length and SHA-256 are checked on every Forge run.

## Admitted cluster

Exactly eight loci are admitted:

1. `VII.def.1`: unit;
2. `VII.def.2`: number;
3. `VII.def.3`: part and measuring;
4. `VII.def.5`: multiple and measured relation;
5. `VII.def.12`: numbers prime to one another;
6. `VII.def.14`: numbers composite to one another;
7. `VII.1`: repeated subtraction reaching a unit;
8. `VII.2`: construction of the greatest common measure, with its porism.

No other Book VII proposition is admitted.

## Historical-to-modern concordance

The concordance preserves these distinctions.

| Historical surface | Bounded modern bridge | Boundary |
|---|---|---|
| Unit | Distinguished arithmetic unit | A unit is not silently merged into Euclid's number domain. |
| Number as a multitude of units | Positive natural representative greater than one | Zero, negative integers, and signed coefficients are excluded. |
| A lesser number measures a greater | Positive exact divisibility with an oriented multiplier | Signed or ring-theoretic divisibility is not attributed to Euclid. |
| Prime to one another | Normalized positive-domain `gcd(a,b) = 1` | This is an interpretive normalization, not Euclid's notation. |
| Repeated subtraction to a unit | Coprimality certificate | The modern remainder algorithm and complexity bounds are not verbatim source claims. |
| Greatest common measure | Positive-domain greatest common divisor analogue | Signed gcd conventions, extended Euclid, and Bézout coefficients are later extensions. |

## Modern extensions kept outside the source claim

The package explicitly classifies the following as later normalizations or extensions:

- division-with-remainder Euclidean algorithm;
- extended Euclidean coefficient production;
- Bézout identity over integers;
- linear Diophantine solvability over integers.

The protected Stage 1 and Stage 2 results may use these modern statements. This historical source lock does not retroactively attribute them to Euclid.

## Authority state

This branch prepares a candidate exact-byte source lock and bounded concordance. Protected source authority arises only after:

1. exact-head Forge checks;
2. GCL conformance;
3. independent non-author historical-mathematics review;
4. Human Steward exact-head disposition;
5. merge-commit-only protected merge;
6. post-merge readback.

The candidate does not authorize a MATH-PROGRAMME reader, edition record, documentary manifest admission, or historical-source authority for illuminated plates. Plates remain `pedagogical_orientation_only`.

Target disposition:

`EUCLID_BOOK_VII_HEATH_1908_SOURCE_LOCK_AND_BOUNDED_CONCORDANCE`
