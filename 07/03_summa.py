# 🎯 Lesson Objective:
# Learn how to use the summation pattern to calculate the total of values in a list or sequence,
# and understand how it relates to loops and accumulation logic.

# ----------------------------------------------------------
# 🧩 1. Implement the summation pattern manually with a list
# ----------------------------------------------------------
def summa(values):
    """Manual implementation of the summation pattern."""
    sum_value = 0  # accumulator
    for i in values:
        sum_value += i  # accumulate values
    return sum_value

val = [10, 20, 30, 40, 50]
print("📍 Manual summation pattern:")
print("Sum of list:", summa(val))  # Output: 150
print()

# ----------------------------------------------------------
# 🧩 2. Use sum() to verify your result
# ----------------------------------------------------------
print("📍 Using built-in sum() for comparison:")
print("Built-in sum result:", sum(val))
print()

# ----------------------------------------------------------
# 🧩 3. Add a condition (e.g., sum only positive values)
# ----------------------------------------------------------
numbers = [5, -2, 8, -1, 4]
positive_sum = 0
for n in numbers:
    if n > 0:
        positive_sum += n

print("📍 Conditional summation (only positives):")
print("Sum of positive numbers:", positive_sum)
print("Built-in check:", sum([n for n in numbers if n > 0]))
print()

# ----------------------------------------------------------
# 🧩 4. Perform summation over a 2D list (matrix)
# ----------------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

total = 0
for row in matrix:
    for num in row:
        total += num

print("📍 Summation over a 2D list (matrix):")
print("Matrix sum:", total)
print("Built-in check with nested sum:", sum(sum(row) for row in matrix))
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - The summation (accumulation) pattern uses a variable to store a running total.
# - Initialize the accumulator before the loop (e.g., total = 0)
# - Update it inside the loop (total += n)
# - The built-in sum() automates this process internally.
# - You can add conditions to filter what gets added.
# - Nested loops allow summation across multi-dimensional data (e.g., matrices).
