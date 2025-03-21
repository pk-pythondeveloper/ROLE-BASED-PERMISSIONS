from sqlalchemy.orm import Session
from models.models import User, Role, Permission,UserRole,RolePermission
from typing import List
from sqlalchemy.orm import Session
from schema.roles import CreateRole
from schema.users import UserCreate,UserResponse
from schema.userroleassign import UserRoleAssign, RolePermissionAssign
from fastapi import HTTPException,Depends
from schema.userroleassign import UserRoleAssign, UserRoleResponse  
from schema.rolepermissionassign import RolePermissionRequest
from database import get_db
from sqlalchemy.orm import Session
from models.models import Role, RolePermission,User,Permission,UserRole,Product
from schema.products import ProductCreate,ProductUpdate
from utils.security import  get_password_hash
from dependencies.auth import get_current_user
from fastapi import HTTPException,status

def assigne_permissions_for_roles(db: Session, role_id: int, permission_ids: list[int]):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        return {"error": "Role not found"}
    permissions = db.query(Permission).filter(Permission.id.in_(permission_ids)).all()
    if not permissions:
        return {"error": "No valid permissions found"}
    role_permissions = [RolePermission(role_id=role_id, permission_id=perm.id) for perm in permissions]
    db.add_all(role_permissions)
    db.commit()
    return {"message": "Permissions assigned successfully"}











