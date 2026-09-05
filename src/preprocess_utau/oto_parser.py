from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class OtoEntry:
    wav: str; alias: str; offset: float; consonant: float; cutoff: float; preutterance: float; overlap: float; source: str; source_alias: str

def _f(x):
    try: return float(x)
    except (ValueError, TypeError): return 0.0

def parse_oto(path):
    path = Path(path); rows=[]
    for raw in path.read_text(encoding='utf-8-sig', errors='replace').splitlines():
        if '=' not in raw or ',' not in raw: continue
        wav, rest = raw.split('=',1); parts=rest.split(',')
        parts += [''] * (5-len(parts))
        alias, offset, consonant, cutoff, pre, overlap = parts[:6]
        rows.append(OtoEntry(str((path.parent / wav).resolve()), alias, _f(offset), _f(consonant), _f(cutoff), _f(pre), _f(overlap), path.parent.name, alias))
    return rows

def discover_oto_roots(root):
    return sorted(p.parent for p in Path(root).rglob('oto.ini'))
