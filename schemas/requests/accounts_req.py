from pydantic import BaseModel, EmailStr


class AccountRegisterReq(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email       : str | None = None

class AccountLoginReq(BaseModel):
    email       : str
    password    : str
