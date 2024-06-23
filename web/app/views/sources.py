from fastapi import Request, APIRouter, Form, Response
from fastapi.responses import HTMLResponse
from config.settings import settings
from models.source import SourceInput
from repository.source_repository import create_source, get_sources, delete_source

router = APIRouter(
    prefix="/source",
    tags=["Sources"],
)


@router.get("/", response_class=HTMLResponse)
async def get_source_list_handler(request: Request):
    sources = await get_sources()
    return settings.TEMPLATES.TemplateResponse(
        name="sources.html",
        context={
            "request": request,
            "sources": sources,
        }
    )


@router.post("/", response_class=HTMLResponse)
async def create_source_handler(request: Request, url: str = Form(...)):
    source = await create_source(SourceInput(url=url))
    return settings.TEMPLATES.TemplateResponse(
        name="source.html",
        context={
            "request": request,
            "source": source,
        }
    )


@router.delete("/{source_id}", response_class=Response)
async def delete_source_handler(source_id: str):
    await delete_source(source_id)
    return
