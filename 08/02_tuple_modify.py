# 🎯 Lesson Objective:
# Understand the immutability of tuples in Python,
# explore what “mutable elements inside an immutable object” means,
# and learn how tuples can still contain changeable data.

# ----------------------------------------------------------
# 🧩 1. Tuples are immutable
# ----------------------------------------------------------
t = (1, 2, 3)
print("📍 Tuples are immutable:")
print("Original tuple:", t)
# t[0] = 99  # ❌ TypeError: 'tuple' object does not support item assignment
print("You cannot modify or reassign tuple elements directly.")
print()

# ----------------------------------------------------------
# 🧩 2. Tuples can contain mutable elements
# ----------------------------------------------------------
t = (1, [2, 3], 4)
print("📍 Tuple containing a mutable element:")
print("Before modifying the list inside tuple:", t)
t[1][0] = 99  # modify list inside tuple
print("After modification:", t)
print("Tuple structure unchanged (still 3 items).")
print()

# ----------------------------------------------------------
# 🧩 3. Why this happens
# ----------------------------------------------------------
inner_list = [1, 2]
t = (inner_list, 3)
print("📍 Tuple stores references, not copies:")
print("Before modifying list:", t)
inner_list.append(99)
print("After modifying the list:", t)
print("Tuple didn't change structurally — list reference remained the same.")
print()

# ----------------------------------------------------------
# 🧩 4. Converting tuple -> list -> tuple (your approach)
# ----------------------------------------------------------
yearly_salary = (50000, 60000, 70000, 80000, 90000)
print("📍 Converting tuple to list to modify it:")
print("Original tuple:", yearly_salary)

# convert to list to modify values
yearly_salary_list = list(yearly_salary)
yearly_salary_list[2] = 75000

# convert back to tuple
modified_yearly_salary = tuple(yearly_salary_list)
print("Modified tuple:", modified_yearly_salary)
print("Type after conversion:", type(modified_yearly_salary))
print()

# ----------------------------------------------------------
# 🧩 5. Checking hashability (immutable vs mutable elements)
# ----------------------------------------------------------
print("📍 Hashability test:")
t1 = (1, 2, 3)
t2 = (1, [2, 3])  # contains mutable list

print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Hash of t1 (all immutable):", hash(t1))  # ✅ Works
try:
    print("Hash of t2 (contains list):", hash(t2))  # ❌ TypeError
except TypeError as e:
    print("Error:", e)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Tuples are immutable → you cannot add, remove, or modify elements directly.
# - A tuple can still hold mutable elements (like lists or sets).
# - The tuple’s structure (the references) is immutable, not the inner objects.
# - To “modify” a tuple, convert it to a list, change it, and convert back.
# - Only tuples with *fully immutable* elements are hashable and usable as dict keys.
# - Common use:
#     * Represent fixed collections (e.g., coordinates, configurations)
#     * Return multiple values from functions safely
