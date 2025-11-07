numbers= [1, 2, 3, 4, 5, 1, 1, 2, 2, 2, 5, 5, 5]
#numbers_with_duplicates = []

#for i in numbers:
#    if i not in numbers_with_duplicates:
#        numbers_with_duplicates.append(i)

#print(numbers_with_duplicates)

numbers_without_duplicates = set(numbers)
print(numbers_without_duplicates)

