# 🎯 Lesson Objective:
# Learn common operations available for tuples in Python,
# including indexing, slicing, concatenation, repetition,
# membership tests, and built-in functions.

# ----------------------------------------------------------
# 🧩 1. Indexing and Slicing
# ----------------------------------------------------------
t = (10, 20, 30, 40, 50)
print("📍 Indexing and slicing:")
print("t[1] =", t[1])      # 20
print("t[-1] =", t[-1])    # 50
print("t[1:3] =", t[1:3])  # (20, 30)
print("t[::-1] =", t[::-1])  # reversed tuple
print()

# ----------------------------------------------------------
# 🧩 2. Concatenation and Repetition
# ----------------------------------------------------------
a = (1, 2)
b = (3, 4)
print("📍 Concatenation and repetition:")
print("a + b =", a + b)       # (1, 2, 3, 4)
print("a * 2 =", a * 2)       # (1, 2, 1, 2)
print()

# ----------------------------------------------------------
# 🧩 3. Membership test
# ----------------------------------------------------------
fruits = ("apple", "banana", "cherry")
print("📍 Membership test:")
print("'banana' in fruits:", "banana" in fruits)
print("'orange' in fruits:", "orange" in fruits)
print()

# ----------------------------------------------------------
# 🧩 4. Built-in functions: len(), min(), max(), sum()
# ----------------------------------------------------------
nums = (4, 1, 7)
print("📍 Built-in functions:")
print("len(nums) =", len(nums))   # 3
print("min(nums) =", min(nums))   # 1
print("max(nums) =", max(nums))   # 7
print("sum(nums) =", sum(nums))   # 12
print()

# ----------------------------------------------------------
# 🧩 5. Tuple methods: count() and index()
# ----------------------------------------------------------
t = (1, 2, 2, 3, 2)
print("📍 Tuple methods:")
print("t.count(2) =", t.count(2))  # 3
print("t.index(3) =", t.index(3))  # position of first 3
print()

# ----------------------------------------------------------
# 🧩 6. Converting tuple → list → tuple (for modification)
# ----------------------------------------------------------
t = (1, 2, 3)
print("📍 Converting tuple to list to modify:")
lst = list(t)
lst.append(4)
t = tuple(lst)
print("Modified tuple:", t)
print()

# ----------------------------------------------------------
# 🧩 7. Tuple unpacking
# ----------------------------------------------------------
names = ('Alice', 'Bob', 'Charlie', 'Diana')
print("📍 Tuple unpacking:")
Alice, Bob, Charlie, Diana = names
print(f"Unpacked → {Alice}, {Bob}, {Charlie}, {Diana}")
print("First two names:", names[:2])
print("Every 3rd name:", names[::3])
print("Length of names tuple:", len(names))
print()

# ----------------------------------------------------------
# 🧩 8. Generator expression to tuple conversion
# ----------------------------------------------------------
numbers = (1, 2, 3, 4, 5)
squares = (i ** 2 for i in numbers)  # generator
squares_tuple = tuple(squares)       # convert to tuple
print("📍 Generator to tuple conversion:")
print("Type of 'squares':", type(squares))
print("Type of 'squares_tuple':", type(squares_tuple))
print("Squared numbers tuple:", squares_tuple)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Tuples support indexing and slicing just like lists.
# - They are immutable → concatenation creates a new tuple.
# - `+` joins tuples, `*` repeats them.
# - Use `in` to test membership.
# - Common built-in functions: len(), min(), max(), sum().
# - Tuple methods: .count(value), .index(value).
# - Convert to list temporarily to modify values.
# - Unpacking lets you assign multiple variables in one line.
# - Generators can be cast to tuples to save results efficiently.
