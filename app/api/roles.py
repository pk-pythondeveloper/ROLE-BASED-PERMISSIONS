from fastapi import FastAPI, APIRouter,Depends,HTTPException
from database import get_db
from schema.roles import CreateRole,RoleResponse
from crud.roles import create_role
from sqlalchemy.orm import Session

router = APIRouter()




@router.post("/", response_model=RoleResponse)
def create_role_api(role: CreateRole, db: Session = Depends(get_db)):
    #call function for creating role
    db_role = create_role(db, role, role_name=role.name)  
    if db_role is None:
        raise HTTPException(status_code=400, detail="Role already registered")
    return RoleResponse(
        id=db_role.id,
        name=db_role.name,
        permission_ids=[]  

    )

    

