"""
mainmodule.py
Demonstrates how to import and use a custom Python module.
Shows how __name__ and __main__ work in practice.
"""

# Importing specific elements from the custom module
# This way we don't need to type: custommodule.PI or custommodule.greeting()
from custommodule import PI, greeting


# ---------------------------------------------------------
# __main__ block – code here only runs when this file is
# executed directly (python mainmodule.py)
#
# It does NOT run when the file is imported from another file.
# ---------------------------------------------------------
if __name__ == "__main__":
    print("mainmodule.py is running as the main program.")

    # Calling the imported function
    greeting("Bob")

    # Printing the imported constant
    print("Value of PI:", PI)

    # Showing the current module name
    print("This module's __name__:", __name__)
else:
    # This will execute only when the module is imported
    print("mainmodule.py was imported, not run directly.")
