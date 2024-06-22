from fastapi import Request, APIRouter, Depends, Form, UploadFile, BackgroundTasks
from fastapi.responses import HTMLResponse
from starlette import status
from repository.source_repository import SourceRepository
from config.settings import settings

router = APIRouter(
    prefix="",
    tags=["Sources"],
)


@router.get("/", response_class=HTMLResponse)
def get_source_list(request: Request):
    sources = SourceRepository().get_sources()

    return settings.TEMPLATES.TemplateResponse(
        request=request,
        name="sources.html",
        context={
            "sources": sources,
        }
    )
