numbers = {1, 2, 3, 4, 5}

for i in numbers:
    print(i)

for i, v in enumerate(numbers):
    print(f"Index: {i}, Value: {v}")
for v in sorted(numbers):
    print(v)
for v in sorted(numbers, reverse=True):
    print(v)
for v in sorted(numbers, key=lambda x: -x):
    print(v)
for v in sorted(numbers, key=lambda x: x % 2):
    print(v)
for v in sorted(numbers, key=lambda x: (x % 2, x)):
    print(v)
for v in sorted(numbers, key=lambda x: (x % 2, -x)):
    print(v)

