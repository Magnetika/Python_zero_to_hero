from os import getcwd, path, makedirs, listdir
from pathlib import Path

# ---------------------------------------------
# Working with os.path (traditional method)
# ---------------------------------------------

# Get the current working directory
print("getcwd():", getcwd())

# Join path components safely (cross-platform)
joined_path = path.join("C:", "Users", "Student", "Documents", "data.txt")
print("Joined path:", joined_path)

# Example path for extracting parts
example_path = "C:/Users/Student/Documents/report.txt"

# Extract filename, directory, and extension
print("basename():", path.basename(example_path))     # report.txt
print("dirname():", path.dirname(example_path))       # C:/Users/Student/Documents
print("splitext():", path.splitext(example_path))     # ('.../report', '.txt')

# Check existence of file or directory
print("File exists?:", path.exists("report.txt"))
print("Is file?:", path.isfile("report.txt"))
print("Is directory?:", path.isdir("C:/Users"))

# ---------------------------------------------
# Using pathlib (modern, recommended method)
# ---------------------------------------------

# Create a Path object
data_dir = Path("C:/Users/Student/Documents")
file_path = data_dir / "data.txt"  # Using / operator to join

print("Path using pathlib:", file_path)

# Extract path parts
example = Path("C:/Users/Student/Documents/report.txt")
print("Name:", example.name)       # report.txt
print("Stem:", example.stem)       # report
print("Suffix:", example.suffix)   # .txt
print("Parent:", example.parent)   # path to folder

# Check file existence
if file_path.exists():
    print("File found:", file_path)
else:
    print("File not found:", file_path)

# Create a directory safely
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)  # no error if folder exists
print("Created directory:", results_dir.resolve())

# List contents of current directory
print("Directory contents:")
for item in Path(".").iterdir():
    print(" -", item)

# Writing & reading a file using pathlib
notes_file = Path("notes.txt")
notes_file.write_text("Hello, Pathlib!")
print("File content:", notes_file.read_text())

# Get the absolute, normalized path
absolute_path = notes_file.resolve()
print("Absolute path:", absolute_path)

# Normalize a messy path using resolve()
messy_path = Path("folder/subfolder/../data")
print("Normalized path:", messy_path.resolve())
