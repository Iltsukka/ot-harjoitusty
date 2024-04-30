from repositories.book_repository import book_repository

class BookService:
    def __init__(self, default_book_repository = book_repository):
        self.book_repository = default_book_repository
    def create_book(self, title, author, username):
        return self.book_repository.add_book(title, author, username)

    def all_books(self, username):
        return self.book_repository.find_all(username)

    def sort_by(self, mechanism, username):
        books = self.all_books(username)
        if mechanism == 'Title':
            return sorted(books, key=lambda book: book.title.lower())
        if mechanism =='Author':
            return sorted(books,key=lambda book: book.author.lower())

        return books

    def delete_book(self, title, author, username):
        if self.book_repository.delete(title, author, username):
            return True
        return False

    def book_exists(self, title, author, username):
        return self.book_repository.find_book(title, author, username)



book_service = BookService()
