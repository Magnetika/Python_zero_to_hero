# 🎯 Lesson Objective:
# Understand how to optimize the bubble sort algorithm
# by reducing unnecessary iterations, detecting early completion,
# and minimizing comparisons.

# ----------------------------------------------------------
# 🧩 1. Improved Bubble Sort — Early Stop Optimization
# ----------------------------------------------------------
def bubble_sort_optimized(values):
    """Bubble sort with early termination if no swaps occur."""
    n = len(values)
    passes = 0
    swaps = 0

    for i in range(n - 1):
        swapped = False
        passes += 1
        for j in range(n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
                swaps += 1
        if not swapped:  # stop if list is already sorted
            break

    return values, passes, swaps


# ----------------------------------------------------------
# 🧩 2. Advanced Optimization — Tracking Last Swap Position
# ----------------------------------------------------------
def bubble_sort_last_swap(values):
    """Bubble sort optimized with last-swap index tracking."""
    n = len(values)
    end = n - 1
    passes = 0
    swaps = 0

    while end > 0:
        last_swap = 0
        passes += 1
        for i in range(end):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                last_swap = i
                swaps += 1
        end = last_swap  # reduces comparison range

        if last_swap == 0:  # early termination
            break

    return values, passes, swaps


# ----------------------------------------------------------
# 🧩 3. Test the algorithm on different types of lists
# ----------------------------------------------------------
import random

test_cases = {
    "Sorted list": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Reversed list": [9, 8, 7, 6, 5, 4, 3, 2, 1],
    "Random list": random.sample(range(1, 10), 9)
}

print("📍 Improved Bubble Sort (Early Stop):")
for name, data in test_cases.items():
    sorted_list, passes, swaps = bubble_sort_optimized(data.copy())
    print(f"{name}: {data}")
    print(f" → Sorted: {sorted_list}, Passes: {passes}, Swaps: {swaps}")
print()

print("📍 Improved Bubble Sort (Last Swap Optimization):")
for name, data in test_cases.items():
    sorted_list, passes, swaps = bubble_sort_last_swap(data.copy())
    print(f"{name}: {data}")
    print(f" → Sorted: {sorted_list}, Passes: {passes}, Swaps: {swaps}")
print()

# ----------------------------------------------------------
# ✅ Summary / Key Points
# ----------------------------------------------------------
# - Basic bubble sort performs redundant comparisons even if the list is sorted.
# - Early stop optimization halts the process when no swaps occur in a pass.
# - Last swap index tracking reduces the comparison range dynamically.
# - Both methods improve efficiency on nearly sorted data.
# - Time Complexity:
#     Best Case: O(n)
#     Average/Worst: O(n²)
# - Space Complexity: O(1) (in-place sorting)
# - Benefits:
#     ✅ Fewer iterations
#     ✅ Faster on sorted or nearly sorted lists
#     ✅ Still simple to understand and implement
