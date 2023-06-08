from pydantic import BaseModel


class UserBase(BaseModel):    
    last_name: str
    first_name: str
    email: str
    
    

class UserGreate(UserBase):
    hashed_password:str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    salary: float
    salary_increase: str

    class Config:
        orm_mode = True

class UserLoginForm(BaseModel):
    email: str
    password: str