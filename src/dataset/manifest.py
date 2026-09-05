import json
from pathlib import Path

def write_jsonl(path, records):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path,'w',encoding='utf-8') as f:
        for r in records: f.write(json.dumps(r, ensure_ascii=False)+'\n')
