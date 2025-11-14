# ============================================================
# Working with the OS module in Python
# Full example with English comments
# ============================================================

import os


# ------------------------------------------------------------
# 1. Get the current working directory
# ------------------------------------------------------------
print("=== Current working directory ===")
print(os.getcwd())


# ------------------------------------------------------------
# 2. Change directory (BE CAREFUL: only works if the path exists)
# ------------------------------------------------------------
# Example (commented out for safety):
# os.chdir("C:/Users/Student/Desktop")
# print(os.getcwd())


# ------------------------------------------------------------
# 3. List files and directories
# ------------------------------------------------------------
print("\n=== List directory contents ===")
print(os.listdir())  # Lists current directory contents


# ------------------------------------------------------------
# 4. Create directories
# ------------------------------------------------------------
print("\n=== Creating directories ===")

# Create a single folder (fails if exists)
# os.mkdir("example_folder")

# Create nested folders safely
# os.makedirs("nested/folder/structure", exist_ok=True)


# ------------------------------------------------------------
# 5. Remove directories (only works if EMPTY)
# ------------------------------------------------------------
print("\n=== Removing directories ===")

# Remove a single empty folder
# os.rmdir("example_folder")

# Remove nested empty folders
# os.removedirs("nested/folder/structure")


# ------------------------------------------------------------
# 6. Delete files
# ------------------------------------------------------------
print("\n=== Deleting files ===")

# Example:
# if os.path.exists("test.txt"):
#     os.remove("test.txt")


# ------------------------------------------------------------
# 7. Rename or move files
# ------------------------------------------------------------
print("\n=== Renaming / moving files ===")

# Example:
# os.rename("old_name.txt", "new_name.txt")
# os.rename("folder/file.txt", "another_folder/file.txt")


# ------------------------------------------------------------
# 8. PATH UTILITIES (os.path)
# ------------------------------------------------------------
print("\n=== Path utilities ===")

p = os.path.join("C:", "Users", "Student", "Documents", "demo.txt")
print("Joined path:", p)

print("Does file exist?", os.path.exists("demo.txt"))
print("Is directory?", os.path.isdir("C:/"))
print("Is file?", os.path.isfile("demo.txt"))

sample_path = "C:/Users/Student/data.txt"
print("Basename:", os.path.basename(sample_path))      # data.txt
print("Dirname:", os.path.dirname(sample_path))        # C:/Users/Student
print("Splitext:", os.path.splitext(sample_path))      # ('.../data', '.txt')


# ------------------------------------------------------------
# 9. Environment variables
# ------------------------------------------------------------
print("\n=== Environment variables ===")

print("USERNAME:", os.environ.get("USERNAME"))
os.environ["MODE"] = "development"
print("MODE:", os.environ.get("MODE"))


# ------------------------------------------------------------
# 10. Run system commands
# ------------------------------------------------------------
print("\n=== System commands ===")

os.system("echo Hello from os.system!")   # Runs shell command


# ------------------------------------------------------------
# 11. YOUR ORIGINAL CODE (integrated and commented)
# ------------------------------------------------------------
print("\n=== Your original examples ===")

from os import cpu_count, path, system

# Number of CPU cores available
print("CPU count:", cpu_count())

# Directory name of the current file
print("Current file directory:", path.dirname(__file__))

# Execute terminal commands
system('echo Hello, World!')
system('python --version')   # Shows Python version
