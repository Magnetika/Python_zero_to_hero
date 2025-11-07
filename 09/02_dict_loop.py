user = {"name": "Alice Smith", "age": 30, "job": "Engineer"}
    
for i in user:
    print(f'key: {i}, value: {user[i]}')

#for i in range(len(user)):
#    key = list(user.keys())[i]
#    value = user[key]
#    print(f'key: {key}, value: {value}')

for i, v in enumerate(user.items()):
    print(f'index: {i}, value: {v}')