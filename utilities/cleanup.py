import os 
import shutil

def cleanup_pycache():
    for dirpath, dirnames, _ in os.walk("."):
        pycache_dirs = [d for d in dirnames if d == '__pycache__']
        for pycache_dir in pycache_dirs:
            pycache_path = os.path.join(dirpath, pycache_dir)
            shutil.rmtree(pycache_path)