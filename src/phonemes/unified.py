from dataclasses import dataclass, asdict

@dataclass
class UnifiedRecord:
    wav: str
    language: str
    phonemes: list
    durations: list
    source: str
    source_alias: str

def to_dict(record): return asdict(record)
