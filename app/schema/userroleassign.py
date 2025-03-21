from pydantic import BaseModel
from typing import List
from models.models import Role
from . permissions import PermissionBase


class UserRoleAssign(BaseModel):
    user_id: int
    role_id: int

    class Config:
        from_attributes = True  # Ensures ORM compatibility

class UserRoleResponse(BaseModel):
    user_id: int
    role_id: int

    class Config:
        orm_mode = True

# Schema for assigning a permission to a role
class RolePermissionAssign(BaseModel):
    role_id: int
    permission_id: int

    class Config:
        from_attributes = True