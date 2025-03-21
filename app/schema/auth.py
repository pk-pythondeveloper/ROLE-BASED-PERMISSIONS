from typing import Optional
from models.models import RefreshToken  
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from schema.users import UserResponse
from pydantic import BaseModel, EmailStr
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    email: str
    password: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr



class UserInDB(BaseModel):
    email:str
    password: str

