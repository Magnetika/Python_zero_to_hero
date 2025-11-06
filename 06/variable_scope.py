# 🎯 Lesson Objective:
# Understand the concept of variable scope in Python,
# learn the difference between local and global variables,
# and recognize how scope affects variable accessibility and lifetime.

# ----------------------------------------------------------
# 🧩 1. Define and access a local variable
# ----------------------------------------------------------
def show_local_scope():
    message = "I'm a local variable!"  # local scope
    print("Inside function:", message)

print("📍 Local variable example:")
show_local_scope()
# print(message)  # ❌ Error: 'message' is not defined (local only)
print()

# ----------------------------------------------------------
# 🧩 2. Access a global variable from a function
# ----------------------------------------------------------
price = 1000
vat_percent = 27
gross_price = 0

def show_global_access():
    print("Accessing global variable inside function:")
    print(f"Price = {price}, VAT = {vat_percent}%")

print("📍 Accessing global variables:")
show_global_access()
print(f"Outside function: price = {price}")
print()

# ----------------------------------------------------------
# 🧩 3. Modify a global variable using 'global'
# ----------------------------------------------------------
def calculate_gross_price():
    global gross_price
    print("Before calculation:", gross_price)
    gross_price = price * (1 + vat_percent / 100)
    print("After calculation:", gross_price)

print("📍 Modifying global variable:")
calculate_gross_price()
print("Outside function, gross_price =", gross_price)
print()

# ----------------------------------------------------------
# 🧩 4. Experiment with variable name shadowing
# ----------------------------------------------------------
x = "global x"

def shadow_example():
    x = "local x"  # shadows the global x
    print("Inside function:", x)

print("📍 Variable shadowing:")
shadow_example()
print("Outside function:", x)  # global value remains unchanged
print()

# ----------------------------------------------------------
# 🧩 5. Explore the LEGB scope rule using nested functions
# ----------------------------------------------------------
def outer_function():
    message = "enclosing message"  # Enclosing scope

    def inner_function():
        local_message = "local message"  # Local scope
        print("Inner:", local_message)
        print("Accessing enclosing variable:", message)  # from outer_function

    inner_function()

print("📍 LEGB rule example (Local → Enclosing → Global → Built-in):")
outer_function()
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Local variables exist only inside functions
# - Global variables exist for the program’s lifetime
# - Use 'global' keyword to modify a global variable in a function
# - Variable shadowing happens when a local name hides a global one
# - LEGB rule defines Python’s scope lookup order:
#   Local → Enclosing → Global → Built-in
