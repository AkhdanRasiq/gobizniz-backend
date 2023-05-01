from pydantic import BaseModel, EmailStr


class AccountLoginResp(BaseModel):
    accessToken : str
    tokenType   : str

class AccountTokenResp(BaseModel):
    id      : int
    email   : str

class AccountResp(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
