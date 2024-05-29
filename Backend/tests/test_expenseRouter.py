from bson import ObjectId

from BalanceUp.Backend.app.db_management.expense_CRUD import get_expense_by_id
from BalanceUp.Backend.app.models.expenseModel import Expense
from BalanceUp.Backend.app.routers.expenseRouter import createExpense, updateExpense, deleteExpense, getExpenseByUserId


def test_createExpense():
    expense = Expense(
        amount=0,
        description="chips",
        date="string",
        user_id="664ef396319b8c6690e4f211",
        category="Food"
    )
    result = createExpense("664ef396319b8c6690e4f211", expense)
    assert "expense id" in result


def test_updateExpense():
    expense = Expense(
        amount=15,
        description="chips",
        date="2024-05-07",
        user_id="664ef396319b8c6690e4f211",
        category="Food"
    )
    result = updateExpense("6653881c5e65102e58ecde4a", expense)
    assert result == {"message": "expense updated successfully"}


def test_deleteExpense():
    result = deleteExpense("6653881c5e65102e58ecde4a")
    assert result == {"message": "expense deleted successfully"}


def test_getExpenseByUserId():
    result = getExpenseByUserId("664ef396319b8c6690e4f211")
    assert result != []
    assert result is not None


def test_getExpenseById():
    result = get_expense_by_id(ObjectId("6654d44923df0863dad94383"))
    assert result is not None

