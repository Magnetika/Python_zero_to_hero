# 🎯 Lesson Objective:
# Learn how to use dictionary unpacking and dictionary comprehensions
# to merge, filter, and transform data in a concise and readable way.

# ----------------------------------------------------------
# 🧩 1. Dictionary unpacking (**)
# ----------------------------------------------------------
dict_a = {"name": "Alice", "age": 25}
dict_b = {"city": "Budapest", "grade": 4.8}

combined = {**dict_a, **dict_b}
print("📍 Merged with ** unpacking:")
print(combined)
print()

# If both have the same key → rightmost wins
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}
merged = {**a, **b}
print("📍 Key conflict (rightmost wins):")
print(merged)
print()

# ----------------------------------------------------------
# 🧩 2. Unpacking in function calls
# ----------------------------------------------------------
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

person = {"name": "Bob", "age": 30}
print("📍 Unpacking dict in function call:")
greet(**person)
print()

# ----------------------------------------------------------
# 🧩 3. Simple dictionary comprehension
# ----------------------------------------------------------
squares = {x: x**2 for x in range(5)}
print("📍 Dictionary comprehension (squares):")
print(squares)
print()

# ----------------------------------------------------------
# 🧩 4. Dictionary comprehension with condition
# ----------------------------------------------------------
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("📍 Comprehension with filtering (even squares):")
print(even_squares)
print()

# ----------------------------------------------------------
# 🧩 5. Transforming existing dictionaries
# ----------------------------------------------------------
student = {"name": "Alice", "grade": 4.8, "age": 25}
uppercase_keys = {k.upper(): v for k, v in student.items()}
print("📍 Transforming keys (to uppercase):")
print(uppercase_keys)
print()

# Modify values (e.g., increase by 10%)
adjusted = {k: v * 1.1 for k, v in {"A": 10, "B": 20, "C": 30}.items()}
print("📍 Transforming values (increase by 10%):")
print(adjusted)
print()

# ----------------------------------------------------------
# 🧩 6. Nested dictionary comprehension
# ----------------------------------------------------------
pairs = {(x, y): x * y for x in range(2) for y in range(3)}
print("📍 Nested comprehension (pairs → products):")
print(pairs)
print()

# ----------------------------------------------------------
# 🧩 7. Real-world use example – net/gross price calculation
# ----------------------------------------------------------
cart_net_prices = {'VGA': 1000, 'CPU': 500, 'Monitor': 300}
cart_gross_prices = {item: price * 1.27 for item, price in cart_net_prices.items()}

print("📍 Gross price calculation using comprehension:")
print(cart_gross_prices)
print()

# ----------------------------------------------------------
# 🧩 8. Proper unpacking examples
# ----------------------------------------------------------
user = {'name': 'Alice', 'age': 30, 'job': 'Engineer'}

# Extracting keys
name_key, age_key, job_key = user
print("📍 Unpacking keys:")
print(name_key, age_key, job_key)  # name age job
print()

# Extracting values
name_val, age_val, job_val = user.values()
print("📍 Unpacking values:")
print(name_val, age_val, job_val)  # Alice 30 Engineer
print()

# Extracting key-value pairs (as tuples)
items = list(user.items())
print("📍 Unpacking items (key-value pairs):")
print(items[0], items[1], items[2])  # ('name', 'Alice') ('age', 30) ('job', 'Engineer')
print()

# ----------------------------------------------------------
# ✅ Key Takeaways
# ----------------------------------------------------------
# ✔ {**a, **b} merges dictionaries → rightmost overwrites duplicates
# ✔ ** can also unpack dictionaries into function keyword arguments
# ✔ Dictionary comprehensions build or transform dicts in one line
# ✔ Use conditions to filter, and expressions to transform data
# ✔ Useful in data transformation, filtering, and merging tasks
