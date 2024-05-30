from pydantic import BaseModel
from enum import Enum
from typing import Union


class ExpenseCategory(str, Enum):
    Housing = "Housing"
    Utilities = "Utilities"
    Transportation = "Transportation"
    Food = "Food"
    Insurance = "Insurance"
    Debt = "Debt"
    Payments = "Payments"
    Entertainment = "Entertainment"
    Healthcare = "Healthcare"
    Education = "Education"
    Personal = "Personal"
    Care = "Care"
    Clothing = "Clothing"
    Savings = "Savings"
    Investments = "Investments"
    Gifts = "Gifts"
    Travel = "Travel"
    Childcare = "Childcare"
    Pets = "Pets"
    Taxes = "Taxes"
    Home = "Home"
    Maintenance = "Maintenance"
    Technology = "Technology"
    income = "income"
    expense = "expense"


class Expense(BaseModel):
    """
        Model representing an expense.

        Attributes:
            amount (float): The amount of the expense.
            description (str): Description of the expense.
            date (str): Date of the expense in the format 'YYYY-MM-DD'.
            user_id (str): The unique identifier of the user associated with the expense.
            category (Union[ExpenseCategory, str]): The category of the expense, chosen from ExpenseCategory enum.
        """
    amount: float
    description: str
    date: str
    user_id: str
    category: Union[ExpenseCategory, str]
