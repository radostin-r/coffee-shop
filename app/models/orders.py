from sqlalchemy import Column, Integer, String, Date, Time, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base_class import Base
from app.models import Customers, SalesOutles, Products, Staff


class Orders(Base):
    __tablename__ = "orders"

    transaction_id = Column(Integer, primary_key=True, index=True)
    transaction_date = Column(Date)
    transaction_time = Column(Time)

    # foreign keys
    sales_outlet_id = Column(Integer, ForeignKey("sales_outlets.sales_outlet_id"))
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))

    instore_yn = Column(String(5))
    order = Column(Integer)
    line_item_id = Column(Integer)
    quantity = Column(Integer)
    line_item_amount = Column(Float)
    unit_price = Column(Float)
    promo_item_yn = Column(String(5))

    # relationships
    sales_outlet = relationship(SalesOutles, back_populates="orders")
    customer = relationship(Customers, back_populates="orders")
    staff = relationship(Staff, back_populates="orders")
    product = relationship(Products, back_populates="orders")
