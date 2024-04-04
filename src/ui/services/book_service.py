from entities.book import Book

class BookService:
    def __init__(self):
        pass
    def create_book(self, title, author):
        pass

    def find_all(self):
        return [Book('Title', 'Author', '1'), Book('Sinuhe', 'Waltari', '2')]

book_service = BookService()