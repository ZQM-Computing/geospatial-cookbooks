# 90-day hero-cookbook and ZQM Labs documentation execution register

**Status:** working plan based on a manual source inventory from 2026-11-06.
This is not a verified analytics baseline, proof of past event delivery, an
endorsement by third-party projects, or a report that every linked example has
passed CI at the same exact commit.

Owner of this register: **ZQM Computing**. ZQM Labs continues to own all
games, hosts, quest content, pricing/fulfillment and player telemetry decisions.
No new paid services or mass-created city pages are authorized here.

## Executive decision

Concentrate improvements in **six hero technical cookbooks**, plus
**three Labs acquisition/hosting surfaces** (reconciled 2026-11-06; see
"Reconciliation" below). The rest of the cookbook catalog
remains navigable and maintained, but is not the near-term content-production
priority. The three phases below are commitments for review, not releases.

The selection is a **provisional weighted evidence ranking**, proposed 2026-11-06
(see "Reconciliation" below): composite /14 = Density (vs GeoPandas
14 units / 24 artifacts) + README quality (§7: problem, quickstart, visual
proof, related links) + Completeness (tests, CI, README depth, size).
Pattern files under `patterns/` count toward units at half weight (0.5 each).
This is an evidence ranking, **not a GitHub-traffic-driven ranking** and not
a prioritization judgment: where the ranking and the prior list disagreed,
the ranking decided (Alex, 2026-11-06).

### Six proposed ZQM Computing heroes (2026-11-06)

**Inventory reconciliation pending (merge gate).** The numeric scores below
are historical proposal inputs, not a newly independently verified census.
Two source-review findings remain open:

- **GeoPandas:** The report's 14 weighted-unit baseline and 24-artifact
  denominator lack a documented, non-overlapping classification of numbered
  example directories, split example 12, and the referenced demos. The
  inspected tree contains 13 example directories and a separate
  `demos/workflow_qa.py` script; the claimed three counted demos have not
  been independently mapped to exact file paths.
- **MapLibre:** The inspected tree contains ten notebook files, ten HTML
  files, and one SQL pattern. The table's 10.5 weighted units may be
  defensible under a unique-example-directory rule, but its 12-artifact
  assertion has no independently reproducible definition.

Before approving the weighted ranking, freeze each source repository's
commit SHA, publish a machine-readable per-path classification
(`example_unit`, `pattern_half_unit`, `demo`, `artifact`, or
`excluded`), specify whether multiple formats in one example count once,
and recalculate each candidate's density and composite score. Keep the
current six-hero list a **planning proposal**, not an evidence-certified
selection, until the inventory and both review threads are reconciled.

| Hero | Reconciled score & evidence (2026-11-06) | Next proof to publish | Release gate |
| --- | --- | --- | --- |
| [GeoPandas](https://github.com/ZQM-Computing/geopandas-cookbook) | **13.00/14 (provisional)** — the reference baseline: 14 units, 24 artifacts, 12 test files, CI, Quickstart; existing synthetic land-change demonstration and offline GIS reasoning scorer | Parcel/environmental-screening walkthrough with known geometry, projected units and reproducible output | Golden numeric invariants, CRS and provenance tests, example output alt text |
| [PostGIS](https://github.com/ZQM-Computing/postgis-cookbook) | **11.78/14** — 9.5 weighted units (6 example dirs + 7 pattern files at half weight), 20 artifacts (2nd on the account), longest hero README (16.2 KB); pattern guide + production runbook | Distribution-aware spatial-index benchmark with reproducible numbers | Exact SQL check assertions, no implicit metric/degree conversion, cold-start caveats |
| [STAC](https://github.com/ZQM-Computing/stac-cookbook) | **11.78/14** — 13 units, 14 artifacts, largest cookbook (506 KB); head of the STAC→COG→TiTiler vertical | A complete **offline** STAC item-to-COG inspection example with asset-resolution and rights checks | Schema validation, deterministic fixture, broken-href failure, no token or live-cloud dependency |
| [GDAL](https://github.com/ZQM-Computing/gdal-cookbook) | **11.53/14** — 11 weighted units (8 example dirs + 6 pattern files at half weight), 15 artifacts spanning CLI, Python and COG creation; foundation library of the whole stack | COG-creation walkthrough cross-linked to the COG cookbook (not duplicated there) | GDAL version and output check, license/asset provenance, no unverified cloud performance claim |
| [pgRouting](https://github.com/ZQM-Computing/pgrouting-cookbook) | **11.50/14** — 12 example units (2nd-most), one runnable `run.sql` per dir, purely SQL end-to-end | Isochrone + service-area walkthrough with known geometry | Exact SQL check assertions, no implicit metric/degree conversion, cold-start caveats |
| [MapLibre](https://github.com/ZQM-Computing/maplibre-cookbook) | **11.12/14 (provisional)** — 10.5 weighted units (10 notebook dirs + 1 pattern file at half weight), 12 artifacts including 10 notebooks (the estate's only notebooks); voted in as 6th hero | First rendered visual proof: an interactive map output committed to the README | Screenshot/diagram with alt text, expected sample output, no fabricated timing claims |

**Named alternates, in order:** GeoParquet (11.24), COG (10.96) / H3 (10.96,
tied), DuckDB Spatial (10.81). All three of the prior list's picks that missed
the cut lose on the approved tiebreak (highest-scored yeses take the slots),
not on a judgment call: GeoParquet misses the top 5 by 0.26, DuckDB by 0.69
despite rising from 10.1 to 10.8 under the patterns rule.

### Reconciliation (decided by Alex, 2026-11-06)

The prior five were GeoPandas, STAC, DuckDB Spatial, GeoParquet, COG. Alex
answered 13 yes/no questions: weighted scoring decides contested slots; if
more than five cookbooks get a yes, the highest-scored yeses take the slots;
MapLibre joins as a 6th hero by direct vote; the density bar is ≥12 weighted
units **and** ≥15 artifacts; the register is the single record of the
reconciled list.

**Proposed method (pending source-to-count reconciliation).** Composite /14 = Density D (0–5, vs GeoPandas 14 units /
24 artifacts: D = ((units÷14) + (artifacts÷24)) ÷ 2 × 5), README §7 (0–4),
and Completeness C (0–5). **Patterns rule:** files under `patterns/` count
toward units at half weight (0.5 each) — a pattern is a reusable snippet,
not a standalone tutorial. The rule applies to every repo equally; pattern
counts were reported from reviewed git trees (DuckDB 8, PostGIS 7, GDAL 6,
GeoParquet 6, COG 6, H3 6, MapLibre 1, GeoPandas/STAC/pgRouting 0). No repo
has more than 8 pattern files, so no cap was needed.

**Sensitivity (disclosed).** Full counting (patterns = 1.0 units) would give
PostGIS 12.4, GDAL 12.1, GeoParquet 11.8, DuckDB 11.5 — and the top 5 would
become GeoPandas, PostGIS, GDAL, STAC, **GeoParquet**, with **pgRouting out**.
The half-weight rule is therefore load-bearing for pgRouting's slot and
GeoParquet's alternate status; it is recorded here so a future re-weighing
can be argued on the merits. Full counting was rejected because it equates
snippets with full tutorials.

**Density bar.** Heroes are to reach **≥12 weighted units AND ≥15 artifacts**.
Only GeoPandas meets both today; STAC (units only), PostGIS (artifacts
only), GDAL (artifacts only, units 1 short), pgRouting (units only) and
MapLibre (neither) are near-GeoPandas on at least one axis. Bringing each
hero to both thresholds is Phase 1 density work, not a re-selection trigger.
The brief's 8–15 runnable-examples band is superseded by this bar for hero
purposes.

**Corrections to the prior register.** GeoPandas has **twelve** numbered
example slots (01–12; #12 split in two, i.e. 13 example dirs + 3 demos),
not "thirteen numbered example folders". DuckDB has **eight** documented SQL
patterns (`patterns/01–08`), not seven.

**Inventory disclaimer:** directory counts and README claims are not an
automated test of each pattern. For every new published result, read the
current workflow and record *exact-head* check state and a locally reproducible
command. Do not confuse documentation density with passed execution.

### Three locked ZQM Labs surfaces (reconciled 2026-11-06)

<!-- coderabbit-ai-generated:v1 -->

<!-- coderabbit-ai-generated-section:v1:b56b98b9d8a1cde40ec533727d0ab5dd2a661881c7e694fb8bd7b7b3eb2a8d7f -->

| Surface | Current evidence (verified live 2026-11-06) | Next improvement and truth guard |
| --- | --- | --- |
| [Free demo](https://zqmlabs.com/games/hunt-for-wisps/play/?demo=1) | Complete six-stop trail, no kit or code required; paid-kit upsell + $49/$199/$349/$499 pricing on the landing page. Sample JSON in [quest-packs](https://github.com/ZQM-Labs/quest-packs/tree/main/sample-quest) | In `ZQM-Labs/quest-packs`, make `sample-quest/README.md` a clear two-path choice: **read/learn** vs. **plan a real hosted route**. Changing waypoint coordinates and QR configuration remains necessary for physical play; the embedded Wisp browser demo is a distinct product. Separately, the Wisp browser demo landing copy still says "Halloween scavenger hunt" — evergreen it to year-round before it fronts a launch |
| [Host Handbook](https://docs.zqmlabs.com/hosting/) | Complete 7-page handbook; "about one hour, total" is the clearest conversion promise in the estate | Answer-first walkthrough from an original prompt to safe six-stop JSON, validation, on-device compatibility, permissions and field playtest. **Evergreen first:** it still frames the game as the Oct 30–Nov 1, 2026 Halloween window |
| [Organizer Toolkit](https://organize.zqmlabs.com/) | Checklist + working QR generator + print specs + day-of troubleshooting + FAQ; the only surface that makes a host self-sufficient | A single safe start-to-finish host checklist, including support boundary, version pin, optional sharing consent and human confirmation of venue readiness |

<!-- /coderabbit-ai-generated:v1 -->

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
| 0 — source and metadata audit | Weeks 1–2 | Record six hero READMEs, the three Labs paths, exact counts/commands, existing headings, canonical links, and CI states; nominate the strongest 2–3 examples per hero |
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

- The six selected heroes have a useful, runnable first-session path with
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
