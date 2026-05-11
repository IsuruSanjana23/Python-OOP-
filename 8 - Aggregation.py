class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def display_books(self):
        return [f"{book.name} by {book.author}" for book in self.books]

class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author

libary1 = Library("Public Lib 1")
libary2 = Library("Public Lib 2")

book1 = Book("Madol doowa","Martine Wickramasingha")
book2 = Book("Harry Porter","J.K. Rowling")

libary1.add_book(book1)
libary1.add_book(book2)

print(libary1.name)
for book in libary1.display_books():
    print(book)
