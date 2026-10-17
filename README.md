# ZQM Geospatial Patterns

<!-- ZQM-START -->
<p align="center">
  <strong>ZQM Labs — Z's Quests & Mischief</strong><br>
  <a href="https://zqmlabs.com">zqmlabs.com</a> •
  <a href="https://github.com/ZQM-Labs">GitHub</a>
</p>
<!-- ZQM-END -->



[![CI](https://github.com/ZQM-Computing/geospatial-patterns/actions/workflows/ci.yml/badge.svg)](https://github.com/ZQM-Computing/geospatial-patterns/actions/workflows/ci.yml)

The umbrella index for all ZQM Computing geospatial repositories — reusable patterns and examples across geospatial stack layers, from format conversion (GDAL) to serving (OGC API, STAC, vector tiles).

## Who this is for

Geospatial developers, GIS analysts, and data engineers who want one doorway into the whole series. Each linked repository documents its own examples and validation. This index is a subject-matter map, not proof that every repository is a production dependency or that the stack is deployed as one integrated system.

## How to use this index

Choose a repository by the problem you need to solve, then follow that repository's own prerequisites and quickstart. Treat the arrows in the diagram below as a conceptual workflow only: actual build-time, runtime, and data dependencies must be confirmed in each project's manifests, scripts, and deployment configuration.

For a repository relationship to be considered verified, document:
- relationship type (build dependency, runtime dependency, data flow, deployment, or documentation only);
- direction and interface (package, command, API, file format, or artifact);
- version/compatibility expectation;
- a reproducible test or configuration proving the connection.

A green CI badge means the linked workflow passed for a commit; it does not establish production use, operational support, or end-to-end integration.

## The stack

```
Desktop (QGIS) → Conversion (GDAL) → Python (GeoPandas) → System of Record (PostGIS)
  → Routing (pgRouting) → Analytical (DuckDB) → Columnar (GeoParquet)
  → Raster (COG) → Discovery (STAC) → Frontend (MapLibre) → Grid (H3)
  → Serving (OGC API – Features)
```

## The repositories

### Data & analysis

| Repo | What it covers |
|------|----------------|
| [postgis-patterns](https://github.com/ZQM-Computing/postgis-patterns) | Production PostGIS patterns: spatial indexing, joins & KNN, SRID management, vector tiles, data quality, partitioning |
| [duckdb-spatial-patterns](https://github.com/ZQM-Computing/duckdb-spatial-patterns) | DuckDB Spatial patterns for analytical geospatial SQL: GeoParquet, spatial joins, KNN, H3 aggregation — no server required |
| [geopandas-patterns](https://github.com/ZQM-Computing/geopandas-patterns) | GeoPandas/Shapely patterns for Python geospatial workflows: spatial joins, CRS handling, overlays, interpolation, performance |
| [pgrouting-patterns](https://github.com/ZQM-Computing/pgrouting-patterns) | pgRouting network analysis on PostGIS: shortest path, driving distance, isochrones, turn restrictions, traffic-aware routing |
| [h3-patterns](https://github.com/ZQM-Computing/h3-patterns) | H3 hexagonal grid patterns: indexing, aggregation, visualization, grid comparisons, performance benchmarks |

### Formats & conversion

| Repo | What it covers |
|------|----------------|
| [gdal-patterns](https://github.com/ZQM-Computing/gdal-patterns) | GDAL/OGR command-line patterns: conversion, reprojection, clipping, mosaicking — production-tested, runnable examples |
| [cog-patterns](https://github.com/ZQM-Computing/cog-patterns) | Cloud Optimized GeoTIFF patterns: creation, validation, TiTiler serving, xarray integration, performance benchmarking |
| [geoparquet-patterns](https://github.com/ZQM-Computing/geoparquet-patterns) | GeoParquet patterns for columnar geospatial analytics: partitioning, predicate pushdown, DuckDB/Spark integration |

### Discovery & serving

| Repo | What it covers |
|------|----------------|
| [stac-patterns](https://github.com/ZQM-Computing/stac-patterns) | STAC patterns for geospatial data discovery: catalogs, item validation, search API, bulk operations, cloud deployment |
| [geospatial-api-reference](https://github.com/ZQM-Computing/geospatial-api-reference) | OGC API – Features reference implementation with FastAPI and PostGIS backends |
| [maplibre-patterns](https://github.com/ZQM-Computing/maplibre-patterns) | MapLibre GL JS patterns for frontend vector tile rendering: custom layers, 3D terrain, performance tuning, interactive maps |

### Desktop & field

| Repo | What it covers |
|------|----------------|
| [qgis-resources](https://github.com/ZQM-Computing/qgis-resources) | QGIS expressions, PyQGIS snippets, Processing scripts, styles, and QField field-collection guides |

### Infrastructure & operations

| Repo | What it covers |
|------|----------------|
| [proxmox-ceph-operations](https://github.com/ZQM-Computing/proxmox-ceph-operations) | Proxmox VE + Ceph operations runbooks: health checks, backup discipline, OSD replacement, upgrade checklists |
| [ollama-fleet-patterns](https://github.com/ZQM-Computing/ollama-fleet-patterns) | Ollama fleet operations: model management, health checks, load-spreading, VRAM budgeting, dependency-light RAG |

## Quickstart

Pick a layer above and start with its README — every repo follows the same shape: who it's for, prerequisites, a runnable quickstart, a patterns catalog, and validation via `pytest`. For the Python stack broadly:

```bash
pip install geopandas duckdb pystac rasterio h3
```

## Repository layout

This repo is the index only:

```
geospatial-patterns/
├── README.md            # this index
├── LICENSE
└── CONTRIBUTING.md
```

## Validation

CI lints the repository on every push and pull request.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Report security issues to zqmcomputing@gmail.com — please do not open a public issue for those.

*Part of [ZQM Computing](https://github.com/ZQM-Computing) — games, gear & a little mischief.*

## License

MIT — see [LICENSE](LICENSE).


<!-- ZQM-FOOTER-START -->
---

<p align="center">
  <em>Play more. Plan less.</em><br>
  <a href="https://zqmlabs.com">zqmlabs.com</a> •
  <a href="https://github.com/ZQM-Labs">ZQM Labs</a> •
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- ZQM-FOOTER-END -->
