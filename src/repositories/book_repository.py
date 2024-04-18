from entities.book import Book
from database_connection import get_database_connection

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        res = cursor.execute('SELECT * FROM books')
        books = res.fetchall()
        book_objects = []
        for book in books:
            book_objects.append(Book(book['title'], book['author'], book['id']))
        return book_objects

    def add_book(self, title, author):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO books (title, author) VALUES (?,?)", (title, author))
        book_id = cursor.lastrowid
        self._connection.commit()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        book = Book(row['title'], row['author'], row['id'])
        return book

    def delete(self, title, author):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM books WHERE title = ? AND author = ?", (title, author))
        deleted_rows = cursor.rowcount
        self._connection.commit()
        if deleted_rows > 0:
            return True
        return False

book_repository = BookRepository(get_database_connection())
