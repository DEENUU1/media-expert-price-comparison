from models import Price
from fastapi import HTTPException
from sqlalchemy import select, insert
from schemas.price_schemas import PriceOutputSchema, PriceInputSchema
from sqlalchemy.orm import Session
from typing import List


def create_price(db: Session, price: PriceInputSchema) -> PriceOutputSchema:
    new_price = Price(**price.dict())
    db.add(new_price)
    db.commit()
    db.refresh(new_price)
    return PriceOutputSchema.from_orm(new_price)
