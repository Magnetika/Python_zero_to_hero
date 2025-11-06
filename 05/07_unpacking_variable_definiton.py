# 🎯 Lesson Objective:
# Learn how to assign values to multiple variables in a single line
# and how to swap variable values efficiently without using temporary variables.

# ----------------------------------------------------------
# 🧩 1. Assign three variables in a single line
# ----------------------------------------------------------
first_name, last_name, age = 'Agnes', 'Szabo', 32
print("📍 Multiple assignment:")
print(first_name, last_name, age)
print()

# ----------------------------------------------------------
# 🧩 2. Swap two variables without a temporary variable
# ----------------------------------------------------------
a, b = 10, 20
print("Before swap:", a, b)

a, b = b, a  # swap values in one line
print("After swap:", a, b)
print()

# ----------------------------------------------------------
# 🧩 3. Unpack a tuple or list into variables
# ----------------------------------------------------------
coordinates = (5, 10)
x, y = coordinates
print("📍 Tuple unpacking:")
print("x =", x, ", y =", y)
print()

# You can do the same with a list:
rgb = [255, 128, 64]
r, g, b = rgb
print("📍 List unpacking:")
print("r =", r, ", g =", g, ", b =", b)
print()

# ----------------------------------------------------------
# 🧩 4. Use _ to ignore unused elements during unpacking
# ----------------------------------------------------------
person_data = ("Agnes", "Szabo", 32, "Hungary")
first, last, _, country = person_data
print("📍 Using _ to ignore unused values:")
print(first, last, country)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Assign multiple variables in one line with commas
# - Swap variables without needing a temporary variable
# - Unpack tuples/lists directly into variables
# - Use `_` as a placeholder for values you don’t need
