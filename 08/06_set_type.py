# 🎯 Lesson Objective:
# Understand what sets are, how they differ from lists and tuples,
# how to create and manipulate them, and how they are used in mathematical and real-world contexts.

# ----------------------------------------------------------
# 🧩 1. Creating sets and removing duplicates
# ----------------------------------------------------------
numbers = {1, 2, 3, 4, 5, 1, 2, 3}  # duplicates automatically removed
print("📍 Creating a set:")
print("Type:", type(numbers))
print("Unique elements:", numbers)
print()

# Empty set vs empty dictionary
empty_set = set()
empty_dict = {}
print("Empty set type:", type(empty_set))
print("Empty dict type:", type(empty_dict))
print()

# ----------------------------------------------------------
# 🧩 2. Adding and removing elements
# ----------------------------------------------------------
print("📍 Basic set operations:")
numbers.add(4)          # already exists → no change
numbers.update([5, 6, 7])  # add multiple elements
print("After update:", numbers)

numbers.remove(1)       # remove existing element
print("After remove(1):", numbers)

numbers.discard(5)      # remove if exists, no error if missing
print("After discard(5):", numbers)

removed = numbers.pop()  # removes an arbitrary element
print("After pop():", numbers, "| Removed element:", removed)

numbers.clear()         # empties the set
print("After clear():", numbers)
print()

# ----------------------------------------------------------
# 🧩 3. Performing mathematical set operations
# ----------------------------------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("📍 Set operations (mathematical):")
print("A =", A)
print("B =", B)
print("Union (A | B):", A | B)
print("Intersection (A & B):", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference (A ^ B):", A ^ B)
print()

# ----------------------------------------------------------
# 🧩 4. Membership test (fast lookup)
# ----------------------------------------------------------
numbers = {1, 2, 3, 4, 5}
print("📍 Membership test:")
print("2 in numbers:", 2 in numbers)
print("10 in numbers:", 10 in numbers)
print()

# ----------------------------------------------------------
# 🧩 5. Converting from other data types
# ----------------------------------------------------------
letters = set("banana")
print("📍 Converting string to set (duplicates removed):", letters)

nums_from_list = set([1, 2, 2, 3, 4, 4])
print("From list:", nums_from_list)
print()

# ----------------------------------------------------------
# 🧩 6. Immutable sets (frozenset)
# ----------------------------------------------------------
frozen = frozenset([1, 2, 3])
print("📍 Frozenset (immutable set):", frozen)
try:
    frozen.add(4)
except AttributeError as e:
    print("Cannot modify frozenset:", e)
print()

# ----------------------------------------------------------
# 🧩 7. Comparison summary
# ----------------------------------------------------------
print("📍 Comparison summary:")
print(f"{'Feature':<20}{'Set':<10}{'List':<10}{'Tuple':<10}")
print(f"{'Ordered':<20}{'No':<10}{'Yes':<10}{'Yes':<10}")
print(f"{'Mutable':<20}{'Yes':<10}{'Yes':<10}{'No':<10}")
print(f"{'Duplicates allowed':<20}{'No':<10}{'Yes':<10}{'Yes':<10}")
print(f"{'Indexed access':<20}{'No':<10}{'Yes':<10}{'Yes':<10}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Sets are unordered, mutable collections of unique elements.
# - Duplicates are automatically removed.
# - Fast membership checks (O(1) on average).
# - Common operations: add(), remove(), discard(), update(), pop(), clear().
# - Mathematical operations: union |, intersection &, difference -, symmetric difference ^.
# - frozenset = immutable version of a set.
# - Sets are ideal for eliminating duplicates, fast lookups, and mathematical data operations.
