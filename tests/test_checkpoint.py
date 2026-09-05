from src.checkpoint.state import save_state,load_state

def test_state(tmp_path):
    p=tmp_path/'s.json'; save_state(p,{'step':1}); assert load_state(p)['step']==1
