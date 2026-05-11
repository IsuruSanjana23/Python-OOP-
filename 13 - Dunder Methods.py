class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Title: {self.title} / Author: {self.author} / Price: {self.price}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        return self.price + other.price

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "price":
            return self.price
        else:
            return f"{key} not found"

book1 = Book("The Hobbit" , "AAK" , 300)
book2 = Book("The Hobbit 2" , "AAK" , 350)

print(book1)
print(book1 == book2)
print(book2 > book1)
print(book2 + book1)
print("Hobbit" in book2)
print(book1["price"])