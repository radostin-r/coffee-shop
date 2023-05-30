import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')

DATABASE_URL = os.getenv('DATABASE_URL')
