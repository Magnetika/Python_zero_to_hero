# 🎯 Lesson Objective:
# Learn how to use the selection pattern to find the first element in a sequence
# that meets a specific condition, and understand how to handle cases when no such element exists.

# ----------------------------------------------------------
# 🧩 1. Find a specific value in a list using selection logic
# ----------------------------------------------------------
def get_index(values, element):
    """Returns the index of the first matching element, or -1 if not found."""
    for i in range(len(values)):
        if values[i] == element:
            return i  # early termination
    return -1  # not found

val = [10, 20, 30, 40, 50]
print("📍 Searching for a specific value:")
print("Index of 30:", get_index(val, 30))
print("Index of 100 (not found):", get_index(val, 100))
print()

# ----------------------------------------------------------
# 🧩 2. Modify the code to find the first even or odd number
# ----------------------------------------------------------
def find_first_even(values):
    """Finds the first even number in the list."""
    for n in values:
        if n % 2 == 0:
            return n
    return None

def find_first_odd(values):
    """Finds the first odd number in the list."""
    for n in values:
        if n % 2 != 0:
            return n
    return None

numbers = [3, 7, 1, 6, 9]
print("📍 Finding first even/odd values:")
print("First even number:", find_first_even(numbers))
print("First odd number:", find_first_odd(numbers))
print()

# ----------------------------------------------------------
# 🧩 3. Track both value and index of the selected element
# ----------------------------------------------------------
def find_first_greater_than(values, limit):
    """Finds the first number greater than 'limit' and its index."""
    for i in range(len(values)):
        if values[i] > limit:
            return values[i], i
    return None, -1

data = [4, 9, 7, 2, 5]
value, index = find_first_greater_than(data, 8)
print("📍 Tracking value and index:")
if index != -1:
    print(f"First number greater than 8: {value} at index {index}")
else:
    print("No matching element found.")
print()

# ----------------------------------------------------------
# 🧩 4. Handling “not found” cases
# ----------------------------------------------------------
index = get_index(val, 999)
if index == -1:
    print("📍 Not found case:")
    print("Element not found in the list.")
else:
    print(f"Element found at index {index}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - The selection pattern finds the first element that matches a condition.
# - Uses early termination (break/return) when found.
# - Initialize result as None or -1 for clarity.
# - Can be applied to values, indices, or both.
# - Always handle the “not found” case to avoid runtime errors.
# - Similar built-ins: .index(), next() with generators.
