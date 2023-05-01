from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from core.config import settings


accessTokenExpire   = timedelta(hours=settings.JWT_ACCESS_TOKEN_EXPIRE_HOURS)
oauth2Scheme        = OAuth2PasswordBearer(tokenUrl="token")


def createAccessToken(data: dict):
    dataEncode = data.copy()

    dataEncode.update({"exp": datetime.utcnow() + accessTokenExpire})
    return jwt.encode(dataEncode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decodeToken(token: str):
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM], options={'verify_exp': False})


def isAuthenticated(token: str):
    isTokenExpired(token)
    # tokenData = decodeToken(token)

    # userData = securityUserRepository.repository.user.getUserById(db, tokenData['id'])
    # if userData == None:
    #     raise HTTPException(
    #         status.HTTP_404_NOT_FOUND,
    #         "User with id: {} is not found".format(token['id'])
    #     )
    # return userData


def isTokenExpired(token: str):
    tokenData   = decodeToken(token)
    dtNow       = int(datetime.timestamp(datetime.now()))
    
    if tokenData['exp'] < dtNow:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token Expired"
        )
