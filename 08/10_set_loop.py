# 🎯 Lesson Objective:
# Learn how to iterate through the elements of a set using for loops,
# understand that sets are unordered collections, and explore practical examples.

# ----------------------------------------------------------
# 🧩 1. Basic iteration
# ----------------------------------------------------------
colors = {"red", "green", "blue"}

print("📍 Basic iteration over a set:")
for color in colors:
    print(color)  # order not guaranteed
print()

# ----------------------------------------------------------
# 🧩 2. Iterating with a condition
# ----------------------------------------------------------
numbers = {10, 25, 30, 45, 60}

print("📍 Conditional iteration:")
for n in numbers:
    if n % 15 == 0:
        print(f"{n} is divisible by 15")
print()

# ----------------------------------------------------------
# 🧩 3. Using enumerate() — numbering elements during iteration
# ----------------------------------------------------------
fruits = {"apple", "banana", "cherry"}

print("📍 Enumerate set elements:")
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")  # index is arbitrary, not positional
print()

# ----------------------------------------------------------
# 🧩 4. Iterating over a set of tuples (unpacking)
# ----------------------------------------------------------
points = {(1, 2), (3, 4), (5, 6)}

print("📍 Iterating over a set of tuples:")
for x, y in points:
    print(f"Point: ({x}, {y})")
print()

# ----------------------------------------------------------
# 🧩 5. Removing duplicates using a set, then iterating
# ----------------------------------------------------------
names = ["Anna", "Bob", "Anna", "Clara"]
unique_names = set(names)

print("📍 Iterating over unique names:")
for name in unique_names:
    print(name)  # order may vary
print()

# ----------------------------------------------------------
# 🧩 6. Performing calculations inside a loop
# ----------------------------------------------------------
numbers = {2, 4, 6, 8}
total = 0

for n in numbers:
    total += n

print("📍 Summing values from a set:")
print("Sum:", total)
print()

# ----------------------------------------------------------
# 🧩 7. Advanced: Using sorted() for ordered iteration
# ----------------------------------------------------------
numbers = {1, 2, 3, 4, 5}
print("📍 Sorted ascending iteration:")
for v in sorted(numbers):
    print(v)

print("📍 Sorted descending iteration:")
for v in sorted(numbers, reverse=True):
    print(v)

print("📍 Custom sort: negative key (reverse order):")
for v in sorted(numbers, key=lambda x: -x):
    print(v)

print("📍 Custom sort: even first, then odd:")
for v in sorted(numbers, key=lambda x: (x % 2, x)):
    print(v)

print("📍 Custom sort: even first, odd descending:")
for v in sorted(numbers, key=lambda x: (x % 2, -x)):
    print(v)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Takeaways
# ----------------------------------------------------------
# ✔ Sets are iterable, but unordered → iteration order is not guaranteed.
# ✔ Use `for element in set:` for standard iteration.
# ✔ Use conditions inside loops for filtering.
# ✔ Use `enumerate()` to pair elements with an index (just a counter).
# ✔ Use `sorted(set)` when you need ordered iteration.
# ✔ Useful for deduplication, membership testing, and numeric calculations.
