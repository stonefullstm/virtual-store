from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.models.account import Account
from app.schemas.accounts import AccountPublic, AccountList, AccountSchema
from app.backend.db import get_session

router = APIRouter(prefix='/accounts')


@router.get('/', response_model=AccountList, tags=['accounts'])
def read_accounts(
    session: Session = Depends(get_session)
):
    accounts = session.exec(select(Account)).all()
    return {'accounts': accounts}


@router.post('/',
             response_model=AccountPublic,
             status_code=201, tags=['accounts'])
def create_account(
    account: AccountSchema,
    session: Session = Depends(get_session)
):
    session.add(account)
    session.commit()
    session.refresh(account)
    return account
