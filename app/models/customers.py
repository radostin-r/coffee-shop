from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    home_store = Column(Integer)
    customer_first_name = Column(String(50), index=True)
    customer_email = Column(String, unique=True, index=True)
    customer_since = Column(Date)
    loyalty_card_number = Column(String(50))
    birthdate = Column(Date)
    gender = Column(String(5))
    birth_year = Column(Integer)

    orders = relationship("Orders", back_populates="customer")
