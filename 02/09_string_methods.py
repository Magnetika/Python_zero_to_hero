name = 'Agnes'

print(len(name))

print(name[0])
print(name[4])
# name[0] = 'g'

print(f'Uppercase name: {name.upper()}')
print(f'Lowercase name: {name.lower()}')

print(f'All characters are lowercase: {name.lower().islower()}')

print(f'count of "A" in name: {name.count("A")}')
print(f'replace "A" with "a": {name.replace("A", "a")}')
