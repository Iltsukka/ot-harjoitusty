import unittest
from services.book_service import BookService
from entities.book import Book

class FakeBookRepository:
    def __init__(self):
        self.books = [Book('Sinuhe', 'Egyptilainen', 1), Book('Sakari', 'Afrikkalainen',2)]
    
    def find_all(self):
        return self.books
    def add_book(self, title, author):
        self.books.append(Book(title, author, 0))
        return True

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.fake_book_repository = FakeBookRepository()
        self.book_service = BookService(self.fake_book_repository)



    def test_all_books_returns_books(self):
        books = self.book_service.all_books()
        self.assertEqual(len(books),2)

    def test_book_creation_returns_true(self):
        response = self.book_service.create_book('Testi', 'Case')
        self.assertTrue(response)

    def test_book_creation_increments_length_of_books(self):
        self.book_service.create_book('Test', 'case')
        self.assertEqual(len(self.book_service.all_books()), 3)
    
    def test_sorting_by_author(self):
        sorted_books = self.book_service.sort_by('Author')
        expected_books = [Book('Sakari', 'Afrikkalainen', 2), Book('Sinuhe','Egyptilainen',1 )]
        for expected, actual in zip(expected_books, sorted_books):
            self.assertEqual(expected.title, actual.title)
            self.assertEqual(expected.author, actual.author)

    def test_sorting_by_title(self):
        sorted_books = self.book_service.sort_by('Title')
        expected_books = [Book('Sakari', 'Afrikkalainen', 2), Book('Sinuhe','Egyptilainen',1 )]
        for expected, actual in zip(expected_books, sorted_books):
            self.assertEqual(expected.title, actual.title)
            self.assertEqual(expected.author, actual.author)

    def test_sorting_default_return(self):
        filtered_books = self.book_service.sort_by('default')
        self.assertEqual(filtered_books, self.book_service.all_books())
        