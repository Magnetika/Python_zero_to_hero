age = 39
age_copy = age

print('age', age)
print('age_copy', age_copy)
print('age memory address', id(age))
print('age_copy memory address', id(age_copy))
print('---')
age += 1
print('age', age)
print('age_copy', age_copy) 
print('age memory address', id(age))
print('age_copy memory address', id(age_copy))
print('---')
name = "John"       
name_copy = name
print('name', name)
print('name_copy', name_copy)
print('name memory address', id(name))
print('name_copy memory address', id(name_copy))
print('---')
name += " Doe"
print('name', name)
print('name_copy', name_copy)
print('name memory address', id(name))
print('name_copy memory address', id(name_copy))
print('---')

