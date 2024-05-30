"""
incomeRouter.py

This module defines API routes related to incomes, including adding, updating, deleting, and retrieving incomes.

"""
from bson import ObjectId
from fastapi import FastAPI, Depends, APIRouter, HTTPException
from datetime import date
from BalanceUp.Backend.app.db_management.income_CRUD import create_income, update_income, get_income_by_id, \
    delete_income, get_incomes_by_user_id
from BalanceUp.Backend.app.models.incomeModel import Income
from BalanceUp.Backend.utils.logDecorator import log_to_file

incomeRouter = APIRouter()


@incomeRouter.post("/{user_id}")
@log_to_file()
def addIncome(user_id: str, income: Income):
    """
        Add a new income.

        Args:
            user_id (str): The unique identifier of the user.
            income (Income): An Income object representing the details of the income to be added.

        Returns:
            dict: A dictionary containing the created income ID if successful, or an error message if failed.
    """
    try:
        user_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid user id")
    try:
        income.user_id = str(user_id)
        income.date = str(date.today())
        newIncome = create_income(income)
        if newIncome:
            return {"income id": str(newIncome)}
        else:
            return "income created failed"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"cannot crater income{str(e)}")


@incomeRouter.put("/{income_id}")
@log_to_file()
def updateIncome(income_id: str, income: Income):
    """
        Update an existing income.

        Args:
            income_id (str): The unique identifier of the income.
            income (Income): An Income object representing the updated details of the income.

        Returns:
            dict: A dictionary containing a success message if the update was successful.
    """
    try:
        incomeId = ObjectId(income_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid income id")
    try:
        old_income = get_income_by_id(incomeId)
        income.user_id = old_income.user_id
        income.date = old_income.date
        update_income(incomeId, income)
        return {"message": "income updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to update this income")


@incomeRouter.delete("/{income_id}")
@log_to_file()
def deleteIncome(income_id: str):
    """
       Delete an income.

       Args:
           income_id (str): The unique identifier of the income to be deleted.

       Returns:
           dict: A dictionary containing a success message if the deletion was successful.
    """
    try:
        incomeId = ObjectId(income_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid income id")
    try:
        delete_income(incomeId)
        return {"message": "income deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to delete this income")


@incomeRouter.get("/{income_id}")
@log_to_file()
def getIncomeById(income_id: str):
    """
       Retrieve an income by its ID.

       Args:
           income_id (str): The unique identifier of the income to be retrieved.

       Returns:
           Income: An Income object representing the retrieved income.
    """
    try:
        incomeId = ObjectId(income_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid income id")
    return get_income_by_id(incomeId)


@incomeRouter.get("/{user_id}")
@log_to_file()
def getIncomesByUserId(user_id: str):
    """
       Retrieve incomes by user ID.

       Args:
           user_id (str): The unique identifier of the user whose incomes are to be retrieved.

       Returns:
           list: A list of incomes associated with the provided user ID.
    """
    try:
        return get_incomes_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to load this incomes")
