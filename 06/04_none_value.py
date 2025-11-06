# 🎯 Lesson Objective:
# Understand the NoneType type and the meaning of None in Python,
# how it represents “no value,” and where it appears in real code.

# ----------------------------------------------------------
# 🧩 1. Create a function without a return statement and print its result
# ----------------------------------------------------------
def greeting():
    print("Hello, World!")  # prints something, but does not return anything

print("📍 Function without explicit return:")
result = greeting()
print("Returned value:", result)  # None
print()

# ----------------------------------------------------------
# 🧩 2. Use None as a placeholder variable value
# ----------------------------------------------------------
basket = None
print("📍 Placeholder variable:")
print("Type of basket:", type(basket))  # <class 'NoneType'>

# Simulating a variable that will be filled later
if basket is None:
    print("The basket is empty (None). Let's add some fruit.")
    basket = ["apple", "banana"]
print("Basket now:", basket)
print()

# ----------------------------------------------------------
# 🧩 3. Check for None using 'is' and 'is not'
# ----------------------------------------------------------
data = None
print("📍 Checking for None using 'is' and 'is not':")
if data is None:
    print("Data is currently None.")

data = "Loaded"
if data is not None:
    print("Data is now available:", data)
print()

# ----------------------------------------------------------
# 🧩 4. Use None in a conditional statement
# ----------------------------------------------------------
optional_value = None

print("📍 None in a conditional context:")
if not optional_value:  # None evaluates to False
    print("This runs because None is falsy.")
else:
    print("This will not run.")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - NoneType has only one value: None
# - Functions without return automatically return None
# - Use None as a placeholder before assigning a real value
# - Always compare with 'is' or 'is not' (not == or !=)
# - None evaluates to False in conditions
