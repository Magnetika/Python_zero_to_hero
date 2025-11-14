# Users list (acts as a simple in-memory database)
users = [
    {"id": 1, "first_name": "John",  "last_name": "Doe",    "email": "john.doe@example.com"},
    {"id": 2, "first_name": "Jane",  "last_name": "Smith",  "email": "jane.smith@example.com"},
    {"id": 3, "first_name": "Alice", "last_name": "Johnson","email": "alice.johnson@example.com"},
    {"id": 4, "first_name": "Bob",   "last_name": "Brown",  "email": "bob.brown@example.com"}
]

def update_user(user_id, first_name=None, last_name=None, email=None):
    """
    Update an existing user.
    Only the fields that are provided (not None) will be updated.
    If the user is not found, the function returns None.
    """

    # Iterate through the users list
    for user in users:

        # Check if we found the user with the matching id
        if user["id"] == user_id:

            # Update fields only if arguments were provided
            if first_name is not None:
                user["first_name"] = first_name

            if last_name is not None:
                user["last_name"] = last_name

            if email is not None:
                user["email"] = email

            # Return the updated user
            return user

    # If no matching user found, return None
    return None


# --- Testing ---
print(update_user(3, first_name="Alicia"))            # Update existing user
print(update_user(4, email="bob.new@example.com"))    # Update another field
print(update_user(10, first_name="Ghost"))            # User not found → No
