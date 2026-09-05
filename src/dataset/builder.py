from pathlib import Path
from ..preprocess_utau.oto_parser import parse_oto, discover_oto_roots
from ..preprocess_utau.normalize import normalize_alias
from ..phonemes.unified import UnifiedRecord, to_dict
from .manifest import write_jsonl

def build(root, output, source, language='ja'):
    records=[]; unresolved=[]
    for oto_root in discover_oto_roots(root):
        for e in parse_oto(oto_root/'oto.ini'):
            if not e.alias.strip(): unresolved.append({'wav':e.wav,'reason':'empty_alias'}); continue
            n=normalize_alias(e.alias, source)
            records.append(to_dict(UnifiedRecord(e.wav,language,[n['phoneme_hint']],[],source,e.alias)))
    write_jsonl(output, records)
    return {'records':len(records),'unresolved':unresolved}
