import file_handler
import crud_operations
from os import path 

PATH = path.join(path.dirname(__file__), 'database', 'books.csv')

books = file_handler.read_file(PATH)

def list_books():
    pass

def find_book():
    pass

def update_book():
    pass

def create_book():
    pass

def delete_book():
    pass

