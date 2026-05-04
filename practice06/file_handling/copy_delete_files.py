import shutil
import os
from pathlib import Path

# Anchor file paths next to this script so the demo works from any cwd.
HERE = Path(__file__).resolve().parent
SRC = HERE / "sample.txt"
DST = HERE / "sample_backup.txt"

# Copying a file
shutil.copy(SRC, DST)

# Deleting the original file safely
if os.path.exists(SRC):
    os.remove(SRC)
    print("Original file deleted.")
