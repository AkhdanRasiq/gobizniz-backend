from fastapi import HTTPException, status
from schemas.requests import accounts_req
from schemas.responses import accounts_resp
from schemas.param import accounts_param
from sqlalchemy.orm import Session
from repository.accounts import get_account_login_repo
from core.hashing import verifyPassword
from core import security

def getAccountLogin(req: accounts_req.AccountLoginReq, db: Session) -> accounts_resp.AccountTokenResp:
    account = get_account_login_repo.getAccountLogin(accounts_param.GetAccountLoginParam(
        db=db,
        email=req.email
    ))
    
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not verifyPassword(req.password, account.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")
    
    resp = security.createAccessToken(dict(accounts_resp.AccountTokenResp(
        id=account.id,
        email=account.email
    )))

    return resp
