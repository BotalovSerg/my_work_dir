from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from auth.hash_password import HashPassword

from database.connection import get_db
from models.models import Staff
from models.users import UserGreate, TokenResponse, UserBase
from datetime import datetime
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token, verify_acces_token

from models.models import Staff
from auth.authenticate import authenticate


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


@user_router.get("/")
async def get_all_user(db: Session=Depends(get_db)) -> dict:
    users = db.query(Staff).all()
    res = []  
    for user in users:
        res.append({
            "last_name": user.last_name,
            "first_name": user.first_name,
            "email": user.email})
    return {
        "message": res
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
    

@user_router.post("/salary")
async def user_salary(id:int, token: str=Depends(authenticate), db: Session=Depends(get_db)) -> dict:
    user = db.query(Staff).filter(Staff.id==id).first()
    if user.email == token:
        print(token)
        return {
            "message": user
        }   
    
    return {
        "message": "Token not user"
    }