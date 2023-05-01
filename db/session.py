from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator


if settings.RDBMS == "mysql":
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.DB_CONFIG_URL}"
if settings.RDBMS == "postgresql":
    SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_CONFIG_URL}"

engine          = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal    = sessionmaker(autocommit=False, autoflush=False, bind=engine)
conn            = engine.connect()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
