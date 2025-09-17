class Library:
    books = []

    def __init__(self, books):
        self.books = books

    def add(self, book):
        self.books.append(book)

    def display(self):
        print("Book list:")
        for b in self.books:
            print(b)
books = ['Harry Potter', 'Lord of the rings', '1984']

library = Library(books)

print("Welcome to the Library Management System.")

while True:
    print("Choose your option:")
    print("1. Display book list")
    print("2. Add book in the library")
    print("3. Write 'exit' to quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display()
    elif choice == "2":
        book = input("Enter the name of the book: ")
        library.add(book)
    elif choice == "exit":
        exit()
    else:
        print("Please choose the option correctly.")
