users = [{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
},
{
    "id": 2, 
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com"
},
{
    "id": 3,
    "first_name": "Alice",
    "last_name": "Johnson",
    "email": "alice.johnson@example.com"
},
{
    "id": 4,
    "first_name": "Bob",
    "last_name": "Brown",
    "email": "bob.brown@example.com"
}]  

def find_user(id):
    for i in users:
        if i['id'] == id:
            return i
    return None

print(find_user(3))  # Should return the user with id 3 
print(find_user(5))  # Should return None since user with id 5 does not exist
