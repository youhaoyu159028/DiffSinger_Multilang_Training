from src.phonemes.compatibility import check_languages

def test_missing(): assert not check_languages(['yue'],['ja','zh'])['ok']
