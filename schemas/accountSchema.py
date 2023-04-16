from pydantic import BaseModel


class Account(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
