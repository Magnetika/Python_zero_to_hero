# 🎯 Lesson Objective:
# Learn how to define and call functions with multiple parameters,
# understand the importance of argument order,
# and differentiate between parameters and arguments.

# ----------------------------------------------------------
# 🧩 1. Define a function with three parameters
# ----------------------------------------------------------
def describe_person(name, age, city):
    """Prints a description of a person."""
    print(f"{name} is {age} years old and lives in {city}.")

print("📍 Function with three parameters:")
describe_person("Alice", 25, "London")
print()

# ----------------------------------------------------------
# 🧩 2. Call it with positional arguments in the correct order
# ----------------------------------------------------------
print("📍 Correct positional argument order:")
describe_person("Bob", 30, "Paris")
print()

# ----------------------------------------------------------
# 🧩 3. Reorder the arguments to see the effect (logical error)
# ----------------------------------------------------------
print("📍 Incorrect argument order (logical mistake):")
describe_person("Paris", 30, "Bob")  # Still runs, but makes no sense
print()

# ----------------------------------------------------------
# 🧩 4. Use keyword arguments to make the call clearer
# ----------------------------------------------------------
print("📍 Using keyword arguments (order no longer matters):")
describe_person(age=28, city="Berlin", name="Clara")
print()

# ----------------------------------------------------------
# 🧩 5. Bonus Example – Practical function with multiple parameters
# ----------------------------------------------------------
def calculate_gross_price(price, vat_percent, currency="HUF"):
    """Return the gross price after adding VAT."""
    return price * (1 + vat_percent / 100), currency

print("📍 Practical example with multiple parameters:")
gross_huf, cur = calculate_gross_price(1000, 27)
print(f"Gross price: {gross_huf} {cur}")

# Wrong order example (logical error):
gross_wrong, _ = calculate_gross_price(27, 1000)
print("Wrong order result:", gross_wrong, cur)
print()

# Uncommenting this would raise an error (missing argument)
# print(calculate_gross_price(1000))  # TypeError
print("📍 Note: Missing arguments cause TypeError.")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Parameters: names in the function definition
# - Arguments: actual values you pass when calling
# - Positional arguments → order matters!
# - Keyword arguments → order doesn't matter
# - Missing required arguments → TypeError
