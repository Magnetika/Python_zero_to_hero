import os

# -------------------------------------------
# 1. Get the current working directory
# -------------------------------------------
print("Current working directory:", os.getcwd())

# -------------------------------------------
# 2. Create a new directory
# -------------------------------------------
dir_name = "example_dir"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)  # Creates a single directory
    print(f"Directory '{dir_name}' created.")
else:
    print(f"Directory '{dir_name}' already exists.")

# -------------------------------------------
# 3. List the contents of the current directory
# -------------------------------------------
print("\nContents of current directory:")
print(os.listdir('.'))

# -------------------------------------------
# 4. Rename the created directory
# -------------------------------------------
new_dir_name = "renamed_dir"

if os.path.exists(dir_name):
    os.rename(dir_name, new_dir_name)  # Renames/moves the directory
    print(f"Directory renamed to '{new_dir_name}'.")
else:
    print(f"Directory '{dir_name}' not found for renaming.")

# -------------------------------------------
# 5. Create a nested directory structure
# -------------------------------------------
nested_path = "projects/python/scripts"
os.makedirs(nested_path, exist_ok=True)  # Creates nested folders safely
print(f"Nested directories '{nested_path}' created.")

# -------------------------------------------
# 6. Check if a path exists, is a file or directory
# -------------------------------------------
print("\nPath checks:")
print("Does 'renamed_dir' exist?", os.path.exists(new_dir_name))
print("Is 'renamed_dir' a directory?", os.path.isdir(new_dir_name))
print("Is 'renamed_dir' a file?", os.path.isfile(new_dir_name))

# -------------------------------------------
# 7. Create a file to demonstrate file operations
# -------------------------------------------
file_name = "example_file.txt"
with open(file_name, "w") as f:
    f.write("This is an example file.")
print(f"\nFile '{file_name}' created.")

# List contents again
print("Directory contents after file creation:")
print(os.listdir('.'))

# -------------------------------------------
# 8. Remove the created file
# -------------------------------------------
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"File '{file_name}' removed.")

# -------------------------------------------
# 9. Remove the renamed directory
# -------------------------------------------
if os.path.exists(new_dir_name):
    os.rmdir(new_dir_name)  # Will work only if directory is empty
    print(f"Directory '{new_dir_name}' removed.")

# -------------------------------------------
# 10. Remove empty nested directories
# -------------------------------------------
os.removedirs(nested_path)  # Removes all empty parent folders
print(f"Nested directories '{nested_path}' removed (if empty).")

# -------------------------------------------
# 11. Walk through directory tree using os.walk()
# -------------------------------------------
print("\nWalking through the current directory tree:\n")
for root, dirs, files in os.walk(".", topdown=True):
    print("Current folder:", root)
    print("Subfolders:", dirs)
    print("Files:", files)
    print("--------------------")

# -------------------------------------------
# Final directory check
# -------------------------------------------
print("\nFinal contents of the current directory:")
print(os.listdir('.'))

# Confirm removal
if not os.path.exists(dir_name):
    print(f"Directory '{dir_name}' does not exist.")

if not os.path.exists(file_name):
    print(f"File '{file_name}' does not exist.")
