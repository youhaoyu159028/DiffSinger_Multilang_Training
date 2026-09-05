from pathlib import Path

def index_wavs(root):
    return {p.name.lower(): p for p in Path(root).rglob('*.wav')}
