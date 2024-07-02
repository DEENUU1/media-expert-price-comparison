from schemas.price_schemas import PriceOutputSchema, PriceInputSchema
from pydantic import BaseModel
from typing import List, Optional


class ProductInputSchema(BaseModel):
    shop_id: int
    name: str
    category: str
    model: str
    description: Optional[str] = None
    prices: Optional[List[PriceInputSchema]] = None
    url: str


class ProductOutputSchema(BaseModel):
    id: int
    shop_id: int
    name: str
    category: str
    model: str
    description: Optional[str] = None
    prices: Optional[List[PriceOutputSchema]] = None
    url: str

    class Config:
        orm_mode = True
        from_attributes = True
