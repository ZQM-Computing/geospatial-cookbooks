# Geospatial workflow services and technical evidence

ZQM Computing helps engineering and environmental teams assess recurring GIS
work, identify useful automation, and define verifiable implementation scopes.
The cookbook collection provides technical references for that work. Each
client engagement still requires validation against actual data and requirements.

## Start with the business problem

| Recurring problem | Relevant technical foundation | Evidence required for a client implementation |
| --- | --- | --- |
| Repeated data preparation and spatial QA | [GeoPandas](https://github.com/ZQM-Computing/geopandas-cookbook), [GDAL](https://github.com/ZQM-Computing/gdal-cookbook) | Agreed input contract, reason-coded rejects, CRS handling, reconciled rows and rerun tests |
| Spatial database migration or slow queries | [PostGIS](https://github.com/ZQM-Computing/postgis-cookbook) | Source/target reconciliation, representative query measurements, rollback and recovery evidence |
| Repeated large-file analytical queries | [GeoParquet](https://github.com/ZQM-Computing/geoparquet-cookbook), [DuckDB Spatial](https://github.com/ZQM-Computing/duckdb-spatial-cookbook) | Equivalent results, recorded dataset size, versions, runtime and memory measurements |
| Repeated desktop GIS processing | [QGIS resources](https://github.com/ZQM-Computing/qgis-resources) | Validated processing inputs/outputs, runtime requirements and operator handoff |

These are topic-to-repository mappings, not claims of deployed integration,
customer outcomes, or guaranteed savings. Prefer the smallest workflow that
addresses the buyer's actual problem.

## Proposed starting engagement

**GIS Workflow Diagnostic — $1,500 fixed fee, subject to confirmed scope and
availability.** One recurring process, up to three agreed representative inputs,
and one target output. Target delivery is five business days after kickoff and
receipt of agreed inputs.

Deliverables:

- A workflow walkthrough and map of the current process.
- A baseline with measured results separated from staff estimates.
- Prioritized automation and validation recommendations.
- A separately scoped implementation proposal with acceptance criteria, or a
  recommendation to retain the current process when investment is not justified.
- A findings review and one consolidated clarification round.

Production implementation, new licenses, full dataset cleanup, fieldwork, and
ongoing support are separate. The diagnostic does not include a certified survey,
engineering opinion, environmental site assessment, or regulatory determination.

Request a 20-minute fit call with [ZQM Computing](mailto:alexzelenski@outlook.com)
about the recurring task, tools, frequency, desired output, and approximate
deadline. Do not send credentials or confidential datasets through ordinary
email or public GitHub issues. Contracting identity, commercial terms and
secure authorized data access must be agreed before delivery.

## Verified synthetic demonstration and supporting references

The [GeoPandas workflow diagnostic demonstration](https://github.com/ZQM-Computing/geopandas-cookbook/blob/main/docs/workflow-diagnostic.md)
was merged in [PR #39](https://github.com/ZQM-Computing/geopandas-cookbook/pull/39)
(commit `45f2ac45d71d6c478be862f455630757c911bace`).
The sample reconciles eight incoming records into two accepted and six
reason-coded rejects. It covers explicit CRS handling, boundary inclusion,
duplicate IDs, repeatability and last-good-output preservation. All eight
GitHub Actions workflows passed on the reviewed PR head before merge. This
proves the synthetic demo contract in that environment, **not** a client
case study, production throughput guarantee, or measured labor savings.

The [QGIS dataset QA guide](https://github.com/ZQM-Computing/qgis-resources/blob/main/docs/DATASET_QA.md)
explains read-only vector/raster inspection and report output. The
[October 31, 2026 runtime baseline](https://github.com/ZQM-Computing/qgis-resources/actions/runs/41242191186)
passed with QGIS 3.40.15 on a Linux runner; subsequent
[report-publication safeguards](https://github.com/ZQM-Computing/qgis-resources/pull/36)
also passed their own exact-head QGIS suite and were merged. Do not infer
Windows or production compatibility from these synthetic tests.

The [PostGIS migration discovery template](https://github.com/ZQM-Computing/postgis-cookbook/blob/main/docs/migration-discovery.md)
provides an inventory, reconciliation, risk and acceptance checklist for
scoping spatial-database changes. Its documentation and SQL examples are
not evidence that a particular client's migration was performed.

## Follow-on professional services

| Offer | Proposed commercial model | Scope boundary |
| --- | --- | --- |
| One-workflow implementation | $5,000–$12,000 test range | Agreed workflow, validation, documentation and handoff; discovery first |
| Fractional geospatial lead | $3,500/month for up to 20 hours | Scheduled technical leadership on a named backlog; no unlimited availability |
| Migration discovery | $2,000–$4,000 test range | Source/target inventory, reconciliation, risks, acceptance criteria; migration separate |

All prices are proposed market tests, subject to confirmed scope and agreement.
Open-source use never requires purchasing services.

## From diagnostic to implementation

An implementation agreement should define input formats and sizes, access,
the responsible reviewer, geometry and boundary rules, acceptance thresholds,
failure recovery, software ownership, maintenance and handoff. Acceptance should
include both representative valid data and deliberately invalid cases.

For a migration, require evidence that records were preserved or explicitly
rejected. For a performance change, compare equivalent results before timing.
For a recurring workflow, measure review and maintenance effort alongside runtime.

Open-source examples remain available under their respective licenses.
Paid engagements cover discovery, client-specific integration, validation,
training and ongoing responsibility. A service purchase is not required to use
the cookbook code.
