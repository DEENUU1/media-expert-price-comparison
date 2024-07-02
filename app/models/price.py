from sqlalchemy import ForeignKey

from . import Base
from sqlalchemy.orm import Mapped, mapped_column


class Price(Base):
    __tablename__ = "prices"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    price: Mapped[float] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
