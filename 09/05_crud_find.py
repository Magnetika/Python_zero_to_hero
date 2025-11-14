# 🎯 Lesson Objective:
# Learn how to perform the Read operation in CRUD for dictionaries — 
# that is, how to access, check, and retrieve values safely.

# ----------------------------------------------------------
# 🧩 Example: List of user dictionaries (like JSON records)
# ----------------------------------------------------------
users = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com"},
    {"id": 3, "first_name": "Alice", "last_name": "Johnson", "email": "alice.johnson@example.com"},
    {"id": 4, "first_name": "Bob", "last_name": "Brown", "email": "bob.brown@example.com"}
]

# ----------------------------------------------------------
# 🧩 Function: Read user by ID (safe dictionary access)
# ----------------------------------------------------------
def find_user(user_id):
    """Return a user dictionary with the given ID, or None if not found."""
    for user in users:
        if user["id"] == user_id:   # direct key access
            return user
    return None  # safe return if not found


# ----------------------------------------------------------
# 🧩 1. Basic dictionary access
# ----------------------------------------------------------
student = {"name": "Alice", "age": 22, "grade": 4.8}
print(student["name"])  # Direct access
# print(student["email"])  # ❌ KeyError if key doesn't exist
print(student.get("email", "Not found"))  # ✅ Safe access with default
print()

# ----------------------------------------------------------
# 🧩 2. Reading multiple items
# ----------------------------------------------------------
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print()

# ----------------------------------------------------------
# 🧩 3. Iterating through items
# ----------------------------------------------------------
for key, value in student.items():
    print(f"{key}: {value}")
print()

# ----------------------------------------------------------
# 🧩 4. Checking for key or value existence
# ----------------------------------------------------------
if "grade" in student:
    print("✅ 'grade' key exists!")
if 22 in student.values():
    print("✅ 22 found among values!")
print()

# ----------------------------------------------------------
# 🧩 5. Nested dictionary access
# ----------------------------------------------------------
students = {
    "A101": {"name": "Alice", "grade": 4.8},
    "A102": {"name": "Bob", "grade": 3.9}
}

# Direct access
print(students["A101"]["name"])  # Alice

# Safe nested access
print(students.get("A103", {}).get("name", "Unknown"))  # Unknown
print()

# ----------------------------------------------------------
# 🧩 6. Real-world example: find_user() usage
# ----------------------------------------------------------
print("📍 Lookup results:")
print(find_user(3))  # Should return Alice Johnson
print(find_user(5))  # Should return None (not found)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Takeaways
# ----------------------------------------------------------
# ✔ Use dict[key] for direct reads (fast, but may raise KeyError)
# ✔ Use .get() for safe reads with optional default values
# ✔ Use .keys(), .values(), .items() for inspection
# ✔ Combine with loops to filter or find items
# ✔ Nested dicts can be read safely with .get(..., {}).get(...)
# ✔ Reading is the "R" in CRUD: retrieving data without modifying it
