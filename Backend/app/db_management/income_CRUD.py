from datetime import datetime

from bson import ObjectId

from BalanceUp.Backend.app.models.incomeModel import Income
from BalanceUp.Backend.app.db_management.connectDB import get_db

db = get_db()
incomes_collection = db['incomes']


def create_income(income: Income) -> ObjectId:
    """
       Creates a new income record in the database.

       Args:
           income (Income): An Income object representing the details of the income.

       Returns:
           ObjectId: The unique identifier of the newly created income record in the database.
       """
    result = incomes_collection.insert_one(income.dict())
    return result.inserted_id


def get_income_by_id(income_id: ObjectId) -> Income:
    """
        Retrieves an income record from the database by its ID.

        Args:
            income_id (ObjectId): The unique identifier of the income record.

        Returns:
            Income: An Income object representing the retrieved income record, or None if not found.
        """
    income_data = incomes_collection.find_one({"_id": income_id})
    return Income(**income_data) if income_data else None


def update_income(income_id: ObjectId, income: Income):
    """
        Updates an existing income record in the database.

        Args:
            income_id (ObjectId): The unique identifier of the income record to be updated.
            income (Income): An Income object containing the updated details of the income.
        """
    incomes_collection.update_one({"_id": income_id}, {"$set": income.dict()})


def delete_income(income_id: ObjectId):
    """
        Deletes an income record from the database.

        Args:
            income_id (ObjectId): The unique identifier of the income record to be deleted.
        """
    incomes_collection.delete_one({"_id": income_id})


def get_incomes_by_user_id(user_id: str):
    """
        Retrieves all incomes associated with a user from the database.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            list: A list of Income objects representing the retrieved incomes.
        """
    incomes_cursor = incomes_collection.find({"user_id": user_id})
    user_incomes = [Income(**income) for income in incomes_cursor]
    return user_incomes


def get_monthly_income(user_id: str):
    """
        Retrieves monthly incomes for a user from the database.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            list: A list containing the total incomes for each day of the current month.
        """
    allIncomes = get_incomes_by_user_id(user_id)
    monthly_incomes = [0] * 31
    for income in allIncomes:
        date = datetime.strptime(income.date, '%Y-%m-%d').date()
        if date.year == date.today().year and date.month == date.today().month:
            monthly_incomes[int(date.day) - 1] += income.amount
    return monthly_incomes


def get_yearly_income(user_id: str):
    """
       Retrieves yearly incomes for a user from the database.

       Args:
           user_id (str): The unique identifier of the user.

       Returns:
           list: A list containing the total incomes for each month of the current year.
       """
    allIncomes = get_incomes_by_user_id(user_id)
    yearly_incomes = [0] * 12
    for income in allIncomes:
        date = datetime.strptime(income.date, '%Y-%m-%d').date()
        if date.year == date.today().year:
            yearly_incomes[int(date.month) - 1] += income.amount
    return yearly_incomes


def get_daily_income(user_id: str, day: int):
    """
       Retrieves daily incomes for a user from the database.

       Args:
           user_id (str): The unique identifier of the user.
           day (int): The day of the month for which incomes are to be retrieved.

       Returns:
           float: The total incomes for the specified day.
       """
    allIncomes = get_incomes_by_user_id(user_id)
    sum = 0
    for income in allIncomes:
        date = datetime.strptime(income.date, '%Y-%m-%d').date()
        if date.year == date.today().year and date.month == date.today().month and date.day == day:
            sum += income.amount
    return sum
