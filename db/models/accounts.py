from db.base_class import Base
from sqlalchemy import Column, Integer, String


class AccountModel(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(50))
    password = Column(String(256))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<Account(id={self.id}, name='{self.name}', email='{self.email}')>"
