def is_contains(values, search):
    for i in values:
        if i == search:
            return True
    return False

val = [10, 20, 30, 40, 50]
print(is_contains(val, 30))  
print(is_contains(val, 60))  