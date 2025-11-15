def read_file(filepath):
    with open(filepath, 'r') as file:
        users = []
        for line in file:
            id, title, author = line.rstrip().split(',')
            users.append({
                'id': int(id),
                'title': title,
                'author': author,
            })
        return users
    
def append_user(filepath, user):
    with open(filepath, 'a') as file:
        user_line = '\n' + ';'.join(str(val) for val in user.values())
        file.write(user_line)

