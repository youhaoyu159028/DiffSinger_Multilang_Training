from pathlib import Path

def find_latest(root):
    files=[p for p in Path(root).glob('**/*') if p.is_file() and p.suffix in {'.ckpt','.pt','.pth','.safetensors'}]
    return max(files, key=lambda p:p.stat().st_mtime) if files else None
