class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        
    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' wasn't borrowed.")

    def __str__(self):
        return f"'{self.title}' by {self.author} - Status: {'Available' if self.is_available else 'Borrowed'}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"'{title}' by {author} has been added to the library.")

    def list_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
        print(f"Sorry, '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print(f"Sorry, '{title}' is not found in the library.")

def main():
    library = Library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View all books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(title)
        elif choice == '3':
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)
        elif choice == '4':
            library.list_books()
        elif choice == '5':
            print("Googbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()