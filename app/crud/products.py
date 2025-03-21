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


#product create 
def create_product(db: Session, product_data: ProductCreate,current_user:UserResponse):
    new_product = Product(
        name=product_data.name,
        description=product_data.description,
        user_id=current_user.id
        
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

from sqlalchemy.orm import Session
from fastapi import HTTPException

def update_product(db: Session, product_data: ProductUpdate, current_user: UserResponse, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # if product.user_id != current_user.id:
    #     raise HTTPException(status_code=403, detail="Permission denied")
    product.name = product_data.name
    product.description = product_data.description
    product.user_id = current_user.id  # Ensure ownership consistency

    db.commit()
    db.refresh(product)
    
    return product

  

def update_some_data(db: Session, updated_data: ProductUpdate, current_user: UserResponse, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    update_data = updated_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(product, key, value)   #setattr() is a built-in function that lets you assign new values to attributes of an object. It's useful when you need to dynamically modify attributes at runtime, or when you don't know attribute names in advance

    db.commit()
    db.refresh(product)

    return product



# def get_product(db: Session, product_id: int):
    
#     return db.query(Product).filter(Product.id == product_id).first()

# def get_all_products(db: Session, skip: int = 0, limit: int = 10):

#     return db.query(Product).offset(skip).limit(limit).all()

# def update_product(db: Session, product_id: int, product_data: ProductUpdate):

#     product = db.query(Product).filter(Product.id == product_id).first()
#     if not product:
#         return None

#     for key, value in product_data.dict(exclude_unset=True).items():
#         setattr(product, key, value)

#     db.commit()
#     db.refresh(product)
#     return product

# def delete_product(db: Session, product_id: int):
    
#     product = db.query(Product).filter(Product.id == product_id).first()
#     if not product:
#         return None

#     db.delete(product)
#     db.commit()
#     return product
