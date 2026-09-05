from src.preprocess_utau.teto import normalize_teto_alias

def test_teto(): assert normalize_teto_alias('a ka')['kind']=='vcv'
