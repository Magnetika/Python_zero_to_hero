x1 = {'a', 'b', 'c'}
x2 = {'b', 'c', 'd'}

print(x1.union(x2))        # {'a', 'b', 'c', 'd'}
print(x1.intersection(x2)) # {'b', 'c'}
print(x1.difference(x2))   # {'a'}
print(x1.symmetric_difference(x2)) # {'a', 'd'}
x1.update(x2)
print(x1)                  # {'a', 'b', 'c', 'd'}
x1.remove('a')
print(x1)                  # {'b', 'c', 'd'}
x1.add('e')
print(x1)                  # {'b', 'c', 'd', 'e'}
x1.clear()
print(x1)                  # set()
