from pathlib import Path

# Anchor the file next to this script so it works from any cwd.
SAMPLE = Path(__file__).resolve().parent / "sample.txt"

with open(SAMPLE, "r") as f:
    # read() gets everything
    # readline() gets one line
    # readlines() returns a list of lines
    content = f.readlines()
    for line in content:
        print(f"Line: {line.strip()}")
