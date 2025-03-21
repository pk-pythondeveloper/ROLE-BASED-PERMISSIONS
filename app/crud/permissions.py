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



#create permission
def create_permission(db: Session, name: str):
    db_permission = Permission(name=name)
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission
# get permissions
def get_permission(db: Session, permission_id: int):
    return db.query(Permission).filter(Permission.id == permission_id).first()
#geting all permissions
def get_permissions(db: Session):
    return db.query(Permission).all()
#update permissions
def update_permission(db: Session, permission_id: int, new_name: str):
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if db_permission:
        db_permission.name = new_name
        db.commit()
        db.refresh(db_permission)
        return db_permission
    return None
#delete permissions
def delete_permission(db: Session, permission_id: int):
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if db_permission:
        db.delete(db_permission)
        db.commit()
        return True
    return False