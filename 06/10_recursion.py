def gcd_loop(a, b):
    
    while b :
        a, b = b, a % b
    return a

print(gcd_loop(3, 33))

def gcd_recursive(a, b):
    return a if b == 0 else gcd_recursive(b, a % b)

print(gcd_recursive(3, 33))