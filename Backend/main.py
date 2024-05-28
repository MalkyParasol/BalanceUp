from fastapi import FastAPI
import uvicorn
from BalanceUp.Backend.app.routers.incomeRouter import incomeRouter
from BalanceUp.Backend.app.routers.expenseRouter import expenseRouter
from BalanceUp.Backend.app.routers.visualRouter import visualRouter
from app.routers.userRouter import userRouter

app = FastAPI()

app.include_router(userRouter, prefix='/user')
app.include_router(incomeRouter, prefix="/incomes")
app.include_router(expenseRouter, prefix="/expenses")
app.include_router(visualRouter,  prefix="/visual")


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
