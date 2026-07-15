# TDOS

Travel Decision Operating System (TDOS) is a decision-centric travel engineering system designed to produce operational, evidence-driven travel decisions and mission artifacts.

## Repository status

This repository is a **TDOS 6.0 engineering foundation bootstrap**.

- Architecture Baseline: `AB-6.0-001`
- Architecture state: `FROZEN`
- Current phase: `Runtime Engineering`
- Reference Implementation: `NOT STARTED`
- Verification: `NOT STARTED`

Canonical historical documents that were not available at bootstrap time are not reconstructed. Missing content is marked explicitly.

## Critical path

```text
CSC v1.0
  ↓
Canonical Signal JSON Schema v1.0
  ↓
Module Runtime Contracts F01–F11
  ↓
Verification Specification
  ↓
Reference Implementation
  ↓
Reference Mission Validation
  ↓
Operational Evidence
```

## Repository map

- `docs/architecture/` — architecture baseline and architecture references
- `docs/governance/` — governance model and decision flow
- `docs/engineering/` — engineering baseline and current-state records
- `standards/` — controlled standards and specifications
- `runtime/` — runtime contracts, artifacts and implementation
- `missions/` — reference missions and evidence
- `simulator/` — development simulator sessions and templates
- `adr/` — Architecture Decision Records
- `backlog/` — controlled backlog
- `tools/` — validation and repository utilities

## Development rules

1. Preserve `AB-6.0-001`.
2. Do not infer missing controlled content.
3. CSC remains the semantic authority.
4. JSON Schema is derived from CSC.
5. Runtime Contracts define module behaviour.
6. Implementation follows approved contracts.
7. Evidence precedes evolution.

## Validation

Run:

```bash
python3 tools/validate_repository.py
```
