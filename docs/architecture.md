# Architecture

GitHub is the source of truth for code/configuration. Kaggle is the formal automated GPU runner. Persistent storage owns datasets/checkpoints. The UTAU parser knows nothing about a specific multilingual base model; model adapters translate the unified representation into a selected model's actual phoneme/language vocabulary.
