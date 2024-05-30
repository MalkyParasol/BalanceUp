from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    """
      Model representing a user.

      Attributes:
          name (str): The username of the user.
          password (str): The password of the user.
          email (Optional[str]): The email address of the user (optional).
          phone (Optional[str]): The phone number of the user (optional).
      """
    name: str
    password: str
    email: Optional[str]
    phone: Optional[str]


