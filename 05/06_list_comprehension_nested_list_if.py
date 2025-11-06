# 🎯 Lesson Objective:
# Learn how to apply conditional filtering (if) within nested list comprehensions
# to create, transform, and filter multi-dimensional data structures efficiently.

# ----------------------------------------------------------
# 📘 DATA SETUP
# ----------------------------------------------------------
rpg_games = [
    ['Earthbound', 'Final Fantasy', 'Chrono Trigger'],
    ['The Witcher', 'Dark Souls', 'Skyrim'],
    ['Pokemon', 'Dragon Quest', 'Fire Emblem']
]

# ----------------------------------------------------------
# 🧩 1. Create a nested list comprehension that filters elements with an if condition
# ----------------------------------------------------------
# Flatten the nested list, keeping only game titles longer than 6 characters
filtered_games = [game for sublist in rpg_games for game in sublist if len(game) > 6]
print("📍 Filtered (len > 6):")
print(filtered_games)
print()

# ----------------------------------------------------------
# 🧩 2. Apply a transformation using if...else inside the comprehension
# ----------------------------------------------------------
# Transform each game name: uppercase if longer than 10 characters, otherwise lowercase
transformed_games = [
    [game.upper() if len(game) > 10 else game.lower() for game in sublist]
    for sublist in rpg_games
]
print("📍 Transformed (upper if >10 chars else lower):")
print(transformed_games)
print()

# ----------------------------------------------------------
# 🧩 3. Combine multiple loops and filters in one comprehension
# ----------------------------------------------------------
# Generate pairs of (game1, game2) where both are long names and not the same
game_pairs = [
    (g1, g2)
    for sublist1 in rpg_games for g1 in sublist1 if len(g1) > 6
    for sublist2 in rpg_games for g2 in sublist2 if len(g2) > 6 and g1 != g2
]
print("📍 Combined loops and filters (pairs of long names):")
print(game_pairs[:10], "...")  # truncate output for readability
print()

# ----------------------------------------------------------
# 🧩 4. Rewrite a nested for loop with conditions as a single comprehension
# ----------------------------------------------------------
flatten_loop = []
for sublist in rpg_games:
    for game in sublist:
        if len(game) > 6:
            flatten_loop.append(game)

# Equivalent comprehension:
flatten_comp = [game for sublist in rpg_games for game in sublist if len(game) > 6]

print("📍 Equivalent comparison:")
print("For loop result:", flatten_loop)
print("List comprehension result:", flatten_comp)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - `if` at the END filters elements from the inner loop
# - `if...else` at the BEGINNING transforms each element
# - Multiple loops and filters can be combined for complex structures
# - Keep your expressions readable — avoid deep nesting for clarity
