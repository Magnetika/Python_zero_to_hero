# 🎯 Lesson Objective:
# Learn how to perform mathematical set operations (union, intersection,
# difference, symmetric difference) using set methods instead of operators,
# and understand when to use each.

# ----------------------------------------------------------
# 🧩 1. Union – .union()
# ----------------------------------------------------------
A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}
C = {'d', 'e', 'f'}

print("📍 Union examples:")
print("A ∪ B:", A.union(B))             # {'a', 'b', 'c', 'd'}
print("A ∪ B ∪ C:", A.union(B, C))      # {'a', 'b', 'c', 'd', 'e', 'f'}
print()

# ----------------------------------------------------------
# 🧩 2. Intersection – .intersection()
# ----------------------------------------------------------
A = {'a', 'b', 'c', 'd'}
B = {'b', 'c', 'e'}

print("📍 Intersection examples:")
print("A ∩ B:", A.intersection(B))      # {'b', 'c'}
print()

# ----------------------------------------------------------
# 🧩 3. Difference – .difference()
# ----------------------------------------------------------
A = {'a', 'b', 'c', 'd'}
B = {'b', 'c', 'e'}
C = {'a'}

print("📍 Difference examples:")
print("A - B:", A.difference(B))        # {'a', 'd'}
print("A - B - C:", A.difference(B, C)) # {'d'}
print()

# ----------------------------------------------------------
# 🧩 4. Symmetric Difference – .symmetric_difference()
# ----------------------------------------------------------
A = {'a', 'b', 'c'}
B = {'b', 'd', 'e'}

print("📍 Symmetric Difference examples:")
print("A Δ B:", A.symmetric_difference(B))  # {'a', 'c', 'd', 'e'}
print()

# ----------------------------------------------------------
# 🧩 5. In-place operations (update methods)
# ----------------------------------------------------------
A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}

print("📍 In-place operations:")
A.update(B)   # union update
print("After update (union):", A)  # {'a', 'b', 'c', 'd'}

A.intersection_update({'b', 'c', 'x'})
print("After intersection_update:", A)  # {'b', 'c'}

A.difference_update({'b'})
print("After difference_update:", A)  # {'c'}

A.symmetric_difference_update({'c', 'z'})
print("After symmetric_difference_update:", A)  # {'z'}
print()

# ----------------------------------------------------------
# 🧩 6. Subset, Superset, and Disjoint Checks
# ----------------------------------------------------------
A = {1, 2}
B = {1, 2, 3}
C = {4, 5}

print("📍 Relationship checks:")
print("A ⊆ B (A is subset of B):", A.issubset(B))     # True
print("B ⊇ A (B is superset of A):", B.issuperset(A)) # True
print("A ∩ C = ∅ (disjoint):", A.isdisjoint(C))       # True
print()

# ----------------------------------------------------------
# 🧩 7. Combined Example – Practical Workflow
# ----------------------------------------------------------
x1 = {'a', 'b', 'c'}
x2 = {'b', 'c', 'd'}

print("📍 Combined workflow:")
print("Union:", x1.union(x2))                  # {'a', 'b', 'c', 'd'}
print("Intersection:", x1.intersection(x2))    # {'b', 'c'}
print("Difference:", x1.difference(x2))        # {'a'}
print("Symmetric Difference:", x1.symmetric_difference(x2))  # {'a', 'd'}

x1.update(x2)
print("After update:", x1)                     # {'a', 'b', 'c', 'd'}

x1.remove('a')
print("After remove('a'):", x1)                # {'b', 'c', 'd'}

x1.add('e')
print("After add('e'):", x1)                   # {'b', 'c', 'd', 'e'}

x1.clear()
print("After clear():", x1)                    # set()
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Use .union(), .intersection(), .difference(), .symmetric_difference()
#   instead of |, &, -, ^ for clarity and method chaining.
# - In-place variants (.update(), .intersection_update(), etc.)
#   modify the set directly without creating a new one.
# - issubset(), issuperset(), and isdisjoint() check set relationships.
# - These methods are especially useful when comparing data collections
#   like user IDs, tags, or categories.
