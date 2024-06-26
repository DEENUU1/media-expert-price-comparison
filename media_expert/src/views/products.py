from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from config.settings import settings
from repository.product_repository import get_product_list, get_product


router = APIRouter(
    prefix="",
    tags=["Products"],
)


@router.get("/", response_class=HTMLResponse)
async def get_products_list_handler(request: Request):
    products = await get_product_list()
    return settings.TEMPLATES.TemplateResponse(
        name="products.html",
        context={
            "request": request,
            "products": products,
        }
    )


@router.get("/{product_id}", response_class=HTMLResponse)
async def get_product_details_handler(request: Request, product_id: str):
    product = await get_product(product_id)
    return settings.TEMPLATES.TemplateResponse(
        name="product_details.html",
        context={
            "request": request,
            "product": product,
        }
    )