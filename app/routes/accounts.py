from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from app.models.account import Account
from app.schemas.accounts import AccountPublic, AccountList, AccountSchema
from app.backend.db import get_session


error_response = {
                400: {
                    "description": "Validation Error.",
                    "content": {
                        "application/json": {
                            "example": {
                                "message": "Validation error on /name/ field"}
                            }
                    },
                },
             }

router = APIRouter(prefix='/accounts')


@router.get(
        '/',
        summary='Returns all accounts.',
        response_model=AccountList,
        tags=['Accounts'])
def read_accounts(
    session: Session = Depends(get_session)
):
    accounts = session.exec(select(Account)).all()
    return {'accounts': accounts}


@router.post('/',
             summary='Create an account.',
             response_model=AccountPublic,
             status_code=201,
             responses=error_response,
             tags=['Accounts'])
def create_account(
    account: AccountSchema,
    session: Session = Depends(get_session)
):
    session.add(account)
    session.commit()
    session.refresh(account)
    return account


@router.get('/{id}',
            response_model=AccountPublic,
            tags=["Accounts"])
def get_account_by_id(
    id: str,
    session: Session = Depends(get_session)
):
    try:
        result = session.exec(select(Account).where(Account.id == id)).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Account not found")
    return result
