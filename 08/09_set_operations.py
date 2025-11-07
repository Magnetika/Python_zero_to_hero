# 🎯 Lesson Objective:
# Learn how to perform mathematical set operations using operators (|, &, -, ^)
# instead of method calls, and understand how these operators map to common
# set theory operations.

# ----------------------------------------------------------
# 🧩 1. Union ( | )
# ----------------------------------------------------------
A = {1, 2, 3}
B = {3, 4, 5}
print("📍 Union (A | B):", A | B)  # {1, 2, 3, 4, 5}
print("Equivalent method:", A.union(B))
print()

# ----------------------------------------------------------
# 🧩 2. Intersection ( & )
# ----------------------------------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5}
print("📍 Intersection (A & B):", A & B)  # {3, 4}
print("Equivalent method:", A.intersection(B))
print()

# ----------------------------------------------------------
# 🧩 3. Difference ( - )
# ----------------------------------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5}
print("📍 Difference (A - B):", A - B)  # {1, 2}
print("Equivalent method:", A.difference(B))
print()

# ----------------------------------------------------------
# 🧩 4. Symmetric Difference ( ^ )
# ----------------------------------------------------------
A = {1, 2, 3}
B = {3, 4, 5}
print("📍 Symmetric Difference (A ^ B):", A ^ B)  # {1, 2, 4, 5}
print("Equivalent method:", A.symmetric_difference(B))
print()

# ----------------------------------------------------------
# 🧩 5. Chaining multiple operations
# ----------------------------------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5}
C = {4, 5, 6}
result = (A | B) & C  # (Union → Intersection)
print("📍 Chained operation (A ∪ B) ∩ C:", result)  # {4, 5}
print()

# ----------------------------------------------------------
# 🧩 6. In-place operators (|=, &=, -=, ^=)
# ----------------------------------------------------------
x = {1, 2, 3}
x |= {4, 5}     # same as x.update({4, 5})
print("📍 In-place Union (|=):", x)

x &= {2, 3, 4}  # same as x.intersection_update({2, 3, 4})
print("In-place Intersection (&=):", x)

x -= {3}        # same as x.difference_update({3})
print("In-place Difference (-=):", x)

x ^= {4, 6}     # same as x.symmetric_difference_update({4, 6})
print("In-place Symmetric Difference (^=):", x)
print()

# ----------------------------------------------------------
# 🧩 7. Practical Example – Combining Datasets
# ----------------------------------------------------------
team_A = {"Anna", "Ben", "Clara"}
team_B = {"Clara", "David", "Ella"}

print("📍 Practical example:")
print("All members (A ∪ B):", team_A | team_B)
print("Shared members (A ∩ B):", team_A & team_B)
print("Unique to A (A - B):", team_A - team_B)
print("Different members (A Δ B):", team_A ^ team_B)
print()

# ----------------------------------------------------------
# 🧩 8. Subset / Superset / Disjoint Checks
# ----------------------------------------------------------
x1 = {'a', 'b', 'c'}
x2 = {'b', 'c', 'd'}

print("📍 Relationship checks:")
print("Union:", x1 | x2)                   # {'a', 'b', 'c', 'd'}
print("Intersection:", x1 & x2)            # {'b', 'c'}
print("Difference:", x1 - x2)              # {'a'}
print("Symmetric Difference:", x1 ^ x2)    # {'a', 'd'}

print("Subset check (x1 <= x2):", x1 <= x2)        # False
print("Superset check (x1 >= x2):", x1 >= x2)      # False
print("Disjoint (x1 ∩ x2 == ∅):", x1.isdisjoint(x2))  # False
print()

# ----------------------------------------------------------
# ✅ Summary / Key Takeaways
# ----------------------------------------------------------
# ✔ |  → Union  (A ∪ B)
# ✔ &  → Intersection  (A ∩ B)
# ✔ -  → Difference  (A - B)
# ✔ ^  → Symmetric Difference  (A Δ B)
# ✔ In-place versions: |=, &=, -=, ^=
# ✔ Relationship operators: <= (subset), >= (superset)
# ✔ Operators are concise and expressive — ideal for mathematical logic.
# ✔ Methods are clearer for chaining and working with many sets at once.
