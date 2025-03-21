from pydantic import BaseModel, EmailStr
from typing import List, Optional

from .permissions import PermissionBase


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str  
    role_ids: Optional[List[int]] = []  
    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role_ids: List[int]  

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    roles: Optional[List[int]] = []

    class Config:
        orm_mode = True
