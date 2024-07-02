from fastapi import Request, APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from fastapi.responses import HTMLResponse
from config.settings import settings
from repository.product_repository import get_products, get_product_by_id
from services.product_price_stats import get_max_product_price, get_avg_product_price, get_min_product_price


router = APIRouter(
    prefix="",
    tags=["Products"],
)


@router.get("/", response_class=HTMLResponse)
def get_products_list_handler(request: Request, db: Session = Depends(get_db)):
    products = get_products(db)

    context = {
        "request": request,
        "products": products,
    }

    return settings.TEMPLATES.TemplateResponse(
        name="products.html",
        context=context
    )


@router.get("/{product_id}", response_class=HTMLResponse)
def get_product_details_handler(request: Request, product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)

    price_json = [price.model_dump() for price in product.prices] if product.prices else []

    context = {
        "request": request,
        "product": product,
        "price_json": price_json,
        "min_price": get_min_product_price(product),
        "max_price": get_max_product_price(product),
        "avg_price": get_avg_product_price(product)
    }

    return settings.TEMPLATES.TemplateResponse(
        name="product_details.html",
        context=context
    )
