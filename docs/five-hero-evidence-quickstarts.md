# Five verified starting points for reproducible GIS

**Choose a question, not a repository count.** These five ZQM Computing
examples use locally generated or synthetic fixtures and have documented
test entry points. Their purpose is reproducibility and inspection,
not marketing claims about speed, customers or externally observed
environmental impacts.

**Verified source inventory:** inspected the linked canonical repositories
after the November 2026 quality changes. Individual examples can require
GDAL, PySTAC, DuckDB extensions or Python project dependencies.
Each repository's *current exact commit and CI* still governs reproducibility.

## 1. What happens when GIS data coverage is missing?

**[DuckDB Spatial: Unknown versus zero](https://github.com/ZQM-Computing/duckdb-spatial-cookbook/blob/main/docs/unknown-vs-zero-parcel-screening.md)**

Read a synthetic four-parcel/nine-site fixture, count recorded
observations only for covered parcels, and preserve `NULL`
for one deliberately uncovered parcel. A zero count does **not**
certify the absence of environmental risk.

```bash
python scripts/run_examples.py
```

Run from the DuckDB Spatial repository root after installing its
documented dependencies. The command executes eight SQL patterns and
the golden expected-result checks.

## 2. Did converting a TIFF to COG preserve its raster?

**[COG: Source-versus-converted integrity](https://github.com/ZQM-Computing/cog-cookbook/blob/main/docs/source-vs-cog-integrity.md)**

Create a synthetic constant-valued 512×512 raster, convert it into a
COG with overviews, and compare dimensions, CRS, geotransform, nodata,
GDAL per-band pixel checksums and local SHA-256 file hashes. A
synthetic match is **not** proof of remote HTTP range efficiency.

The linked guide includes exact prerequisite, generation, conversion
and evidence-report commands:

```bash
python examples/07-source-cog-integrity/run.py \
  examples/01-cog-creation/data/input.tif \
  examples/01-cog-creation/output/output_overviews.tif \
  --output /tmp/cog-integrity-evidence.json
```

Run this only **after** the guide's synthetic raster creation and
Example 01 conversion; the command alone requires existing files.

## 3. Are claimed GeoParquet size and speed wins actually measured?

**[GeoParquet: Evidence-first format comparison](https://github.com/ZQM-Computing/geoparquet-cookbook/blob/main/docs/measured-format-stories.md)**

The existing 10,000-synthetic-point smoke run produces exact
GeoJSON/GeoParquet byte counts, single-run timings, a filter count,
software versions and a machine-readable JSON report.

```bash
python examples/06-performance/run.py
```

This does **not** test Shapefile conversion, 1.1 million real
polygons or universal GeoParquet speedups. A credible performance
study needs matched data, verified semantics, repeated runs and
documented cache/hardware state.

## 4. Can my STAC assets be checked for file integrity?

**[STAC: Local asset integrity](https://github.com/ZQM-Computing/stac-cookbook/blob/main/examples/13-stac-asset-integrity/run.py)**

The example generates original synthetic bytes, creates a local
STAC Item/Catalog with file-size and SHA-256 multihash fields,
then checks the saved local referenced asset. It rejects escaped
or untrusted local paths. No cloud bucket or paid API is required.

```bash
python examples/13-stac-asset-integrity/run.py
```

Run from the STAC repository root after installing the documented
PySTAC dependencies. This proves the synthetic asset reference
integrity test, not ownership of third-party remote imagery or
continuous live STAC service availability.

## 5. How should I sanity-check AI-generated spatial answers?

**[GeoPandas: Offline spatial reasoning checks](https://github.com/ZQM-Computing/geopandas-cookbook/blob/main/docs/spatial-ai-evaluation.md)**

Inspect six public, synthetic reasoning questions—area, distance,
boundary inclusion, spatial-join cardinality, geographic CRS area
handling and missing imagery coverage. Optionally score a manually
assembled JSON response set.

```bash
python demos/spatial_ai_arena.py --questions
```

This is **not** a blinded model benchmark, vendor leaderboard or
evidence of integration with an external model provider.

## Choose a product path without conflating ZQM brands

ZQM Computing publishes these reusable GIS analysis patterns.
[ZQM Labs](https://github.com/ZQM-Labs) separately maintains
[a public six-stop content sample](https://github.com/ZQM-Labs/quest-packs/tree/main/sample-quest),
[a first-quest authoring tutorial](https://github.com/ZQM-Labs/quest-authoring/blob/main/guide/write-your-first-quest.md)
and an [offline organizer kit](https://github.com/ZQM-Labs/organizer-toolkit).
The game demo, a source code fixture, a reviewed host event and
a completed purchase are different states.

For prospective commercial GIS work, see
[ZQM Computing's workflow-services guide](workflow-services.md).
For host-run quest feasibility, see the ZQM Labs public authoring
and organizer documentation. No customer outcome, paid service
availability or measured organic traffic is asserted here.

## Publication evidence checklist

Any example included in a case study or social post must carry:
source commit and runtime version; fixture/data license;
question and expected answer; verification command/test; relevant
units/CRS; exact measured result if using numbers; limitations;
and a clear separation between **synthetic demonstration** and
real observational/customer evidence.

These quickstarts are technical entry points, not statistics about
GitHub stars, visits, sales, model ranking or outdoor engagement.
