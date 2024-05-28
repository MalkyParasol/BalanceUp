from bson import ObjectId
from fastapi import FastAPI, Depends, APIRouter, HTTPException
from datetime import date
from BalanceUp.Backend.app.db_management.income_CRUD import create_income, update_income, get_income_by_id, \
    delete_income, get_incomes_by_user_id
from BalanceUp.Backend.app.models.incomeModel import Income

incomeRouter = APIRouter()


@incomeRouter.post("/{user_id}")
def addIncome(user_id: str, income: Income):
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
def updateIncome(income_id: str, income: Income):
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
def deleteIncome(income_id: str):
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
def getIncomeById(income_id: str):
    try:
        incomeId = ObjectId(income_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid income id")
    return get_income_by_id(incomeId)


@incomeRouter.get("/{user_id}")
def getIncomesByUserId(user_id: str):
    try:
        return get_incomes_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to load this incomes")
