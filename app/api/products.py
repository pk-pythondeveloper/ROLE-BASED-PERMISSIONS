from fastapi import APIRouter, Depends, HTTPException,status,Request
from sqlalchemy.orm import Session
from database import get_db
from schema.products import ProductCreate, ProductUpdate,ProductResponse
from crud.products import create_product,update_product,update_some_data
from dependencies.auth import get_current_user
from models.models import User,Product
from core.permissions import check_permission

router = APIRouter()
@router.post("/", response_model=ProductResponse)

@check_permission('allka') 
async def create_product(
    request: Request, 
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    print(user)

    new_product = Product(
        name=product_data.name,
        description=product_data.description,
        user_id=user.id
    )

    print(new_product, "------------------- Product created -------------------")

    db.add(new_product)
    db.commit()
    db.refresh(new_product)  
    return new_product  


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)):
    # check_permission("delete", user) 
    product = db.query(Product).filter(Product.id == product_id, Product.user_id == user.id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found or unauthorized")
    db.delete(product)
    print("----------------delete ho gaya re------")
    db.commit()
    return {"message": "Product deleted successfully"}

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    # check_permission("Read", user) 
    products=db.query(Product).all()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found or unauthorized")
    return products

@router.put("/{product_id}", response_model=ProductResponse)
def update_product_details(product_id: int,product_data: ProductUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)):
    # check_permission("put", user) 
    updated_data = update_product(db, product_data, user, product_id) 
    return updated_data

@router.patch("/{product_id}", response_model=ProductResponse)
def update_partially(product_id: int,updated_datas: ProductUpdate,db: Session = Depends(get_db),user: User = Depends(get_current_user)):
    check_permission("update", user) 
    updated_data = update_some_data(db, updated_datas, user, product_id)  
    return updated_data


