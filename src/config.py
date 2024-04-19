import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    print('failed to load_dotenv')


DATABASE_NAME = os.getenv('DATABASE_NAME') or 'database.sqlite'
