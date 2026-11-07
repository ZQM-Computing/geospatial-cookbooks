# Shareable geospatial content: experiment register

**Status: dated research-to-execution plan (2026-11-06), not a claim
that each concept is implemented, popular with ZQM audiences, or published.**

Owner: **ZQM Computing**. Audience: geospatial developers, environmental
planners and GIS decision makers. ZQM Labs owns games and player engagement
under its distinct brand; this index must not change Labs game release status.

## Formats and repository ownership

| Priority | Public-facing format | Correct home | Evidence state |
| --- | --- | --- | --- |
| P0 | Synthetic then verified before/after spatial stories | [GeoPandas cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) | Synthetic generator + regression tests merged in PR #44. Real Earth-change detection not implemented. |
| P0 | AI versus GIS expert: projection, area, join, provenance test | GeoPandas, DuckDB Spatial, and GIS QA cookbook examples | Proposed; must test deterministic expected answers before making claims about models. |
| P1 | Reproducible short-form cartography / #30DayMapChallenge | GDAL, GeoPandas, MapLibre and H3 cookbooks | Editorial concept; November 2026 event window. Prompt/date schedules need current verification before posting. |
| P1 | Cinematic globe or live-Earth explainers | MapLibre, OGC, STAC and COG cookbooks | Research only; requires licensing, operating cost, provenance and performance review. |
| P1 | Browser-native GIS performance comparisons | GeoPandas, GDAL and emerging Rust GIS tools | Proposed; use identical data, environment and measured metrics rather than unsupported "X is faster" statements. |
| P2 | Stylized city maps built from permitted datasets | MapLibre + rendering/art tooling | Concept only; no unlicensed map tiles or third-party imagery. |
| P2 | Reproducible geography quiz datasets | Labs game prototype with Computing providing independently vetted analysis where appropriate | Experimental; Labs owns player-facing experience. |

## Content release contract

Every published technical content item should carry:

1. Question/hook and intended audience; short-form caption plus accessible
   alternate description for images or animation.
2. Input dataset name, source URL, acquisition date, license and allowed
   redistribution or screenshot rights.
3. Processing command or notebook commit, software versions, CRS/coordinate
   units, precision, study boundary and known limitations.
4. Method and test evidence. Keep synthetic examples explicitly labeled;
   do not convert simulated changes into claims about actual places.
5. Graphic or clip, companion evidence artifact, and stable reproducible
   example link on GitHub. Do not publish private parcels, client data,
   credentials, paid game answer keys, or sensitive locations.
6. One truthful, relevant call to action: technical reuse, diagnostic
   inquiry, or scoped preliminary screening. Never imply regulatory
   approval, survey certification, or an unverified product launch.
7. Publication date, channel, consent/privacy basis where applicable, and
   a single primary success metric with denominator.

## Small-batch validation

- Publish three distinct formats with existing open-source tools and no
  new recurring cloud spend; label each as an experiment.
- Record impressions/reach where reported, visit-to-repo click-through,
  meaningful technical reuse, and qualified buyer inquiries **separately**.
- Treat views and likes as awareness, not revenue, project demand,
  or proof of accuracy.
- Reuse the same validated analysis artifact across a short clip,
  annotated still, technical walkthrough and README link; change the
  presentation without changing data claims or provenance.
- Stop or revise themes that generate attention without useful audience
  or inquiry signals. Do not invent benchmarks or success thresholds.

## Existing implementation

The [GeoPandas shareable spatial stories guide](https://github.com/ZQM-Computing/geopandas-cookbook/blob/main/docs/shareable-spatial-stories.md)
is the first implemented engineering demonstration. It produces **synthetic**
coverage-comparison images and auditable area metrics, not observed
environmental change. Its tests run in the cookbook's CI.

## Boundaries and dependencies

ZQM Labs independently owns its
[Daily Geo Mystery prototype review](https://github.com/ZQM-Labs/zqmlabs-site/pull/86),
quest pack specification, game player, community moderation, and public
availability statements. Do not reuse quest-player authorization, score
services, or paid fulfillment systems for these experiments without
separate design review. Do not alter production analytics or deploy from
this documentation index.

This is a prioritized backlog, not an automatic schedule, live news feed,
or a publication promise. Validate external trends at the time of posting.
