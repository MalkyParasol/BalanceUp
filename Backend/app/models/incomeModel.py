from pydantic import BaseModel


class Income(BaseModel):
    """
       Model representing an income.

       Attributes:
           amount (float): The amount of the income.
           source (str): Source of the income.
           description (str): Description of the income.
           date (str): Date of the income in the format 'YYYY-MM-DD'.
           user_id (str): The unique identifier of the user associated with the income.
       """
    amount: float
    source: str
    description: str
    date: str
    user_id: str
