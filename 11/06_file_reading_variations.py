from os import chdir, path

chdir(path.join(path.dirname(__file__)))

with open("copied_example.txt", "r") as file:
    content = file.read(4)
    print(content)
