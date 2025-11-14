import os
import shutil
from pathlib import Path

# -------------------------------------------------------
# Ensure the script runs in its own folder
# -------------------------------------------------------
base_dir = Path(__file__).parent
os.chdir(base_dir)
print("Current working directory:", os.getcwd())


# =======================================================
# 1. CREATE TEST DIRECTORIES AND FILES
# =======================================================

# Create a source directory
src_dir = Path("source_folder")
src_dir.mkdir(exist_ok=True)

# Create a file inside source_folder
file_path = src_dir / "example.txt"
file_path.write_text("This is an example file created for shutil demonstration.")
print("\nCreated:", file_path)


# =======================================================
# 2. COPY FILES
# =======================================================

# Copy file to a new location
copy_target = Path("copied_example.txt")
shutil.copy(file_path, copy_target)
print("File copied using shutil.copy():", copy_target)

# Copy file with metadata preserved
copy2_target = Path("copied_with_metadata.txt")
shutil.copy2(file_path, copy2_target)
print("File copied with metadata using shutil.copy2():", copy2_target)


# =======================================================
# 3. COPY AN ENTIRE DIRECTORY
# =======================================================

backup_dir = Path("backup_folder")

# Copy directory and allow overwriting if it exists (Python 3.8+)
shutil.copytree(src_dir, backup_dir, dirs_exist_ok=True)
print("\nDirectory copied using shutil.copytree():", backup_dir)


# =======================================================
# 4. MOVE FILES OR DIRECTORIES
# =======================================================

moved_dir = Path("moved_folder")

# Move the entire directory
shutil.move(str(src_dir), moved_dir)
print("Directory moved to:", moved_dir)


# =======================================================
# 5. DELETE DIRECTORIES RECURSIVELY
# =======================================================

if backup_dir.exists():
    shutil.rmtree(backup_dir)
    print("\nRemoved entire directory tree using shutil.rmtree():", backup_dir)


# =======================================================
# 6. CREATE ZIP ARCHIVE
# =======================================================

archive_name = "folder_archive"
shutil.make_archive(archive_name, "zip", root_dir=moved_dir)
print("\nZIP archive created:", archive_name + ".zip")


# =======================================================
# 7. UNPACK ZIP ARCHIVE
# =======================================================

extract_dir = Path("unzipped_folder")
shutil.unpack_archive(archive_name + ".zip", extract_dir)
print("ZIP archive extracted to:", extract_dir)


# =======================================================
# 8. DISK USAGE INFORMATION
# =======================================================

total, used, free = shutil.disk_usage("/")
print("\nDisk usage:")
print("Total space:", total // (2**30), "GB")
print("Free space:", free // (2**30), "GB")


# =======================================================
# FINISH
# =======================================================

print("\nFinal directory contents:")
for item in os.listdir("."):
    print(" -", item)

print("\nShutil demo complete.")
