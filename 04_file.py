from pathlib import Path

# -------------------------------------------------------
# Set working directory to the folder of this script
# -------------------------------------------------------
base_dir = Path(__file__).parent
print("Current working folder:", base_dir)

# -------------------------------------------------------
# 1. CREATE A TEST FILE AND WRITE CONTENT
# -------------------------------------------------------
file_path = base_dir / "example.txt"

# Write (overwrite) content to a file
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Hello from Python file handling!\n")
    f.write("This is the second line.\n")

print("File created and written:", file_path)


# -------------------------------------------------------
# 2. APPEND NEW TEXT TO THE FILE
# -------------------------------------------------------
with open(file_path, "a", encoding="utf-8") as f:
    f.write("Appended line at the end.\n")

print("Content appended to the file.\n")


# -------------------------------------------------------
# 3. READ THE ENTIRE FILE
# -------------------------------------------------------
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Full file content:")
print(content)


# -------------------------------------------------------
# 4. READ FILE LINE BY LINE
# -------------------------------------------------------
print("Reading file line-by-line:")
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        print("LINE:", line.strip())


# -------------------------------------------------------
# 5. READ LINES INTO A LIST
# -------------------------------------------------------
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("\nList of lines:", lines)


# -------------------------------------------------------
# 6. CHECK IF FILE EXISTS BEFORE OPENING
# -------------------------------------------------------
if file_path.exists():
    print("\nFile exists:", file_path.name)
else:
    print("\nFile does not exist!")


# -------------------------------------------------------
# 7. ERROR HANDLING WITH try–except
# -------------------------------------------------------
try:
    with open("missing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\nERROR: missing_file.txt not found.")


# -------------------------------------------------------
# 8. COPY CONTENT FROM ONE FILE TO ANOTHER
# -------------------------------------------------------
copy_path = base_dir / "copy_of_example.txt"

with open(file_path, "r", encoding="utf-8") as src, open(copy_path, "w", encoding="utf-8") as dst:
    dst.write(src.read())

print("\nFile copied to:", copy_path)


# -------------------------------------------------------
# 9. READ ONLY FIRST N CHARACTERS
# -------------------------------------------------------
with open(file_path, "r", encoding="utf-8") as f:
    first_10 = f.read(10)

print("\nFirst 10 characters:", repr(first_10))


# -------------------------------------------------------
# 10. USE tell() AND seek() POSITIONING
# -------------------------------------------------------
with open(file_path, "r", encoding="utf-8") as f:
    print("\nCurrent cursor position:", f.tell())
    f.seek(0)
    print("After seek(0):", f.tell())
    print("Reading first 5 chars:", f.read(5))


print("\nFile handling demo finished successfully.")
