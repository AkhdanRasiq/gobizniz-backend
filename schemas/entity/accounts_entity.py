from pydantic import BaseModel


class AccountEntity(BaseModel):
    id          : int
    name        : str
    email       : str
    password    : str

    class Config:
        orm_mode =  True
