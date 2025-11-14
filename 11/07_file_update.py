"""
Full file-handling practice using the file 'copied_example.txt'.
This script demonstrates:
- overwriting files
- appending content
- reading full files / reading line-by-line
- updating lines
- removing lines
- replacing words
- safe rewriting using temporary files
- counting lines/words/characters
All examples use ONLY the file: copied_example.txt
"""

import os

# ---------------------------------------------------------
# Helper: Ensure the file exists before we begin
# ---------------------------------------------------------
if not os.path.exists("copied_example.txt"):
    with open("copied_example.txt", "w", encoding="utf-8") as f:
        f.write("Line 1: original content\n")
        f.write("Line 2: more content\n")
        f.write("Line 3: keyword=test\n")
print("Initial file ready.\n")


# =========================================================
# 1. OVERWRITE THE FILE COMPLETELY
# =========================================================
print("=== 1. OVERWRITE FILE ===")

with open("copied_example.txt", "w", encoding="utf-8") as f:
    f.write("This is new overwritten content.\n")
    f.write("Everything before this is deleted.\n")

print("File overwritten.\n")

# TASK:
# Overwrite the file with your own custom text (3–5 lines).


# =========================================================
# 2. APPEND NEW DATA TO THE FILE
# =========================================================
print("=== 2. APPEND TO FILE ===")

with open("copied_example.txt", "a", encoding="utf-8") as f:
    f.write("Appended line A.\n")
    f.write("Appended line B.\n")

print("Content appended.\n")

# TASK:
# Add your name and the current date as new appended lines.


# =========================================================
# 3. READ THE FULL CONTENT
# =========================================================
print("=== 3. READ ENTIRE FILE ===")

with open("copied_example.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("Full content:\n", content, "\n")

# TASK:
# Read and print ONLY the first 20 characters of the file.


# =========================================================
# 4. READ THE FILE LINE BY LINE
# =========================================================
print("=== 4. READ LINE BY LINE ===")

with open("copied_example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("Line →", line.strip())

print()

# TASK:
# Print each line with a line number (1., 2., 3., ...).


# =========================================================
# 5. REPLACE WORDS IN THE FILE AND REWRITE
# =========================================================
print("=== 5. REPLACE WORD IN FILE ===")

with open("copied_example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

updated_lines = [line.replace("Appended", "Replaced") for line in lines]

with open("copied_example.txt", "w", encoding="utf-8") as f:
    f.writelines(updated_lines)

print("Word replacement done.\n")

# TASK:
# Replace every occurrence of "Replaced" with "UPDATED".


# =========================================================
# 6. REMOVE LINES MATCHING A CONDITION
# =========================================================
print("=== 6. REMOVE LINES CONTAINING A WORD ===")

with open("copied_example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("copied_example.txt", "w", encoding="utf-8") as f:
    for line in lines:
        if "delete" not in line.lower():    # remove lines containing "delete"
            f.write(line)

print("Conditional removal complete.\n")

# TASK:
# Remove all lines that contain a number (use any digit test like '1' in line).


# =========================================================
# 7. SAFE UPDATE USING A TEMPORARY FILE
# =========================================================
print("=== 7. SAFE UPDATE WITH TEMP FILE ===")

with open("copied_example.txt", "r", encoding="utf-8") as src, \
     open("temp_file.txt", "w", encoding="utf-8") as temp:

    for line in src:
        temp.write(line.replace("Replaced", "SAFE-UPDATED"))

os.replace("temp_file.txt", "copied_example.txt")

print("Safe update complete.\n")

# TASK:
# Try replacing any custom keyword using the safe temp-file technique.


# =========================================================
# 8. COUNT LINES, WORDS, CHARACTERS
# =========================================================
print("=== 8. COUNTING STATISTICS ===")

with open("copied_example.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Lines     →", len(lines))
print("Words     →", len(words))
print("Characters →", characters, "\n")

# TASK:
# Print which line is the longest (by character count).


# =========================================================
# 9. PRINT FILE IN REVERSE ORDER
# =========================================================
print("=== 9. PRINT REVERSED LINES ===")

with open("copied_example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in reversed(lines):
    print(line.strip())

print()

# TASK:
# Save the reversed output into a new file: reversed_output.txt


# =========================================================
# 10. READ ONLY FIRST N LINES
# =========================================================
print("=== 10. FIRST 3 LINES ===")

with open("copied_example.txt", "r", encoding="utf-8") as f:
    for i in range(3):
        print(f.readline().strip())

print()

# TASK:
# Read and print only the LAST 2 lines.
