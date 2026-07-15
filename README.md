# TDOS 6.0

TDOS is a decision-centric travel operating system intended to convert travel needs, verified evidence, constraints and runtime observations into operational decisions and mission artifacts.

## Repository status

- Architecture baseline: `AB-6.0-001`
- Architecture state: Frozen
- Current phase: Runtime Engineering
- Reference implementation: Not started
- Verification execution: Not started

This repository is an engineering baseline repository. It separates architecture, governance, runtime semantics, implementation contracts, reference missions and Development Simulator inputs.

## Critical dependency chain

```text
CSC v1.0
  -> Canonical Signal JSON Schema v1.0
  -> Module Runtime Contracts F01-F11
  -> Verification Specification
  -> Reference Implementation
  -> Reference Mission Validation
  -> Operational Evidence
```

Downstream artifacts shall not redefine upstream semantics.

## Repository map

- `docs/architecture`: architecture baseline and design documents
- `docs/governance`: governance summaries and review flows
- `docs/engineering`: current engineering state and baseline-set information
- `standards`: controlled engineering standards and specifications
- `runtime/contracts`: F01-F11 runtime contracts
- `runtime/reference-implementation`: implementation skeleton
- `missions`: reference mission evidence and candidate inputs
- `simulator`: Development Simulator onboarding, TECR and session records
- `tests`: verification test assets

## Important limitation

Several canonical artifacts remain under development. Files marked `DRAFT`, `NOT STARTED`, or `PLACEHOLDER` are not approved baseline content.
