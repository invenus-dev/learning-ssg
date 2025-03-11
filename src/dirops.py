import os
import shutil

def delete_dir_contents(dir):
    """Delete all contents of a directory."""
    if not os.path.exists(dir):
        return
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def copy_dir(src, dst):
    """Copy a directory tree from src to dst recursively."""
    # check dst dir exists
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_dir(s, d)
        else:
            shutil.copy2(s, d)
    