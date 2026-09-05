# Kaggle runner

`kernel-metadata.json` requests a T4 GPU and internet access. `train_kaggle.py` installs dependencies, runs the real CUDA check, then calls the same project training entry point.

The GitHub Actions workflow submits this directory with `kaggle kernels push -p kaggle`.
