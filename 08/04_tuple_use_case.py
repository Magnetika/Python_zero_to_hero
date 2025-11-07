location = (35.6895, 139.6917) 
rgb_color = (255, 0, 0)

def user_factory(first_name, last_name, age):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    age = int(age)
    return (first_name, last_name, age)

print(user_factory("john", "doe", "30"))  # Output: ('John', 'Doe', 30)
print(location)  # Output: (35.6895, 139.6917)
print(rgb_color)  # Output: (255, 0, 0)
