from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schema.userroleassign import UserRoleAssign,UserRoleResponse
from crud.assigne_role_to_users import assigne_role_for_user

router = APIRouter()
#api for assine role to the user
@router.post("/", response_model=UserRoleResponse)
def assign_role(data: UserRoleAssign, db: Session = Depends(get_db)):
    #call the assigne role for user for for assine role
    response = assigne_role_for_user(db, user_id=data.user_id, role_id=data.role_id)
    if response is None:  
        raise HTTPException(status_code=500, detail="Failed to assign role")
    return response


