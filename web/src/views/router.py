from fastapi import APIRouter
from . import sources


router = APIRouter(
    prefix=""
)

router.include_router(sources.router)
