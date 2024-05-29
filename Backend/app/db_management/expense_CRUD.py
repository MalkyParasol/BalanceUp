from datetime import datetime
from typing import List

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


def get_expenses_by_user_id(user_id: str):
    expenses_cursor = expenses_collection.find({"user_id": user_id})
    user_expenses = [Expense(**expense) for expense in expenses_cursor]
    return user_expenses


def get_monthly_expense(user_id: str):
    allExpense = get_expenses_by_user_id(user_id)
    monthly_expenses = [0] * 31
    for expense in allExpense:
        date = datetime.strptime(expense.date, '%Y-%m-%d').date()
        if date.year == date.today().year and date.month == date.today().month:
            monthly_expenses[int(date.day) - 1] += expense.amount
    return monthly_expenses


def get_yearly_expense(user_id: str):
    allExpenses = get_expenses_by_user_id(user_id)
    yearly_expenses = [0] * 12
    for expense in allExpenses:
        date = datetime.strptime(expense.date, '%Y-%m-%d').date()
        if date.year == date.today().year:
            yearly_expenses[int(date.month) - 1] += expense.amount
    return yearly_expenses


def get_daily_expense(user_id: str, day: int):
    allExpenses = get_expenses_by_user_id(user_id)
    sum = 0
    for expense in allExpenses:
        date = datetime.strptime(expense.date, '%Y-%m-%d').date()
        if date.year == date.today().year and date.month == date.today().month and date.day == day:
            sum += expense.amount
    return sum
