import file_handler
import crud_operations
from os import path 

PATH = path.join(path.dirname(__file__), 'database', 'books.csv')

books = file_handler.read_file(PATH)

def list_books():
    print(books)

def find_book():
    id = int(input("Enter book ID to find: "))
    print(crud_operations.find_item(books, id))

def update_book():
    pass

def create_book():
    pass

def delete_book():
    pass

