# 🎯 Lesson Objective:
# Learn how to use the counting pattern to determine how many elements
# in a list or sequence meet a specific condition.

# ----------------------------------------------------------
# 🧩 1. Count all elements in a list manually and with len()
# ----------------------------------------------------------
numbers = [3, 7, 2, 8, 4]
count = 0
for n in numbers:
    count += 1

print("📍 Counting all elements manually:")
print("Number of elements:", count)
print("Using len():", len(numbers))
print()

# ----------------------------------------------------------
# 🧩 2. Count only elements that satisfy a condition
# ----------------------------------------------------------
def count_value(values, search):
    """Counts how many times a given value appears in the list."""
    counter = 0
    for i in values:
        if i == search:
            counter += 1
    return counter

val = [10, 20, 30, 10, 10, 40, 50]
print("📍 Conditional counting (specific value):")
print("Occurrences of 10:", count_value(val, 10))  # Output: 3
print("Occurrences of 20:", count_value(val, 20))  # Output: 1
print("Occurrences of 60:", count_value(val, 60))  # Output: 0
print()

# ----------------------------------------------------------
# 🧩 3. Apply counting to a 2D structure (matrix)
# ----------------------------------------------------------
matrix = [
    [1, 0, 1],
    [1, 1, 0]
]

count_ones = 0
for row in matrix:
    for val in row:
        if val == 1:
            count_ones += 1

print("📍 Counting in a 2D matrix:")
print("Number of ones:", count_ones)
print()

# ----------------------------------------------------------
# 🧩 4. Rewrite the loop using a generator and sum()
# ----------------------------------------------------------
numbers = [3, 7, 2, 8, 4]
even_count = sum(1 for n in numbers if n % 2 == 0)

print("📍 Counting with a generator and sum():")
print("Even numbers:", even_count)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Counting pattern: count += 1 whenever a condition is true
# - Works for any iterable (list, tuple, string, matrix, etc.)
# - Use len() for total count, or manual loops for filtered counts
# - Generator + sum() provides a clean, Pythonic one-liner
# - Algorithm steps:
#   1. Initialize a counter variable (count = 0)
#   2. Iterate through the collection
#   3. Check condition
#   4. Increment counter if true
#   5. Return or print the result
