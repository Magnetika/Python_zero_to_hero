# 🧠 Python Immutability & Memory Management – Practice Script
# ------------------------------------------------------------
# Cél: Megérteni a mutability/immutability fogalmát, az id() működését,
# a másolás típusait, és a garbage collection alapjait.


# ----------------------------------------------------------------------
# 1️⃣ Alapok: azonosító (id) és reassignment immutable típusoknál
# ----------------------------------------------------------------------

age = 39
print("age (39) id:", id(age))

age = 18  # új érték -> új objektum
print("age (18) id:", id(age))
print("-" * 60)


# ----------------------------------------------------------------------
# 2️⃣ Mutability vs. Immutability – különböző adattípusok
# ----------------------------------------------------------------------

num = 10
print("num id:", id(num))
num += 1  # új érték, új objektum
print("num id after change:", id(num))

text = "hello"
print("text id:", id(text))
text += " world"  # string immutable → új objektum jön létre
print("text id after change:", id(text))

my_tuple = (1, 2, 3)
print("tuple id:", id(my_tuple))
my_tuple += (4,)  # új tuple jön létre
print("tuple id after change:", id(my_tuple))

my_list = [1, 2, 3]
print("list id:", id(my_list))
my_list.append(4)  # list mutable → ugyanaz az objektum
print("list id after change:", id(my_list))
print("-" * 60)


# ----------------------------------------------------------------------
# 3️⃣ Objektumazonosság és aliasing (több változó ugyanarra az objektumra mutat)
# ----------------------------------------------------------------------

numbers = [1, 2, 3]
alias = numbers  # alias ugyanarra a listára mutat
print("numbers id:", id(numbers), "| alias id:", id(alias))

alias.append(4)
print("numbers:", numbers)
print("alias:", alias)
print("-" * 60)


# ----------------------------------------------------------------------
# 4️⃣ Másolás: shallow vs. deep copy
# ----------------------------------------------------------------------

import copy

nested = [[1, 2], [3, 4]]
shallow_copy = nested.copy()
deep_copy = copy.deepcopy(nested)

nested[0].append(99)  # csak a shallow copy és az eredeti változik

print("Original:", nested)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)
print("-" * 60)


# ----------------------------------------------------------------------
# 5️⃣ Új hozzárendelés immutable típusnál
# ----------------------------------------------------------------------

s = "immutable"
print("Before change:", id(s))
s = "changed"  # új objektum jön létre
print("After change:", id(s))
print("-" * 60)


# ----------------------------------------------------------------------
# 6️⃣ Referenciaszámolás – hány változó mutat ugyanarra az objektumra
# ----------------------------------------------------------------------

import sys

a = [1, 2, 3]
b = a
c = a
print("Initial refcount:", sys.getrefcount(a))

del b
print("After deleting b:", sys.getrefcount(a))

del c
print("After deleting c:", sys.getrefcount(a))
print("-" * 60)


# ----------------------------------------------------------------------
# 7️⃣ Garbage Collector – bekapcsolás, kikapcsolás, statisztika
# ----------------------------------------------------------------------

import gc

print("GC enabled initially:", gc.isenabled())
gc.disable()
print("GC enabled after disable:", gc.isenabled())

gc.enable()
print("GC re-enabled:", gc.isenabled())

print("Collected objects (manual gc):", gc.collect())
print("-" * 60)

print("✅ Script finished successfully.")
