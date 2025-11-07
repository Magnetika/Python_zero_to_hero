# 🎯 Lesson Objective:
# Learn how sets are applied in real-world programming scenarios
# such as removing duplicates, handling unique data, performing
# fast lookups, and executing mathematical operations on data collections.

# ----------------------------------------------------------
# 🧩 1. Removing duplicates from data
# ----------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 1, 1, 2, 2, 5, 5, 5]
print("📍 Original list:", numbers)

numbers_without_duplicates = set(numbers)
print("Unique numbers (set):", numbers_without_duplicates)

# Convert back to list if needed
unique_list = list(numbers_without_duplicates)
print("Unique numbers (list):", unique_list)
print()

# ----------------------------------------------------------
# 🧩 2. Fast membership testing
# ----------------------------------------------------------
print("📍 Fast membership test:")
banned_users = {"alice", "bob", "charlie"}
user = "bob"

if user in banned_users:
    print(f"Access denied for {user}")
else:
    print(f"Welcome, {user}")
print()

# ----------------------------------------------------------
# 🧩 3. Finding unique / shared items between collections
# ----------------------------------------------------------
print("📍 Comparing sets (union, intersection, difference):")
group_A = {"Anna", "Ben", "Clara"}
group_B = {"Ben", "David", "Ella"}

print("Common:", group_A & group_B)   # Intersection
print("Only in A:", group_A - group_B) # Difference
print("All unique:", group_A | group_B) # Union
print()

# ----------------------------------------------------------
# 🧩 4. Detecting duplicates in data
# ----------------------------------------------------------
numbers = [1, 2, 3, 3, 4, 5, 1]
has_duplicates = len(numbers) != len(set(numbers))
print("📍 Detecting duplicates:")
print("List:", numbers)
print("Has duplicates:", has_duplicates)
print()

# ----------------------------------------------------------
# 🧩 5. Handling large datasets efficiently
# ----------------------------------------------------------
print("📍 Large dataset membership check:")
valid_ids = set(range(1_000_000))  # 1 million elements
print("Is 123456 valid?", 123456 in valid_ids)
print("Is 999999 valid?", 999999 in valid_ids)
print()

# ----------------------------------------------------------
# 🧩 6. Comparing datasets (real-world example)
# ----------------------------------------------------------
print("📍 Comparing two customer lists:")
system_A = {"Anna", "Ben", "Clara", "David"}
system_B = {"Clara", "David", "Eva", "Frank"}

missing_in_B = system_A - system_B
new_in_B = system_B - system_A

print("Missing in B:", missing_in_B)
print("New in B:", new_in_B)
print()

# ----------------------------------------------------------
# 🧩 7. Text and word processing
# ----------------------------------------------------------
print("📍 Unique word extraction from text:")
sentence = "the quick brown fox jumps over the lazy dog the quick fox"
unique_words = set(sentence.split())
print("Unique words:", unique_words)
print("Word count:", len(unique_words))
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# ✔ Sets automatically remove duplicates — perfect for data cleaning
# ✔ Membership testing (in operator) is O(1) → very fast
# ✔ Set operations simplify comparisons between collections:
#       - Union (|)            → combine all
#       - Intersection (&)     → common elements
#       - Difference (-)       → unique to one set
#       - Symmetric diff (^)   → unique to both
# ✔ Great for filtering, deduplication, and data comparison
# ✔ frozenset() provides an immutable alternative (safe for dict keys)
