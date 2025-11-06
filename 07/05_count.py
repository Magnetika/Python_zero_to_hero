def count_value(vales, search):
    counter = 0
    for i in vales:
        if i == search:
            counter += 1
    return counter

val = [ 10, 20, 30, 10, 10, 40, 50 ]
print(count_value(val, 10))  # Output: 3
print(count_value(val, 20))  # Output: 1
print(count_value(val, 60))  # Output: 0
