from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import settings

if settings.DEBUG:
    SQLALCHEMY_DATABASE_URL = settings.SQLITE_DATABASE_URL
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
else:
    SQLALCHEMY_DATABASE_URL = settings.POSTGRE_DATABASE_URL
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    """
    Create a database session.

    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
