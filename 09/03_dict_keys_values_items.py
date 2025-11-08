# 🎯 Lesson Objective:
# Learn how to iterate through a dictionary using for loops to access
# keys, values, and key–value pairs, and understand when to use each.

# ----------------------------------------------------------
# 🧩 Example dictionary
# ----------------------------------------------------------
user = {'name': 'Alice', 'age': 30, 'job': 'Engineer'}

# ----------------------------------------------------------
# 🧩 1. Exploring dictionary views
# ----------------------------------------------------------
print("📍 Dictionary views:")
print("Keys:", user.keys())
print("Values:", user.values())
print("Items:", user.items())
print()

# ----------------------------------------------------------
# 🧩 2. Iterating through keys (default behavior)
# ----------------------------------------------------------
print("📍 Iterating through keys:")
for key in user.keys():
    print("Key:", key)
print()

# ----------------------------------------------------------
# 🧩 3. Iterating through values
# ----------------------------------------------------------
print("📍 Iterating through values:")
for value in user.values():
    print("Value:", value)
print()

# ----------------------------------------------------------
# 🧩 4. Iterating through key–value pairs
# ----------------------------------------------------------
print("📍 Iterating through key–value pairs:")
for key, value in user.items():
    print(f"{key}: {value}")
print()

# ----------------------------------------------------------
# 🧩 5. Conditional logic inside loop
# ----------------------------------------------------------
print("📍 Conditional check during iteration:")
for key, value in user.items():
    if key == "age" and value >= 30:
        print(f"🎉 {user['name']} is an experienced {user['job']}")
print()

# ----------------------------------------------------------
# 🧩 6. Nested dictionary iteration
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
# 🧩 7. Enumerating dictionary items
# ----------------------------------------------------------
print("📍 Enumerating key–value pairs:")
for index, (key, value) in enumerate(user.items(), start=1):
    print(f"{index}. {key} → {value}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Takeaways
# ----------------------------------------------------------
# ✔ Looping over a dict (for key in dict) → iterates keys by default.
# ✔ Use .values() when you only need the values.
# ✔ Use .items() to get both key and value in one go.
# ✔ Dictionaries preserve insertion order (Python 3.7+).
# ✔ Use conditions inside loops to filter or evaluate values.
# ✔ Nested dicts can be looped with nested for loops.
