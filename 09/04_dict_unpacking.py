user = {'name': 'Alice', 'age': 30, 'job': 'Enigineer'}
name, age, job = user
print(name, age, job)  # Output: Alice 30 Enigineer

name, age, job = user.values()
print(name, age, job)  # Output: Alice 30 Enigineer

name, age, job = user.items()
print(name, age, job)  # Output: name age job

cart_net_prices = {'VGA': 1000, 'CPU': 500, 'Monitor': 300}
cart_gross_prices = {k: v * 1.2 for k, v in cart_net_prices.items()}