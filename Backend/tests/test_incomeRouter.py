from fastapi import HTTPException

from BalanceUp.Backend.app.models.incomeModel import Income
from BalanceUp.Backend.app.routers.incomeRouter import addIncome, updateIncome, deleteIncome, getIncomeById, \
    getIncomesByUserId


def testAddIncome():
    income = Income(amount=50, source="gift", description="gift for birthday", date='29-05-2024',
                    user_id="664ef396319b8c6690e4f211")
    result = addIncome("664ef396319b8c6690e4f211", income)
    assert "income id" in result


def testUpdateIncome():
    income = Income(amount=50, source="gift", description="gift for birthday", date='2024-05-29',
                    user_id="664ef396319b8c6690e4f211")
    result = updateIncome("665775f9c3fc8a2f270195ce", income)
    assert result == {"message": "income updated successfully"}


def testGetIncomeById():
    income = Income(amount=50, source="gift", description="gift for birthday", date='2024-05-29',
                    user_id="664ef396319b8c6690e4f211")
    result = getIncomeById("665775f9c3fc8a2f270195ce")
    assert result == income


def testGetIncomesByUserId():

    user_id = "664ef396319b8c6690e4f211"
    try:
        result = getIncomesByUserId(user_id)

        assert result is not None
    except HTTPException as e:

        assert False, f"HTTPException raised with status code {e.status_code}: {e.detail}"
    except Exception as e:

        assert False, f"Unexpected exception: {e}"

    invalid_user_id = "invalid_user_id"
    try:
        getIncomesByUserId(invalid_user_id)
    except HTTPException as e:
        assert e.status_code == 400
        assert e.detail == "failed to load this incomes"
    except Exception as e:
        assert False, f"Unexpected exception: {e}"

