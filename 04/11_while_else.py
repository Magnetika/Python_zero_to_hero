i = 0
while i < 10:
    print
    i += 1

for i in range(10):
    print(i)


number = 13
i = 2
while i <= number // 2:
    if number % i == 0:
        print(f"{number} is not a prime number.")
        break
    i += 1
else:
    print(f"{number} is a prime number.") 
  