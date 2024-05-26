from bson import ObjectId

from BalanceUp.Backend.app.models.incomeModel import Income
from BalanceUp.Backend.app.db_management.connectDB import get_db

db = get_db()
incomes_collection = db['incomes']


def create_income(income: Income) -> ObjectId:
    result = incomes_collection.insert_one(income.dict())
    return result.inserted_id


def get_income_by_id(income_id: ObjectId) -> Income:
    income_data = incomes_collection.find_one({"_id": income_id})
    return Income(**income_data) if income_data else None


def update_income(income_id: ObjectId, income: Income):
    incomes_collection.update_one({"_id": income_id}, {"$set": income.dict()})


def delete_income(income_id: ObjectId):
    incomes_collection.delete_one({"_id": income_id})
