from pymongo import MongoClient
from BalanceUp.Backend.app.db_management.config import MONGODB_URI, DATABASE_NAME

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]


def get_db():
    return db
