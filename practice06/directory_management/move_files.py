from pathlib import Path
import shutil

# Anchor work next to this script so it doesn't depend on the current cwd.
HERE = Path(__file__).resolve().parent
SRC = HERE / "data.txt"
ARCHIVE = HERE / "archive"

# Create a source file and a destination folder
SRC.touch()
ARCHIVE.mkdir(exist_ok=True)

# Move the file
shutil.move(str(SRC), str(ARCHIVE / "data_v1.txt"))
