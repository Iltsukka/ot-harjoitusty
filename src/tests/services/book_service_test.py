import unittest
from services.book_service import BookService
from entities.book import Book

class FakeBookRepository:
    def __init__(self):
        self.books = [Book('Sinuhe', 'Egyptilainen', 1)]
    
    def find_all(self):
        return self.books
    def add_book(self, title, author):
        self.books.append(Book(title, author, 0))
        return True
fake_book_repository = FakeBookRepository()

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_service = BookService(fake_book_repository)


    def test_all_books_returns_books(self):
        books = self.book_service.all_books()
        self.assertEqual(len(books),1)

    def test_book_creation_returns_true(self):
        response = self.book_service.create_book('Testi', 'Case')
        self.assertTrue(response)

    def test_book_creation_increments_length_of_books(self):
        self.book_service.create_book('Test', 'case')
        self.assertEqual(len(self.book_service.all_books()), 2)