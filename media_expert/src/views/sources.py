from fastapi import Request, APIRouter, Form, Response, Depends
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

from config.database import get_db
from config.settings import settings
from schemas.source_schemas import SourceOutputSchema, SourceInputSchema
from repository.source_repository import create_source, get_sources, delete_source


router = APIRouter(
    prefix="/source",
    tags=["Sources"],
)


@router.get("", response_class=HTMLResponse)
def get_source_list_handle(request: Request, db: Session = Depends(get_db)):
    sources = get_sources(db)
    return settings.TEMPLATES.TemplateResponse(
        name="sources.html",
        context={
            "request": request,
            "sources": sources,
        }
    )


@router.delete("/{source_id}", response_class=Response)
def delete_source_handler(source_id: int, db: Session = Depends(get_db)):
    delete_source(db, source_id)
    return


@router.post("", response_class=HTMLResponse)
def create_source_handler(request: Request, url: str = Form(...), db: Session = Depends(get_db)):
    source = create_source(db, SourceInputSchema(url=url))

    context = {
        "request": request,
        "source": source,
    }

    return settings.TEMPLATES.TemplateResponse(
        name="source.html",
        context=context
    )

