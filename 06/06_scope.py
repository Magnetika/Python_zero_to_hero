global_variable = 'global'
print(global_variable)

def log():
    local_variable = 'local'
    print(local_variable)
    print(global_variable)


log()
print(global_variable)

