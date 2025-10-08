import argparse

def get_config():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vfs", type=str, default=None)
    ap.add_argument("--prompt", type=str, default=None)
    ap.add_argument("--script", type=str, default=None)
    return ap.parse_args()