from pydantic import BaseModel


class AccountSchema(BaseModel):
    id: str
    name: str
    email: str
    password: str
    status: bool


class AccountPublic(BaseModel):
    id: str
    name: str
    email: str
    status: bool


class AccountList(BaseModel):
    accounts: list[AccountPublic]
