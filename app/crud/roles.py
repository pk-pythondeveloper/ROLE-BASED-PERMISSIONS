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



def create_role(db: Session, role: CreateRole, role_name: str):

    permission_ids = role.permission_ids  
    print(permission_ids,"----------that is my permission id----------")
    #cheking permission is existing or not 
    existing_permissions = db.query(Permission.id).filter(Permission.id.in_(permission_ids)).all()
    existing_permission_ids = {perm.id for perm in existing_permissions}  # Convert to set
    if not all(pid in existing_permission_ids for pid in permission_ids):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid permission ID(s) provided")

    #role allready register or not
    existing_role = db.query(Role).filter(Role.name == role_name).first()
    if existing_role:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role is already registered")
    db_role = Role(name=role_name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)

    # Assign permissions to the role
    role_permissions = [RolePermission(role_id=db_role.id, permission_id=pid) for pid in permission_ids]
    db.add_all(role_permissions)
    db.commit()

    return db_role