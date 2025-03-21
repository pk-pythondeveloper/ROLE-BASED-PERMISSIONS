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



from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def assigne_role_for_user(db: Session, user_id: int, role_id: int):
    
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")

    existing_user_role = db.query(UserRole).filter(
        UserRole.user_id == user_id,
        UserRole.role_id == role_id
    ).first()

    if existing_user_role:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already has this role")

    # Assign role to user
    new_user_role = UserRole(user_id=user_id, role_id=role_id)
    db.add(new_user_role)
    db.commit()
    db.refresh(new_user_role)

    return {"message": "Role assigned successfully"}
