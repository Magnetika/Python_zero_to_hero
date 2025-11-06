# 🎯 Lesson Objective:
# Learn how to find the maximum value in a list or sequence using iteration,
# and understand how this logic connects to algorithms such as sorting or searching.

# ----------------------------------------------------------
# 🧩 1. Write a function that finds the largest number in a list
# ----------------------------------------------------------
def get_maximum(values):
    """Finds the largest value in a list manually."""
    max_value = values[0]
    for i in range(1, len(values)):
        if values[i] > max_value:
            max_value = values[i]
    return max_value

val = [10, 20, 30, 40, 50]
print("📍 Manual maximum search:")
print("Maximum value:", get_maximum(val))
print()

# ----------------------------------------------------------
# 🧩 2. Compare the result with Python’s built-in max()
# ----------------------------------------------------------
print("📍 Comparison with built-in max():")
print("Manual result:", get_maximum(val))
print("Built-in max():", max(val))
print()

# ----------------------------------------------------------
# 🧩 3. Implement maximum search for a 2D list (matrix)
# ----------------------------------------------------------
matrix = [
    [4, 1, 9],
    [7, 5, 2],
    [8, 3, 6]
]

def get_matrix_maximum(matrix):
    """Finds the largest value in a 2D list."""
    max_value = matrix[0][0]
    for row in matrix:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value

print("📍 Maximum search in a 2D list (matrix):")
print("Matrix maximum:", get_matrix_maximum(matrix))
print()

# ----------------------------------------------------------
# 🧩 4. Track the index of the maximum element as well
# ----------------------------------------------------------
def get_maximum_with_index(values):
    """Finds the largest value and its index."""
    max_value = values[0]
    max_index = 0
    for i in range(1, len(values)):
        if values[i] > max_value:
            max_value = values[i]
            max_index = i
    return max_value, max_index

nums = [12, 4, 56, 7, -3, 9]
max_val, max_idx = get_maximum_with_index(nums)
print("📍 Tracking index of maximum value:")
print(f"Maximum value: {max_val} at index {max_idx}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Manual maximum search teaches comparison logic used in sorting algorithms
# - Built-in max() does the same internally, but faster
# - For 2D structures, nested loops are needed
# - Tracking the index is useful for later algorithms (e.g., selection sort)
# - Algorithm steps:
#   1. Initialize a reference (current maximum)
#   2. Iterate through all elements
#   3. Compare and update when a larger element is found
#   4. Return the final maximum (and optionally its position)
