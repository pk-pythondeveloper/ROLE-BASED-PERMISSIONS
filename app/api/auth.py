from datetime import timedelta,datetime
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import User
from schema.auth import Token,Login
from utils.security import verify_password, get_password_hash
from utils.utils import ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db
from dependencies.auth import authenticate_user,get_current_user,create_access_token


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")


router =APIRouter ()
@router.post("/login/", response_model=Token)
def login_for_access_token(login: Login, db: Session = Depends(get_db)):
    user = authenticate_user(db, login.email, login.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "You have access!", "user": current_user.email}
