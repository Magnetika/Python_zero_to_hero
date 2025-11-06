def summa(values):
 sum_value = 0  # accumulator
 for i in values:
    sum_value += i  # accumulate values
 return sum_value

def average(values):
    return summa(values) / len(values) if values else 0

val = [10, 20, 30, 40, 50]
print("📍 Average of list:", average(val))  # Output: 30.0

