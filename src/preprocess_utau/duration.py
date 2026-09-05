def oto_duration_seconds(entry, sample_rate=44100):
    # OTO cutoff is expressed in milliseconds; negative cutoff means duration from file end.
    return max(0.0, (entry.cutoff if entry.cutoff >= 0 else 0.0) / 1000.0)
