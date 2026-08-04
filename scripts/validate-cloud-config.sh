#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "Validating .cursor/environment.json..."
python3 -m json.tool .cursor/environment.json > /dev/null

python3 <<'PY'
import json
from pathlib import Path

path = Path(".cursor/environment.json")
data = json.loads(path.read_text())

allowed = {"name", "install", "start", "terminals", "ports", "build", "snapshot", "agentCanUpdateSnapshot", "user", "repositoryDependencies"}
unknown = set(data.keys()) - allowed
if unknown:
    raise SystemExit(f"Unknown keys in environment.json: {sorted(unknown)}")

if "install" not in data:
    raise SystemExit("environment.json must define an install script")

print("environment.json OK")
PY

test -f AGENTS.md || { echo "AGENTS.md missing"; exit 1; }
grep -q "Cursor Cloud specific instructions" AGENTS.md || { echo "AGENTS.md missing cloud section"; exit 1; }

echo "All cloud config checks passed."
