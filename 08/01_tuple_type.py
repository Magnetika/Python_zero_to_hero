# 🎯 Lesson Objective:
# Understand what tuples are, how to create and use them, and why they are immutable.
# Learn the main differences between tuples and lists.

# ----------------------------------------------------------
# 🧩 1. Creating tuples in different ways
# ----------------------------------------------------------
numbers = (1, 2, 3)
print("📍 Tuple creation with parentheses:", numbers)
print("Type:", type(numbers))

coordinates = 10, 20  # parentheses optional
print("Tuple without parentheses:", coordinates)

single = (5,)  # note the comma!
print("Single-element tuple:", single)
print("Type of single:", type(single))
print()

# ----------------------------------------------------------
# 🧩 2. Access and slice tuple elements
# ----------------------------------------------------------
colors = ("red", "green", "blue", "yellow")
print("📍 Accessing tuple elements:")
print("First color:", colors[0])
print("Last color:", colors[-1])
print("Slice [1:3]:", colors[1:3])
print()

# ----------------------------------------------------------
# 🧩 3. Try to modify a tuple (observe the error)
# ----------------------------------------------------------
data = (1, 2, 3)
print("📍 Tuple immutability:")
# data[0] = 10  # ❌ Uncommenting this will cause TypeError
print("Tuples cannot be modified directly.")
print()

# ----------------------------------------------------------
# 🧩 4. Store mutable elements inside a tuple
# ----------------------------------------------------------
mixed = (1, [2, 3])
print("Before modification:", mixed)
mixed[1][0] = 99  # allowed, because the list inside is mutable
print("After modifying inner list:", mixed)
print()

# ----------------------------------------------------------
# 🧩 5. Tuple operations
# ----------------------------------------------------------
a = (1, 2)
b = (3, 4)
print("📍 Tuple operations:")
print("Concatenation:", a + b)
print("Repetition:", a * 2)
print("Membership test (2 in a):", 2 in a)
print()

# ----------------------------------------------------------
# 🧩 6. Using tuple methods
# ----------------------------------------------------------
yearly_salary = (50000, 60000, 70000, 80000, 90000)
print("📍 Tuple methods:")
print("Length:", len(yearly_salary))
print("Count of 70000:", yearly_salary.count(70000))
print("Index of 80000:", yearly_salary.index(80000))
print()

# ----------------------------------------------------------
# 🧩 7. Adding a new element via concatenation (since immutable)
# ----------------------------------------------------------
new_salary = (550000,)  # must include comma
yearly_salary += new_salary
print("Updated tuple after concatenation:", yearly_salary)
print()

# ----------------------------------------------------------
# 🧩 8. Returning and unpacking multiple values from a function
# ----------------------------------------------------------
def min_max(values):
    """Returns the smallest and largest values as a tuple."""
    return min(values), max(values)

result = min_max([3, 7, 2, 9])
print("📍 Function returning a tuple:", result)
low, high = result  # tuple unpacking
print(f"Unpacked → Min: {low}, Max: {high}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Tuples are ordered and immutable collections.
# - Defined with parentheses (optional for multiple items).
# - Single-element tuples require a trailing comma.
# - Support indexing, slicing, +, *, and membership tests.
# - Immutability → elements cannot be added, removed, or changed.
# - Tuples can contain mutable objects (e.g., lists).
# - Common use cases:
#     * Returning multiple values from functions
#     * Fixed data structures (e.g., coordinates, dates, records)
#     * Dictionary keys (since they are hashable)
