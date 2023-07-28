from sqlmodel import SQLModel, Field
# from pydantic import EmailStr


class Account(SQLModel, table=True):

    id: str = Field(primary_key=True, max_length=14)
    name: str = Field(max_length=100)
    email: str = Field(max_length=100, unique=True)
    password: str = Field(max_length=10)
    status: bool = Field(default=True)
