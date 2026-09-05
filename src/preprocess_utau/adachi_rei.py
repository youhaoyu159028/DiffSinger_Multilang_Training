def normalize_adachi_alias(alias):
    a = alias.strip()
    return {'source_alias': a, 'kind': 'alias', 'phoneme_hint': a}
