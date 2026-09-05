#!/usr/bin/env python3
import argparse, os, subprocess, time
from pathlib import Path
from .utils.config import load_yaml
from .utils.logging import setup_logging, append_jsonl
from .checkpoint.finder import find_latest
from .checkpoint.state import save_state

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',default='configs/train.yaml'); ap.add_argument('--resume',action='store_true'); ap.add_argument('--dry-run',action='store_true'); args=ap.parse_args()
    cfg=load_yaml(args.config); log=setup_logging(cfg['logging']['log_file']); append_jsonl(cfg['logging']['events_file'],{'event':'started','time':time.time()})
    command=cfg.get('trainer',{}).get('command',[])
    if not command:
        log.error('trainer.command is empty; configure the actual DiffSinger trainer before training.'); return 2
    ckpt=find_latest(cfg['checkpoint']['root']) if (args.resume or cfg['training'].get('resume')) else None
    state={'status':'starting','max_steps':cfg['training']['max_steps'],'resume_checkpoint':str(ckpt) if ckpt else None,'time':time.time()}; save_state(cfg['logging']['state_file'],state)
    if args.dry_run or cfg['training'].get('dry_run'):
        log.info('Dry run: %s', command); state['status']='dry_run_ok'; save_state(cfg['logging']['state_file'],state); return 0
    env=os.environ.copy(); env['DIFFSINGER_MAX_STEPS']=str(cfg['training']['max_steps'])
    if ckpt: env['DIFFSINGER_RESUME_CHECKPOINT']=str(ckpt)
    log.info('Launching trainer: %s',' '.join(command))
    p=subprocess.Popen(command,cwd=cfg['trainer'].get('cwd') or None,env=env,text=True)
    rc=p.wait(); state['status']='completed' if rc==0 else 'failed'; state['returncode']=rc; save_state(cfg['logging']['state_file'],state); append_jsonl(cfg['logging']['events_file'],{'event':state['status'],'time':time.time(),'returncode':rc}); return rc
if __name__=='__main__': raise SystemExit(main())
