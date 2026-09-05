# Troubleshooting

## CUDA says available but training fails
Run `bash scripts/check_environment.sh`. It performs an actual CUDA tensor operation, not only `torch.cuda.is_available()`.

## Dataset unexpectedly contains unrelated WAVs
Use the UTAU discovery step. Only directories containing `oto.ini` should be parsed as voicebank roots.

## Resume starts from the wrong run
Inspect `outputs/training_state.json` and checkpoint metadata. Each run records config/model/git information where available.
