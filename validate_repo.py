from pathlib import Path

REQUIRED = [
    "README.md",
    "docs/engineering/CURRENT_STATE.md",
    "standards/FIP/FIP-v1.0.md",
    "standards/DSOS/DSOS-v1.0.md",
    "standards/REII/REII-v1.0.md",
    "simulator/TECR/TECR-v1.0.md",
    "standards/CSC/CSC-v1.0.md",
]

root = Path(__file__).resolve().parents[1]
missing = [item for item in REQUIRED if not (root / item).exists()]
if missing:
    raise SystemExit("Missing required files:\n" + "\n".join(missing))
print("TDOS repository bootstrap validation passed.")
