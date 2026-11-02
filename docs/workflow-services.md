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

Contact [ZQM Computing](mailto:zqmcomputing@gmail.com) with the recurring task,
tools, frequency, desired output, and approximate deadline. Do not send
credentials or confidential data through public GitHub issues. Commercial
terms and authorized data access are agreed before work begins.

## Demonstration under review

[GeoPandas PR #39](https://github.com/ZQM-Computing/geopandas-cookbook/pull/39)
adds a synthetic input-to-QA-report demonstration. At preparation, it is proposed
work, not a merged release. Use the PR to inspect its current status and checks.

The submitted revision `f5e2393444224715e774f0954d13264a67ca0830` passed 21 local
tests, the documentation checker, and a command-line smoke run. The fixture
reconciles eight rows into two accepted and six rejected. Tests cover invalid
batches, boundary inclusion, duplicate IDs, coordinate transformation,
repeatability, failed publication and input overwrite protection.

The bundle includes the source hash, software versions, CRS and rejection reasons.
It is a local single-writer demonstration using synthetic data. No client savings,
production throughput, multi-user operation or regulatory suitability is asserted.

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
