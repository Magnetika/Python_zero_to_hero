# ======================================================================
# Reusable CRUD Operations for Dictionaries
# Fully commented and structured in one complete Python file
# ======================================================================


# -------------------------------------------------------------
# CREATE operation
# -------------------------------------------------------------
def create_entry(data, key, value):
    """
    Create a new key-value pair in the dictionary.
    If the key already exists, the function will NOT overwrite it.
    """
    if key not in data:
        data[key] = value
        print(f"[CREATE] Added: {key} = {value}")
    else:
        print(f"[CREATE] Key '{key}' already exists. Nothing was added.")


# -------------------------------------------------------------
# READ operation
# -------------------------------------------------------------
def read_entry(data, key):
    """
    Read (retrieve) a value from the dictionary.
    Returns the value if the key exists, otherwise returns 'Key not found'.
    """
    return data.get(key, "Key not found")


# -------------------------------------------------------------
# UPDATE operation
# -------------------------------------------------------------
def update_entry(data, key, value):
    """
    Update an existing key or create it if it does not exist.
    This makes update() useful for both modifying and adding data.
    """
    data[key] = value
    print(f"[UPDATE] {key} updated to: {value}")


# -------------------------------------------------------------
# DELETE operation
# -------------------------------------------------------------
def delete_entry(data, key):
    """
    Delete a key-value pair from the dictionary.
    If the key does not exist, nothing happens.
    """
    if key in data:
        del data[key]
        print(f"[DELETE] Removed key: {key}")
    else:
        print(f"[DELETE] Key '{key}' not found. Nothing was removed.")


# ======================================================================
# Optional: Generic CRUD handler in a single function
# ======================================================================
def crud_action(data, action, key=None, value=None):
    """
    Perform a CRUD action using a single function.
    Supported actions: create, read, update, delete.
    """
    if action == "create":
        return create_entry(data, key, value)
    elif action == "read":
        return read_entry(data, key)
    elif action == "update":
        return update_entry(data, key, value)
    elif action == "delete":
        return delete_entry(data, key)
    else:
        print("[ERROR] Unknown CRUD action:", action)


# ======================================================================
# CRUD Class Version (OOP)
# ======================================================================
class CRUDManager:
    """
    A reusable class that manages CRUD operations on an internal dictionary.
    """

    def __init__(self):
        self.data = {}

    def create(self, key, value):
        """Add a new key-value pair only if the key does not already exist."""
        if key not in self.data:
            self.data[key] = value
            print(f"[CREATE] Added {key}: {value}")
        else:
            print(f"[CREATE] '{key}' already exists.")

    def read(self, key):
        """Retrieve the value associated with the key."""
        return self.data.get(key, "Key not found")

    def update(self, key, value):
        """Change or add the key-value pair."""
        self.data[key] = value
        print(f"[UPDATE] {key} = {value}")

    def delete(self, key):
        """Remove the key if it exists."""
        removed = self.data.pop(key, None)
        if removed is not None:
            print(f"[DELETE] Removed {key}")
        else:
            print(f"[DELETE] '{key}' not found.")


# ======================================================================
# DEMO OF ALL CRUD FEATURES
# ======================================================================
if __name__ == "__main__":
    print("\n========== SIMPLE CRUD FUNCTION DEMO ==========\n")

    student = {}

    # CREATE
    create_entry(student, "name", "Alice")
    create_entry(student, "age", 22)
    create_entry(student, "name", "Duplicate")  # will not overwrite

    # READ
    print("[READ]", read_entry(student, "name"))
    print("[READ]", read_entry(student, "grade"))  # not found

    # UPDATE
    update_entry(student, "grade", 4.8)
    update_entry(student, "age", 23)

    # DELETE
    delete_entry(student, "age")
    delete_entry(student, "unknown")

    print("\nStudent dictionary:", student)

    print("\n========== CRUD ACTION HANDLER DEMO ==========\n")

    users = {}

    crud_action(users, "create", "admin", "active")
    crud_action(users, "update", "admin", "inactive")
    print("[READ]", crud_action(users, "read", "admin"))
    crud_action(users, "delete", "admin")

    print("Users dictionary:", users)

    print("\n========== CRUD MANAGER CLASS DEMO ==========\n")

    manager = CRUDManager()
    manager.create("user", "Alice")
    manager.update("user", "Bob")
    print("[READ]", manager.read("user"))
    manager.delete("user")

    print("Manager data:", manager.data)
