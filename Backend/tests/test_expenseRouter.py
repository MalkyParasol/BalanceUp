"""
test_expenseRouter.py

This module contains unit tests for the expense router endpoints.

"""
from bson import ObjectId

from BalanceUp.Backend.app.db_management.expense_CRUD import get_expense_by_id
from BalanceUp.Backend.app.models.expenseModel import Expense
from BalanceUp.Backend.app.routers.expenseRouter import createExpense, updateExpense, deleteExpense, getExpenseByUserId


def test_createExpense():
    """
       Test case for the createExpense endpoint.

       It tests whether a new expense can be successfully created.

    """
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
    """
        Test case for the updateExpense endpoint.

        It tests whether an existing expense can be successfully updated.

    """
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
    """
        Test case for the deleteExpense endpoint.

        It tests whether an existing expense can be successfully deleted.

    """
    result = deleteExpense("6653881c5e65102e58ecde4a")
    assert result == {"message": "expense deleted successfully"}


def test_getExpenseByUserId():
    """
      Test case for the getExpenseByUserId endpoint.

      It tests whether expenses for a specific user can be successfully retrieved.

    """
    result = getExpenseByUserId("664ef396319b8c6690e4f211")
    assert result != []
    assert result is not None


def test_getExpenseById():
    """
       Test case for the get_expense_by_id function.

       It tests whether an expense can be successfully retrieved by its ID.

    """
    result = get_expense_by_id(ObjectId("6654d44923df0863dad94383"))
    assert result is not None

