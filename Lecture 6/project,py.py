
import os
import sys
import platform
from pathlib import Path

print("=== PC SYSTEM HEALTH MONITOR ===")

# 1. System information
print("--- System Information ---")
print("Operating System:", platform.system())
print("OS Version:", platform.release())
print("Python Version:", sys.version.split()[0])
print("Current Directory:", os.getcwd())

# 2. Analyze a folder
folder = input("Enter folder path to analyze: ").strip()
folder = Path(folder)

if not folder.is_dir():
    print("Invalid folder path!")
    sys.exit()

# 3. Get files
files = [f for f in folder.iterdir() if f.is_file()]

print("Total files:", len(files))

# 4. Find large files (over 1 MB)
large_files = [
    f for f in files
    if f.stat().st_size > 1_000_000
]

print("\nFiles larger than 1 MB:")

for file in large_files:
    size_mb = file.stat().st_size / (1024 * 1024)
    print(f"{file.name}: {size_mb:.2f} MB")

# 5. Count file extensions
extensions = {}

for file in files:
    ext = file.suffix.lower() or "No extension"
    extensions[ext] = extensions.get(ext, 0) + 1

print("--- File Type Report ---")

for ext, count in extensions.items():
    print(f"{ext}: {count} file(s)")

print("Analysis completed!")
