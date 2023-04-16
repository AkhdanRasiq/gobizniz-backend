from fastapi import Depends, APIRouter
from connections.dbSql import SessionLocal
from sqlalchemy.orm import Session
from schemas import accountSchema
from models import AccountModel


app = APIRouter(prefix="/user")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example route
@app.get("/all", response_model=list[accountSchema.Account])
def get_users(db: Session = Depends(get_db)):
    db = SessionLocal()
    accounts = db.query(AccountModel).all()
    return accounts
