# Geospatial repository documentation standard

Use this checklist when creating or revising a ZQM Computing geospatial pattern repository. It is intended to make examples reproducible and comparable; it does not assert that every repository is production deployed.

## Required README sections

1. **Purpose and scope** — the problem solved, supported formats/versions, and explicit exclusions.
2. **Prerequisites** — operating system assumptions, minimum versions, system packages, Python/Node/Go dependencies, and required external services.
3. **Quickstart** — commands that work from a clean checkout, with expected output and a cleanup command where resources are created.
4. **Examples** — input files, exact commands, expected output or invariant, and links to source files.
5. **Validation** — the CI workflow, local test command, and what the checks do not cover.
6. **Coordinate reference systems** — when spatial data is involved, state CRS/SRID, units, axis-order assumptions, and reprojection expectations.
7. **Data provenance and licensing** — distinguish synthetic fixtures from real data; document source, license, attribution, and privacy constraints for non-synthetic data.
8. **Performance and operational limits** — note expected scale, memory/disk needs, indexes, network access, and known failure modes.
9. **Security** — secret handling, least-privilege guidance, dependency audit coverage, and safe defaults.
10. **Relationships** — list related repositories and label each link as documentation, build dependency, runtime dependency, data flow, or deployment relationship.
11. **Maintenance** — supported versions, maintainer/contact, last verified date, and deprecation policy.

## Reproducible example contract

Every example should be runnable without private data or credentials. Prefer small synthetic fixtures. Each example should state:

- exact prerequisites and version assumptions;
- one copyable command or script;
- what files/services it creates and how to clean them up;
- expected output, exit status, or assertion;
- how the example handles invalid input and failure;
- whether the test is fully offline or contacts external services.

Avoid calling a pattern “production-tested” unless the repository contains verifiable test evidence and the claim defines the tested environment and scope.

## Dependency and integration labels

Use one of these terms for each asserted relationship:

- **Build dependency** — required to build/package the project.
- **Runtime dependency** — required while the deployed service runs.
- **Data flow** — produces or consumes a documented file/API format.
- **Deployment relationship** — publishes or configures a running environment.
- **Documentation link** — useful reading only; not a dependency.
- **Conceptual workflow** — suggested sequence, not verified integration.

A stack diagram is conceptual unless CI or deployment configuration proves the links. For an integration claim, identify the artifact/interface, direction, version expectation, and a reproducible check.

## Review checklist

- [ ] Quickstart tested from a clean checkout.
- [ ] Commands match the current file paths and dependency versions.
- [ ] Synthetic data is labeled and no private data or credentials are committed.
- [ ] CRS/SRID, units, and axis order are explicit where relevant.
- [ ] CI status and coverage limitations are accurately described.
- [ ] Links resolve and repository names match their canonical GitHub slugs.
- [ ] Deployment claims are backed by current configuration, not just a README.
- [ ] Date-sensitive instructions include a last-verified date.
