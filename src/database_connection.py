import os
import sqlite3
from config import DATABASE_NAME

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "data", DATABASE_NAME))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
