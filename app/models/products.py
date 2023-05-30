from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_group = Column(String)
    product_category = Column(String)
    product_type = Column(String)
    product = Column(String)
    product_description = Column(String)

    orders = relationship("Orders", back_populates="product")
