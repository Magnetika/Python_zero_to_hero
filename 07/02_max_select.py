def get_maximum(values):
    max_value = values[0]
    for i in range(1, len(values)):
        if values[i] > max_value:
            max_value = values[i]
    return max_value
# Example usage
val = [10, 20, 30, 40, 50]
print(get_maximum(val))  # Output: 50
# This function iterates through a list of values and returns the maximum value found.
