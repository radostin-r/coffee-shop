from fastapi import APIRouter

from app.api.routers import customers, products

router = APIRouter()
router.include_router(customers.router, prefix="/customers", tags=["customers"])
router.include_router(products.router, prefix="/products", tags=["products"])
