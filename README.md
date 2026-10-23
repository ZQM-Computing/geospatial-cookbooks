# ZQM Geospatial Cookbooks

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering &amp; Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a> ·
  <a href="https://github.com/ZQM-Labs">ZQM Labs</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

[![CI](https://github.com/ZQM-Computing/geospatial-cookbooks/actions/workflows/ci.yml/badge.svg)](https://github.com/ZQM-Computing/geospatial-cookbooks/actions/workflows/ci.yml)

The umbrella index for all ZQM Computing geospatial repositories — reusable cookbooks and examples across geospatial stack layers, from format conversion (GDAL) to serving (OGC API, STAC, vector tiles).

## Repository role and status

**Status:** Active, public.

**What this repository is:** The umbrella index for the ZQM Computing geospatial cookbook series — one doorway into every cookbook repository, organized by stack layer from format conversion (GDAL) through storage and indexing (PostGIS, H3, GeoParquet) to serving (OGC API, STAC, vector tiles). It also carries the series' repository documentation standard.

**What it contributes:** The map of the portfolio. Each linked repository documents its own layer in depth; this repository is how a reader finds the right one, and it is portfolio evidence of the breadth of the geospatial engineering practice behind ZQM Computing.

**Standing:** The portfolio program was completed and Tier-1 hardened on 2026-10-15, with prose CI enforced as required status checks. This repository is an index — the pattern repositories do not depend on it at runtime, and no deployment depends on it.

## Who this is for

Geospatial developers, GIS analysts, and data engineers who want one doorway into the whole series. Each linked repository documents its own examples and validation. This index is a subject-matter map, not proof that every repository is a production dependency or that the stack is deployed as one integrated system.

## Repository documentation standard

Repository maintainers should follow the [geospatial repository documentation standard](docs/repository-documentation-standard.md) for prerequisites, reproducible examples, data provenance, CRS/SRID assumptions, dependency labels, and security guidance.

## How to use this index

Choose a repository by the problem you need to solve, then follow that repository's own prerequisites and quickstart. Treat the arrows in the diagram below as a conceptual workflow only: actual build-time, runtime, and data dependencies must be confirmed in each project's manifests, scripts, and deployment configuration.

For a repository relationship to be considered verified, document:

- relationship type (build dependency, runtime dependency, data flow, deployment, or documentation only);
- direction and interface (package, command, API, file format, or artifact);
- version/compatibility expectation;
- a reproducible test or configuration proving the connection.

A green CI badge means the linked workflow passed for a commit; it does not establish production use, operational support, or end-to-end integration.

## The stack

```text
Desktop (QGIS) → Conversion (GDAL) → Python (GeoPandas) → System of Record (PostGIS)
  → Routing (pgRouting) → Analytical (DuckDB) → Columnar (GeoParquet)
  → Raster (COG) → Discovery (STAC) → Frontend (MapLibre) → Grid (H3)
  → Serving (OGC API – Features)
```

## The repositories

### Data & analysis

| Repo | What it covers |
|------|----------------|
| [postgis-cookbook](https://github.com/ZQM-Computing/postgis-cookbook) | Production PostGIS cookbook: spatial indexing, joins & KNN, SRID management, vector tiles, data quality, partitioning |
| [duckdb-spatial-cookbook](https://github.com/ZQM-Computing/duckdb-spatial-cookbook) | DuckDB Spatial cookbook for analytical geospatial SQL: GeoParquet, spatial joins, KNN, H3 aggregation — no server required |
| [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) | GeoPandas/Shapely cookbook for Python geospatial workflows: spatial joins, CRS handling, overlays, interpolation, performance |
| [pgrouting-cookbook](https://github.com/ZQM-Computing/pgrouting-cookbook) | pgRouting network analysis on PostGIS: shortest path, driving distance, isochrones, turn restrictions, traffic-aware routing |
| [h3-cookbook](https://github.com/ZQM-Computing/h3-cookbook) | H3 hexagonal grid cookbook: indexing, aggregation, visualization, grid comparisons, performance benchmarks |

### Formats & conversion

| Repo | What it covers |
|------|----------------|
| [gdal-cookbook](https://github.com/ZQM-Computing/gdal-cookbook) | GDAL/OGR command-line cookbook: conversion, reprojection, clipping, mosaicking — production-tested, runnable examples |
| [cog-cookbook](https://github.com/ZQM-Computing/cog-cookbook) | Cloud Optimized GeoTIFF cookbook: creation, validation, TiTiler serving, xarray integration, performance benchmarking |
| [geoparquet-cookbook](https://github.com/ZQM-Computing/geoparquet-cookbook) | GeoParquet cookbook for columnar geospatial analytics: partitioning, predicate pushdown, DuckDB/Spark integration |

### Discovery & serving

| Repo | What it covers |
|------|----------------|
| [stac-cookbook](https://github.com/ZQM-Computing/stac-cookbook) | STAC cookbook for geospatial data discovery: catalogs, item validation, search API, bulk operations, cloud deployment |
| [geospatial-api-reference](https://github.com/ZQM-Computing/geospatial-api-reference) | OGC API – Features reference implementation with FastAPI and PostGIS backends |
| [maplibre-cookbook](https://github.com/ZQM-Computing/maplibre-cookbook) | MapLibre GL JS cookbook for frontend vector tile rendering: custom layers, 3D terrain, performance tuning, interactive maps |

### Desktop & field

| Repo | What it covers |
|------|----------------|
| [qgis-resources](https://github.com/ZQM-Computing/qgis-resources) | QGIS expressions, PyQGIS snippets, Processing scripts, styles, and QField field-collection guides |

### Infrastructure & operations

| Repo | What it covers |
|------|----------------|
| [proxmox-ceph-operations](https://github.com/ZQM-Computing/proxmox-ceph-operations) | Proxmox VE + Ceph operations runbooks: health checks, backup discipline, OSD replacement, upgrade checklists |
| [ollama-fleet-cookbook](https://github.com/ZQM-Computing/ollama-fleet-cookbook) | Ollama fleet operations cookbook: model management, health checks, load-spreading, VRAM budgeting, dependency-light RAG |

## Quickstart

This repository is an index, not an installable geospatial stack. Choose the smallest repository that addresses your task, open its README, and install only that project's documented prerequisites. Do not install every stack dependency globally: GDAL, PostGIS/pgRouting, DuckDB, STAC services, and browser examples have different runtime requirements.

A safe starting sequence is:

1. Select a repository from [The repositories](#the-repositories).
2. Read its prerequisites and data-provenance notes before running commands.
3. Use synthetic/sample data where provided; do not commit credentials or sensitive datasets.
4. Run the validation command documented by that repository.
5. Record the tested commit and environment when using results in a production workflow.

## Repository layout

This repo is the index only:

```text
geospatial-cookbooks/
├── README.md            # this index
├── docs/                # documentation standard
├── scripts/             # index validation helpers
├── tests/               # validation tests
├── LICENSE
└── CONTRIBUTING.md
```

## Validation

The index and the linked example repositories have separate validation responsibilities. A green badge is useful only for the exact workflow and commit it represents; it is not proof that every linked repository has been tested or that the projects work together end to end.

Before relying on CI, inspect the linked workflow and confirm that it executes substantive checks rather than placeholder commands. The index should be treated as **not fully validated** until its own workflow checks the repository references and documentation. See [the repository documentation standard](docs/repository-documentation-standard.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

*Part of [ZQM Computing](https://github.com/ZQM-Computing) — geospatial engineering, scientific computing, and infrastructure patterns; the geospatial arm of [ZQM Labs](https://zqmlabs.com), makers of Z's Quests & Mischief location games.*

<!-- ZQM-FOOTER-START -->
<!-- markdownlint-disable MD033 -->
---

<p align="center">
  <em>Geospatial engineering · Scientific computing · Reproducible cookbooks</em><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a> ·
  <a href="https://github.com/ZQM-Labs">ZQM Labs</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-FOOTER-END -->
