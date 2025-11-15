def read_file(filepath):
    books = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # CSV uses ';' as separator in this dataset
            parts = line.split(';')
            if len(parts) < 3:
                continue
            id_str, title, author = parts[0].strip(), parts[1].strip(), parts[2].strip()
            try:
                book_id = int(id_str)
            except ValueError:
                # skip malformed id lines
                continue
            books.append({
                'id': book_id,
                'title': title,
                'author': author,
            })
    return books


def write_file(filepath, books):
    # write using ';' as separator to match the existing file
    with open(filepath, 'w', encoding='utf-8') as file:
        for book in books:
            row = ';'.join([str(book.get('id', '')), book.get('title', ''), book.get('author', '')]) + '\n'
            file.write(row)


def find_item(books, book_id):
    for book in books:
        if book.get('id') == book_id:
            return book
    return None


def update_item(book_id, books, new_book):
    for i, book in enumerate(books):
        if book.get('id') == book_id:
            books[i] = new_book
            return True
    return False


def add_item(books, title, author):
    max_id = max((b.get('id', 0) for b in books), default=0)
    new_id = max_id + 1
    new_book = {'id': new_id, 'title': title, 'author': author}
    books.append(new_book)
    return new_book


def delete_item(book_id, books):
    for i, book in enumerate(books):
        if book.get('id') == book_id:
            del books[i]
            return True
    return False

