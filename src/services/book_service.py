from repositories.book_repository import book_repository

class BookService:
    def __init__(self, default_book_repository = book_repository):
        self.book_repository = default_book_repository
    def create_book(self, title, author):
        return self.book_repository.add_book(title, author)

    def all_books(self):
        return self.book_repository.find_all()

    def sort_by(self, mechanism):
        books = self.all_books()
        if mechanism == 'Title':
            return sorted(books, key=lambda book: book.title.lower())
        if mechanism =='Author':
            return sorted(books,key=lambda book: book.author.lower())

        return books


book_service = BookService()
