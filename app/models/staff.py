from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True, index=True)

    orders = relationship("Orders", back_populates="staff")
