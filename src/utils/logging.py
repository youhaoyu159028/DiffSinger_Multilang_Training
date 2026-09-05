import json, logging, sys
from pathlib import Path

def setup_logging(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger('diffsinger')
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    fmt = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    sh = logging.StreamHandler(sys.stdout); sh.setFormatter(fmt); logger.addHandler(sh)
    fh = logging.FileHandler(path, encoding='utf-8'); fh.setFormatter(fmt); logger.addHandler(fh)
    return logger

def append_jsonl(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')
