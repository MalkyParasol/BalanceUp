# connectDB.py
from pymongo import MongoClient
from BalanceUp.Backend.app.db_management.config import get_mongodb_uri, get_database_name


def connect_to_db():
    """
    Connect to the MongoDB database using the configured URI and database name.
    Returns the database object.
    """
    mongodb_uri = get_mongodb_uri()
    database_name = get_database_name()
    client = MongoClient(mongodb_uri)
    db = client[database_name]
    return db


def get_db():
    """
    Get the database object.
    """
    return connect_to_db()
