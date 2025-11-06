# 🎯 Lesson Objective:
# Understand how functions return values using the return statement,
# how returned values can be stored and reused,
# and the difference between returning and printing.

# ----------------------------------------------------------
# 🧩 1. Create a function that returns a numeric result
# ----------------------------------------------------------
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add(3, 5)
print("📍 Returning a numeric result:")
print(f"3 + 5 = {result}")
print()

# ----------------------------------------------------------
# 🧩 2. Return multiple values and unpack them
# ----------------------------------------------------------
def get_min_max(numbers):
    """Return both the smallest and largest values from a list."""
    return min(numbers), max(numbers)

low, high = get_min_max([1, 5, 8, 0])
print("📍 Returning multiple values (unpacking):")
print(f"Lowest: {low}, Highest: {high}")
print()

# ----------------------------------------------------------
# 🧩 3. Compare return vs print() behavior
# ----------------------------------------------------------
def show_sum(a, b):
    """Prints the sum but does not return it."""
    print("Sum is:", a + b)

def return_sum(a, b):
    """Returns the sum for later use."""
    return a + b

print("📍 Return vs Print comparison:")
x = show_sum(3, 4)   # Prints, but returns None
y = return_sum(3, 4) # Returns 7

print("Value stored in x (print version):", x)
print("Value stored in y (return version):", y)
print()

# ----------------------------------------------------------
# 🧩 4. Observe what happens when no return is used
# ----------------------------------------------------------
def show_message():
    print("Hello!")

print("📍 Function without explicit return:")
print(show_message())  # Prints 'Hello!' and then None
print()

# ----------------------------------------------------------
# 🧩 5. Your example: returning based on a condition
# ----------------------------------------------------------
def even_or_odd(number):
    """Return 'Even' if the number is even, 'Odd' if the number is odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("📍 Function return examples:")
print("4 is", even_or_odd(4))
print("7 is", even_or_odd(7))
print("10 is", even_or_odd(10))
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - `return` sends data back to the caller for reuse
# - `print` only displays output on screen
# - Functions without `return` automatically return `None`
# - You can return multiple values (as tuples)
# - Use return for reusable and testable code
