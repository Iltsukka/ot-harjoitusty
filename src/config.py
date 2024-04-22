import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    print('make sure that the .env file is in the top level and not in /src')


DATABASE_NAME = os.getenv('DATABASE_NAME') or 'database.sqlite'
