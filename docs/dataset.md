# Dataset pipeline

1. Discover voicebank roots from `oto.ini`.
2. Parse aliases and timing fields.
3. Apply Teto/Adachi-specific normalization.
4. Produce a unified JSONL manifest.
5. Validate WAV existence and model compatibility.
6. Stop on unsupported mappings rather than silently substituting phonemes.
