from sqlmodel import SQLModel, Field
# from typing import Optional
from datetime import date


class Transaction(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    value: float = Field(gt=0)
    cashback: float = Field(ge=0)
    transaction_date: date = Field(default=date.today())
    account_id: str = Field(default=None, foreign_key='account.id')
