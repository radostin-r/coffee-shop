from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.orders import Orders
from app.models.products import Products
from app.schemas.products import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Products, ProductCreate, ProductUpdate]):

    def get_top_selling_products_by_year(self, db: Session, year: int):
        """
        Get all products that have orders for a given year. Return a list of top 10 products order by quantity sold.

        :param db: Sqlalchemy Session
        :param year: The year we want
        :return: List of tuples with Product obj and total_quantity
        """
        subquery = db.query(Orders.product_id, func.sum(Orders.quantity).label('total_quantity')). \
            filter(func.extract('year', Orders.transaction_date) == year). \
            group_by(Orders.product_id). \
            subquery()

        return db.query(self.model, subquery.c.total_quantity). \
            join(subquery, self.model.product_id == subquery.c.product_id). \
            order_by(desc(subquery.c.total_quantity)). \
            limit(10). \
            all()


product = CRUDProduct(Products)
