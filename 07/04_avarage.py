# 🎯 Lesson Objective:
# Learn how to calculate the average (mean) of numeric data using loops and built-in functions,
# and understand the relationship between total sum and element count.

# ----------------------------------------------------------
# 🧩 1. Write your own loop to calculate an average
# ----------------------------------------------------------
def summa(values):
    """Manual summation function (accumulation pattern)."""
    sum_value = 0
    for i in values:
        sum_value += i
    return sum_value

def average(values):
    """Calculates average using custom summation."""
    if values:
        return summa(values) / len(values)
    else:
        return 0  # avoid division by zero

val = [10, 20, 30, 40, 50]
print("📍 Manual average calculation:")
print("Average of list:", average(val))  # Output: 30.0
print()

# ----------------------------------------------------------
# 🧩 2. Use sum() and len() for the same purpose
# ----------------------------------------------------------
numbers = [2, 4, 6, 8, 10]
average_builtin = sum(numbers) / len(numbers)
print("📍 Using built-in functions:")
print("Average (built-in):", average_builtin)
print()

# ----------------------------------------------------------
# 🧩 3. Handle empty input safely
# ----------------------------------------------------------
empty_list = []
print("📍 Handling empty list safely:")
if empty_list:
    avg = sum(empty_list) / len(empty_list)
else:
    avg = 0
print("Average of empty list:", avg)
print()

# ----------------------------------------------------------
# 🧩 4. Compute conditional averages (e.g., only positives)
# ----------------------------------------------------------
numbers = [3, -5, 7, -2, 9]
positive_numbers = [n for n in numbers if n > 0]

if positive_numbers:
    avg_positive = sum(positive_numbers) / len(positive_numbers)
else:
    avg_positive = 0

print("📍 Conditional average (only positives):")
print("Average of positive numbers:", avg_positive)
print()

# ----------------------------------------------------------
# 🧩 5. Compute average for 2D data (matrix)
# ----------------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

total = 0
count = 0
for row in matrix:
    for num in row:
        total += num
        count += 1

matrix_avg = total / count
print("📍 Average for a 2D list (matrix):")
print("Matrix average:", matrix_avg)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Average = Total Sum / Count of elements
# - Combine accumulation and iteration
# - Use built-ins: sum() + len() for simplicity
# - Handle empty input to avoid ZeroDivisionError
# - Conditional averages filter which elements are counted
# - Extendable to nested data (e.g., 2D lists, matrices)
