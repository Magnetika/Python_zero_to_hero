# ============================================================
# RANDOM MODULE – COMPLETE EXAMPLE FILE WITH ENGLISH COMMENTS
# Covers: random numbers, choices, shuffling, sampling, seeding,
# and small simulations (dice, coin toss).
# ============================================================

import random  # Import the built-in random module


# ------------------------------------------------------------
# 1. Random floating-point numbers
# ------------------------------------------------------------
print("=== Random floating numbers ===")
print(random.random())        # Random float in [0.0, 1.0)
print(random.uniform(10, 20)) # Random float between 10 and 20


# ------------------------------------------------------------
# 2. Random integers
# ------------------------------------------------------------
print("\n=== Random integers ===")
print(random.randint(1, 6))        # Random number 1–6
print(random.randrange(0, 10, 2))  # Random even number between 0–8


# ------------------------------------------------------------
# 3. Random choice from a list
# ------------------------------------------------------------
print("\n=== Random choice ===")
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))       # Pick a random fruit


# ------------------------------------------------------------
# 4. Random sample (multiple unique choices)
# ------------------------------------------------------------
print("\n=== Random sample (unique picks) ===")
numbers = [1, 2, 3, 4, 5, 6]
print(random.sample(numbers, 3))   # 3 unique random elements


# ------------------------------------------------------------
# 5. Shuffle a list
# ------------------------------------------------------------
print("\n=== Shuffle a list ===")
items = [1, 2, 3, 4, 5]
random.shuffle(items)              # Shuffles the list in place
print(items)


# ------------------------------------------------------------
# 6. Simulating random events
# ------------------------------------------------------------
print("\n=== Random simulations ===")
dice_roll = random.randint(1, 6)
print("Dice rolled:", dice_roll)

coin_toss = random.choice(["Heads", "Tails"])
print("Coin toss:", coin_toss)


# ------------------------------------------------------------
# 7. Using seed() for reproducible results
# ------------------------------------------------------------
print("\n=== Using seed (reproducible randomness) ===")
random.seed(42)
print(random.randint(1, 100))  # Always the same with seed 42
print(random.randint(1, 100))  # Same sequence every time

# Reset seed to get the same sequence again
random.seed(42)
print(random.randint(1, 100))  # Matches the first run


# ------------------------------------------------------------
# 8. Generating multiple random values in a loop
# ------------------------------------------------------------
print("\n=== Looping to generate random numbers ===")
for _ in range(5):
    print(random.randint(1, 100))


# ------------------------------------------------------------
# 9. Your original code included and enhanced
# ------------------------------------------------------------
print("\n=== Your original examples ===")
from random import randint, shuffle

number = randint(1, 100)  # Random integer 1–100
print("randint ->", number)

nums = [1, 2, 3, 4, 5]
shuffle(nums)             # Shuffle list in place
print("shuffle ->", nums)

fruits = ['apple', 'banana', 'cherry']
rand_fruit_index = randint(0, len(fruits) - 1)
print("random index pick ->", fruits[rand_fruit_index])
