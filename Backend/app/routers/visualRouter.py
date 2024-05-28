from fastapi import FastAPI, Depends, APIRouter, HTTPException
import matplotlib.pyplot as plt
import numpy as np
from BalanceUp.Backend.app.db_management.expense_CRUD import get_monthly_expense, get_yearly_expense, get_daily_expense
from BalanceUp.Backend.app.db_management.income_CRUD import get_monthly_income, get_yearly_income, get_daily_income

visualRouter = APIRouter()


# @visualRouter.get("year/{user_id}")
# def geyYearlyVisual(user_id: str):


@visualRouter.get("month/{user_id}")
def getMonthlyVisual(user_id: str):
    incomes = get_monthly_income(user_id)
    expense = get_monthly_expense(user_id)
    days = range(0, 31)
    plt.plot(days, incomes, '-g', label="incomes")
    plt.plot(days, expense, '-r', label="expense")
    plt.scatter(days, incomes, c='green', s=31)
    plt.scatter(days, expense, c='red', s=31)
    plt.title("monthly incomes and expenses")
    plt.xlabel("days")
    plt.ylabel("amount")
    plt.legend()
    return plt.show()


@visualRouter.get("year/line/{user_id}")
def getMonthlyVisual(user_id: str):
    incomes = get_yearly_income(user_id)
    expense = get_yearly_expense(user_id)
    month = range(0, 12)
    plt.plot(month, incomes, '-g', label="incomes")
    plt.plot(month, expense, '-r', label="expense")
    plt.scatter(month, incomes, c='green', s=12)
    plt.scatter(month, expense, c='red', s=12)
    plt.title("monthly incomes and expenses")
    plt.xlabel("days")
    plt.ylabel("amount")
    plt.legend()
    return plt.show()

@visualRouter.get("day/{user_id}/{day}")
def getMonthlyVisual(user_id: str,day:int):
    incomes = get_daily_income(user_id,day)
    expense = get_daily_expense(user_id,day)
    myLabels = ["incomes", "expenses"]
    myValues = [incomes,expense]
    myExplode = [0.2, 0]
    plt.pie(myValues, labels=myLabels, explode=myExplode, shadow=True)
    plt.legend()
    return plt.show()

@visualRouter.get("year/{user_id}")
def getMonthlyVisual(user_id: str):
    incomes = get_yearly_income(user_id)
    expense = get_yearly_expense(user_id)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    bar_width = 0.35
    index = np.arange(len(months))

    # Plotting the income and expenses graph
    plt.figure(figsize=(10, 5))
    plt.bar(index, incomes, bar_width, color='green', label='Income')
    plt.bar(index + bar_width, expense, bar_width, color='red', label='Expenses')

    plt.title('Income and Expenses by Month')
    plt.xlabel('Months')
    plt.ylabel('Amounts')
    plt.xticks(index + bar_width / 2, months)
    plt.legend()

    plt.tight_layout()


    return plt.show()

# @visualRouter.get("month/{user_id")
# def getMonthlyVisual(user_id: str):
