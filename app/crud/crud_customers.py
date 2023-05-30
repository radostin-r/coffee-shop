import datetime

from sqlalchemy import extract, func, select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Orders
from app.models.customers import Customers
from app.schemas import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customers, CustomerCreate, CustomerUpdate]):
    def get_customers_with_birthday(self, db: Session):
        today = datetime.date.today()
        return db.query(self.model).filter(
            extract('month', self.model.birthdate) == today.month,
            extract('day', self.model.birthdate) == today.day
        ).all()

    def get_customers_with_last_order_date(self, db: Session):
        subquery = select(
            Orders.customer_id,
            func.max(Orders.transaction_date).label('last_order_date')
        ).group_by(Orders.customer_id).subquery()

        return db.query(self.model.customer_id, self.model.customer_email, subquery.c.last_order_date). \
            join(subquery, self.model.customer_id == subquery.c.customer_id).all()


customer = CRUDCustomer(Customers)
