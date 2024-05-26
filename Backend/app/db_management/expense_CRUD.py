from bson import ObjectId

from BalanceUp.Backend.app.db_management.connectDB import get_db
from BalanceUp.Backend.app.models.expenseModel import Expense

db = get_db()
expenses_collection = db["expenses"]


def create_expense(expense: Expense) -> ObjectId:
    result = expenses_collection.insert_one(expense.dict())
    return result.inserted_id


def get_expense_by_id(expense_id: ObjectId) -> Expense:
    expense_data = expenses_collection.find_one({"_id": expense_id})
    return Expense(**expense_data) if expense_data else None


def update_expense(expense_id: ObjectId, expense: Expense):
    expenses_collection.update_one({"_id": expense_id}, {"$set": expense.dict()})

def delete_expense(expense_id: ObjectId):
    expenses_collection.delete_one({"_id": expense_id})