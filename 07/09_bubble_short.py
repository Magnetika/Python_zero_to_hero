# 🎯 Lesson Objective:
# Understand and implement the bubble sort algorithm,
# a simple comparison-based sorting method that repeatedly swaps
# adjacent elements if they are in the wrong order.

# ----------------------------------------------------------
# 🧩 1. Implement a basic bubble sort manually
# ----------------------------------------------------------
def bubble_sort(values):
    """Basic bubble sort implementation (ascending order)."""
    n = len(values)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    return values

val = [-2, 45, 0, 11, -9]
print("📍 Basic Bubble Sort:")
print("Original list:", val)
print("Sorted list:", bubble_sort(val.copy()))
print()

# ----------------------------------------------------------
# 🧩 2. Optimize using the “swapped” flag (early stop)
# ----------------------------------------------------------
def bubble_sort_optimized(values):
    """Optimized bubble sort that stops early if no swaps occur."""
    n = len(values)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break  # already sorted
    return values

numbers = [5, 2, 9, 1, 5, 6]
print("📍 Optimized Bubble Sort (early stop):")
print("Original:", numbers)
print("Sorted:", bubble_sort_optimized(numbers.copy()))
print()

# ----------------------------------------------------------
# 🧩 3. Sort a list in descending order (reverse logic)
# ----------------------------------------------------------
def bubble_sort_descending(values):
    """Bubble sort that sorts elements in descending order."""
    n = len(values)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if values[j] < values[j + 1]:  # reverse condition
                values[j], values[j + 1] = values[j + 1], values[j]
    return values

val = [3, 1, 4, 1, 5, 9]
print("📍 Bubble Sort (descending):")
print("Original:", val)
print("Sorted descending:", bubble_sort_descending(val.copy()))
print()

# ----------------------------------------------------------
# 🧩 4. Count the number of swaps made during sorting
# ----------------------------------------------------------
def bubble_sort_with_count(values):
    """Bubble sort that counts the number of swaps."""
    n = len(values)
    swap_count = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swap_count += 1
    return values, swap_count

val = [64, 34, 25, 12, 22, 11, 90]
sorted_list, swaps = bubble_sort_with_count(val.copy())
print("📍 Bubble Sort with Swap Counter:")
print("Original list:", val)
print("Sorted list:", sorted_list)
print("Total swaps:", swaps)
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Bubble sort repeatedly swaps adjacent elements if they’re out of order.
# - After each pass, the largest unsorted element “bubbles” to the end.
# - Time Complexity:
#     Best   → O(n)   (already sorted, optimized)
#     Average/Worst → O(n²)
# - Space Complexity: O(1) (in-place)
# - Pros: simple, easy to understand
# - Cons: inefficient for large lists
# - Optimization: use a `swapped` flag to stop early when no swaps occur.
