from ..utils.subprocess import run_command
class LocalRunner:
    def run(self, command, cwd=None): return run_command(command,cwd=cwd)
