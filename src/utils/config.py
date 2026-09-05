from pathlib import Path
import yaml

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}

def project_root():
    return Path(__file__).resolve().parents[2]
