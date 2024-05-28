from datetime import date

from bson import ObjectId
from fastapi import FastAPI, Depends, APIRouter, HTTPException

from BalanceUp.Backend.app.db_management.expense_CRUD import create_expense, get_expense_by_id, update_expense, \
    delete_expense, get_expenses_by_user_id
from BalanceUp.Backend.app.models.expenseModel import Expense

expenseRouter = APIRouter()


@expenseRouter.post("/{user_id}")
def createExpense(user_id: str, expense: Expense):
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
def updateExpense(expense_id: str, expense: Expense):
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
def deleteExpense(expense_id: str):
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
def getExpenseByUserId(user_id: str):
    try:
        return get_expenses_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to load this expenses")


@expenseRouter.get("/{expense_id}")
def getIncomeById(expense_id: str):
    try:
        expenseId = ObjectId(expense_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid expense id")
    return get_expense_by_id(expenseId)
