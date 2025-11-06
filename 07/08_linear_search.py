# 🎯 Lesson Objective:
# Learn how to implement the linear search algorithm to find a specific element in a list,
# understand how it works, and compare it with Python’s built-in search operations.

# ----------------------------------------------------------
# 🧩 1. Implement a basic linear search manually
# ----------------------------------------------------------
def linear_search(values, element):
    """Returns the index of the element if found, otherwise -1."""
    for i in range(len(values)):
        if values[i] == element:
            return i  # stop searching once found
    return -1  # not found

val = [10, 20, 30, 40, 50]
print("📍 Manual Linear Search:")
print("Index of 30:", linear_search(val, 30))  # Output: 2
print("Index of 60:", linear_search(val, 60))  # Output: -1
print()

# ----------------------------------------------------------
# 🧩 2. Modify to return both value and index
# ----------------------------------------------------------
def linear_search_with_value(values, element):
    """Returns both the value and its index if found, otherwise (None, -1)."""
    for i in range(len(values)):
        if values[i] == element:
            return values[i], i
    return None, -1

value, index = linear_search_with_value(val, 40)
print("📍 Returning both value and index:")
if index != -1:
    print(f"Found value {value} at index {index}")
else:
    print("Element not found.")
print()

# ----------------------------------------------------------
# 🧩 3. Use the 'in' operator and compare results
# ----------------------------------------------------------
target = 30
print("📍 Using Python's built-in search:")
if target in val:
    print(f"Found {target} using 'in' operator!")
else:
    print(f"{target} not found.")

# Safe version of index() using try-except
try:
    print("Index found using .index():", val.index(target))
except ValueError:
    print("Element not found using .index().")
print()

# ----------------------------------------------------------
# 🧩 4. Handle “not found” safely without errors
# ----------------------------------------------------------
target = 60
print("📍 Safe search (handling missing elements):")
try:
    print("Index found using .index():", val.index(target))
except ValueError:
    print(f"{target} not found safely (no crash).")
print()

# ----------------------------------------------------------
# 🧩 5. Extra – Linear Search in nested lists (optional)
# ----------------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

def linear_search_2d(matrix, target):
    """Searches for an element in a 2D list and returns (row, col) if found."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i, j)
    return None

print("📍 Linear search in a 2D list:")
result = linear_search_2d(matrix, 5)
if result:
    print(f"Element found at row {result[0]}, column {result[1]}")
else:
    print("Element not found.")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Linear search checks elements sequentially (O(n) time)
# - Works on unsorted lists
# - Stops immediately when a match is found (efficient early termination)
# - Return -1 or None when not found to avoid errors
# - Built-in alternatives:
#     - 'in' → True/False check
#     - '.index()' → returns index or raises ValueError if not found
# - Simple, but not efficient for very large datasets
