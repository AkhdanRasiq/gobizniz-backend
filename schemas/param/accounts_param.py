from pydantic import BaseModel
from sqlalchemy.orm import Session


class GetAccountLoginParam(BaseModel):
    db: Session
    email: str

    class Config:
        arbitrary_types_allowed = True
