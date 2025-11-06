# 🎯 Lesson Objective:
# Learn how to implement the decision pattern to determine
# whether at least one element in a collection satisfies a given condition.

# ----------------------------------------------------------
# 🧩 1. Write a decision algorithm to check if a list contains a specific value
# ----------------------------------------------------------
def is_contains(values, search):
    """Checks if the given element exists in the list."""
    for i in values:
        if i == search:
            return True
    return False

val = [10, 20, 30, 40, 50]
print("📍 Manual decision pattern:")
print("List contains 30:", is_contains(val, 30))   # True
print("List contains 60:", is_contains(val, 60))   # False
print()

# ----------------------------------------------------------
# 🧩 2. Decision algorithm to check if list contains a negative number
# ----------------------------------------------------------
numbers = [3, 7, -2, 9, 5]
has_negative = False

for n in numbers:
    if n < 0:
        has_negative = True
        break

print("📍 Checking for negative numbers:")
print("Contains negative number:", has_negative)
print()

# ----------------------------------------------------------
# 🧩 3. Use any() to simplify the same logic
# ----------------------------------------------------------
numbers = [3, 7, -2, 9, 5]
has_negative = any(n < 0 for n in numbers)

print("📍 Using built-in any() function:")
print("Contains negative number:", has_negative)
print()

# ----------------------------------------------------------
# 🧩 4. Extend the algorithm to nested lists (matrices)
# ----------------------------------------------------------
matrix = [
    [1, 3, 5],
    [7, 8, 9]
]

found_even = False
for row in matrix:
    for val in row:
        if val % 2 == 0:
            found_even = True
            break
    if found_even:
        break

print("📍 Decision pattern in 2D list (matrix):")
print("Matrix contains even number:", found_even)
print()

# Same logic with any() + nested generator:
found_even_any = any(val % 2 == 0 for row in matrix for val in row)
print("📍 Simplified with any():", found_even_any)
print()

# ----------------------------------------------------------
# 🧩 5. Add handling for empty lists
# ----------------------------------------------------------
empty_list = []
contains_value = any(x > 0 for x in empty_list)
print("📍 Handling empty list:")
print("Contains positive number:", contains_value)  # False
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Decision pattern checks if at least one element meets a condition
# - Common structure:
#     flag = False
#     for item in collection:
#         if condition:
#             flag = True
#             break
# - any() automates this logic elegantly
# - Works with nested structures and empty lists
# - Great for conditions like "exists?" or "contains?"
