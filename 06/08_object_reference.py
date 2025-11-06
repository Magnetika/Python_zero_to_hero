# 🎯 Lesson Objective:
# Understand how Python passes arguments to functions by object reference,
# what this means for mutable and immutable objects,
# and how it affects variable behavior inside and outside functions.

# ----------------------------------------------------------
# 🧩 1. Write a function that attempts to modify an immutable object
# ----------------------------------------------------------
def increase_counter(counter):
    """Tries to modify an immutable object (int)."""
    counter += 1  # creates a new object (rebinding)
    print("Inside function:", counter)

global_counter = 1
print("📍 Immutable object (int) example:")
increase_counter(global_counter)
print("Outside function:", global_counter)  # unchanged
print()

# ----------------------------------------------------------
# 🧩 2. Write a function that modifies a mutable object (list)
# ----------------------------------------------------------
def add_item_to_basket(item, basket):
    """Mutates a list by appending a new item."""
    basket.append(item)
    print("Inside function:", basket)

basket = ["VGA"]
print("📍 Mutable object (list) example:")
add_item_to_basket("CPU", basket)
print("Outside function:", basket)  # list is changed
print()

# ----------------------------------------------------------
# 🧩 3. Observe the difference between rebinding and mutation
# ----------------------------------------------------------
def reassign_list(lst):
    """Rebinds the local variable lst to a new list (does not affect original)."""
    lst = [0, 0, 0]  # new reference
    print("Inside (reassigned):", lst)

def mutate_list(lst):
    """Mutates the original list (affects the caller)."""
    lst[0] = 99
    print("Inside (mutated):", lst)

numbers = [1, 2, 3]
print("📍 Rebinding vs Mutation:")
reassign_list(numbers)
print("After reassign_list:", numbers)  # unchanged

mutate_list(numbers)
print("After mutate_list:", numbers)  # modified
print()

# ----------------------------------------------------------
# 🧩 4. Test with another immutable type (string)
# ----------------------------------------------------------
def modify_string(s):
    """Tries to modify an immutable string."""
    s += " world"  # creates a new string
    print("Inside function:", s)

greeting = "Hello"
print("📍 Immutable object (string) example:")
modify_string(greeting)
print("Outside function:", greeting)  # unchanged
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Python passes references to objects (not copies)
# - Immutable objects (int, str, tuple) cannot be changed inside a function
# - Mutable objects (list, dict, set) can be changed (mutated)
# - Rebinding (assigning a new object) does not affect the original
# - Mutation changes the same object that both references point to
