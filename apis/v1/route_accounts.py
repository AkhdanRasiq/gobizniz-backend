from fastapi import Depends, APIRouter, HTTPException, status
from db.session import SessionLocal, get_db
from sqlalchemy.orm import Session
from schemas.requests import accounts_req
from schemas.responses import accounts_resp
from db.base import AccountModel
from core import hashing

from services.v1.accounts import get_account_login_service


route = APIRouter()

@route.get("/all", response_model=list[accounts_resp.AccountResp])
def get_users(db: Session = Depends(get_db)):
    db = SessionLocal()
    accounts = db.query(AccountModel).all()
    return accounts


@route.post("/", response_model=accounts_resp.AccountResp)
def create_new_account(req:accounts_req.AccountRegisterReq, db:Session = Depends(get_db)):
    account = AccountModel(
        name=req.name,
        email=req.email,
        password=hashing.hashPassword(req.password)
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


@route.post("/login", response_model=accounts_resp.AccountLoginResp)
async def account_login(req: accounts_req.AccountLoginReq, db: Session = Depends(get_db)):
    resp = get_account_login_service.getAccountLogin(req, db)

    return accounts_resp.AccountLoginResp(accessToken=resp, tokenType="bearer")

