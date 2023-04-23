from fastapi import Depends, APIRouter
from db.session import SessionLocal, get_db
from sqlalchemy.orm import Session
from schemas import accountSchema
from db.base import AccountModel
# from db.models.accounts import AccountModel


route = APIRouter()

@route.get("/all", response_model=list[accountSchema.Account])
def get_users(db: Session = Depends(get_db)):
    db = SessionLocal()
    accounts = db.query(AccountModel).all()
    return accounts

@route.post("/", response_model=accountSchema.Account)
def create_new_account(req:accountSchema.AccountRegister, db:Session = Depends(get_db)):
    account = AccountModel(
        name=req.name,
        email=req.email
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account
