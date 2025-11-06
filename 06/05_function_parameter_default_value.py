# 🎯 Lesson Objective:
# Learn how to define functions with default parameter values,
# understand how they work, and explore common use cases and potential pitfalls.

# ----------------------------------------------------------
# 🧩 1. Create a function with one default parameter
# ----------------------------------------------------------
def greet(name="Guest"):
    """Greets a user by name or as 'Guest' if no name is given."""
    print(f"Hello, {name}!")

print("📍 One default parameter:")
greet()
greet("Alice")
print()

# ----------------------------------------------------------
# 🧩 2. Create a function with multiple default parameters
# ----------------------------------------------------------
def calculate_gross_price(price, vat_percent=27, currency="HUF"):
    """Returns the gross price after adding VAT."""
    return price * (1 + vat_percent / 100), currency

print("📍 Multiple default parameters:")
print(calculate_gross_price(2000))        # uses default 27% VAT
print(calculate_gross_price(2000, 5))     # custom VAT
print(calculate_gross_price(2000, 10, "EUR"))
print()

# ----------------------------------------------------------
# 🧩 3. Demonstrate how argument order affects calls
# ----------------------------------------------------------
def describe_trip(destination, days=7, transport="car"):
    print(f"Trip to {destination} for {days} days by {transport}.")

print("📍 Positional and keyword argument order:")
describe_trip("Paris")                                # default days and transport
describe_trip("Rome", 5)                              # overrides days
describe_trip("Berlin", transport="train", days=3)    # keyword arguments (order flexible)
print()

# ----------------------------------------------------------
# 🧩 4. Test what happens with mutable default parameters
# ----------------------------------------------------------
# ⚠️ Wrong way – mutable default list reused between calls
def add_item_wrong(item, items=[]):
    items.append(item)
    return items

print("📍 Mutable default pitfall (wrong approach):")
print(add_item_wrong("apple"))   # ['apple']
print(add_item_wrong("banana"))  # ['apple', 'banana'] ❌ unexpected behavior
print()

# ✅ Correct way – use None to avoid reusing the same list
def add_item_to_basket(item, basket=None):
    if basket is None:
        basket = []  # creates a new list each time
    basket.append(item)
    return basket

print("📍 Correct handling of mutable defaults:")
print(add_item_to_basket("apple"))
print(add_item_to_basket("banana"))
print(add_item_to_basket("orange"))
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Default parameters make arguments optional
# - Defaults must come *after* required parameters
# - Use keyword arguments for clarity
# - Avoid mutable default values (like lists or dicts)
# - Use `None` as a safe default and create a new object inside
