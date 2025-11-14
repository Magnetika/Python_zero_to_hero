# Existing users list (this simulates a simple in-memory database)
users = [
    {"id": 1, "first_name": "John",  "last_name": "Doe",    "email": "john.doe@example.com"},
    {"id": 2, "first_name": "Jane",  "last_name": "Smith",  "email": "jane.smith@example.com"},
    {"id": 3, "first_name": "Alice", "last_name": "Johnson","email": "alice.johnson@example.com"},
    {"id": 4, "first_name": "Bob",   "last_name": "Brown",  "email": "bob.brown@example.com"}
]

def create_user(first_name, last_name, email):
    """
    Create a new user dictionary and add it to the users list.
    Automatically generates the next available ID.
    Returns the newly created user.
    """

    # Generate a new ID (max existing ID + 1)
    # If the users list is empty, start from 1
    new_id = max(user["id"] for user in users) + 1 if users else 1

    # Create the new user dictionary
    new_user = {
        "id": new_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }

    # Add it to the users list (our database)
    users.append(new_user)

    # Return the newly created user
    return new_user


# --- Testing the Create function ---
print(create_user("Daniel", "Green", "daniel.green@example.com"))
print(create_user("Laura", "White", "laura.white@example.com"))

# Check results (last two users)
for user in users[-2:]:
    print(user)
