#!/usr/bin/env bash
set -euo pipefail
mkdir -p checkpoints
printf '%s\n' "Checkpoint persistence is handled by the configured trainer + external sync. Do not commit binary checkpoints." 
