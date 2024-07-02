from models import Source
from fastapi import HTTPException
from sqlalchemy import select
from schemas.source_schemas import SourceInputSchema, SourceOutputSchema
from sqlalchemy.orm import Session
from typing import List


def create_source(db: Session, source: SourceInputSchema) -> SourceOutputSchema:
    source = Source(**source.dict())
    db.add(source)
    db.commit()
    db.refresh(source)
    return SourceOutputSchema.from_orm(source)


def get_sources(db: Session) -> List[SourceOutputSchema]:
    sources = db.execute(select(Source))
    return [SourceOutputSchema.from_orm(source) for source in sources.scalars()]


def delete_source(db: Session, source_id: int):
    source = db.get(Source, source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    db.delete(source)
    db.commit()
