import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api import dependencies
from app.crud import crud_products

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/top-selling-products/{year}")
def get_top_selling_products(year: int, db: Session = Depends(dependencies.get_db)) -> dict:
    """
    Get customers that have a birthday today

    :param year: int the year we want
    :param db: db Session
    :return: dict with products list
    """
    products = crud_products.product.get_top_selling_products_by_year(db, year)
    if not products:
        logger.info('Failed to fetch top selling products')
        raise HTTPException(status_code=404, detail=f"No products found for year={year}")
    products = [schemas.ProductWithSales(product=prod[0].product, total_sales=prod[1]) for prod in products]
    logger.info('SUCCESS fetch top selling products')
    return {"products": products}
