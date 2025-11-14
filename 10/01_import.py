# ======================================================================
# MODULE IMPORT EXAMPLES
# Demonstrates: full imports, partial imports, aliases, custom modules,
# built-in modules, dir(), and wildcard imports.
# ======================================================================


# -------------------------------------------------------------
# 1. Importing the entire module
# -------------------------------------------------------------
import math  # Import the built-in math module

print("=== Full module import ===")
print(math.pi)           # Accessing pi through the module
print(math.fabs(-120))   # Using absolute value function
print(math.sin(math.pi / 2))  # sin(90°) must be in radians


# -------------------------------------------------------------
# 2. Importing specific functions from a module
# -------------------------------------------------------------
from math import sqrt, ceil

print("\n=== Partial import ===")
print(sqrt(16))   # Only sqrt is available
print(ceil(3.14)) # Only ceil is available


# -------------------------------------------------------------
# 3. Importing everything (NOT recommended)
# -------------------------------------------------------------
from math import *

print("\n=== Wildcard import (not recommended) ===")
print(pi)                     # pi works because everything was imported
print(fabs(-120))             # Same as math.fabs()
print(sin(90))                # sin(90 radians) – just a demonstration
print(dir())                  # List all names in the current scope


# -------------------------------------------------------------
# 4. Using aliases with modules and functions
# -------------------------------------------------------------
import math as m          # Renaming module
from math import sqrt as square_root  # Renaming function

print("\n=== Aliases ===")
print(m.pow(2, 3))        # Using alias 'm' instead of 'math'
print(square_root(25))    # Using alias for sqrt()


# -------------------------------------------------------------
# 5. Importing and using a custom module
#    (Assume you have a file named greetings.py in the same directory)
#
#    greetings.py:
#    ----------------
#    def hello(name):
#        return f\"Hello, {name}!\"
#
# -------------------------------------------------------------
try:
    import greetings  # Custom module (must exist in the same folder)

    print("\n=== Custom module import ===")
    print(greetings.hello("Alice"))

except ModuleNotFoundError:
    print("\n[INFO] Custom module 'greetings.py' not found.")
    print("Create a file named greetings.py with a hello() function to test.")


# -------------------------------------------------------------
# 6. Checking module contents using dir()
# -------------------------------------------------------------
print("\n=== Directory listing of math module ===")
print(dir(math))  # Shows all attributes inside the math module


# -------------------------------------------------------------
# 7. Simple demonstration of how modules are imported only once
# -------------------------------------------------------------
print("\n=== Import test ===")

import math
print("Math imported again, but Python loads it only once internally.")
