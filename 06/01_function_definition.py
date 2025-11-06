# 🎯 Lesson Objective:
# Learn how to define custom functions in Python,
# use parameters and arguments effectively,
# and explore common built-in functions.

# ----------------------------------------------------------
# 🧩 1. Create a simple function with no parameters
# ----------------------------------------------------------
def say_hello():
    """Prints a simple greeting message."""
    print("Hello, world!")

print("📍 Function with no parameters:")
say_hello()
print()

# ----------------------------------------------------------
# 🧩 2. Create a function with parameters and return a result
# ----------------------------------------------------------
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(3, 5)
print("📍 Function with parameters and return value:")
print(f"3 + 5 = {result}")
print()

# Another example – your greeting function:
def greeting(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")

print("📍 Greeting function:")
greeting("Alice")
greeting("Bob")
greeting("Charlie")
print()

# ----------------------------------------------------------
# 🧩 3. Use built-in functions on different data types
# ----------------------------------------------------------
numbers = [4, 8, 15, 16, 23, 42]
word = "Python"

print("📍 Built-in function examples:")
print("Length of list:", len(numbers))
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("Sum of numbers:", sum(numbers))
print("Type of variable 'word':", type(word))
print("Range example:", list(range(5)))
print()

# ----------------------------------------------------------
# 🧩 4. Practice naming and structuring functions clearly
# ----------------------------------------------------------
def calculate_average(scores):
    """Calculates the average of a list of numbers."""
    return sum(scores) / len(scores)

grades = [90, 80, 70, 100]
avg = calculate_average(grades)
print("📍 Custom function with clear naming:")
print(f"The average grade is: {avg}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Define functions with `def` keyword
# - Use parameters to pass input, and return for output
# - Built-in functions like len(), sum(), max(), type() are always available
# - Keep functions focused and well-named
# - Prefer `return` over `print` for reusable logic

# (Optional) To explore all built-in functions:
# print(dir(__builtins__))
# ----------------------------------------------------------