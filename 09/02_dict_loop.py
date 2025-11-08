# 🎯 Lesson Objective:
# Learn how to iterate through a dictionary using for loops
# to access keys, values, and key–value pairs, and understand when to use each.

# ----------------------------------------------------------
# 🧩 1. Basic dictionary
# ----------------------------------------------------------
user = {"name": "Alice Smith", "age": 30, "job": "Engineer"}

# ----------------------------------------------------------
# 🧩 2. Iterating through keys (default behavior)
# ----------------------------------------------------------
print("📍 Iterating over keys:")
for key in user:
    print("Key:", key)
print()

# ----------------------------------------------------------
# 🧩 3. Accessing values during iteration
# ----------------------------------------------------------
print("📍 Keys and their values:")
for key in user:
    print(f"{key} → {user[key]}")
print()

# ----------------------------------------------------------
# 🧩 4. Iterating explicitly over keys
# ----------------------------------------------------------
print("📍 Using .keys():")
for key in user.keys():
    print("Key:", key)
print()

# ----------------------------------------------------------
# 🧩 5. Iterating only over values
# ----------------------------------------------------------
print("📍 Using .values():")
for value in user.values():
    print("Value:", value)
print()

# ----------------------------------------------------------
# 🧩 6. Iterating over key–value pairs
# ----------------------------------------------------------
print("📍 Using .items():")
for key, value in user.items():
    print(f"{key}: {value}")
print()

# ----------------------------------------------------------
# 🧩 7. Using conditions in dictionary loops
# ----------------------------------------------------------
print("📍 Conditional iteration:")
for key, value in user.items():
    if key == "age" and value >= 30:
        print("Experienced employee ✅")
print()

# ----------------------------------------------------------
# 🧩 8. Enumerating dictionary items (with index)
# ----------------------------------------------------------
print("📍 Using enumerate() on dictionary items:")
for i, (key, value) in enumerate(user.items(), start=1):
    print(f"{i}. {key} → {value}")
print()

# ----------------------------------------------------------
# 🧩 9. Iterating through nested dictionaries
# ----------------------------------------------------------
students = {
    "A101": {"name": "Alice", "grade": 4.7},
    "A102": {"name": "Bob", "grade": 3.9}
}

print("📍 Iterating through nested dictionaries:")
for student_id, info in students.items():
    print(f"ID: {student_id}")
    for key, value in info.items():
        print(f"  {key}: {value}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Takeaways
# ----------------------------------------------------------
# ✔ Looping over a dict → de
