from os import mkdir, path, rmdir, listdir, remove

# Create a new directory
dir_name = "example_dir"
if not path.exists(dir_name):  
    mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")
else:
    print(f"Directory '{dir_name}' already exists.")
# List contents of the current directory
print("Contents of the current directory:")
print(listdir('.'))
# Remove the created directory
if path.exists(dir_name):
    rmdir(dir_name)
    print(f"Directory '{dir_name}' removed.")   
# Create a new file in the directory
file_name = "example_file.txt"
with open(file_name, 'w') as f:
    f.write("This is an example file.")
print(f"File '{file_name}' created.")
# List contents of the current directory again  
print("Contents of the current directory after file creation:")
print(listdir('.'))
# Remove the created file
if path.exists(file_name):
    remove(file_name)
    print(f"File '{file_name}' removed.")   
# Final contents of the current directory
print("Final contents of the current directory:")
print(listdir('.'))
# Check if the directory exists
if not path.exists(dir_name):
    print(f"Directory '{dir_name}' does not exist.")
# Check if the file exists
if not path.exists(file_name):
    print(f"File '{file_name}' does not exist.")
