from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class SalesOutles(Base):
    __tablename__ = "sales_outlets"

    sales_outlet_id = Column(Integer, primary_key=True, index=True)

    orders = relationship("Orders", back_populates="sales_outlet")
