from pydantic import BaseModel
from pydantic import EmailStr


class AccountSchema(BaseModel):
    id: str
    name: str
    email: EmailStr
    password: str
    status: bool


class AccountPublic(BaseModel):
    id: str
    name: str
    email: EmailStr
    status: bool


class AccountList(BaseModel):
    accounts: list[AccountPublic]
