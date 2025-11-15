import books


while True:
    command = int(input("Enter command (1: List, 2: Find, 3: Create, 4: Update, 5: Delete, 6: Exit): "))



    if command == 1:
        books.list_books()
    elif command == 2:
        books.find_book()
    elif command == 3:
        books.create_book()
    elif command == 4:
        books.update_book()
    elif command == 5:
        books.delete_book()
    elif command == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid command")

