import json
from pathlib import Path

def save_state(path, state):
    Path(path).parent.mkdir(parents=True,exist_ok=True); Path(path).write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')

def load_state(path):
    p=Path(path); return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
