#!/usr/bin/env bash
set -euo pipefail
bash scripts/check_environment.sh
python -m src.train --config configs/train.yaml --dry-run
