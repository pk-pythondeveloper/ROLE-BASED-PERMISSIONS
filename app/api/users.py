from fastapi import APIRouter, Depends, HTTPException

from schema.users import UserCreate,UserResponse
from database import SessionLocal
from models.models import User
from crud.users import create_user
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter()



#api for creating user
@router.post("/", response_model=UserResponse)
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    #call function to create user
    db_user = create_user(db, user)
    # Handle duplicate user
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already registered")

    return {
        "id": db_user.id,
        "username": db_user.username,
        "email": db_user.email,
        "role_ids": [role.id for role in db_user.roles]
    }

# # Get user by ID
# @router.get("/users/{user_id}", response_model=schemas.UserResponse)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(crud.User).filter(crud.User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# # Update user information
# @router.put("/users/{user_id}", response_model=schemas.UserResponse)
# def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
#     user = db.query(crud.User).filter(crud.User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     # Call the CRUD function to update the user
#     updated_user = crud.update_user(db, user_id, user_update)
#     return updated_user
