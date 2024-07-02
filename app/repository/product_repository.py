from models import Product, Price
from fastapi import HTTPException
from sqlalchemy import select
from schemas.product_schemas import ProductInputSchema, ProductOutputSchema
from sqlalchemy.orm import Session
from typing import List


def create_product(db: Session, product: ProductInputSchema) -> ProductOutputSchema:
    price_objects = [Price(**price.dict()) for price in product.prices] if product.prices else []

    new_product = Product(
        shop_id=product.shop_id,
        name=product.name,
        category=product.category,
        model=product.model,
        description=product.description,
        url=product.url,
        prices=price_objects
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return ProductOutputSchema.from_orm(new_product)


def get_products(db: Session) -> List[ProductOutputSchema]:
    products = db.execute(select(Product))
    return [ProductOutputSchema.from_orm(product) for product in products.scalars()]


def get_product_by_id(db: Session, product_id: int) -> ProductOutputSchema:
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductOutputSchema.from_orm(product)


def product_exists_by_shop_id(db: Session, shop_id: int) -> bool:
    return db.scalar(select(Product).where(Product.shop_id == shop_id))


def get_product_by_shop_id(db: Session, shop_id: int) -> ProductOutputSchema:
    product = db.scalar(select(Product).where(Product.shop_id == shop_id))
    return ProductOutputSchema.from_orm(product)
