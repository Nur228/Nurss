import os
from pathlib import Path

# Anchor work next to this script so it doesn't depend on the current cwd.
HERE = Path(__file__).resolve().parent

# Create nested directories
os.makedirs(HERE / "parent" / "child" / "grandchild", exist_ok=True)

# List files and folders in this script's directory
print("Directory Contents:", os.listdir(HERE))

# Find files by extension (e.g., .py)
py_files = [f for f in os.listdir(HERE) if f.endswith(".py")]
print(f"Python files found: {py_files}")
