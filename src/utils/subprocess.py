import subprocess

def run_command(command, cwd=None, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True, check=False)
