class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f'{self.title}, {self.author}'
    
    # def __eq__(self, other):
    #     return isinstance(other, Book) and self.title == other.title and self.author == other.author

class Library():
    def __init__(self):
        self.books = []
    

    def add_book(self, book):
        if book in self.books:
            raise ValueError('No book')
        
        self.books.append(book)
    
    def show_books(self):
        return [str(book) for book in self.books]
    


book = Book('The Naked Sun', 'Isaac Asimov')
book1 = Book('I am the greatest', 'Mohamed Ali')
library = Library()
library.add_book(book)
library.add_book(book1)

print(library.show_books())