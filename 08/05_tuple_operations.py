print((1,2) + (3,4))  
print((1,2) * 2)

names = ('Alice', 'Bob', 'Charlie', 'Diana')
print(names[:2])
print(names[::3])

Alice, Bob, Charlie, Diana = names
print(Alice, Bob, Charlie, Diana)
print(len(names))

numbers = (1, 2, 3, 4, 5)
squares = (i**2 for i in numbers)
squares_tuple = tuple(squares)
print(type(squares))
print(type(squares_tuple))
print(squares_tuple)
