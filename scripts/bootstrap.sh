#!/usr/bin/env bash
set -euo pipefail
python -m pip install -U pip
python -m pip install -r requirements.txt
bash scripts/check_environment.sh || true
