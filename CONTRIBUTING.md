# Contributing

## Baseline protection

`AB-6.0-001` is frozen. Contributions shall not modify architecture, ownership, governance, accepted ADRs or design principles without authorized review.

## Required process

1. Register or update the candidate in TECR.
2. Evaluate the candidate using FIP.
3. Identify affected controlled assets.
4. Apply RQC and governance-compatibility checks.
5. Produce an authorized review decision before integration.
6. Add verification and traceability evidence.

## Branches

- `main`: accepted baseline and explicitly labelled work-in-progress artifacts
- `develop`: integration work
- `feature/<name>`: isolated candidate work

## Commit convention

Use concise messages such as:

- `docs: revise CSC validation rules`
- `runtime: add F03 contract draft`
- `test: add canonical signal validation cases`
