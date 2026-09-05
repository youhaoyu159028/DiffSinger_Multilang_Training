import argparse
from .check_environment import main as check
from .train import main as train

def main():
    p=argparse.ArgumentParser(); p.add_argument('command',choices=['check','train']); a=p.parse_args(); return check() if a.command=='check' else train()
if __name__=='__main__': raise SystemExit(main())
