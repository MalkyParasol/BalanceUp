from datetime import datetime

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


def get_incomes_by_user_id(user_id: str):
    incomes_cursor = incomes_collection.find({"user_id": user_id})
    user_incomes = [Income(**income) for income in incomes_cursor]
    return user_incomes


def get_monthly_income(user_id: str):
    allIncomes = get_incomes_by_user_id(user_id)
    monthly_incomes = [0] * 31
    for income in allIncomes:
        date = datetime.strptime(income.date, '%Y-%m-%d').date()
        if date.year == date.today().year and date.month == date.today().month:
            monthly_incomes[int(date.day) - 1] += income.amount
    return monthly_incomes


def get_yearly_income(user_id: str):
    allIncomes = get_incomes_by_user_id(user_id)
    yearly_incomes = [0] * 12
    for income in allIncomes:
        date = datetime.strptime(income.date, '%Y-%m-%d').date()
        if date.year == date.today().year:
            yearly_incomes[int(date.month) - 1] += income.amount
    return yearly_incomes


def get_daily_income(user_id: str, day: int):
    allIncomes = get_incomes_by_user_id(user_id)
    sum = 0
    for income in allIncomes:
        date = datetime.strptime(income.date, '%Y-%m-%d').date()
        if date.year == date.today().year and date.month == date.today().month and date.day == day:
            sum += income.amount
    return sum
