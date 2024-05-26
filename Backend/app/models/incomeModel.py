import datetime

from bson import ObjectId
from pydantic import BaseModel
from datetime import date


class Income(BaseModel):
    amount: float
    source: str
    description: str
    date: str
    user_id: str
