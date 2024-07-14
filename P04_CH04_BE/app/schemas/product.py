from pydantic import BaseModel, HttpUrl, field_validator
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[HttpUrl] = None

    @field_validator('image_url')
    def convert_url_to_str(cls, v):
        return str(v)


class ProductCreate(ProductBase):
    category_id: int

class ProductUpdate(ProductBase):
    category_id: Optional[int] = None

class ProductInDBBase(ProductBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True

class Product(ProductInDBBase):
    pass

class ProductInDB(ProductInDBBase):
    pass
