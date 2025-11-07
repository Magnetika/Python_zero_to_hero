user = {
    "name": "Alice Smith",
    "age": 30,
}

print(type(user))  # Output: <class 'dict'>

duplicated = {'name': 'Alice Smith', 'name': 'Bob Johnson'}
print(duplicated)  # Output: {'name': 'Bob Johnson'}

print(user["name"])  # Output: Alice Smith

user['name'] = 'Bob Johnson'
print(user['name'])  # Output: Bob Johnson

user['job'] = 'Engineer'
print(user)  # Output: {'name': 'Bob Johnson', 'age': 30, 'job': 'Engineer'}

user.update({'age': 31, 'city': 'New York', 'hobby': 'Photography'})
print(user)  # Output: {'name': 'Bob Johnson', 'age': 31, 'job': 'Engineer', 'city': 'New York', 'hobby': 'Photography'}

user.pop('hobby')
print(user)  # Output: {'name': 'Bob Johnson', 'age': 31, 'job': 'Engineer', 'city': 'New York'}

