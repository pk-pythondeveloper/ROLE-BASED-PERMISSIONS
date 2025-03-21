from pydantic import BaseModel
from typing import List
from models.models import Permission

# Schema for Permission
class PermissionBase(BaseModel):
    name: str

class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True




