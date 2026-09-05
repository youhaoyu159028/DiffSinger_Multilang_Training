from src.phonemes.unified import UnifiedRecord

def test_record(): assert UnifiedRecord('a.wav','ja',['a'],[],'teto','a').language=='ja'
