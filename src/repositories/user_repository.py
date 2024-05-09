import sqlite3
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def user_exists(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM users WHERE username = ?
                       AND password = ?''', (username, password))
        user = cursor.fetchone()
        if user:
            return True
        return False

    def create_user(self, username, password):
        cursor = self._connection.cursor()
        try:
            cursor.execute('''INSERT INTO users (username, password)
                            VALUES (?,?)''', (username, password))
            self._connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def delete_users(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from users')
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
