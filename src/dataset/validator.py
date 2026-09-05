from pathlib import Path

def validate_manifest(path):
    errors=[]
    for i,line in enumerate(Path(path).read_text(encoding='utf-8').splitlines(),1):
        if not line.strip(): continue
        import json
        try: r=json.loads(line)
        except Exception as e: errors.append(f'line {i}: invalid json: {e}'); continue
        wav=r.get('wav')
        if not wav or not Path(wav).exists(): errors.append(f'line {i}: missing wav: {wav}')
    return errors
