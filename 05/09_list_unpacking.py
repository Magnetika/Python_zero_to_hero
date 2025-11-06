# 🎯 Lesson Objective:
# Learn how to unpack lists into individual variables,
# how to use the * operator for flexible unpacking,
# and understand how it differs from tuple and string unpacking.

# ----------------------------------------------------------
# 📘 DATA SETUP
# ----------------------------------------------------------
user = ['Agnes', 'Szabo', 32]

# ----------------------------------------------------------
# 🧩 1. Unpack a list into multiple variables
# ----------------------------------------------------------
first_name, last_name, age = user
print("📍 Basic list unpacking:")
print(first_name, last_name, age)
print()

# ----------------------------------------------------------
# 🧩 2. Use * to capture multiple elements
# ----------------------------------------------------------
numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers
print("📍 Using * to capture middle elements:")
print("first:", first)
print("middle:", middle)
print("last:", last)
print()

# ----------------------------------------------------------
# 🧩 3. Ignore unnecessary values with _
# ----------------------------------------------------------
data = [100, 200, 300, 400]
a, b, _, d = data
print("📍 Using _ to ignore a value:")
print(a, b, d)
print()

# ----------------------------------------------------------
# 🧩 4. Combine unpacking with loops or function returns
# ----------------------------------------------------------
def get_player_data():
    return ["Link", "Hylian", 17, "Sword Master"]

name, race, age, title = get_player_data()
print("📍 Function return unpacking:")
print(f"{name} is a {race} aged {age}, known as '{title}'")
print()

# Unpacking inside a loop:
players = [
    ["Mario", "Plumber"],
    ["Zelda", "Princess"],
    ["Kirby", "Hero"]
]

print("📍 Loop unpacking:")
for name, role in players:
    print(f"{name} → {role}")
print()

# ----------------------------------------------------------
# 🧩 Bonus: Nested list unpacking (from your example)
# ----------------------------------------------------------
grades = [1, [2, 3, 4], 5, [4, 5]]
a, (b, c, d), e, (f, g) = grades
print("📍 Nested list unpacking:")
print(a, b, c, d, e, f, g)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Lists can be unpacked like tuples or strings
# - Use * to capture multiple values as a list
# - Use _ to ignore values you don’t need
# - Combine unpacking with loops and function outputs
# - Ensure the number of variables matches the structure
