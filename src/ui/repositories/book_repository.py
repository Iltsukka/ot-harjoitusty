from entities.book import Book

class BookRepository:
    def __init__(self):
        self._books = [Book('Testbook', 'Waltari', 2), Book('Roman', 'Waltari', 3), Book('The grapes of wrath', 'Steinbeck', 4)]

    def find_all(self):
        return self._books
    
    def add_book(self, title, author):
        self._books.append(Book(title, author,0))
        return True

book_repository = BookRepository()
