"""
expenseRouter.py

This module defines API routes related to expenses, including creating, updating, deleting, and retrieving expenses.

"""
from datetime import date

from bson import ObjectId
from fastapi import FastAPI, Depends, APIRouter, HTTPException

from BalanceUp.Backend.app.db_management.expense_CRUD import create_expense, get_expense_by_id, update_expense, \
    delete_expense, get_expenses_by_user_id
from BalanceUp.Backend.app.models.expenseModel import Expense
from BalanceUp.Backend.utils.logDecorator import log_to_file

expenseRouter = APIRouter()


@expenseRouter.post("/{user_id}")
@log_to_file()
def createExpense(user_id: str, expense: Expense):
    """
        Create a new expense.

        Args:
            user_id (str): The unique identifier of the user.
            expense (Expense): An Expense object representing the details of the expense to be created.

        Returns:
            dict: A dictionary containing the created expense ID if successful, or an error message if failed.
        """
    try:
        user_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid user id")
    try:
        expense.user_id = str(user_id)
        expense.date = str(date.today())
        newExpense = create_expense(expense)
        if newExpense:
            return {"expense id": str(newExpense)}
        else:
            return "expense created failed"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"cannot crater expense{str(e)}")


@expenseRouter.put("/{expense_id}")
@log_to_file()
def updateExpense(expense_id: str, expense: Expense):
    """
       Update an existing expense.

       Args:
           expense_id (str): The unique identifier of the expense.
           expense (Expense): An Expense object representing the updated details of the expense.

       Returns:
           dict: A dictionary containing a success message if the update was successful.
       """
    try:
        expenseId = ObjectId(expense_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid expense id")
    try:
        old_income = get_expense_by_id(expenseId)
        expense.user_id = old_income.user_id
        expense.date = old_income.date
        update_expense(expenseId, expense)
        return {"message": "expense updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"failed to update this expense{e}")


@expenseRouter.delete("/{expense_id}")
@log_to_file()
def deleteExpense(expense_id: str):
    """
        Delete an expense.

        Args:
            expense_id (str): The unique identifier of the expense to be deleted.

        Returns:
            dict: A dictionary containing a success message if the deletion was successful.
        """
    try:
        expenseId = ObjectId(expense_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid expense id")
    try:
        delete_expense(expenseId)
        return {"message": "expense deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to delete this expense")


@expenseRouter.get("/{user_id}")
@log_to_file()
def getExpenseByUserId(user_id: str):
    """
        Retrieve expenses by user ID.

        Args:
            user_id (str): The unique identifier of the user whose expenses are to be retrieved.

        Returns:
            list: A list of expenses associated with the provided user ID.
    """
    try:
        return get_expenses_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to load this expenses")


@expenseRouter.get("/{expense_id}")
@log_to_file()
def getExpenseById(expense_id: str):
    """
        Retrieve an expense by its ID.

        Args:
            expense_id (str): The unique identifier of the expense to be retrieved.

        Returns:
            Expense: An Expense object representing the retrieved expense.
    """
    try:
        expenseId = ObjectId(expense_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid expense id")
    return get_expense_by_id(expenseId)
