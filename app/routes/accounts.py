from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.models.account import Account
from app.schemas.accounts import AccountList
from app.backend.db import get_session

router = APIRouter(prefix='/accounts')


@router.get('/', response_model=AccountList)
def read_accounts(
    session: Session = Depends(get_session)
):
    accounts = session.exec(select(Account)).all()
    return {'accounts': accounts}
