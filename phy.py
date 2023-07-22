#library system
books = []
def entry():
    code = int(input("Enter the book code: "))
    author = input("Enter the author name: ")
    book = input("Enter the book name: ")
    quantity = int(input("Enter the number of copies: "))
    book_data = [code, author, book, quantity]
    return book_data

def add():
    book_data = entry()
    books.append(book_data)
    print("Book added successfully.")

def dele():
    code_to_delete = int(input("Enter the book code to delete: "))
    for book_data in books:
        if book_data[0] == code_to_delete:
            books.remove(book_data)
            print("Book removed successfully.")
            return
    print("Invalid book code. Book not found.")

def issue():
    code_to_issue = int(input("Enter the book code to issue: "))
    for book_data in books:
        if book_data[0] == code_to_issue:
            if book_data[3] > 0:
                book_data[3] -= 1
                print("Book issued successfully.")
                return
            else:
                print("No copies of the book available for issue.")
                return
    print("Invalid book code. Book not found.")

def reci():
    code_to_receive = int(input("Enter the book code to receive: "))
    for book_data in books:
        if book_data[0] == code_to_receive:
            book_data[3] += 1
            print("Book received successfully.")
            return
    print("Invalid book code. Book not found.")

for i in range(100):
    print("\n\nWELCOME TO LIBRARY\n")
    print("1. Add books")
    print("2. Delete books")
    print("3. Issue books")
    print("4. Receive books")
    print("5. Display books")
    op = int(input("Choose the option: "))
    if op == 1:
        add()
    elif op == 2:
        dele()
    elif op == 3:
        issue()
    elif op == 4:
        reci()
    elif op == 5:
        print(books)
    else:
        print("Invalid entry")