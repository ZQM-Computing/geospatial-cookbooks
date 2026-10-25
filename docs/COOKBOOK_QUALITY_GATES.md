# Cookbook quality gates

## Purpose

Use this checklist to distinguish a useful, reproducible cookbook from a directory of plausible-looking snippets. Apply it repository by repository; do not infer maturity from README polish, repository size, badge presence, or a green static workflow.

## Evidence levels

| Level | Meaning | Minimum evidence |
|---|---|---|
| 0 — Discoverable | Users can identify the tool's purpose and limitations. | Accurate README, prerequisites, license, support status, links. |
| 1 — Reproducible | A new user can run at least one meaningful example. | Clean-checkout quickstart, pinned or bounded dependencies, synthetic/sample inputs, expected output. |
| 2 — Behavior-tested | Tests assert outcomes rather than implementation markers. | Deterministic fixtures; assertions for values, schemas, geometry/CRS, errors, and output safety as relevant. |
| 3 — Runtime-validated | The real engine executes the examples. | Exact commit, engine/provider versions, successful runtime CI or recorded reproducible run. |
| 4 — Integrated | Handoffs to another repository or service are demonstrated. | Explicit interface and compatibility contract plus an automated integration test or verified configuration. |
| 5 — Operationally hardened | Failure, scale, and recovery behavior are addressed. | Failure/cancellation/overwrite tests, performance limits, security/data provenance, troubleshooting and recovery guidance. |

A level is awarded only when its evidence exists. Unknown means **not yet verified**, not failed and not passed.

## Cross-cutting acceptance checklist

For each cookbook, record pass/fail/not-verified with a link to evidence:

- [ ] Clean-checkout quickstart succeeds without private credentials or undocumented manual setup.
- [ ] Example inputs are included, generated synthetically, or fetched from documented authoritative sources with licensing and provenance recorded.
- [ ] Expected outputs are described and asserted by tests.
- [ ] Dependencies and tested runtime versions are explicit.
- [ ] Spatial workflows state CRS/SRID, units, axis order, geometry semantics, nodata/resampling, and boundary behavior where applicable.
- [ ] Invalid input and no-result cases produce clear, actionable outcomes.
- [ ] Source inputs and pre-existing outputs are preserved unless an explicit overwrite/repair option is supplied.
- [ ] Reports and outputs are deterministic where feasible; timestamps and machine-specific paths do not create noisy diffs.
- [ ] CI distinguishes lint/static checks, unit/contract tests, actual engine/runtime tests, and external-service/manual checks.
- [ ] Security-sensitive examples do not embed credentials, disable validation, or imply authorization from reachability alone.
- [ ] README claims match the current code and CI evidence.
- [ ] Repository-to-repository relationships are labelled as documentation, build dependency, runtime dependency, data flow, or deployment; untested arrows remain conceptual.

## Domain-specific evidence

### QGIS / GDAL / raster

Test with synthetic raster/vector fixtures. Assert CRS, dimensions, extent, resolution, nodata behavior, feature counts, and expected numeric or geometric results. Include rotated affine transforms, empty intersections, missing CRS, failed writes, and existing-output preservation where relevant. A Python syntax check is not a QGIS runtime test.

### GeoPandas / GeoParquet / DuckDB / PostGIS

Assert geometry and attribute preservation, CRS metadata, schema, null/empty geometry behavior, duplicate and one-to-many join semantics, and stable query results. Benchmark claims must include dataset shape, versions, hardware/runtime context, and reproducible commands. For database examples, test initialization and cleanup against an isolated database.

### STAC / COG / OGC API / MapLibre

Validate STAC objects against the stated specification/version; inspect COG layout and overviews rather than only file extension; test API pagination, filtering, error responses, and authorization; and execute browser examples with known data sources and attribution. A local sample backend does not prove a live service is deployed.

### H3 / pgRouting

Test cell/resolution and coordinate edge cases, aggregation semantics, graph topology, unreachable destinations, directionality, and cost handling. A plausible map or route image is not a correctness assertion.

## Portfolio integration contract

Before claiming that repository A integrates with repository B, document:

1. The direction and purpose of the handoff.
2. The concrete interface: package, CLI, API, file format, or artifact.
3. Supported versions and relevant data/CRS assumptions.
4. A reproducible integration test or configuration proving the handoff.
5. Failure behavior and ownership of validation at the boundary.

Keep conceptual workflows in diagrams, but label them clearly. Do not promote a conceptual relationship to a verified dependency without evidence.

## Audit record template

Create one record per repository in an issue, PR, or tracker:

- Repository and commit SHA:
- Audit date:
- Evidence level achieved (0–5):
- Static/unit/runtime/integration checks and links:
- Confirmed defects (reproduction steps and impact):
- Not-yet-verified claims:
- Highest-value next change:
- Acceptance test for that change:
- Decision: improve / maintain / consolidate / archive, with rationale.

## Prioritization

Prioritize defects that can silently produce wrong spatial results, destroy or overwrite data, misrepresent CRS/units, expose data, or make a documented workflow fail. Next prioritize missing runnable end-to-end examples and tests. Defer SEO-only polishing when a repository's core examples cannot yet be reproduced.

This rubric is a governance tool, not evidence that any repository has passed it. Assess each project from its actual code, fixtures, workflows, and current commit.
