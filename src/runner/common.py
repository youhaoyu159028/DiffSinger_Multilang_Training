import os

def environment_snapshot():
    return {'git_sha': os.getenv('GITHUB_SHA','unknown'), 'runner': os.getenv('RUNNER_NAME','local')}
