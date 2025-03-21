from fastapi import HTTPException, Depends,Request
from sqlalchemy.orm import Session
from models.models import User, Role, Permission
from database import get_db
from dependencies.auth import get_current_user  
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.models import User, Permission
from database import get_db
from dependencies.auth import get_current_user  # Assumes you have a function to get the logged-in user
from functools import wraps
#manually we are cheking permission 
# def check_permission(required_permission: str, user: User = Depends(get_current_user)):
#     # Extract permissions from the user's roles
#     user_permissions = {perm.name for role in user.roles for perm in role.permissions}

#     if required_permission not in user_permissions:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Permission denied",
#         )

#     return True  # User has permission
# danmicall cheked permission
# def check_permission(resource: str):
#     async def permission_checker(request: Request, user: User = Depends(get_current_user)):
#         method_to_permission = {
#             "POST": "post",
#             "GET": "get",
#             "PUT": "put",
#             "PATCH": "patch",
#             "DELETE": "delete",
#         } 
#         action = method_to_permission.get(request.method)
#         if not action:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Unsupported HTTP method for permissions"
#             )
#         required_permission = f"{action}"

#         # Extract user permissions from roles
#         user_permissions = {perm.name for role in user.roles for perm in role.permissions}

#         # Debugging: Print the user's permissions
#         print(f"User Permissions: {user_permissions}","------------------")
#         print(f"Required Permission: {required_permission}","-----------")

#         if required_permission not in user_permissions:
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail="Permission denied",
#             )

#     return permission_checker

from functools import wraps
from fastapi import Request, HTTPException, Depends, status
from typing import Callable
# Ensure correct import

def check_permission(resource: str):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(
            request: Request,
            *args,
            db=Depends(get_db), 
            user: User = Depends(get_current_user), 
            **kwargs
        ):
            method_to_permission = {
                "POST": "post",
                "GET": "get",
                "PUT": "put",
                "PATCH": "patch",
                "DELETE": "delete",
            }
            action = method_to_permission.get(request.method)
            if not action:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Unsupported HTTP method for permissions"
                )
            required_permission = f"{action}"

            # Extract user permissions from roles
            user_permissions = {perm.name for role in user.roles for perm in role.permissions}

            # Debugging: Print the user's permissions
            print(f"User Permissions: {user_permissions}","------------------")
            print(f"Required Permission: {required_permission}","-----------")

            if required_permission not in user_permissions:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Permission denied",
                )

        
            return await func(request, *args, db=db, user=user, **kwargs)

        return wrapper
    return decorator


#what is wraps
#ans:-When you create a decorator, it wraps around a function. Without @wraps, the function's metadata (like __name__, __doc__, etc.) gets replaced by the decorator’s metadata.
  # If the user has permission, proceed

# def has_permission(user: User, permission_name: str) -> bool:
#     for role in user.roles:
#         print(role,"-------------role aaya--------")
#         for permission in role.permissions:  
#             if permission.name == permission_name:
                
#                 return True

#     return False


# def check_permission(permission_name: str):
#     print(permission_name,"ther eaaoiijoafoaf")
#     # breakpoint()
#     def permission_dependency(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#         if not has_permission(current_user, permission_name, db):
#             print(current_user,"------------------this is my current user------")
#             raise HTTPException(status_code=403, detail="Permission denied")
#         print(current_user)
#         return current_user
#     return permission_dependency
