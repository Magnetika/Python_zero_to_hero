users = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com"},
    {"id": 3, "first_name": "Alice", "last_name": "Johnson", "email": "alice.johnson@example.com"},
    {"id": 4, "first_name": "Bob", "last_name": "Brown", "email": "bob.brown@example.com"}
]

# ----------------------------------------------------------
# READ helper function
# ----------------------------------------------------------
def find_user(id):
    for user in users:
        if user["id"] == id:
            return user
    return None


# ----------------------------------------------------------
# DELETE user by id
# ----------------------------------------------------------
def remove_user(id):
    user = find_user(id)
    if user is not None:
        users.remove(user)       # remove dictionary from list
        return True              # indicate success
    return False                 # delete failed (id not found)


# ----------------------------------------------------------
# DEMO
# ----------------------------------------------------------
print(find_user(3))  # Should return user #3
print(find_user(5))  # Should return None

remove_user(2)       # Remove user with ID 2
print(find_user(2))  # Should now be None
print(users)         # See remaining user list
