from models import Price
from schemas.price_schemas import PriceOutputSchema, PriceInputSchema
from sqlalchemy.orm import Session


def create_price(db: Session, price: PriceInputSchema) -> PriceOutputSchema:
    new_price = Price(**price.dict())
    db.add(new_price)
    db.commit()
    db.refresh(new_price)
    return PriceOutputSchema.from_orm(new_price)
