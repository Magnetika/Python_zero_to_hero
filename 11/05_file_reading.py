from os import chdir, path

# ------------------------------------------------------------
# Set working directory to the directory where this script is
# ------------------------------------------------------------
chdir(path.dirname(__file__))

# ------------------------------------------------------------
# Read an entire file safely using try–except
# ------------------------------------------------------------
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("Full content of copied_example.txt:\n")
        print(content)
except FileNotFoundError:
    print("ERROR: copied_example.txt not found.")
    content = ""


# ------------------------------------------------------------
# Read file line-by-line (safer & memory efficient)
# ------------------------------------------------------------
print("\nReading file line-by-line:")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())   # strip removes \n
except FileNotFoundError:
    print("ERROR: copied_example.txt not found.")


# ------------------------------------------------------------
# Read all lines into a list using readlines()
# ------------------------------------------------------------
print("\nReading file using readlines():")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(lines)  # prints a Python list of lines
except FileNotFoundError:
    print("ERROR: copied_example.txt not found.")
    lines = []


# ------------------------------------------------------------
# Print file contents with line numbers
# ------------------------------------------------------------
print("\nFile contents with line numbers:")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}: {line.strip()}")
except FileNotFoundError:
    pass


# ------------------------------------------------------------
# Copy content from one file to another
# ------------------------------------------------------------
print("\nCopying file to new file: output_copy.txt")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as src, \
         open("output_copy.txt", "w", encoding="utf-8") as dest:

        for line in src:
            dest.write(line)

    print("Copy completed successfully.")
except FileNotFoundError:
    print("ERROR: copied_example.txt not found, cannot copy.")


# ------------------------------------------------------------
# Filter lines - print only lines containing a keyword
# ------------------------------------------------------------
print("\nFiltering lines containing the word 'INFO':")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "INFO" in line:
                print(line.strip())
except FileNotFoundError:
    pass


# ------------------------------------------------------------
# Read first N characters of a file
# ------------------------------------------------------------
print("\nReading the first 20 characters:")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        first_20 = f.read(20)
        print(first_20)
except FileNotFoundError:
    pass


print("\nFile reading & processing demo finished successfully.")
