from datetime import datetime

from bson import ObjectId

from BalanceUp.Backend.app.db_management.connectDB import get_db
from BalanceUp.Backend.app.models.expenseModel import Expense

db = get_db()
expenses_collection = db["expenses"]


def create_expense(expense: Expense) -> ObjectId:
    """
        Creates a new expense record in the database.

        Args:
            expense (Expense): An Expense object representing the details of the expense.

        Returns:
            ObjectId: The unique identifier of the newly created expense record in the database.
        """
    result = expenses_collection.insert_one(expense.dict())
    return result.inserted_id


def get_expense_by_id(expense_id: ObjectId) -> Expense:
    """
        Retrieves an expense record from the database by its ID.

        Args:
            expense_id (ObjectId): The unique identifier of the expense record.

        Returns:
            Expense: An Expense object representing the retrieved expense record, or None if not found.
        """
    expense_data = expenses_collection.find_one({"_id": expense_id})
    return Expense(**expense_data) if expense_data else None


def update_expense(expense_id: ObjectId, expense: Expense):
    """
       Updates an existing expense record in the database.

       Args:
           expense_id (ObjectId): The unique identifier of the expense record to be updated.
           expense (Expense): An Expense object containing the updated details of the expense.
       """
    expenses_collection.update_one({"_id": expense_id}, {"$set": expense.dict()})


def delete_expense(expense_id: ObjectId):
    """
        Deletes an expense record from the database.

        Args:
            expense_id (ObjectId): The unique identifier of the expense record to be deleted.
        """
    expenses_collection.delete_one({"_id": expense_id})


def get_expenses_by_user_id(user_id: str):
    """
        Retrieves all expenses associated with a user from the database.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            list: A list of Expense objects representing the retrieved expenses.
        """
    expenses_cursor = expenses_collection.find({"user_id": user_id})
    user_expenses = [Expense(**expense) for expense in expenses_cursor]
    return user_expenses


def get_monthly_expense(user_id: str):
    """
        Retrieves monthly expenses for a user from the database.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            list: A list containing the total expenses for each day of the current month.
        """
    allExpense = get_expenses_by_user_id(user_id)
    monthly_expenses = [0] * 31
    for expense in allExpense:
        date = datetime.strptime(expense.date, '%Y-%m-%d').date()
        if date.year == date.today().year and date.month == date.today().month:
            monthly_expenses[int(date.day) - 1] += expense.amount
    return monthly_expenses


def get_yearly_expense(user_id: str):
    """
        Retrieves yearly expenses for a user from the database.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            list: A list containing the total expenses for each month of the current year.
    """
    allExpenses = get_expenses_by_user_id(user_id)
    yearly_expenses = [0] * 12
    for expense in allExpenses:
        date = datetime.strptime(expense.date, '%Y-%m-%d').date()
        if date.year == date.today().year:
            yearly_expenses[int(date.month) - 1] += expense.amount
    return yearly_expenses


def get_daily_expense(user_id: str, day: int):
    """
       Retrieves daily expenses for a user from the database.

       Args:
           user_id (str): The unique identifier of the user.
           day (int): The day of the month for which expenses are to be retrieved.

       Returns:
           float: The total expenses for the specified day.
       """
    allExpenses = get_expenses_by_user_id(user_id)
    sum = 0
    for expense in allExpenses:
        date = datetime.strptime(expense.date, '%Y-%m-%d').date()
        if date.year == date.today().year and date.month == date.today().month and date.day == day:
            sum += expense.amount
    return sum
