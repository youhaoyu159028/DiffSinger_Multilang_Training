def normalize_alias(alias, source):
    if source == 'teto':
        from .teto import normalize_teto_alias; return normalize_teto_alias(alias)
    if source == 'adachi_rei':
        from .adachi_rei import normalize_adachi_alias; return normalize_adachi_alias(alias)
    return {'source_alias': alias.strip(), 'kind': 'unknown', 'phoneme_hint': alias.strip()}
