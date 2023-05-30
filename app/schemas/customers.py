import datetime

from pydantic import BaseModel


class CustomerBase(BaseModel):
    customer_first_name: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass


class Customer(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True


class CustomerLastOrder(BaseModel):
    customer_id: int
    customer_email: str
    last_order_date: datetime.date
