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


def create_user(db: Session, user: UserCreate):
    #check perivious user
    existing_user = db.query(User).filter((User.email == user.email) | (User.username == user.username) ).first()
    if existing_user:
        return None  
    # if there is no user related to this email crating new user 
    db_user = User(username=user.username, email=user.email, password=get_password_hash(user.password))
    if user.role_ids:
        roles = db.query(Role).filter(Role.id.in_(user.role_ids)).all()
        db_user.roles.extend(roles)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user