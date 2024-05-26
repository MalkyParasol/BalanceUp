from fastapi import FastAPI
import uvicorn
from BalanceUp.Backend.app.routers.incomeRouter import incomeRouter
from BalanceUp.Backend.app.routers.expenseRouter import expenseRouter
from app.routers.userRouter import userRouter

app = FastAPI()

app.include_router(userRouter, prefix='/user')
app.include_router(incomeRouter, prefix="/incomes")
app.include_router(expenseRouter, prefix="/expenses")

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
