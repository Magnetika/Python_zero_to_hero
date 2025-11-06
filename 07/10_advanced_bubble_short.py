def bubble_short(values):
   for i in range(len(values)):
      swapped = False
      for j in range(len(values) - 1 - i):
         print(i, j)
         if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            swapped = True
      if not swapped:
         break
   return values

val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bubble_short(val))

