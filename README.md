# DiffSinger Multilingual Training

A resumable, hardware-agnostic training controller for UTAU voicebanks and multilingual DiffSinger models.

## Target
- Voices: 重音テト / Teto, 足立レイ / Adachi Rei
- Languages: Japanese, Mandarin Chinese, English, Cantonese
- GPU backend: Kaggle first; local/Colab-compatible execution is kept separate from the formal automation path.
- Persistent storage: external dataset/checkpoint storage; GitHub stores source/configuration only.

## Pipeline
UTAU voicebank -> UTAU parser -> unified dataset -> model adapter -> compatibility check -> DiffSinger trainer -> checkpoint -> persistent storage

The project does **not** include voicebanks, pretrained weights, or model binaries. Put them outside Git history and configure their paths through environment variables/configuration.

## Quick start
```bash
bash scripts/bootstrap.sh
bash scripts/check_environment.sh
bash scripts/dry_run.sh
bash scripts/train.sh
```

For Kaggle, the GitHub Actions workflow can push `kaggle/` as a Kaggle kernel after `KAGGLE_API_TOKEN` is configured as a repository secret.

## Safety of data handling
Do not commit raw WAV voicebanks, ONNX model weights, checkpoints, tokens, or private storage credentials. Check the voicebank/model licenses before training or redistributing generated assets.
