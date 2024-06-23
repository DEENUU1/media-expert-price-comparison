from fastapi import Request, APIRouter, Form, HTTPException
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
