from pydantic import BaseModel, EmailStr


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
