from os import chdir, path

# -------------------------------------------------------------------
# Set working directory to the folder where this script is located
# -------------------------------------------------------------------
chdir(path.dirname(__file__))

# -------------------------------------------------------------------
# Basic Example: Read a fixed number of characters (your original code)
# -------------------------------------------------------------------
print("=== Reading first 4 characters ===")
with open("copied_example.txt", "r", encoding="utf-8") as file:
    content = file.read(4)
    print(content)


# -------------------------------------------------------------------
# Example 1 – Reading the entire file
# -------------------------------------------------------------------
print("\n=== Full file content ===")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    print("ERROR: File not found.")


# -------------------------------------------------------------------
# Example 2 – Reading a file line by line
# -------------------------------------------------------------------
print("\n=== Reading line by line ===")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    pass


# -------------------------------------------------------------------
# Example 3 – Reading all lines into a list
# -------------------------------------------------------------------
print("\n=== readlines() example ===")
try:
    with open("copied_example.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("Number of lines:", len(lines))
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    pass


# -------------------------------------------------------------------
# Example 4 – Reading only the first 20 characters
# -------------------------------------------------------------------
print("\n=== First 20 characters ===")
with open("copied_example.txt", "r", encoding="utf-8") as f:
    print(f.read(20))


# -------------------------------------------------------------------
# Example 5 – Counting words and lines
# -------------------------------------------------------------------
print("\n=== Line and word count ===")
with open("copied_example.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print("Lines:", len(text.splitlines()))
    print("Words:", len(text.split()))


# -------------------------------------------------------------------
# Example 6 – Numbering lines using enumerate()
# -------------------------------------------------------------------
print("\n=== Numbered lines ===")
with open("copied_example.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")


# -------------------------------------------------------------------
# Example 7 – Filter lines containing a keyword
# -------------------------------------------------------------------
print("\n=== Filter lines containing 'INFO' ===")
with open("copied_example.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "INFO" in line:
            print(line.strip())


# -------------------------------------------------------------------
# Example 8 – Skipping empty lines
# -------------------------------------------------------------------
print("\n=== Skip empty lines ===")
with open("copied_example.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() != "":
            print(line.strip())


# -------------------------------------------------------------------
# Example 9 – Manual CSV-style parsing
# -------------------------------------------------------------------
print("\n=== CSV-style reading ===")
try:
    with open("grades.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, grade = line.strip().split(",")
            print(f"{name} scored {grade}")
except FileNotFoundError:
    print("grades.txt not found (this example requires that file).")


# -------------------------------------------------------------------
# Example 10 – Reading only the first N lines
# -------------------------------------------------------------------
print("\n=== First 3 lines ===")
with open("copied_example.txt", "r", encoding="utf-8") as f:
    for _ in range(3):
        print(f.readline().strip())


# -------------------------------------------------------------------
# Example 11 – Print file in reverse order
# -------------------------------------------------------------------
print("\n=== Reversed lines ===")
with open("copied_example.txt", "r", encoding="utf-8") as f:
    for line in reversed(f.readlines()):
        print(line.strip())


# -------------------------------------------------------------------
# Example 12 – Handling missing files
# -------------------------------------------------------------------
print("\n=== Safe reading missing file ===")
try:
    with open("missing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File missing_file.txt does not exist.")


# -------------------------------------------------------------------
# Example 13 – Reading with UTF-8 encoding
# -------------------------------------------------------------------
print("\n=== UTF-8 file reading ===")
try:
    with open("hungarian.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("hungarian.txt missing – create it to test UTF-8 reading.")


# -------------------------------------------------------------------
# Example 14 – Chunk reading (large files)
# -------------------------------------------------------------------
print("\n=== Reading in chunks (32 bytes) ===")
with open("copied_example.txt", "r", encoding="utf-8") as f:
    while True:
        chunk = f.read(32)
        if not chunk:
            break
        print(chunk, end="")


# -------------------------------------------------------------------
# Example 15 – Processing numeric data in a file
# -------------------------------------------------------------------
print("\n\n=== Reading sales.txt and calculating average ===")
try:
    total = 0
    count = 0
    with open("sales.txt", "r", encoding="utf-8") as f:
        for line in f:
            total += float(line.strip())
            count += 1
    print("Average sale:", total / count)
except FileNotFoundError:
    print("sales.txt missing – create it to test numeric processing.")
except ZeroDivisionError:
    print("sales.txt is empty.")
