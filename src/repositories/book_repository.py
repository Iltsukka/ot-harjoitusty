from entities.book import Book

class BookRepository:
    def __init__(self):
        self._books = [Book('Testbook', 'Waltari', 2),
                        Book('Roman', 'Waltari', 3), Book('The grapes of wrath', 'Steinbeck', 4)]

    def find_all(self):
        return self._books

    def add_book(self, title, author):
        book = Book(title, author, 0)
        self._books.append(book)
        return book

book_repository = BookRepository()
