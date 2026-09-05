def normalize_teto_alias(alias):
    a = alias.strip()
    return {'source_alias': a, 'kind': 'vcv' if ' ' in a else 'cv', 'phoneme_hint': a}
