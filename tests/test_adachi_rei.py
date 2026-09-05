from src.preprocess_utau.adachi_rei import normalize_adachi_alias

def test_adachi(): assert normalize_adachi_alias('a')['phoneme_hint']=='a'
