from datetime import date
from pydantic import BaseModel
from typing import Optional


class Price(BaseModel):
    price: Optional[float] = None
    date: date

    def dict(self, **kwargs) -> dict:
        data = super().dict(**kwargs)
        data['date'] = self.date.isoformat()
        return data
