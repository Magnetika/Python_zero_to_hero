def bubble_sort(values):
    for i in range(len(values)):
        for j in range(0, len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    return values

val = [-2, 45, 0, 11, -9]
print(bubble_sort(val))
