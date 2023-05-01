import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME    : str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION : str = os.getenv("PROJECT_VERSION")

    RDBMS           : str = os.getenv("RDBMS")
    DB_USER         : str = os.getenv("DB_USER")
    DB_PASSWORD     : str = os.getenv("DB_PASSWORD")
    DB_HOST         : str = os.getenv("DB_HOST", "localhost")
    DB_PORT         : str = os.getenv("DB_PORT")
    DB_DATABASE     : str = os.getenv("DB_DATABASE")
    DB_CONFIG_URL   : str = f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

    IS_PRODUCTION   : str = os.getenv("IS_PRODUCTION", "false")

    JWT_SECRET_KEY                  : str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM                   : str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRE_HOURS   : int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_HOURS", 24))


settings = Settings()
