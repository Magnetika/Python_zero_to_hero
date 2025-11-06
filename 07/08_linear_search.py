def linear_search(values, element):
    for i in range(len(values)):
        if values[i] == element:
            return i
    return -1

val = [10, 20, 30, 40, 50]
print(linear_search(val, 30))  # Output: 2
print(linear_search(val, 60))  # Output: -1

