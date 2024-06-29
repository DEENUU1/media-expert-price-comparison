from pydantic import BaseModel

from typing import Optional


class PriceInputSchema(BaseModel):
    price: Optional[float] = None
    date: str
    product_id: Optional[int] = None


class PriceOutputSchema(PriceInputSchema):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True
