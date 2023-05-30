import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api import dependencies
from app.crud import crud_customers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/birthday")
def get_customers_with_birthday(db: Session = Depends(dependencies.get_db)) -> dict:
    """
    Get customers that have a birthday today
    :param db: sqlalchemy Session
    :return: dict
    """
    logger.info("Fetch customers with birthday today")
    customers = crud_customers.customer.get_customers_with_birthday(db)
    customers = [schemas.Customer.from_orm(customer) for customer in customers]
    return {"customers": customers}


@router.get("/last-order-per-customer")
def get_last_order_for_customer(db: Session = Depends(dependencies.get_db)) -> dict:
    """
    Get last order date for all customers
    :param db: sqlalchemy Session
    :return: dict
    """
    customers = crud_customers.customer.get_customers_with_last_order_date(db)
    if not customers:
        logger.info("FAILED to fetch customers with last order date")
        raise HTTPException(status_code=404, detail="No customers found.")
    customers = [
        schemas.CustomerLastOrder(customer_id=customer[0], customer_email=customer[1], last_order_date=customer[2]) for
        customer in customers]
    logger.info("SUCCESS fetch customers with last order date")
    return {"customers": customers}
