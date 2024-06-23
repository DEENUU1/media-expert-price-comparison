from fastapi import Request, APIRouter, Form, Response
from fastapi.responses import HTMLResponse
from config.settings import settings
from models.source import SourceInput
from repository.source_repository import SourceRepository

router = APIRouter(
    prefix="/source",
    tags=["Sources"],
)


@router.get("/", response_class=HTMLResponse)
def get_source_list(request: Request):
    sources = SourceRepository().get_sources()
    return settings.TEMPLATES.TemplateResponse(
        name="sources.html",
        context={
            "request": request,
            "sources": sources,
        }
    )


@router.post("/", response_class=HTMLResponse)
def create_source(request: Request, url: str = Form(...)):
    source = SourceRepository().create_source(SourceInput(url=url))
    return settings.TEMPLATES.TemplateResponse(
        name="source.html",
        context={
            "request": request,
            "source": source,
        }
    )


@router.delete("/{source_id}", response_class=Response)
def delete_source(source_id: str):
    SourceRepository().delete_source(source_id)
