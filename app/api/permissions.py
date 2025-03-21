from fastapi import FastAPI, APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
from crud.permissions import create_permission
from schema.permissions import PermissionBase,Permission
from typing import List

router = APIRouter()


@router.post("/")
def create_permission_api(permission: PermissionBase, db: Session = Depends(get_db)):
    # call create permission function
    db_permission = create_permission(db, permission.name)
    return db_permission

