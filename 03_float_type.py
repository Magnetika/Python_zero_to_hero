print(10.1)
print(-10.1)

# min value
print(-1.79e308)
# -inf
print(-1.8e308)

# max value
print(1.79e308)
# +inf
print(1.8e308)

# closest non zero value
print(5e-324)
# zero
print(1e-325)

print(type(10.1))

a = 3.14
b = -2.718
c = 0.0
print(a, b, c)
print(type(a))


x = 10
y = float(x)
print(y)
print(type(y))

z = 7.89
print(int(z))

value = 3.1415926535
print(round(value, 2))
print(round(value, 4))
print(round(value))

x = 0.1 + 0.2
print(x)
print(x == 0.3)

import math
print(math.isclose(0.1 + 0.2, 0.3))

import sys
print(sys.float_info)
print("Maximum:", sys.float_info.max)
print("Minimum:", sys.float_info.min)

print(1e308)
print(1e309)  # próbáld ki!
