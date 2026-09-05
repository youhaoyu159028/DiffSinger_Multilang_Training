from .finder import find_latest
class CheckpointManager:
    def __init__(self, root): self.root=root
    def latest(self): return find_latest(self.root)
