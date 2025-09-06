"""
===========================================================
📌 WORKING WITH FILE PATHS – COMPLETE NOTES
===========================================================

File paths are essential when working with files and directories in Python.  
Python provides two major ways to handle paths:
1. os.path (older, procedural)
2. pathlib (modern, object-oriented)

This file covers both approaches with examples.

-----------------------------------------------------------
📌 BASIC TERMINOLOGY
-----------------------------------------------------------
- Absolute Path → Full path from root (C:/Users/... on Windows)
- Relative Path → Path relative to the current working directory
- Current Working Directory (CWD) → Folder where Python is running

"""

# ===========================================================
# 1️⃣ USING os AND os.path MODULE
# ===========================================================
import os

print("📌 Using os.path for File Paths:")

# Get Current Working Directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Join paths (cross-platform)
file_path = os.path.join(cwd, "example.txt")
print("Joined File Path:", file_path)

# Get directory name and file name
print("Directory Name:", os.path.dirname(file_path))
print("Base File Name:", os.path.basename(file_path))

# Check if a path exists
print("Path exists?", os.path.exists(file_path))

# Split path into directory and filename
print("Split Path:", os.path.split(file_path))

# Get file extension
print("File Extension:", os.path.splitext(file_path))

# Normalize a path (clean unnecessary ../)
path_with_dots = os.path.normpath("folder1/../folder2/file.txt")
print("Normalized Path:", path_with_dots)

# Absolute Path
print("Absolute Path:", os.path.abspath("example.txt"))

# ===========================================================
# 2️⃣ USING pathlib MODULE (Recommended Modern Approach)
# ===========================================================
from pathlib import Path

print("\n📌 Using pathlib for File Paths:")

# Create a Path object
p = Path("example.txt")
print("Path Object:", p)

# Get absolute path
print("Absolute Path:", p.resolve())

# Get Parent Directory
print("Parent Directory:", p.parent)

# Get file name and suffix
print("File Name:", p.name)
print("File Suffix:", p.suffix)

# Check if file exists
print("File exists?", p.exists())

# Combine paths using /
new_path = Path.cwd() / "subfolder" / "data.txt"
print("Combined Path:", new_path)

# Create directory if not exists
Path("new_folder").mkdir(exist_ok=True)

# Iterate through files in a directory
print("Files in current directory:")
for file in Path.cwd().iterdir():
    print(" -", file)

# List only .txt files
print("Only TXT files in current directory:")
for file in Path.cwd().glob("*.txt"):
    print(" -", file)

# Recursively list files
print("All files recursively:")
for file in Path.cwd().rglob("*"):
    print(" -", file)

# ===========================================================
# 3️⃣ HANDLING FILES WITH PATH OBJECTS
# ===========================================================
example_file = Path("example.txt")

# Write text to file
example_file.write_text("Hello from pathlib!\nThis is a test file.")
print(f"Wrote to {example_file}")

# Read text from file
print("File Contents:")
print(example_file.read_text())

# Rename and Delete Files
renamed_file = Path("renamed_example.txt")
if example_file.exists():
    example_file.rename(renamed_file)
    print("File renamed to:", renamed_file)

if renamed_file.exists():
    renamed_file.unlink()  # Deletes the file
    print("File deleted successfully!")

# ===========================================================
# 4️⃣ CROSS-PLATFORM COMPATIBILITY
# ===========================================================
print("\n📌 Cross-Platform Paths:")
# Windows uses backslash \, Linux/Mac uses /
# Use pathlib or os.path.join to avoid issues
windows_style_path = Path("folder") / "subfolder" / "file.txt"
print("Cross-platform Path:", windows_style_path)

# ===========================================================
# 5️⃣ REAL-WORLD USE CASES
# ===========================================================
print("\n📌 Real-World Use Cases:")

# ✅ Example 1: Read all .log files from a logs directory
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)
for i in range(3):
    (logs_dir / f"log{i}.log").write_text(f"This is log {i}")

print("Log Files Found:")
for log_file in logs_dir.glob("*.log"):
    print(f" - {log_file.name}: {log_file.read_text()}")

# ✅ Example 2: Data Processing - Combine CSV files
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
(data_dir / "data1.csv").write_text("name,age\nAlice,25\nBob,30")
(data_dir / "data2.csv").write_text("name,age\nCharlie,22\nDaisy,28")

import pandas as pd
csv_files = list(data_dir.glob("*.csv"))
dfs = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(dfs)
print("\nCombined CSV Data:")
print(combined_df)

# ✅ Example 3: Safe file handling - check before reading
file_to_read = Path("safe_file.txt")
if file_to_read.exists():
    print("Safe File Contents:", file_to_read.read_text())
else:
    print("File not found, skipping read.")

"""
===========================================================
📌 SUMMARY
===========================================================
✅ os.path → Useful for quick path manipulation (old style)
✅ pathlib → Recommended (object-oriented, more readable)
✅ Always use join()/Path() instead of hardcoding slashes for cross-platform compatibility
✅ Use pathlib for modern file handling (mkdir, unlink, read_text, write_text)
✅ Real-world use cases include data pipelines, logging systems, file backups
===========================================================
"""
