#!/usr/bin/env bash
set -euo pipefail
: "Usage: scripts/preprocess.sh ROOT OUTPUT SOURCE [LANGUAGE]"
ROOT="${1:?root}"; OUT="${2:?output}"; SOURCE="${3:?source}"; LANG="${4:-ja}"
python - <<PY
from src.dataset.builder import build
print(build(r'''$ROOT''',r'''$OUT''',r'''$SOURCE''',r'''$LANG'''))
PY
