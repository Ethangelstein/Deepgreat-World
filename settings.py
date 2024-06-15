import os

from dotenv import load_env

load_env()

FLASK_DATABASE_HOST = os.environ.get("FLASK_DATABASE_HOST")
FLASK_DATABASE_PASSWORD = os.environ.get("FLASK_DATABASE_PASSWORD")
FLASK_DATABASE_USER = os.environ.get("FLASK_DATABASE_USER")
FLASK_DATABASE = os.environ.get("FLASK_DATABASE")
