from fastapi import APIRouter

from .health import health
from .order import order

router = APIRouter()

router.include_router(health, tags=["Health"])
router.include_router(order, tags=["Order"])