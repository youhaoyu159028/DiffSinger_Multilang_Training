from src.preprocess_utau.oto_parser import parse_oto

def test_parse(tmp_path):
    (tmp_path/'a.wav').write_bytes(b'')
    (tmp_path/'oto.ini').write_text('a.wav=ka,0,100,0,50,25\n',encoding='utf-8')
    x=parse_oto(tmp_path/'oto.ini'); assert x[0].alias=='ka'; assert x[0].preutterance==50
