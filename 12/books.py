import crud_operations
from os import path

PATH = path.join(path.dirname(__file__), 'database', 'books.csv')

# load books into memory
books = crud_operations.read_file(PATH)


def list_books():
    if not books:
        print("No books found.")
        return
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']}")


def find_book():
    try:
        book_id = int(input("Enter book ID to find: "))
    except ValueError:
        print("Invalid ID")
        return
    book = crud_operations.find_item(books, book_id)
    if book:
        print(f"Found: ID={book['id']}, Title={book['title']}, Author={book['author']}")
    else:
        print("Book not found.")


def update_book():
    try:
        book_id = int(input("Enter book ID to update: "))
    except ValueError:
        print("Invalid ID")
        return
    book = crud_operations.find_item(books, book_id)
    if not book:
        print("Book not found.")
        return
    # prompt for new values, leave blank to keep
    new_title = input(f"Enter new title (leave blank to keep '{book['title']}'): ").strip()
    new_author = input(f"Enter new author (leave blank to keep '{book['author']}'): ").strip()
    updated = book.copy()
    if new_title:
        updated['title'] = new_title
    if new_author:
        updated['author'] = new_author
    if crud_operations.update_item(book_id, books, updated):
        crud_operations.write_file(PATH, books)
        print("Book updated successfully.")
    else:
        print("Failed to update book.")


def create_book():
    title = input("Enter title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    author = input("Enter author: ").strip()
    if not author:
        print("Author cannot be empty.")
        return
    new_book = crud_operations.add_item(books, title, author)
    crud_operations.write_file(PATH, books)
    print(f"Book created: ID={new_book['id']}, Title={new_book['title']}")


def delete_book():
    try:
        book_id = int(input("Enter book ID to delete: "))
    except ValueError:
        print("Invalid ID")
        return
    book = crud_operations.find_item(books, book_id)
    if not book:
        print("Book not found.")
        return
    confirm = input(f"Are you sure you want to delete '{book['title']}'? (y/N): ").lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return
    if crud_operations.delete_item(book_id, books):
        crud_operations.write_file(PATH, books)
        print("Book deleted.")
    else:
        print("Failed to delete book.")

