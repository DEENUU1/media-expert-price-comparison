from . import Base
from sqlalchemy.orm import Mapped, mapped_column


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    url: Mapped[str] = mapped_column(index=True, unique=True)
