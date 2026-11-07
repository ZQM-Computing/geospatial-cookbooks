# 90-day hero-cookbook and ZQM Labs documentation execution register

**Status:** working plan based on a manual source inventory from 2026-11-06.
This is not a verified analytics baseline, proof of past event delivery, an
endorsement by third-party projects, or a report that every linked example has
passed CI at the same exact commit.

Owner of this register: **ZQM Computing**. ZQM Labs continues to own all
games, hosts, quest content, pricing/fulfillment and player telemetry decisions.
No new paid services or mass-created city pages are authorized here.

## Executive decision

Concentrate improvements in **five hero technical cookbooks**, plus
**three Labs acquisition/hosting surfaces**. The rest of the cookbook catalog
remains navigable and maintained, but is not the near-term content-production
priority. The three phases below are commitments for review, not releases.

The selection uses relevance to current GIS buyers, ability to provide
synthetic/reproducible examples, the existing example directory inventory,
cross-link value, and dependency/operational burden. This is a prioritization
judgment, **not a GitHub-traffic-driven ranking**.

### Five initial ZQM Computing heroes

| Hero | Observed source structure (at review) | Next proof to publish | Release gate |
| --- | --- | --- | --- |
| [GeoPandas](https://github.com/ZQM-Computing/geopandas-cookbook) | Thirteen numbered example folders, including a similarly numbered GeoPackage example; existing synthetic land-change demonstration and offline GIS reasoning scorer | Parcel/environmental-screening walkthrough with known geometry, projected units and reproducible output | Golden numeric invariants, CRS and provenance tests, example output alt text |
| [STAC](https://github.com/ZQM-Computing/stac-cookbook) | Thirteen numbered example areas covering catalog, API, COG, validation and integrity | A complete **offline** STAC item-to-COG inspection example with asset-resolution and rights checks | Schema validation, deterministic fixture, broken-href failure, no token or live-cloud dependency |
| [DuckDB Spatial](https://github.com/ZQM-Computing/duckdb-spatial-cookbook) | Seven documented SQL patterns plus three `examples/` folders | Answer-first SQL walkthrough comparing a synthetic parcel screening operation with GeoPandas or PostGIS | Exact SQL check assertions, no implicit metric/degree conversion, cold-start caveats |
| [GeoParquet](https://github.com/ZQM-Computing/geoparquet-cookbook) | Seven example folders including a legacy-looking `01-cog-creation` folder; measurement export added in a recent merged PR | Evidence-backed file-size, fidelity and predicate-pushdown tutorial using the **same** fixture | Exact source bytes, feature/attribute/CRS equivalence, repeated timing caveats, no copied Shapefile claims |
| [COG](https://github.com/ZQM-Computing/cog-cookbook) | Six example areas from creation through full workflow | Range-read/overview tutorial with synthetic raster and exact validation report | GDAL version and output check, license/asset provenance, no unverified cloud performance claim |

**Inventory disclaimer:** directory counts and README claims are not an
automated test of each pattern. For every new published result, read the
current workflow and record *exact-head* check state and a locally reproducible
command. Do not confuse documentation density with passed execution.

### Three initial ZQM Labs surfaces

| Surface | Current evidence | Next improvement and truth guard |
| --- | --- | --- |
| [Free sample](https://github.com/ZQM-Labs/quest-packs/tree/main/sample-quest) | Public six-stop JSON and editing instructions exist | Make its README a clear two-path choice: **read/learn** vs. **plan a real hosted route**. Changing waypoint coordinates and QR configuration remains necessary for physical play; the embedded Wisp browser demo is a distinct product |
| [First-quest/host handbook](https://github.com/ZQM-Labs/quest-authoring) | SPEC v1 and validator, authoring guide and generator exist | Answer-first walkthrough from an original prompt to safe six-stop JSON, validation, on-device compatibility, permissions and field playtest |
| [Organizer Toolkit](https://github.com/ZQM-Labs/organizer-toolkit) | QR/print/troubleshooting instructions, community event planning templates and a local aggregate calculator exist | A single safe start-to-finish host checklist, including support boundary, version pin, optional sharing consent and human confirmation of venue readiness |

### Content quality rubric

Assess evidence **per runnable pattern**, not via README word counts.
Keep each criterion as `pass / fail / not tested` with an exact source path,
commit, command and test artifact. Never silently mark a skipped workflow
as passed.

1. **Intent:** question-shaped title, 2–3 sentence direct answer and why it matters.
2. **Reproduce:** exact prerequisites, one-command or short command sequence,
   deterministic/cleared fixture and clearly described output.
3. **Correctness:** tests or reviewed expected answers cover units, CRS,
   row/geometry counts, failure states and version dependency.
4. **Usability:** screenshot/diagram or accessible textual output, alt text,
   expected sample output and explanation of limitations.
5. **Discovery:** unique canonical URL, useful links from the umbrella index,
   related hero pages and a **correctly labeled** Labs use case when relevant.
6. **Claim discipline:** no fabricated timings, model rankings, measured
   customer improvements, screenshots, paid functionality or conversions.

A hero becomes a launch candidate when its selected core examples satisfy
all six criteria. A repo-wide badge alone is insufficient.

## Sequencing: 90 days (not an automated schedule)

| Phase | Window | Concrete review deliverable |
| --- | --- | --- |
| 0 — source and metadata audit | Weeks 1–2 | Record five hero READMEs, the three Labs paths, exact counts/commands, existing headings, canonical links, and CI states; nominate the strongest 2–3 examples per hero |
| 1 — answer-first example density | Weeks 2–6 | Improve **existing** examples and tests before adding breadth; add a worked first quest and truthful demo-versus-kit documentation |
| 2 — conversion and real evidence | Weeks 5–8 | Verify an actual free-demo-to-organizer inquiry path; publish only approved, anonymized pilot or manual aggregate evidence with denominators; add a reviewed playtest study if one truly exists |
| 3 — discovery readiness | Weeks 7–12 | Cross-link vetted heroes, verify rendered site pages and search indexing, then draft a coordinated launch package for review. No automatic social posting or unmeasured paid spending |

### Link architecture and ownership

- ZQM Computing umbrella → individual **hero** cookbook → runnable example
  and tests → another closely related cookbook. Keep links descriptive.
- From an applicable hero, a clearly named **demonstration/application**
  link may point to ZQM Labs; state that Labs owns quests and game releases,
  while Computing owns reusable GIS analysis.
- Labs commercial site → truthful free browser demo (where verified) →
  dedicated pack authoring/host learning path → **inquiry for a scoped pilot**.
  The source site deploy is pinned by the Computing monorepo; merged site
  Markdown does **not** establish that a new page is live.
- The free sample JSON, playable embedded demo and venue-approved paid
  event are **different artifacts**. Do not combine their labels or metrics.

### Measurement: verify before publishing

No current ZQM search impressions, install conversions, sample completion
cohort, paid host revenue or customer case study was established by this
inventory. GitHub star counts are **not** customer funnel measurements.

Use a consent-appropriate, privacy-minimal aggregate register with:

| Stage | Definition | Source needed |
| --- | --- | --- |
| Developer discovery | Qualified GitHub/documentation click or search-referral | A dated, access-authorized analytics report |
| Game entry | An explicitly defined sample/demo start | A reviewed source/counter with consent basis |
| Completion | A tested full six-stop finish for the same eligible cohort | Dated host event proof or reviewed aggregate |
| Organizer interest | Distinct, qualified request for a host pilot | Approved private inquiry ledger |
| Commercial result | Signed scope and **verified** checkout/fulfillment | Private contract and transaction evidence |

Report missing/unsupported as **not measured**. Never insert fake "0%" or
a synthetic fixture into a public success story. The
[Organizer Toolkit](https://github.com/ZQM-Labs/organizer-toolkit)
contains an optional **offline aggregate calculator**, which explicitly
marks results unverified and suppresses small cohorts; that is not a live
analytics integration.

## Coordinated launch: gates before dates

A focused release window is reasonable **only after**:

- The five selected heroes have a useful, runnable first-session path with
  validated results and corrected canonical/internal links.
- The Labs browser demo and host inquiry can be exercised end-to-end with
  no false booking claim, unsupported locale or stale player source pin.
- A first-time organizer can follow the six-stop sample instructions without
  assuming that sample coordinates designate a lawful public route.
- At least one approved test outcome or **explicit absence of evidence**
  is presented truthfully; screenshots of example outputs use owned assets.
- Maintainers confirm content/IP rights, accessibility, privacy, support
  capacity, rollbacks, and release manifests before publication.

Do not launch all 90+ cookbooks, buy ads, build an unsupervised author
marketplace or enable background geolocation merely to meet an editorial
calendar.
