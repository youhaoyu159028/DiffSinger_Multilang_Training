import json,sys
from pathlib import Path
p=Path('outputs/training_state.json')
print(p.read_text(encoding='utf-8') if p.exists() else '{"status":"not_started"}')
