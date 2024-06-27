from fastapi import APIRouter
from . import sources, products


router = APIRouter(
    prefix=""
)

router.include_router(sources.router)
router.include_router(products.router)