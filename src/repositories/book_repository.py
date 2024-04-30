from entities.book import Book
from database_connection import get_database_connection

class BookRepository:
    """Luokka, joka vastaa kirjojen tietokantaoperaatioista

    Attributes: connection: Tietokantayhteys.
    """
    def __init__(self, connection):
        """Luokan konstruktori, joka luo uuden BookRepository olion

        Args:
            connection: Tietokantayhteys.
        """
        self._connection = connection

    def find_all(self, username):
        """Hakee tietokannasta kaikki kirjat

        Returns:
            Lista Book -olioita, joilla attribuutit 'title', 'author' ja 'id'
        """
        cursor = self._connection.cursor()
        res = cursor.execute('SELECT * FROM books WHERE username = ?',(username,))
        books = res.fetchall()
        book_objects = []
        for book in books:
            book_objects.append(Book(book['title'], book['author'], book['id']))
        return book_objects

    def add_book(self, title, author, username):
        """Lisää kirjan tietokantaan

        Args:
            title: Kirjan nimi.
            author: Kirjailijan nimi.

        Returns:
            Kirja-objekti, jolla atribuutit 'title', 'author' ja 'id'.
        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO books (title, author, username) VALUES (?,?,?)", (title, author, username))
        book_id = cursor.lastrowid
        self._connection.commit()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        book = Book(row['title'], row['author'], row['id'])
        return book

    def delete(self, title, author, username):
        """Poistaa kirjan tiedot tietokannasta

        Args:
            title: Kirjan nimi.
            author: Kirjailijan nimi.

        Returns:
            True, jos poisto onnistuu, muutoin False.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM books WHERE title = ? AND author = ? AND username = ?", (title, author, username))
        deleted_rows = cursor.rowcount
        self._connection.commit()
        if deleted_rows > 0:
            return True
        return False

    def find_book(self, title, author, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM books WHERE title = ? AND author = ? AND username = ?", (title, author, username))
        book = cursor.fetchone()
        if book:
            return True
        return False

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from books')
        self._connection.commit()

book_repository = BookRepository(get_database_connection())
