from repositories.book_repository import book_repository

class BookService:
    def __init__(self, default_book_repository = book_repository):
        self.book_repository = default_book_repository
    def create_book(self, title, author):
        if self.book_repository.add_book(title, author):
            return True

        return False

    def all_books(self):
        return self.book_repository.find_all()

book_service = BookService()
