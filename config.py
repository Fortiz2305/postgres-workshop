import os

DB_NAME = os.environ.get('DB_NAME', None)
DB_USER = os.environ.get('DB_USER', None)
DB_PASSWORD = os.environ.get('DB_PASSWORD', None)
DB_HOST = os.environ.get('DB_HOST', 'localhost')
