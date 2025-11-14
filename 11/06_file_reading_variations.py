from os import chidr, path

chdir(path.join(path.dirname(__file__), "unzipped_folder"))

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    