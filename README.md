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

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![GitHub](https://img.shields.io/github/stars/ZQM-Computing/geospatial-cookbooks?style=social)
[![CI](https://github.com/ZQM-Computing/geospatial-cookbooks/actions/workflows/ci.yml/badge.svg)](https://github.com/ZQM-Computing/geospatial-cookbooks/actions/workflows/ci.yml)

Explore the ZQM Computing geospatial cookbook series: practical GIS and spatial-data engineering examples for QGIS, GDAL, GeoPandas, PostGIS, DuckDB Spatial, GeoParquet, H3, STAC, Cloud Optimized GeoTIFFs, OGC APIs, and browser mapping. Each repository documents its own prerequisites and validation scope; the index does not imply a deployed end-to-end stack.

## Related application: ZQM Observatory

[zqm-observatory](https://github.com/ZQM-Computing/zqm-observatory) is a separate public-data intelligence application that may reuse patterns documented by this cookbook series. It is not part of the cookbook index manifest, and the link does not assert runtime dependencies or end-to-end integration. See its [geospatial repository integration map](https://github.com/ZQM-Computing/zqm-observatory/blob/main/docs/geospatial-repository-integration.md) for proposed handoffs and the evidence required before calling them verified.

## Repository role and status

**Status:** Active, public.

**What this repository is:** The umbrella index for the ZQM Computing geospatial cookbook series — one doorway into every pattern repository, organized by stack layer from format conversion (GDAL) through storage and indexing (PostGIS, H3, GeoParquet) to serving (OGC API, STAC, vector tiles). It also carries the series' repository documentation standard.

**What it contributes:** The map of the portfolio. Each linked repository documents its own layer in depth; this repository is how a reader finds the right one, and it is portfolio evidence of the breadth of the geospatial engineering practice behind ZQM Computing.

**Standing:** This repository is a documentation index. Its references and its own CI should be verified independently; a completed documentation pass does not establish production readiness or end-to-end integration. The pattern repositories do not depend on this index at runtime, and no deployment depends on it.

## Who this is for

Geospatial developers, GIS analysts, and data engineers who want one doorway into the whole series. Each linked repository documents its own examples and validation. This index is a subject-matter map, not proof that every repository is a production dependency or that the stack is deployed as one integrated system.

## Canonical repository manifest

The [repository manifest](docs/repository-manifest.json) records the canonical slugs for every repository listed in this index. It is a documentation registry only—not a dependency graph, runtime integration claim, or deployment inventory. The consistency check runs in the standard unit-test suite. Run it locally with:

```sh
python -m unittest discover -s tests -p 'test_repository_manifest.py' -v
```

## Cookbook quality gates

Use the [cookbook quality gates](docs/COOKBOOK_QUALITY_GATES.md) to assess reproducibility, behavioral correctness, runtime validation, integration evidence, and operational safety consistently across the series. The rubric distinguishes confirmed defects from work that has not yet been verified; it does not imply that every repository has passed.

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
| [postgis-cookbook](https://github.com/ZQM-Computing/postgis-cookbook) | PostGIS cookbook: spatial indexing, joins & KNN, SRID management, vector tiles, data quality, partitioning |
| [duckdb-spatial-cookbook](https://github.com/ZQM-Computing/duckdb-spatial-cookbook) | DuckDB Spatial cookbook for analytical geospatial SQL: GeoParquet, spatial joins, KNN, H3 aggregation — no server required |
| [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) | GeoPandas/Shapely cookbook for Python geospatial workflows: spatial joins, CRS handling, overlays, interpolation, performance |
| [pgrouting-cookbook](https://github.com/ZQM-Computing/pgrouting-cookbook) | pgRouting network analysis on PostGIS: shortest path, driving distance, isochrones, turn restrictions, traffic-aware routing |
| [h3-cookbook](https://github.com/ZQM-Computing/h3-cookbook) | H3 hexagonal grid cookbook: indexing, aggregation, visualization, grid comparisons, performance benchmarks |
| [grass-cookbook](https://github.com/ZQM-Computing/grass-cookbook) | A GRASS cookbook for geoscientific analysis, terrain, and watershed modeling |
| [saga-cookbook](https://github.com/ZQM-Computing/saga-cookbook) | A SAGA cookbook for terrain analysis and geoscientific modeling from the command line |
| [whitebox-cookbook](https://github.com/ZQM-Computing/whitebox-cookbook) | A WhiteboxTools cookbook for terrain, hydrology, and LiDAR analysis from the command line |
| [cloudcompare-cookbook](https://github.com/ZQM-Computing/cloudcompare-cookbook) | A CloudCompare cookbook for point-cloud visualization, registration, and comparison |
| [pgpointcloud-cookbook](https://github.com/ZQM-Computing/pgpointcloud-cookbook) | A pgPointCloud cookbook for point-cloud patches in Postgres, PDAL ingest |
| [osmnx-cookbook](https://github.com/ZQM-Computing/osmnx-cookbook) | A OSMnx cookbook for street networks, routing, and OpenStreetMap graphs in Python |
| [timescaledb-cookbook](https://github.com/ZQM-Computing/timescaledb-cookbook) | A TimescaleDB cookbook — time-series hypertables on Postgres |
| [metpy-cookbook](https://github.com/ZQM-Computing/metpy-cookbook) | A MetPy cookbook — meteorological calculations on gridded data |
| [earthengine-cookbook](https://github.com/ZQM-Computing/earthengine-cookbook) | A Earth Engine cookbook — planetary-scale geospatial analysis from Python |
| [pymupdf-cookbook](https://github.com/ZQM-Computing/pymupdf-cookbook) | A PyMuPDF cookbook — PDF text, layout, and redaction from Python |
| [pdfplumber-cookbook](https://github.com/ZQM-Computing/pdfplumber-cookbook) | A pdfplumber cookbook — table and text extraction from PDFs |

### Formats & conversion

| Repo | What it covers |
|------|----------------|
| [gdal-cookbook](https://github.com/ZQM-Computing/gdal-cookbook) | GDAL/OGR command-line cookbook: runnable examples for conversion, reprojection, clipping, and mosaicking |
| [cog-cookbook](https://github.com/ZQM-Computing/cog-cookbook) | Cloud Optimized GeoTIFF cookbook: creation, validation, TiTiler serving, xarray integration, performance benchmarking |
| [geoparquet-cookbook](https://github.com/ZQM-Computing/geoparquet-cookbook) | GeoParquet cookbook for columnar geospatial analytics: partitioning, predicate pushdown, DuckDB/Spark integration |
| [pdal-cookbook](https://github.com/ZQM-Computing/pdal-cookbook) | A PDAL cookbook for point-cloud pipelines, translation, and pgPointCloud ingest |
| [rasterio-cookbook](https://github.com/ZQM-Computing/rasterio-cookbook) | A rasterio cookbook for raster reads, windows, reprojection, and COG pairing in Python |
| [rio-cogeo-cookbook](https://github.com/ZQM-Computing/rio-cogeo-cookbook) | A rio-cogeo cookbook — COG creation and validation from Python |
| [exiftool-cookbook](https://github.com/ZQM-Computing/exiftool-cookbook) | A ExifTool cookbook — metadata reading and writing from the command line |

### Discovery & serving

| Repo | What it covers |
|------|----------------|
| [stac-cookbook](https://github.com/ZQM-Computing/stac-cookbook) | STAC cookbook for geospatial data discovery: catalogs, item validation, search API, bulk operations, cloud deployment |
| [geospatial-api-reference](https://github.com/ZQM-Computing/geospatial-api-reference) | OGC API – Features reference implementation with FastAPI and PostGIS backends |
| [maplibre-cookbook](https://github.com/ZQM-Computing/maplibre-cookbook) | MapLibre GL JS cookbook for frontend vector tile rendering: custom layers, 3D terrain, performance tuning, interactive maps |
| [geoserver-cookbook](https://github.com/ZQM-Computing/geoserver-cookbook) | A GeoServer cookbook for publishing, styling, federating, and securing OGC services with GeoServer and PostGIS |
| [titiler-cookbook](https://github.com/ZQM-Computing/titiler-cookbook) | A TiTiler cookbook for serving cloud-native rasters as dynamic map tiles, STAC endpoints, and statistics APIs |
| [pgstac-cookbook](https://github.com/ZQM-Computing/pgstac-cookbook) | A pgSTAC cookbook for running a STAC catalog inside PostGIS and serving it with stac-fastapi |
| [martin-cookbook](https://github.com/ZQM-Computing/martin-cookbook) | A Martin cookbook for serving vector tiles straight from PostGIS, with function sources and tile serving at scale |
| [mapserver-cookbook](https://github.com/ZQM-Computing/mapserver-cookbook) | A MapServer cookbook for fast OGC services from mapfiles, via MS4W |
| [geonetwork-cookbook](https://github.com/ZQM-Computing/geonetwork-cookbook) | A GeoNetwork cookbook for spatial metadata catalogs, harvesting, and CSW search |
| [elasticsearch-cookbook](https://github.com/ZQM-Computing/elasticsearch-cookbook) | A Elasticsearch cookbook for single-node indices, mappings, and geo search |
| [geonode-cookbook](https://github.com/ZQM-Computing/geonode-cookbook) | A GeoNode cookbook — catalog, maps, and documents on Django and GeoServer |
| [osrm-cookbook](https://github.com/ZQM-Computing/osrm-cookbook) | A OSRM cookbook — routing engines from OpenStreetMap data |
| [pelias-cookbook](https://github.com/ZQM-Computing/pelias-cookbook) | A Pelias cookbook — open geocoding from OpenStreetMap and open data |
| [pystac-cookbook](https://github.com/ZQM-Computing/pystac-cookbook) | A pystac cookbook — STAC catalogs in Python: building, reading, and validating |
| [mapproxy-cookbook](https://github.com/ZQM-Computing/mapproxy-cookbook) | A MapProxy cookbook — cached and merged WMS/WMTS services |

### Desktop & field

| Repo | What it covers |
|------|----------------|
| [qgis-resources](https://github.com/ZQM-Computing/qgis-resources) | QGIS expressions, PyQGIS snippets, Processing scripts, styles, and QField field-collection guides |
| [qgis-cookbook](https://github.com/ZQM-Computing/qgis-cookbook) | A QGIS cookbook — PyQGIS automation, processing scripts, and plugin patterns |
| [webodm-cookbook](https://github.com/ZQM-Computing/webodm-cookbook) | A WebODM cookbook — drone imagery processing into maps and models |

### Infrastructure & operations

| Repo | What it covers |
|------|----------------|
| [proxmox-ceph-operations](https://github.com/ZQM-Computing/proxmox-ceph-operations) | Proxmox VE + Ceph operations runbooks: health checks, backup discipline, OSD replacement, upgrade checklists |
| [ollama-fleet-cookbook](https://github.com/ZQM-Computing/ollama-fleet-cookbook) | Ollama fleet operations cookbook: model management, health checks, load-spreading, VRAM budgeting, dependency-light RAG |
| [minio-cookbook](https://github.com/ZQM-Computing/minio-cookbook) | A MinIO cookbook for S3-compatible object storage from a source build |
| [nodered-cookbook](https://github.com/ZQM-Computing/nodered-cookbook) | A Node-RED cookbook for flow-based automation for geospatial and IoT triggers |
| [grafana-cookbook](https://github.com/ZQM-Computing/grafana-cookbook) | A Grafana cookbook for dashboards, datasources, and alerts for geospatial stacks |
| [prometheus-cookbook](https://github.com/ZQM-Computing/prometheus-cookbook) | A Prometheus cookbook for scrape jobs, PromQL, and alert rules with windows_exporter |
| [mosquitto-cookbook](https://github.com/ZQM-Computing/mosquitto-cookbook) | A Mosquitto cookbook for MQTT broker setup, listeners, and pub/sub patterns |
| [portainer-cookbook](https://github.com/ZQM-Computing/portainer-cookbook) | A Portainer cookbook — container management with an API and UI |
| [caddy-cookbook](https://github.com/ZQM-Computing/caddy-cookbook) | A Caddy cookbook — automatic-HTTPS reverse proxying from config and API |
| [authelia-cookbook](https://github.com/ZQM-Computing/authelia-cookbook) | A Authelia cookbook — single sign-on and two-factor authentication for proxied services |
| [uptime-kuma-cookbook](https://github.com/ZQM-Computing/uptime-kuma-cookbook) | A Uptime Kuma cookbook — uptime monitoring with status pages and notifications |
| [datahub-cookbook](https://github.com/ZQM-Computing/datahub-cookbook) | A DataHub cookbook — metadata catalog and lineage over data platforms |
| [vaultwarden-cookbook](https://github.com/ZQM-Computing/vaultwarden-cookbook) | A Vaultwarden cookbook — self-hosted password vault with clients and API |


### Pipelines & orchestration

| Repo | What it covers |
|------|----------------|
| [prefect-cookbook](https://github.com/ZQM-Computing/prefect-cookbook) | A Prefect cookbook for workflow orchestration, schedules, and deployments |
| [nifi-cookbook](https://github.com/ZQM-Computing/nifi-cookbook) | A NiFi cookbook for visual dataflow, ingestion, and feed-to-PostGIS pipelines |
| [dlt-cookbook](https://github.com/ZQM-Computing/dlt-cookbook) | A dlt cookbook for ELT pipelines from Python into Postgres and DuckDB |
| [dbt-cookbook](https://github.com/ZQM-Computing/dbt-cookbook) | A dbt cookbook for SQL transformations, models, and tests on Postgres |
| [airflow-cookbook](https://github.com/ZQM-Computing/airflow-cookbook) | A Airflow cookbook — DAGs, schedules, and geospatial pipelines |
| [redpanda-cookbook](https://github.com/ZQM-Computing/redpanda-cookbook) | A Redpanda cookbook — Kafka-compatible streaming for geospatial events |
| [airbyte-cookbook](https://github.com/ZQM-Computing/airbyte-cookbook) | A Airbyte cookbook — connector-based ELT into Postgres and DuckDB |
| [meltano-cookbook](https://github.com/ZQM-Computing/meltano-cookbook) | A Meltano cookbook — Singer-based ELT pipelines as code |

### Visualization & apps

| Repo | What it covers |
|------|----------------|
| [superset-cookbook](https://github.com/ZQM-Computing/superset-cookbook) | A Superset cookbook — dashboards and SQL exploration over geospatial tables |
| [streamlit-cookbook](https://github.com/ZQM-Computing/streamlit-cookbook) | A Streamlit cookbook — Python data apps for geospatial exploration |
| [folium-cookbook](https://github.com/ZQM-Computing/folium-cookbook) | A folium cookbook — interactive Leaflet maps from Python |
| [keplergl-cookbook](https://github.com/ZQM-Computing/keplergl-cookbook) | A kepler.gl cookbook — large-scale geospatial visualization in notebooks and apps |
| [plotly-cookbook](https://github.com/ZQM-Computing/plotly-cookbook) | A Plotly cookbook — interactive charts and geo charts from Python |

### Intelligence & OSINT

| Repo | What it covers |
|------|----------------|
| [scrapy-cookbook](https://github.com/ZQM-Computing/scrapy-cookbook) | A Scrapy cookbook for polite web scraping spiders, pipelines, and exports |
| [theharvester-cookbook](https://github.com/ZQM-Computing/theharvester-cookbook) | A theHarvester cookbook for passive reconnaissance from public sources |
| [spiderfoot-cookbook](https://github.com/ZQM-Computing/spiderfoot-cookbook) | A SpiderFoot cookbook for passive OSINT automation as a service |
| [amass-cookbook](https://github.com/ZQM-Computing/amass-cookbook) | A Amass cookbook for passive subdomain enumeration and graph output |
| [sherlock-cookbook](https://github.com/ZQM-Computing/sherlock-cookbook) | A Sherlock cookbook for username presence checks across public sites |
| [maigret-cookbook](https://github.com/ZQM-Computing/maigret-cookbook) | A Maigret cookbook for username search with extended site coverage and reporting |
| [shodan-cookbook](https://github.com/ZQM-Computing/shodan-cookbook) | A Shodan cookbook for internet-device search from the command line |
| [sentinelsat-cookbook](https://github.com/ZQM-Computing/sentinelsat-cookbook) | A sentinelsat cookbook for Copernicus Sentinel search and download patterns |
| [reconng-cookbook](https://github.com/ZQM-Computing/reconng-cookbook) | A Recon-ng cookbook for modular reconnaissance workspaces and resource scripts |
| [nuclei-cookbook](https://github.com/ZQM-Computing/nuclei-cookbook) | A Nuclei cookbook for bounded, authorized template scanning |
| [misp-cookbook](https://github.com/ZQM-Computing/misp-cookbook) | A MISP cookbook for threat-intelligence sharing platform, localhost-only deployment |
| [intelowl-cookbook](https://github.com/ZQM-Computing/intelowl-cookbook) | A IntelOwl cookbook — API-driven threat-intelligence enrichment |
| [snscrape-cookbook](https://github.com/ZQM-Computing/snscrape-cookbook) | A snscrape cookbook — social media scraping from Python and CLI |
| [ghunt-cookbook](https://github.com/ZQM-Computing/ghunt-cookbook) | A GHunt cookbook — Google-account investigation from a session |
| [certstream-cookbook](https://github.com/ZQM-Computing/certstream-cookbook) | A certstream cookbook — live certificate-transparency feeds in Python |
| [dnsrecon-cookbook](https://github.com/ZQM-Computing/dnsrecon-cookbook) | A dnsrecon cookbook — DNS enumeration from the command line |
| [ipwhois-cookbook](https://github.com/ZQM-Computing/ipwhois-cookbook) | A ipwhois cookbook — WHOIS and RDAP lookups from Python |
| [h8mail-cookbook](https://github.com/ZQM-Computing/h8mail-cookbook) | A h8mail cookbook — email breach hunting from the command line |
| [subfinder-cookbook](https://github.com/ZQM-Computing/subfinder-cookbook) | A Subfinder cookbook — passive subdomain discovery from public sources |
| [sublist3r-cookbook](https://github.com/ZQM-Computing/sublist3r-cookbook) | A Sublist3r cookbook — subdomain enumeration with search-engine sources |
| [holehe-cookbook](https://github.com/ZQM-Computing/holehe-cookbook) | A Holehe cookbook — email presence checks across public services |
| [phoneinfoga-cookbook](https://github.com/ZQM-Computing/phoneinfoga-cookbook) | A PhoneInfoga cookbook — phone-number OSINT from the command line |
| [blackbird-cookbook](https://github.com/ZQM-Computing/blackbird-cookbook) | A Blackbird cookbook — username search across social platforms |
| [waybackpy-cookbook](https://github.com/ZQM-Computing/waybackpy-cookbook) | A waybackpy cookbook — Wayback Machine queries and archiving from Python |
| [instaloader-cookbook](https://github.com/ZQM-Computing/instaloader-cookbook) | A Instaloader cookbook — Instagram data collection from the command line |
| [censys-cookbook](https://github.com/ZQM-Computing/censys-cookbook) | A Censys cookbook — internet scanning data from the command line |

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

The index CI checks repository-table structure against the machine-readable [canonical repository manifest](docs/repository-manifest.json), validates owner/slug consistency, and checks local Markdown links. It does not live-check remote GitHub availability or prove linked examples run or integrate together. Update the manifest and README together when the indexed portfolio changes. See [the repository documentation standard](docs/repository-documentation-standard.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

*Part of [ZQM Computing](https://github.com/ZQM-Computing) — geospatial engineering, scientific computing, and infrastructure patterns; the geospatial arm of [ZQM Labs](https://zqmlabs.com), makers of Z's Quests & Mischief location games.*

## License

MIT — see [LICENSE](LICENSE).

<!-- ZQM-FOOTER-START -->
<!-- markdownlint-disable MD033 -->
---

<p align="center">
  <em>Geospatial engineering · Scientific computing · Reproducible patterns</em><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a> ·
  <a href="https://github.com/ZQM-Labs">ZQM Labs</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-FOOTER-END -->
