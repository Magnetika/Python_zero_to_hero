from os import chdir, path

chdir(path.join(path.dirname(__file__)))

with open(file = 'copied_example.txt', mode='w', encoding='utf-8') as file:
    content = ['1.new file content', '2.new file content', '3.new file content']
    file.write(content) 
    

