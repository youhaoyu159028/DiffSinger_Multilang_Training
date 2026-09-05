import os, subprocess, sys
print('Kaggle runner bootstrap')
print('GPU selection requested: T4; actual hardware must be validated.')
subprocess.run([sys.executable,'-m','pip','install','-r','requirements.txt'],check=False)
rc=subprocess.call(['bash','scripts/check_environment.sh'])
if rc:
    raise SystemExit('Environment check failed; refusing to start training.')
raise SystemExit(subprocess.call(['bash','scripts/train.sh']))
