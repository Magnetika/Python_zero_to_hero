def get_index(values, element):
    for i in range(len(values)):
        if values[i] == element:
            return i
        
val = [10, 20, 30, 40, 50]
print(get_index(val, 30))         

print(val.index(30))