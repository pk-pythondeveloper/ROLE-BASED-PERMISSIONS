from pydantic import BaseModel
from typing import List
from models.models import Role
from . permissions import PermissionBase

# Schema for Role
class CreateRole(BaseModel):
    name: str
    permission_ids: list[int]


class RoleResponse(BaseModel):
    id: int
    name: str
    permission_ids: List[int] 

    class Config:
        from_attributes = True  

