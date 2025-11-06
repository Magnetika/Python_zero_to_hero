# 🎯 Lesson Objective:
# Understand the concept of recursion, how a function can call itself,
# how to define base and recursive cases, and when recursion is useful.

# ----------------------------------------------------------
# 🧩 1. Write a simple recursive function with a base case
# ----------------------------------------------------------
def countdown(n):
    """Counts down recursively to 0."""
    if n <= 0:  # base case
        print("Go!")
    else:        # recursive case
        print(n)
        countdown(n - 1)

print("📍 Simple recursion example (countdown):")
countdown(5)
print()

# ----------------------------------------------------------
# 🧩 2. Implement a recursive factorial function
# ----------------------------------------------------------
def factorial(n):
    """Calculates factorial recursively."""
    if n == 1:  # base case
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) = {n} * factorial({n-1}) → {result}")
        return result

print("📍 Recursive factorial example:")
print("5! =", factorial(5))
print()

# ----------------------------------------------------------
# 🧩 3. Compare recursion vs loop for the same problem (GCD)
# ----------------------------------------------------------
def gcd_loop(a, b):
    """Finds GCD using an iterative approach."""
    print("Iterative GCD steps:")
    while b:
        print(f"a={a}, b={b} → a % b = {a % b}")
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    """Finds GCD using recursion."""
    print(f"Recursive call: gcd({a}, {b})")
    if b == 0:  # base case
        print(f"Base case reached → return {a}")
        return a
    return gcd_recursive(b, a % b)

print("📍 Iteration vs Recursion comparison (GCD):")
print("Loop result:", gcd_loop(3, 33))
print("Recursive result:", gcd_recursive(3, 33))
print()

# ----------------------------------------------------------
# 🧩 4. Observe the stack unwinding process
# ----------------------------------------------------------
def fibonacci(n):
    """Shows recursion depth using Fibonacci sequence."""
    print(f"Calculating fibonacci({n})")
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("📍 Stack unwinding demonstration (Fibonacci):")
print("fibonacci(4) =", fibonacci(4))
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Recursion = function calling itself
# - Must have a base case to stop recursion
# - Recursive case reduces the problem
# - Each call adds a frame to the call stack
# - Stack unwinds as base cases are resolved
# - Recursion vs Iteration:
#     → Recursion: elegant, expressive
#     → Iteration: usually faster and uses less memory
