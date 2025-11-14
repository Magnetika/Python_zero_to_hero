"""
name_conflict.py
Demonstrates how module name conflicts occur and how to resolve them.
Shows how standard library modules and custom modules can be confused
if naming is not handled carefully.
"""

# Importing the real built-in Python math module
import math

# Importing our custom module — be sure the file is named matematica.py
# This simulates a name collision risk if the custom module had been named "math.py"
import mathematical

# Getting standard library module names to inspect potential conflicts
from sys import stdlib_module_names

# Print value from the standard math module
print("math.pi from standard library:", math.pi)

# Print value from the custom matematica module
print("pi from custom matematica module:", mathematical.pi)

# Show the list of standard library modules
print("Standard library module names:")
print(stdlib_module_names)

# Example: showing how aliasing can avoid name conflicts
import mathematical as custom_math

print("Accessing custom module via alias:", custom_math.pi)
