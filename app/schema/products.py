from pydantic import BaseModel
from typing import Optional

from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProductCreate(ProductBase):  # Inherit from ProductBase
    pass  

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models
