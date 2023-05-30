from pydantic import BaseModel


class ProductBase(BaseModel):
    product: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True


class ProductWithSales(ProductBase):
    total_sales: int
