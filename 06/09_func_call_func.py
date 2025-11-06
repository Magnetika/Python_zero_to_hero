# 🎯 Lesson Objective:
# Learn how to call one function from within another,
# understand how control flow moves between functions,
# and see how this helps organize and reuse code effectively.

# ----------------------------------------------------------
# 🧩 1. Create two functions where one calls the other
# ----------------------------------------------------------
def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

def welcome_user():
    """Calls greet() from inside to welcome a specific user."""
    user = "Alice"
    print("Inside welcome_user()")
    greet(user)
    print("End of welcome_user()")

print("📍 Function calling another function:")
welcome_user()
print()

# ----------------------------------------------------------
# 🧩 2. Return a value from one function and use it in another
# ----------------------------------------------------------
def add(a, b):
    """Returns the sum of two numbers."""
    print(f"Adding {a} + {b}")
    return a + b

def display_sum(x, y):
    """Calls add() and prints the result."""
    print("Inside display_sum()")
    total = add(x, y)
    print("Sum is:", total)
    print("End of display_sum()")

print("📍 Returning value between functions:")
display_sum(3, 5)
print()

# ----------------------------------------------------------
# 🧩 3. Trace execution order using print() statements
# ----------------------------------------------------------
def a():
    print("Start A")
    b()
    print("End A")

def b():
    print("Inside B")

print("📍 Tracing execution flow:")
a()
print()

# ----------------------------------------------------------
# 🧩 4. Write a nested call chain (A → B → C)
# ----------------------------------------------------------
def function_a():
    print("Start A")
    function_b()
    print("End A")

def function_b():
    print("  Start B")
    function_c()
    print("  End B")

def function_c():
    print("    Inside C")

print("📍 Nested call chain (A → B → C):")
function_a()
print()

# ----------------------------------------------------------
# 🧩 5. Practical Example – price calculation chain
# ----------------------------------------------------------
def calculate_gross_price(price, vat_percent):
    """Adds VAT to a given price."""
    print(f"Applying VAT ({vat_percent}%) to {price}")
    return price * (1 + vat_percent / 100)

def apply_discount(price, discount_percent):
    """Applies discount to the given price."""
    print(f"Applying discount ({discount_percent}%) to {price}")
    return price * (1 - discount_percent / 100)

def calculate_final_price(price, vat_percent=27, discount_percent=0):
    """Calculates final price with optional discount and VAT."""
    print("Starting final price calculation...")
    discounted = apply_discount(price, discount_percent) if discount_percent > 0 else price
    gross = calculate_gross_price(discounted, vat_percent)
    print("Calculation complete.")
    return gross

print("📍 Function chaining example with return values:")
print("Final price (no discount):", calculate_final_price(1000))
print()
print("Final price (with discount):", calculate_final_price(1000, 5, 10))
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Functions can call each other to reuse logic
# - Execution "jumps" into the called function and returns after it finishes
# - Returned values can be passed between functions
# - Use print() to trace control flow (helpful for debugging)
# - Modular functions improve code organization and reusability
