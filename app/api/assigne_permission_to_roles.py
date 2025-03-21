from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schema.rolepermissionassign import  RolePermissionRequest
from crud.assigne_permission_to_roles import assigne_permissions_for_roles


router = APIRouter()
#api assine role
@router.post("/")
def assigne_role_permissions(request: RolePermissionRequest, db: Session = Depends(get_db)):
    #assigne_permission function
    return assigne_permissions_for_roles(db, request.role_id, request.permission_ids)