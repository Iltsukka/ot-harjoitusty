import unittest
from repositories.book_repository import BookRepository
from database_connection import get_database_connection
from initialize_database import initialize_database
from entities.book import Book

class TestBookRepository(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self._connection = get_database_connection()
        self._book_repository = BookRepository(self._connection)
        self._book_repository.add_book('Dogmaster', 'Chicken')
        self._book_repository.add_book('Catmaster', 'Kukko')

    def test_return_all_books_as_objects(self):
        books = self._book_repository.find_all()
        self.assertEqual(len(books), 2)
        for book in books:
            self.assertIsInstance(book, Book)
        self.assertEqual(books[0].title, 'Dogmaster')
        self.assertEqual(books[0].author, 'Chicken')
        self.assertEqual(books[1].title, 'Catmaster')
        self.assertEqual(books[1].author, 'Kukko')
        
    
    def test_adding_a_book(self):
        book = self._book_repository.add_book('title', 'author')
        self.assertEqual(book.title, 'title')
        self.assertEqual(book.author, 'author')
        books = self._book_repository.find_all()
        self.assertEqual(len(books), 3)

