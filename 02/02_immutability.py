age = 39
print(id(age))

age = 18
print(id(age))


num = 10
print("num id:", id(num))
num += 1
print("num id after change:", id(num))

text = "hello"
print("text id:", id(text))
text += " world"
print("text id after change:", id(text))

my_tuple = (1, 2, 3)
print("tuple id:", id(my_tuple))
my_tuple += (4,)
print("tuple id after change:", id(my_tuple))

my_list = [1, 2, 3]
print("list id:", id(my_list))
my_list.append(4)
print("list id after change:", id(my_list))


numbers = [1, 2, 3]
alias = numbers  # alias ugyanarra a listára mutat
print(id(numbers), id(alias))

alias.append(4)
print("numbers:", numbers)
print("alias:", alias)

import copy

nested = [[1, 2], [3, 4]]
shallow_copy = nested.copy()
deep_copy = copy.deepcopy(nested)

nested[0].append(99)

print("Original:", nested)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

s = "immutable"
print("Before:", id(s))
s = "changed"
print("After:", id(s))

import sys

a = [1, 2, 3]
b = a
c = a
print("Refcount:", sys.getrefcount(a))

del b
print("After deleting b:", sys.getrefcount(a))

del c
print("After deleting c:", sys.getrefcount(a))

import gc

print("GC enabled:", gc.isenabled())
gc.disable()
print("GC enabled after disable:", gc.isenabled())
gc.enable()
print("GC re-enabled:", gc.isenabled())

print("Collected objects:", gc.collect())
