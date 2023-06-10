from pydantic import BaseModel


class UserBase(BaseModel):    
    last_name: str
    first_name: str
    email: str

    
    
class UserGreate(UserBase):
    password: str

    class Config:
        schema_extra = {
            "example" : {
                "last_name": "Last ame",
                "first_name": "First name",
                "email": "mail@mail.com",
                "password": "password"
            }
        }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str