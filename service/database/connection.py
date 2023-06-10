from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings
from typing import Optional



SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

class Settings(BaseSettings):
    SECRET_KEY: Optional[str] = "default"


    class Config:
        env_file = ".env"