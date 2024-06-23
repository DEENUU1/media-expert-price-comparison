from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from config.settings import settings
from repository.product_repository import get_product_list


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

