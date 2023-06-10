from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from auth.hash_password import HashPassword

from database.connection import get_db
from models.models import Staff
from models.users import UserGreate, TokenResponse
from datetime import datetime
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token

from models.models import Staff


user_router = APIRouter(
    tags=["User"]
)

hash_password = HashPassword()

@user_router.post("/signup")
async def sing_new_user(user: UserGreate, db: Session=Depends(get_db)) -> dict:
    new_user = Staff(
        last_name=user.last_name,
        first_name=user.first_name,
        email=user.email,
        password=hash_password.create_hash(user.password),
        salary_increase=datetime.utcnow()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {

        "new_user": new_user

    }


@user_router.get("/{id}")
async def get_one_user(id: int, db: Session=Depends(get_db)) -> dict:
    user = db.query(Staff).filter(Staff.id==id).first()  

    return {
        "message": user
    }


@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)) -> dict:
    user_exist = db.query(Staff).filter(Staff.email==user.username).first()
    
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }