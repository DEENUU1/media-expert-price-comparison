from pydantic import BaseModel, Field
from typing import Optional, List
from models.price import Price


class Product(BaseModel):
    shop_id: int
    name: str
    category: str
    description: Optional[str] = None
    model: Optional[str] = None
    prices: List[Price] = Field(default_factory=list)

    def dict(self, **kwargs):
        data = super().dict(**kwargs)
        data['prices'] = [price.dict(**kwargs) for price in self.prices]
        return data
