# 🎯 Lesson Objective:
# Learn what a dictionary (dict) is, how to create and use it,
# and understand its key properties such as key-value storage,
# mutability, and fast lookup behavior.

# ----------------------------------------------------------
# 🧩 1. Creating dictionaries
# ----------------------------------------------------------
user = {
    "name": "Alice Smith",
    "age": 30,
}

print("📍 Dictionary type check:")
print(type(user))  # <class 'dict'>
print("User data:", user)
print()

# Duplicated keys: later key overwrites earlier one
duplicated = {'name': 'Alice Smith', 'name': 'Bob Johnson'}
print("📍 Duplicated key example:")
print(duplicated)  # {'name': 'Bob Johnson'}
print()

# ----------------------------------------------------------
# 🧩 2. Accessing elements
# ----------------------------------------------------------
print("📍 Accessing elements by key:")
print("Name:", user["name"])  # direct access
print("Age (safe access):", user.get("age"))  # safe access
print("Missing key (with default):", user.get("city", "N/A"))  # N/A if missing
print()

# ----------------------------------------------------------
# 🧩 3. Adding and modifying items
# ----------------------------------------------------------
print("📍 Adding & modifying values:")
user["name"] = "Bob Johnson"  # modify existing
user["job"] = "Engineer"      # add new
print("Updated user:", user)
print()

# ----------------------------------------------------------
# 🧩 4. Updating multiple values at once
# ----------------------------------------------------------
user.update({
    "age": 31,
    "city": "New York",
    "hobby": "Photography"
})
print("📍 After user.update():")
print(user)
print()

# ----------------------------------------------------------
# 🧩 5. Removing items
# ----------------------------------------------------------
print("📍 Removing elements:")
user.pop("hobby")      # remove by key
print("After pop('hobby'):", user)

user.popitem()         # removes last inserted pair
print("After popitem():", user)

del user["city"]       # delete by key
print("After del user['city']:", user)
print()

# ----------------------------------------------------------
# 🧩 6. Dictionary views (keys, values, items)
# ----------------------------------------------------------
user = {
    "name": "Bob Johnson",
    "age": 31,
    "job": "Engineer"
}

print("📍 Dictionary views:")
print("Keys:", user.keys())
print("Values:", user.values())
print("Items:", user.items())
print()

print("Iterating over keys and values:")
for key, value in user.items():
    print(f"{key}: {value}")
print()

# ----------------------------------------------------------
# 🧩 7. Checking membership
# ----------------------------------------------------------
print("📍 Membership testing:")
print("'name' in user →", "name" in user)  # True (checks keys)
print("'Bob Johnson' in user →", "Bob Johnson" in user)  # False (not key)
print()

# ----------------------------------------------------------
# 🧩 8. Nested dictionaries
# ----------------------------------------------------------
students = {
    "A101": {"name": "Alice", "age": 21},
    "A102": {"name": "Bob", "age": 23}
}

print("📍 Nested dictionaries:")
print("All students:", students)
print("Student A101 name:", students["A101"]["name"])
print()

# ----------------------------------------------------------
# 🧩 9. Creating a dictionary using dict()
# ----------------------------------------------------------
person = dict(name="John", age=30, city="Paris")
print("📍 Dictionary created with dict():")
print(person)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# ✔ Dictionaries store key–value pairs.
# ✔ Keys must be unique and immutable (e.g., str, int, tuple).
# ✔ Values can be any type (mutable or immutable).
# ✔ Mutable → can modify, add, or delete elements.
# ✔ Fast access → O(1) average lookup time.
# ✔ Ordered since Python 3.7 (insertion order preserved).
