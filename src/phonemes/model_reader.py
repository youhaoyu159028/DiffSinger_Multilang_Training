import json
from pathlib import Path

def read_model_metadata(root):
    root=Path(root); out={'root':str(root)}
    for name in ['phonemes.json','languages.json']:
        p=root/name
        if p.exists(): out[name]=json.loads(p.read_text(encoding='utf-8'))
    return out
