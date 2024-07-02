from . import Base, Price
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    shop_id: Mapped[int] = mapped_column(index=True)
    name: Mapped[str] = mapped_column(index=True)
    category: Mapped[str] = mapped_column(index=True)
    model: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(nullable=True)
    url: Mapped[str] = mapped_column(index=True, unique=True)
    prices: Mapped[List[Price]] = relationship("Price", backref="product", cascade="all, delete-orphan")
