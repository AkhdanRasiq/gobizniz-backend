from pydantic import BaseModel, EmailStr


class Account(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

class AccountRegister(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
