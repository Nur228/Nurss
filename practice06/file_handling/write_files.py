from pathlib import Path

# Anchor the file next to this script so it works from any cwd.
SAMPLE = Path(__file__).resolve().parent / "sample.txt"

# Creating and writing to a file
with open(SAMPLE, "w") as f:
    f.write("Hello Python!\n")
    f.write("This is Practice 6.\n")

# Appending new lines
with open(SAMPLE, "a") as f:
    f.write("Appending a third line here.\n")
