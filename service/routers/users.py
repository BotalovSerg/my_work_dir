from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.models import Staff
from models.users import UserGreate, UserBase
from datetime import datetime


user_router = APIRouter(
    tags=["User"]
)

@user_router.post("/signup")
async def sing_new_user(user: UserGreate, db: Session=Depends(get_db)) -> dict:
    new_user = Staff(
        last_name=user.last_name,
        first_name=user.first_name,
        email=user.email,
        password=user.password,
        salary_increase=datetime.utcnow()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {

        "new_user": new_user

    }


@user_router.get("/{id}")
async def get_all_users(id: int, db: Session=Depends(get_db)) -> dict:
    user = db.query(Staff).filter(Staff.id==id).first()  

    return {
        "message": user
    }