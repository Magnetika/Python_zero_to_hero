# 🎯 Lesson Objective:
# Learn how to find the minimum value in a list or sequence using iteration,
# and understand how this logic forms the basis for simple sorting algorithms.

# ----------------------------------------------------------
# 🧩 1. Write a function that finds the smallest number in a list
# ----------------------------------------------------------
def get_minimum(values):
    """Finds the smallest value in a list using manual iteration."""
    min_value = values[0]
    for i in range(1, len(values)):
        if values[i] < min_value:
            min_value = values[i]
    return min_value

val = [10, 20, 30, 40, 50]
print("📍 Manual minimum search:")
print("Minimum value:", get_minimum(val))
print()

# ----------------------------------------------------------
# 🧩 2. Compare the result with Python’s built-in min()
# ----------------------------------------------------------
print("📍 Comparison with built-in min():")
print("Manual result:", get_minimum(val))
print("Built-in min():", min(val))
print()

# ----------------------------------------------------------
# 🧩 3. Implement minimum search for a 2D list (matrix)
# ----------------------------------------------------------
matrix = [
    [4, 1, 9],
    [7, 5, 2],
    [8, 3, 6]
]

def get_matrix_minimum(matrix):
    """Finds the smallest number in a 2D list."""
    min_value = matrix[0][0]
    for row in matrix:
        for value in row:
            if value < min_value:
                min_value = value
    return min_value

print("📍 Minimum search in a 2D list (matrix):")
print("Matrix minimum:", get_matrix_minimum(matrix))
print()

# ----------------------------------------------------------
# 🧩 4. Track the index of the minimum element as well
# ----------------------------------------------------------
def get_minimum_with_index(values):
    """Finds the smallest value and its index."""
    min_value = values[0]
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < min_value:
            min_value = values[i]
            min_index = i
    return min_value, min_index

nums = [12, 4, 56, 7, -3, 9]
min_val, min_idx = get_minimum_with_index(nums)
print("📍 Tracking index of minimum value:")
print(f"Minimum value: {min_val} at index {min_idx}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Manual minimum search helps understand algorithmic logic
# - Built-in min() is a shorthand version of the same idea
# - For 2D lists, nested loops are used to access all elements
# - Tracking indices is useful for sorting and searching algorithms
# - Algorithm steps:
#   1. Initialize a reference (current minimum)
#   2. Iterate through elements
#   3. Compare and update
#   4. Return the smallest value (and optionally its position)
