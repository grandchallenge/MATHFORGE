# YM-D003 / Balaban theorem-body acquisition record

## Record

- Campaign: `YM-001`.
- Parent debt: `YM-D003`.
- Downstream target: `YM-D003-BAL-R002 — STABILITY_TO_CONTINUUM_OBSERVABLE_EXISTENCE`.
- Protected Forge baseline: `a609f40e809ebe74f35dc4ceb069c15e4d21f26e`.
- Audit date: `2026-09-18`; recovery replay: `2026-09-19`.
- Purpose: acquire theorem-number/equation-exact Balaban source detail needed to test whether the admitted four-dimensional ultraviolet-stability theorem can be strengthened downstream into existence of a continuum gauge-invariant observable hierarchy.

## Governing distinction

This record separates three evidence classes:

1. **primary bibliographic/source metadata**, which may be admitted when directly verified from publisher, institutional repository, Project Euclid/OpenAIRE, or OSTI/ETDE surfaces;
2. **primary theorem-body bytes/renderings**, required before equation-level hypotheses can be consumed downstream;
3. **third-party extraction locators**, which may guide acquisition but are not theorem authority.

## Primary source identities reverified

### BAL-CMP119

T. Bałaban, *Convergent renormalization expansions for lattice gauge theories*, Communications in Mathematical Physics 119 (1988), 243–285.

- DOI: `10.1007/BF01217741`.
- Springer article surface directly verifies title, volume, pages, publication date and abstract.
- Rutgers institutional record labels the version of record open and resolves the same DOI.
- OpenAIRE identifies Project Euclid as a data source and exposes Project Euclid object `cmp/1104162401`.
- Source-level abstract: complete effective densities include large-field domains and the renormalization transformations preserve their form; the inspected convergence conclusion is explicitly qualified to superrenormalizable models.

### BAL-CMP122-I

T. Bałaban, *Large field renormalization. I. The basic step of the R operation*, Communications in Mathematical Physics 122 (1989), 175–202.

- DOI: `10.1007/BF01257412`.
- Springer, Rutgers, INSPIRE, OpenAIRE, and OSTI/ETDE independently agree on bibliographic identity.
- Source-level abstract: constructs the large-field `R` operation; explicitly defers completion of the four-dimensional ultraviolet-stability proof to Part II.

### BAL-CMP122-II

T. Bałaban, *Large field renormalization. II. Localization, exponentiation, and bounds for the R operation*, Communications in Mathematical Physics 122 (1989), 355–392.

- DOI: `10.1007/BF01238433`.
- Springer and Rutgers directly verify title, volume, pages and article identity.
- OpenAIRE identifies Project Euclid as a data source and exposes Project Euclid object `euclid.cmp/1104178467`.
- Source-level abstract explicitly states that the paper completes the proof of ultraviolet stability of four-dimensional pure gauge field theories, as formulated in Theorem 1.

## Primary theorem-body acquisition attempts

### Springer

Direct article and `content/pdf` endpoints were opened for CMP119 and CMP122 I–II.

Result: the execution plane is redirected to Springer article previews requiring institutional/subscription access for the full PDF. No theorem-body PDF bytes were obtained.

### Project Euclid

Project Euclid article/PDF objects were reached through OpenAIRE for CMP119 and CMP122-II.

Result: the article/PDF surface resolves through an anti-bot iframe/Incapsula resource on this execution plane. The PDF body cannot be rendered or downloaded here. No checksum is asserted.

### Rutgers institutional repository

Rutgers exposes authoritative bibliographic records and, for CMP119/CMP116, marks the version of record open, but the file link resolves to the DOI rather than an independently downloadable repository copy.

Result: metadata corroboration only; no theorem-body bytes acquired.

### OSTI/ETDE and INSPIRE

These independently corroborate CMP122-I bibliographic identity and abstract scope.

Result: abstract/metadata only; no theorem-body bytes acquired.

### Broad public mirror search

No independent primary or author-hosted copy of CMP119 or CMP122 I–II was found that could be byte-locked on this execution plane.

### Preservation-network recovery

A later recovery pass checked preservation registries rather than ordinary publisher/mirror discovery.

The ISSN Portal record for Communications in Mathematical Physics (online ISSN 1432-0916, ISSN-L 0010-3616) reports:

- Internet Archive preservation for Springer Science & Business Media content covering 1965–2003;
- Portico preservation covering 1988 onward and explicitly listing 1989 volume 122 issue 3 among preserved holdings;
- CLOCKSS preservation covering the historical archive, but CLOCKSS is a dark archive and does not provide ordinary user access absent a trigger event.

The ISSN record links the Internet Archive serial collection `pub_communications-in-mathematical-physics`. The collection surface is JavaScript-dependent on this execution plane, and direct metadata/download enumeration did not expose the 1989 volume-122 issue bytes to the available retrieval interface. Therefore preservation is independently established, but theorem-body bytes are still not acquired and no archive checksum is asserted.

This is a materially narrower blocker than source nonexistence: at least one preservation network is known to hold the journal range, but the current execution interface cannot yet retrieve and independently inspect the preserved issue object.

## Non-authoritative locator evidence

A public third-party research repository reports private/local primary PDFs and rendered page extractions for the Balaban series. This material is **not** imported as source authority.

It is retained only as a navigation aid for later primary verification. The same repository reports a private CMP122-II PDF artifact named `balaban-largefield-II-cmp122-1104178467.pdf`, byte size `4030232`, SHA-256 `80ab1ee09fff0a5b6840a568b72c400a812858425da3200bc5c1c9e2d6941482`. Because neither those bytes nor an independently authoritative copy are exposed, this fingerprint is locator evidence only; it is not adopted as a Forge source lock.

Its reported target loci are:

- CMP119: printed pp. 257–261, including equations `(2.31)` and `(2.42)`;
- CMP122-I: printed p. 192, including equation `(1.70)`;
- CMP122-II: late-paper Theorem 1 and printed pp. 388–390, including equations `(1.98)`–`(1.100)`.

The third-party repository itself labels several of these records as `located` or `visual_confirmed` rather than source-extracted theorem authority and warns against promoting local activity estimates into a global mass-gap claim.

These locators may be used to target a later lawful primary scan. They may not be used as premises in MATHSOLVE.

## 2026-09-19 no-mutation reconnaissance and recovery replay

A fresh read-only reconnaissance rebound the Yang–Mills campaign before any repository mutation.

Protected heads observed at disposition time:

- MATH-PROGRAMME: `d45bd36a6f86c6651b9d40de8191a89e3b793618`;
- MATHFORGE: `a11c6dedede09af6f3c67c5eec337941b73d4d3a`;
- MATHSOLVE: `866612322207cb9e25530215bbfc064dd865ee60`;
- MATHCERT: `1f15e8b1d4f6307aedac5aecfd10bd06b89ab445`;
- INTELLECT: `7e6b61ddf77e2d73309657d089a98cae84cc735f`.

The current Programme routing gate, Solve handoff, D002/D003/D004 obligation DAGs, Solve campaign manifest, Forge acquisition record, and Cert route were re-read from protected state. No newer protected Yang–Mills result supplied a four-dimensional limiting hierarchy, no protected source lock admitted the Balaban theorem body, and MATHCERT still retains `YM-001` as pending without mathematical adjudication. The Programme external-execution-plane changes admitted on 2026-09-19 alter execution topology only and do not change mathematical or source authority.

Reconnaissance disposition:

`PROCEED_WITH_BALABAN_SOURCE_RECOVERY`.

### Immutable external locator manifest

Recovery located the public repository `lluiseriksson/THE-ERIKSSON-PROGRAMME` at immutable commit

`990d228e11707e7244c70843f48968721ab3e3f7`.

Its public artifact manifest

`source-packets/manifests/source-artifact-manifest.json`

records a private/local CMP122-II source packet with:

- PDF name `balaban-largefield-II-cmp122-1104178467.pdf`;
- PDF SHA-256 `80ab1ee09fff0a5b6840a568b72c400a812858425da3200bc5c1c9e2d6941482`;
- PDF byte size `4030232`;
- full-text extraction SHA-256 `ed6fff77db968cf38006ecebd9aa5044e9d239a60af2e8aaa0d810edeed3d423`;
- first-page render SHA-256 `c8eb0356343a8002698ebc0f936b7eaf37434b874c95c0c7ebe5d708eb21b1b7`;
- second-page render SHA-256 `98787cde88bb840e06cf9310af03d74a9d68af07b801a3be951a988cbbd04820`;
- PDF-page-36 / printed-page-390 render SHA-256 `874c016dea69eae3db29d0acba843b3547bfcbb5e8091eeeecdf02351fe7f66d`.

The same repository's public state explicitly says that raw private source artifacts and generated source packets remain out of public Git. Direct GitHub retrieval of the named PDF, text extraction, and render paths returned `404 Not Found`; only their manifest metadata is publicly available. The manifest's source root is a user-local Windows path rather than an independently retrievable primary archive.

Therefore this materially corroborates the previously recorded private-cache fingerprint but does **not** convert it into source authority. No theorem-body bytes or page render were independently acquired or inspected in this tranche.

### Archive and repository replay

The recovery ladder was replayed against the current execution plane:

- Springer continues to expose metadata/abstract scope but not independently downloadable theorem-body bytes;
- Project Euclid object `euclid.cmp/1104178467` remains blocked by its anti-bot/Incapsula surface;
- Rutgers independently confirms the exact CMP122-II bibliographic identity but exposes no independently retrievable theorem body;
- Internet Archive collection metadata / advanced-search endpoints could not be accessed through the available web retrieval interface, and direct network fallback in the execution container could not resolve the archive host;
- broad searches of HathiTrust, Portico/CLOCKSS-facing public surfaces, institutional/author mirrors, DOI/Crossref-derived surfaces, and ordinary public mirrors yielded no independently inspectable theorem-body reproduction.

Portico/CLOCKSS/Internet-Archive preservation evidence remains locator/preservation evidence only. Preservation is not equivalent to theorem-body possession.

### Resulting acquisition boundary

The recovery result is now more precise:

`PRIMARY_THEOREM_BODY_KNOWN_TO_EXIST_IN_PRESERVATION_AND_PRIVATE_SOURCE_PACKET__NO_INDEPENDENTLY_INSPECTABLE_BYTES_ON_CURRENT_EXECUTION_PLANE`.

The downstream blocker remains unchanged:

`MISSING_PRIMARY_BALABAN_THEOREM_BODY_FOR_STABILITY_TO_CONTINUUM_OBSERVABLE_EXISTENCE`.

A third party's content-addressed assertion that it holds the PDF is not an independently verified Forge source lock. Equation-level Balaban bounds therefore remain inadmissible as MATHSOLVE premises.

### Deterministic next evidence action

Reopen this tranche only when one of the following exposes actual theorem-body bytes or equivalently authoritative renders to this governed execution:

1. retrieve CMP122-II from the Internet Archive preserved serial item or another authoritative archive with independently downloadable bytes;
2. obtain the private/user-local CMP122-II PDF named above, then independently match its bibliographic first page to DOI `10.1007/BF01238433`, recompute its SHA-256, and inspect Theorem 1 plus printed pp. 388–390;
3. receive a user-provided primary scan and independently bind bibliographic identity, page range, and digest;
4. obtain an equivalently authoritative theorem-body reproduction with exact page/equation provenance.

The private-cache SHA-256 may be compared after independent acquisition, but a matching manifest claim alone must never substitute for possession and inspection of the source bytes.

## What is established now

The following are provider-safe facts:

1. the three primary source identities above are exact and independently corroborated;
2. Balaban Part II explicitly claims completion of four-dimensional pure-gauge ultraviolet stability;
3. the exact downstream theorem-body loci requiring inspection have been sharply localized;
4. preservation registries independently establish that the relevant CMP journal range is preserved, including volume 122 issue 3;
5. this execution plane does not presently possess independently verified theorem-body bytes or page renders for CMP119/CMP122 I–II.

## What remains unestablished

The current evidence does **not** establish:

- the complete hypotheses and quantifier structure of Balaban's Theorem 1;
- the exact definitions and domains attached to the cited `R`, boundary, or large-field activities;
- a cross-scale Cauchy/tightness/consistency estimate for gauge-invariant observables;
- a theorem turning ultraviolet stability into existence of a continuum observable hierarchy;
- uniqueness of any continuum limit;
- infrared/infinite-volume removal;
- any OS, physical-scale, spectral-gap, confinement, novelty, or terminal claim.

## Downstream disposition

`YM-D003-BAL-R002` remains blocked at the exact source-evidentiary interface:

`MISSING_PRIMARY_BALABAN_THEOREM_BODY_FOR_STABILITY_TO_CONTINUUM_OBSERVABLE_EXISTENCE`.

MATHSOLVE may use the protected high-level theorem interface `YM-T-210`, but it may not consume equation-level quantitative bounds or manufacture a compactness/Cauchy theorem from third-party transcriptions.

## Reopening condition

Reopen this acquisition tranche when at least one of the following becomes available:

1. publisher/Project-Euclid/author-hosted primary PDF bytes accessible for independent checksum and page rendering;
2. a user-provided primary scan whose bibliographic identity can be independently matched and whose digest can be locked;
3. an equivalently authoritative theorem-body reproduction with exact page/equation provenance sufficient for independent visual verification.

Upon reopening, inspect and bind the exact target loci before any Solve theorem attempts to use the internal bounds.

## Continuity checkpoint

Material source identities:

- CMP119 DOI `10.1007/BF01217741`;
- CMP122-I DOI `10.1007/BF01257412`;
- CMP122-II DOI `10.1007/BF01238433`, Project Euclid object `euclid.cmp/1104178467`;
- Internet Archive serial collection `pub_communications-in-mathematical-physics`;
- non-authoritative private-cache locator fingerprint for CMP122-II: SHA-256 `80ab1ee09fff0a5b6840a568b72c400a812858425da3200bc5c1c9e2d6941482`, 4,030,232 bytes.

Failed routes retained: Springer subscription preview, Project Euclid Incapsula surface, Rutgers DOI-only file link, metadata-only OSTI/ETDE/INSPIRE, ordinary public mirror search, JavaScript-blocked Internet Archive collection enumeration, and dark-archive CLOCKSS access.

Deterministic next evidence action:

1. retrieve the preserved CMP 122(3) issue or article bytes from Internet Archive through an interface that exposes the archived item, or obtain another primary/equivalently authoritative scan;
2. independently verify the bibliographic first page and CMP122-II Theorem 1 plus printed pp. 388–390 / equations `(1.98)`–`(1.100)`;
3. recompute the acquired artifact digest and record it as a Forge source lock; the private-cache fingerprint above may be compared only after independent acquisition and must not substitute for it;
4. inspect CMP119 pp. 257–261 and CMP122-I p. 192 if BAL-R002 needs their internal hypotheses;
5. only then reopen MATHSOLVE `YM-D003-BAL-R002` for equation-level theorem work.
