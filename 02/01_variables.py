# 🐍 Python Variables – Practice Script
# ------------------------------------
# Cél: Változók létrehozása, újraértékelése, elnevezési szabályok és típusok megismerése

# 1️⃣ Egyszerű változók létrehozása és módosítása
age = 39
print(age)
print(age + 1)

# Új érték hozzárendelése ugyanahhoz a változóhoz
age = 18
print(age)

# 2️⃣ Más típusú változó: fizetés
yearly_salary = 100000
print(yearly_salary)

# 3️⃣ Python kulcsszavak megtekintése (nem használhatók változónévként)
print(help('keywords'))

# 4️⃣ Konstans jellegű érték (PEP 8 szerint nagybetűs név)
PI = 3.14
print(PI)

# 5️⃣ Több változó és különböző típusok
name = "Anna"
age = 25
height = 1.68
print(name, age, height)

# 6️⃣ Változó újraértékelése és rövidített növelés
counter = 1
print(counter)
counter = counter + 1
print(counter)
counter += 1  # rövidebb forma
print(counter)

# 7️⃣ Különböző elnevezési stílusok (csak az első ajánlott)
snake_case = "recommended"
camelCase = "usedInOtherLanguages"
PascalCase = "usedForClasses"
UPPER_CASE = "constant"
print(snake_case, camelCase, PascalCase, UPPER_CASE)

# 8️⃣ Olvashatóság példa
a = 500
b = 600
c = a + b
print(c)

# Olvashatóbb megoldás:
salary_january = 500
salary_february = 600
total_salary = salary_january + salary_february
print(total_salary)

# 9️⃣ Dinamikus típusosság bemutatása
data = 42
print(data, type(data))

data = "forty-two"
print(data, type(data))

data = 3.14
print(data, type(data))

# 🔟 Példa: Személyes adatok (statikus kiírás)
print("Name: Anna Kovács")
print("Age: 19")
print("Student: True")

# 11️⃣ Formázott szöveg (f-string)
book_title = "Python Crash Course"
author = "Eric Matthes"
year_published = 2019
print(f"My favorite book is {book_title} by {author} ({year_published}).")

# 12️⃣ Felhasználói bevitel (interaktív)
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}, next year you will be {age + 1} years old!")
