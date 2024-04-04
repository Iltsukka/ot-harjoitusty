from entities.book import Book

class BookService:
    def __init__(self):
        pass
    def create_book(self, title, author):
        pass

    def find_all(self):
        return [Book('Title', 'Author1', '1'), Book('Sinune Egyptiläinen', 'Author2', '2')]

book_service = BookService()