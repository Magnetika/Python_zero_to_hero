# 🎯 Lesson Objective:
# Learn how tuples are used in real-world Python programming,
# understand why immutability can be beneficial,
# and recognize practical use cases where tuples are preferred over lists.

# ----------------------------------------------------------
# 🧩 1. Returning multiple values from a function
# ----------------------------------------------------------
def calculate_stats(numbers):
    """Return total and average as a tuple."""
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg  # returns a tuple

stats = calculate_stats([5, 10, 15])
print("📍 Returning multiple values from a function:")
print("Result tuple:", stats)
total, average = stats  # tuple unpacking
print(f"Total: {total}, Average: {average}")
print()

# ----------------------------------------------------------
# 🧩 2. Representing structured data
# ----------------------------------------------------------
person = ("Alice", 28, "Engineer")
print("📍 Representing structured data with tuples:")
print(f"{person[0]} is a {person[2]} aged {person[1]}.")
print()

# You can also generate structured tuples dynamically:
def user_factory(first_name, last_name, age):
    """Return a user record as a tuple."""
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    age = int(age)
    return (first_name, last_name, age)

user = user_factory("john", "doe", "30")
print("Generated user tuple:", user)
print()

# ----------------------------------------------------------
# 🧩 3. Using tuples as dictionary keys
# ----------------------------------------------------------
print("📍 Tuples as dictionary keys:")
locations = {
    (47.4979, 19.0402): "Budapest",
    (48.8566, 2.3522): "Paris",
    (35.6895, 139.6917): "Tokyo"
}
print("Paris is located at:", [k for k, v in locations.items() if v == "Paris"])
print("Location lookup:", locations[(35.6895, 139.6917)])
print()

# ----------------------------------------------------------
# 🧩 4. Iterating over tuple-based (database-like) records
# ----------------------------------------------------------
print("📍 Tuple-based data iteration (like database rows):")
rows = [
    ("Alice", "HR", 3500),
    ("Bob", "IT", 4200),
    ("Eve", "Finance", 3900)
]

for name, dept, salary in rows:
    print(f"{name} from {dept} earns ${salary}")
print()

# ----------------------------------------------------------
# 🧩 5. Storing constants or configuration data
# ----------------------------------------------------------
print("📍 Constants stored as tuples:")
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print("Days of the week:", DAYS_OF_WEEK)
print("First day:", DAYS_OF_WEEK[0])
print()

# ----------------------------------------------------------
# 🧩 6. Using tuples in sets (tuples are hashable)
# ----------------------------------------------------------
print("📍 Tuples in sets:")
points = {(1, 2), (3, 4), (1, 2)}  # duplicates automatically removed
print("Set of unique points:", points)
print()

# ----------------------------------------------------------
# 🧩 7. Real-world structured tuple examples
# ----------------------------------------------------------
print("📍 Real-world examples:")
location = (35.6895, 139.6917)  # Tokyo coordinates
rgb_color = (255, 0, 0)         # RGB color (red)
print("Location (Tokyo):", location)
print("RGB color (red):", rgb_color)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Tuples are immutable and ordered → great for fixed, structured data.
# - Common real-world uses:
#     * Returning multiple values from functions
#     * Representing structured, read-only records
#     * Using as dictionary keys or elements in sets
#     * Storing constants or configuration data
# - Advantages:
#     ✅ Immutability → prevents accidental changes
#     ✅ Hashable → usable as dict keys
#     ✅ Lightweight and faster than lists
#     ✅ Clear semantics → data is meant to stay constant
