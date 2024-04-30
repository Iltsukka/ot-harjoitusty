import unittest
from repositories.book_repository import book_repository
from entities.book import Book

class TestBookRepository(unittest.TestCase):

    def setUp(self):
        book_repository.delete_all()
        book_repository.add_book('Dogmaster', 'Chicken','test-user')
        book_repository.add_book('Catmaster', 'Kukko', 'test-user')

    def test_return_all_books_as_objects(self):
        books = book_repository.find_all('test-user')
        self.assertEqual(len(books), 2)
        for book in books:
            self.assertIsInstance(book, Book)
        self.assertEqual(books[0].title, 'Dogmaster')
        self.assertEqual(books[0].author, 'Chicken')
        self.assertEqual(books[1].title, 'Catmaster')
        self.assertEqual(books[1].author, 'Kukko')
        
    
    def test_adding_a_book(self):
        book = book_repository.add_book('title', 'author', 'test-user')
        self.assertEqual(book.title, 'title')
        self.assertEqual(book.author, 'author')
        books = book_repository.find_all('test-user')
        self.assertEqual(len(books), 3)
    
    def test_deleting_a_book(self):
        book_repository.delete('Dogmaster','Chicken','test-user')
        books = book_repository.find_all('test-user')
        self.assertEqual(len(books),1)
    
    def test_searching_for_specific_book(self):
        book = book_repository.find_book('Catmaster', 'Kukko', 'test-user')
        self.assertTrue(book)
        non_existing_book = book_repository.find_book('chillaa', 'jäinen','godzilla')
        self.assertFalse(non_existing_book)

