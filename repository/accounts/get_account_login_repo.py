from db.base import AccountModel
from schemas.entity import accounts_entity
from schemas.param import accounts_param


def getAccountLogin(param: accounts_param.GetAccountLoginParam):
    user: accounts_entity = param.db.query(AccountModel).filter(
        AccountModel.email == param.email
        ).first()

    return user
