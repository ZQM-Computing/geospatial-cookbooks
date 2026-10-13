# ZQM Geospatial Patterns

Production-tested geospatial patterns for every layer of the stack — from conversion (GDAL) to serving (STAC API).

**ZQM Computing** is the geospatial engineering arm of **ZQM Labs** — the games studio behind Z's Quests & Mischief. These patterns ground ZQM Labs games in real-world locations across Volusia County, Florida.

ZQM Labs builds location-based scavenger-hunt games. ZQM Computing provides the geospatial engine: QGIS for desktop mapping, GDAL for asset conversion, GeoPandas for spatial analysis, PostGIS for system of record, pgRouting for route optimization, DuckDB for analytics, COG/STAC for raster serving, MapLibre for frontend, and H3 for location binning.

## The Stack

```
Desktop (QGIS) -> Conversion (GDAL) -> Python (GeoPandas) -> System of Record (PostGIS)
    -> Routing (pgRouting) -> Analytical (DuckDB) -> Columnar (GeoParquet)
    -> Raster (COG) -> Discovery (STAC) -> Frontend (MapLibre) -> Grid (H3)
    -> Serving (OGC API Features)
```

## Repos

| Layer | Repo | Description |
|---|---|---|
| Desktop | [qgis-resources](https://github.com/ZQM-Computing/qgis-resources) | QGIS expressions, PyQGIS, styles, QField |
| Conversion | [gdal-patterns](https://github.com/ZQM-Computing/gdal-patterns) | GDAL/OGR CLI: reprojection, conversion, VRT |
| Python | [geopandas-patterns](https://github.com/ZQM-Computing/geopandas-patterns) | GeoPandas: spatial joins, CRS, overlays |
| System of Record | [postgis-patterns](https://github.com/ZQM-Computing/postgis-patterns) | PostGIS: indexing, MVT, KNN |
| Routing | [pgrouting-patterns](https://github.com/ZQM-Computing/pgrouting-patterns) | pgRouting: Dijkstra, A*, isochrones |
| Analytical | [duckdb-spatial-patterns](https://github.com/ZQM-Computing/duckdb-spatial-patterns) | DuckDB: SQL spatial, GeoParquet, H3 |
| Columnar | [geoparquet-patterns](https://github.com/ZQM-Computing/geoparquet-patterns) | GeoParquet: partitioning, predicate pushdown |
| Raster | [cog-patterns](https://github.com/ZQM-Computing/cog-patterns) | Cloud Optimized GeoTIFF: creation, serving |
| Discovery | [stac-patterns](https://github.com/ZQM-Computing/stac-patterns) | STAC: catalogs, validation, search API |
| Frontend | [maplibre-patterns](https://github.com/ZQM-Computing/maplibre-patterns) | MapLibre GL JS: vector tiles, 3D terrain |
| Grid | [h3-patterns](https://github.com/ZQM-Computing/h3-patterns) | H3: hexagonal binning, aggregation |
| Serving | [geospatial-api-reference](https://github.com/ZQM-Computing/geospatial-api-reference) | OGC API - Features with FastAPI |
| Infrastructure | [proxmox-ceph-operations](https://github.com/ZQM-Computing/proxmox-ceph-operations) | Proxmox VE + Ceph runbooks |
| AI ops | [ollama-fleet-patterns](https://github.com/ZQM-Computing/ollama-fleet-patterns) | Ollama fleet operations |

## Quick start

```bash
# Python stack
pip install geopandas duckdb pystac rasterio h3

# System stack
sudo apt install gdal-bin postgresql postgis pgrouting

# Docker stack
docker-compose up -d  # pgrouting-patterns
```

## Who this is for

Geospatial developers, GIS analysts, data engineers, and Python developers who need production-tested patterns for spatial data workflows.

## License

MIT — see each repo's LICENSE file.

*Part of [ZQM Labs](https://github.com/ZQM-Computing) — games, gear & a little mischief.*
