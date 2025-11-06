def even_or_odd(number):
    """Return 'Even' if the number is even, 'Odd' if the number is odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("📍 Function return examples:")
print("4 is", even_or_odd(4))
print("7 is", even_or_odd(7))
print("10 is", even_or_odd(10))
print()