#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    'docs/architecture/AB-6.0-001.md',
    'docs/engineering/Current-State.md',
    'standards/TESP/TESP-v1.0.md',
    'standards/DSOS/DSOS-v1.0.md',
    'standards/FIP/FIP-v1.0.md',
    'standards/TECR/TECR-v1.0.md',
    'standards/TECR/registry.csv',
    'standards/REII/REII-v1.0.md',
    'standards/RQC/RQC-v1.0.md',
    'standards/CSC/CSC-v1.0.md',
    'standards/json-schema/Canonical-Signal.schema.json',
]
errors=[]
for rel in REQUIRED:
    if not (ROOT/rel).exists():
        errors.append(f'Missing: {rel}')
for i in range(1,12):
    code=f'F{i:02d}'
    rel=f'runtime/contracts/{code}-Runtime-Contract.md'
    if not (ROOT/rel).exists():
        errors.append(f'Missing: {rel}')
try:
    json.loads((ROOT/'standards/json-schema/Canonical-Signal.schema.json').read_text())
except Exception as exc:
    errors.append(f'Invalid JSON Schema placeholder: {exc}')
if errors:
    print('Repository validation FAILED')
    print('\n'.join(errors))
    sys.exit(1)
print('Repository validation PASSED')
