import hashlib

from sqlalchemy.orm import Session
from .models import Staff
from .forms import UserGreate
from .utils import get_password_hash



def get_user_by_email(db: Session, email: str):
    return db.query(Staff).filter(Staff.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 50):
    return db.query(Staff).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserGreate):
    new_user = Staff(
        last_name=user.last_name,
        first_name=user.first_name,
        email=user.email,
        hashed_password=get_password_hash(user.hashed_password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user