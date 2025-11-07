# 🎯 Lesson Objective:
# Learn how to iterate through the elements of a tuple using for loops,
# and understand how tuple iteration works in both simple and nested structures.

# ----------------------------------------------------------
# 🧩 1. Basic iteration
# ----------------------------------------------------------
yearly_salary = (50000, 60000, 70000, 80000, 90000)
print("📍 Basic tuple iteration:")
for salary in yearly_salary:
    print(salary)
print()

# ----------------------------------------------------------
# 🧩 2. Iterating with indexes (range + len)
# ----------------------------------------------------------
print("📍 Iterating with indexes using range(len()):")
for i in range(len(yearly_salary)):
    print(f"Index {i}: value = {yearly_salary[i]}")
print()

# ----------------------------------------------------------
# 🧩 3. Using enumerate() for cleaner iteration
# ----------------------------------------------------------
print("📍 Using enumerate() for index + value:")
for i, v in enumerate(yearly_salary):
    print(f"Index {i}: value = {v}")
print()

# ----------------------------------------------------------
# 🧩 4. Iterating over nested tuples with unpacking
# ----------------------------------------------------------
employees = (
    ("Alice", 25, "Developer"),
    ("Bob", 30, "Designer"),
    ("Eve", 22, "Tester")
)

print("📍 Iterating over nested tuples (unpacking):")
for name, age, role in employees:
    print(f"{name} is {age} years old and works as a {role}.")
print()

# ----------------------------------------------------------
# 🧩 5. Iterating over mixed data types
# ----------------------------------------------------------
info = ("Python", 3.12, True)
print("📍 Iterating over mixed-type tuple:")
for item in info:
    print(type(item), "→", item)
print()

# ----------------------------------------------------------
# 🧩 6. Combining iteration with a condition
# ----------------------------------------------------------
scores = (55, 80, 92, 47, 100)
print("📍 Conditional iteration (filtering passing scores):")
for score in scores:
    if score >= 60:
        print("Pass:", score)
    else:
        print("Fail:", score)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Tuples are iterable just like lists and strings.
# - Use `for element in tuple` for direct iteration.
# - Use `enumerate()` to get both index and value cleanly.
# - Tuple unpacking makes nested iteration elegant and readable.
# - Tuples can store heterogeneous data — no type restriction.
# - You can apply conditional logic inside loops for filtering or selection.
