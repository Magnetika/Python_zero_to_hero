"""
custommodule.py
A simple custom-made Python module.
Contains a constant (PI) and a function (greeting).
This module will demonstrate how imports and __main__ work.
"""

# A constant value inside the module
PI = 3.14


def greeting(name):
    """Prints a friendly greeting."""
    print(f"Hello, {name}!")


# ---------------------------------------------------------
# __main__ block inside the module
# This only executes if you run:
#     python custommodule.py
# It DOES NOT execute when imported into another script.
# ---------------------------------------------------------
if __name__ == "__main__":
    print("custommodule.py is running directly.")
    greeting("Alice")
    print("PI =", PI)
    print("This module's __name__:", __name__)
else:
    print("custommodule.py was imported into another file.")
