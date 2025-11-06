# 🎯 Lesson Objective:
# Learn how to add conditional logic (if) to list comprehensions to filter elements based on specific criteria.

# ----------------------------------------------------------
# 📘 DATA SETUP
# ----------------------------------------------------------
rpg_games = [
    ['Earthbound', 'Final Fantasy', 'Chrono Trigger'],
    ['The Witcher', 'Dark Souls', 'Skyrim'],
    ['Pokemon', 'Dragon Quest', 'Fire Emblem']
]

# ----------------------------------------------------------
# 🧩 1. Create a filtered list using a single condition
# ----------------------------------------------------------
# Flatten the nested list and keep only games with names longer than 6 characters
flatten_rpg_games = [game for sublist in rpg_games for game in sublist if len(game) > 6]
print("📍 Single condition (>6 letters):")
print(flatten_rpg_games)
print()

# ----------------------------------------------------------
# 🧩 2. Use multiple conditions in a comprehension
# ----------------------------------------------------------
# Keep games that are longer than 6 letters AND contain a space
filtered_multiple = [game for sublist in rpg_games for game in sublist if len(game) > 6 and " " in game]
print("📍 Multiple conditions (>6 letters AND has space):")
print(filtered_multiple)
print()

# ----------------------------------------------------------
# 🧩 3. Apply an if...else expression inside a comprehension
# ----------------------------------------------------------
# Label each game as 'Long name' or 'Short name' based on its length
labels = ["Long name" if len(game) > 6 else "Short name"
          for sublist in rpg_games for game in sublist]
print("📍 Using if...else inside comprehension:")
print(labels)
print()

# ----------------------------------------------------------
# 🧩 4. Compare readability with equivalent for loops
# ----------------------------------------------------------
flatten_rpg_games_loop = []
for sublist in rpg_games:
    for game in sublist:
        if len(game) > 6:
            flatten_rpg_games_loop.append(game)

print("📍 Equivalent using for loops:")
print(flatten_rpg_games_loop)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Takeaways
# ----------------------------------------------------------
# - `if` at the END filters elements
# - `if...else` at the BEGINNING decides what value to return
# - List comprehensions improve readability for simple conditions
# - For complex logic, traditional loops may be clearer
