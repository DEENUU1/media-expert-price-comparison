from fastapi import Request, APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from fastapi.responses import HTMLResponse
from config.settings import settings
from repository.product_repository import get_products, get_product_by_id

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

    context = {
        "request": request,
        "product": product,
    }

    return settings.TEMPLATES.TemplateResponse(
        name="product_details.html",
        context=context
    )
